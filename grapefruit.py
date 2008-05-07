# 
# GrapeFruit - Color manipulation in Python
# 
# Copyright (c) 2008, Xavier Basty
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
# 
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
# 
#     * Neither the name of the GrapeFruit nor the names of its contributors
#       may be used to endorse or promote products derived from this software
#       without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDER "AS IS" AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

def rgbToHSL(r, g, b):
    """
    Convert the color from RGB coordinates to HSL.
    
    @param r        the Red component [0~1]
    @param g        the Green component [0~1]
    @param b        the Blue component [0~1]
    
    @return         (h, s, l) -> ([0~360], [0~1], [0~1])
    """
    minVal = min(r, g, b)    	# min RGB value
    maxVal = max(r, g, b)    	# max RGB value

    l = (maxVal + minVal) / 2.0
    if (minVal == maxVal):
    	return (0.0, 0.0, l)	# achromatic (gray)

    d = maxVal - minVal      	# delta RGB value

    if (l < 0.5): s = d / (maxVal + minVal)
    else: s = d / (2.0 - maxVal - minVal)

    dr, dg, db = [(maxVal - val) / d for val in (r, g, b)]

    if (r == maxVal): h = db - dg
    elif (g == maxVal): h = 2.0 + dr - db
    else: h = 4.0 + dg - dr
    
    h = (h*60.0) % 360.0
    return (h, s, l)

def _hueToRGB(n1, n2, h):
    h = h % 60.0
    if (h < 1.0): return n1 + ((n2-n1) * h)
    if (h < 3.0): return n2
    if (h < 4.0): return n1 + ((n2-n1) * (4.0 - h))
    return n1

def hslToRGB(h, s, l):
    """
    Convert the color from HSL coordinates to RGB.
    
    @param h        the Hus component [0~1]
    @param s        the Saturation component [0~1]
    @param l        the Lightness component [0~1]
    
    @return         (r, g, b) -> ([0~1], [0~1], [0~1])
    """
    if (s == 0): return (l, l, l)	# achromatic (gray)

    if (l < 0.5): n2 = l * (1.0 + s)
    else: n2 = l+s - (l*s)

    n1 = (2.0 * l) - n2

    h /= 60.0
    r = _hueToRGB(n1, n2, h + 2)
    g = _hueToRGB(n1, n2, h)
    b = _hueToRGB(n1, n2, h - 2)

    return (r, g, b)

def rgbToHSV(r, g, b):
    """
    Convert the color from RGB coordinates to HSV.
    
    @param r        the Red component [0~1]
    @param g        the Green component [0~1]
    @param b        the Blue component [0~1]
    
    @return         (h, s, v) -> ([0~360], [0~1], [0~1])
                    if s == 0, then h is set to 0
    """
    v = max(r, g, b)
    d = v - min(r, g, b)    
    if (d == 0): return (0.0, 0.0, v)
    s = d / v

    dr, dg, db = [(v - val) / d for val in (r, g, b)]

    if (r == v):
        h = db - dg             # between yellow & magenta
    elif (g == v):
        h = 2.0 + dr - db		# between cyan & yellow
    else: # b == v
        h = 4.0 + dg - dr		# between magenta & cyan
    
    h = (h*60.0) % 360.0
    return (h, s, v)

def hsvToRGB(h, s, v):
    """
    Convert the color from RGB coordinates to HSV.
    
    @param h        the Hus component [0~1]
    @param s        the Saturation component [0~1]
    @param v        the Value component [0~1]
    
    @return         (r, g, b) -> ([0~1], [0~1], [0~1])
    """
    if (s == 0): return (v, v, v)	# achromatic (gray)
    
    h /= 60.0
    h = h % 6.0

    i = int(h)
    f = h - i
    if (not (i&1)): f = 1-f     # if i is even
    
    m = v * (1.0 - s)
    n = v * (1.0 - (s * f))
    
    if (i == 0): return (v, n, m)
    elif (i == 1): return (n, v, m)
    elif (i == 2): return (m, v, n)
    elif (i == 3): return (m, n, v)
    elif (i == 4): return (n, m, v)
    else: return (v, m, n)

def rgbToYIQ(r, g, b):
    """
    Convert the color from RGB to YIQ.
    
    @param r        the Red component [0~1]
    @param g        the Green component [0~1]
    @param b        the Blue component [0~1]
    
    @return         (y, i, q) -> ([0~1], [0~1], [0~1])
    """
    y = (r * 0.2989) + (g * 0.5866) + (b *0.1114)
    i = (r * 0.5959) - (g * 0.2741) - (b *0.3218)
    q = (r * 0.2113) - (g * 0.5227) + (b *0.3113)
    return (y, i, q)

