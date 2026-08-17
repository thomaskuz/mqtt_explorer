# Python Concepts for IoT Development

A beginner's guide to understanding functions, methods, classes, and objects.

---

## Part 1: Variables and Types

A **variable** is a container that holds data.

```python
temperature = 25.5
humidity = 60
sensor_name = "sensor-01"
is_active = True
```

**What are these?**
- `temperature: 25.5` (float/decimal number)
- `humidity: 60` (integer/whole number)
- `sensor_name: "sensor-01"` (string/text)
- `is_active: True` (boolean/true or false)

**Why?** Variables let you store data so you can use it later.

---

## Part 2: Functions (The Basics)

A **function** is a reusable block of code that does ONE job.

Think of it as a tool: you give it input → it does work → it gives you output.

```python
def convert_celsius_to_fahrenheit(celsius):
    """Convert temperature from Celsius to Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Using (calling) the function
temp_c = 25
temp_f = convert_celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f}°F")  # Output: 25°C = 77.0°F
```

**What's happening here?**
1. Define the function with a name: `convert_celsius_to_fahrenheit`
2. Give it an input: `celsius`
3. Do work inside the function
4. Return a result: `return fahrenheit`
5. Call the function: `convert_celsius_to_fahrenheit(25)`

**Why functions?**
- **DRY principle:** Don't Repeat Yourself — write it once, use it many times
- **Testable:** Easy to test and debug one piece of code
- **Readable:** Function names tell you what they do
- **Reusable:** Use the same function in different parts of your code

### Another example: Function without return

```python
def print_sensor_status(sensor_id, temperature, is_online):
    """Print the status of a sensor."""
    status = "✓ Online" if is_online else "✗ Offline"
    print(f"[{sensor_id}] {status} - Temp: {temperature}°C")

print_sensor_status("sensor-01", 25.5, True)   # Output: [sensor-01] ✓ Online - Temp: 25.5°C
print_sensor_status("sensor-02", 22.3, False)  # Output: [sensor-02] ✗ Offline - Temp: 22.3°C
```

This function prints something but doesn't return a value.

---

## Part 3: Functions with Multiple Parameters

Some problems need multiple inputs.

```python
def calculate_dew_point(temperature, humidity):
    """Calculate dew point from temperature and humidity."""
    a = 17.27
    b = 237.7
    alpha = ((a * temperature) / (b + temperature)) + (humidity / 100)
    dew_point = (b * alpha) / (a - alpha)
    return round(dew_point, 2)

dew = calculate_dew_point(25, 60)
print(f"Dew point at 25°C and 60% humidity: {dew}°C")  # Output: 3.44°C
```

**Why multiple parameters?**
- Some problems need multiple pieces of information
- Each parameter is separate input
- The function signature tells readers what data it needs

---

## Part 4: Dictionaries (Organizing Data)

A **dictionary** is a collection of key-value pairs.

Like a real dictionary: you look up a WORD (key) to find its DEFINITION (value).

```python
sensor_reading = {
    "sensor_id": "sensor-01",
    "temperature_c": 25.5,
    "humidity_pct": 60,
    "is_online": True,
    "timestamp": "2026-08-12T10:00:00Z"
}

print(f"Sensor ID: {sensor_reading['sensor_id']}")        # sensor-01
print(f"Temperature: {sensor_reading['temperature_c']}")  # 25.5
```

**Why dictionaries?**
- **Named access:** `sensor_reading['temperature_c']` is clearer than `data[0]`
- **Flexible:** Easy to add new fields without changing code
- **JSON-ready:** Matches JSON format (important for MQTT!)
- **Self-documenting:** You can see what each field means

---

## Part 5: Lists and Loops

A **list** is an ordered collection of items.

```python
sensor_readings = [
    {"sensor_id": "sensor-01", "temperature_c": 25.5},
    {"sensor_id": "sensor-02", "temperature_c": 22.3},
    {"sensor_id": "sensor-03", "temperature_c": 28.1},
]

# Loop through each reading
print("All sensor readings:")
for reading in sensor_readings:
    print(f"  {reading['sensor_id']}: {reading['temperature_c']}°C")
```

**Output:**
```
All sensor readings:
  sensor-01: 25.5°C
  sensor-02: 22.3°C
  sensor-03: 28.1°C
```

**Why loops?**
- Process multiple items without writing code for each one
- Handle unknown number of items (1 sensor or 1000 sensors)
- Clean, readable code

---

## Part 6: Objects and Classes

