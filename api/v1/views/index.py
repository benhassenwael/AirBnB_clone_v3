#!/usr/bin/python3
"""index API endpoint"""
from api.v1.views import app_views
from models import storage
from flask.json import jsonify


@app_views.route('/status', strict_slashes=False)
def get_status():
    """Returns HTTP status 200"""
    return jsonify({"status": "OK"}), 200


@app_views.route('/stats', strict_slashes=False)
def get_stats():
    """Returns number of each object by type"""
    objs = {
        "Amenity": "amenities",
        "City": "cities",
        "Place": "places",
        "Review": "reviews",
        "State": "states",
        "User": "users"
    }
    stats = {name: storage.count(cls) for cls, name in objs.items()}
    return jsonify(stats)
