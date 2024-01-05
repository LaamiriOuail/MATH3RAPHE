# Use a base image with Python and PyQt5 dependencies
FROM python:3

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application directory into the container
COPY . .

# Specify the command to run your PyQt5 application
CMD ["python", "controller/manager.py"]
