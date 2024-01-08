#!/usr/bin/python3
"""AirBNB Flask API"""
from api.v1.views import app_views
from flask import Flask, make_response, jsonify
from models import storage
from os import getenv


host = getenv('HBNB_API_HOST', '0.0.0.0'),
port = getenv('HBNB_API_PORT', 5000)

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """close storage session."""
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    """Handler for 404 error."""
    error_resp = {
        "error": "Not found"
    }

    return make_response(jsonify(error_resp), 404)


if __name__ == '__main__':
    app.run(host=host, port=port, threaded=True)
