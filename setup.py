#! /usr/bin/env python
from setuptools import find_packages, setup

setup(
    name="Archur",
    version="0.0.1",
    author="Morten Linderud, Gregor Best",
    author_email="morten@linderud.pw, gbe@unobtanium.de",
    description="nREPL implementation in Hylang",
    long_description="nREPL implementation in Hylang",
    license="MIT",
    scripts=["archur.py"],
    entry_points={
        'console_scripts': [
            'archur = archur:main',
        ]
    },
    url="https://github.com/Foxboron/Archur",
    platforms=['any'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Lisp",
        "Topic :: Software Development :: Libraries",
    ]
)

