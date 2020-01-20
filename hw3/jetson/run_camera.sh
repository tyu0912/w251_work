# Destroy previous builds
docker kill camera
docker rm camera

# Build new containers of the camera service
docker build -t camera -f Dockerfile.camera .

xhost +

docker run --name camera \
           --network my-network \
           --privileged \
           -v /tmp:/tmp \
           -v /dev/bus/usb:/dev/bus/usb \
           -e QT_X11_NO_MITSHM=1 \
           -e DISPLAY \
           camera 
