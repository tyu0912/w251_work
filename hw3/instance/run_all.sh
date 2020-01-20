# Remove old network and clean any missed objects
docker network kill my-network
docker system prune -f 

# Create new network
docker network create --driver bridge my-network

# Run all the scripts
bash run_receiver.sh
bash run_decoder.sh