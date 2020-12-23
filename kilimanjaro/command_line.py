# -*- coding: utf-8 -*-

from .dbutils.wiz import Wiz as ConnCollector
import argparse
import os
import sys
import importlib


def hello():
    print("Hello world!")


def dbgenie_(DB_FOLDER, DB_URI, *extensions):
    dbcollector = ConnCollector(
        path=DB_FOLDER,
        cache=None
    )
    dbcollector.collect(DB_URI, *extensions)
    dbcollector.setup()


def dbgenie():
    parser = argparse.ArgumentParser(
        description = """This helper commend takes case of creating PostgreSQL
        database with all required extensions (if available).""",
        formatter_class = argparse.RawTextHelpFormatter
    )
    parser.add_argument("settings",
        help = 'Path for application settings file containing at least DB_FOLDER and DB_URI variables',
        required = True
    )

    parser.add_argument("-e", "--extensions", nargs="*", default=[])

    args = parser.parse_args()

    # Courtesy of: https://stackoverflow.com/a/55892361/1039510
    pathname, filename = os.path.split(args.settings)
    sys.path.append(os.path.abspath(pathname))
    modname = os.path.splitext(filename)[0]
    settings = importlib.import_module(modname)
    dbgenie_(settings.DB_FOLDER, settings.DB_URI, *args.extensions)