This is the important part! Objects and classes organize your code around real-world things.

### What's a class?

A **class** is a BLUEPRINT for creating objects.

- Defines what data an object has (attributes)
- Defines what an object can DO (methods)

**Analogy:** A class is like a recipe, an object is the actual cake.

### Creating a Class

```python
class Sensor:
    """Blueprint for a sensor object."""

    def __init__(self, sensor_id, location):
        """
        Constructor: runs when you create a new Sensor
        self = the object being created
        These are ATTRIBUTES (data the object holds)
        """
        self.sensor_id = sensor_id
        self.location = location
        self.temperature = None
        self.humidity = None

    def read_temperature(self):
        """A METHOD: a function that belongs to this object."""
        import random
        self.temperature = round(random.uniform(20, 30), 2)
        return self.temperature

    def read_humidity(self):
        """Another method."""
        import random
        self.humidity = round(random.uniform(40, 70), 2)
        return self.humidity

    def get_status(self):
        """Return a formatted status string."""
        temp_str = f"{self.temperature}°C" if self.temperature else "N/A"
        humidity_str = f"{self.humidity}%" if self.humidity else "N/A"
        return f"[{self.sensor_id}] ({self.location}) Temp: {temp_str}, Humidity: {humidity_str}"
```

### Creating Objects (Instances)

```python
# Creating objects from the class blueprint
sensor1 = Sensor("sensor-01", "Living Room")
sensor2 = Sensor("sensor-02", "Bedroom")

# Each object has its own data
sensor1.read_temperature()
sensor1.read_humidity()
sensor2.read_temperature()
sensor2.read_humidity()

print(sensor1.get_status())  # [sensor-01] (Living Room) Temp: 25.3°C, Humidity: 55.2%
print(sensor2.get_status())  # [sensor-02] (Bedroom) Temp: 22.1°C, Humidity: 48.9%
```

**Why classes?**
- **Organization:** Combine related data and behavior together
- **Reusability:** Create multiple objects from one blueprint
- **Independence:** Each object has its own state (sensor1.temperature ≠ sensor2.temperature)
- **Real-world modeling:** Classes represent real things (a real sensor)

---

## Part 7: Methods vs Functions

This is a key distinction!

### Functions

- Standalone code that does work
- Called like: `convert_celsius_to_fahrenheit(25)`
- Doesn't belong to any object

### Methods

- A function that belongs to an object
- Called like: `sensor1.read_temperature()`
- Belongs to the sensor1 object
- Can access the object's data using `self`

```python
# Function call
result = convert_celsius_to_fahrenheit(25)

# Method call
temp = sensor1.read_temperature()
```

**Why the difference?**
- Methods have access to the object's state (`self`)
- Functions are general-purpose tools
- Makes code cleaner and more organized

---

## Part 8: Understanding 'self'

`self` is a reference to the object itself.

It lets methods access and modify the object's data.

```python
class SmartSensor:
    def __init__(self, sensor_id):
        self.sensor_id = sensor_id      # Each object has its own sensor_id
        self.readings = []              # Each object has its own readings list

    def add_reading(self, value):
        """Add a reading to the list."""
        self.readings.append(value)     # self.readings = THIS object's list
        print(f"[{self.sensor_id}] Added reading: {value}")

    def get_average(self):
        """Calculate average of all readings."""
        if not self.readings:
            return 0
        return sum(self.readings) / len(self.readings)

# Create two sensors
sensor1 = SmartSensor("sensor-01")
sensor2 = SmartSensor("sensor-02")

# Add readings to sensor1
sensor1.add_reading(25.0)
sensor1.add_reading(25.5)
sensor1.add_reading(26.0)

# sensor2 stays empty
print(f"Sensor1 average: {sensor1.get_average()}")  # 25.5
print(f"Sensor2 average: {sensor2.get_average()}")  # 0
```

**Key insight:**
- `self.sensor_id` refers to THIS object's sensor_id
- `self.readings` refers to THIS object's readings list
- Each object has its own separate data
- `self` is how methods know which object they belong to

---

## Part 9: Callbacks (Functions as Parameters)

A **callback** is a function you pass to another function.

It says: "When X happens, call THIS function"

