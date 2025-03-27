import requests
from datetime import datetime, timedelta

# ===== THINGSPEAK CONFIGURATION =====
# Replace these values with your actual ThingSpeak channel details
CHANNEL_ID = "2894468"                # Found in your channel URL
READ_API_KEY = "DP3S854124NCZAE2"     # Found in API Keys tab of your channel
# ====================================

def get_channel_feeds():
    # Fetches the most recent data entries from ThingSpeak channel
    url = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json"
    params = {
        "api_key": READ_API_KEY,
        "results": 10  # Number of most recent records to fetch
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        print(f"DEBUG: API Response - {response.status_code}")  # Debug line
        if response.status_code == 200:
            data = response.json()
            print(f"DEBUG: Raw API Response - {data}")  # Debug line
            return data.get('feeds', [])
        return None
    except Exception as e:
        print(f"Connection Error: {str(e)}")
        return None

def show_sensor_readings(feeds):
    # Displays the sensor data or troubleshooting instructions if no data found
    if not feeds:
        print("\nCRITICAL: No data found. Immediate checks needed:")
        print("1. Is virtual_station.py running and showing 'HTTP 200'?")
        print("2. Verify READ_API_KEY matches your channel's Read Key")
        print("3. Manually check: https://thingspeak.com/channels/2894396")
        print("4. Try this direct link:")
        print(f"   https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json?api_key={READ_API_KEY}&results=2")
        return
    
    print(f"\nSUCCESS: Found {len(feeds)} data points")
    for feed in feeds:
        print(f"\nTimestamp: {feed.get('created_at')}")
        print(f"Temperature: {feed.get('field1')}°C")
        print(f"Humidity: {feed.get('field2')}%")
        print(f"CO2: {feed.get('field3')}ppm")

if __name__ == "__main__":
    print("Fetching historical data from ThingSpeak...")
    data = get_channel_feeds()
    show_sensor_readings(data)