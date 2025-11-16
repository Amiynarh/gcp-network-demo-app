#!/bin/bash
# Install necessary packages 
apt-get update
apt-get install -y python3-pip git python3-venv -y 
# Clone the application
git clone https://github.com/Amiynarh/gcp-network-demo-app /opt/app
cd /opt/app

# --- START VIRTUAL ENVIRONMENT  ---
# Create a venv named 'app_venv'
python3 -m venv app_venv
# Activate the venv (Source the activation script)
source app_venv/bin/activate

# Install dependencies using the VENV's pip
pip install -r requirements.txt

# Run the application using the VENV's python interpreter
nohup /opt/app/app_venv/bin/python main.py > /var/log/app.log 2>&1 &