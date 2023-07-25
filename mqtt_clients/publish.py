import paho.mqtt.client as mqtt
import time, datetime, json
import random as r

# MQTT information
# convert these to env variables
hostname = "test.mosquitto.org"
PORT = 1883
topic = "SYS_TEST/iotarray_SYS"

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
            [{
                "device_code": "iot1lgcswi1",
                "device_code": "logic_switch",
                "reading": r.randint(0, 1),
                "datetime": str(datetime.datetime.now()),
            },
            {
                "device_code": "iot2lgcswi2",
                "device_code": "logic_switch",
                "reading": r.randint(0, 1),
                "datetime": str(datetime.datetime.now()),
            },
            {
                "device_code": "iot3lgtsnsr1",
                "device_code": "light_sensor",
                "reading": r.uniform(3.5, 5.0),
                "datetime": str(datetime.datetime.now()),
            },
            {
                "device_code": "iot4lgtsnsr2",
                "device_code": "light_sensor",
                "reading": r.uniform(0.3, 5.0),
                "datetime": str(datetime.datetime.now()),
            }]
        )
        client.publish(topic, data)
        print(f"Sent: {data}")
        time.sleep(1)  # Change the delay as per your requirement

except KeyboardInterrupt:
    print("Disconnecting from the broker...")
    # Disconnect from the broker when the program is interrupted (Ctrl+C)
    client.disconnect()
    client.loop_stop()
