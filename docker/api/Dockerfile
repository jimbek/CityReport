# Set up a Python 3.14 environment
FROM python:3.14-slim

# Define the working directory inside the container
WORKDIR /app

# Copy the necessary application files
COPY /lib /app/lib
COPY /routes /app/routes

COPY api.py /app/api.py

# Install flask
RUN pip install Flask==3.1.3