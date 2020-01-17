import paho.mqtt.client as mqtt
import time
import cv2
import ibm_boto3
from ibm_botocore.client import Config, ClientError

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


def create_text_file(bucket_name, item_name, file_text):
    print("Creating new item: {0}".format(item_name))
    try:
        cos.Object(bucket_name, item_name).put(
            Body=file_text
        )
        print("Item: {0} created!".format(item_name))
    except ClientError as be:
        print("CLIENT ERROR: {0}\n".format(be))
    except Exception as e:
        print("Unable to create text file: {0}".format(e))


local_client = mqtt.Client()

local_client.on_connect = on_connect
local_client.on_message = on_message
local_client.connect(MQTT_HOST, MQTT_PORT, 60)

# Create resource
#cos = ibm_boto3.resource("s3",
#    ibm_api_key_id=COS_API_KEY_ID,
#    ibm_service_instance_id=COS_RESOURCE_CRN,
#    ibm_auth_endpoint=COS_AUTH_ENDPOINT,
#    config=Config(signature_version="oauth"),
#    endpoint_url=COS_ENDPOINT
#)

#go into a loop
client.loop_forever()
