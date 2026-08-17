"""
Part 9: Event Loops

An event loop is a program that waits for events and responds to them.
CRUCIAL for IoT: your MQTT client runs in an event loop!

Run: python tests/09_event_loops.py
"""

import time

print("\n" + "="*70)
print("EVENT LOOPS")
print("="*70)

# ============================================================================
# WHAT IS AN EVENT LOOP?
# ============================================================================

print("\n" + "-"*70)
print("What Is an Event Loop?")
print("-"*70)

print("""
An event loop is a simple concept:

while True:
    # Wait for something to happen (event)
    event = wait_for_event()

    # When something happens, respond to it (handle event)
    if event == "button_pressed":
        handle_button_press()
    elif event == "temperature_high":
        handle_high_temp()
    elif event == "message_received":
        handle_message()

This is the core pattern of event-driven programming!
""")

# ============================================================================
# SIMPLE EVENT LOOP EXAMPLE
# ============================================================================

print("\n" + "-"*70)
print("Example 1: Simple Event Loop")
print("-"*70)

class SimpleEventLoop:
    """A basic event loop simulator."""

    def __init__(self):
        self.handlers = {}  # Dictionary of {event: callback}
        self.running = False

    def on(self, event_name, callback):
        """Register a callback for an event."""
        self.handlers[event_name] = callback

    def emit(self, event_name, data=None):
        """Trigger an event (call its callback)."""
        if event_name in self.handlers:
            self.handlers[event_name](data)

    def run(self):
        """Run the event loop."""
        self.running = True
        print("  Event loop started")


# Define event handlers (callbacks)
def on_connection(data):
    print(f"  ✓ Event: {data}")


def on_sensor_reading(data):
    print(f"  📊 Event: {data}")


def on_error(data):
    print(f"  ✗ Event: {data}")


# Create and use event loop
loop = SimpleEventLoop()
loop.on("connected", on_connection)
loop.on("reading", on_sensor_reading)
loop.on("error", on_error)

loop.run()

# Emit (trigger) events
loop.emit("connected", "Connected to MQTT broker")
loop.emit("reading", "Temperature: 25.5°C")
loop.emit("error", "Connection timeout")

# ============================================================================
# EVENT LOOP IN REAL MQTT
# ============================================================================

print("\n" + "-"*70)
print("Example 2: Event Loop in MQTT")
print("-"*70)

print("""
Your MQTT client RUNS an event loop:

import paho.mqtt.client as mqtt

client = mqtt.Client()
client.on_connect = on_connect      # Register callbacks
client.on_disconnect = on_disconnect
client.on_message = on_message

client.connect("localhost", 1883)

# This starts the event loop!
# It continuously:
# 1. Waits for network events
# 2. Calls callbacks when events happen
# 3. Handles reconnection
client.loop_forever()               # Blocks and runs forever


The event loop is ALWAYS running in the background!
When the broker sends you a message, the loop:
1. Receives it
2. Calls your on_message() callback
3. Your callback handles the message
4. Loop continues waiting
""")

# ============================================================================
# BLOCKING VS NON-BLOCKING
# ============================================================================

print("\n" + "-"*70)
print("Example 3: Blocking Event Loop")
print("-"*70)

print("\nBlocking loop (loop_forever):")
print("""
client.loop_forever()  # This BLOCKS - code after it never runs!

while True:
    # Process events
    # Reconnect if needed
    # Handle timeouts
    pass
""")

print("\nNon-blocking loop (client.loop):")
print("""
while True:
    client.loop(timeout=0.1)  # Process for 100ms, then return

    # You can do other things here!
    temp = read_sensor()
    humidity = read_sensor()

    # Then process events again
    client.loop(timeout=0.1)
""")

# ============================================================================
# SIMULATING A SENSOR LOOP
# ============================================================================

print("\n" + "-"*70)
print("Example 4: Sensor Data with Event Loop")
print("-"*70)

class SensorEventLoop:
    """Simulates a sensor reading loop."""

    def __init__(self):
        self.on_reading = None
        self.on_high_temp = None

    def register_handlers(self, on_reading, on_high_temp):
        """Register callbacks."""
        self.on_reading = on_reading
        self.on_high_temp = on_high_temp

    def read_sensor(self):
        """Simulate reading a sensor."""
        import random
        return round(random.uniform(20, 30), 2)

    def run(self):
        """Run the sensor loop."""
        print("\n  Starting sensor event loop...")

        for i in range(3):
            # Read sensor (generate event)
            temperature = self.read_sensor()

            # Emit event - call appropriate callback
            if self.on_reading:
                self.on_reading(temperature)

            if temperature > 27 and self.on_high_temp:
                self.on_high_temp(temperature)

            time.sleep(0.5)  # Simulate delay between readings

        print("  Sensor loop finished")


def handle_reading(temp):
    """Callback: handle normal reading."""
    print(f"    📊 Reading: {temp}°C")


