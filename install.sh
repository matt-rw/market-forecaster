#!/usr/bin/bash

# Install Docker and Docker Compose
sudo apt update
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common
## Install the official GPG key for Docker
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
## Add Docker repository
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
## Update package list
sudo apt update
## Install Docker Engine
sudo apt install -y docker-ce docker-ce-cli containerd.io
## Optional: Verify Docker installed correctly: sudo docker run hello-world
## Install Docker Compose v2 as a plugin
sudo apt install -y docker-compose-plugin
## Verify docker compose installed correctly
docker compose version
## Allow running Docker without sudo
sudo usermod -aG docker $USER
## Log back in for changes to apply (or run `newgrp docker`)



