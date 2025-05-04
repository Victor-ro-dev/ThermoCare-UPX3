from application.configs.mqtt_configs import mqtt_broker_config
import json
from application.main.db.connection_db import dataBaseConnection

class MqttCallbacks:

    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
            client.subscribe(mqtt_broker_config['TOPIC']) 
            print(f"Subscribed to topic: {mqtt_broker_config['TOPIC']}")
        else:
            print(f"Failed to connect, return code {rc}")


    def on_subscribe(client, userdata, mid, granted_qos):
        print(f"Subscribed to topic! {mqtt_broker_config['TOPIC']}")
        print(f"QoS: {granted_qos}")


    def on_message(client, userdata, msg):
        data = json.loads(msg.payload.decode())
        dataBaseConnection.insert_sensor_data(data)

    def on_disconnect(client, userdata, rc):
        print("Disconnected from MQTT Broker!")
        print(f"Return Code: {rc}")
