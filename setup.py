#!/usr/bin/env python

from distutils.core import setup
from setuptools import setup, find_packages

setup(name='Evergreen',
      version='1.0',
      description='Lightweight Django CMS',
      author='Craig Sander',
      author_email='csander@centriole-solutions.com',
      url='',
      packages=find_packages(),
      data_files=['',['evergreen/manage/templates/*.html']],
     )
