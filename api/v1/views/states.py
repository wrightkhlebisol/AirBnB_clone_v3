#!/usr/bin/python3
"""State Blueprint"""
from flask import jsonify, request
from api.v1.views import app_views


@app_views.route('/states', methods=['GET', 'POST'])
def states():
    """Get list of all state"""
    print(request.method)
    states = storage.all().to_dict()

    return make_response(jsonify(states))


@app_views.route('/states/<state_id>', methods=['GET', 'PUT', 'DELETE'])
def states_by_id():
    """Get list of all state"""
    print(request.method)
    states = storage.all().to_dict()

    return make_response(jsonify(states))
