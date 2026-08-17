"""
Python Concepts for IoT Development
A beginner's guide to understanding functions, methods, classes, and objects.

Run this file to see examples:
    python3 tests/python_iot_concepts.py
"""

# ==============================================================================
# PART 1: VARIABLES AND TYPES
# ==============================================================================

print("\n" + "="*70)
print("PART 1: VARIABLES AND TYPES")
print("="*70)

# A variable is a container that holds data
temperature = 25.5
humidity = 60
sensor_name = "sensor-01"
is_active = True

print(f"Temperature: {temperature} (type: {type(temperature).__name__})")
print(f"Humidity: {humidity} (type: {type(humidity).__name__})")
print(f"Sensor name: {sensor_name} (type: {type(sensor_name).__name__})")
print(f"Is active: {is_active} (type: {type(is_active).__name__})")

print("\nWHY? Variables let you store data so you can use it later.")


# ==============================================================================
# PART 2: FUNCTIONS (The Basics)
# ==============================================================================

print("\n" + "="*70)
print("PART 2: FUNCTIONS")
print("="*70)

# A function is a reusable block of code that does ONE job
# Think of it as a tool: you give it input, it does work, it gives you output

def convert_celsius_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.

    This function:
    - Takes one input (celsius)
    - Does a calculation
    - Returns the result
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


# Using (calling) the function
temp_c = 25
temp_f = convert_celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f}°F")

print("\nWHY functions?")
print("- DRY principle: Don't Repeat Yourself")
print("- If you need this conversion 100 times, write it once")
print("- Easy to test and debug")
print("- Readable code")


# Another example: a function that doesn't return anything
def print_sensor_status(sensor_id, temperature, is_online):
    """Print the status of a sensor."""
    status = "✓ Online" if is_online else "✗ Offline"
    print(f"[{sensor_id}] {status} - Temp: {temperature}°C")


print_sensor_status("sensor-01", 25.5, True)
print_sensor_status("sensor-02", 22.3, False)


# ==============================================================================
# PART 3: FUNCTIONS WITH MULTIPLE PARAMETERS
# ==============================================================================

print("\n" + "="*70)
print("PART 3: FUNCTIONS WITH MULTIPLE PARAMETERS")
print("="*70)

def calculate_dew_point(temperature, humidity):
    """
    Calculate dew point from temperature and humidity.
    This function needs TWO inputs to work.
    """
    # Simplified dew point formula
    a = 17.27
    b = 237.7
    alpha = ((a * temperature) / (b + temperature)) + (humidity / 100)
    dew_point = (b * alpha) / (a - alpha)
    return round(dew_point, 2)


dew = calculate_dew_point(25, 60)
print(f"Dew point at 25°C and 60% humidity: {dew}°C")

print("\nWHY multiple parameters?")
print("- Some problems need multiple inputs")
print("- Each parameter is a separate piece of information")
print("- Function signature tells readers what data it needs")


# ==============================================================================
# PART 4: DICTIONARIES AND DATA STRUCTURES
# ==============================================================================

print("\n" + "="*70)
print("PART 4: DICTIONARIES (Organizing Data)")
print("="*70)

# A dictionary is a collection of key-value pairs
# Like a real dictionary: you look up a WORD (key) to find its DEFINITION (value)

sensor_reading = {
    "sensor_id": "sensor-01",
    "temperature_c": 25.5,
    "humidity_pct": 60,
    "is_online": True,
    "timestamp": "2026-08-12T10:00:00Z"
}

print(f"Sensor ID: {sensor_reading['sensor_id']}")
print(f"Temperature: {sensor_reading['temperature_c']}")

print("\nWHY dictionaries?")
print("- Named access: sensor_reading['temperature_c'] is clearer than data[0]")
print("- Easy to add new fields without changing code")
print("- Matches JSON format (important for MQTT!)")
print("- Self-documenting: you can see what each field means")


# ==============================================================================
# PART 5: LISTS AND LOOPING
# ==============================================================================

print("\n" + "="*70)
print("PART 5: LISTS AND LOOPS")
print("="*70)

# A list is an ordered collection of items
sensor_readings = [
    {"sensor_id": "sensor-01", "temperature_c": 25.5},
    {"sensor_id": "sensor-02", "temperature_c": 22.3},
    {"sensor_id": "sensor-03", "temperature_c": 28.1},
]

# Loop through each reading
print("All sensor readings:")
for reading in sensor_readings:
    print(f"  {reading['sensor_id']}: {reading['temperature_c']}°C")

print("\nWHY loops?")
print("- Process multiple items without writing code for each one")
print("- Handle unknown number of items (1 sensor or 1000 sensors)")
print("- Clean, readable code")


# ==============================================================================
# PART 6: OBJECTS AND CLASSES (The Hard Part!)
# ==============================================================================

print("\n" + "="*70)
print("PART 6: OBJECTS AND CLASSES")
print("="*70)

print("\nWhat's a class?")
print("- A BLUEPRINT for creating objects")
print("- Defines what data an object has (attributes)")
print("- Defines what an object can DO (methods)")
print("\nAnalogy: A class is like a recipe, an object is the actual cake")

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
        """
        A METHOD: a function that belongs to this object
        It has access to self (the object's data)
        """
        # In real life, this would read from a sensor
        # Here we just simulate it
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


# Creating objects (instances) from the class blueprint
sensor1 = Sensor("sensor-01", "Living Room")
sensor2 = Sensor("sensor-02", "Bedroom")

print(f"\nCreated two sensors:")
print(f"  - {sensor1.sensor_id} in {sensor1.location}")
print(f"  - {sensor2.sensor_id} in {sensor2.location}")

