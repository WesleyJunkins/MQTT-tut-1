import paho.mqtt.client as mqtt

# Go to https://www.hivemq.com/mqtt/public-mqtt-broker/ for info.

def on_message(client, userdata, message):
    print(f"Received message {message.payload.decode()} on topic {message.topic}")

clientId = "Subscriber"
broker_address = "broker.hivemq.com"
port = 1883
websocketPort = 8000

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, clientId)
client.on_message = on_message
client.connect(broker_address, port)

# Subscribe to a topic
topic = "test/myTopic"
client.subscribe(topic)
print(f"Subscribed to topic {topic}")

client.loop_forever()

