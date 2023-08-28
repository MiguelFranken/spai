#!/bin/bash

# Source secrets
source secrets.env

# An array of your service names
SERVICES=("smart-personas-review-generator" "smart-personas-frontend" "smart-personas-accessibility-reporter")

# Corresponding environment variable names for each service's deploy hook
DEPLOY_HOOK_VARS=("DEPLOY_HOOK_REVIEW_GENERATOR" "DEPLOY_HOOK_FRONTEND" "DEPLOY_HOOK_ACCESSIBILITY_REPORTER")

# Login to Docker Hub
docker login

# Enable Docker BuildKit
export DOCKER_BUILDKIT=1

# Iterate over each service name
for i in "${!SERVICES[@]}"; do
    SERVICE=${SERVICES[$i]}

    # Build the Docker image with BuildKit and specific platform
    docker build --platform=linux/amd64 -t $DOCKER_USERNAME/$SERVICE:latest ./services/$SERVICE

    # Push the Docker image to Docker Hub
    docker push $DOCKER_USERNAME/$SERVICE:latest

    # Trigger the deploy hook using curl
    DEPLOY_HOOK_VAR_NAME=${DEPLOY_HOOK_VARS[$i]}
    DEPLOY_HOOK_URL=${!DEPLOY_HOOK_VAR_NAME}
    curl -X GET "$DEPLOY_HOOK_URL"
done
