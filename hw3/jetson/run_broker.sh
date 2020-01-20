# Clean up older runs
docker kill broker
docker rm broker

# Build new from respective Dockerfile and config file
docker build -t mosquitto_broker -f Dockerfile.mosquitto_broker .
docker run --name broker -p :1883 --network my-network mosquitto_broker sh -c "mosquitto -v -c /broker.conf"

# The below are the config settings:
#
# connection jetson
# topic face_cutter/camera-broker1
# address forwarder:1883
#
# where connection is the name for the camera broker. It is called jetson.
# The topic is as all other services to standardize the whole thing
# since the data flow is linear. The address points to the container name
# "forwarder" with its default port of 1883.