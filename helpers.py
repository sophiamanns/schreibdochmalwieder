#!/usr/bin/env python3
"""
This file contains helper functions to be used by the schreibdochmalwieder package.
"""
import json
from hashlib import sha512
from os import listdir
from config import ASSETS_DIR, ASSETS_CONFIG_FILE

def name_to_number(name, n_max):
    """
    Returns a (default: 2-digit) number for a given string. By using a hash function, it is ensured, that strings with a low Levenshtein distance yield completely different numbers, yet the same string always yields the same.

        In [33]: name_to_number("Christin", 58)
        Out[33]: 37

        In [33]: name_to_number("Christin", 58)
        Out[33]: 37

        In [34]: name_to_number("Christina", 58)
        Out[34]: 49

        In [35]: name_to_number("Christiane", 58)
        Out[35]: 44

        In [37]: name_to_number("Christian", 58)
        Out[37]: 29
    """
    normal_name = name.lower().strip()
    hash = sha512(normal_name.encode("utf-8")).hexdigest()
    for l in "abcdef":
        hash = hash.replace(l, "")
    n_exp = len(str(n_max))
    return map_range(int(hash[:n_exp]), n_exp, n_max)

def map_range(n, n_exp, n_max):
    """
    Maps a n digit number to another n digit number, where n_max is the maximum number for n digit numbers.

    E.g. if n=99, and n_max=58, then the range 0 - 99 will be mapped to integer numbers between 0 and 58.
    """
    return int(n*n_max/(10**n_exp-1))

def get_assets(assets_config_file=ASSETS_CONFIG_FILE, assets_dir=ASSETS_DIR):
    with open(assets_config_file) as infile:
        assets_config = json.load(infile)
    return assets_config
