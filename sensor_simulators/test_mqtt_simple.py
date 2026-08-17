
import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print(f"Connected with code {rc}")

def on_disconnect(client, userdata, rc):
    print(f"Disconnected with code {rc}")

client = mqtt.Client(client_id="test-simple")
client.on_connect = on_connect
client.on_disconnect = on_disconnect

print("Connecting...")
client.connect("localhost", 1883, keepalive=60)

print("Running loop for 10 seconds...")
for i in range(100):
    client.loop(timeout=0.1)
    time.sleep(0.1)
    if i % 10 == 0:
        print(f"  Still connected... ({i})")

client.disconnect()
print("Done")
