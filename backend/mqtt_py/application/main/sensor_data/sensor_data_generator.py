import random
from time import sleep
def simulate_sensor_data():
        data = {
            "temperatura": round(random.uniform(20.0, 40.0), 2),
            "data": "2025-03-03",
            "hora": "12:00:00"
        }
        print(f"Generated sensor data: {data}")

        return data