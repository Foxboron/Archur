#! /usr/bin/env python
from setuptools import find_packages, setup

setup(
    name="Archur",
    version="0.0.1",
    author="Morten Linderud",
    author_email="morten@linderud.pw",
    description="Arch linux wallpaper generator",
    long_description="Arch linux wallpaper generator",
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
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries",
    ]
)

