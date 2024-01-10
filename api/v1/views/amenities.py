#!/usr/bin/python3
"""Amenity View"""
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from models.amenity import Amenity


@app_views.route('/amenities/', methods=['GET', 'POST'])
def amenities():
    """Get list of all amenity"""

    if request.method == 'GET':
        all_amenities = []
        amenities = storage.all(Amenity)

        for k, v in amenities.items():
            all_amenities.append(v.to_dict())

        return make_response(jsonify(all_amenities))
    elif request.method == 'POST':
        if not request.is_json:
            return make_response("Not a JSON", 400)

        request_body = request.get_json()

        if not request_body.get('name'):
            return make_response("Missing name", 400)

        new_amenity = Amenity(**request_body)
        new_amenity.save()

        return make_response(jsonify(new_amenity.to_dict()), 201)


@app_views.route('/amenities/<amenity_id>', methods=['GET', 'PUT', 'DELETE'])
def amenities_by_id(amenity_id):
    """Get amenity by ID"""

    amenities = storage.get(Amenity, amenity_id)

    if not amenities:
        return abort(404)

    if request.method == 'GET':
        return make_response(jsonify(amenities.to_dict()))
    elif request.method == 'DELETE':
        storage.delete(amenity)
        storage.save()

        return make_response(jsonify({}), 200)
    else:
        if not request.is_json:
            return make_response("Not a JSON", 400)
        request_body = request.get_json()

        return make_response(jsonify(request_body), 200)