def yiqToRGB(y, i, q):
    """
    Convert the color from YIQ coordinates to RGB.
    
    @param y        the Y component [0~1]
    @param i        the I component [0~1]
    @param q        the Q component [0~1]
    
    @return         (r, g, b) -> ([0~1], [0~1], [0~1])
    """
    r = y + (i * 0.9562) + (q * 0.6210)
    g = y - (i * 0.2717) - (q * 0.6485)
    b = y - (i * 1.1053) + (q * 1.7020)
    return (r, g, b)

def rgbToYUV(r, g, b):
    """
    Convert the color from RGB coordinates to YUV.
    
    @param r        the Red component [0~1]
    @param g        the Green component [0~1]
    @param b        the Blue component [0~1]
    
    @return         (y, u, v) -> ([0~1], [-0.436~0.436], [-0.615~0.615])
    """
    y =  (r * 0.29900) + (g * 0.58700) + (b * 0.11400)
    u = -(r * 0.14713) - (g * 0.28886) + (b * 0.43600)
    v =  (r * 0.61500) - (g * 0.51499) - (b * 0.10001)
    return (y, u, v)

def yuvToRGB(y, u, v):
    """
    Convert the color from YUV coordinates to RGB.
    
    @param y        the Y component [0~1]
    @param u        the U component [-0.436~0.436]
    @param v        the V component [-0.615~0.615]
    
    @return         (r, g, b) -> ([0~1], [0~1], [0~1])
    """
    """Convert the color from YUV to RGB.
    
    (y, u, v) -> ([0~1], [0~1], [0~1])
    (r, g, b) -> ([0~1], [0~1], [0~1])
    """
    r = y + (v * 1.13983)
    g = y - (u * 0.39465) - (v * 0.58060)
    b = y + (u * 2.03211)
    return (r, g, b)

def rgbToXYZ(r, g, b):
    """
    Convert the color from RGB coordinates to CIE 1931 XYZ.
    
    @param r        the Red component [0~1]
    @param g        the Green component [0~1]
    @param b        the Blue component [0~1]
    
    @return         (x, y, z) -> ([0~1], [0~1], [0~1])
    """
    r, g, b = [((v > 0.04045) and [((v + 0.055) / 1.055) ** 2.4] or [v / 12.92])[0] for v in (r, g, b)]
        
    x = ((r * 41.2453) + (g * 35.7580) + (b * 18.0423)) / 100
    y = ((r * 21.2671) + (g * 71.5160) + (b * 07.2169)) / 100
    z = ((r *  1.9334) + (g * 11.9193) + (b * 95.0227)) / 100
    return (x, y, z)

def xyzToRGB(x, y, z):
    """
    Convert the color from CIE 1931 XYZ coordinates to RGB.
    
    @param x        the X component [0~1]
    @param y        the Y component [0~1]
    @param z        the Z component [0~1]
    
    @return         (r, g, b) -> ([0~1], [0~1], [0~1])
    """
    r =  (x * 3.240479) - (y * 1.537150) - (z * 0.498535)
    g = -(x * 0.969256) + (y * 1.875992) + (z * 0.041556)
    b =  (x * 0.055648) - (y * 0.204043) + (z * 1.057311)
    
    r, g, b = [((v > 0.0031308) and [(1.055 * (v ** (1/2.4))) - 0.055] or [v * 12.92])[0] for v in (r, g, b)]
    return (r, g, b)

def xyzToLAB(x, y, z, wref=(0.95047, 1.00000, 1.08883)):
    """
    Convert the color from CIE XYZ to CIE L*a*b*.
    
    @param x        the X component [0~1]
    @param y        the Y component [0~1]
    @param z        the Z component [0~1]
    @param wref     the whitepoint reference, default is 2 degrees, D65 (daylight)
    
    @return         (L, a, b) -> ([0~100], [-1~1], [-1~1])
    """
    x /= wref[0]
    y /= wref[1]
    z /= wref[2]
    
    x, y, z = [((v > 0.008856) and [v ** (1.0/3)] or [(7.787 * v) + (16.0/116)])[0] for v in (x, y, z)]
    
    l = (1.16 * y) - 0.16
    a = 5.0 * (x - y)
    b = 2.0 * (y - z)
    
    return (l, a, b)

