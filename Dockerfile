#This is a test Dockerfile to test the Cycode scan feature for CI/CD Security

# Bad Dockerfile with potentially problematic configurations

# Use a non-slim base image for better compatibility, but this could increase image size
FROM ubuntu:latest

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies with apt-get, combining multiple packages in one line, which can be risky
RUN apt-get update && apt-get install -y \
    openssl \
    bash \
    curl \
    nginx \
    nodejs \
 && rm -rf /var/lib/apt/lists/*

# Expose port 80 to allow outside access to our application
EXPOSE 80

# Use a non-root user to improve security, but it might not be properly configured
USER nobody

# Set environment variables
ENV ENVIRONMENT=production

# Run nginx as the main command, but no configuration or error handling is provided
CMD ["nginx"]

# Notes:
# 1. Using the latest tag for the base image might lead to unpredictability and potential compatibility issues.
# 2. Combining multiple package installations in a single RUN instruction can make it difficult to debug and troubleshoot.
# 3. Running services as a non-root user can improve security, but it requires proper configuration and may not work as intended in all scenarios.
# 4. Not providing proper error handling or configuration for the main command (CMD) can lead to unexpected behavior during container startup.

