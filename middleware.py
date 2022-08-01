#!/bin/python
# Name:
# Author:MGHarvey
# Descirption:
"""
Docstring:read by the help
"""

@app.route('/')  # @ is a decorator
def index():
    return "Hello World"


#  @app.route('/api/db')
def db():
    return "Hallo DB Graduates"
