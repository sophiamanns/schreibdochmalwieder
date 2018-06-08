#!/usr/bin/env python3
"""
This file contains helper functions to be used by the schreibdochmalwieder package.
"""

from hashlib import sha512

def name_to_number(name, length=2):
    """
    Returns a (default: 2-digit) number for a given string. By using a hash function, it is ensured, that strings with a low Levenshtein distance yield completely different numbers, yet the same string always yields the same.
    """
    normal_name = name.lower().strip()
    hash = sha512(name.encode("utf-8")).hexdigest()
    for l in "abcdef":
        hash = hash.replace(l, "")
    return int(hash[:length])
