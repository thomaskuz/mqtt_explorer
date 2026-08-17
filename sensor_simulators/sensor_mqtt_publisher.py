import random
import time
from datetime import datetime, timezone
from pydantic import BaseModel
import paho.mqtt.client as mqtt

SENSOR_ID = "sensor-01"
INTERVAL_SECONDS = 5
MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "sensors/sensor-01/reading"

# Define a Pydantic model for the sensor reading, Pydantic is used for data validation and serialization

class SensorReading(BaseModel):
    sensor_id: str
    timestamp: str
    temperature_c: float
    humidity_pct: float
    pressure_hpa: float

# Generate a random sensor reading

def generate_reading() -> dict:
    return {
        "sensor_id": SENSOR_ID,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "temperature_c": round(random.uniform(18.0, 30.0), 2),
        "humidity_pct": round(random.uniform(30.0, 70.0), 2),
        "pressure_hpa": round(random.uniform(990.0, 1025.0), 2),
    }

# These are the callback functions for MQTT events, they will be called when the client connects or disconnects from the broker

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✓ Connected to MQTT broker")
    else:
        print(f"✗ Connection failed with code {rc}")


def on_disconnect(client, userdata, rc):
    if rc != 0:
        print(f"✗ Unexpected disconnection: {rc}")



def main():
    print(f"Connecting to MQTT broker at {MQTT_BROKER}:{MQTT_PORT}...")

    client = mqtt.Client(client_id="sensor-publisher")
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect

    client.connect(MQTT_BROKER, MQTT_PORT, keepalive=60)

    print(f"Publishing sensor data every {INTERVAL_SECONDS}s. Press Ctrl+C to stop.\n")

    last_publish = time.time()

    try:
        while True:
            client.loop(timeout=0.1)

            if time.time() - last_publish >= INTERVAL_SECONDS:
                reading_dict = generate_reading()
                validated_reading = SensorReading(**reading_dict)
                payload = validated_reading.model_dump_json()
                client.publish(MQTT_TOPIC, payload, qos=1, retain=True)
                print(f"  → Published to {MQTT_TOPIC}")
                last_publish = time.time()

    except KeyboardInterrupt:
        print("\n✓ Stopping...")
    finally:
        client.disconnect()
        print("✓ Stopped.")


if __name__ == "__main__":
    main()