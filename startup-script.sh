#!/bin/bash
# Install necessary packages
apt-get update
apt-get install -y python3-pip git
# Clone the application repository
# IMPORTANT: Replace [YOUR_REPO_URL] with the actual URL where you host the code.
git clone https://github.com/Amiynarh/gcp-network-demo-app /opt/app
# Navigate to the app directory
cd /opt/app
# Install Python dependencies
pip3 install -r requirements.txt
# Run the application using nohup/screen/supervisor, we'll use a simple nohup for this demo
# The application runs in the background and redirects output to /var/log/app.log
# Note: For production, use a proper service manager like systemd or supervisor.
nohup python3 main.py > /var/log/app.log 2>&1 &