def labToXYZ(l, a, b, wref=(0.95047, 1.00000, 1.08883)):
    """
    Convert the color from CIE L*a*b* to CIE 1931 XYZ.
    
    @param l        the L component [0~100]
    @param a        the a component [-1~1]
    @param b        the a component [-1~1]
    @param wref     the whitepoint reference, default is 2 degrees, D65 (daylight)
    
    @return         (x, y, z) -> ([0~1], [0~1], [0~1])
    """
    y = (l + 0.16) / 1.16
    x = (a / 5.0) + y
    z = y - (b / 2.0)
    
    x, y, z = [((v > 0.008856) and [v ** 3] or [(v - (16.0 / 116)) / 7.787])[0] for v in (x, y, z)]
    
    x *= wref[0]
    y *= wref[1]
    z *= wref[2]
    
    return (x, y, z)

def cmykToCMY(c, m, y, k):
    """
    Convert the color from CMYK coordinates to CMY.
    
    @param c        the Cyan component [0~1]
    @param m        the Magenta component [0~1]
    @param y        the Yellow component [0~1]
    @param k        the Black component [0~1]
    
    @return         (c, m, y) -> ([0~1], [0~1], [0~1])
    """
    return tuple([(v * (1-k) + k) for v in (c, m, y)])

def cmyToCMYK(c, m, y):
    """
    Convert the color from CMY coordinates to CMYK.
    
    @param c        the Cyan component [0~1]
    @param m        the Magenta component [0~1]
    @param y        the Yellow component [0~1]
    
    @return         (c, m, y, k) -> ([0~1], [0~1], [0~1], [0~1])
    """
    b = min(c, m, y)
    if (b == 1.0):
        return (0.0, 0.0, 0.0, 1.0)
    else:
        c, m, y = [((v-b) / (1-b)) for v in (c, m, y)]
        return (c, m, y, b)

def rgbToCMY(r, g, b):
    """
    Convert the color from RGB coordinates to CMY.
    
    @param r        the Red component [0~1]
    @param g        the Green component [0~1]
    @param b        the Blue component [0~1]
    
    @return         (c, m, y) -> ([0~1], [0~1], [0~1])
    """
    return (1-r, 1-g, 1-b)

def cmyToRGB(c, m, y):
    """
    Convert the color from CMY coordinates to RGB.
    
    @param c        the Cyan component [0~1]
    @param m        the Magenta component [0~1]
    @param y        the Yellow component [0~1]
    
    @return         (r, g, b) -> ([0~1], [0~1], [0~1])
    """
    return (1-c, 1-m, 1-y)

def rgbToHTML(r, g, b):
    """
    Convert the color from (r, g, b) to #RRGGBB.
    
    @param r        the Red component [0~1]
    @param g        the Green component [0~1]
    @param b        the Blue component [0~1]
    
    @return         #RRGGBB -> #000000~#FFFFFF
    """
    r, g, b = [min(round(v*255), 255) for v in (r, g, b)]
    return '#%02x%02x%02x' % (r, g, b)

def htmlToRGB(html):
    """
    Convert the HTML color to (r, g, b).
    
    @param html		#RRGGBB or #RGB or a color name
    
    @return         (r, g, b) -> ([0~1], [0~1], [0~1])
    """
    html = html.strip()
    if html[0] == '#':
        html = html[1:]
    elif namedColors.has_key(html.lower()):
            html = namedColors[html.lower()][1:]

    if len(html) == 6:
        r, g, b = html[:2], html[2:4], html[4:]
    elif len(html) == 3:
        r, g, b = html[:1], html[1:2], html[2:3]
        r, g, b = [v+v for v in (r, g, b)]
    else:
        raise ValueError, "input #%s is not in #RRGGBB format" % html
    r, g, b = [(int(n, 16) / 255.0) for n in (r, g, b)]
    return (r, g, b)

def rgbToPIL(r, g, b):
    """
    Convert the color from RGB to a PIL-compatible integer.
    
    @param r        the Red component [0~1]
    @param g        the Green component [0~1]
    @param b        the Blue component [0~1]
    
    @return         PIL -> 0xBBGGRR
    """
    r, g, b = [min(int(round(v*255)), 255) for v in (r, g, b)]
    return (b << 16) + (g << 8) + r

def pilToRGB(pil):
    """
    Convert the color from a PIL-compatible integer to RGB.
    
    @param pil      0xBBGGRR
    
    @return         (r, g, b) -> ([0~1], [0~1], [0~1])
    """
    r = 0xff & pil
    g = 0xff & (pil >> 8)
    b = 0xff & (pil >> 16)

    r, g, b = [v / 255.0 for v in (r, g, b)]

    return (r, g, b)

