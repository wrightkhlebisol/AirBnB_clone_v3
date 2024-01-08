#!/usr/bin/python3
"""City View"""
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from models.city import City


@app_views.route('/citys/', methods=['GET', 'POST'])
def citys():
    """Get list of all city"""

    if request.method == 'GET':
        all_citys = []
        citys = storage.all(City)

        for k, v in citys.items():
            all_citys.append(v.to_dict())

        return make_response(jsonify(all_citys))
    elif request.method == 'POST':
        if not request.is_json:
            return make_response("Not a JSON", 400)

        request_body = request.get_json()

        if not request_body.get('name'):
            return make_response("Missing name", 400)

        new_city = City(request_body)
        print(new_city)
        # storage.new(request_body)
        # storage.save()

        return make_response(jsonify(request_body), 201)


@app_views.route('/citys/<city_id>', methods=['GET', 'PUT', 'DELETE'])
def citys_by_id(city_id):
    """Get city by ID"""

    citys = storage.get(City, city_id)

    if not citys:
        return abort(404)

    if request.method == 'GET':
        return make_response(jsonify(citys.to_dict()))
    elif request.method == 'DELETE':
        storage.delete(city)
        storage.save()

        return make_response(jsonify({}), 200)
    else:
        if not request.is_json:
            return make_response("Not a JSON", 400)
        request_body = request.get_json()

        return make_response(jsonify(request_body), 200)
