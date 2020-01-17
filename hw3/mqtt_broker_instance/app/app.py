import paho.mqtt.client as mqtt
import time



def on_connect(client, userdata, flags, rc):
    print("connected to local broker with rc: " + str(rc))
    client.subscribe(MQTT_TOPIC)


def on_message(client, userdata, msg):
    try:
        print("message received!")	
        
        #if we wanted to re-publish this message, something like this should work
        msg = msg.payload
    

    except:
        print("Unexpected error:", sys.exc_info()[0])


def on_publish(client, userdata, mid):
    print("Picture Sent to Instance Broker")


local_client = mqtt.Client()

local_client.on_connect = on_connect
local_client.on_message = on_message
local_client.connect(MQTT_HOST, MQTT_PORT, 60)


#go into a loop
client.loop_forever()
