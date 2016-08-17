#!/usr/bin/python
# -*- coding: utf-8 -*-#

# Copyright (c) 2008-2016, Xavier Basty
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

"""GrapeFruit - Color manipulation in Python"""

from __future__ import division

import sys

_oneThird = 1.0 / 3
_srgbGammaCorrInv = 0.03928 / 12.92
_sixteenHundredsixteenth = 16.0 / 116

_RybWheel = (
    0,  26,  52,
   83, 120, 130,
  141, 151, 162,
  177, 190, 204,
  218, 232, 246,
  261, 275, 288,
  303, 317, 330,
  338, 345, 352,
  360)

_RgbWheel = (
    0,   8,  17,
   26,  34,  41,
   48,  54,  60,
   81, 103, 123,
  138, 155, 171,
  187, 204, 219,
  234, 251, 267,
  282, 298, 329,
  360)

# Tristumulus values calculated from the CIE chromaticity coordinates on
# https://en.wikipedia.org/wiki/Standard_illuminant#White_points_of_standard_illuminants
WHITE_REFERENCE = {
  # 2° (CIE 1931)
  'std_A'       : (1.098470, 1.000000, 0.355823), # 2856K, Incandescent / Tungsten
  'std_B'       : (0.990927, 1.000000, 0.853133), # 4874K, Direct sunlight at noon (obsolete)
  'std_C'       : (0.980706, 1.000000, 1.182250), # 6774K, Average / North sky Daylight (obsolete)
  'std_D50'     : (0.964212, 1.000000, 0.825188), # 5003K, Horizon Light
  'std_D55'     : (0.956797, 1.000000, 0.921481), # 5503K, Mid-morning / Mid-afternoon Daylight
  'std_D65'     : (0.950429, 1.000000, 1.088900), # 6504K, Noon Daylight (Television, sRGB color space)
  'std_D75'     : (0.949722, 1.000000, 1.226390), # 7504K, North sky Daylight
  'std_E'       : (1.000000, 1.000000, 1.000000), # 5454K, Equal energy
  'std_F1'      : (0.928336, 1.000000, 1.036650), # 6430K, Daylight Fluorescent
  'std_F2'      : (0.991447, 1.000000, 0.673159), # 4230K, Cool White Fluorescent
  'std_F3'      : (1.037530, 1.000000, 0.498605), # 3450K, White Fluorescent
  'std_F4'      : (1.091470, 1.000000, 0.388133), # 2940K, Warm White Fluorescent
  'std_F5'      : (0.908720, 1.000000, 0.987229), # 6350K, Daylight Fluorescent
  'std_F6'      : (0.973091, 1.000000, 0.601905), # 4150K, Lite White Fluorescent
  'std_F7'      : (0.950172, 1.000000, 1.086300), # 6500K, D65 simulator, Daylight simulator
  'std_F8'      : (0.964125, 1.000000, 0.823331), # 5000K, D50 simulator, Sylvania F40 Design 50
  'std_F9'      : (1.003650, 1.000000, 0.678684), # 4150K, Cool White Deluxe Fluorescent
  'std_F10'     : (0.961735, 1.000000, 0.817123), # 5000K, Philips TL85, Ultralume 50
  'std_F11'     : (1.008990, 1.000000, 0.642617), # 4000K, Philips TL84, Ultralume 40
  'std_F12'     : (1.080460, 1.000000, 0.392275), # 3000K, Philips TL83, Ultralume 30
  # 10° (CIE 1964)
  'sup_A'       : (1.111420, 1.000000, 0.351998),
  'sup_B'       : (0.991778, 1.000000, 0.843493),
  'sup_C'       : (0.972857, 1.000000, 1.161450),
  'sup_D50'     : (0.967206, 1.000000, 0.814280),
  'sup_D55'     : (0.957967, 1.000000, 0.909253),
  'sup_D65'     : (0.948097, 1.000000, 1.073050),
  'sup_D75'     : (0.944171, 1.000000, 1.206430),
  'sup_E'       : (1.000000, 1.000000, 1.000000),
  'sup_F1'      : (0.947913, 1.000000, 1.031910),
  'sup_F2'      : (1.032450, 1.000000, 0.689897),
  'sup_F3'      : (1.089680, 1.000000, 0.519648),
  'sup_F4'      : (1.149610, 1.000000, 0.409633),
  'sup_F5'      : (0.933686, 1.000000, 0.986363),
  'sup_F6'      : (1.021480, 1.000000, 0.620736),
  'sup_F7'      : (0.957797, 1.000000, 1.076180),
  'sup_F8'      : (0.971146, 1.000000, 0.811347),
  'sup_F9'      : (1.021160, 1.000000, 0.678256),
  'sup_F10'     : (0.990012, 1.000000, 0.831340),
  'sup_F11'     : (1.038200, 1.000000, 0.655550),
  'sup_F12'     : (1.114280, 1.000000, 0.403530)}

# The default white reference, use 2° Standard Observer, D65 (daylight)
_DEFAULT_WREF = WHITE_REFERENCE['std_D65']


NAMED_COLOR = {
  'aliceblue':            '#f0f8ff',
  'antiquewhite':         '#faebd7',
  'aqua':                 '#00ffff',
  'aquamarine':           '#7fffd4',
  'azure':                '#f0ffff',
  'beige':                '#f5f5dc',
  'bisque':               '#ffe4c4',
  'black':                '#000000',
  'blanchedalmond':       '#ffebcd',
  'blue':                 '#0000ff',
  'blueviolet':           '#8a2be2',
  'brown':                '#a52a2a',
  'burlywood':            '#deb887',
  'cadetblue':            '#5f9ea0',
  'chartreuse':           '#7fff00',
  'chocolate':            '#d2691e',
  'coral':                '#ff7f50',
  'cornflowerblue':       '#6495ed',
  'cornsilk':             '#fff8dc',
  'crimson':              '#dc143c',
  'cyan':                 '#00ffff',
  'darkblue':             '#00008b',
  'darkcyan':             '#008b8b',
  'darkgoldenrod':        '#b8860b',
  'darkgray':             '#a9a9a9',
  'darkgrey':             '#a9a9a9',
  'darkgreen':            '#006400',
  'darkkhaki':            '#bdb76b',
  'darkmagenta':          '#8b008b',
  'darkolivegreen':       '#556b2f',
  'darkorange':           '#ff8c00',
  'darkorchid':           '#9932cc',
  'darkred':              '#8b0000',
  'darksalmon':           '#e9967a',
  'darkseagreen':         '#8fbc8f',
  'darkslateblue':        '#483d8b',
  'darkslategray':        '#2f4f4f',
  'darkslategrey':        '#2f4f4f',
  'darkturquoise':        '#00ced1',
  'darkviolet':           '#9400d3',
  'deeppink':             '#ff1493',
  'deepskyblue':          '#00bfff',
  'dimgray':              '#696969',
  'dimgrey':              '#696969',
  'dodgerblue':           '#1e90ff',
  'firebrick':            '#b22222',
  'floralwhite':          '#fffaf0',
  'forestgreen':          '#228b22',
  'fuchsia':              '#ff00ff',
  'gainsboro':            '#dcdcdc',
  'ghostwhite':           '#f8f8ff',
  'gold':                 '#ffd700',
  'goldenrod':            '#daa520',
  'gray':                 '#808080',
  'grey':                 '#808080',
  'green':                '#008000',
  'greenyellow':          '#adff2f',
  'honeydew':             '#f0fff0',
  'hotpink':              '#ff69b4',
  'indianred':            '#cd5c5c',
  'indigo':               '#4b0082',
  'ivory':                '#fffff0',
  'khaki':                '#f0e68c',
  'lavender':             '#e6e6fa',
  'lavenderblush':        '#fff0f5',
  'lawngreen':            '#7cfc00',
  'lemonchiffon':         '#fffacd',
  'lightblue':            '#add8e6',
  'lightcoral':           '#f08080',
  'lightcyan':            '#e0ffff',
  'lightgoldenrodyellow': '#fafad2',
  'lightgreen':           '#90ee90',
  'lightgray':            '#d3d3d3',
  'lightgrey':            '#d3d3d3',
  'lightpink':            '#ffb6c1',
  'lightsalmon':          '#ffa07a',
  'lightseagreen':        '#20b2aa',
  'lightskyblue':         '#87cefa',
  'lightslategray':       '#778899',
  'lightslategrey':       '#778899',
  'lightsteelblue':       '#b0c4de',
  'lightyellow':          '#ffffe0',
  'lime':                 '#00ff00',
  'limegreen':            '#32cd32',
  'linen':                '#faf0e6',
  'magenta':              '#ff00ff',
  'maroon':               '#800000',
  'mediumaquamarine':     '#66cdaa',
  'mediumblue':           '#0000cd',
  'mediumorchid':         '#ba55d3',
  'mediumpurple':         '#9370db',
  'mediumseagreen':       '#3cb371',
  'mediumslateblue':      '#7b68ee',
  'mediumspringgreen':    '#00fa9a',
  'mediumturquoise':      '#48d1cc',
  'mediumvioletred':      '#c71585',
  'midnightblue':         '#191970',
  'mintcream':            '#f5fffa',
  'mistyrose':            '#ffe4e1',
  'moccasin':             '#ffe4b5',
  'navajowhite':          '#ffdead',
  'navy':                 '#000080',
  'oldlace':              '#fdf5e6',
  'olive':                '#808000',
  'olivedrab':            '#6b8e23',
  'orange':               '#ffa500',
  'orangered':            '#ff4500',
  'orchid':               '#da70d6',
  'palegoldenrod':        '#eee8aa',
  'palegreen':            '#98fb98',
  'paleturquoise':        '#afeeee',
  'palevioletred':        '#db7093',
  'papayawhip':           '#ffefd5',
  'peachpuff':            '#ffdab9',
  'peru':                 '#cd853f',
  'pink':                 '#ffc0cb',
  'plum':                 '#dda0dd',
  'powderblue':           '#b0e0e6',
  'purple':               '#800080',
  'red':                  '#ff0000',
  'rosybrown':            '#bc8f8f',
  'royalblue':            '#4169e1',
  'saddlebrown':          '#8b4513',
  'salmon':               '#fa8072',
  'sandybrown':           '#f4a460',
  'seagreen':             '#2e8b57',
  'seashell':             '#fff5ee',
  'sienna':               '#a0522d',
  'silver':               '#c0c0c0',
  'skyblue':              '#87ceeb',
  'slateblue':            '#6a5acd',
  'slategray':            '#708090',
  'slategrey':            '#708090',
  'snow':                 '#fffafa',
  'springgreen':          '#00ff7f',
  'steelblue':            '#4682b4',
  'tan':                  '#d2b48c',
  'teal':                 '#008080',
  'thistle':              '#d8bfd8',
  'tomato':               '#ff6347',
  'turquoise':            '#40e0d0',
  'violet':               '#ee82ee',
  'wheat':                '#f5deb3',
  'white':                '#ffffff',
  'whitesmoke':           '#f5f5f5',
  'yellow':               '#ffff00',
  'yellowgreen':          '#9acd32'}

