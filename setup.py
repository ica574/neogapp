#!/usr/bin/env python

from distutils.core import setup

setup(
    name="neogapp",
    version="1.0",
    description="A modernised version of the Gaussian Processes in Python package to be used natively with Python 3",
    license="GPLv3",
    author="Isaac Cilia Attard",
    author_email="contact@isaacciliaattard.com",
    original_author="Marina Seikel",
    original_author_email="marina@jorrit.de",
    url="http://www.acgc.uct.ac.za/~seikel/GAPP/index.html",
    packages=["gapp", "gapp.covfunctions"],
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib',
        'emcee',
        'acor',
    ]
)
