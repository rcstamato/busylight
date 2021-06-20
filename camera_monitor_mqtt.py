#!/Users/ricardostamato/miniconda3/bin/python

import time
import subprocess
import select
import paho.mqtt.client as mqtt

# The callback for when the mqtt client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully")
    else:
        print("Connect returned result code: " + str(rc))

# create and config mqtt client
client = mqtt.Client()
client.on_connect = on_connect

# enable TLS
client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)

# set username and password
client.username_pw_set("busylight", "Passw0rd")

# connect to HiveMQ Cloud on port 8883
client.connect("b5a503092762466cb301345286096f43.s1.eu.hivemq.cloud", 8883)

# Command to check if camera is on
cmd = '/usr/bin/log stream'
f = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
p = select.poll()
p.register(f.stdout)

while True:
    if p.poll():
        line = f.stdout.readline()
        if 'Streaming on event kCameraStreamStart' in str(line):
            client.publish("busylight/stamato", "ON", retain=True)
            print('Published ON event')
        elif 'Init on event kCameraStreamStop' in str(line):
            client.publish("busylight/stamato", "OFF", retain=True)
            print('Published OFF event')
