import paho.mqtt.client as mqtt
import time
import logging


logger_mqtt = logging.getLogger()
LOCAL_MQTT_HOST="broker"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="face_cutter/camera-broker1"


def on_connect(client, userdata, flags, rc):
    logger_mqtt.warning("connected to local broker with rc: " + str(rc))
    client.subscribe(LOCAL_MQTT_TOPIC)


def on_message(client, userdata, msg):
    try:
        logger_mqtt.warning("message received!")	
        
        #if we wanted to re-publish this message, something like this should work
        msg = msg.payload
        remote_client.publish(REMOTE_MQTT_TOPIC, payload=msg, qos=0, retain=False)
    except:
        logger_mqtt.warning("Unexpected error:", sys.exc_info()[0])


def on_publish(client, userdata, mid):
    logger_mqtt.warning("Picture Sent to Instance Broker")


local_client = mqtt.Client()

local_client.on_connect = on_connect
local_client.on_message = on_message
local_client.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)