# Define variables
PACKAGE_NAME=csp_extractor
MAIN_SCRIPT=$(PACKAGE_NAME)/main.py

# Install dependencies
install:
	pip install -r requirements.txt

# Run the main script
start:
	@if not defined HTML_FILE ( \
		echo. && echo ERROR: No HTML file provided! && \
		echo Usage: make start HTML_FILE=tests/test_file1.html && echo. && \
		exit /b 1 \
	) else ( \
		python -m $(PACKAGE_NAME).main $(HTML_FILE) \
	)

# Build the Docker image
docker-build:
	docker build -t my-apache-test .

# Run the Docker container
docker-run:
	docker run -dit --name my-apache-server -p 8080:80 my-apache-test

# Stop and remove the Docker container
docker-clean:
	docker stop my-apache-server
	docker rm my-apache-server


# Build binary using PyInstaller
build-binary:
	pyinstaller --onefile $(MAIN_SCRIPT)
