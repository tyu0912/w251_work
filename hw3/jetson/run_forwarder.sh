# Clean up older runs
docker kill forwarder
docker rm forwarder

# Build new from respective Dockerfile and config file
docker build -t mosquitto_forwarder -f Dockerfile.mosquitto_forwarder .
docker run --name forwarder --network my-network mosquitto_forwarder sh -c "mosquitto -v -c /forwarder.conf"

# The below are the config settings:
#
# connection bridge-01
# topic face_cutter/camera-broker1 both 0
# address 169.53.129.167:1883
#
# where connection is the name for the new bridge, topic is two way 
# (though QoS is 0 and we don't expect messages to come back). 
# These two variables can be tuned in the future if needed.
# The address points to the instance IP with the port of 1883
# for the receiving broker.