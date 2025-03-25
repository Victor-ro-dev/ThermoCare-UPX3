import paho.mqtt.client as mqtt
from application.configs.mqtt_configs import mqtt_broker_config
from application.main.mqtt_connection.callbacks import MqttCallbacks
import json


class MqttClientConnection:
    def __init__(self, broker_ip: str, broker_port: int, client_name: str, keep_alive: int, topic: str):
        self.__broker_ip = broker_ip
        self.__broker_port = broker_port
        self.__client_name = client_name
        self.__keep_alive = keep_alive
        self.__topic = topic
        self.__mqtt_client = None

    def start_connection(self):
        mqtt_client = mqtt.Client(self.__client_name)

        mqtt_client.on_connect = MqttCallbacks.on_connect
        mqtt_client.on_subscribe = MqttCallbacks.on_subscribe
        mqtt_client.on_message = MqttCallbacks.on_message  

        mqtt_client.connect(host=self.__broker_ip, port=self.__broker_port, keepalive=self.__keep_alive)
        self.__mqtt_client = mqtt_client
        self.__mqtt_client.loop_start()
        print("Connection started")

    def end_connection(self):
        try:
            self.__mqtt_client.loop_stop()
            self.__mqtt_client.disconnect()
            return True
        except Exception as e:
            print(f"Error ending connection: {e}")
    
    def publish_data(self, data: dict):
        result = self.__mqtt_client.publish(self.__topic, json.dumps(data))
        print(f"Publish result: {result}")
