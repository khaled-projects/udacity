# Use a slim version of Python as the base image
FROM python:3.10-slim-buster
# Set environment variables
ENV DB_USERNAME=myuser
ENV DB_PASSWORD=${POSTGRES_PASSWORD}
ENV DB_HOST=127.0.0.1
ENV DB_PORT=5432
ENV DB_NAME=mydatabase

# Update package lists and install required packages
RUN apt-get update -y && \
    apt-get install -y build-essential libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Update Python modules
RUN pip install --upgrade pip setuptools wheel

# Set the working directory in the container
WORKDIR /analytics

# Copy the application code to the container
COPY . .

# Install any dependencies needed for your application
RUN pip install -r requirements.txt

# Run your Python application
CMD ["python", "app.py"]
