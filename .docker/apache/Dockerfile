# Use an official Apache image as a base
FROM httpd:2.4

# Copy your website into Apache's default directory
COPY ./tests/index.html /usr/local/apache2/htdocs/

# Copy the custom Apache configuration file into the container
COPY ./apache/apache-config.conf /usr/local/apache2/conf/extra/apache-config.conf

# Include the custom configuration in the main Apache config
RUN echo "Include /usr/local/apache2/conf/extra/apache-config.conf" >> /usr/local/apache2/conf/httpd.conf

# Expose the default port for Apache
EXPOSE 80
