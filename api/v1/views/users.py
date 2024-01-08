#!/usr/bin/python3
"""User View"""
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from models.user import User


@app_views.route('/users/', methods=['GET', 'POST'])
def users():
    """Get list of all user"""

    if request.method == 'GET':
        all_users = []
        users = storage.all(User)

        for k, v in users.items():
            all_users.append(v.to_dict())

        return make_response(jsonify(all_users))
    elif request.method == 'POST':
        if not request.is_json:
            return make_response("Not a JSON", 400)

        request_body = request.get_json()

        if not request_body.get('name'):
            return make_response("Missing name", 400)

        new_user = User(request_body)
        print(new_user)
        # storage.new(request_body)
        # storage.save()

        return make_response(jsonify(request_body), 201)


@app_views.route('/users/<user_id>', methods=['GET', 'PUT', 'DELETE'])
def users_by_id(user_id):
    """Get user by ID"""

    users = storage.get(User, user_id)

    if not users:
        return abort(404)

    if request.method == 'GET':
        return make_response(jsonify(users.to_dict()))
    elif request.method == 'DELETE':
        storage.delete(user)
        storage.save()

        return make_response(jsonify({}), 200)
    else:
        if not request.is_json:
            return make_response("Not a JSON", 400)
        request_body = request.get_json()

        return make_response(jsonify(request_body), 200)
