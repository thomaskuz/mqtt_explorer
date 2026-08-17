"""
Part 5: Classes and Objects

A class is a BLUEPRINT for creating objects.
An object is an INSTANCE of a class.

Analogy: Class = Recipe, Object = The actual cake

Run: python tests/05_classes_and_objects.py
"""

print("\n" + "="*70)
print("CLASSES AND OBJECTS")
print("="*70)

# Define a class (blueprint)
class Sensor:
    """A blueprint for a sensor object."""

    def __init__(self, sensor_id, location):
        """
        Constructor: runs when you create a new object.
        self = the object being created
        """
        self.sensor_id = sensor_id
        self.location = location
        self.temperature = None
        self.humidity = None

    def read_temperature(self):
        """Read temperature from this sensor."""
        import random
        self.temperature = round(random.uniform(20, 30), 2)
        return self.temperature

    def read_humidity(self):
        """Read humidity from this sensor."""
        import random
        self.humidity = round(random.uniform(40, 70), 2)
        return self.humidity

    def get_status(self):
        """Return a formatted status string."""
        temp_str = f"{self.temperature}°C" if self.temperature else "N/A"
        humidity_str = f"{self.humidity}%" if self.humidity else "N/A"
        return f"[{self.sensor_id}] ({self.location}) Temp: {temp_str}, Humidity: {humidity_str}"


print("\nExample 1: Create objects from the class")

# Create objects (instances)
sensor1 = Sensor("sensor-01", "Living Room")
sensor2 = Sensor("sensor-02", "Bedroom")

print(f"  Created: {sensor1.sensor_id} in {sensor1.location}")
print(f"  Created: {sensor2.sensor_id} in {sensor2.location}")

print("\nExample 2: Call methods on objects")

# Call methods
sensor1.read_temperature()
sensor1.read_humidity()
sensor2.read_temperature()
sensor2.read_humidity()

print(f"  {sensor1.get_status()}")
print(f"  {sensor2.get_status()}")

print("\n" + "-"*70)
print("UNDERSTANDING self")
print("-"*70)

print("""
'self' is a reference to the object itself.
It lets methods access the object's data.

When you call: sensor1.read_temperature()
Python automatically does: Sensor.read_temperature(sensor1)

'self' = sensor1 (the object)
""")

print(f"\nEach object has its own data:")
print(f"  sensor1.temperature = {sensor1.temperature}")
print(f"  sensor2.temperature = {sensor2.temperature}")

print("\n" + "-"*70)
print("ATTRIBUTES VS METHODS")
print("-"*70)

print("""
ATTRIBUTES: Data that the object holds
  - sensor.sensor_id
  - sensor.temperature
  - sensor.location

METHODS: Functions that belong to the object
  - sensor.read_temperature()
  - sensor.read_humidity()
  - sensor.get_status()
""")

print("\n" + "-"*70)
print("DIFFERENT CLASSES FOR DIFFERENT THINGS")
print("-"*70)

class TemperatureSensor:
    """Specialized sensor for just temperature."""

    def __init__(self, sensor_id):
        self.sensor_id = sensor_id
        self.readings = []

    def read(self):
        """Take a temperature reading."""
        import random
        temp = round(random.uniform(20, 30), 2)
        self.readings.append(temp)
        return temp

    def get_average(self):
        """Get average of all readings."""
        if not self.readings:
            return 0
        return round(sum(self.readings) / len(self.readings), 2)


print("\nTemperatureSensor class:")
temp_sensor = TemperatureSensor("temp-01")

print(f"  Read 1: {temp_sensor.read()}°C")
print(f"  Read 2: {temp_sensor.read()}°C")
print(f"  Read 3: {temp_sensor.read()}°C")
print(f"  Average: {temp_sensor.get_average()}°C")
print(f"  All readings: {temp_sensor.readings}")

print("\n" + "-"*70)
print("WHY CLASSES?")
print("-"*70)

print("""
✓ Organize related data and behavior together
✓ Create multiple objects from one blueprint
✓ Each object has its own independent state
✓ Models real-world things (a real sensor)
✓ Reusable and maintainable code
""")

print("\n" + "="*70)
print("EXERCISES")
print("="*70)

print("""
1. Create a class called "HumiditySensor":
   - Takes sensor_id in __init__
   - Has method read() that returns random humidity (30-70%)
   - Has method status() that prints "[sensor-id] Humidity: XX%"

2. Create two HumiditySensor objects and call methods

3. Create a class called "MotionSensor":
   - Takes location in __init__
   - Has is_motion attribute (boolean)
   - Has method detect() that returns True/False
   - Has method alert() that prints if motion detected

4. Use all three sensor classes together:
   - Create one of each type
   - Call their methods
   - Print their status
""")
