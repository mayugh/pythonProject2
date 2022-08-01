#! /bin/python
# Name:app.py
# Author:MGHarvey
# Version: 1.0
# Description:
"""
Docstring:read by the help
"""

from flask import Flask  # importing a class called Flask
from routes import initialise_routes

# Create a Flask object with the name of the module
app = Flask(__name__)


initialise_routes(app)


if __name__ == "__main__":
    #  Execute if running as a program
    app.run(debug=True)
