"""
Part 7: Callbacks

A callback is a function you pass to another function.
It says: "When X happens, call THIS function"

This is CRUCIAL for MQTT! on_connect(), on_disconnect(), etc. are callbacks.

Run: python tests/07_callbacks.py
"""

print("\n" + "="*70)
print("CALLBACKS - Functions as Parameters")
print("="*70)

# ============================================================================
# SIMPLE CALLBACK EXAMPLE
# ============================================================================

print("\n" + "-"*70)
print("Example 1: Simple Callback")
print("-"*70)

def on_high_temperature(sensor_id, temperature):
    """This is a CALLBACK - it gets called when something happens."""
    print(f"  ⚠️  ALERT: {sensor_id} temperature is {temperature}°C!")


def check_temperature(sensor_id, temperature, on_high_callback):
    """
    Check if temperature is OK.
    If too high, call the callback function.
    """
    if temperature > 27:
        on_high_callback(sensor_id, temperature)
    else:
        print(f"  ✓ {sensor_id} temperature OK: {temperature}°C")


print("\nCase 1: Temperature is normal (25°C)")
check_temperature("sensor-01", 25.0, on_high_temperature)

print("\nCase 2: Temperature is too high (28.5°C)")
check_temperature("sensor-02", 28.5, on_high_temperature)

# ============================================================================
# WHY CALLBACKS?
# ============================================================================

print("\n" + "-"*70)
print("WHY CALLBACKS?")
print("-"*70)

print("""
✓ EVENT-DRIVEN: "When X happens, do Y"
✓ FLEXIBLE: You can pass different callbacks
✓ DECOUPLED: Checker doesn't need to know about the handler
✓ MQTT USE: on_connect(), on_disconnect(), on_message()
""")

# ============================================================================
# REAL MQTT EXAMPLE
# ============================================================================

print("\n" + "-"*70)
print("Example 2: Simulating MQTT Callbacks")
print("-"*70)

def my_on_connect(client, rc):
    """This callback runs when we connect to MQTT broker."""
    if rc == 0:
        print("  ✓ Connected to MQTT broker")
    else:
        print(f"  ✗ Connection failed: code {rc}")


def my_on_disconnect(client, rc):
    """This callback runs when we disconnect from MQTT broker."""
    if rc != 0:
        print(f"  ✗ Unexpected disconnect: code {rc}")


def my_on_message(topic, message):
    """This callback runs when we receive a message."""
    print(f"  📨 Message received on {topic}: {message}")


class MockMQTTClient:
    """Simulates an MQTT client."""

    def __init__(self):
        self.on_connect = None
        self.on_disconnect = None
        self.on_message = None

    def connect(self, broker):
        """Simulate connecting to broker."""
        print(f"\nConnecting to {broker}...")
        # Simulate connection - call the callback
        if self.on_connect:
            self.on_connect(self, 0)  # 0 = success

    def disconnect(self):
        """Simulate disconnecting."""
        print("Disconnecting...")
        # Call the disconnect callback
        if self.on_disconnect:
            self.on_disconnect(self, 0)  # 0 = normal disconnect

    def receive_message(self, topic, message):
        """Simulate receiving a message."""
        # Call the message callback
        if self.on_message:
            self.on_message(topic, message)


# Create MQTT client
client = MockMQTTClient()

# Register callbacks (like in real MQTT)
client.on_connect = my_on_connect
client.on_disconnect = my_on_disconnect
client.on_message = my_on_message

# Use the client - callbacks get called automatically
client.connect("localhost:1883")
client.receive_message("sensors/temp", "25.5")
client.receive_message("sensors/humidity", "60.0")
client.disconnect()

# ============================================================================
# MULTIPLE CALLBACKS
# ============================================================================

print("\n" + "-"*70)
print("Example 3: Different Callbacks for Different Situations")
print("-"*70)

def on_danger(sensor_id, value):
    """Alert level callback."""
    print(f"  🚨 DANGER: {sensor_id} = {value}")


def on_warning(sensor_id, value):
    """Warning level callback."""
    print(f"  ⚠️  WARNING: {sensor_id} = {value}")


def on_safe(sensor_id, value):
    """Safe level callback."""
    print(f"  ✓ SAFE: {sensor_id} = {value}")


def check_sensor_level(sensor_id, value, on_danger_cb, on_warning_cb, on_safe_cb):
    """Check sensor value and call appropriate callback."""
    if value > 30:
        on_danger_cb(sensor_id, value)
    elif value > 25:
        on_warning_cb(sensor_id, value)
    else:
        on_safe_cb(sensor_id, value)


print("\nChecking sensor values:")
check_sensor_level("temp-01", 22.0, on_danger, on_warning, on_safe)
check_sensor_level("temp-02", 26.5, on_danger, on_warning, on_safe)
check_sensor_level("temp-03", 31.0, on_danger, on_warning, on_safe)

# ============================================================================
# CALLBACKS WITH OBJECTS
# ============================================================================

print("\n" + "-"*70)
print("Example 4: Callbacks with Methods")
print("-"*70)

class AlertSystem:
    """System that handles alerts."""

    def __init__(self):
        self.alerts = []

    def on_high_temp(self, sensor_id, temperature):
        """Callback: handle high temperature."""
        message = f"High temp alert: {sensor_id} = {temperature}°C"
        self.alerts.append(message)
        print(f"  Alert logged: {message}")

    def get_alert_count(self):
        """Check how many alerts."""
        return len(self.alerts)


# Create alert system
alerts = AlertSystem()

# Check temperatures, callbacks will log alerts
print("\nMonitoring temperatures:")
check_temperature("sensor-01", 25.0, alerts.on_high_temp)
check_temperature("sensor-02", 28.5, alerts.on_high_temp)
check_temperature("sensor-03", 26.0, alerts.on_high_temp)

print(f"\nTotal alerts: {alerts.get_alert_count()}")

print("\n" + "="*70)
print("EXERCISES")
print("="*70)

print("""
1. Create two callback functions:
   - on_connected()
   - on_disconnected()
   Then create a simple_device() function that:
   - Takes two callbacks as parameters
   - Calls on_connected() at start
   - Calls on_disconnected() at end

2. Create a sensor monitoring system with callbacks for:
   - on_reading_received(value)
   - on_reading_invalid(value)
   Filter based on valid range (15-35°C)

3. Create an alert system with callbacks:
   - on_critical(message)
   - on_warning(message)
   - on_info(message)
   Call appropriate callback based on alert level

4. Simulate an MQTT client like example 2:
   - Add on_publish callback
   - Add on_subscribe callback
   - Test with MockMQTTClient

5. Explain WHY callbacks are better than:
   a) Having the checker print the results directly
   b) Having the checker modify an object's state
""")
