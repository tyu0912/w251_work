import numpy as np
import cv2
import time

# Getting the face detection xml. This file is found directly in the cv2 (opencv) github repo
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Grabbing the video capture methods. Note, 0 worked for me instead of 1.
cap = cv2.VideoCapture(0)
    
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))

print("Detecting Pics")
start = time.time()
counter = 1

while 1:
    # Detecting and processing pics
    ret, img = cap.read()
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:

        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        img = img[y:y+h, x:x+w]

    
    counter += 1
    print("Frame Rate: " + str(counter/(time.time() - start)))

    cv2.imshow("frame", img)

    # Loop breaking parameter
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

# Pause time
time.sleep(1) 
        
# Stop and clean-up
cap.release()
cv2.destroyAllWindows()
