import numpy as np
import cv2

# Getting the face detection xml. This file is found directly in the cv2 (opencv) github repo
# face_cascade = cv2.CascadeClassifier('/src/haarcascade_frontalface_default.xml')

# Grabbing the video capture methods. Note, 0 worked for me instead of 1.
try:
    cap = cv2.VideoCapture(0)
except:
    cap = cv2.VideoCapture(1)
    
#cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))

print("Detecting Pics")

while 1:
    # Detecting and processing pics
    ret, img = cap.read()
    
    cv2.imshow("frame", img)
        
    # Loop breaking parameter
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

# Pause time
time.sleep(1) 
        
# Stop and clean-up
cap.release()
cv2.destiroyAllWindows()
