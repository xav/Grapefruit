.. _grapefruit-index:

========================
GrapeFruit Documentation
========================

Welcome! This is the documentation for GrapeFruit |release|, 
last updated |today|.

See the :ref:`genindex` for a list of the topics.


.. module:: grapefruit
.. moduleauthor:: Xavier Basty <xbasty@gmail.com>

==========================
The Color class
==========================

.. class:: Color

The grapefruit module contains only the :class:`Color` class, which exposes all
the functionnalities. It can be used to store a color value and manipulate it,
or convert it to another color system.

If you are only interested in converting you colors from one system to another,
you can store them using regular tuples instead of :class:`Color` instances.
You can then use the class static methods to perform the conversions.

:class:`Color` stores both the RGB and HSL representation of the color.
This makes possible to keep the hue intact when the color is a pure white
due to its lightness.
However, certain operations work only with the RGB values, and might then
lose the hue.

All the operations assume that you provide values in the specified ranges,
no checks are made whatsoever. If you provide a value outside of the
specified ranges, you'll get some strange results...

The class instances are immutable, all the methods return a new instance
of the :class:`Color` class, and all the properties are read-only.

.. note::

   Some operations may provide results a bit outside the specified ranges,
   the results are not capped.
   This is due to certain color systems having a widers gamut than others.


Class content
---------------

- :ref:`class-constants`

  - :const:`Color.WHITE_REFERENCE`
  - :const:`Color.NAMED_COLOR`

- :ref:`conversion-functions`

  - :meth:`Color.RgbToHsl`
  - :meth:`Color.HslToRgb`
  - :meth:`Color.RgbToHsv`
  - :meth:`Color.HsvToRgb`
  - :meth:`Color.RgbToYiq`
  - :meth:`Color.YiqToRgb`
  - :meth:`Color.RgbToYuv`
  - :meth:`Color.YuvToRgb`
  - :meth:`Color.RgbToXyz`
  - :meth:`Color.XyzToRgb`
  - :meth:`Color.XyzToLab`
  - :meth:`Color.LabToXyz`
  - :meth:`Color.CmykToCmy`
  - :meth:`Color.CmyToCmyk`
  - :meth:`Color.RgbToCmy`
  - :meth:`Color.CmyToRgb`
  - :meth:`Color.RgbToHtml`
  - :meth:`Color.HtmlToRgb`
  - :meth:`Color.RgbToPil`
  - :meth:`Color.PilToRgb`
  - :meth:`Color.RgbToWebSafe`
  - :meth:`Color.RgbToGreyscale`
  - :meth:`Color.RgbToRyb`
  - :meth:`Color.RybToRgb`

- :ref:`instantiation-functions`

  - :meth:`Color.NewFromRgb`
  - :meth:`Color.NewFromHsl`
  - :meth:`Color.NewFromHsv`
  - :meth:`Color.NewFromYiq`
  - :meth:`Color.NewFromYuv`
  - :meth:`Color.NewFromXyz`
  - :meth:`Color.NewFromLab`
  - :meth:`Color.NewFromCmy`
  - :meth:`Color.NewFromCmyk`
  - :meth:`Color.NewFromHtml`
  - :meth:`Color.NewFromPil`

- :ref:`properties`

  - :attr:`Color.alpha`
  - :attr:`Color.whiteRef`
  - :attr:`Color.rgb`
  - :attr:`Color.hue`
  - :attr:`Color.hsl`
  - :attr:`Color.hsv`
  - :attr:`Color.yiq`
  - :attr:`Color.yuv`
  - :attr:`Color.xyz`
  - :attr:`Color.lab`
  - :attr:`Color.cmy`
  - :attr:`Color.cmyk`
  - :attr:`Color.html`
  - :attr:`Color.pil`
  - :attr:`Color.webSafe`
  - :attr:`Color.greyscale`

- :ref:`manipulation-methods`

  - :meth:`Color.ColorWithAlpha`
  - :meth:`Color.ColorWithWhiteRef`
  - :meth:`Color.ColorWithHue`
  - :meth:`Color.ColorWithSaturation`
  - :meth:`Color.ColorWithLightness`
  - :meth:`Color.DarkerColor`
  - :meth:`Color.LighterColor`
  - :meth:`Color.Saturate`
  - :meth:`Color.Desaturate`
  - :meth:`Color.WebSafeDither`