# Calling methods (functions that belong to the object)
print("\nReading sensors:")
sensor1.read_temperature()
sensor1.read_humidity()
sensor2.read_temperature()
sensor2.read_humidity()

print(f"  {sensor1.get_status()}")
print(f"  {sensor2.get_status()}")

print("\nWHY classes?")
print("- Organize related data AND behavior together")
print("- Create multiple objects from one blueprint (sensor1, sensor2, ...)")
print("- Each object has its own state (sensor1.temperature ≠ sensor2.temperature)")
print("- Models real-world things (a real sensor)")


# ==============================================================================
# PART 7: METHODS VS FUNCTIONS
# ==============================================================================

print("\n" + "="*70)
print("PART 7: METHODS vs FUNCTIONS")
print("="*70)

print("\nFUNCTION: Standalone code that does work")
print("  - Called like: convert_celsius_to_fahrenheit(25)")
print("  - Doesn't belong to any object")

print("\nMETHOD: A function that belongs to an object")
print("  - Called like: sensor1.read_temperature()")
print("  - Belongs to the sensor1 object")
print("  - Can access the object's data (self.sensor_id, self.temperature)")

# Demonstration
print(f"\nFunction call: {convert_celsius_to_fahrenheit(25)}")
print(f"Method call: {sensor1.read_temperature()}")


# ==============================================================================
# PART 8: UNDERSTANDING 'self'
# ==============================================================================

print("\n" + "="*70)
print("PART 8: UNDERSTANDING 'self'")
print("="*70)

print("'self' is a reference to the object itself")
print("It lets methods access the object's data")

class SmartSensor:
    def __init__(self, sensor_id):
        self.sensor_id = sensor_id
        self.readings = []  # List to store all readings

    def add_reading(self, value):
        """Add a reading to the list."""
        self.readings.append(value)
        print(f"[{self.sensor_id}] Added reading: {value}")

    def get_average(self):
        """Calculate average of all readings."""
        if not self.readings:
            return 0
        return sum(self.readings) / len(self.readings)


smart_sensor = SmartSensor("sensor-01")
smart_sensor.add_reading(25.0)
smart_sensor.add_reading(25.5)
smart_sensor.add_reading(26.0)

print(f"Average: {smart_sensor.get_average()}°C")
print(f"All readings: {smart_sensor.readings}")

print("\nNotice:")
print("- self.sensor_id refers to THIS object's sensor_id")
print("- self.readings refers to THIS object's readings list")
print("- Each object has its own separate data")


# ==============================================================================
# PART 9: CALLBACKS (Important for MQTT!)
# ==============================================================================

print("\n" + "="*70)
print("PART 9: CALLBACKS (Functions as Parameters)")
print("="*70)

print("A callback is a function you pass to another function")
print("It says: 'When X happens, call THIS function'")

# Simple example
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


print("\nExample 1: Temperature is normal")
check_temperature("sensor-01", 25.0, on_temperature_high)

print("\nExample 2: Temperature is too high")
check_temperature("sensor-02", 28.5, on_temperature_high)

print("\nWHY callbacks?")
print("- Event-driven programming: 'When this happens, do that'")
print("- Used in MQTT: on_connect(), on_disconnect(), on_message()")
print("- Decouples code: the callback handler doesn't need to know how to check")


# ==============================================================================
# PART 10: IMPORTS AND LIBRARIES
# ==============================================================================

print("\n" + "="*70)
print("PART 10: IMPORTS AND LIBRARIES")
print("="*70)

import random
import json
from datetime import datetime, timezone

print("Imports bring in code that other people wrote")
print("You don't need to write everything from scratch")

sensor_data = {
    "sensor_id": "sensor-01",
    "temperature": 25.5,
    "timestamp": datetime.now(timezone.utc).isoformat()
}

json_string = json.dumps(sensor_data)
print(f"\nSensor data as JSON:\n{json_string}")

print("\nWHY libraries?")
print("- Don't reinvent the wheel")
print("- json: converts between Python dicts and JSON strings")
print("- datetime: handles dates and times")
print("- paho-mqtt: handles MQTT connections (used in your script!)")


# ==============================================================================
# SUMMARY
# ==============================================================================

print("\n" + "="*70)
print("SUMMARY: How These Concepts Connect")
print("="*70)

print("""
In your MQTT Publisher script, you use ALL these concepts:

1. VARIABLES: MQTT_BROKER, INTERVAL_SECONDS, etc.

2. FUNCTIONS: generate_reading()

3. CLASSES: SensorReading (Pydantic BaseModel)

4. OBJECTS:
   - mqtt.Client() creates a client object
   - sensor_reading = SensorReading(...) creates a sensor object

5. METHODS:
   - client.connect() - method to connect
   - client.publish() - method to publish
   - validated_reading.model_dump_json() - method to serialize

6. CALLBACKS:
   - on_connect(client, userdata, flags, rc)
   - on_disconnect(client, userdata, rc)
   - These run automatically when events happen

7. IMPORTS:
   - import paho.mqtt.client as mqtt
   - from pydantic import BaseModel
   - import random, json, etc.

All these concepts work together to create your IoT application!
""")

print("\n" + "="*70)
print("WHAT TO PRACTICE")
print("="*70)

print("""
Try modifying this file:

1. Create a new class called "TemperatureSensor" with methods:
   - read() - returns a random temperature
   - convert_to_fahrenheit() - converts stored temperature

2. Create a function that takes a list of sensor objects
   and returns the average temperature

3. Create a callback that gets called when any sensor
   reads above 25°C

4. Use json.dumps() to convert sensor objects to JSON

Work through these exercises to practice!
""")