def _webSafeComponent(c, alt=False):
    """
    Convert a color component to its web safe equivalent
    
    @param c        the component value [0~1]
    @param alt      if true, return the alternative value instead of the nearest
                    one.
    
    @return         the web safe equivalent of the component value.
    """
    safe = (0.0, 0.2, 0.4, 0.6, 0.8, 1.0)
    safePairs = ((0.0, 0.2),
                 (0.2, 0.4),
                 (0.4, 0.6),
                 (0.6, 0.8),
                 (0.8, 1.0))

    if (c in safe):
        return c

    for pair in safePairs:
        if ((pair[0] < c) and (pair[1] > c)):
            if (alt):
                if ((c - pair[0]) > (pair[1] - c)): return pair[0]
                else:return pair[1]
            else:
                if ((c - pair[0]) > (pair[1] - c)): return pair[1]
                else:return pair[0]
    
    return 1.0

def rgbToWebSafe(r, g, b, alt=False):
    """
    Convert the color from RGB to 'web safe' RGB
    
    @param r        the Red component [0~1]
    @param g        the Green component [0~1]
    @param b        the Blue component [0~1]
    @param alt      if true, use the alternative color instead of the nearest
                    one. Can be used for dithering.
    
    @return         (r, g, b) -> ([0~1], [0~1], [0~1])
    """
    r, g, b = [_webSafeComponent(v, alt) for v in (r, g, b)]
    return (r, g, b)

def rgbToGreyscale(r, g, b):
	"""
	Convert the color from RGB to its greyscale equivalent

    @param r        the Red component [0~1]
    @param g        the Green component [0~1]
    @param b        the Blue component [0~1]
    
    @return         (r, g, b) -> ([0~1], [0~1], [0~1])
	"""
	v = (r + g + b) / 3.0
	return (v, v, v)

def fromRGB(rgb, alpha = 1.0):
    """
    Create a Color from the specifed RGB values.
    
    @param rgb      (r, g, b) -> ([0~1], [0~1], [0~1])
    @param a        the color transparency [0~1], default is opaque
    
    @return         A new Color instance
    """
    return Color(rgb, "rgb", alpha)

def fromHSL(hsl, alpha = 1.0):
    """
    Create a Color from the specifed HSL values.
    
    @param hsl      (h, s, l) -> ([0~360], [0~1], [0~1])
    @param a        the color transparency [0~1], default is opaque
    
    @return         A new Color instance
    """
    return Color(hsl, "hsl", alpha)

def fromHSV(hsv, alpha = 1.0):
    """
    Create a Color from the specifed HSV values.
    
    @param hsv      (h, s, v) -> ([0~360], [0~1], [0~1])
    @param a        the color transparency [0~1], default is opaque
    
    @return         A new Color instance
    """
    h, s, l = rgbToHSL(*hsvToRGB(*hsv))
    return Color((hsv[0], s, l), "hsl", alpha)

def fromYIQ(yiq, alpha = 1.0):
    """
    Create a Color from the specifed YIQ values.
    
    @param yiq      (y, i, q) -> ([0~1], [0~1], [0~1])
    @param a        the color transparency [0~1], default is opaque
    
    @return         A new Color instance
    """
    return Color(yiqToRGB(*yiq), "rgb", alpha)

def fromYUV(yuv, alpha = 1.0):
    """
    Create a Color from the specifed YUV values.
    
    @param yuv      (y, u, v) -> ([0~1], [0~1], [0~1])
    @param a        the color transparency [0~1], default is opaque
    
    @return         A new Color instance
    """
    return Color(yuvToRGB(*yuv), "rgb", alpha)

def fromXYZ(xyz, alpha = 1.0):
    """
    Create a Color from the specifed CIE-XYZ values.
    
    @param xyz      (x, y, z) -> ([0~1], [0~1], [0~1])
    @param a        the color transparency [0~1], default is opaque
    
    @return         A new Color instance
    """
    return Color(xyzToRGB(*xyz), "rgb", alpha)

def fromLAB(lab, alpha = 1.0, wref=(0.95047, 1.00000, 1.08883)):
    """
    Create a Color from the specifed CIE-LAB values.
    
    @param lab      (l, a, b) -> ([0~1], [0~1], [0~1])
    @param a        the color transparency [0~1], default is opaque
    @param wref     the whitepoint reference, default is 2 degrees, D65 (daylight)
    
    @return         A new Color instance
    """
    return Color(xyzToRGB(*labToXYZ(wref=wref, *lab)), "rgb", alpha)

