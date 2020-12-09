# -*- coding: utf-8 -*-

import json, os

DIR = "resources"
PATH = os.path.join(os.path.dirname(__file__), DIR)

"""
Resources for Colorbrewer:
    * Home: https://colorbrewer2.org
    * Repository: https://github.com/axismaps/colorbrewer/
    * All scales: https://github.com/axismaps/colorbrewer/blob/master/export/colorbrewer.json
"""

class Colors(dict):
    """docstring for Colors."""
    def __init__(self):
        super(Colors, self).__init__()
        for filename in os.listdir(PATH):
            if filename.endswith(".json"):
                fname, ext = os.path.splitext(filename)
                with open(os.fsencode(os.path.join(PATH, filename))) as source:
                    self[fname] = json.load(source)

colors = Colors()
