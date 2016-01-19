#!/usr/bin/env python

# Remove .egg-info directory if it exists, to avoid dependency problems with
# partially-installed packages (20160119/dphiffer)

import os, sys
from shutil import rmtree

cwd = os.path.dirname(os.path.realpath(sys.argv[0]))
egg_info = cwd + "/mapzen.whosonfirst.mapshaper.egg-info"
if os.path.exists(egg_info):
    rmtree(egg_info)

from setuptools import setup, find_packages

packages = find_packages()
desc = open("README.md").read()
version = open("VERSION").read()

setup(
    name='mapzen.whosonfirst.mapshaper',
    namespace_packages=['mapzen', 'mapzen.whosonfirst', 'mapzen.whosonfirst.mapshaper'],
    version=version,
    description='Python libraries (targeted for but not specific to Who\'s On First data) for working with mapshaper\'s CLI interface.',
    author='Mapzen',
    url='https://github.com/whosonfirst/py-mapzen-whosonfirst-mapshaper',
    install_requires=[
        'geojson',
        ],
    dependency_links=[
        ],
    packages=packages,
    scripts=[
        'scripts/wof-mapshaper-centroidify',
        ],
    download_url='https://github.com/whosonfirst/py-mapzen-whosonfirst-mapshaper/releases/tag/' + version,
    license='BSD')
