# libraries
import paho.mqtt.client as mqtt
import pymongo
import json

# env variables
broker_address = "test.mosquitto.org"
port = 1883
topic = "test/tool1"
mongo_conn_str = (
    "mongodb+srv://kennethr:jldWyszwZi8bRtsN@data-main.ubaxa5i.mongodb.net/data_main"
)

# create mongoclient
mongo_client = pymongo.MongoClient(mongo_conn_str).get_database("mqtt").RawSignals
data = []


# Functions
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to the MQTT broker")
        client.subscribe(topic)
    else:
        print(f"Failed to connect. Return code: {rc}")


def on_message(client, userdata, msg):
    new_data = msg.payload.decode()
    print(f"Received message: {new_data}")
    data.append(json.loads(new_data))


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
    client.disconnect()
    if len(data) > 0:
        print("Writing to mongodb")
        mongo_client.insert_many(data)
        print(f"Inserted {len(data)} records.")

    client.loop_stop()
