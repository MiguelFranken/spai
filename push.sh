#!/bin/bash

# Set your Docker username as a variable
DOCKER_USERNAME="miguelfranken96"

# An array of your service names
SERVICES=("smart-personas-review-generator" "smart-personas-frontend" "smart-personas-accessibility-reporter")

# Login to Docker Hub
docker login

# Iterate over each service name
for SERVICE in "${SERVICES[@]}"; do
    # Tag the Docker image
    docker tag $SERVICE $DOCKER_USERNAME/$SERVICE:latest
    
    # Push the Docker image to Docker Hub
    docker push $DOCKER_USERNAME/$SERVICE:latest
done
