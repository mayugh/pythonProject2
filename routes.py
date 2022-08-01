#! /bin/python
# Name:routes.py
# Author:MGHarvey
# Version: 1.0
# Description:
"""
Docstring:read by the help
"""

from middleware import index, db
from flask import jsonify


def initialise_routes(app):
    app.add_url_rule('/api/hello', 'index', index)
    app.add_url_rule('/api/db', 'db', db)
    app.add_url_rule('/api/', 'list_routes', list_routes, methods=['GET'], defaults={'app': app})
    return None


def list_routes(app):
    for route in app.url_map.iter_rules():


        # print(route)
        # print(route.endpoint)
        # print(route.methods)
    return "Routes Info"


def