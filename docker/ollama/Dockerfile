# Setup the ollama environment.
FROM ollama/ollama:latest

# Copy the ollama model file into the container.
COPY model.sh /model.sh

# Start ollama in the background.
ENTRYPOINT ["/bin/sh", "/model.sh"]