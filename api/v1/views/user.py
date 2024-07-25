#!/usr/bin/python3
"""
A script to handle users API
"""
from api.v1.views import app_views
from flask import jsonify, request, abort, url_for, redirect
from models.user import User
from models.auth import Auth
from sqlalchemy.orm.exc import NoResultFound


AUTH = Auth()

@app_views.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """
    A method used to handle users.
    """
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = AUTH._db.find_user_by(email=email)
            return jsonify({"message": "email already registered"}), 400
        except NoResultFound:
            user = AUTH.register_user(email, password)
            return jsonify({
                            "email": "{}".format(email),
                            "message": "user created"})


@app_views.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """
    A method to log user into the app.
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if (AUTH.valid_login(email, password)):
        new_session = AUTH.create_session(email)
        user = AUTH._db.find_user_by(email=email)
        args = {'session_id': new_session}
        AUTH._db.update_user(user.id, **args)
        res = jsonify({"email": "{}".format(email), "message": "logged in"})
        res.set_cookie("session_id", new_session)
        return res
    else:
        abort(401)

@app_views.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """
    A method to logout a user.
    """
    session_id = request.form.get('session_id')
    if (session_id is None):
        abort(403)
    user = AUTH.get_user_from_session_id(session_id)
    if (user is None):
        abort(403)
    if user:
        AUTH.destroy_session(user.id)
    res = jsonify({})
    res.set_cookie('session_id', '', expires=0)
    return jsonify({"message": "User logged out"}), 200

@app_views.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    """
    A method to get and verify a user by session_id.
    """
    session_id = request.cookies.get('session_id')
    if (session_id is None):
        abort(403)
    try:
        args = {'session_id': session_id}
        user = AUTH._db.find_user_by(**args)
        if (user):
            return jsonify({"email": "{}".format(user.email)}), 200
        abort(403)
    except NoResultFound:
        abort(403)


@app_views.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token():
    """
    A method used to generate token
    """
    email = request.form['email']
    try:
        args = {'email': email}
        user = AUTH._db.find_user_by(**args)
        token = AUTH.get_reset_password_token(user.email)
        return jsonify({
                       "email": "{}".format(user.email),
                       "reset_token": "{}".format(token)}), 200
    except NoResultFound:
        abort(403)