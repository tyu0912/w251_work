# HW3: Internet of Things

The task of this homework is to send pictures from the Jetson TX2 to an Object Store on IBM Cloud. The main technologies and software that were recommended and used in this project include a webcam, OpenCV, Docker, Alpine, Ubuntu, and Mosquitto. A diagram of the pipeline can be found at https://github.com/MIDS-scaling-up/v2/tree/master/week03/hw.

## 1. Jetson

On the Jetson side, there are three main parts:
1. Camera
2. Broker
3. Forwarder

Each part has its own bash script to run that will trigger its respective Dockerfile, config files, and app components. This was done to make each part more unit testable. To get everything up and running, the `run_all.sh` can be used which also sets up a user-defined bridge network for the whole thing. Per the diagram, the pictures from the camera are captured by OpenCV which will then pass on the message to a Mosquitto broker. This broker then passes the message to the forwarder which launches it to the instance for further processing. More details can be found via the line comments of each file.

## 2. Instance

On the Instance side, there are two main parts:
1. Receiver 
2. Decoder

With a similar file structure and concept as the Jetson side, the receiver is a mosquitto broker responsible for catching all the messages from the forwarder above. The decoder is registered to the receiver broker service and therefore will get the messages as well. It then takes the messages, decodes them and saves them to an Object Store Bucket on the IBM Cloud.
