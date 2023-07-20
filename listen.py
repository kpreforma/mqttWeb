import paho.mqtt.client as mqtt

# MQTT broker information
broker_address = "localhost"
port = 1883
topic = "test/tool1"

# Callback functions
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to the MQTT broker")
        client.subscribe(topic)
    else:
        print(f"Failed to connect. Return code: {rc}")

def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()}")

# Create an MQTT client instance
client = mqtt.Client("subscriber_client")

# Set the callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the broker
client.connect(broker_address, port)

# Start the MQTT loop
client.loop_start()

try:
    # Keep the script running to continue receiving messages
    while True:
        pass

except KeyboardInterrupt:
    print("Disconnecting from the broker...")
    # Disconnect from the broker when the program is interrupted (Ctrl+C)
    client.disconnect()
    client.loop_stop()
