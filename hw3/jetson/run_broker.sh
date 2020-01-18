docker kill broker
docker rm broker

#docker network kill my-network
#docker system prune -f 


#docker build -t mosquitto_forwarder -f Dockerfile.mosquitto_forwarder .
docker build -t mosquitto_broker -f Dockerfile.mosquitto_broker .

#docker network create --driver bridge my-network

#docker run -it --name forwarder --network bridge -p 1883:1883 mosquitto_forwarder
docker run --name broker -p :1883 --network my-network mosquitto_broker sh -c "mosquitto -v -c /broker.conf"


#xhost+
#docker build -t camera -f Dockerfile.camera .
