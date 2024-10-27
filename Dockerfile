

# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Ensure we run as root
USER root

# Set the working directory in the container
WORKDIR /app

# Upgrade pip to the latest version
RUN python -m pip install --upgrade pip

# Copy requirements.txt and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application code into the container
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Environment variables for Python optimizations
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


# Define environment variable
ENV FLASK_APP=your_flask_app_name.py  


# run the application
CMD ["python", "ui_service_main.py"]


######################



