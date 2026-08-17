"""
Part 6: Methods vs Functions

KEY DIFFERENCE:
- Function: Standalone code
- Method: A function that belongs to an object

Run: python tests/06_methods_vs_functions.py
"""

print("\n" + "="*70)
print("METHODS VS FUNCTIONS")
print("="*70)

# ============================================================================
# FUNCTIONS (standalone)
# ============================================================================

print("\n" + "-"*70)
print("FUNCTIONS: Standalone Code")
print("-"*70)

def convert_celsius_to_fahrenheit(celsius):
    """A function: standalone, not attached to any object."""
    return (celsius * 9/5) + 32

print("\nFunction call:")
result = convert_celsius_to_fahrenheit(25)
print(f"  convert_celsius_to_fahrenheit(25) = {result}°F")
print(f"  Type: {type(result)}")

# ============================================================================
# METHODS (belong to objects)
# ============================================================================

print("\n" + "-"*70)
print("METHODS: Functions That Belong to Objects")
print("-"*70)

class Temperature:
    """A class with methods."""

    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        """A method: belongs to this object, has access to self."""
        return (self.celsius * 9/5) + 32

    def to_kelvin(self):
        """Another method."""
        return self.celsius + 273.15


# Create an object
temp = Temperature(25)

print(f"\nMethod calls:")
print(f"  temp.to_fahrenheit() = {temp.to_fahrenheit()}°F")
print(f"  temp.to_kelvin() = {temp.to_kelvin()}K")

print("\n" + "-"*70)
print("KEY DIFFERENCES")
print("-"*70)

print("""
FUNCTION:
  - Called: convert_celsius_to_fahrenheit(25)
  - Standalone, doesn't know about objects
  - Takes all needed data as parameters
  - Cannot access object's state

METHOD:
  - Called: temp.to_fahrenheit()
  - Belongs to an object
  - Can access self (the object's data)
  - Knows about the object's state

Example:
  Function: You give it data, it processes it
  Method: The object has data, the method uses it
""")

print("\n" + "-"*70)
print("WHEN TO USE EACH")
print("-"*70)

print("""
USE FUNCTIONS FOR:
✓ Utility operations (convert, calculate, validate)
✓ Stateless operations (no need to remember state)
✓ Reusable across different contexts

USE METHODS FOR:
✓ Operations tied to an object
✓ Operations that modify object state
✓ Operations that use object's internal data
""")

print("\n" + "-"*70)
print("REAL IoT EXAMPLE")
print("-"*70)

# A utility function
def calculate_heat_index(temperature, humidity):
    """Function: pure calculation."""
    c1 = -42.379
    c2 = 2.04901523
    c3 = 10.14333127
    c4 = -0.22475541
    c5 = -0.00683783
    c6 = -0.05481717
    c7 = 0.00122874
    c8 = 0.00085282
    c9 = -0.00000199

    t = temperature
    rh = humidity

    hi = (c1 + c2*t + c3*rh + c4*t*rh + c5*t**2 + c6*rh**2 +
          c7*t**2*rh + c8*t*rh**2 + c9*t**2*rh**2)
    return round(hi, 2)


# A class with methods
class Sensor:
    """A sensor object with methods."""

    def __init__(self, sensor_id, location):
        self.sensor_id = sensor_id
        self.location = location
        self.temperature = None
        self.humidity = None

    def take_reading(self, temp, humid):
        """Method: stores data in the object."""
        self.temperature = temp
        self.humidity = humid

    def get_heat_index(self):
        """Method: uses the object's stored data."""
        if self.temperature is None or self.humidity is None:
            return None
        return calculate_heat_index(self.temperature, self.humidity)

    def status(self):
        """Method: returns formatted info about this specific sensor."""
        heat_index = self.get_heat_index()
        hi_str = f"Heat Index: {heat_index}°F" if heat_index else "No data"
        return f"[{self.sensor_id}] {self.location} - {self.temperature}°C, {self.humidity}% - {hi_str}"


print("\nUsing function and methods together:")

sensor = Sensor("sensor-01", "Outside")
sensor.take_reading(35, 70)

print(f"\n  Function call:")
print(f"    calculate_heat_index(35, 70) = {calculate_heat_index(35, 70)}°F")

print(f"\n  Method call:")
print(f"    sensor.get_heat_index() = {sensor.get_heat_index()}°F")

print(f"\n  Method that uses data:")
print(f"    {sensor.status()}")

print("\n" + "="*70)
print("EXERCISES")
print("="*70)

print("""
1. Create a function that calculates average of three numbers

2. Create a class "DataCollector" with:
   - Method add_reading(value)
   - Method get_average() that uses the stored data
   - Compare to the function version

3. Create a function validate_temperature(temp)
   - Returns True if 0 < temp < 50, False otherwise

4. Add method validate_reading() to a sensor class
   - Uses object's stored temperature
   - Returns True/False based on valid range

5. Decide: Should this be a function or method?
   a) Calculate dew point (function or method?)
   b) Check if a sensor is online (function or method?)
   c) Convert between units (function or method?)
""")
