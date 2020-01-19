import os
import paho.mqtt.client as mqtt
import time
import logging
import cv2
from bucket_writer import upload_large_file
import uuid
from PIL import Image

logger_mqtt = logging.getLogger()

LOCAL_MQTT_HOST="receiver"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="face_cutter/camera_broker1"


def on_connect(client, userdata, flags, rc):
    print("Connected to receiver")
    
    logger_mqtt.warning("connected to local broker with rc: " + str(rc))
    client.subscribe(LOCAL_MQTT_TOPIC)


def on_message(client, userdata, msg):
    try:
	print("message received!")
        logger_mqtt.warning("message received!")
        
	picture = Image.frombytes('RGBA', (128,128), msg.payload, 'raw')
        filename = "./picture_dump/" +  uuid.uuid4() + '.jpg'
        print("picture decoded")


        picture.save(filename),
        print("picture saved in temp")

        time.sleep(1)
        
        upload_large_file("tennisonyu-w251-hw3", picture, filename)
        print("picture uploaded")

        time.sleep(1)

        os.remove(filename)
        print("picture deleted")

    except:
	logger_mqtt.warning("Unexpected error:", sys.exec_info()[0])


local_client = mqtt.Client()

local_client.on_connect = on_connect
local_client.on_message = on_message

local_client.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)

local_client.loop_forever()
