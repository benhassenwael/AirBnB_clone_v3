#!/usr/bin/python3
""" First endpoint route returning the status """
from flask import Flask, json
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask('v1')
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_storage(exception):
    """Close app storage"""
    storage.close()

@app.errorhandler(404)
def not_found(error):
    """Handle 404 not found errors and return json object"""
    return json.jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = getenv('HBNB_API_PORT', '5000')
    app.run(host=host, port=port)
