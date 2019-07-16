#!/usr/bin/env python3

from os.path import join, abspath, dirname

BASE_DIR = dirname(abspath(__file__))
STATIC_DIR = join(BASE_DIR, "static")
ASSETS_DIR = join(STATIC_DIR, "assets")
LETTERPAPER_DIR = join(STATIC_DIR, "letterpaper")
ASSETS_CONFIG_FILE = join(BASE_DIR, "assets_config.json")
DIEDERICH_ASSETS_CONFIG_FILE = ASSETS_CONFIG_FILE
DIEDERICH_LETTERPAPER_DIR = LETTERPAPER_DIR
DIEDERICH_ASSETS_DIR = ASSETS_DIR
HERBARIUM_ASSETS_DIR = join(STATIC_DIR, "herbarium", "band_3")
HERBARIUM_ASSETS_CONFIG_FILE= join(STATIC_DIR, "herbarium_config.json")
HERBARIUM_LETTERPAPER_DIR = join(STATIC_DIR, "herbarium_letterpaper")
