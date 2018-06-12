#!/usr/bin/env python3

from os.path import join, abspath, dirname

BASE_DIR = dirname(abspath(__file__))
STATIC_DIR = join(BASE_DIR, "static")
ASSETS_DIR = join(STATIC_DIR, "assets")
ASSETS_CONFIG_FILE = join(BASE_DIR, "assets_config.json")
