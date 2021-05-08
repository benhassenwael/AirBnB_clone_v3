#!/usr/bin/python3

from api.v1.views import app_views
from models import storage
import json


@app_views.route('/status')
def get_status():
    """Returns HTTP status 200"""
    return json.dumps({"status": "OK"}), 200

@app_views.route('/stats')
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
    stats = {name : storage.count(cls) for cls, name in objs.items()}
    return json.dumps(stats)
