#!/bin/bash

# Run the Docker container with environment variables from the .env file
docker run -p 4000:4000 -e PORT=4000 --env-file ./.env groupes