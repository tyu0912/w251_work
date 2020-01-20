import os
import paho.mqtt.client as mqtt
import time
import logging
import cv2
from bucket_writer import upload_large_file
import uuid
from PIL import Image
import numpy as np

# Setting the mosquitto settings
LOCAL_MQTT_HOST="receiver"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="face_cutter/camera-broker1"


# Setting behavior functions 
def on_connect(client, userdata, flags, rc):
    print("connected to receiver with rc: " + str(rc))
    client.subscribe(LOCAL_MQTT_TOPIC)


def on_message(client, userdata, msg):
    try:
	    print("message received. Decoding...")

        # Decoding the pic
	    decode = np.frombuffer(msg.payload, dtype=np.uint8)
        picture = cv2.imdecode(decode, flags=1)
        
        # Saving the pic in temp
        theid = str(uuid.uuid4()) + '.png'
        filename = "/src/picture_dump/" +  theid
        cv2.imwrite(filename, picture)
        
        # Uploading the pic
        upload_large_file("tennisonyu-w251-hw3", theid, filename)
        
        time.sleep(1)
        
        # Deleting the pic in temp
        os.remove(filename)
        print("Picture uploaded and removed from temp")

    except:
        print("Didn't work:", sys.exec_info()[0])


# Connecting to mosquitto client and keeping the service open.
local_client = mqtt.Client()

local_client.on_connect = on_connect
local_client.on_message = on_message

local_client.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)

local_client.loop_forever()
