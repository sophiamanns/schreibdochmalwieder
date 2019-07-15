#!/usr/bin/env python3
"""
This is the application file. It contains the main program and
is meant to be executed
"""

from pathlib import Path
from flask import Flask, render_template, url_for, redirect, request
from random import randint
from helpers import name_to_number, get_assets
from config import HERBARIUM_LETTERPAPER_DIR, BASE_DIR

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/herbarium")
def herbarium():
    h_path = Path(HERBARIUM_LETTERPAPER_DIR)
    image_preview = []
    row = []
    for i, image in enumerate(h_path.glob("*_thumb.png")):
        image = {"image_id": i,
                 "image_url": image.relative_to(BASE_DIR)}
        row.append(image)
        if i+1%6 == 0:
            image_preview.append(row)
            row = []
    image_preview.append(row)
    return render_template("herbarium.html", image_preview=image_preview)


@app.route("/paperbyname/", methods=['POST'])
def paperbyname():
    return redirect(
            url_for('letterpaper') + "/{}".format(str(name_to_number(request.form['name'], 58)))
    )


@app.route("/letterpaper")
def letterpaper():
    return redirect(
            url_for('letterpaper') + "/{}".format(str(randint(0, len(get_assets()))))
    )

@app.route("/herbarium_letterpaper/<int:letterpaper_id>")
def herbarium_letterpaper_with_id(letterpaper_id=None):

    if not letterpaper_id:
        letterpaper_id = randint(0, len(get_assets()))

    img_url = url_for('static', filename="herbarium_letterpaper/letterpaper_{}.png".format(letterpaper_id))
    pdf_url = url_for('static', filename="herbarium_letterpaper/letterpaper_{}.pdf".format(letterpaper_id))
    letterpaper_url = url_for('letterpaper')
    this_page_url = f"herbarium_letterpaper/{letterpaper_id}"

    return render_template("letterpaper.html",
                           letterpaper_id=str(letterpaper_id),
                           img_url=img_url,
                           pdf_url=pdf_url,
                           letterpaper_url=letterpaper_url,
                           this_page_url=this_page_url)

@app.route("/letterpaper/<int:letterpaper_id>")
def letterpaper_with_id(letterpaper_id=None):

    if not letterpaper_id:
        letterpaper_id = randint(0, len(get_assets()))

    img_url = url_for('static', filename="letterpaper/letterpaper_{}.png".format(letterpaper_id))
    pdf_url = url_for('static', filename="letterpaper/letterpaper_{}.pdf".format(letterpaper_id))
    letterpaper_url = url_for('letterpaper')
    this_page_url = letterpaper_url + "/{}".format(letterpaper_id)

    return render_template("letterpaper.html",
                           letterpaper_id=str(letterpaper_id),
                           img_url=img_url,
                           pdf_url=pdf_url,
                           letterpaper_url=letterpaper_url,
                           this_page_url=this_page_url)
