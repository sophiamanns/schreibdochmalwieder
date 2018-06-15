#!/usr/bin/env python3
"""
This is the application file. It contains the main program and
is meant to be executed
"""

import svgwrite
import cairosvg

from os.path import join
from svgwrite.image import Image
from flask import Flask, render_template, url_for, redirect, request
from random import randint
from helpers import name_to_number, get_assets
from config import ASSETS_DIR

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/paperbyname/", methods=['POST'])
def paperbyname():
    return redirect(url_for('letterpaper')+ "/{}".format(str(name_to_number(request.form['name'], 58))))

@app.route("/letterpaper")
def letterpaper():
    return redirect(url_for('letterpaper')+ "/{}".format(str(randint(0, len(get_assets())))))

@app.route("/letterpaper/<int:letterpaper_id>")
def letterpaper_with_id(letterpaper_id=None):

    if not letterpaper_id:
        letterpaper_id = randint(0, len(get_assets()))

    img_url = url_for('static', filename="letterpaper/letterpaper_{}.png".format(letterpaper_id))
    pdf_url = url_for('static', filename="letterpaper/letterpaper_{}.pdf".format(letterpaper_id))
    letterpaper_url = url_for('letterpaper')
    this_page_url = letterpaper_url + "/{}".format(letterpaper_id)

    return render_template( "letterpaper.html",
                            letterpaper_id=str(letterpaper_id),
                            img_url=img_url,
                            pdf_url=pdf_url,
                            letterpaper_url=letterpaper_url,
                            this_page_url=this_page_url)
