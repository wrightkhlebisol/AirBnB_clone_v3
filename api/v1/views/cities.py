#!/usr/bin/python3
"""City View"""
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from models.city import City


@app_views.route('/cities/', methods=['GET', 'POST'])
def cities():
    """Get list of all city"""

    if request.method == 'GET':
        all_cities = []
        cities = storage.all(City)

        for k, v in cities.items():
            all_cities.append(v.to_dict())

        return make_response(jsonify(all_cities))
    elif request.method == 'POST':
        if not request.is_json:
            return make_response("Not a JSON", 400)

        request_body = request.get_json()

        if not request_body.get('name'):
            return make_response("Missing name", 400)

        new_city = City(request_body)
        new_city.save()

        return make_response(jsonify(new_city.to_dict()), 201)


@app_views.route('/cities/<city_id>', methods=['GET', 'PUT', 'DELETE'])
def cities_by_id(city_id):
    """Get city by ID"""

    cities = storage.get(City, city_id)

    if not cities:
        return abort(404)

    if request.method == 'GET':
        return make_response(jsonify(cities.to_dict()))
    elif request.method == 'DELETE':
        storage.delete(city)
        storage.save()

        return make_response(jsonify({}), 200)
    else:
        if not request.is_json:
            return make_response("Not a JSON", 400)
        request_body = request.get_json()

        return make_response(jsonify(request_body), 200)
