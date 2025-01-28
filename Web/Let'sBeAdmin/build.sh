#!/bin/sh
IMAGE_NAME="lets-be-admin"
CONTAINER_NAME="lets-be-admin"

# Build the Docker image
docker build -t ${IMAGE_NAME} .

# Check if the container is already running
if docker ps | grep -q "${CONTAINER_NAME}"; then
    echo "Container ${CONTAINER_NAME} is running. Stopping and removing it..."
    # Stop the running container
    docker stop ${CONTAINER_NAME}
    # Remove the stopped container
    docker rm ${CONTAINER_NAME}
    echo "Container ${CONTAINER_NAME} has been stopped and removed."
fi

# Start a new container from the built image
echo "Starting a new container from the ${IMAGE_NAME} image..."
docker run -d --name ${CONTAINER_NAME} -p 62233:62233 ${IMAGE_NAME}

echo "Container ${CONTAINER_NAME} started successfully."