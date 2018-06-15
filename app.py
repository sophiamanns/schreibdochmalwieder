#!/usr/bin/env python3
"""
This is the application file. It contains the main program and
is meant to be executed
"""

import svgwrite
import cairosvg

from os.path import join
from svgwrite.image import Image
from flask import Flask, render_template, url_for
from random import randint
from helpers import name_to_number, get_assets
from config import ASSETS_DIR

app = Flask(__name__)

@app.route("/")
def index():
    print(get_assets())
    return render_template("index.html")

@app.route("/paperbyname/")
@app.route("/paperbyname/<name>")
def paperbyname(name=None):
    if not name:
        return("Sinnlos...")
    else:
        return str(name_to_number(name, 58))

@app.route("/letterpaper")
@app.route("/letterpaper/<int:letterpaper_id>")
def letterpaper(letterpaper_id=None):
    if not letterpaper_id:
        letterpaper_id = randint(0, len(get_assets()))
    return render_template("letterpaper.html", random_id=str(letterpaper_id))
