DOCKER_FILE_PATH=./ci/build/Dockerfile
DOCKER_COMPOSE_FILE_PATH=./ci/build/docker-compose.yml
DOCKER_IMAGE_NAME=simple_file_storage_api_image
DOCKER_CONTAINER_NAME=simple_file_storage_api_container


build:
	@echo "Building the application..."
	@docker build -t $(DOCKER_IMAGE_NAME) -f $(DOCKER_FILE_PATH) .

logs:
	@echo "Showing the application logs..."
	@docker-compose -f $(DOCKER_COMPOSE_FILE_PATH) logs

run:
	@echo "Running the application..."
	@docker-compose -f $(DOCKER_COMPOSE_FILE_PATH) up

stop:
	@echo "Stopping the application..."
	@docker-compose -f $(DOCKER_COMPOSE_FILE_PATH) down

clean:
	@echo "Cleaning the application..."
	@docker rmi -f $(DOCKER_IMAGE_NAME)
	@docker rm -f $(DOCKER_CONTAINER_NAME)

all: build run logs