def fromCMY(cmy, alpha = 1.0):
    """
    Create a Color from the specifed CMY values.
    
    @param cmy      (c, m, y) -> ([0~1], [0~1], [0~1])
    @param a        the color transparency [0~1], default is opaque
    
    @return         A new Color instance
    """
    return Color(cmyToRGB(*cmy), "rgb", alpha)

def fromCMYK(cmyk, alpha = 1.0):
    """
    Create a Color from the specifed CMYK values.
    
    @param cmy      (c, m, y, k) -> ([0~1], [0~1], [0~1])
    @param a        the color transparency [0~1], default is opaque
    
    @return         A new Color instance
    """
    return Color(cmyToRGB(*cmykToCMY(*cmyk)), "rgb", alpha)

def fromHTML(html, alpha = 1.0):
    """
    Create a Color from the specifed HTML color definition.
    
    @param html     #RRGGBB or #RGB or the color name
    @param a        the color transparency [0~1], default is opaque
    
    @return         A new Color instance
    """
    return Color(htmlToRGB(html), "rgb", alpha)

def fromPIL(pil, alpha = 1.0):
    """
    Create a Color from the specifed PIL color.
    
    @param pil      0xBBGGRR
    @param a        the color transparency [0~1], default is opaque
    
    @return         A new Color instance
    """
    return Color(pilToRGB(pil), "rgb", alpha)

# o2: Observer 2 degrees (CIE 1931)
# o10: Observer 10 degrees (CIE 1964)
whiteReferences = {
    "o2a"    	: (1.09850, 1.00000, 0.35585), # Tungsten illumination with color temperature of 3800 K
    "o2c"    	: (0.98074, 1.00000, 1.18232), # Fluorescent illumination with correlated color temperature about 5200 K(),
    "o2d50"  	: (0.96422, 1.00000, 0.85521), # 
    "o2d55"  	: (0.95682, 1.00000, 0.92149), # Daylight simulation with color temperature of 5500 K
    "o2d65"  	: (0.95047, 1.00000, 1.08883), # Noon daylight simulation with color temperature of 6500 K
    "o2d75"  	: (0.94972, 1.00000, 1.22638), # 
    "o2f2"   	: (0.99187, 1.00000, 0.67395), # Fluorescent
    "o2f7"   	: (0.95044, 1.00000, 1.08755), # 
    "o2f11"  	: (1.00966, 1.00000, 0.64370), # 
    "o10a"   	: (1.11144, 1.00000, 0.35200), # Tungsten illumination with color temperature of 3800 K
    "o10c"   	: (0.97285, 1.00000, 1.16145), # Fluorescent illumination with correlated color temperature about 5200 K
    "o10d50"	: (0.96720, 1.00000, 0.81427), # 
    "o10d55" 	: (0.95799, 1.00000, 0.90926), # Daylight simulation with color temperature of 5500 K
    "o10d65" 	: (0.94811, 1.00000, 1.07304), # Noon daylight simulation with color temperature of 6500 K
    "o10d75" 	: (0.94416, 1.00000, 1.20641), # 
    "o10f2"  	: (1.03280, 1.00000, 0.69026), # Fluorescent
    "o10f7"  	: (0.95792, 1.00000, 1.07687), # 
    "o10f11" 	: (1.03866, 1.00000, 0.65627)} # 

