# Smart Personas AI

## Live
Visit https://smart-personas-frontend.onrender.com/

## Overview
This repository contains the Docker configuration for deploying the Smart-Personas microservices. Traefik is used as a reverse proxy to route traffic to appropriate services. Each microservice has its own Docker container for modularity and scalability.

## Directory Structure

- `/`: Root directory contains the main `docker-compose.yml` which orchestrates all services.
- `/static`: Directory containing static files, like the `hosts.txt` for Gasmask.
- `/projects`: This directory contains individual microservices. Each sub-directory represents a specific microservice.

## Prerequisites

- Docker and Docker Compose installed
- Gasmask (for managing local domain routing)

### Deployment Prerequisites
- Secrets stored in `secrets.env` (this file is not committed due to security reasons). Use `secrets.env.example` as a template to create your own.


## Setting Up

1. **Clone the Repository**:
    ```bash
    git clone git@gitlab.dev.dwinternal.com:denkwerk/ki/spai.git && cd docker
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

Once everything is up and running, you can test the application via the `smart-personas-frontend` service by
browsing to the following website in your browser:
```
http://a11y-ai.smart-personas.local
```

## Viewing Logs

To view logs for all service, use the Makefile in the root directory:
```bash
make logs
```

To view logs for a specific service, use one of these commands:
```bash
make logs-review-generator
```

```bash
make logs-accessibility-reporter
```

```bash
make logs-frontend
```

## Build & Deploy Microservices via Render.com
First, make sure you have the `secrets.env` file set up in the root directory. Then, trigger the deployment by executing the `deploy.sh` script:
```bash
./deploy.sh
```