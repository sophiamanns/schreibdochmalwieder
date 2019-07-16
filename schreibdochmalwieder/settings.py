#!/usr/bin/env python3

from os.path import join, abspath, dirname

# assets config keys
WIDTH = "width"
HEIGHT = "height"
FILENAME = "filename"
OPACITY = "opacity"

# paper configuration
PAPER_WIDTH = 210
PAPER_HEIGHT = 297
PAPER_MARGIN = 10

# paths
BASE_DIR = dirname(abspath(__file__))
STATIC_DIR = join(BASE_DIR, "static")
DIEDERICH_ASSETS_DIR = join(STATIC_DIR, "assets")
DIEDERICH_LETTERPAPER_DIR = join(STATIC_DIR, "letterpaper")
DIEDERICH_ASSETS_CONFIG_FILE = join(BASE_DIR, "assets_config.json")
HERBARIUM_ASSETS_DIR = join(STATIC_DIR, "herbarium", "band_3")
HERBARIUM_ASSETS_CONFIG_FILE = join(BASE_DIR, "herbarium_config.json")
HERBARIUM_LETTERPAPER_DIR = join(STATIC_DIR, "herbarium_letterpaper")
