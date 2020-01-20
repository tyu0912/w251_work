# This kills the network and cleans up anything that is lingerring
docker network kill my-network
docker system prune -f 

# Creating a new network 
docker network create --driver bridge my-network