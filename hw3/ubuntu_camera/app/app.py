import numpy as np
import cv2
import resource.mqtt

face_cascade = cv2.CascadeClassifier('/src/app/utils/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(1)

cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))

i = 0

while 1:
    ret, img = cap.read()
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        gray = gray[y:y+h, x:x+w]

        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        img = img[y:y+h, x:x+w]

        cv2.imshow("frame", img)
        
        rc, png = cv2.imencode(".png", img)
        msg = png.tobytes()

        #with open('/src/app/pic_dump/{i}.txt'.format(i=i), 'wb') as test:
        #    test.write(msg)
        #    i += 1

        client.publish(LOCAL_MQTT_TOPIC, payload=msg, qos=0, retain=False)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()