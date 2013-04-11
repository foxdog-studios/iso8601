#!/usr/bin/env python

from distutils.core import setup

setup(
    name='iso8601',
    version='0.0.1',
    description='IS0 8601 parser',
    author='Peter Sutton',
    author_email='foxxy@foxdogstudios.com',
    url='https://github.com/foxdog-studios/iso8601',
    packages=['iso8601'],
    package_dir={'iso8601': 'src/iso8601'},
)
