#!/usr/bin/env python3
"""
The Blueprint for the application.
"""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
from api.v1.views.monitor import *
from api.v1.views.user import *
