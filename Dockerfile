# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 4000

# Define environment variable
ENV API_KEY "AIRTABLE"

# Run app.py when the container launches
CMD streamlit run --server.port $PORT app.py