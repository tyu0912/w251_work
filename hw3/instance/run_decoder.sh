docker kill decoder
docker rm decoder

docker build -t picture_decoder -f Dockerfile.decoder .

docker run --name decoder --network my-network  picture_decoder

