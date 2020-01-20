# Importing package. Note the mqtt package which is the file also in this directory

import numpy as np
import cv2
from mqtt import *

# Getting the face detection xml. This file is found directly in the cv2 (opencv) github repo
face_cascade = cv2.CascadeClassifier('/src/haarcascade_frontalface_default.xml')

# Grabbing the video capture methods. Note, 0 worked for me instead of 1.
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))

print("Detecting Pics")

# Starts the loop for communicating to mosquitto
local_client.loop_start()

while 1:
    # Detecting and processing pics
    ret, img = cap.read()
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        gray = gray[y:y+h, x:x+w]

        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        img = img[y:y+h, x:x+w]

        # The below is to see what the output of the image looks like
        # cv2.imshow("frame", img)
        
        # Encoding the pic and sending it to the broker
        png = cv2.imencode(".png", img)[1]
        msg = bytearray(png)

        local_client.publish(LOCAL_MQTT_TOPIC, payload=msg, qos=0, retain=False)

    # Loop breaking parameter
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

# Pause time
time.sleep(1) 
        
# Stop and clean-up
local_client.loop_stop()
local_client.disconnect()
cap.release()
cv.destroyAllWindows()
