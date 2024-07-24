#!/usr/bin/env python3
"""
A script to handle the scores API
"""
from api.v1.views import app_views
from flask import jsonify
from models.web_page_monitor import WebPageMonitor as Monitor
from os import environ
from models.auth import Auth


online = environ.get("ONLINE", "True")
url = "https://www.livescores.com/"
file1 = "./livescores/live_football.html"
file2 = "./livescores/live_football_usa_mls.html"
instance = Monitor()
args = {"file": file1, "file2": file2, "online": online, "url": url}
AUTH = Auth()


@app_views.route("/list_of_sports", methods=['GET'], strict_slashes=False)
def list_of_sports():
    """
    A method to get list of sports
    """
    print(AUTH._db.add_user(email="zeus@gmail.com", hashed_password="password"))
    result = instance.set_dict_of_sports(**args)
    return jsonify({"data": result})

@app_views.route("/football_today", methods=['GET'], strict_slashes=False)
def football_today():
    """
    A method to get football games for the day
    """
    result = instance.football_today(online)
    return jsonify({"data": result})

@app_views.route("/football_live", methods=['GET'], strict_slashes=False)
def football_live():
    """
    A method to get football live games
    """
    result = instance.football_live(online)
    return jsonify({"data": result})

@app_views.route("/basketball_today", methods=['GET'], strict_slashes=False)
def basketball_today():
    """
    A method to get basketball games for the day
    """
    result = instance.basketball_today(online)
    return jsonify({"data": result})

@app_views.route("/basketball_live", methods=['GET'], strict_slashes=False)
def basketball_live():
    """
    A method to get basketball live games for the day
    """
    result = instance.basketball_live(online)
    return jsonify({"data": result})

@app_views.route("/cricket_today", methods=['GET'], strict_slashes=False)
def cricket_today():
    """
    A method to get cricket games for the day
    """
    result = instance.cricket_today(online)
    return jsonify({"data": result})

@app_views.route("/cricket_live", methods=['GET'], strict_slashes=False)
def cricket_live():
    """
    A method to get cricket live games for the day
    """
    result = instance.cricket_live(online)
    return jsonify({"data": result})

@app_views.route("/hockey_today", methods=['GET'], strict_slashes=False)
def hockey_today():
    """
    A method to get hockey games for the day
    """
    result = instance.hockey_today(online)
    return jsonify({"data": result})

@app_views.route("/hockey_live", methods=['GET'], strict_slashes=False)
def hockey_live():
    """
    A method to get hockey live games for the day
    """
    result = instance.hockey_live(online)
    return jsonify({"data": result})

@app_views.route("/tennis_today", methods=['GET'], strict_slashes=False)
def tennis_today():
    """
    A method to get tennis games for the day
    """
    result = instance.tennis_today(online)
    return jsonify({"data": result})

@app_views.route("/tennis_live", methods=['GET'], strict_slashes=False)
def tennis_live():
    """
    A method to get tennis games for the day
    """
    result = instance.tennis_live(online)
    return jsonify({"data": result})
