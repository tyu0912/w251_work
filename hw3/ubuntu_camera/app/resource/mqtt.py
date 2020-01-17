import paho.mqtt.client as mqtt

MQTT_HOST="127.0.0.1"
MQTT_PORT=1883
MQTT_TOPIC="picture_2_broker"

client = mqtt.Client()

def on_connect_jtx2_broker(client, userdata, flags, rc):
    print("connected to local broker with rc: " + str(rc))
    client.subscribe(MQTT_TOPIC)


def on_publish_jtx2_broker(client, userdata, mid):
    print("Picture Sent to Jetson Broker")

client.on_connect = on_connect_jtx2_broker
client.on_publish = on_publish_jtx2_broker

client.connect(MQTT_HOST, MQTT_PORT, 60)