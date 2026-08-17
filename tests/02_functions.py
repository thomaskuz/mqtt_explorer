"""
Part 2: Functions

A function is a reusable block of code that does ONE job.
Think: give it input → it does work → it returns output.

Run: python tests/02_functions.py
"""

print("\n" + "="*70)
print("FUNCTIONS - The Basics")
print("="*70)

# Simple function with one input and one output
def convert_celsius_to_fahrenheit(celsius):
    """Convert temperature from Celsius to Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

print("\nExample 1: Simple conversion")
temp_c = 25
temp_f = convert_celsius_to_fahrenheit(temp_c)
print(f"  {temp_c}°C = {temp_f}°F")

# Function with multiple inputs
def calculate_dew_point(temperature, humidity):
    """Calculate dew point from temperature and humidity."""
    a = 17.27
    b = 237.7
    alpha = ((a * temperature) / (b + temperature)) + (humidity / 100)
    dew_point = (b * alpha) / (a - alpha)
    return round(dew_point, 2)

print("\nExample 2: Multiple inputs")
dew = calculate_dew_point(25, 60)
print(f"  Dew point at 25°C and 60% humidity: {dew}°C")

# Function that doesn't return anything (but prints)
def print_sensor_status(sensor_id, temperature, is_online):
    """Print the status of a sensor."""
    status = "✓ Online" if is_online else "✗ Offline"
    print(f"  [{sensor_id}] {status} - Temp: {temperature}°C")

print("\nExample 3: Function that prints (no return)")
print_sensor_status("sensor-01", 25.5, True)
print_sensor_status("sensor-02", 22.3, False)

# Function that returns multiple values
def read_sensor(sensor_id):
    """Read temperature and humidity from a sensor."""
    import random
    temperature = round(random.uniform(20, 30), 2)
    humidity = round(random.uniform(40, 70), 2)
    return temperature, humidity

print("\nExample 4: Return multiple values")
temp, humid = read_sensor("sensor-01")
print(f"  Sensor reading: {temp}°C, {humid}%")

print("\n" + "-"*70)
print("WHY FUNCTIONS?")
print("-"*70)

print("""
✓ DRY (Don't Repeat Yourself): Write once, use many times
✓ Testable: Easy to test one piece of code
✓ Readable: Function names tell you what they do
✓ Maintainable: Change logic in one place
""")

print("\n" + "-"*70)
print("FUNCTION ANATOMY")
print("-"*70)

print("""
def function_name(parameter1, parameter2):
    \"\"\"Description of what this function does.\"\"\"
    # Do work here
    result = parameter1 + parameter2
    return result

- def: keyword to define a function
- function_name: what you call it
- parameters: inputs the function needs (optional)
- docstring: explanation (in triple quotes)
- return: what the function gives back (optional)
""")

print("\n" + "="*70)
print("EXERCISES")
print("="*70)

print("""
1. Create a function that takes two temperatures and returns the average

2. Create a function that takes sensor_id and temperature,
   and returns True if temperature > 25, False otherwise

3. Create a function that prints a formatted sensor message:
   [sensor-id] Temperature: XX°C, Humidity: YY%

4. Create a function that converts humidity percentage to a level:
   < 30%: "Low"
   30-60%: "Comfortable"
   > 60%: "High"
""")
