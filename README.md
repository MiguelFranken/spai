# Smart Personas AI

## Overview
This repository contains the Docker configuration for deploying the Smart-Personas microservices. Traefik is used as a reverse proxy to route traffic to appropriate services. Each microservice has its own Docker container for modularity and scalability.

## Directory Structure

- `/`: Root directory contains the main `docker-compose.yml` which orchestrates all services.
- `/static`: Directory containing static files, like the `hosts.txt` for Gasmask.
- `/projects`: This directory contains individual microservices. Each sub-directory represents a specific microservice.

## Prerequisites

- Docker and Docker Compose installed
- Gasmask (for managing local domain routing)

## Setting Up

1. **Clone the Repository**:
    ```bash
    git clone [your-repository-url] && cd docker
    ```

2. **Build the Microservices**:
   From the root directory, use the provided Makefile:
    ```bash
    make build-all
    ```

3. **Set Up Local Domain Routing with Gasmask**:
    - Open Gasmask
    - Create a remote host file
    - Enter `http://localhost:9999/hosts.txt`
    - Rename the new host file to `smart-personas`
    - Activate the host file (ensure other host files are deactivated)

4. **Start the Services**:
   From the root directory:
    ```bash
    make run
    ```

## Testing

Once everything is up and running, you can test the `smart-personas-review-generator` service by accessing:
```
http://review-generator.local
```

## Viewing Logs

To view logs for a specific service, navigate to its directory under `/projects` and use the Makefile provided:
```bash
make logs
```
