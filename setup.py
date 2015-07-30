#!/usr/bin/env python
# coding: utf-8

"""
An ad-hoc lightweight SPARQL endpoint served from a file.
"""

try:
    from setuptools import setup
except:
    from distutils.core import setup

from adhocsparql import __version__

install_requires = [
    'Flask>=0.10.1',
    'Flask-Cors>=2.0.1',
    'rdflib>=4.2.0',
]

setup(name='adhs',
      version=__version__,
      description='An ad-hoc lightweight SPARQL endpoint served from a file.',
      url='https://github.com/nareike/adhs',
      author='AN',
      author_email='an@example.com',
      packages=['adhocsparql'],
      package_data={'adhocsparql': ['templates/response.html',
                                    'templates/sparql.html']},
      include_package_data=True,
      package_dir={'adhs': 'adhocsparql'},
      scripts=['adhs.py'],
      install_requires=install_requires,
)
