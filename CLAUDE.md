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
├── sensor_simulators/              # Sensor data generation
│   ├── sensor_data_generator.py    # CLI: generates readings every 5s (stdout)
│   └── sensor_rest_api.py          # REST API: exposes readings via HTTP
├── tests/                          # Learning and test files
│   └── datastruc.py                # Python dict learning example
├── .venv/                          # Python virtual environment
└── CLAUDE.md                        # This file
```

## Current Status

- ✅ Created `sensor_data_generator.py` — generates random sensor readings (temperature, humidity, pressure) as JSON every 5 seconds
- ✅ Created `sensor_rest_api.py` — FastAPI REST API that exposes sensor readings as JSON via HTTP
- ⏳ Next: Add MQTT publishing; set up Docker broker containers

## Setup

### Prerequisites
- Python 3.12+
- Docker (for running MQTT brokers)
- Git

### Install Dependencies

1. Activate the virtual environment:
   ```bash
   source .venv/bin/activate
   ```

2. Install packages:
   ```bash
   pip install fastapi uvicorn
   ```

### Run Sensor Generator (CLI)

```bash
python3 sensor_simulators/sensor_data_generator.py
```

Output (one reading every 5s):
```json
{"sensor_id": "sensor-01", "timestamp": "2026-08-03T12:00:00.123456+00:00", "temperature_c": 24.57, "humidity_pct": 45.3, "pressure_hpa": 1013.25}
```

Stop with **Ctrl+C**.

### Run Sensor REST API

```bash
python3 sensor_simulators/sensor_rest_api.py
```

The API runs on `http://localhost:5000`.

**Endpoints:**
- `GET /sensor` — returns a new sensor reading as JSON
- `GET /health` — health check (returns `{"status": "ok"}`)
- `GET /docs` — interactive API documentation (Swagger UI)

**Example:**
```bash
curl http://localhost:5000/sensor
```

Response:
```json
{"sensor_id": "sensor-01", "timestamp": "2026-08-03T12:34:56.789012+00:00", "temperature_c": 24.57, "humidity_pct": 45.3, "pressure_hpa": 1013.25}
```

## Key Files

- **`sensor_simulators/sensor_data_generator.py`** — CLI tool. Infinite loop that generates randomized sensor readings (temperature: 18–30°C, humidity: 30–70%, pressure: 990–1025 hPa) with ISO 8601 timestamps. Uses stdlib only (json, random, time, datetime). One reading per line to stdout.

- **`sensor_simulators/sensor_rest_api.py`** — FastAPI REST API. Exposes `/sensor` and `/health` endpoints. Generates a new reading each time `/sensor` is called. Includes automatic API documentation at `/docs`.

## Dependencies

**Current:**
- `fastapi` — REST API framework
- `uvicorn` — ASGI server for FastAPI
- Python stdlib: json, random, time, datetime

**Future additions:**
- `paho-mqtt` — for MQTT publishing/subscribing
- `docker-py` — for programmatic Docker container management (optional)

## Development Notes

- All sensor readings are returned as single-line JSON for easy piping/processing
- Timestamps are UTC to avoid timezone confusion
- Random values are within realistic ranges for atmospheric sensors
- CLI script exits cleanly on Ctrl+C
- REST API includes automatic OpenAPI/Swagger documentation
- Both CLI and API use the same `generate_reading()` function

## Next Steps

1. Add MQTT publishing to the sensor simulator (publish to broker)
2. Create Docker Compose file with multiple MQTT brokers (Mosquitto, HiveMQ, etc.)
3. Build subscriber scripts to consume and validate messages
4. Add performance metrics and logging
5. Create integration tests for the REST API