def rgb_to_hsl(r, g=None, b=None):
  """Convert the color from RGB coordinates to HSL.

  Parameters:
    :r:
      The Red component value [0...1]
    :g:
      The Green component value [0...1]
    :b:
      The Blue component value [0...1]

  Returns:
    The color as an (h, s, l) tuple in the range:
    h[0...360],
    s[0...1],
    l[0...1]

  >>> rgb_to_hsl(1, 0.5, 0)
  (30.0, 1.0, 0.5)

  """
  if type(r) in [list,tuple]:
    r, g, b = r

  minVal = min(r, g, b)       # min RGB value
  maxVal = max(r, g, b)       # max RGB value

  l = (maxVal + minVal) / 2.0
  if minVal==maxVal:
    return (0.0, 0.0, l)    # achromatic (gray)

  d = maxVal - minVal         # delta RGB value

  if l < 0.5: s = d / (maxVal + minVal)
  else: s = d / (2.0 - maxVal - minVal)

  dr, dg, db = [(maxVal-val) / d for val in (r, g, b)]

  if r==maxVal:
    h = db - dg
  elif g==maxVal:
    h = 2.0 + dr - db
  else:
    h = 4.0 + dg - dr

  h = (h*60.0) % 360.0
  return (h, s, l)

def _hue_to_rgb(n1, n2=None, h=None):
  if type(n1) in [list,tuple]:
    n1, n2, h = n1

  h %= 6.0
  if h < 1.0: return n1 + ((n2-n1) * h)
  if h < 3.0: return n2
  if h < 4.0: return n1 + ((n2-n1) * (4.0 - h))
  return n1

def hsl_to_rgb(h, s=None, l=None):
  """Convert the color from HSL coordinates to RGB.

  Parameters:
    :h:
      The Hue component value [0...1]
    :s:
      The Saturation component value [0...1]
    :l:
      The Lightness component value [0...1]

  Returns:
    The color as an (r, g, b) tuple in the range:
    r[0...1],
    g[0...1],
    b[0...1]

  >>> hsl_to_rgb(30.0, 1.0, 0.5)
  (1.0, 0.5, 0.0)

  """
  if type(h) in [list,tuple]:
    h, s, l = h

  if s==0: return (l, l, l)   # achromatic (gray)

  if l<0.5: n2 = l * (1.0 + s)
  else: n2 = l+s - (l*s)

  n1 = (2.0 * l) - n2

  h /= 60.0
  hueToRgb = _hue_to_rgb
  r = hueToRgb(n1, n2, h + 2)
  g = hueToRgb(n1, n2, h)
  b = hueToRgb(n1, n2, h - 2)

  return (r, g, b)

def rgb_to_hsv(r, g=None, b=None):
  """Convert the color from RGB coordinates to HSV.

  Parameters:
    :r:
      The Red component value [0...1]
    :g:
      The Green component value [0...1]
    :b:
      The Blue component value [0...1]

  Returns:
    The color as an (h, s, v) tuple in the range:
    h[0...360],
    s[0...1],
    v[0...1]

  >>> rgb_to_hsv(1, 0.5, 0)
  (30.0, 1.0, 1.0)

  """
  if type(r) in [list,tuple]:
    r, g, b = r

  v = float(max(r, g, b))
  d = v - min(r, g, b)
  if d==0: return (0.0, 0.0, v)
  s = d / v

  dr, dg, db = [(v - val) / d for val in (r, g, b)]

  if r==v:
    h = db - dg             # between yellow & magenta
  elif g==v:
    h = 2.0 + dr - db       # between cyan & yellow
  else: # b==v
    h = 4.0 + dg - dr       # between magenta & cyan

  h = (h*60.0) % 360.0
  return (h, s, v)

def hsv_to_rgb(h, s=None, v=None):
  """Convert the color from RGB coordinates to HSV.

  Parameters:
    :h:
      The Hus component value [0...1]
    :s:
      The Saturation component value [0...1]
    :v:
      The Value component [0...1]

  Returns:
    The color as an (r, g, b) tuple in the range:
    r[0...1],
    g[0...1],
    b[0...1]

  >>> hsv_to_rgb(30.0, 1.0, 0.5)
  (0.5, 0.25, 0.0)

  """
  if type(h) in [list,tuple]:
    h, s, v = h

  if s==0: return (v, v, v)   # achromatic (gray)

  h /= 60.0
  h = h % 6.0

  i = int(h)
  f = h - i
  if not(i&1): f = 1-f     # if i is even

  m = v * (1.0 - s)
  n = v * (1.0 - (s * f))

  if i==0: return (v, n, m)
  if i==1: return (n, v, m)
  if i==2: return (m, v, n)
  if i==3: return (m, n, v)
  if i==4: return (n, m, v)
  return (v, m, n)

def rgb_to_yiq(r, g=None, b=None):
  """Convert the color from RGB to YIQ.

  Parameters:
    :r:
      The Red component value [0...1]
    :g:
      The Green component value [0...1]
    :b:
      The Blue component value [0...1]

  Returns:
    The color as an (y, i, q) tuple in the range:
    y[0...1],
    i[0...1],
    q[0...1]

  >>> '(%g, %g, %g)' % rgb_to_yiq(1, 0.5, 0)
  '(0.592263, 0.458874, -0.0499818)'

  """
  if type(r) in [list,tuple]:
    r, g, b = r

  y = (r * 0.29895808) + (g * 0.58660979) + (b *0.11443213)
  i = (r * 0.59590296) - (g * 0.27405705) - (b *0.32184591)
  q = (r * 0.21133576) - (g * 0.52263517) + (b *0.31129940)
  return (y, i, q)

def yiq_to_rgb(y, i=None, q=None):
  """Convert the color from YIQ coordinates to RGB.

  Parameters:
    :y:
      Tte Y component value [0...1]
    :i:
      The I component value [0...1]
    :q:
      The Q component value [0...1]

  Returns:
    The color as an (r, g, b) tuple in the range:
    r[0...1],
    g[0...1],
    b[0...1]

  >>> '({}, {}, {})'.format(*[round(v, 6) for v in yiq_to_rgb(0.592263, 0.458874, -0.0499818)])
  '(1.0, 0.5, 1e-06)'

  """
  if type(y) in [list,tuple]:
    y, i, q = y
  r = y + (i * 0.9562) + (q * 0.6210)
  g = y - (i * 0.2717) - (q * 0.6485)
  b = y - (i * 1.1053) + (q * 1.7020)
  return (r, g, b)

