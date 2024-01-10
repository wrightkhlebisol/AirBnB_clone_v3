#!/usr/bin/python3
"""Places Amenity View"""
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from models.place import Place
from models.amenity import Amenity


@app_views.route('/place_amenities/', methods=['GET', 'POST'])
def place_amenities():
    """Get list of all place_amenity"""

    if request.method == 'GET':
        all_place_amenitys = []
        place_amenitys = storage.all(Place)

        for k, v in place_amenitys.items():
            all_place_amenitys.append(v.to_dict())

        return make_response(jsonify(all_place_amenitys))
    elif request.method == 'POST':
        if not request.is_json:
            return make_response("Not a JSON", 400)

        request_body = request.get_json()

        if not request_body.get('name'):
            return make_response("Missing name", 400)

        new_place_amenity = Place(request_body)
        new_place_amenity.save()

        return make_response(jsonify(new_place_amenity.to_dict()), 201)


@app_views.route('/place_amenitys/<place_amenity_id>',
                 methods=['GET', 'PUT', 'DELETE'])
def place_amenitys_by_id(place_amenity_id):
    """Get place_amenity by ID"""

    place_amenitys = storage.get(Place, place_amenity_id)

    if not place_amenitys:
        return abort(404)

    if request.method == 'GET':
        return make_response(jsonify(place_amenitys.to_dict()))
    elif request.method == 'DELETE':
        storage.delete(place_amenity)
        storage.save()

        return make_response(jsonify({}), 200)
    else:
        if not request.is_json:
            return make_response("Not a JSON", 400)
        request_body = request.get_json()

        return make_response(jsonify(request_body), 200)
