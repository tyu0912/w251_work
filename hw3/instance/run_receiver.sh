docker kill receiver
docker rm receiver

docker build -t mosquitto_receiver -f Dockerfile.mosquitto_receiver .

docker run --name receiver -p 1883:1883 --network my-network mosquitto_receiver sh -c "mosquitto -v -c receiver.conf"
