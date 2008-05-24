#!/usr/bin/python
# -*- coding: utf-8 -*-#

# Copyright (c) 2008, Xavier Basty
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
# http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

'''GrapeFruit setup and build script.'''

# $Id$
__author__ = 'Xavier Basty <xbasty@gmail.com>'
__version__ = '0.1a1'


# The base package metadata to be used by both distutils and setuptools
METADATA = dict(
  name = "grapefruit",
  version = __version__,
  py_modules = ['grapefruit'],
  author = 'Xavier Basty',
  author_email = 'xbasty@gmail.com',
  description = 'A module to manipulate color information easily.',
  license = 'Apache License 2.0',
  url = 'http://code.google.com/p/grapefruit/',
  download_url = 'http://grapefruit.googlecode.com/files/grapefruit-%s.tar.gz' % \
    __version__,
  keywords ='color conversion',
)

# Extra package metadata to be used only if setuptools is installed
SETUPTOOLS_METADATA = dict(
  install_requires = ['setuptools'],
  include_package_data = True,
  zip_safe = True,
  classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Multimedia :: Graphics',
  ],
  test_suite = 'grapefruit_test.suite',
)

def Read(file):
  return open(file).read()

def BuildLongDescription():
  return '\n'.join([Read('README'), Read('CHANGES')])

def Main():
  # Build the long_description from the README and CHANGES files
  METADATA['long_description'] = BuildLongDescription()
  
  # Use setuptools if available, otherwise fallback and use distutils
  try:
    import setuptools
    METADATA.update(SETUPTOOLS_METADATA)
    setuptools.setup(**METADATA)
  except ImportError:
    import distutils.core
    distutils.core.setup(**METADATA)


if __name__ == '__main__':
  Main()
