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

def sub(client, topic):
    client.subscribe(topic)
    client.on_message = on_message

# ~~~   your code starts here   ~~~

# Message handler
def on_message(client, userdata, message):
    print(f"Received message {message.payload.decode()} on topic {message.topic}")

# Create client
client = create_client("testPublisher1", "Htil2017", "ac468314de194d56906aa94b21f74655.s1.eu.hivemq.cloud")

# Subscribe to a topic
sub(client, "htil/test/topic")
print(f"Subscribed to topic")

# Loop
client.loop_forever()