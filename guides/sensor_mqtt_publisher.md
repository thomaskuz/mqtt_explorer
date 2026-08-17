# MQTT Publisher Script Guide

## The Big Picture

Your script does one thing: **continuously send sensor data to an MQTT broker**.

```
Your Script (Client) → MQTT Broker → Anyone listening (Subscribers)
```

The broker is like a **post office** — it receives messages and delivers them to anyone who's subscribed to that "address" (topic).

---

## Part 1: Setup & Constants

```python
SENSOR_ID = "sensor-01"
INTERVAL_SECONDS = 5
MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "sensors/sensor-01/reading"
```

**What is this?**
- `MQTT_BROKER` = where the post office (broker) lives
- `MQTT_PORT` = which door to knock on (1883 is the standard MQTT port)
- `MQTT_TOPIC` = the address/channel you're sending to (like a mailing address)
- `INTERVAL_SECONDS` = how often you deliver packages (every 5 seconds)

**Why constants?** So if you need to change them later (different broker, different frequency), you change one place, not scattered throughout the code.

---

## Part 2: The Data Model (Pydantic)

```python
class SensorReading(BaseModel):
    sensor_id: str
    timestamp: str
    temperature_c: float
    humidity_pct: float
    pressure_hpa: float
```

**What is this?**
This defines the **shape** of your data. It's a contract that says: "Every sensor message must have these 5 fields, with these exact types."

**Why?**
- **Validation** — if you accidentally send `temperature_c="hot"` (string instead of number), Pydantic rejects it
- **Documentation** — subscribers know exactly what fields to expect
- **Consistency** — all messages have the same structure

---

## Part 3: Generate Data

```python
def generate_reading() -> dict:
    return {
        "sensor_id": SENSOR_ID,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "temperature_c": round(random.uniform(18.0, 30.0), 2),
        "humidity_pct": round(random.uniform(30.0, 70.0), 2),
        "pressure_hpa": round(random.uniform(990.0, 1025.0), 2),
    }
```

**What is this?**
Creates fake sensor data. Every call returns a new reading with:
- Current timestamp (when the reading was taken)
- Random values for temp/humidity/pressure (simulating a real sensor)

**Why random?** Because we don't have a real sensor, so we simulate realistic values.

---

## Part 4: Callbacks (The Important Part!)

```python
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✓ Connected to MQTT broker")
    else:
        print(f"✗ Connection failed with code {rc}")

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print(f"✗ Unexpected disconnection: {rc}")
```

**What is this?**
These are **event handlers** — functions that run automatically when certain events happen.

**Why?**
- `on_connect` runs when the client successfully connects to the broker
- `on_disconnect` runs when the client loses connection

**Analogy:** Like setting up a doorbell. When someone arrives (connects), the doorbell rings (callback runs).

---

## Part 5: The Main Loop (The Heart)

```python
client = mqtt.Client(client_id="sensor-publisher")
client.on_connect = on_connect
client.on_disconnect = on_disconnect

client.connect(MQTT_BROKER, MQTT_PORT, keepalive=60)

last_publish = time.time()

while True:
    client.loop(timeout=0.1)

    if time.time() - last_publish >= INTERVAL_SECONDS:
        reading_dict = generate_reading()
        validated_reading = SensorReading(**reading_dict)
        payload = validated_reading.model_dump_json()
        client.publish(MQTT_TOPIC, payload, qos=1, retain=True)
        print(f"  → Published to {MQTT_TOPIC}")
        last_publish = time.time()
```

### Line 1-2: Create a client

```python
client = mqtt.Client(client_id="sensor-publisher")
```
- Creates an MQTT client object (your connection representative)
- `client_id` is like your name — the broker uses this to identify you
- **Why?** Only one client with the same name can be connected (prevents duplicates)

### Line 3-4: Register callbacks

```python
client.on_connect = on_connect
client.on_disconnect = on_disconnect
```
- Tells paho-mqtt: "When you connect, run `on_connect()`. When you disconnect, run `on_disconnect()`."

### Line 6: Connect to broker

```python
client.connect(MQTT_BROKER, MQTT_PORT, keepalive=60)
```
- Initiates connection to the broker at `localhost:1883`
- `keepalive=60` means: "If I don't hear from the broker for 60 seconds, something's wrong"
- **Why keepalive?** Detects broken connections and reconnects automatically

### Line 8: Track publish timing

```python
last_publish = time.time()
```
- Remembers when you last published, so we can publish again at the right interval

### Line 10: The event loop

```python
client.loop(timeout=0.1)
```
- **This is critical.** It processes network events for 0.1 seconds
- Checks for incoming messages, handles reconnection, triggers callbacks
- **Why?** MQTT is asynchronous — this keeps the connection alive and responsive

### Line 12-19: Publish on interval

```python
if time.time() - last_publish >= INTERVAL_SECONDS:
    reading_dict = generate_reading()
    validated_reading = SensorReading(**reading_dict)
    payload = validated_reading.model_dump_json()
    client.publish(MQTT_TOPIC, payload, qos=1, retain=True)
```

Every 5 seconds:
1. Generate new sensor data
2. Validate it with Pydantic
3. Convert to JSON string
4. **Publish** the JSON to the topic
5. `qos=1` means "deliver at least once" (reliable)
6. `retain=True` means "keep this message on the broker" (new subscribers see it)

---

## The Loop Cycle (What happens repeatedly)

```
1. client.loop() → handle network events (100 times per second)
2. Check if 5 seconds have passed
3. If yes → generate, validate, publish
4. Repeat forever
```

---

## Why This Design?

**Separation of concerns:**
- `generate_reading()` — data generation
- `SensorReading` — validation
- `client.publish()` — sending
- `client.loop()` — connection management

Each part has one job. If you need to change how data is generated, you edit `generate_reading()`. If you need to add fields, you edit `SensorReading`. Clear and maintainable.