def rgb_to_yuv(r, g=None, b=None):
  """Convert the color from RGB coordinates to YUV.

  Parameters:
    :r:
      The Red component value [0...1]
    :g:
      The Green component value [0...1]
    :b:
      The Blue component value [0...1]

  Returns:
    The color as an (y, u, v) tuple in the range:
    y[0...1],
    u[-0.436...0.436],
    v[-0.615...0.615]

  >>> '(%g, %g, %g)' % rgb_to_yuv(1, 0.5, 0)
  '(0.5925, -0.29156, 0.357505)'

  """
  if type(r) in [list,tuple]:
    r, g, b = r

  y =  (r * 0.29900) + (g * 0.58700) + (b * 0.11400)
  u = -(r * 0.14713) - (g * 0.28886) + (b * 0.43600)
  v =  (r * 0.61500) - (g * 0.51499) - (b * 0.10001)
  return (y, u, v)

def yuv_to_rgb(y, u=None, v=None):
  """Convert the color from YUV coordinates to RGB.

  Parameters:
    :y:
      The Y component value [0...1]
    :u:
      The U component value [-0.436...0.436]
    :v:
      The V component value [-0.615...0.615]

  Returns:
    The color as an (r, g, b) tuple in the range:
    r[0...1],
    g[0...1],
    b[0...1]

  >>> '(%g, %g, %g)' % yuv_to_rgb(0.5925, -0.2916, 0.3575)
  '(0.999989, 0.500015, -6.3276e-05)'

  """
  if type(y) in [list,tuple]:
    y, u, v = y
  r = y + (v * 1.13983)
  g = y - (u * 0.39465) - (v * 0.58060)
  b = y + (u * 2.03211)
  return (r, g, b)

def rgb_to_xyz(r, g=None, b=None):
  """Convert the color from sRGB to CIE XYZ.

  The methods assumes that the RGB coordinates are given in the sRGB
  colorspace (D65).

  .. note::

     Compensation for the sRGB gamma correction is applied before converting.

  Parameters:
    :r:
      The Red component value [0...1]
    :g:
      The Green component value [0...1]
    :b:
      The Blue component value [0...1]

  Returns:
    The color as an (x, y, z) tuple in the range:
    x[0...1],
    y[0...1],
    z[0...1]

  >>> '(%g, %g, %g)' % rgb_to_xyz(1, 0.5, 0)
  '(0.488941, 0.365682, 0.0448137)'

  """
  if type(r) in [list,tuple]:
    r, g, b = r

  r, g, b = [((v <= 0.03928) and [v / 12.92] or [((v+0.055) / 1.055) **2.4])[0] for v in (r, g, b)]

  x = (r * 0.4124) + (g * 0.3576) + (b * 0.1805)
  y = (r * 0.2126) + (g * 0.7152) + (b * 0.0722)
  z = (r * 0.0193) + (g * 0.1192) + (b * 0.9505)
  return (x, y, z)

def xyz_to_rgb(x, y=None, z=None):
  """Convert the color from CIE XYZ coordinates to sRGB.

  .. note::

     Compensation for sRGB gamma correction is applied before converting.

  Parameters:
    :x:
      The X component value [0...1]
    :y:
      The Y component value [0...1]
    :z:
      The Z component value [0...1]

  Returns:
    The color as an (r, g, b) tuple in the range:
    r[0...1],
    g[0...1],
    b[0...1]

  >>> '(%g, %g, %g)' % xyz_to_rgb(0.488941, 0.365682, 0.0448137)
  '(1, 0.5, 6.81883e-08)'

  """
  if type(x) in [list,tuple]:
    x, y, z = x
  r =  (x * 3.2406255) - (y * 1.5372080) - (z * 0.4986286)
  g = -(x * 0.9689307) + (y * 1.8757561) + (z * 0.0415175)
  b =  (x * 0.0557101) - (y * 0.2040211) + (z * 1.0569959)
  return tuple((((v <= _srgbGammaCorrInv) and [v * 12.92] or [(1.055 * (v ** (1/2.4))) - 0.055])[0] for v in (r, g, b)))

def xyz_to_lab(x, y=None, z=None, wref=_DEFAULT_WREF):
  """Convert the color from CIE XYZ to CIE L*a*b*.

  Parameters:
    :x:
      The X component value [0...1]
    :y:
      The Y component value [0...1]
    :z:
      The Z component value [0...1]
    :wref:
      The whitepoint reference, default is 2° D65.

  Returns:
    The color as an (L, a, b) tuple in the range:
    L[0...100],
    a[-1...1],
    b[-1...1]

  >>> '(%g, %g, %g)' % xyz_to_lab(0.488941, 0.365682, 0.0448137)
  '(66.9518, 0.430841, 0.739692)'

  >>> '(%g, %g, %g)' % xyz_to_lab(0.488941, 0.365682, 0.0448137, WHITE_REFERENCE['std_D50'])
  '(66.9518, 0.41166, 0.67282)'

  """
  if type(x) in [list,tuple]:
    x, y, z = x
  # White point correction
  x /= wref[0]
  y /= wref[1]
  z /= wref[2]

  # Nonlinear distortion and linear transformation
  x, y, z = [((v > 0.008856) and [v**_oneThird] or [(7.787 * v) + _sixteenHundredsixteenth])[0] for v in (x, y, z)]

  # Vector scaling
  l = (116 * y) - 16
  a = 5.0 * (x - y)
  b = 2.0 * (y - z)

  return (l, a, b)

def lab_to_xyz(l, a=None, b=None, wref=_DEFAULT_WREF):
  """Convert the color from CIE L*a*b* to CIE 1931 XYZ.

  Parameters:
    :l:
      The L component [0...100]
    :a:
      The a component [-1...1]
    :b:
      The a component [-1...1]
    :wref:
      The whitepoint reference, default is 2° D65.

  Returns:
    The color as an (x, y, z) tuple in the range:
    x[0...q],
    y[0...1],
    z[0...1]

  >>> '(%g, %g, %g)' % lab_to_xyz(66.9518, 0.43084, 0.739692)
  '(0.48894, 0.365682, 0.0448137)'

  >>> '(%g, %g, %g)' % lab_to_xyz(66.9518, 0.411663, 0.67282, WHITE_REFERENCE['std_D50'])
  '(0.488942, 0.365682, 0.0448137)'

  """
  if type(l) in [list,tuple]:
    l, a, b = l
  y = (l + 16) / 116
  x = (a / 5.0) + y
  z = y - (b / 2.0)
  return tuple((((v > 0.206893) and [v**3] or [(v - _sixteenHundredsixteenth) / 7.787])[0] * w for v, w in zip((x, y, z), wref)))

def cmyk_to_cmy(c, m=None, y=None, k=None):
  """Convert the color from CMYK coordinates to CMY.

  Parameters:
    :c:
      The Cyan component value [0...1]
    :m:
      The Magenta component value [0...1]
    :y:
      The Yellow component value [0...1]
    :k:
      The Black component value [0...1]

  Returns:
    The color as an (c, m, y) tuple in the range:
    c[0...1],
    m[0...1],
    y[0...1]

  >>> '(%g, %g, %g)' % cmyk_to_cmy(1, 0.32, 0, 0.5)
  '(1, 0.66, 0.5)'

  """
  if type(c) in [list,tuple]:
    c, m, y, k = c
  mk = 1-k
  return ((c*mk + k), (m*mk + k), (y*mk + k))

def cmy_to_cmyk(c, m=None, y=None):
  """Convert the color from CMY coordinates to CMYK.

  Parameters:
    :c:
      The Cyan component value [0...1]
    :m:
      The Magenta component value [0...1]
    :y:
      The Yellow component value [0...1]

  Returns:
    The color as an (c, m, y, k) tuple in the range:
    c[0...1],
    m[0...1],
    y[0...1],
    k[0...1]

  >>> '(%g, %g, %g, %g)' % cmy_to_cmyk(1, 0.66, 0.5)
  '(1, 0.32, 0, 0.5)'

  """
  if type(c) in [list,tuple]:
    c, m, y = c
  k = min(c, m, y)
  if k==1.0: return (0.0, 0.0, 0.0, 1.0)
  mk = 1.0-k
  return ((c-k) / mk, (m-k) / mk, (y-k) / mk, k)

def rgb_to_cmy(r, g=None, b=None):
  """Convert the color from RGB coordinates to CMY.

  Parameters:
    :r:
      The Red component value [0...1]
    :g:
      The Green component value [0...1]
    :b:
      The Blue component value [0...1]

  Returns:
    The color as an (c, m, y) tuple in the range:
    c[0...1],
    m[0...1],
    y[0...1]

  >>> rgb_to_cmy(1, 0.5, 0)
  (0, 0.5, 1)

  """
  if type(r) in [list,tuple]:
    r, g, b = r
  return (1-r, 1-g, 1-b)

