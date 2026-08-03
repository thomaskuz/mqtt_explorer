# MQTT Explorer

An MQTT testing playground for experimenting with different MQTT brokers running in Docker containers.

## Project Goal

Build a modular testing environment to:
- Generate realistic sensor data at regular intervals
- Test publishing to different MQTT brokers (running in separate Docker containers)
- Compare broker behavior, performance, and reliability
- Start with sensor data generation; expand to include MQTT publishing and subscription logic

## Architecture

```
mqtt_explorer/
├── sensor_simulators/        # Sensor data generation
│   └── sensor_data_generator.py   # Generates temp/humidity/pressure readings every 5s
├── tests/                    # Learning and test files
│   └── datastruc.py         # Python dict learning example
├── .venv/                    # Python virtual environment
└── CLAUDE.md                 # This file
```

## Current Status

- ✅ Created `sensor_data_generator.py` — generates random sensor readings (temperature, humidity, pressure) as JSON every 5 seconds
- ⏳ Next: Add MQTT publishing; set up Docker broker containers

## Setup

### Prerequisites
- Python 3.12+
- Docker (for running MQTT brokers)
- Git

### Install & Run

1. Activate the virtual environment:
   ```bash
   source .venv/bin/activate
   ```

2. Run the sensor generator:
   ```bash
   python3 sensor_simulators/sensor_data_generator.py
   ```
   
   Output (one reading every 5s):
   ```json
   {"sensor_id": "sensor-01", "timestamp": "2026-08-03T12:00:00.123456+00:00", "temperature_c": 24.57, "humidity_pct": 45.3, "pressure_hpa": 1013.25}
   ```

## Key Files

- **`sensor_simulators/sensor_data_generator.py`** — Infinite loop that generates randomized sensor readings (temperature: 18–30°C, humidity: 30–70%, pressure: 990–1025 hPa) with ISO 8601 timestamps. Uses stdlib only (json, random, time, datetime).

## Dependencies

Currently only uses Python standard library. Future additions:
- `paho-mqtt` — for MQTT publishing/subscribing
- `docker-py` — for programmatic Docker container management (optional)

## Development Notes

- All sensor readings are printed as single-line JSON for easy piping/processing
- Timestamps are UTC to avoid timezone confusion
- Random values are within realistic ranges for atmospheric sensors
- Script exits cleanly on Ctrl+C

## Next Steps

1. Add MQTT publishing to the sensor generator
2. Create Docker Compose file with multiple MQTT brokers (Mosquitto, HiveMQ, etc.)
3. Build subscriber scripts to test message delivery/ordering
4. Add performance metrics and logging
