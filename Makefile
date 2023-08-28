SHELL := /bin/bash

.PHONY: default build-all run stop logs logs-review-generator logs-frontend logs-accessibility-reporter help

default: help

#########
######### === DOCKER STUFF ===

build-all: # Iterate over subdirectories in the services directory and build each Docker image
	@docker-compose build

run: # Start the docker containers defined in docker-compose.yml
	@echo "Starting all services with Docker Compose..."
	@docker-compose up -d

stop:
	@echo "Stopping all services..."
	@docker-compose down

logs: # Show and follow logs of services defined in docker-compose.yml
	@echo "Fetching logs for services..."
	@docker-compose logs -f

logs-review-generator: # Show and follow logs of review generator service
	@echo "Fetching logs for review generator service..."
	@docker compose logs --tail 300 -f smart-personas-review-generator

logs-frontend: # Show and follow logs of frontend service
	@echo "Fetching logs for frontend service..."
	@docker compose logs --tail 300 -f smart-personas-frontend

logs-accessibility-reporter: # Show and follow logs of accessibility reporter service
	@echo "Fetching logs for accessibility reporter service..."
	@docker compose logs --tail 300 -f smart-personas-accessibility-reporter

#########
######### === HELP ===

help: # Show help for this make file
	@grep -E '(^[a-zA-Z0-9 -]+.*#|^#########+(?:[a-zA-Z0-9 -]))'  Makefile | while read -r l; do printf "\033[1;32m$$(echo $$l: | sed -e 's/#########.*//g' | cut -f 1 -d':')\033[00m$$(echo $$l | sed -e 's/|n/\n/g' | cut -f 2- -d'#')\n"; done
