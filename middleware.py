#!/bin/python
# Name:
# Author:MGHarvey
# Descirption:
"""
Docstring:read by the help
"""

from flask import jsonify, request, abort
#  @app.route('/')  # @ is a decorator

heroes = [{'name': 'beckenbaur', 'nationality': 'german', 'occupation': 'footballer'},
          {'name': 'ryan reynolds', 'nationality': 'canadian', 'occupation': 'actor'},
          {'name': 'herry potter', 'nationality': 'british', 'occupation': 'wizard'},
          ]


def index():
    return "Hello World"


#  @app.route('/api/db')
def db():
    return "Hallo DB Graduates"


def user_profile(id):
    return f"Profile page of user #{id}"


def hero():
    return jsonify(heroes)


def hero_add():
    try:
        data = request.get_json(force=True)  # Get DATA FROM POST HTTP request
        name = data['name']
        nationality = data['nationality']
        occupation = data['occupation']

        if name and nationality and occupation:
            heroes.append({'name': name,
                           'nationality': nationality,
                           'occupation': occupation})
            return jsonify({'Hero ' + name: "Added Successfully"})
    except Exception as err:
        print(err)
        abort(400)

