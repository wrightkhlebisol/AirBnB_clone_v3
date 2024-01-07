#!/usr/bin/python3
"""AirBNB Flask API"""
from flask import Flask
from models import storage
from os import getenv


host = getenv('HBNB_API_HOST', '0.0.0.0'),
port = getenv('HBNB_API_PORT', 5000)

app = Flask(__name__)

@app.route('/api/v1/status')
def status():
    return {
        "status": "OK"
    }


if __name__ == '__main__':
    app.run(host, port)



