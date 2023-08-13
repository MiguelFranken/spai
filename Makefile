.PHONY: build-all run stop

# Iterate over subdirectories in the projects directory and build each Docker image
build-all:
	@for dir in projects/*; do \
		if [ -d "$$dir" ]; then \
			echo "Building Docker image for microservice in $$dir..."; \
			docker build -t $$(basename $$dir) -f $$dir/Dockerfile $$dir; \
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