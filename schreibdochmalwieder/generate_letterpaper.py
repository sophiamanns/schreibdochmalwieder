#!/usr/bin/env python3
"""
This file is supposed to be run before executing the server for the first time. It generates
the configuration for the assets.
"""
import json
import svgwrite
import cairosvg
import click

from pathlib import Path
from PIL import Image
from os import listdir, mkdir
from os.path import join, isdir
from config import ASSETS_DIR, ASSETS_CONFIG_FILE, LETTERPAPER_DIR
from helpers import get_assets
from svgwrite.image import Image as svgimage

WIDTH = 'width'
HEIGHT = 'height'
FILENAME = 'filename'
OPACITY = 'opacity'

PAPER_WIDTH = 210
PAPER_HEIGHT = 297
PAPER_MARGIN = 10


def generate_assets_config(assets_dir=ASSETS_DIR, assets_config_file=ASSETS_CONFIG_FILE,
        opacity=1.0):
    """
    This function generates a json file in the BASE_DIR where the principal
    dimensions of all images/assets are put.
    """
    config = list()
    for filename in listdir(assets_dir):
        print("Generating config for {}".format(filename))
        with Image.open(join(assets_dir, filename)) as im:
            config.append({WIDTH: im.size[0],
                           HEIGHT: im.size[1],
                           FILENAME: filename,
                           OPACITY: opacity})

    with open(assets_config_file, "w") as outfile:
        json.dump(config, outfile, indent=4)


def generate_letterpaper(
        letterpaper_dir=LETTERPAPER_DIR,
        assets_dir=ASSETS_DIR,
        assets_config=ASSETS_CONFIG_FILE):
    """
    This function generates the letterpaper from the assets.
    """
    for n_asset, asset_config in enumerate(get_assets(assets_dir, assets_config)):
        filename = "letterpaper_{}".format(n_asset)
        svg_filename = "{}.svg".format(filename)
        pdf_filename = "{}.pdf".format(filename)
        png_filename = "{}.png".format(filename)
        thumb_filename = "{}_thumb.png".format(filename)
        svg_path = join(letterpaper_dir, svg_filename)
        pdf_path = join(letterpaper_dir, pdf_filename)
        png_path = join(letterpaper_dir, png_filename)
        thumb_path = join(letterpaper_dir, thumb_filename)

        print("Generating {} from {}".format(pdf_path, asset_config[FILENAME]))
        paper = svgwrite.Drawing(svg_path, size=("210mm", "297mm"), viewBox=("0 0 210 297"))

        # make bg white
        paper.add(paper.rect(insert=(0*svgwrite.mm, 0*svgwrite.mm),
                  size=(210*svgwrite.mm, 297*svgwrite.mm),
                  fill='white'))

        # Add Pattern or Background
        image_path = join(assets_dir, asset_config[FILENAME])

        image_dims = (asset_config[WIDTH], asset_config[HEIGHT])

        if image_dims[0] > PAPER_WIDTH-PAPER_MARGIN:
            image_dims = tuple(
                    image_dim/(image_dims[0]/(PAPER_WIDTH-PAPER_MARGIN))
                    for image_dim in image_dims
            )

        if image_dims[1] > PAPER_HEIGHT-PAPER_MARGIN:
            image_dims = tuple(
                    image_dim/(image_dims[1]/(PAPER_HEIGHT-PAPER_MARGIN))
                    for image_dim in image_dims
            )

        image = svgimage(image_path,
                         size=(image_dims),
                         insert=(PAPER_MARGIN/2, PAPER_MARGIN/2),
                         opacity=asset_config[OPACITY])
        paper.add(image)

        # Save and Convert
        paper.save()
        cairosvg.svg2pdf(url=svg_path, write_to=pdf_path)
        cairosvg.svg2png(url=svg_path, write_to=png_path)
        cairosvg.svg2png(url=svg_path, write_to=thumb_path, scale=0.1)


def make_letterpaper_dir(letterpaper_dir=LETTERPAPER_DIR):
    if not isdir(letterpaper_dir):
        mkdir(letterpaper_dir)

@click.command()
@click.option("--letterpaper-dir", default=LETTERPAPER_DIR)
@click.option("--opacity", default=1.0, type=float)
@click.argument("assets_dir", type=click.Path(exists=True))
@click.argument("assets_config")
def main(letterpaper_dir, opacity, assets_dir, assets_config):
    """
    All setup functions are to be put here.
    """
    cwd = Path.cwd()
    assets_dir = cwd / assets_dir
    assets_config = cwd / assets_config
    generate_assets_config(assets_dir, assets_config, opacity)
    make_letterpaper_dir(letterpaper_dir)
    generate_letterpaper(letterpaper_dir, assets_dir, assets_config)


if __name__ == "__main__":
    main()
