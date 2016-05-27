#!/usr/bin/env python

from distutils.core import setup
from setuptools import setup, find_packages

import os
import re
import shutil
import sys

package = 'evergreen'


def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]


def get_package_data(package):
    """
    Return all files under the root package, that are not in a
    package themselves.
    """
    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, '__init__.py'))]

    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                          for filename in filenames])
    return {package: filepaths}


setup(name='Evergreen',
      version='1.0',
      description='Lightweight Django CMS',
      author='Craig Sander',
      author_email='csander@centriole-solutions.com',
      url='',
      packages=find_packages(),
      package_data=get_package_data('evergreen'),
     )
