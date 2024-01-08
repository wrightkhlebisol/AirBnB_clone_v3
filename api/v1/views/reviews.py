#!/usr/bin/python3
"""Review View"""
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from models.review import Review


@app_views.route('/reviews/', methods=['GET', 'POST'])
def reviews():
    """Get list of all review"""

    if request.method == 'GET':
        all_reviews = []
        reviews = storage.all(Review)

        for k, v in reviews.items():
            all_reviews.append(v.to_dict())

        return make_response(jsonify(all_reviews))
    elif request.method == 'POST':
        if not request.is_json:
            return make_response("Not a JSON", 400)

        request_body = request.get_json()

        if not request_body.get('name'):
            return make_response("Missing name", 400)

        new_review = Review(request_body)
        print(new_review)
        # storage.new(request_body)
        # storage.save()

        return make_response(jsonify(request_body), 201)


@app_views.route('/reviews/<review_id>', methods=['GET', 'PUT', 'DELETE'])
def reviews_by_id(review_id):
    """Get review by ID"""

    reviews = storage.get(Review, review_id)

    if not reviews:
        return abort(404)

    if request.method == 'GET':
        return make_response(jsonify(reviews.to_dict()))
    elif request.method == 'DELETE':
        storage.delete(review)
        storage.save()

        return make_response(jsonify({}), 200)
    else:
        if not request.is_json:
            return make_response("Not a JSON", 400)
        request_body = request.get_json()

        return make_response(jsonify(request_body), 200)
