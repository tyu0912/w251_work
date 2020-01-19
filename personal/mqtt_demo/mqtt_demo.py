# pip install paho-mqtt
import paho.mqtt.client as mqtt
import time

#LOCAL_MQTT_HOST="mosquitto"

LOCAL_MQTT_HOST="127.0.0.1"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="test_topic"

def on_connect_local(client, userdata, flags, rc):
    print("connected to local broker with rc: " + str(rc))
    client.subscribe(LOCAL_MQTT_TOPIC)
	
def on_message(client, userdata, msg):
    try:
        print("message received!")	
        # if we wanted to re-publish this message, something like this should work
        # msg = msg.payload
        # remote_mqttclient.publish(REMOTE_MQTT_TOPIC, payload=msg, qos=0, retain=False)
    except:
        print("Unexpected error:", sys.exc_info()[0])

client = mqtt.Client()
client.on_connect = on_connect_local
client.on_message = on_message

client.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
#client.publish(LOCAL_MQTT_TOPIC,"Tennison Hiii")

#go into a loop
client.loop_forever()

