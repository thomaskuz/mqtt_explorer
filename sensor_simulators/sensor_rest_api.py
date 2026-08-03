import random
from datetime import datetime, timezone
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

SENSOR_ID = "sensor-01"


class SensorReading(BaseModel):
    sensor_id: str
    timestamp: str
    temperature_c: float
    humidity_pct: float
    pressure_hpa: float


class HealthStatus(BaseModel):
    status: str


def generate_reading() -> dict:
    return {
        "sensor_id": SENSOR_ID,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "temperature_c": round(random.uniform(18.0, 30.0), 2),
        "humidity_pct": round(random.uniform(30.0, 70.0), 2),
        "pressure_hpa": round(random.uniform(990.0, 1025.0), 2),
    }


@app.get("/sensor", response_model=SensorReading)
def get_sensor_reading() -> dict:
    """Return a single sensor reading."""
    return generate_reading()


@app.get("/health", response_model=HealthStatus)
def health() -> dict:
    """Health check endpoint."""
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
