import paho.mqtt.client as mqtt
import time


def on_connect(client, userdata, flags, rc):
    print("connected to local broker with rc: " + str(rc))
    client.subscribe(LOCAL_MQTT_TOPIC)


def on_message(client, userdata, msg):
    try:
        print("message received!")	
        
        #if we wanted to re-publish this message, something like this should work
        msg = msg.payload
        remote_client.publish(REMOTE_MQTT_TOPIC, payload=msg, qos=0, retain=False)
    except:
        print("Unexpected error:", sys.exc_info()[0])


def on_publish(client, userdata, mid):
    print("Picture Sent to Instance Broker")


local_client = mqtt.Client()

local_client.on_connect = on_connect
local_client.on_message = on_message
local_client.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)


remote_client = mqtt.Client()

remote_client.on_publish = on_publish
remote_client.connect(REMOTE_MQTT_HOST, REMOTE_MQTT_PORT, 60)


#go into a loop
client.loop_forever()