- :ref:`generation-methods`

  - :meth:`Color.ComplementaryColor`
  - :meth:`Color.TriadicScheme`
  - :meth:`Color.TetradicScheme`
  - :meth:`Color.AnalogousScheme`

- :ref:`blending-methods`

  - :meth:`Color.AlphaBlend`
  - :meth:`Color.Blend`


Example usage
---------------

  To create an instance of the grapefruit.Color from RGB values:
  
    >>> import grapefruit
    >>> r, g, b = 1, 0.5, 0
    >>> col = grapefruit.Color.NewFromRgb(r, g, b)
  
  To get the values of the color in another colorspace:
  
    >>> h, s, v = col.hsv
    >>> l, a, b = col.lab
  
  To get the complementary of a color:
  
    >>> compl = col.ComplementaryColor()
    >>> print compl.hsl
    (210.0, 1.0, 0.5)
  
  To directly convert RGB values to their HSL equivalent:
  
    >>> h, s, l = Color.RgbToHsl(r, g, b)



.. _class-constants:

Class Constants
-----------------

.. data:: Color.WHITE_REFERENCE

The reference white points of the CIE standards illuminants, calculated from
the chromaticity coordinates found at:
http://en.wikipedia.org/wiki/Standard_illuminant

A dictionary mapping the name of the CIE standard illuminants to their reference
white points. The white points are required for the XYZ <-> L*a*b conversions.

The key names are build using the following pattern: ``<observer>_<illuminant>``

The possible values for ``<observer>`` are:

  ======  ===================================
  Value   Observer
  ======  ===================================
  std     CIE 1931 2° Standard Observer
  sup     CIE 1964 10° Supplementary Observer
  ======  ===================================

The possible values for ``<illuminant>`` are the name of the standard illuminants:

  ======  ========  ==================================================
  Value   CCT       Illuminant
  ======  ========  ==================================================
  A       2856 K    Incandescent tungsten
  B       4874 K    Direct sunlight at noon (obsolete)
  C       6774 K    North sky daylight (obsolete)
  D50     5003 K    ICC Profile PCS. Horizon light.
  D55     5503 K    Compromise between incandescent and daylight
  D65     6504 K    Noon daylight (TV & sRGB colorspace)
  D75     7504 K    North sky day light
  E       ~5455 K   Equal energy radiator (not a black body)
  F1      6430 K    Daylight Fluorescent
  F2      4230 K    Cool White Fluorescent
  F3      3450 K    White Fluorescent
  F4      2940 K    Warm White Fluorescent
  F5      6350 K    Daylight Fluorescent
  F6      4150 K    Lite White Fluorescent
  F7      6500 K    Broadband fluorescent, D65 simulator
  F8      5000 K    Broadband fluorescent, D50 simulator
  F9      4150 K    Broadband fluorescent, Cool White Deluxe
  F10     5000 K    Narrowband fluorescent, Philips TL85, Ultralume 50
  F11     4000 K    Narrowband fluorescent, Philips TL84, Ultralume 40
  F12     3000 K    Narrowband fluorescent, Philips TL83, Ultralume 30
  ======  ========  ==================================================

.. data:: Color.NAMED_COLOR

The names and RGB values of the X11 colors supported by popular browsers, with
the gray/grey spelling issues, fixed so that both work (e.g light*grey* and
light*gray*).

Note: For *Gray*, *Green*, *Maroon* and *Purple*, the HTML/CSS values are used
instead of the X11 ones
(see `X11/CSS clashes <http://en.wikipedia.org/wiki/X11_color_names#Color_names_that_clash_between_X11_and_HTML.2FCSS>`_)

Reference: `CSS3 Color module <http://www.w3.org/TR/css3-iccprof#x11-color>`_


.. _conversion-functions:

Conversion functions
--------------------

The conversion functions are static methods of the :class:`Color` class that
let you convert a color stored as the list of its components rather than
as a :class:`Color` instance.

.. automethod:: Color.RgbToHsl

.. automethod:: Color.HslToRgb

.. automethod:: Color.RgbToHsv

.. automethod:: Color.HsvToRgb

.. automethod:: Color.RgbToYiq

