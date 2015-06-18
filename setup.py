#!/usr/bin/env python

from setuptools import setup, find_packages

packages = find_packages()
desc = open("README.md").read(),

setup(
    name='mapzen.pelias',
    namespace_packages=['mapzen'],
    version='0.4',
    description='Simple Python wrapper for the Mapzen Pelias API',
    author='Mapzen',
    url='https://github.com/thisisaaronland/py-mapzen-pelias',
    install_requires=[
        'requests',
        'geojson',
        'mapzen.geojson',
        ],
    packages=packages,
    scripts=[
        ],
    download_url='https://github.com/thisisaaronland/py-mapzen-pelias/releases/tag/v0.1',
    license='BSD')
