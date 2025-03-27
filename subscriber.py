import paho.mqtt.client as mqtt
import json

# ===== MQTT CONFIGURATION =====
# Network communication settings
MQTT_SERVER = "mqtt.eclipseprojects.io"  # Public test broker
NODE_ID_PATTERN = "sensor_node_*"        # Wildcard for all devices
DATA_TOPIC = f"iot_network/{NODE_ID_PATTERN}/readings"

# ===== CONNECTION HANDLERS =====
def handle_connection(client, userdata, flags, rc, properties=None):
    """Callback for MQTT connection events"""
    if rc == mqtt.MQTT_ERR_SUCCESS:
        print("Established connection with message broker")
        # Subscribe using proper wildcard syntax
        client.subscribe("iot_network/+/readings")  # + matches single level
    else:
        print(f"Connection failed with error code: {rc}")

def process_incoming_message(client, userdata, message):
    """Handles incoming sensor data messages"""
    try:
        sensor_data = json.loads(message.payload.decode())
        
        print("\n=== SENSOR READING RECEIVED ===")
        device_id = message.topic.split('/')[1]
        print(f"Device: {device_id}")
        print(f"Temperature: {sensor_data['temperature']}°C")
        print(f"Humidity: {sensor_data['humidity']}%")
        print(f"CO₂ Concentration: {sensor_data['co2']}ppm")
        print(f"Measurement Time: {sensor_data['timestamp']}")
    except Exception as error:
        print(f"Message processing error: {str(error)}")

# ===== CLIENT SETUP =====
# Initialize MQTT client with version 2 protocol
mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqtt_client.on_connect = handle_connection
mqtt_client.on_message = process_incoming_message

# ===== MAIN EXECUTION =====
try:
    print("Initializing MQTT listener...")
    mqtt_client.connect(MQTT_SERVER, 1883, 60)
    print("Monitoring for sensor data transmissions...")
    mqtt_client.loop_forever()
except KeyboardInterrupt:
    print("\nTerminating listener connection...")
    mqtt_client.disconnect()
except Exception as error:
    print(f"Network error occurred: {str(error)}")