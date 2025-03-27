import random
import time
import json
import paho.mqtt.client as mqtt
import requests
from datetime import datetime

# ===== APPLICATION CONFIGURATION =====
# Unique identifier for this sensor station
DEVICE_IDENTIFIER = "sensor_node_" + str(random.randint(1000, 9999))

# Cloud service connection parameters
MQTT_SERVER = "mqtt.eclipseprojects.io"  # Public MQTT test broker
DATA_CHANNEL = f"iot_network/{DEVICE_IDENTIFIER}/measurements"

# Cloud analytics platform credentials (UPDATE THESE)
TS_WRITE_KEY = "4IOM44YO9KI34A4U"  # ThingSpeak channel write authorization
TS_ENDPOINT = f"https://api.thingspeak.com/update?api_key={TS_WRITE_KEY}"

# ===== NETWORK CONNECTION HANDLER =====
def handle_broker_connection(client, userdata, flags, connection_code):
    """Callback for MQTT connection events"""
    print(f"Established broker connection (Status: {connection_code})")

# Initialize communication client
network_client = mqtt.Client()
network_client.on_connect = handle_broker_connection
network_client.connect(MQTT_SERVER, 1883, 60)

# ===== MEASUREMENT GENERATION =====
def simulate_environmental_data():
    """Creates randomized sensor readings with timestamp"""
    return {
        "temp": round(random.uniform(-50, 50), 2),      # Celsius
        "humidity": round(random.uniform(0, 100), 2),   # Percentage
        "co2_level": random.randint(300, 2000),         # PPM
        "reading_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

# ===== DATA TRANSMISSION =====
def upload_to_cloud(measurements):
    """Sends sensor data to cloud analytics platform"""
    transmission_params = {
        "field1": measurements["temp"],
        "field2": measurements["humidity"],
        "field3": measurements["co2_level"]
    }
    try:
        server_response = requests.get(TS_ENDPOINT, params=transmission_params)
        print(f"Cloud service response: HTTP {server_response.status_code}")
    except Exception as error:
        print(f"Transmission error: {str(error)}")

# ===== MAIN OPERATION CYCLE =====
def run_sensor_node():
    """Primary execution loop for sensor data collection and transmission"""
    try:
        while True:
            # Generate new environmental measurements
            current_measurements = simulate_environmental_data()
            
            # Transmit via MQTT protocol
            data_package = json.dumps(current_measurements)
            network_client.publish(DATA_CHANNEL, data_package)
            print(f"Transmitted data: {data_package}")
            
            # Upload to cloud service
            upload_to_cloud(current_measurements)
            
            # Measurement interval
            time.sleep(30)
            
    except KeyboardInterrupt:
        print("\nTerminating sensor node operation...")
        network_client.disconnect()

# ===== SYSTEM INITIALIZATION =====
if __name__ == "__main__":
    print(f"Initializing environmental sensor node: {DEVICE_IDENTIFIER}")
    network_client.loop_start()
    run_sensor_node()