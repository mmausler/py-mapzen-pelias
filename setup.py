#!/usr/bin/env python

from setuptools import setup, find_packages

packages = find_packages()
desc = open("README.md").read(),

setup(
    name='mapzen.pelias',
    namespace_packages=['mapzen'],
    version='0.23',
    description='Simple Python wrapper for the Mapzen Pelias API',
    author='Mapzen',
    url='https://github.com/thisisaaronland/py-mapzen-pelias',
    install_requires=[
        'requests',
        'geojson',
        ],
    dependency_links=[],
    packages=packages,
    scripts=[
        'scripts/mz-geocode',
        'scripts/mz-reverse-geocode',
        ],
    download_url='https://github.com/thisisaaronland/py-mapzen-pelias/releases/tag/v0.2',
    license='BSD')