def cmy_to_rgb(c, m=None, y=None):
  """Convert the color from CMY coordinates to RGB.

  Parameters:
    :c:
      The Cyan component value [0...1]
    :m:
      The Magenta component value [0...1]
    :y:
      The Yellow component value [0...1]

  Returns:
    The color as an (r, g, b) tuple in the range:
    r[0...1],
    g[0...1],
    b[0...1]

  >>> cmy_to_rgb(0, 0.5, 1)
  (1, 0.5, 0)

  """
  if type(c) in [list,tuple]:
    c, m, y = c
  return (1-c, 1-m, 1-y)

def rgb_to_ints(r, g=None, b=None):
  """Convert the color in the standard [0...1] range to ints in the [0..255] range.

  Parameters:
    :r:
      The Red component value [0...1]
    :g:
      The Green component value [0...1]
    :b:
      The Blue component value [0...1]

  Returns:
    The color as an (r, g, b) tuple in the range:
    r[0...255],
    g[0...2551],
    b[0...2551]

  >>> rgb_to_ints(1, 0.5, 0)
  (255, 128, 0)

  """
  if type(r) in [list,tuple]:
    r, g, b = r
  return tuple(int(round(v*255)) for v in (r, g, b))

def ints_to_rgb(r, g=None, b=None):
  """Convert ints in the [0...255] range to the standard [0...1] range.

  Parameters:
    :r:
      The Red component value [0...255]
    :g:
      The Green component value [0...255]
    :b:
      The Blue component value [0...255]

  Returns:
    The color as an (r, g, b) tuple in the range:
    r[0...1],
    g[0...1],
    b[0...1]

  >>> '(%g, %g, %g)' % ints_to_rgb((255, 128, 0))
  '(1, 0.501961, 0)'

  """
  if type(r) in [list,tuple]:
    r, g, b = r
  return tuple(float(v) / 255.0 for v in [r, g, b])

def rgb_to_html(r, g=None, b=None):
  """Convert the color from (r, g, b) to #RRGGBB.

  Parameters:
    :r:
      The Red component value [0...1]
    :g:
      The Green component value [0...1]
    :b:
      The Blue component value [0...1]

  Returns:
    A CSS string representation of this color (#RRGGBB).

  >>> rgb_to_html(1, 0.5, 0)
  '#ff8000'

  """
  if type(r) in [list,tuple]:
    r, g, b = r
  return '#%02x%02x%02x' % tuple((min(round(v*255), 255) for v in (r, g, b)))

def html_to_rgb(html):
  """Convert the HTML color to (r, g, b).

  Parameters:
    :html:
      the HTML definition of the color (#RRGGBB or #RGB or a color name).

  Returns:
    The color as an (r, g, b) tuple in the range:
    r[0...1],
    g[0...1],
    b[0...1]

  Throws:
    :ValueError:
      If html is neither a known color name or a hexadecimal RGB
      representation.

  >>> '(%g, %g, %g)' % html_to_rgb('#ff8000')
  '(1, 0.501961, 0)'
  >>> '(%g, %g, %g)' % html_to_rgb('ff8000')
  '(1, 0.501961, 0)'
  >>> '(%g, %g, %g)' % html_to_rgb('#f60')
  '(1, 0.4, 0)'
  >>> '(%g, %g, %g)' % html_to_rgb('f60')
  '(1, 0.4, 0)'
  >>> '(%g, %g, %g)' % html_to_rgb('lemonchiffon')
  '(1, 0.980392, 0.803922)'

  """
  html = html.strip().lower()
  if html[0]=='#':
    html = html[1:]
  elif html in NAMED_COLOR:
    html = NAMED_COLOR[html][1:]

  if len(html)==6:
    rgb = html[:2], html[2:4], html[4:]
  elif len(html)==3:
    rgb = ['%c%c' % (v,v) for v in html]
  else:
    raise ValueError("input #%s is not in #RRGGBB format" % html)

  return tuple(((int(n, 16) / 255.0) for n in rgb))

def rgb_to_pil(r, g=None, b=None):
  """Convert the color from RGB to a PIL-compatible integer.

  Parameters:
    :r:
      The Red component value [0...1]
    :g:
      The Green component value [0...1]
    :b:
      The Blue component value [0...1]

  Returns:
    A PIL compatible integer (0xBBGGRR).

  >>> '0x%06x' % rgb_to_pil(1, 0.5, 0)
  '0x0080ff'

  """
  if type(r) in [list,tuple]:
    r, g, b = r
  r, g, b = [min(int(round(v*255)), 255) for v in (r, g, b)]
  return (b << 16) + (g << 8) + r

def pil_to_rgb(pil):
  """Convert the color from a PIL-compatible integer to RGB.

  Parameters:
    pil: a PIL compatible color representation (0xBBGGRR)
  Returns:
    The color as an (r, g, b) tuple in the range:
    the range:
    r: [0...1]
    g: [0...1]
    b: [0...1]

  >>> '(%g, %g, %g)' % pil_to_rgb(0x0080ff)
  '(1, 0.501961, 0)'

  """
  r = 0xff & pil
  g = 0xff & (pil >> 8)
  b = 0xff & (pil >> 16)
  return tuple((v / 255.0 for v in (r, g, b)))

def _websafe_component(c, alt=False):
  """Convert a color component to its web safe equivalent.

  Parameters:
    :c:
      The component value [0...1]
    :alt:
      If True, return the alternative value instead of the nearest one.

  Returns:
    The web safe equivalent of the component value.

  """
  # This sucks, but floating point between 0 and 1 is quite fuzzy...
  # So we just change the scale a while to make the equality tests
  # work, otherwise it gets wrong at some decimal far to the right.
  sc = c * 100.0

  # If the color is already safe, return it straight away
  d = sc % 20
  if d==0: return c

  # Get the lower and upper safe values
  l = sc - d
  u = l + 20

  # Return the 'closest' value according to the alt flag
  if alt:
    if (sc-l) >= (u-sc): return l/100.0
    else: return u/100.0
  else:
    if (sc-l) >= (u-sc): return u/100.0
    else: return l/100.0

def rgb_to_websafe(r, g=None, b=None, alt=False):
  """Convert the color from RGB to 'web safe' RGB

  Parameters:
    :r:
      The Red component value [0...1]
    :g:
      The Green component value [0...1]
    :b:
      The Blue component value [0...1]
    :alt:
      If True, use the alternative color instead of the nearest one.
      Can be used for dithering.

  Returns:
    The color as an (r, g, b) tuple in the range:
    the range:
    r[0...1],
    g[0...1],
    b[0...1]

  >>> '(%g, %g, %g)' % rgb_to_websafe(1, 0.55, 0.0)
  '(1, 0.6, 0)'

  """
  if type(r) in [list,tuple]:
    r, g, b = r
  websafeComponent = _websafe_component
  return tuple((websafeComponent(v, alt) for v in (r, g, b)))

def rgb_to_greyscale(r, g=None, b=None):
  """Convert the color from RGB to its greyscale equivalent

  Parameters:
    :r:
      The Red component value [0...1]
    :g:
      The Green component value [0...1]
    :b:
      The Blue component value [0...1]

  Returns:
    The color as an (r, g, b) tuple in the range:
    the range:
    r[0...1],
    g[0...1],
    b[0...1]

  >>> '(%g, %g, %g)' % rgb_to_greyscale(1, 0.8, 0)
  '(0.6, 0.6, 0.6)'

  """
  if type(r) in [list,tuple]:
    r, g, b = r
  v = (r + g + b) / 3.0
  return (v, v, v)

def rgb_to_ryb(hue):
  """Maps a hue on the RGB color wheel to Itten's RYB wheel.

  Parameters:
    :hue:
      The hue on the RGB color wheel [0...360]

  Returns:
    An approximation of the corresponding hue on Itten's RYB wheel.

  >>> rgb_to_ryb(15)
  26.0

  """
  d = hue % 15
  i = int(hue / 15)
  x0 = _RybWheel[i]
  x1 = _RybWheel[i+1]
  return x0 + (x1-x0) * d / 15

def ryb_to_rgb(hue):
  """Maps a hue on Itten's RYB color wheel to the standard RGB wheel.

  Parameters:
    :hue:
      The hue on Itten's RYB color wheel [0...360]

  Returns:
    An approximation of the corresponding hue on the standard RGB wheel.

  >>> ryb_to_rgb(15)
  8.0

  """
  d = hue % 15
  i = int(hue / 15)
  x0 = _RgbWheel[i]
  x1 = _RgbWheel[i+1]
  return x0 + (x1-x0) * d / 15


