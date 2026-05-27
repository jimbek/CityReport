# Set up a Python 3.14 environment
FROM python:3.14-slim

# Define the working directory inside the container
WORKDIR /app

# Copy the necessary application files
COPY /lib /app/lib
COPY /pages /app/pages
COPY /services /app/services

COPY admin.py /app/admin.py

# Install streamlit
RUN pip install streamlit==1.57.0