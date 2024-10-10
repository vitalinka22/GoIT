# Use a base image (in this case Python 3.9)
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container's working directory
COPY . /app

# Install dependencies from the requirements.txt file
RUN pip install --no-cache-dir -r requirements.txt

# Define the default command to run the personal assistant application
CMD ["python", "main.py"]