class Color(object):
  """Hold a color value.

  Example usage:

  To create an instance of the grapefruit.Color from RGB values:

    >>> import grapefruit
    >>> r, g, b = 1, 0.5, 0
    >>> col = grapefruit.Color.from_rgb(r, g, b)

  To get the values of the color in another colorspace:

    >>> h, s, v = col.hsv
    >>> l, a, b = col.lab

  To get the complementary of a color:

    >>> compl = col.complementary_color(mode='rgb')
    >>> compl.hsl
    (210.0, 1.0, 0.5)

  To directly convert RGB values to their HSL equivalent:

    >>> h, s, l = rgb_to_hsl(r, g, b)

  """

  # --==================--------------------------------------------------------
  # -- Creation methods --
  # --==================--

  @staticmethod
  def from_rgb(r, g, b, alpha=1.0, wref=_DEFAULT_WREF):
    """Create a new instance based on the specifed RGB values.

    Parameters:
      :r:
        The Red component value [0...1]
      :g:
        The Green component value [0...1]
      :b:
        The Blue component value [0...1]
      :alpha:
        The color transparency [0...1], default is opaque
      :wref:
        The whitepoint reference, default is 2° D65.

    Returns:
      A grapefruit.Color instance.

    >>> Color.from_rgb(1.0, 0.5, 0.0)
    Color(1.0, 0.5, 0.0, 1.0)
    >>> Color.from_rgb(1.0, 0.5, 0.0, 0.5)
    Color(1.0, 0.5, 0.0, 0.5)

    """
    return Color((r, g, b), 'rgb', alpha, wref)

  @staticmethod
  def from_hsl(h, s, l, alpha=1.0, wref=_DEFAULT_WREF):
    """Create a new instance based on the specifed HSL values.

    Parameters:
      :h:
        The Hue component value [0...1]
      :s:
        The Saturation component value [0...1]
      :l:
        The Lightness component value [0...1]
      :alpha:
        The color transparency [0...1], default is opaque
      :wref:
        The whitepoint reference, default is 2° D65.

    Returns:
      A grapefruit.Color instance.

    >>> Color.from_hsl(30, 1, 0.5)
    Color(1.0, 0.5, 0.0, 1.0)
    >>> Color.from_hsl(30, 1, 0.5, 0.5)
    Color(1.0, 0.5, 0.0, 0.5)

    """
    return Color((h, s, l), 'hsl', alpha, wref)

  @staticmethod
  def from_hsv(h, s, v, alpha=1.0, wref=_DEFAULT_WREF):
    """Create a new instance based on the specifed HSV values.

    Parameters:
      :h:
        The Hus component value [0...1]
      :s:
        The Saturation component value [0...1]
      :v:
        The Value component [0...1]
      :alpha:
        The color transparency [0...1], default is opaque
      :wref:
        The whitepoint reference, default is 2° D65.

    Returns:
      A grapefruit.Color instance.

    >>> Color.from_hsv(30, 1, 1)
    Color(1.0, 0.5, 0.0, 1.0)
    >>> Color.from_hsv(30, 1, 1, 0.5)
    Color(1.0, 0.5, 0.0, 0.5)

    """
    h2, s, l = rgb_to_hsl(*hsv_to_rgb(h, s, v))
    return Color((h, s, l), 'hsl', alpha, wref)

  @staticmethod
  def from_yiq(y, i, q, alpha=1.0, wref=_DEFAULT_WREF):
    """Create a new instance based on the specifed YIQ values.

    Parameters:
      :y:
        The Y component value [0...1]
      :i:
        The I component value [0...1]
      :q:
        The Q component value [0...1]
      :alpha:
        The color transparency [0...1], default is opaque
      :wref:
        The whitepoint reference, default is 2° D65.

    Returns:
      A grapefruit.Color instance.

    >>> Color.from_yiq(0.5922, 0.45885,-0.05)
    Color(0.999902, 0.499955, -6.7e-05, 1.0)
    >>> Color.from_yiq(0.5922, 0.45885,-0.05, 0.5)
    Color(0.999902, 0.499955, -6.7e-05, 0.5)

    """
    return Color(yiq_to_rgb(y, i, q), 'rgb', alpha, wref)

  @staticmethod
  def from_yuv(y, u, v, alpha=1.0, wref=_DEFAULT_WREF):
    """Create a new instance based on the specifed YUV values.

    Parameters:
      :y:
        The Y component value [0...1]
      :u:
        The U component value [-0.436...0.436]
      :v:
        The V component value [-0.615...0.615]
      :alpha:
        The color transparency [0...1], default is opaque
      :wref:
        The whitepoint reference, default is 2° D65.

    Returns:
      A grapefruit.Color instance.

    >>> Color.from_yuv(0.5925, -0.2916, 0.3575)
    Color(0.999989, 0.500015, -6.3e-05, 1.0)
    >>> Color.from_yuv(0.5925, -0.2916, 0.3575, 0.5)
    Color(0.999989, 0.500015, -6.3e-05, 0.5)

    """
    return Color(yuv_to_rgb(y, u, v), 'rgb', alpha, wref)

  @staticmethod
  def from_xyz(x, y, z, alpha=1.0, wref=_DEFAULT_WREF):
    """Create a new instance based on the specifed CIE-XYZ values.

    Parameters:
      :x:
        The Red component value [0...1]
      :y:
        The Green component value [0...1]
      :z:
        The Blue component value [0...1]
      :alpha:
        The color transparency [0...1], default is opaque
      :wref:
        The whitepoint reference, default is 2° D65.

    Returns:
      A grapefruit.Color instance.

    >>> Color.from_xyz(0.488941, 0.365682, 0.0448137)
    Color(1.0, 0.5, 0.0, 1.0)
    >>> Color.from_xyz(0.488941, 0.365682, 0.0448137, 0.5)
    Color(1.0, 0.5, 0.0, 0.5)

    """
    return Color(xyz_to_rgb(x, y, z), 'rgb', alpha, wref)

  @staticmethod
  def from_lab(l, a, b, alpha=1.0, wref=_DEFAULT_WREF):
    """Create a new instance based on the specifed CIE-LAB values.

    Parameters:
      :l:
        The L component [0...100]
      :a:
        The a component [-1...1]
      :b:
        The a component [-1...1]
      :alpha:
        The color transparency [0...1], default is opaque
      :wref:
        The whitepoint reference, default is 2° D65.

    Returns:
      A grapefruit.Color instance.

    >>> Color.from_lab(66.951823, 0.43084105, 0.73969231)
    Color(1.0, 0.5, -0.0, 1.0)
    >>> Color.from_lab(66.951823, 0.41165967, 0.67282012, wref=WHITE_REFERENCE['std_D50'])
    Color(1.0, 0.5, -0.0, 1.0)
    >>> Color.from_lab(66.951823, 0.43084105, 0.73969231, 0.5)
    Color(1.0, 0.5, -0.0, 0.5)
    >>> Color.from_lab(66.951823, 0.41165967, 0.67282012, 0.5, WHITE_REFERENCE['std_D50'])
    Color(1.0, 0.5, -0.0, 0.5)

    """
    return Color(xyz_to_rgb(*lab_to_xyz(l, a, b, wref)), 'rgb', alpha, wref)

  @staticmethod
  def from_cmy(c, m, y, alpha=1.0, wref=_DEFAULT_WREF):
    """Create a new instance based on the specifed CMY values.

    Parameters:
      :c:
        The Cyan component value [0...1]
      :m:
        The Magenta component value [0...1]
      :y:
        The Yellow component value [0...1]
      :alpha:
        The color transparency [0...1], default is opaque
      :wref:
        The whitepoint reference, default is 2° D65.

    Returns:
      A grapefruit.Color instance.

    >>> Color.from_cmy(0, 0.5, 1)
    Color(1.0, 0.5, 0.0, 1.0)
    >>> Color.from_cmy(0, 0.5, 1, 0.5)
    Color(1.0, 0.5, 0.0, 0.5)

    """
    return Color(cmy_to_rgb(c, m, y), 'rgb', alpha, wref)

  @staticmethod
  def from_cmyk(c, m, y, k, alpha=1.0, wref=_DEFAULT_WREF):
    """Create a new instance based on the specifed CMYK values.

    Parameters:
      :c:
        The Cyan component value [0...1]
      :m:
        The Magenta component value [0...1]
      :y:
        The Yellow component value [0...1]
      :k:
        The Black component value [0...1]
      :alpha:
        The color transparency [0...1], default is opaque
      :wref:
        The whitepoint reference, default is 2° D65.

    Returns:
      A grapefruit.Color instance.

    >>> Color.from_cmyk(1, 0.32, 0, 0.5)
    Color(0.0, 0.34, 0.5, 1.0)
    >>> Color.from_cmyk(1, 0.32, 0, 0.5, 0.5)
    Color(0.0, 0.34, 0.5, 0.5)

    """
    return Color(cmy_to_rgb(*cmyk_to_cmy(c, m, y, k)), 'rgb', alpha, wref)

  @staticmethod
  def from_html(html, alpha=1.0, wref=_DEFAULT_WREF):
    """Create a new instance based on the specifed HTML color definition.

    Parameters:
      :html:
        The HTML definition of the color (#RRGGBB or #RGB or a color name).
      :alpha:
        The color transparency [0...1], default is opaque.
      :wref:
        The whitepoint reference, default is 2° D65.

    Returns:
      A grapefruit.Color instance.

    >>> Color.from_html('#ff8000')
    Color(1.0, 0.501961, 0.0, 1.0)
    >>> Color.from_html('ff8000')
    Color(1.0, 0.501961, 0.0, 1.0)
    >>> Color.from_html('#f60')
    Color(1.0, 0.4, 0.0, 1.0)
    >>> Color.from_html('f60')
    Color(1.0, 0.4, 0.0, 1.0)
    >>> Color.from_html('lemonchiffon')
    Color(1.0, 0.980392, 0.803922, 1.0)
    >>> Color.from_html('#ff8000', 0.5)
    Color(1.0, 0.501961, 0.0, 0.5)

    """
    return Color(html_to_rgb(html), 'rgb', alpha, wref)

  @staticmethod
  def from_pil(pil, alpha=1.0, wref=_DEFAULT_WREF):
    """Create a new instance based on the specifed PIL color.

    Parameters:
      :pil:
        A PIL compatible color representation (0xBBGGRR)
      :alpha:
        The color transparency [0...1], default is opaque
      :wref:
        The whitepoint reference, default is 2° D65.

    Returns:
      A grapefruit.Color instance.

    >>> Color.from_pil(0x0080ff)
    Color(1.0, 0.501961, 0.0, 1.0)
    >>> Color.from_pil(0x0080ff, 0.5)
    Color(1.0, 0.501961, 0.0, 0.5)

    """
    return Color(pil_to_rgb(pil), 'rgb', alpha, wref)


  def __init__(self, values, mode='rgb', alpha=1.0, wref=_DEFAULT_WREF):
    """Instantiate a new grapefruit.Color object.

    Parameters:
      :values:
        The values of this color, in the specified representation.
      :mode:
        The representation mode used for values.
      :alpha:
        the alpha value (transparency) of this color.
      :wref:
        The whitepoint reference, default is 2° D65.

    """
    if not(isinstance(values, tuple)):
      raise TypeError("values must be a tuple")

    if mode=='rgb':
      self.__rgb = tuple([float(v) for v in values])
      self.__hsl = rgb_to_hsl(*self.__rgb)
    elif mode=='hsl':
      self.__hsl = tuple([float(v) for v in values])
      self.__rgb = hsl_to_rgb(*self.__hsl)
    else:
      raise ValueError("Invalid color mode: " + mode)

    self.__a = alpha
    self.__wref = wref

  # --=====================-----------------------------------------------------
  # -- Convenience methods --
  # --=====================--

  def __ne__(self, other):
    return not self.__eq__(other)

  def __eq__(self, other):
    try:
      if isinstance(other, Color):
        return (self.__rgb==other.__rgb) and (self.__a==other.__a) and (self.__wref==other.__wref)
      if len(other) != 4:
        return False
      return list(self.__rgb + (self.__a,)) == list(other)
    except TypeError:
      return False
    except AttributeError:
      return False

  def __repr__(self):
    return "Color({}, {}, {}, {})".format(*[round(v, 6) for v in (self.__rgb + (self.__a,))])

  def __str__(self):
    """A string representation of this grapefruit.Color instance.

    Returns:
      The RGBA representation of this grapefruit.Color instance.

    """
    return "({}, {}, {}, {})".format(*[round(v, 6) for v in (self.__rgb + (self.__a,))])

  if sys.version_info[0] < 3:
    def __unicode__(self):
      """A unicode string representation of this grapefruit.Color instance.

      Returns:
        The RGBA representation of this grapefruit.Color instance.

      """
      return unicode("({}, {}, {}, {})".format(*[round(v, 6) for v in (self.__rgb + (self.__a,))]))

  def __iter__(self):
    return iter(self.__rgb + (self.__a,))

  def __len__(self):
    return 4

  # --============--------------------------------------------------------------
  # -- Properties --
  # --============--

  @property
  def is_legal(self):
    """Boolean indicating whether the color is within the legal gamut."""
    return all(0.0 <= v <= 1.0 for v in self)

  @property
  def alpha(self):
    """The transparency of this color. 0.0 is transparent and 1.0 is fully opaque."""
    return self.__a
  @alpha.setter
  def alpha(self, value):
    self.__a = value

  @property
  def white_ref(self):
    """the white reference point of this color."""
    return self.__wref
  @white_ref.setter
  def white_ref(self, value):
    self.__wref = value


  @property
  def rgb(self):
    """The RGB values of this Color."""
    return self.__rgb
  @rgb.setter
  def rgb(self, value):
    self.__rgb = tuple([float(v) for v in value])
    self.__hsl = rgb_to_hsl(*self.__rgb)

  @property
  def rgba(self):
    """The RGBA values of this Color."""
    return (self.__rgb + (self.__a,))
  @rgba.setter
  def rgba(self, value):
    self.__rgb = tuple([float(v) for v in value[:3]])
    self.__a = float(value[3])
    self.__hsl = rgb_to_hsl(*self.__rgb)

  @property
  def red(self):
    return self.__rgb[0]
  @red.setter
  def red(self, value):
    self.__rgb = (float(value), self.__rgb[1], self.__rgb[2])
    self.__hsl = rgb_to_hsl(*self.__rgb)

  @property
  def green(self):
    return self.__rgb[1]
  @green.setter
  def green(self, value):
    self.__rgb = (self.__rgb[0], float(value), self.__rgb[2])
    self.__hsl = rgb_to_hsl(*self.__rgb)

  @property
  def blue(self):
    return self.__rgb[2]
  @blue.setter
  def blue(self, value):
    self.__rgb = (self.__rgb[0], self.__rgb[1], float(value))
    self.__hsl = rgb_to_hsl(*self.__rgb)


  @property
  def hsl(self):
    """The HSL values of this Color."""
    return self.__hsl
  @hsl.setter
  def hsl(self, value):
    self.__hsl = tuple([float(v) for v in value])
    self.__rgb = hsl_to_rgb(*self.__hsl)

  @property
  def hsl_hue(self):
    """The hue of this color."""
    return self.__hsl[0]
  @hsl_hue.setter
  def hsl_hue(self, value):
    self.__hsl = (float(value), self.__hsl[1], self.__hsl[2])
    self.__rgb = hsl_to_rgb(*self.__hsl)

  @property
  def hsv(self):
    """The HSV values of this Color."""
    return rgb_to_hsv(*self.__rgb)
  @hsv.setter
  def hsv(self, value):
    self.__rgb = hsv_to_rgb(*value)
    self.__hsl = rgb_to_hsl(*self.__rgb)

  @property
  def yiq(self):
    """The YIQ values of this Color."""
    return rgb_to_yiq(*self.__rgb)
  @yiq.setter
  def yiq(self, value):
    self.__rgb = yiq_to_rgb(*value)
    self.__hsl = rgb_to_hsl(*self.__rgb)

  @property
  def yuv(self):
    """The YUV values of this Color."""
    return rgb_to_yuv(*self.__rgb)
  @yuv.setter
  def yuv(self, value):
    self.__rgb = yuv_to_rgb(*value)
    self.__hsl = rgb_to_hsl(*self.__rgb)

  @property
  def xyz(self):
    """The CIE-XYZ values of this Color."""
    return rgb_to_xyz(*self.__rgb)
  @xyz.setter
  def xyz(self, value):
    self.__rgb = xyz_to_rgb(*value)
    self.__hsl = rgb_to_hsl(*self.__rgb)

  @property
  def lab(self):
    """The CIE-LAB values of this Color."""
    return xyz_to_lab(wref=self.__wref, *rgb_to_xyz(*self.__rgb))
  @lab.setter
  def lab(self, value):
    self.__rgb = xyz_to_rgb(lab_to_xyz(*value))
    self.__hsl = rgb_to_hsl(*self.__rgb)

  @property
  def cmy(self):
    """The CMY values of this Color."""
    return rgb_to_cmy(*self.__rgb)
  @cmy.setter
  def cmy(self, value):
    self.__rgb = cmy_to_rgb(*value)
    self.__hsl = rgb_to_hsl(*self.__rgb)

  @property
  def cmyk(self):
    """The CMYK values of this Color."""
    return cmy_to_cmyk(*rgb_to_cmy(*self.__rgb))
  @cmyk.setter
  def cmyk(self, value):
    self.__rgb = cmy_to_rgb(*cmyk_to_cmy(*value))
    self.__hsl = rgb_to_hsl(*self.__rgb)

  @property
  def ints(self):
    """This Color as a tuple of integers in the range [0...255]"""
    return rgb_to_ints(*self.__rgb)
  @ints.setter
  def ints(self, value):
    self.__rgb = ints_to_rgb(*value)
    self.__hsl = rgb_to_hsl(*self.__rgb)

  @property
  def html(self):
    """This Color as an HTML color definition."""
    return rgb_to_html(*self.__rgb)
  @html.setter
  def html(self, value):
    self.__rgb = html_to_rgb(value)
    self.__hsl = rgb_to_hsl(*self.__rgb)

  @property
  def pil(self):
    """This Color as a PIL compatible value."""
    return rgb_to_pil(*self.__rgb)
  @pil.setter
  def pil(self, value):
    self.__rgb = pil_to_rgb(value)
    self.__hsl = rgb_to_hsl(*self.__rgb)

  @property
  def websafe(self):
    """The web safe color nearest to this one (RGB)."""
    return rgb_to_websafe(*self.__rgb)

  @property
  def greyscale(self):
    """The greyscale equivalent to this color (RGB)."""
    return rgb_to_greyscale(*self.rgb)

  def with_alpha(self, alpha):
    """Create a new instance based on this one with a new alpha value.

    Parameters:
      :alpha:
        The transparency of the new color [0...1].

    Returns:
      A grapefruit.Color instance.

    >>> Color.from_rgb(1.0, 0.5, 0.0, 1.0).with_alpha(0.5)
    Color(1.0, 0.5, 0.0, 0.5)

    """
    return Color(self.__rgb, 'rgb', alpha, self.__wref)

  def with_white_ref(self, wref, labAsRef=False):
    """Create a new instance based on this one with a new white reference.

    Parameters:
      :wref:
        The whitepoint reference.
      :labAsRef:
        If True, the L*a*b* values of the current instance are used as reference
        for the new color; otherwise, the RGB values are used as reference.

    Returns:
      A grapefruit.Color instance.


    >>> c = Color.from_rgb(1.0, 0.5, 0.0, 1.0, WHITE_REFERENCE['std_D65'])

    >>> c2 = c.with_white_ref(WHITE_REFERENCE['sup_D50'])
    >>> c2.rgb
    (1.0, 0.5, 0.0)
    >>> '(%g, %g, %g)' % c2.white_ref
    '(0.967206, 1, 0.81428)'

    >>> c2 = c.with_white_ref(WHITE_REFERENCE['sup_D50'], labAsRef=True)
    >>> '(%g, %g, %g)' % c2.rgb
    '(1.01463, 0.490341, -0.148133)'
    >>> '(%g, %g, %g)' % c2.white_ref
    '(0.967206, 1, 0.81428)'
    >>> '(%g, %g, %g)' % c.lab
    '(66.9518, 0.430841, 0.739692)'
    >>> '(%g, %g, %g)' % c2.lab
    '(66.9518, 0.430841, 0.739693)'

    """
    if labAsRef:
      l, a, b = self.lab
      return Color.from_lab(l, a, b, self.__a, wref)
    else:
      return Color(self.__rgb, 'rgb', self.__a, wref)

  def with_hue(self, hue):
    """Create a new instance based on this one with a new hue.

    Parameters:
      :hue:
        The hue of the new color [0...360].

    Returns:
      A grapefruit.Color instance.

    >>> Color.from_hsl(30, 1, 0.5).with_hue(60)
    Color(1.0, 1.0, 0.0, 1.0)
    >>> Color.from_hsl(30, 1, 0.5).with_hue(60).hsl
    (60.0, 1.0, 0.5)

    """
    h, s, l = self.__hsl
    return Color((hue, s, l), 'hsl', self.__a, self.__wref)

  def with_saturation(self, saturation):
    """Create a new instance based on this one with a new saturation value.

    .. note::

       The saturation is defined for the HSL mode.

    Parameters:
      :saturation:
        The saturation of the new color [0...1].

    Returns:
      A grapefruit.Color instance.

    >>> Color.from_hsl(30, 1, 0.5).with_saturation(0.5)
    Color(0.75, 0.5, 0.25, 1.0)
    >>> Color.from_hsl(30, 1, 0.5).with_saturation(0.5).hsl
    (30.0, 0.5, 0.5)

    """
    h, s, l = self.__hsl
    return Color((h, saturation, l), 'hsl', self.__a, self.__wref)

  def with_lightness(self, lightness):
    """Create a new instance based on this one with a new lightness value.

    Parameters:
      :lightness:
        The lightness of the new color [0...1].

    Returns:
      A grapefruit.Color instance.

    >>> Color.from_hsl(30, 1, 0.5).with_lightness(0.25)
    Color(0.5, 0.25, 0.0, 1.0)
    >>> Color.from_hsl(30, 1, 0.5).with_lightness(0.25).hsl
    (30.0, 1.0, 0.25)

    """
    h, s, l = self.__hsl
    return Color((h, s, lightness), 'hsl', self.__a, self.__wref)

  def darker(self, level):
    """Create a new instance based on this one but darker.

    Parameters:
      :level:
        The amount by which the color should be darkened to produce
        the new one [0...1].

    Returns:
      A grapefruit.Color instance.

    >>> Color.from_hsl(30, 1, 0.5).darker(0.25)
    Color(0.5, 0.25, 0.0, 1.0)
    >>> Color.from_hsl(30, 1, 0.5).darker(0.25).hsl
    (30.0, 1.0, 0.25)

    """
    h, s, l = self.__hsl
    return Color((h, s, max(l - level, 0)), 'hsl', self.__a, self.__wref)

  def lighter(self, level):
    """Create a new instance based on this one but lighter.

    Parameters:
      :level:
        The amount by which the color should be lightened to produce
        the new one [0...1].

    Returns:
      A grapefruit.Color instance.

    >>> Color.from_hsl(30, 1, 0.5).lighter(0.25)
    Color(1.0, 0.75, 0.5, 1.0)
    >>> Color.from_hsl(30, 1, 0.5).lighter(0.25).hsl
    (30.0, 1.0, 0.75)

    """
    h, s, l = self.__hsl
    return Color((h, s, min(l + level, 1)), 'hsl', self.__a, self.__wref)

  def saturate(self, level):
    """Create a new instance based on this one but more saturated.

    Parameters:
      :level:
        The amount by which the color should be saturated to produce
        the new one [0...1].

    Returns:
      A grapefruit.Color instance.

    >>> Color.from_hsl(30, 0.5, 0.5).saturate(0.25)
    Color(0.875, 0.5, 0.125, 1.0)
    >>> Color.from_hsl(30, 0.5, 0.5).saturate(0.25).hsl
    (30.0, 0.75, 0.5)

    """
    h, s, l = self.__hsl
    return Color((h, min(s + level, 1), l), 'hsl', self.__a, self.__wref)

  def desaturate(self, level):
    """Create a new instance based on this one but less saturated.

    Parameters:
      :level:
        The amount by which the color should be desaturated to produce
        the new one [0...1].

    Returns:
      A grapefruit.Color instance.

    >>> Color.from_hsl(30, 0.5, 0.5).desaturate(0.25)
    Color(0.625, 0.5, 0.375, 1.0)
    >>> Color.from_hsl(30, 0.5, 0.5).desaturate(0.25).hsl
    (30.0, 0.25, 0.5)

    """
    h, s, l = self.__hsl
    return Color((h, max(s - level, 0), l), 'hsl', self.__a, self.__wref)

  def nearest_legal(self):
    """Create a new instance that is the nearest legal color to this one.

    >>> Color.from_rgb(2.0, 0.0, 3.0).nearest_legal()
    Color(1.0, 0.0, 1.0, 1.0)
    """
    return Color.from_rgb(*[max(min(v, 1.0), 0.0) for v in self])

  def websafe_dither(self):
    """Return the two websafe colors nearest to this one.

    Returns:
      A tuple of two grapefruit.Color instances which are the two
      web safe colors closest this one.

    >>> c = Color.from_rgb(1.0, 0.45, 0.0)
    >>> c1, c2 = c.websafe_dither()
    >>> c1
    Color(1.0, 0.4, 0.0, 1.0)
    >>> c2
    Color(1.0, 0.6, 0.0, 1.0)

    """
    return (
      Color(rgb_to_websafe(*self.__rgb), 'rgb', self.__a, self.__wref),
      Color(rgb_to_websafe(alt=True, *self.__rgb), 'rgb', self.__a, self.__wref))

  def complementary_color(self, mode='ryb'):
    """Create a new instance which is the complementary color of this one.

    Parameters:
      :mode:
        Select which color wheel to use for the generation (ryb/rgb).


    Returns:
      A grapefruit.Color instance.

    >>> Color.from_hsl(30, 1, 0.5).complementary_color(mode='rgb')
    Color(0.0, 0.5, 1.0, 1.0)
    >>> Color.from_hsl(30, 1, 0.5).complementary_color(mode='rgb').hsl
    (210.0, 1.0, 0.5)

    """
    h, s, l = self.__hsl

    if mode == 'ryb': h = rgb_to_ryb(h)
    h = (h+180)%360
    if mode == 'ryb': h = ryb_to_rgb(h)

    return Color((h, s, l), 'hsl', self.__a, self.__wref)

  def make_gradient(self, target, steps=100):
    """Create a list with the gradient colors between this and the other color.

    Parameters:
      :target:
        The grapefruit.Color at the other end of the gradient.
      :steps:
        The number of gradients steps to create.


    Returns:
      A list of grapefruit.Color instances.

    >>> c1 = Color.from_rgb(1.0, 0.0, 0.0, alpha=1)
    >>> c2 = Color.from_rgb(0.0, 1.0, 0.0, alpha=0)
    >>> c1.make_gradient(c2, 3)
    [Color(0.75, 0.25, 0.0, 0.75), Color(0.5, 0.5, 0.0, 0.5), Color(0.25, 0.75, 0.0, 0.25)]

    """
    gradient = []
    rgba1 = self.__rgb + (self.__a,)
    rgba2 = target.__rgb + (target.__a,)

    steps += 1
    for n in range(1, steps):
      d = 1.0*n/steps
      r = (rgba1[0]*(1-d)) + (rgba2[0]*d)
      g = (rgba1[1]*(1-d)) + (rgba2[1]*d)
      b = (rgba1[2]*(1-d)) + (rgba2[2]*d)
      a = (rgba1[3]*(1-d)) + (rgba2[3]*d)

      gradient.append(Color((r, g, b), 'rgb', a, self.__wref))

    return gradient

  def make_monochrome_scheme(self):
    """Return 4 colors in the same hue with varying saturation/lightness.

    Returns:
      A tuple of 4 grapefruit.Color in the same hue as this one,
      with varying saturation/lightness.

    >>> c = Color.from_hsl(30, 0.5, 0.5)
    >>> ['(%g, %g, %g)' % clr.hsl for clr in c.make_monochrome_scheme()]
    ['(30, 0.2, 0.8)', '(30, 0.5, 0.3)', '(30, 0.2, 0.6)', '(30, 0.5, 0.8)']

    """
    def _wrap(x, min, thres, plus):
      if (x-min) < thres: return x + plus
      else: return x-min

    h, s, l = self.__hsl

    s1 = _wrap(s, 0.3, 0.1, 0.3)
    l1 = _wrap(l, 0.5, 0.2, 0.3)

    s2 = s
    l2 = _wrap(l, 0.2, 0.2, 0.6)

    s3 = s1
    l3 = max(0.2, l + (1-l)*0.2)

    s4 = s
    l4 = _wrap(l, 0.5, 0.2, 0.3)

    return (
      Color((h, s1,  l1), 'hsl', self.__a, self.__wref),
      Color((h, s2,  l2), 'hsl', self.__a, self.__wref),
      Color((h, s3,  l3), 'hsl', self.__a, self.__wref),
      Color((h, s4,  l4), 'hsl', self.__a, self.__wref))

  def make_triadic_scheme(self, angle=120, mode='ryb'):
    """Return two colors forming a triad or a split complementary with this one.

    Parameters:
      :angle:
        The angle between the hues of the created colors.
        The default value makes a triad.
      :mode:
        Select which color wheel to use for the generation (ryb/rgb).

    Returns:
      A tuple of two grapefruit.Color forming a color triad with
      this one or a split complementary.

    >>> c1 = Color.from_hsl(30, 1, 0.5)

    >>> c2, c3 = c1.make_triadic_scheme(mode='rgb')
    >>> c2.hsl
    (150.0, 1.0, 0.5)
    >>> c3.hsl
    (270.0, 1.0, 0.5)

    >>> c2, c3 = c1.make_triadic_scheme(angle=40, mode='rgb')
    >>> c2.hsl
    (190.0, 1.0, 0.5)
    >>> c3.hsl
    (230.0, 1.0, 0.5)

    """
    h, s, l = self.__hsl
    angle = min(angle, 120) / 2.0

    if mode == 'ryb': h = rgb_to_ryb(h)
    h += 180
    h1 = (h - angle) % 360
    h2 = (h + angle) % 360
    if mode == 'ryb':
      h1 = ryb_to_rgb(h1)
      h2 = ryb_to_rgb(h2)

    return (
      Color((h1, s,  l), 'hsl', self.__a, self.__wref),
      Color((h2, s,  l), 'hsl', self.__a, self.__wref))

  def make_tetradic_scheme(self, angle=30, mode='ryb'):
    """Return three colors froming a tetrad with this one.

    Parameters:
      :angle:
        The angle to substract from the adjacent colors hues [-90...90].
        You can use an angle of zero to generate a square tetrad.
      :mode:
        Select which color wheel to use for the generation (ryb/rgb).

    Returns:
      A tuple of three grapefruit.Color forming a color tetrad with
      this one.

    >>> col = Color.from_hsl(30, 1, 0.5)
    >>> [c.hsl for c in col.make_tetradic_scheme(mode='rgb', angle=30)]
    [(90.0, 1.0, 0.5), (210.0, 1.0, 0.5), (270.0, 1.0, 0.5)]

    """
    h, s, l = self.__hsl

    if mode == 'ryb': h = rgb_to_ryb(h)
    h1 = (h + 90 - angle) % 360
    h2 = (h + 180) % 360
    h3 = (h + 270 - angle) % 360
    if mode == 'ryb':
      h1 = ryb_to_rgb(h1)
      h2 = ryb_to_rgb(h2)
      h3 = ryb_to_rgb(h3)

    return (
      Color((h1, s,  l), 'hsl', self.__a, self.__wref),
      Color((h2, s,  l), 'hsl', self.__a, self.__wref),
      Color((h3, s,  l), 'hsl', self.__a, self.__wref))

  def make_analogous_scheme(self, angle=30, mode='ryb'):
    """Return two colors analogous to this one.

    Args:
      :angle:
        The angle between the hues of the created colors and this one.
      :mode:
        Select which color wheel to use for the generation (ryb/rgb).

    Returns:
      A tuple of grapefruit.Colors analogous to this one.

    >>> c1 = Color.from_hsl(30, 1, 0.5)

    >>> c2, c3 = c1.make_analogous_scheme(angle=60, mode='rgb')
    >>> c2.hsl
    (330.0, 1.0, 0.5)
    >>> c3.hsl
    (90.0, 1.0, 0.5)

    >>> c2, c3 = c1.make_analogous_scheme(angle=10, mode='rgb')
    >>> c2.hsl
    (20.0, 1.0, 0.5)
    >>> c3.hsl
    (40.0, 1.0, 0.5)

    """
    h, s, l = self.__hsl

    if mode == 'ryb': h = rgb_to_ryb(h)
    h += 360
    h1 = (h - angle) % 360
    h2 = (h + angle) % 360
    if mode == 'ryb':
      h1 = ryb_to_rgb(h1)
      h2 = ryb_to_rgb(h2)

    return (Color((h1, s,  l), 'hsl', self.__a, self.__wref),
        Color((h2, s,  l), 'hsl', self.__a, self.__wref))

  def alpha_blend(self, other):
    """Alpha-blend this color on the other one.

    Args:
      :other:
        The grapefruit.Color to alpha-blend with this one.

    Returns:
      A grapefruit.Color instance which is the result of alpha-blending
      this color on the other one.

    >>> c1 = Color.from_rgb(1, 0.5, 0, 0.2)
    >>> c2 = Color.from_rgb(1, 1, 1, 0.8)
    >>> c3 = c1.alpha_blend(c2)
    >>> c3
    Color(1.0, 0.875, 0.75, 0.84)

    """
    # get final alpha channel
    fa = self.__a + other.__a - (self.__a * other.__a)

    # get percentage of source alpha compared to final alpha
    if fa==0: sa = 0
    else: sa = min(1.0, self.__a/other.__a)

    # destination percentage is just the additive inverse
    da = 1.0 - sa

    sr, sg, sb = [v * sa for v in self.__rgb]
    dr, dg, db = [v * da for v in other.__rgb]

    return Color((sr+dr, sg+dg, sb+db), 'rgb', fa, self.__wref)

  def blend(self, other, percent=0.5):
    """blend this color with the other one.

    Args:
      :other:
        the grapefruit.Color to blend with this one.

    Returns:
      A grapefruit.Color instance which is the result of blending
      this color on the other one.

    >>> c1 = Color.from_rgb(1, 0.5, 0, 0.2)
    >>> c2 = Color.from_rgb(1, 1, 1, 0.6)
    >>> c3 = c1.blend(c2)
    >>> c3
    Color(1.0, 0.75, 0.5, 0.4)

    """
    dest = 1.0 - percent
    rgb = tuple(((u * percent) + (v * dest) for u, v in zip(self.__rgb, other.__rgb)))
    a = (self.__a * percent) + (other.__a * dest)
    return Color(rgb, 'rgb', a, self.__wref)

def _test():
  import doctest
  reload(doctest)
  doctest.testmod()

if __name__=='__main__':
  _test()

# vim: ts=2 sts=2 sw=2 et
