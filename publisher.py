from paho.mqtt import client as mqtt

# Go to https://www.hivemq.com/mqtt/public-mqtt-broker/ for info.

clientId = "Publisher"
broker_address = "broker.hivemq.com" # The address of the broker. If using online, use a URL. If hosting yourself, use an IP address.
port = 1883 # Default MQTT port
websocketPort = 8000 # The port you should use if you want to incorporate websockets

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, clientId)
client.connect(broker_address, port)

# Publish to a topic
topic = "test/myTopic"
message = "Hello, this is Wes!"
client.publish(topic, message)
print(f"Published message {message} to topic {topic}")
client.publish(topic, message)
print(f"Published message {message} to topic {topic}")
client.publish(topic, message)
print(f"Published message {message} to topic {topic}")

client.loop_forever()