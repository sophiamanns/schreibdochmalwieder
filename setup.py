#!/usr/bin/env python3
"""
This file is supposed to be run before executing the server for the first time. It generates
the configuration for the assets.
"""
import json

from PIL import Image
from os import listdir
from os.path import join
from config import ASSETS_DIR, ASSETS_CONFIG_FILE

def generate_assets_config(assets_dir=ASSETS_DIR, assets_config_file=ASSETS_CONFIG_FILE):
    """
    This function generates a json file in the BASE_DIR where the principal
    dimensions of all images/assets are put.
    """
    config=list()
    for filename in listdir(assets_dir):
        print("Generating config for {}".format(filename))
        with Image.open(join(assets_dir, filename)) as im:
            config.append({  'width': im.size[0],
                        'height': im.size[1],
                        'filename': filename})

    with open(assets_config_file, "w") as outfile:
        json.dump(config, outfile, indent=4)


def main():
    """
    All setup functions are to be put here.
    """
    generate_assets_config()


if __name__ == "__main__":
    main()