# X11 colour table (from "CSS3 module: Color working draft"), with
# gray/grey spelling issues fixed.  This is a superset of HTML 4.0
# colour names used in CSS 1.
namedColors = {
    "aliceblue":            "#f0f8ff",
    "antiquewhite":         "#faebd7",
    "aqua":                 "#00ffff",
    "aquamarine":           "#7fffd4",
    "azure":                "#f0ffff",
    "beige":                "#f5f5dc",
    "bisque":               "#ffe4c4",
    "black":                "#000000",
    "blanchedalmond":       "#ffebcd",
    "blue":                 "#0000ff",
    "blueviolet":           "#8a2be2",
    "brown":                "#a52a2a",
    "burlywood":            "#deb887",
    "cadetblue":            "#5f9ea0",
    "chartreuse":           "#7fff00",
    "chocolate":            "#d2691e",
    "coral":                "#ff7f50",
    "cornflowerblue":       "#6495ed",
    "cornsilk":             "#fff8dc",
    "crimson":              "#dc143c",
    "cyan":                 "#00ffff",
    "darkblue":             "#00008b",
    "darkcyan":             "#008b8b",
    "darkgoldenrod":        "#b8860b",
    "darkgray":             "#a9a9a9",
    "darkgrey":             "#a9a9a9",
    "darkgreen":            "#006400",
    "darkkhaki":            "#bdb76b",
    "darkmagenta":          "#8b008b",
    "darkolivegreen":       "#556b2f",
    "darkorange":           "#ff8c00",
    "darkorchid":           "#9932cc",
    "darkred":              "#8b0000",
    "darksalmon":           "#e9967a",
    "darkseagreen":         "#8fbc8f",
    "darkslateblue":        "#483d8b",
    "darkslategray":        "#2f4f4f",
    "darkslategrey":        "#2f4f4f",
    "darkturquoise":        "#00ced1",
    "darkviolet":           "#9400d3",
    "deeppink":             "#ff1493",
    "deepskyblue":          "#00bfff",
    "dimgray":              "#696969",
    "dimgrey":              "#696969",
    "dodgerblue":           "#1e90ff",
    "firebrick":            "#b22222",
    "floralwhite":          "#fffaf0",
    "forestgreen":          "#228b22",
    "fuchsia":              "#ff00ff",
    "gainsboro":            "#dcdcdc",
    "ghostwhite":           "#f8f8ff",
    "gold":                 "#ffd700",
    "goldenrod":            "#daa520",
    "gray":                 "#808080",
    "grey":                 "#808080",
    "green":                "#008000",
    "greenyellow":          "#adff2f",
    "honeydew":             "#f0fff0",
    "hotpink":              "#ff69b4",
    "indianred":            "#cd5c5c",
    "indigo":               "#4b0082",
    "ivory":                "#fffff0",
    "khaki":                "#f0e68c",
    "lavender":             "#e6e6fa",
    "lavenderblush":        "#fff0f5",
    "lawngreen":            "#7cfc00",
    "lemonchiffon":         "#fffacd",
    "lightblue":            "#add8e6",
    "lightcoral":           "#f08080",
    "lightcyan":            "#e0ffff",
    "lightgoldenrodyellow": "#fafad2",
    "lightgreen":           "#90ee90",
    "lightgray":            "#d3d3d3",
    "lightgrey":            "#d3d3d3",
    "lightpink":            "#ffb6c1",
    "lightsalmon":          "#ffa07a",
    "lightseagreen":        "#20b2aa",
    "lightskyblue":         "#87cefa",
    "lightslategray":       "#778899",
    "lightslategrey":       "#778899",
    "lightsteelblue":       "#b0c4de",
    "lightyellow":          "#ffffe0",
    "lime":                 "#00ff00",
    "limegreen":            "#32cd32",
    "linen":                "#faf0e6",
    "magenta":              "#ff00ff",
    "maroon":               "#800000",
    "mediumaquamarine":     "#66cdaa",
    "mediumblue":           "#0000cd",
    "mediumorchid":         "#ba55d3",
    "mediumpurple":         "#9370db",
    "mediumseagreen":       "#3cb371",
    "mediumslateblue":      "#7b68ee",
    "mediumspringgreen":    "#00fa9a",
    "mediumturquoise":      "#48d1cc",
    "mediumvioletred":      "#c71585",
    "midnightblue":         "#191970",
    "mintcream":            "#f5fffa",
    "mistyrose":            "#ffe4e1",
    "moccasin":             "#ffe4b5",
    "navajowhite":          "#ffdead",
    "navy":                 "#000080",
    "oldlace":              "#fdf5e6",
    "olive":                "#808000",
    "olivedrab":            "#6b8e23",
    "orange":               "#ffa500",
    "orangered":            "#ff4500",
    "orchid":               "#da70d6",
    "palegoldenrod":        "#eee8aa",
    "palegreen":            "#98fb98",
    "paleturquoise":        "#afeeee",
    "palevioletred":        "#db7093",
    "papayawhip":           "#ffefd5",
    "peachpuff":            "#ffdab9",
    "peru":                 "#cd853f",
    "pink":                 "#ffc0cb",
    "plum":                 "#dda0dd",
    "powderblue":           "#b0e0e6",
    "purple":               "#800080",
    "red":                  "#ff0000",
    "rosybrown":            "#bc8f8f",
    "royalblue":            "#4169e1",
    "saddlebrown":          "#8b4513",
    "salmon":               "#fa8072",
    "sandybrown":           "#f4a460",
    "seagreen":             "#2e8b57",
    "seashell":             "#fff5ee",
    "sienna":               "#a0522d",
    "silver":               "#c0c0c0",
    "skyblue":              "#87ceeb",
    "slateblue":            "#6a5acd",
    "slategray":            "#708090",
    "slategrey":            "#708090",
    "snow":                 "#fffafa",
    "springgreen":          "#00ff7f",
    "steelblue":            "#4682b4",
    "tan":                  "#d2b48c",
    "teal":                 "#008080",
    "thistle":              "#d8bfd8",
    "tomato":               "#ff6347",
    "turquoise":            "#40e0d0",
    "violet":               "#ee82ee",
    "wheat":                "#f5deb3",
    "white":                "#ffffff",
    "whitesmoke":           "#f5f5f5",
    "yellow":               "#ffff00",
    "yellowgreen":          "#9acd32",
}

