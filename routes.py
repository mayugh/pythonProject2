#! /bin/python
# Name:routes.py
# Author:MGHarvey
# Version: 1.0
# Description:
"""
Docstring:read by the help
"""

from middleware import index, db


def initialise_routes(app):
    app.add_url_rule('/api/', 'index', index)
    app.add_url_rule('/api/db', 'db', db)
    return None
