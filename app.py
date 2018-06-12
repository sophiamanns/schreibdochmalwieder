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
def letterpaper():
    assets = get_assets()
    random_id = randint(0, len(assets))
    asset_config = assets[random_id]

    paper = svgwrite.Drawing("test.svg", size=("210mm", "297mm"), viewBox=("0 0 210 297"))
    image_path = join(ASSETS_DIR, asset_config['filename'])
    image = Image(image_path, size=(asset_config['width'], asset_config['height']), insert=(0, 0))
    paper.add(image)
    paper.save()
    cairosvg.svg2pdf(url="test.svg", write_to="test.pdf")
    return str(random_id)
