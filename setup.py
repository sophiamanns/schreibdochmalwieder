#!/usr/bin/env python3
"""
This file is supposed to be run before executing the server for the first time. It generates
the configuration for the assets.
"""
import json
import svgwrite
import cairosvg

from PIL import Image
from os import listdir, mkdir
from os.path import join, isdir
from config import ASSETS_DIR, ASSETS_CONFIG_FILE, LETTERPAPER_DIR
from helpers import get_assets
from svgwrite.image import Image as svgimage

WIDTH='width'
HEIGHT='height'
FILENAME="filename"

def generate_assets_config(assets_dir=ASSETS_DIR, assets_config_file=ASSETS_CONFIG_FILE):
    """
    This function generates a json file in the BASE_DIR where the principal
    dimensions of all images/assets are put.
    """
    config=list()
    for filename in listdir(assets_dir):
        print("Generating config for {}".format(filename))
        with Image.open(join(assets_dir, filename)) as im:
            config.append({  WIDTH: im.size[0],
                             HEIGHT: im.size[1],
                             FILENAME: filename})

    with open(assets_config_file, "w") as outfile:
        json.dump(config, outfile, indent=4)

def generate_letterpaper():
    """
    This function generates the letterpaper from the assets.
    """
    for n_asset, asset_config in enumerate(get_assets()):
        filename = "letterpaper_{}".format(n_asset)
        svg_filename = "{}.svg".format(filename)
        pdf_filename = "{}.pdf".format(filename)
        png_filename = "{}.png".format(filename)
        svg_path = join(LETTERPAPER_DIR, svg_filename)
        pdf_path = join(LETTERPAPER_DIR, pdf_filename)
        png_path = join(LETTERPAPER_DIR, png_filename)

        print("Generating {} from {}".format(pdf_path, asset_config[FILENAME]))
        paper = svgwrite.Drawing(svg_path, size=("210mm", "297mm"), viewBox=("0 0 210 297"))

        # make bg white
        paper.add(paper.rect(insert=(0*svgwrite.mm, 0*svgwrite.mm), size=(210*svgwrite.mm, 297*svgwrite.mm),
fill='white'))

        # Add Pattern or Background
        image_path = join(ASSETS_DIR, asset_config[FILENAME])
        image = svgimage(image_path, size=(asset_config[WIDTH], asset_config[HEIGHT]), insert=(0, 0))
        paper.add(image)

        # Save and Convert
        paper.save()
        cairosvg.svg2pdf(url=svg_path, write_to=pdf_path)
        cairosvg.svg2png(url=svg_path, write_to=png_path)

def make_letterpaper_dir(letterpaper_dir=LETTERPAPER_DIR):
    if not isdir(letterpaper_dir):
        mkdir(letterpaper_dir)

def main():
    """
    All setup functions are to be put here.
    """
    generate_assets_config()
    make_letterpaper_dir()
    generate_letterpaper()


if __name__ == "__main__":
    main()
