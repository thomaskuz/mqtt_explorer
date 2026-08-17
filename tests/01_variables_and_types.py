"""
Part 1: Variables and Types

A variable is a container that holds data.
This script shows the basic data types you'll use in IoT.

Run: python tests/01_variables_and_types.py
"""

print("\n" + "="*70)
print("VARIABLES AND TYPES")
print("="*70)

# A variable stores data with a name
temperature = 25.5
humidity = 60
sensor_name = "sensor-01"
is_active = True

print(f"\nTemperature: {temperature} (type: {type(temperature).__name__})")
print(f"Humidity: {humidity} (type: {type(humidity).__name__})")
print(f"Sensor name: {sensor_name} (type: {type(sensor_name).__name__})")
print(f"Is active: {is_active} (type: {type(is_active).__name__})")

print("\nWHY? Variables let you store data so you can use it later.")

print("\n" + "-"*70)
print("DIFFERENT DATA TYPES")
print("-"*70)

# Float (decimal numbers)
print("\nFloats (decimals):")
temp_celsius = 25.5
print(f"  temp_celsius = {temp_celsius}")
print(f"  Type: {type(temp_celsius).__name__}")

# Integer (whole numbers)
print("\nIntegers (whole numbers):")
sensor_count = 5
print(f"  sensor_count = {sensor_count}")
print(f"  Type: {type(sensor_count).__name__}")

# String (text)
print("\nStrings (text):")
location = "Living Room"
print(f"  location = '{location}'")
print(f"  Type: {type(location).__name__}")

# Boolean (True/False)
print("\nBooleans (True/False):")
is_online = True
print(f"  is_online = {is_online}")
print(f"  Type: {type(is_online).__name__}")

# None (empty/no value)
print("\nNone (nothing/empty):")
last_error = None
print(f"  last_error = {last_error}")
print(f"  Type: {type(last_error).__name__}")

print("\n" + "-"*70)
print("TYPE CONVERSION")
print("-"*70)

# Convert string to integer
temp_str = "25"
temp_int = int(temp_str)
print(f"\nString to integer:")
print(f"  temp_str = '{temp_str}' (type: {type(temp_str).__name__})")
print(f"  temp_int = {temp_int} (type: {type(temp_int).__name__})")

# Convert integer to string
sensor_id = 1
sensor_id_str = str(sensor_id)
print(f"\nInteger to string:")
print(f"  sensor_id = {sensor_id} (type: {type(sensor_id).__name__})")
print(f"  sensor_id_str = '{sensor_id_str}' (type: {type(sensor_id_str).__name__})")

# Convert to float
count = 5
count_float = float(count)
print(f"\nInteger to float:")
print(f"  count = {count} (type: {type(count).__name__})")
print(f"  count_float = {count_float} (type: {type(count_float).__name__})")

print("\n" + "="*70)
print("EXERCISES")
print("="*70)

print("""
1. Create a variable for each sensor reading:
   - sensor_id (string)
   - temperature (float)
   - humidity (float)
   - is_active (boolean)

2. Print each variable with its type

3. Convert temperature from string "28.5" to float

4. Create a variable for timestamp (string) and print it
""")
