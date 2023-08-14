.PHONY: build-all run stop

# Iterate over subdirectories in the services directory and build each Docker image
build-all:
	@for dir in services/*; do \
		if [ -d "$$dir" ]; then \
			echo "Building Docker image for microservice in $$dir..."; \
			docker build --platform linux/amd64 -t $$(basename $$dir) -f $$dir/Dockerfile $$dir; \
		fi \
	done

run:
	@echo "Starting all services with Docker Compose..."
	@docker-compose up -d

stop:
	@echo "Stopping all services..."
	@docker-compose down

logs:
	@echo "Fetching logs for services..."
	@docker-compose logs -f

logs-review-generator:
	@echo "Fetching logs for review generator service..."
	@docker compose logs --tail 300 -f smart-personas-review-generator