def handle_high_temp(temp):
    """Callback: handle high temperature."""
    print(f"    ⚠️  High temp alert: {temp}°C")


sensor_loop = SensorEventLoop()
sensor_loop.register_handlers(handle_reading, handle_high_temp)
sensor_loop.run()

# ============================================================================
# EVENT LOOP WITH MULTIPLE EVENTS
# ============================================================================

print("\n" + "-"*70)
print("Example 5: Multiple Events per Loop Iteration")
print("-"*70)

class IOTDevice:
    """Simulates an IoT device with multiple event sources."""

    def __init__(self):
        self.on_connect = None
        self.on_message = None
        self.on_disconnect = None
        self.connected = False
        self.message_queue = []

    def simulate_connect(self):
        """Simulate connection event."""
        self.connected = True
        if self.on_connect:
            self.on_connect()

    def simulate_message(self, msg):
        """Simulate receiving a message."""
        self.message_queue.append(msg)

    def simulate_disconnect(self):
        """Simulate disconnection event."""
        self.connected = False
        if self.on_disconnect:
            self.on_disconnect()

    def loop_once(self):
        """One iteration of the event loop."""
        # Check for messages
        if self.message_queue and self.on_message:
            msg = self.message_queue.pop(0)
            self.on_message(msg)


print("\n  Running IoT device loop:")

device = IOTDevice()

# Register handlers
device.on_connect = lambda: print("    ✓ Connected")
device.on_message = lambda msg: print(f"    📨 Message: {msg}")
device.on_disconnect = lambda: print("    ✗ Disconnected")

# Simulate events
device.simulate_connect()
device.simulate_message("Temperature: 25.5°C")
device.simulate_message("Humidity: 60%")
device.loop_once()
device.loop_once()
device.simulate_disconnect()

# ============================================================================
# WHY EVENT LOOPS?
# ============================================================================

print("\n" + "-"*70)
print("Why Event Loops?")
print("-"*70)

print("""
✓ RESPONSIVE: Instantly react to events (messages, connections)
✓ EFFICIENT: Don't waste CPU checking for events constantly
✓ SIMPLE: Linear flow - event happens, callback runs
✓ SCALABLE: Handle thousands of events with one loop
✓ REAL-TIME: Perfect for IoT where timing matters

EVENT LOOP PATTERN:
1. Initialize system
2. Register event handlers (callbacks)
3. Enter loop
4. Loop continuously:
   - Check for events
   - Call appropriate callbacks
   - Sleep briefly to save CPU
5. Exit loop when done
""")

# ============================================================================
# MQTT CLIENT.LOOP VARIATIONS
# ============================================================================

print("\n" + "-"*70)
print("MQTT Loop Variations in Your Project")
print("-"*70)

print("""
In your sensor_mqtt_publisher.py:

    while True:
        client.loop(timeout=0.1)    # Process for 100ms

        if time.time() - last_publish >= INTERVAL_SECONDS:
            # Read sensor and publish
            reading = generate_reading()
            client.publish(MQTT_TOPIC, payload)
            last_publish = time.time()

This is called a POLLING EVENT LOOP:
- Calls client.loop() to process MQTT events
- Does your own work (read sensor, publish)
- Repeats

Alternative (blocking loop):
    def on_message(client, userdata, msg):
        # Handle message
        print(msg.payload)

    client.on_message = on_message
    client.loop_forever()  # Runs forever, calls on_message when needed

Both are event loops - one gives you control, one is simpler.
""")

print("\n" + "="*70)
print("EXERCISES")
print("="*70)

print("""
1. Create a simple event loop that:
   - Registers two callbacks: on_button_press, on_led_change
   - Emits events in a loop
   - Callbacks respond to events

2. Create a sensor loop that:
   - Reads temperature every 0.5 seconds
   - Calls on_reading() for normal temps
   - Calls on_high_temp() for temps > 25°C

3. Modify the IoTDevice class to:
   - Add a "battery_low" event
   - Add handler for battery_low
   - Simulate battery_low event

4. Explain the difference between:
   a) client.loop_forever()
   b) while True: client.loop(timeout=0.1)

5. Design an event loop for:
   - MQTT connection events
   - Sensor reading events
   - Error events
   - What callbacks would you need?

6. In your MQTT publisher, identify:
   - What is the event loop?
   - What events are being handled?
   - What are the callbacks?
   - Why use client.loop() instead of loop_forever()?
""")

print("\n" + "-"*70)
print("Key Takeaway")
print("-"*70)

print("""
Event loops are the FOUNDATION of event-driven systems like MQTT.

Your MQTT client IS an event loop:
1. It continuously processes network events
2. When something happens (connection, message, disconnect)
3. It calls your callback
4. Your callback handles it
5. Loop continues

This is why MQTT feels responsive and real-time!
""")
