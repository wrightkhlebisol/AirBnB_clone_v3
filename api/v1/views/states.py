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
        if not request.is_json:
            return make_response("Not a JSON", 400)

        request_body = request.get_json()

        if not request_body.get('name'):
            return make_response("Missing name", 400)

        new_state = State(**request_body)
        new_state.save()

        return make_response(
            jsonify(
                new_state.to_dict()
            ), 201)


@app_views.route('/states/<state_id>', methods=['GET', 'PUT', 'DELETE'])
def states_by_id(state_id):
    """Get state by ID"""

    state = storage.get(State, state_id)

    if not state:
        return abort(404)

    if request.method == 'GET':
        return make_response(jsonify(state.to_dict()))
    elif request.method == 'DELETE':
        storage.delete(state)
        storage.save()

        return make_response(jsonify({}), 200)
    else:
        if not request.is_json:
            return make_response("Not a JSON", 400)
        request_body = request.get_json()
        state.name = request_body['name']
        storage.new(state)
        storage.save()

        return make_response(jsonify(state.to_dict()), 200)
