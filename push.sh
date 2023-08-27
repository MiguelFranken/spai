#!/bin/bash

# Set your Docker username as a variable
DOCKER_USERNAME="miguelfranken96"

# An array of your service names
SERVICES=("smart-personas-review-generator" "smart-personas-frontend" "smart-personas-accessibility-reporter")

# Login to Docker Hub
docker login

# Enable Docker BuildKit
export DOCKER_BUILDKIT=1

# Iterate over each service name
for SERVICE in "${SERVICES[@]}"; do
    # Build the Docker image with BuildKit and specific platform
    docker build --platform=linux/amd64 -t $DOCKER_USERNAME/$SERVICE:latest ./services/$SERVICE

    # Push the Docker image to Docker Hub
    docker push $DOCKER_USERNAME/$SERVICE:latest
done
