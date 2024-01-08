#!/usr/bin/python3
"""State View"""
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from models.state import State


@app_views.route('/states/', methods=['GET', 'POST'])
def states():
    """Get list of all state"""

    if request.method == 'GET':
        all_states = []
        states = storage.all(State)

        for k, v in states.items():
            all_states.append(v.to_dict())

        return make_response(jsonify(all_states))
    elif request.method == 'POST':
        return make_response(jsonify('POSTING...'))


@app_views.route('/states/<state_id>', methods=['GET', 'PUT', 'DELETE'])
def states_by_id(state_id):
    """Get state by ID"""

    if request.method == 'GET':
        states = storage.get(State, state_id)

        if states:
            return make_response(jsonify(states.to_dict()))
        else:
            return abort(404)
    elif request.method == 'DELETE':
        state = storage.get(State, state_id)

        if not state:
            return abort(404)
        storage.delete(state)
        storage.save()

        return make_response(jsonify({}), 200)
    else:
        pass
