#!/usr/bin/python3
"""Place View"""
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from models.place import Place


@app_views.route('/places/', methods=['GET', 'POST'])
def places():
    """Get list of all place"""

    if request.method == 'GET':
        all_places = []
        places = storage.all(Place)

        for k, v in places.items():
            all_places.append(v.to_dict())

        return make_response(jsonify(all_places))
    elif request.method == 'POST':
        if not request.is_json:
            return make_response("Not a JSON", 400)

        request_body = request.get_json()

        if not request_body.get('name'):
            return make_response("Missing name", 400)

        new_place = Place(request_body)
        print(new_place)
        # storage.new(request_body)
        # storage.save()

        return make_response(jsonify(request_body), 201)


@app_views.route('/places/<place_id>', methods=['GET', 'PUT', 'DELETE'])
def places_by_id(place_id):
    """Get place by ID"""

    places = storage.get(Place, place_id)

    if not places:
        return abort(404)

    if request.method == 'GET':
        return make_response(jsonify(places.to_dict()))
    elif request.method == 'DELETE':
        storage.delete(place)
        storage.save()

        return make_response(jsonify({}), 200)
    else:
        if not request.is_json:
            return make_response("Not a JSON", 400)
        request_body = request.get_json()

        return make_response(jsonify(request_body), 200)
