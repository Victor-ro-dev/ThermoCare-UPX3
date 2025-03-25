from application.main.mqtt_connection.mqtt_client_connection import MqttClientConnection
from application.configs.mqtt_configs import mqtt_broker_config
from time import sleep
from application.main.sensor_data.sensor_data_generator import simulate_sensor_data

mqtt_client = MqttClientConnection(
    broker_ip=mqtt_broker_config['HOST'],
    broker_port=mqtt_broker_config['PORT'],
    client_name=mqtt_broker_config['CLIENT_NAME'],
    keep_alive=mqtt_broker_config['KEEP_ALIVE'],
    topic=mqtt_broker_config['TOPIC']
)

def main():
    try:
        mqtt_client.start_connection()
        print("MQTT connection started")

        # ✅ Envio imediato antes do loop
        data = simulate_sensor_data()
        mqtt_client.publish_data(data)

        while True:
            data = simulate_sensor_data()
            mqtt_client.publish_data(data)
            sleep(30)

    except KeyboardInterrupt:
        mqtt_client.end_connection()
        print("Connection ended")

    while True:
        sleep(0.001)
