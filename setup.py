#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''The setup and build script for the library.'''

from setuptools import setup, find_packages

setup(
  name = "python-ebml",
  url = "https://github.com/jspiros/python-ebml",
  description = "EBML (Extensible Binary Meta Language) library for Python",
  long_description = open('README.rst').read(),
  author = "Joseph Spiros",
  author_email = "joseph@josephspiros.com",
  version = '0.1',
  install_requires = [
        'setuptools',
  ],
  platforms=['OS Independent'],
  license='BSD',
  packages = find_packages(),
  namespace_packages=['ebml'],
  package_data={'': ['*.xml']}, 
  include_package_data = True,
  zip_safe = False,
)