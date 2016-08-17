==========
GrapeFruit
==========

.. image:: https://img.shields.io/pypi/v/grapefruit.svg?style=flat
   :target: https://pypi.python.org/pypi/grapefruit/
   :alt: Latest PyPI version

.. image:: https://img.shields.io/travis/xav/Grapefruit/master.svg?style=flat
   :target: https://travis-ci.org/xav/grapefruit/
   :alt: Travis CI build status

.. image:: https://coveralls.io/repos/github/xav/Grapefruit/badge.svg?branch=master&style=flat
   :target: https://coveralls.io/github/xav/Grapefruit?branch=master
   :alt: Test coverage

.. image:: https://img.shields.io/github/license/xav/Grapefruit.svg?style=flat
   :alt: License

GrapeFruit is a pure Python module that let you easily manipulate and convert color information.
Its Primary goal is to be *natural* and *flexible*.

The following color systems are supported by GrapeFruit:
  * RGB (sRGB)
  * HSL
  * HSV
  * YIQ
  * YUV
  * CIE-XYZ
  * CIE-LAB (with the illuminant you want)
  * CMY
  * CMYK
  * HTML/CSS color definition (#RRGGBB, #RGB or the X11 color name)
  * RYB (Itten's )rtistic color wheel


Installation
============

You can install ``grapefruit`` driectly from PyPY. Just run::

  pip install grapefruit

And you're set.

If you want to use the latest version, you can install directly from the sources
by running::

  pip install git+https://github.com/xav/Grapefruit

You can also use a specific revision (branch/tag/commit)::

  pip install git+https://github.com/xav/Grapefruit@master


Usage
=====

To get complete demo of each function, please read the source code which is
heavily documented and provide a lot of examples in doctest format.

Here is a reduced sample of a common usage scenario:


Conversion of raw color values
------------------------------

+-----------+-----+------+-----------+-----+-----+------+------+-----+-----+-----+-----+---------+-----+-----+-----+
| ↓from/to→ | cmy | cmyk | greyscale | hsl | hsv | html | ints | lab | pil | rgb | ryb | websafe | xyz | yiq | yuv |
+-----------+-----+------+-----------+-----+-----+------+------+-----+-----+-----+-----+---------+-----+-----+-----+
| cmy       |     | yes  |           |     |     |      |      |     |     | yes |     |         |     |     |     |
+-----------+-----+------+-----------+-----+-----+------+------+-----+-----+-----+-----+---------+-----+-----+-----+
| cmyk      | yes |      |           |     |     |      |      |     |     |     |     |         |     |     |     |
+-----------+-----+------+-----------+-----+-----+------+------+-----+-----+-----+-----+---------+-----+-----+-----+
| greyscale |     |      |           |     |     |      |      |     |     |     |     |         |     |     |     |
+-----------+-----+------+-----------+-----+-----+------+------+-----+-----+-----+-----+---------+-----+-----+-----+
| hsl       |     |      |           |     |     |      |      |     |     | yes |     |         |     |     |     |
+-----------+-----+------+-----------+-----+-----+------+------+-----+-----+-----+-----+---------+-----+-----+-----+
| hsv       |     |      |           |     |     |      |      |     |     | yes |     |         |     |     |     |
+-----------+-----+------+-----------+-----+-----+------+------+-----+-----+-----+-----+---------+-----+-----+-----+
| html      |     |      |           |     |     |      |      |     |     | yes |     |         |     |     |     |
+-----------+-----+------+-----------+-----+-----+------+------+-----+-----+-----+-----+---------+-----+-----+-----+
| ints      |     |      |           |     |     |      |      |     |     | yes |     |         |     |     |     |
+-----------+-----+------+-----------+-----+-----+------+------+-----+-----+-----+-----+---------+-----+-----+-----+
| lab       |     |      |           |     |     |      |      |     |     |     |     |         | yes |     |     |
+-----------+-----+------+-----------+-----+-----+------+------+-----+-----+-----+-----+---------+-----+-----+-----+
| pil       |     |      |           |     |     |      |      |     |     | yes |     |         |     |     |     |
+-----------+-----+------+-----------+-----+-----+------+------+-----+-----+-----+-----+---------+-----+-----+-----+
| rgb       | yes |      | yes       | yes | yes | yes  | yes  |     | yes |     | yes | yes     |     | yes | yes |
+-----------+-----+------+-----------+-----+-----+------+------+-----+-----+-----+-----+---------+-----+-----+-----+
| ryb       |     |      |           |     |     |      |      |     |     | yes |     |         | yes |     |     |
+-----------+-----+------+-----------+-----+-----+------+------+-----+-----+-----+-----+---------+-----+-----+-----+
| websafe   |     |      |           |     |     |      |      |     |     |     |     |         |     |     |     |
+-----------+-----+------+-----------+-----+-----+------+------+-----+-----+-----+-----+---------+-----+-----+-----+
| xyz       |     |      |           |     |     |      |      | yes |     | yes |     |         |     |     |     |
+-----------+-----+------+-----------+-----+-----+------+------+-----+-----+-----+-----+---------+-----+-----+-----+
| yiq       |     |      |           |     |     |      |      |     |     | yes |     |         |     |     |     |
+-----------+-----+------+-----------+-----+-----+------+------+-----+-----+-----+-----+---------+-----+-----+-----+
| yuv       |     |      |           |     |     |      |      |     |     | yes |     |         |     |     |     |
+-----------+-----+------+-----------+-----+-----+------+------+-----+-----+-----+-----+---------+-----+-----+-----+


Instantiation
-------------


Reading/Writing values
----------------------


Generate variations of a color
------------------------------


Generate color schemes based on a start color
---------------------------------------------


Contributing
============

Any suggestion or issue is welcome. Push request are very welcome,
please check out the guidelines.



License
=========

::

  Copyright (c) 2008-2016, Xavier Basty

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
