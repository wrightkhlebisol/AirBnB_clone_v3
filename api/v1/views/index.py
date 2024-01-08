#!/usr/bin/python3
"""Blueprint views"""
from api.v1.views import app_views
from flask import jsonify, make_response
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {
    "amenities": Amenity,
    "Cities": City,
    "Places": Place,
    "Reviews": Review,
    "States": State,
    "Users": User
}


@app_views.route('/status')
def status():
    return make_response(jsonify({'status': 'OK'}))


@app_views.route('/stats')
def stats():
    stats = {}

    for k, v in classes.items():
        stats[k.lower()] = storage.count(v)

    return make_response(jsonify(stats))
