#!/usr/bin/env python3
"""
A script used to start the flask application.
"""
from api.v1.views import app_views
from flask import Flask, make_response, jsonify
from flask_cors import CORS
from os import environ


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

@app.errorhandler(408)
def not_found(error):
    """
    A method to show there is an error with the users
    connection.
    """
    return make_response(jsonify({'error': "connection error"}), 408)

@app.errorhandler(404)
def not_found(error):
    """
    A method to show there is an error with the users
    connection.
    """
    return make_response(jsonify({'error': "Not found"}), 404)

@app.errorhandler(403)
def not_found(error):
    """
    A method to show user is forbidden.
    """
    return make_response(jsonify({'error': "Forbidden"}), 403)


if __name__ == "__main__":
    """
    Main function
    """
    host = environ.get('API_HOST')
    port = environ.get('API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True, debug=True)
