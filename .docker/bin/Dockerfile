# Base image for building Linux binary
FROM python:3.10 AS linux-builder

# Copy your application files into the container
ADD ../../. /app/

# Set the working directory inside the container
WORKDIR /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create the Linux binary
RUN pyinstaller --onefile -n csp_extractor csp_extractor/main.py

# Base image for building Windows binary
#FROM ubuntu:20.04 AS windows-builder

# Install Wine and dependencies for Windows binary compilation
#RUN dpkg --add-architecture i386 && \
#    apt update && \
#    apt install -y wine64 wine32 python3 python3-pip

# Copy your application files into the container
#ADD ../../. /app/

# Set the working directory inside the container
#WORKDIR /app

# Install Python requirements
RUN pip3 install --no-cache-dir -r requirements.txt

# Create the Windows binary using Wine
RUN #pyinstaller --onefile -n csp_extractor csp_extractor/main.py

# Final stage to collect the built binaries
FROM alpine:latest AS final-stage

WORKDIR /output

# Copy Linux binary from the linux-builder stage
COPY --from=linux-builder /app/dist/csp_extractor /output/

# Copy Windows binary from the windows-builder stage
#COPY --from=windows-builder /app/dist/csp_extractor.exe /output/

CMD ["ls", "-la", "/output"]