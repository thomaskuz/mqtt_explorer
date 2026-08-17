"""
Part 3: Dictionaries

A dictionary is a collection of key-value pairs.
Like a real dictionary: look up a WORD (key) to find its DEFINITION (value).

Run: python tests/03_dictionaries.py
"""

print("\n" + "="*70)
print("DICTIONARIES - Organizing Data")
print("="*70)

# Create a dictionary
sensor_reading = {
    "sensor_id": "sensor-01",
    "temperature_c": 25.5,
    "humidity_pct": 60,
    "is_online": True,
    "timestamp": "2026-08-12T10:00:00Z"
}

print("\nExample 1: Create and access a dictionary")
print(f"  Full reading: {sensor_reading}")
print(f"  Sensor ID: {sensor_reading['sensor_id']}")
print(f"  Temperature: {sensor_reading['temperature_c']}")

print("\n" + "-"*70)
print("WORKING WITH DICTIONARIES")
print("-"*70)

# Access values
print("\nAccessing values:")
print(f"  sensor_reading['temperature_c'] = {sensor_reading['temperature_c']}")

# Add new key-value pair
print("\nAdding new data:")
sensor_reading["pressure_hpa"] = 1013.25
print(f"  Added pressure: {sensor_reading['pressure_hpa']}")

# Modify existing value
print("\nModifying data:")
sensor_reading["temperature_c"] = 26.0
print(f"  Updated temperature: {sensor_reading['temperature_c']}")

# Check if key exists
print("\nChecking if key exists:")
if "temperature_c" in sensor_reading:
    print(f"  ✓ temperature_c exists: {sensor_reading['temperature_c']}")
if "power_usage" not in sensor_reading:
    print(f"  ✗ power_usage doesn't exist")

# Get all keys and values
print("\nAll keys:")
print(f"  {list(sensor_reading.keys())}")

print("\nAll values:")
print(f"  {list(sensor_reading.values())}")

print("\n" + "-"*70)
print("WHY DICTIONARIES?")
print("-"*70)

print("""
✓ Named access: sensor_reading['temperature_c'] is clear
✓ Flexible: Add fields without changing structure
✓ JSON-ready: Matches JSON format (important for MQTT!)
✓ Self-documenting: Field names explain what each value is
""")

print("\n" + "-"*70)
print("LOOPING THROUGH DICTIONARIES")
print("-"*70)

print("\nLoop through key-value pairs:")
for key, value in sensor_reading.items():
    print(f"  {key}: {value}")

print("\nLoop through keys only:")
for key in sensor_reading.keys():
    print(f"  {key}")

print("\nLoop through values only:")
for value in sensor_reading.values():
    print(f"  {value}")

print("\n" + "-"*70)
print("MULTIPLE DICTIONARIES")
print("-"*70)

# List of dictionaries (common in IoT)
sensor_readings = [
    {"sensor_id": "sensor-01", "temperature_c": 25.5, "humidity_pct": 60},
    {"sensor_id": "sensor-02", "temperature_c": 22.3, "humidity_pct": 65},
    {"sensor_id": "sensor-03", "temperature_c": 28.1, "humidity_pct": 55},
]

print("\nList of sensor readings:")
for reading in sensor_readings:
    print(f"  {reading['sensor_id']}: {reading['temperature_c']}°C, {reading['humidity_pct']}%")

print("\n" + "="*70)
print("EXERCISES")
print("="*70)

print("""
1. Create a dictionary for a sensor with:
   - sensor_id
   - location
   - temperature
   - last_updated (timestamp as string)

2. Add a new field "battery_level" with value 85

3. Print all the data in a formatted way

4. Create a list of 3 different sensors and loop through them

5. Find the sensor with the highest temperature
""")
