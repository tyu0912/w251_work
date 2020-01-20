# Remove prior runs
docker kill receiver
docker rm receiver

# Build new containers
docker build -t mosquitto_receiver -f Dockerfile.mosquitto_receiver .
docker run --name receiver -p 1883:1883 --network my-network mosquitto_receiver sh -c "mosquitto -v -c receiver.conf"

# Note that the receiver.conf is intentionally empty
# This is because it was later realized the default settings are ok
# Still included just for consistency.