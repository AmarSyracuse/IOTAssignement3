# IOTAssignement3

This Repository consists of:
- **Sensor Nodes**: Simulate environmental data (temperature, humidity, CO₂)
- **MQTT Broker**: Handles real-time data transmission
- **Monitoring Client**: Subscribes and displays sensor data
- **ThingSpeak Cloud**: Stores and visualizes historical data

## 🏗 Architecture


graph TD
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

Steps
Clone the repository:

bash
Copy
git clone https://github.com/yourusername/iot-sensor-monitor.git
cd iot-sensor-monitor
Install dependencies:

bash
Copy
pip install -r requirements.txt


Data Flow
Sensor node generates simulated readings every 30 seconds

Data is published to MQTT broker and sent to ThingSpeak

Monitor client subscribes to broker and displays real-time data

ThingSpeak stores data for visualization and analysis

🛠 Troubleshooting
Symptom	Possible Cause	Solution
No data received	Incorrect topic	Verify topic patterns match
Connection errors	Network issues	Check broker URL and connectivity
ThingSpeak failures	Invalid API key	Verify write key permissions
JSON decode errors	Malformed payload	Ensure consistent data format


ThingSpeak API
Endpoint: https://api.thingspeak.com/update

Parameters:

api_key (required)

field1 (temperature)

field2 (humidity)

field3 (CO₂)
