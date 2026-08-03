import json
import random
import time
from datetime import datetime, timezone

SENSOR_ID = "sensor-01"
INTERVAL_SECONDS = 5


def generate_reading() -> dict:
    return {
        "sensor_id": SENSOR_ID,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "temperature_c": round(random.uniform(18.0, 30.0), 2),
        "humidity_pct": round(random.uniform(30.0, 70.0), 2),
        "pressure_hpa": round(random.uniform(990.0, 1025.0), 2),
    }


def main():
    print(f"Generating sensor data every {INTERVAL_SECONDS}s. Press Ctrl+C to stop.")
    try:
        while True:
            reading = generate_reading()
            print(json.dumps(reading))
            time.sleep(INTERVAL_SECONDS)
    except KeyboardInterrupt:
        print("\nStopped.")


if __name__ == "__main__":
    main()
