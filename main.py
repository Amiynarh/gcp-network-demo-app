#!/usr/bin/env python3
"""
GCP Network Reliability Demo Backend
A simple Flask application with health check endpoint
"""

from flask import Flask
import socket

app = Flask(__name__)

# Get the hostname once at startup
HOSTNAME = socket.gethostname()


@app.route('/')
def index():
    """Root endpoint that displays a welcome message with the instance hostname"""
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>GCP Network Demo</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background-color: #f0f0f0;
            }}
            .container {{
                text-align: center;
                padding: 40px;
                background-color: white;
                border-radius: 10px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }}
            h1 {{
                color: #4285f4;
            }}
            .hostname {{
                color: #34a853;
                font-weight: bold;
                font-size: 1.2em;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Hello from the GCP Network Reliability Demo Backend!</h1>
            <p>Instance Name: <span class="hostname">{HOSTNAME}</span></p>
        </div>
    </body>
    </html>
    '''


@app.route('/healthz')
def healthz():
    """Health check endpoint for load balancer"""
    return 'Healthy', 200


if __name__ == '__main__':
    # Run on port 80 with host 0.0.0.0 to accept connections from any interface
    app.run(host='0.0.0.0', port=80, debug=False)
