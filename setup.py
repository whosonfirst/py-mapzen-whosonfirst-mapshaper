#!/usr/bin/env python

from setuptools import setup, find_packages

packages = find_packages()
desc = open("README.md").read(),

setup(
    name='mapzen.whosonfirst.mapshaper',
    namespace_packages=['mapzen', 'mapzen.whosonfirst', 'mapzen.whosonfirst.mapshaper'],
    version='0.04',
    description='Python libraries (targeted for but not specific to Who\'s On First data) for working with mapshaper\'s CLI interface.',
    author='Mapzen',
    url='https://github.com/mapzen/py-mapzen-whosonfirst-mapshaper',
    install_requires=[
        'geojson',
        ],
    dependency_links=[
        ],
    packages=packages,
    scripts=[
        'scripts/wof-mapshaper-centroidify',
        ],
    download_url='https://github.com/whosonfirst/py-mapzen-whosonfirst-mapshaper/releases/tag/v0.04',
    license='BSD')
