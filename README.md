# IOTAssignement3

This Repository consists of:
- **Sensor Nodes**: Simulate environmental data (temperature, humidity, CO₂)
- **MQTT Broker**: Handles real-time data transmission
- **Monitoring Client**: Subscribes and displays sensor data
- **ThingSpeak Cloud**: Stores and visualizes historical data

IoT Environmental Monitoring System Requirements
**Python 3.x
MQTT
ThingSpeak**

📝 Overview
A comprehensive IoT solution for monitoring environmental conditions in real-time, featuring:

MQTT-based sensor data transmission

ThingSpeak cloud integration for data storage

Multi-node support with wildcard subscriptions

Real-time visualization of sensor metrics

🖥️ System Components
1. Sensor Node Simulator (virtual_station.py)
Generates simulated environmental data (temperature, humidity, CO₂)

Publishes to MQTT broker every 30 seconds

Simultaneously sends data to ThingSpeak cloud

2. Data Monitor (data_monitor.py)
Subscribes to MQTT topics using wildcards

Displays real-time sensor readings in console

Handles multiple sensor nodes simultaneously

3. Cloud Dashboard
ThingSpeak for historical data visualization

Web-based interface for remote monitoring

## 🏗 Architecture
    A[Sensor Node] -->|MQTT Publish| B[Broker]
    B -->|MQTT Subscribe| C[Monitor]
    A -->|HTTP POST| D[ThingSpeak]
    C --> E[Console Display]
    D --> F[Web Dashboard]

✨ Features
Real-time sensor data monitoring

Multiple node support with wildcard subscriptions

Secure MQTT communication

Cloud data storage and visualization

Error handling and connection recovery

JSON formatted data payloads

Timestamped readings

💻 Installation
Prerequisites
Python 3.8+

pip package manager


Data Flow
Sensor node generates simulated readings every 30 seconds

Data is published to MQTT broker and sent to ThingSpeak

Monitor client subscribes to broker and displays real-time data

ThingSpeak stores data for visualization and analysis

**Troubleshooting:**

ThingSpeak Field Mapping
Temperature → field1
(Numeric values in °C)

Humidity → field2
(Numeric values in % RH)

CO₂ Level → field3
(Numeric values in ppm)

**Key Notes:**
Case-Sensitive: Fields must be lowercase (field1, not Field1)

**Data Limits:**

Max 8 fields per channel

Field values support integers and floats

Visualization:
Each field automatically generates a separate graph in ThingSpeak

API Reference:
Update via URL:
https://api.thingspeak.com/update?api_key=YOUR_KEY&field1=TEMP&field2=HUMIDITY&field3=CO2

**Parameters:**
Sensor Parameter	ThingSpeak Field	Data Type	Units	Example Value
Temperature	        field1	            float	    °C	    23.5
Humidity	        field2	            float	    % RH	45.7
CO₂ Level	        field3	            integer	    ppm	    650

api_key (required) which should be taken from ThingsSpeak

field1 (temperature)

field2 (humidity)

field3 (CO₂)