.. automethod:: Color.YiqToRgb

.. automethod:: Color.RgbToYuv

.. automethod:: Color.YuvToRgb

.. automethod:: Color.RgbToXyz

.. automethod:: Color.XyzToRgb

.. automethod:: Color.XyzToLab

.. automethod:: Color.LabToXyz

.. automethod:: Color.CmykToCmy

.. automethod:: Color.CmyToCmyk

.. automethod:: Color.RgbToCmy

.. automethod:: Color.CmyToRgb

.. automethod:: Color.RgbToHtml

.. automethod:: Color.HtmlToRgb

.. automethod:: Color.RgbToPil

.. automethod:: Color.PilToRgb

.. automethod:: Color.RgbToWebSafe

.. automethod:: Color.RgbToGreyscale

.. automethod:: Color.RgbToRyb

.. automethod:: Color.RybToRgb



.. _instantiation-functions:

Instantiation functions
-----------------------

The instantiation functions let you create a new instance of the :class:`Color`
class from the color components using the color system of your choice.

.. automethod:: Color.NewFromRgb

.. automethod:: Color.NewFromHsl

.. automethod:: Color.NewFromHsv

.. automethod:: Color.NewFromYiq

.. automethod:: Color.NewFromYuv

.. automethod:: Color.NewFromXyz

.. automethod:: Color.NewFromLab

.. automethod:: Color.NewFromCmy

.. automethod:: Color.NewFromCmyk

.. automethod:: Color.NewFromHtml

.. automethod:: Color.NewFromPil



.. _properties:

Properties
----------

The properties get the value of the instance in the specified color model.

The properties returning calculated values unless marked otherwise.

.. note::

   All the properties are read-only. You need to make a copy of the instance
   to modify the color value.

.. autoattribute:: Color.alpha

  *This value is not calculated,  the stored value is returned directly.*

.. autoattribute:: Color.whiteRef

  *This value is not calculated,  the stored value is returned directly.*

.. autoattribute:: Color.rgb

  *This value is not calculated,  the stored value is returned directly.*

.. autoattribute:: Color.hue

  *This value is not calculated,  the stored value is returned directly.*

.. autoattribute:: Color.hsl

  *This value is not calculated,  the stored value is returned directly.*

.. autoattribute:: Color.hsv

.. autoattribute:: Color.yiq

.. autoattribute:: Color.yuv

.. autoattribute:: Color.xyz

.. autoattribute:: Color.lab

.. autoattribute:: Color.cmy

.. autoattribute:: Color.cmyk

.. autoattribute:: Color.html

.. autoattribute:: Color.pil

.. autoattribute:: Color.webSafe

.. attribute:: Color.greyscale



.. _manipulation-methods:

Manipulation methods
--------------------

The manipulations methods let you create a new color by changing an existing
color properties.

.. note::

   The methods **do not** modify the current Color instance. They create a
   new instance or a tuple of new instances with the specified modifications.

.. automethod:: Color.ColorWithAlpha

.. automethod:: Color.ColorWithWhiteRef

.. automethod:: Color.ColorWithHue

.. automethod:: Color.ColorWithSaturation

.. automethod:: Color.ColorWithLightness

.. automethod:: Color.DarkerColor

.. automethod:: Color.LighterColor

.. automethod:: Color.Saturate

.. automethod:: Color.Desaturate

.. automethod:: Color.WebSafeDither



.. _generation-methods:

Generation methods
------------------

The generation methods let you create a color scheme by using a color as the
start point.

All the method, appart from MonochromeScheme, have a 'mode' parameter that
let you choose which color wheel should be used to generate the scheme.

The following modes are available:
  :ryb:
    The `RYB <http://en.wikipedia.org/wiki/RYB_color_model>`_ color wheel,
    or *artistic color wheel*. While scientifically incorrect, it generally
    produces better schemes than RGB.
  :rgb:
    The standard RGB color wheel.

.. automethod:: Color.ComplementaryColor

.. automethod:: Color.MonochromeScheme

.. automethod:: Color.TriadicScheme

.. automethod:: Color.TetradicScheme

.. automethod:: Color.AnalogousScheme



.. _blending-methods:

Blending methods
----------------

.. automethod:: Color.AlphaBlend

.. automethod:: Color.Blend
