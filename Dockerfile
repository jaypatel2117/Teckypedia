# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the entire current directory into the container's working directory
COPY . .

# Expose port 5000 to allow communication to the Flask application
EXPOSE 5000

# Specify the command to run the Flask application
CMD ["python", "app.py"]
