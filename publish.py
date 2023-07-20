import paho.mqtt.client as mqtt
import time

# MQTT information
hostname = "localhost"
PORT = 1883
topic = "test/tool1"

# Create a MQTT client
client = mqtt.Client("sender")

# Callback functions
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to the MQTT broker")
    else:
        print(f"Failed to connect. Return code: {rc}")

def on_publish(client, userdata, mid):
    print("Message published")

# Set the callback functions
client.on_connect = on_connect
client.on_publish = on_publish

# Connect to the broker
client.connect(hostname)

# Start the MQTT loop
client.loop_start()

try:
    while True:
        # Generate some data to send
        data = "Hello, MQTT!"  # Replace with your own data to be sent

        # Publish the data to the specified topic
        client.publish(topic, data)

        # Print the sent data for demonstration purposes
        print(f"Sent: {data}")

        # Wait for a short duration before publishing the next message
        time.sleep(5)  # Change the delay as per your requirement

except KeyboardInterrupt:
    print("Disconnecting from the broker...")
    # Disconnect from the broker when the program is interrupted (Ctrl+C)
    client.disconnect()
    client.loop_stop()
