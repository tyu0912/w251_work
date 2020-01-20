docker network kill my-network
docker system prune -f 

docker network create --driver bridge my-network

bash run_receiver.sh
bash run_decoder.sh