class Color:
    def __init__(self, values, mode="rgb", alpha = 1.0):
    	if (mode == "rgb"):
    		self.__rgb = values
    		self.__hsl = rgbToHSL(*values)
    	elif (mode == "hsl"):
    		self.__hsl = values
    		self.__rgb = hslToRGB(*values)
    	else:
    		raise ValueError("Invalid color mode: " + mode)

        self.__a = alpha
    
    def __eq__(self, other):
    	if (isinstance(other, tuple)):
    		if (len(other) != 4):
    			return False
    		return self.__rgb + (self.__a,) == other
    	elif (isinstance(other, Color)):
    		return self.__rgb + (self.__a,) == other.__rgb + (other.__a,)

    def __repr__(self):
        return str(self.__rgb + (self.__a,))
    
    def __str__(self):
        return "(%.2f%%, %.2f%%, %.2f%%), a=%.2f%%" % tuple([v * 100 for v in self.__rgb] + [self.__a * 100])
    
    def __unicode__(self):
        return u"(%.2f%%, %.2f%%, %.2f%%), a=%.2f%%" % tuple([v * 100 for v in self.__rgb] + [self.__a * 100])
    
    def __iter__(self):
    	return iter(self.__rgb + (self.__a,))

    def __asRGB(self):
        return self.__rgb
    rgb = property(fget=__asRGB, doc="The RGB values of this Color.")

    def __asHSL(self):
        return self.__hsl
    hsl = property(fget=__asHSL, doc="The HSL values of this Color.")
    
    def __asHSV(self):
    	h, s, v = rgbToHSV(*self.__rgb)
        return (self.__hsl[0], s, v)
    hsv = property(fget=__asHSV, doc="The HSV values of this Color.")

    def __asYIQ(self):
        return rgbToYIQ(*self.__rgb)
    yiq = property(fget=__asYIQ, doc="The YIQ values of this Color.")
    
    def __asYUV(self):
        return rgbToYUV(*self.__rgb)
    yuv = property(fget=__asYUV, doc="The YUV values of this Color.")
    
    def __asXYZ(self):
        return rgbToXYZ(*self.__rgb)
    xyz = property(fget=__asXYZ, doc="The CIE-XYZ values of this Color.")
    
    def __asLAB(self, wref=(0.95047, 1.00000, 1.08883)):
        return xyzToLAB(wref=wref, *rgbToXYZ(*self.__rgb))
    lab = property(fget=__asLAB, doc="The CIE-LAB values of this Color.")
    
    def __asCMY(self):
        return rgbToCMY(*self.__rgb)
    cmy = property(fget=__asCMY, doc="The CMY values of this Color.")
    
    def __asCMYK(self):
        return cmyToCMYK(*rgbToCMY(*self.__rgb))
    cmyk = property(fget=__asCMYK, doc="The CMYK values of this Color.")
    
    def __asHTML(self):
        return rgbToHTML(*self.__rgb)
    html = property(fget=__asHTML, doc="This Color as an HTML color definition.")
    
    def __asPIL(self):
        return rgbToPIL(*self.__rgb)
    pil = property(fget=__asPIL, doc="This Color as a PIL compatible value.")

    def __aswebSafe(self):
        return rgbToWebSafe(*self.__rgb)
    webSafe = property(fget=__aswebSafe, doc="The web safe color nearest to this one (RGB).")
    
    def __asGreyscale(self):
        return rgbToGreyscale(*self.rgb)
    greyscale = property(fget=__asGreyscale, doc="The greyscale equivalent to this color (RGB).")

    def colorWitgAlpha(self, alpha):
        """
        Create a new Color based on this one, but with the provided alpha value.
        
        @param alpha	the color alpha [0~1].
        @return         a new Color instances.
        """
        return Color(self.__rgb, "rgb", alpha)

    def colorWithHue(self, hue):
        """
        Create a new Color based on this one, but with the provided hue value.
        
        @param hue		the color hue [0~360].
        @return         a new Color instances.
        """
        h, s, l = self.__asHSL()
        return fromHSL((hue, s, l), self.__a)
    
    def colorWithSaturation(self, saturation):
        """
        Create a new Color based on this one, but with the provided saturation value (using the HSL color model).
        
        @param saturation	the color saturation [0~1].
        @return         	a new Color instances
        """
        h, s, l = self.__asHSL()
        return fromHSL((h, saturation, l), self.__a)

    def colorWithLightness(self, lightness):
        """
        Create a new Color based on this one, but with the provided lightness value.
        
        @param lightness	the color lightness [0~1].
        @return         	a new Color instances
        """
        h, s, l = self.__asHSL()
        return fromHSL((h, s, lightness), self.__a)

    def darkerColor(self, level):
        """
        Create a new Color based on this one, but darker by the given level.
        
        @param level	the amount by which the color should be darkered [0~1].
        @return         a new Color instances
        """
        h, s, l = self.__asHSL()
        l = max(l - level, 0)
        return fromHSL((h, s, l), self.__a)
    
    def lighterColor(self, level):
        """
        Create a new Color based on this one, but lighter by the given level.
        
        @param level	the amount by which the color should be lightened [0~1].
        @return         a new Color instances
        """
        h, s, l = self.__asHSL()
        l = min(l + level, 1)
        return fromHSL((h, s, l), self.__a)

    def complementaryColor(self):
        """
        Create a new Color which is the complementary of this one.
        
        @return         a new Color instances
        """
        h, s, l = self.__asHSL()
        return fromHSL(((h + 180) % 360, s, l), self.__a)

    def webSafeDither(self):
        """
        Return a tuple of two Color which are the two web safe colors closest
        to the actual color represented by this one.
        """
        return (fromRGB(rgbToWebSafe(*self.__rgb), self.__a),
                fromRGB(rgbToWebSafe(alt = True, *self.__rgb), self.__a))

    def triadicScheme(self, angle=120):
        """
        Create a tuple of two Color which form a color triad with this one or a
        split complementary.
        
        @param angle	the angle between the complimentary and the triadic hues,
                        default is a regular triad.
        @return         a tuple of Color instances
        """
        h, s, l = self.__asHSL()
        angle = max(angle, 120) / 2.0
        h += 180
        h1 = (h - angle) % 360
        h2 = (h + angle) % 360
        return (fromHSL((h1, s, l), self.__a),
                fromHSL((h2, s, l), self.__a))

    def tetradicScheme(self):
        """
        Create a tuple of three Color which form a color tetrad with this one.
        
        @return         a tuple of Color instances
        """
        h, s, l = self.__asHSL()
        h1 = (h + 90) % 360
        h2 = (h + 180) % 360
        h3 = (h + 270) % 360
        return (fromHSL((h1, s, l), self.__a),
                fromHSL((h2, s, l), self.__a),
                fromHSL((h3, s, l), self.__a))

    def analogousScheme(self, angle=60):
        """
        Create a tuple of colors analogous to this one.
        
        @param angle	the angle between the colors hues.
        @return         a tuple of Color instances
        """
        h, s, l = self.__asHSL()
        h += 360
        h1 = (h - 60) % 360
        h2 = (h + 60) % 360
        return (fromHSL((h1, s, l), self.__a),
                fromHSL((h2, s, l), self.__a))

    def alphaBlend(self, other):
        """
        Create a new Color which is the result of alpha-blending this color with another one.
        
        @param other	the color to alpha-blend with this one.
        @return         a new Color instances
        """
        # get final alpha channel
        fa = self.__a + other.__a - (self.__a * other.__a)

        # get percentage of source alpha compared to final alpha
        if (fa == 0): sa = 0
        else: sa = self.__a / other.__a

        # destination percentage is just the additive inverse
        da = 1.0 - sa

        sr, sg, sb = [v * sa for v in self.__rgb]
        dr, dg, db = [v * da for v in other.__rgb]
        
        return fromRGB((sr+dr, sg+dg, sb+db), fa)

    def blend(self, other, percent=0.5):
        """
        Create a new Color which is the result of blending this color with another one.
        
        @param other	the color to blend with this one.
        @return         a new Color instances
        """
        source = 1.0 - percent
        f = lambda u,v: (u*0.5) + (v*0.5)
        r,g,b = map(f, self.__rgb, other.__rgb)
        a = f(self.__a, other.__a)
        return fromRGB((r,g,b), a)
