import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully")
    else:
        print("Connect returned result code: " + str(rc))

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("Received message: " + msg.topic + " -> " + msg.payload.decode("utf-8"))

# create the client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# enable TLS
client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)

# set username and password
client.username_pw_set("busylight", "Passw0rd")

# connect to HiveMQ Cloud on port 8883
client.connect("b5a503092762466cb301345286096f43.s1.eu.hivemq.cloud", 8883)

# subscribe to the topic
client.subscribe("busylight/stamato")

# Blocking call that processes network traffic, dispatches callbacks and handles reconnecting.
client.loop_forever()