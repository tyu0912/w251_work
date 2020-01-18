docker kill forwarder
docker rm forwarder


docker build -t mosquitto_forwarder -f Dockerfile.mosquitto_forwarder .
docker run --name forwarder --network my-network mosquitto_forwarder sh -c "mosquitto -v -c /forwarder.conf"

#docker run -ti --name forwarder --network my-network mosquitto_forwarder ping google.com