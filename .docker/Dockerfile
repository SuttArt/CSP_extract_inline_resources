# Stage 1: Build the binary using Python
FROM python:3.10 AS binary-builder

# Copy your application files into the container
ADD .. /app/

# Set the working directory inside the container
WORKDIR /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Build the binary with PyInstaller
RUN pyinstaller --onefile -n csp_extractor csp_extractor/main.py

# Stage 2: Run the binary to generate the web files
FROM binary-builder AS file-generator

# Run the binary to process the HTML file and generate www_dist
WORKDIR /app
RUN ./dist/csp_extractor ./tests/index.html

# Stage 3: Set up Apache and serve the generated files
FROM httpd:2.4

# Copy the generated web files from the previous stage
COPY --from=file-generator /app/www_dist/ /usr/local/apache2/htdocs/

# Copy the custom Apache configuration file into the container
COPY ./apache/apache-config.conf /usr/local/apache2/conf/extra/apache-config.conf

# Include the custom configuration in the main Apache config
RUN echo "Include /usr/local/apache2/conf/extra/apache-config.conf" >> /usr/local/apache2/conf/httpd.conf

# Expose the default port for Apache
EXPOSE 80

# Start Apache in the foreground
CMD ["httpd-foreground"]