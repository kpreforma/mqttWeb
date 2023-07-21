import paho.mqtt.client as mqtt
import time, datetime, json
import random as r

# MQTT information
# convert these to env variables
hostname = "test.mosquitto.org"
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
        data = json.dumps(
            {
                "device_code": "tool1",
                "status": r.randint(0, 1),
                "datetime": str(datetime.datetime.now()),
            }
        )
        client.publish(topic, data)
        print(f"Sent: {data}")
        time.sleep(2)  # Change the delay as per your requirement

except KeyboardInterrupt:
    print("Disconnecting from the broker...")
    # Disconnect from the broker when the program is interrupted (Ctrl+C)
    client.disconnect()
    client.loop_stop()
