"""
Part 8: Imports and Libraries

Imports bring in code that other people wrote.
You don't need to write everything from scratch!

Run: python tests/08_imports_and_libraries.py
"""

print("\n" + "="*70)
print("IMPORTS AND LIBRARIES")
print("="*70)

# ============================================================================
# STANDARD LIBRARY IMPORTS
# ============================================================================

print("\n" + "-"*70)
print("Using Standard Library (Built-in Python modules)")
print("-"*70)

# Random module
import random

print("\n1. RANDOM MODULE")
print(f"  Random integer: {random.randint(1, 10)}")
print(f"  Random float: {random.uniform(20.0, 30.0)}")
print(f"  Random choice: {random.choice(['sensor-01', 'sensor-02', 'sensor-03'])}")

# JSON module
import json

print("\n2. JSON MODULE")
sensor_data = {
    "sensor_id": "sensor-01",
    "temperature_c": 25.5,
    "humidity_pct": 60
}

json_string = json.dumps(sensor_data)
print(f"  Python dict: {sensor_data}")
print(f"  JSON string: {json_string}")

# Convert back
parsed = json.loads(json_string)
print(f"  Parsed back: {parsed}")

# Datetime module
from datetime import datetime, timezone

print("\n3. DATETIME MODULE")
now = datetime.now(timezone.utc)
print(f"  Current time: {now}")
print(f"  ISO format: {now.isoformat()}")

# Time module
import time

print("\n4. TIME MODULE")
print(f"  Current timestamp: {time.time()}")
print(f"  Sleep 1 second...", end=" ")
time.sleep(1)
print("Done!")

# ============================================================================
# IMPORTING SPECIFIC ITEMS
# ============================================================================

print("\n" + "-"*70)
print("Importing Specific Items")
print("-"*70)

from math import sqrt, pi

print(f"\nFrom math module:")
print(f"  sqrt(16) = {sqrt(16)}")
print(f"  pi = {pi}")

# ============================================================================
# COMMON IoT LIBRARIES
# ============================================================================

print("\n" + "-"*70)
print("Common IoT Libraries (What You'll Use)")
print("-"*70)

print("""
1. PYDANTIC (Data validation)
   - Used in your MQTT publisher script
   - Validates and serializes data

   from pydantic import BaseModel
   class SensorReading(BaseModel):
       temperature_c: float

2. PAHO-MQTT (MQTT client)
   - Connects to MQTT brokers
   - Publishes and subscribes to messages

   import paho.mqtt.client as mqtt
   client = mqtt.Client()

3. RANDOM (Generate test data)
   - Already shown above

4. JSON (Serialize data)
   - Already shown above

5. DATETIME (Timestamps)
   - Already shown above
""")

# ============================================================================
# ALIASING IMPORTS
# ============================================================================

print("\n" + "-"*70)
print("Aliasing (Shorter Names)")
print("-"*70)

import random as rnd

print(f"\nUsing alias:")
print(f"  rnd.randint(1, 100) = {rnd.randint(1, 100)}")

# ============================================================================
# WHERE DO LIBRARIES COME FROM?
# ============================================================================

print("\n" + "-"*70)
print("Where Do Libraries Come From?")
print("-"*70)

print("""
STANDARD LIBRARY (Built-in with Python):
✓ random, json, datetime, time, math, etc.
✓ No installation needed
✓ Always available

THIRD-PARTY LIBRARIES (From PyPI):
✓ paho-mqtt (MQTT)
✓ pydantic (validation)
✓ numpy (math)
✓ flask (web framework)

Install with: pip install package_name
""")

# ============================================================================
# CREATING YOUR OWN MODULES
# ============================================================================

print("\n" + "-"*70)
print("Creating Your Own Modules")
print("-"*70)

print("""
You can create your own Python files and import them!

File: my_sensors.py
----
def read_temperature():
    return 25.5

def read_humidity():
    return 60


Then in another file:
----
from my_sensors import read_temperature, read_humidity

temp = read_temperature()
humid = read_humidity()
""")

# ============================================================================
# ORGANIZE IMPORTS
# ============================================================================

print("\n" + "-"*70)
print("Best Practice: Import Organization")
print("-"*70)

print("""
Put imports at the TOP of your file, in this order:

1. Standard library imports
   import random
   import json
   from datetime import datetime

2. Third-party library imports
   import paho.mqtt.client as mqtt
   from pydantic import BaseModel

3. Local imports (your own code)
   from my_sensors import read_temperature


This makes it easy to see what a file depends on.
""")

# ============================================================================
# EXAMPLE: COMPLETE IMPORT SECTION
# ============================================================================

print("\n" + "-"*70)
print("Example: Complete Sensor Project Imports")
print("-"*70)

print("""
# Standard library
import random
import json
from datetime import datetime, timezone

# Third-party
import paho.mqtt.client as mqtt
from pydantic import BaseModel

# Local
# (none in this example)

# Now your code can use all these:
# - random.uniform()
# - json.dumps()
# - datetime.now()
# - mqtt.Client()
# - BaseModel for Pydantic classes
""")

print("\n" + "="*70)
print("EXERCISES")
print("="*70)

print("""
1. Use json module to:
   - Create a dict
   - Convert to JSON string
   - Convert back to dict

2. Use datetime module to:
   - Get current time
   - Print in ISO format
   - Create a timestamp string

3. Create a simple sensor data structure and:
   - Use random for values
   - Use json to serialize
   - Use datetime for timestamp

4. Import only what you need:
   from random import uniform, choice
   Use these imports in your code

5. Explain what library you'd use for:
   a) Connecting to MQTT broker
   b) Validating sensor data
   c) Storing data as JSON
   d) Getting current time
""")
