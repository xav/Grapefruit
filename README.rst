=====================
README for GrapeFruit
=====================

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
  * RYB (artistic color wheel
Installing
============

**From the sources:**

Download the latest grapefruit library from:

  https://github.com/xav/Grapefruit


Untar the source distribution and run::

  $ python setup.py build
  $ python setup.py install


Testing
=========

With setuptools installed::

  $ python setup.py test

Without setuptools installed::

  $ python grapefruit_test.py


Documentation
===============

You can download a compiled version of the documentation at:

  https://github.com/xav/Grapefruit/downloads

The documentation is generated from reStructuredText sources by Sphinx.
If you need to build it, go into the doc folder and run::

  make <builder>

Or, if you're running windows::

  makedoc.cmd


License
=========

::

  Copyright (c) 2008, Xavier Basty
  
  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at
  
  http://www.apache.org/licenses/LICENSE-2.0
  
  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
