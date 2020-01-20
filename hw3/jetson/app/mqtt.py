# This file houses functions and variables 
# for the index file to do messaging via 
# mosquitto

import paho.mqtt.client as mqtt
import time

# Setting the mosquitto settings
LOCAL_MQTT_HOST="broker"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="face_cutter/camera-broker1"

# Functions for behavior handling
def on_connect(client, userdata, flags, rc):
    print("connected to local broker with rc: " + str(rc))
    client.subscribe(LOCAL_MQTT_TOPIC)


def on_publish(client, userdata, mid):
    print("Picture Sent to Broker")


# Setting up client and connecting
local_client = mqtt.Client()

local_client.on_connect = on_connect
local_client.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)