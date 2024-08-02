from paho.mqtt import client as mqtt
import time

# Go to https://www.hivemq.com/mqtt/public-mqtt-broker/ for info.

def create_client(username, password, broker_address, clientId="client", port=8883, websocketPort=8884):
    clientId = clientId
    broker_address = broker_address
    port = port
    websocketPort = websocketPort
    username = username
    password = password
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.username_pw_set(username, password)
    client.tls_set()
    client.connect(broker_address, port)
    return client

def pub(client, topic, message):
    client.publish(topic, message)

# ~~~   your code starts here   ~~~

# Create client
client = create_client("testPublisher1", "Htil2024ExamplePassword", "ac468314de194d56906aa94b21f74655.s1.eu.hivemq.cloud")

# Publish a counter message every 0.01 seconds
counter = 0
while True:
    pub(client, "htil/test/topic", counter)
    print(f"Published message {counter}")
    counter += 1
    time.sleep(0.01)

# Loop
client.loop_forever()