```python
def on_temperature_high(sensor_id, temperature):
    """This function gets called when temp is too high."""
    print(f"⚠️  ALERT: {sensor_id} temperature is {temperature}°C!")

def check_temperature(sensor_id, temperature, on_high_callback):
    """
    Check if temperature is acceptable.
    If too high, call the callback function.
    """
    if temperature > 27:
        on_high_callback(sensor_id, temperature)
    else:
        print(f"✓ {sensor_id} temperature OK: {temperature}°C")

# Example 1: Temperature is normal
check_temperature("sensor-01", 25.0, on_temperature_high)
# Output: ✓ sensor-01 temperature OK: 25.0°C

# Example 2: Temperature is too high
check_temperature("sensor-02", 28.5, on_temperature_high)
# Output: ⚠️  ALERT: sensor-02 temperature is 28.5°C!
```

**Why callbacks?**
- **Event-driven:** "When this happens, do that"
- **Used in MQTT:** `on_connect()`, `on_disconnect()`, `on_message()`
- **Decoupled code:** The callback handler doesn't need to know about the checking logic

**In your MQTT script:**
```python
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected")

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Disconnected")

# Pass these callbacks to the client
client.on_connect = on_connect
client.on_disconnect = on_disconnect

# Now they get called automatically when connection events happen
```

---

## Part 10: Imports and Libraries

**Imports** bring in code that other people wrote.

You don't need to write everything from scratch!

```python
import random
import json
from datetime import datetime, timezone

# Using random library
random_temp = random.uniform(20, 30)

# Using json library
sensor_data = {"sensor_id": "sensor-01", "temperature": 25.5}
json_string = json.dumps(sensor_data)
# Output: {"sensor_id": "sensor-01", "temperature": 25.5}

# Using datetime library
now = datetime.now(timezone.utc)
timestamp = now.isoformat()
# Output: 2026-08-12T10:00:00.123456+00:00
```

**Common IoT libraries:**
- `json` — converts between Python dicts and JSON strings
- `datetime` — handles dates and times
- `paho-mqtt` — handles MQTT connections
- `pydantic` — validates and serializes data
- `random` — generates random numbers

**Why libraries?**
- Don't reinvent the wheel
- Well-tested, reliable code
- Focus on your logic, not implementation details
- Huge time saver

---

## Summary: How These Concepts Connect

In your MQTT Publisher script, you use ALL these concepts:

| Concept | Example |
|---------|---------|
| **Variables** | `MQTT_BROKER = "localhost"`, `INTERVAL_SECONDS = 5` |
| **Functions** | `generate_reading()` — creates sensor data |
| **Dictionaries** | `{"sensor_id": "sensor-01", "temperature_c": 25.5}` |
| **Classes** | `SensorReading(BaseModel)` — defines data structure |
| **Objects** | `mqtt.Client()` creates a client object |
| **Methods** | `client.connect()`, `client.publish()`, `validated_reading.model_dump_json()` |
| **Callbacks** | `on_connect()`, `on_disconnect()` — run automatically when events happen |
| **Imports** | `import paho.mqtt.client`, `from pydantic import BaseModel` |

All these concepts work together to create your IoT application!

---

## Practice Exercises

Try these to practice:

### Exercise 1: Create a New Class
Create a class called `TemperatureSensor` with:
- `__init__()` that takes sensor_id and location
- `read()` method that returns a random temperature (18-30°C)
- `convert_to_fahrenheit()` method that converts stored temperature
- `get_info()` method that returns a formatted string with all info

### Exercise 2: Function with List
Create a function called `get_average_temperature()` that:
- Takes a list of sensor objects as input
- Reads temperature from each sensor
- Returns the average temperature

### Exercise 3: Callbacks with Sensors
Create a callback function called `on_high_temperature()` that:
- Takes sensor_id and temperature as parameters
- Prints an alert if temperature > 27°C
- Pass it to each sensor when reading temperature

### Exercise 4: JSON Serialization
Create a function called `sensor_to_json()` that:
- Takes a sensor object as input
- Creates a dictionary with sensor_id, temperature, humidity, timestamp
- Converts it to JSON string using `json.dumps()`
- Returns the JSON string

### Exercise 5: Combine Everything
Create a complete IoT system that:
- Creates 3 sensor objects
- Has a callback for high temperatures
- Reads all sensors
- Stores readings in a list
- Prints JSON of each reading

---

## Next Steps

1. **Read through this guide** — understand each concept
2. **Run the Python file** (`tests/python_iot_concepts.py`) — see the examples
3. **Try the practice exercises** — experiment and learn
4. **Ask questions** — any concept that's unclear?
5. **Modify the code** — break things, fix them, learn!

This knowledge is your foundation for IoT development!
