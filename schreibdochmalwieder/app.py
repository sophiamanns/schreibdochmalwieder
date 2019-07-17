#!/usr/bin/env python3
"""
This is the application file. It contains the main program and
is meant to be executed
"""
import settings
import json

from pathlib import Path
from flask import Flask, render_template, url_for, redirect, request
from random import randint
from helpers import name_to_number, get_assets

app = Flask(__name__)

diederich_assets = get_assets(
    settings.DIEDERICH_ASSETS_DIR, settings.DIEDERICH_ASSETS_CONFIG_FILE
)
herbarium_assets = get_assets(
    settings.HERBARIUM_ASSETS_DIR, settings.HERBARIUM_ASSETS_CONFIG_FILE
)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/herbarium")
def herbarium():
    h_path = Path(settings.HERBARIUM_LETTERPAPER_DIR).relative_to(settings.STATIC_DIR)
    image_preview = []
    row = []
    for i, image in enumerate(herbarium_assets):
        image = {
            "image_id": i,
            "image_url": url_for(
            "static", filename="{}/letterpaper_{}_thumb.png".format(h_path, i)
            ),
        }
        row.append(image)
        if i + 1 % 6 == 0:
            image_preview.append(row)
            row = []
    image_preview.append(row)
    return render_template("herbarium.html", image_preview=image_preview)


@app.route("/paperbyname/", methods=["POST"])
def paperbyname():
    return redirect(
        url_for("letterpaper")
        + "/{}".format(str(name_to_number(request.form["name"], 58)))
    )



@app.route("/herbarium_letterpaper/<int:letterpaper_id>")
def herbarium_letterpaper_with_id(letterpaper_id=None):

    if letterpaper_id is None:
        letterpaper_id = randint(0, len(herbarium_assets))

    orig_id = herbarium_assets[letterpaper_id][settings.FILENAME].lstrip("0")[:-4]

    img_url = url_for(
        "static",
        filename="herbarium_letterpaper/letterpaper_{}.png".format(letterpaper_id),
    )
    pdf_url = url_for(
        "static",
        filename="herbarium_letterpaper/letterpaper_{}.pdf".format(letterpaper_id),
    )

    return render_template(
        "herbarium_letterpaper.html",
        letterpaper_id=str(letterpaper_id),
        img_url=img_url,
        pdf_url=pdf_url,
        letterpaper_orig_id=orig_id,
    )


@app.route("/letterpaper")
def letterpaper():
    return redirect(
        url_for("letterpaper") + "/{}".format(str(randint(0, len(diederich_assets))))
    )


@app.route("/letterpaper/<int:letterpaper_id>")
def letterpaper_with_id(letterpaper_id=None):

    if letterpaper_id is None:
        letterpaper_id = randint(0, diederich_assets)

    img_url = url_for(
        "static", filename="letterpaper/letterpaper_{}.png".format(letterpaper_id)
    )
    pdf_url = url_for(
        "static", filename="letterpaper/letterpaper_{}.pdf".format(letterpaper_id)
    )

    return render_template(
        "letterpaper.html",
        letterpaper_id=str(letterpaper_id),
        img_url=img_url,
        pdf_url=pdf_url,
    )
