# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kilimanjaro",
    version="0.0.1",
    author="Manuele Pesenti",
    author_email="manuele@inventati.org",
    description="Generic tools I want to bring almost always with me",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/manuelep/kilimanjaro",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "matplotlib",
        "numpy",
        "py4web",
        # "psycopg2"
    ],
    entry_points = {
        'console_scripts': ['dbgenie=kilimanjaro.command_line:dbgenie', 'hello=kilimanjaro.command_line:hello'],
    },
    zip_safe=False
)
