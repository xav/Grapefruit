# 
# GrapeFruit unit tests
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

import grapefruit
import unittest

class TestGrapeFruit(unittest.TestCase):
    def test_rgbToHSL(self):
        rgb = (1, 0.5, 0)
        hsl = (30.0, 1, 0.5)
        self.assertEqual(hsl, grapefruit.rgbToHSL(*rgb))

    def test_hslToRGB(self):
        hsl = (30, 1, 0.5)
        rgb = (1, 0.5, 0)
        self.assertEqual(rgb, grapefruit.hslToRGB(*hsl))

    def test_rgbToHSV(self):
        rgb = (1, 0.5, 0)
        hsv = (30, 1, 1)
        self.assertEqual(hsv, grapefruit.rgbToHSV(*rgb))

    def test_hsvToRGB(self):
        hsv = (30, 1, 1)
        rgb = (1, 0.5, 0)
        self.assertEqual(rgb, grapefruit.hsvToRGB(*hsv))

    def test_rgbToYIQ(self):
        rgb = (1, 0.5, 0)
        yiq = (0.59220000, 0.458849999,-0.05005000)
        y, i, q = grapefruit.rgbToYIQ(*rgb)
        self.assertAlmostEqual(y, yiq[0])
        self.assertAlmostEqual(i, yiq[1])
        self.assertAlmostEqual(q, yiq[2])

    def test_yiqToRGB(self):
        yiq = (0.5922, 0.45885,-0.05)
        rgb = (0.99990237, 0.49995545, -0.00006690)
        r, g, b = grapefruit.yiqToRGB(*yiq)
        self.assertAlmostEqual(r, rgb[0])
        self.assertAlmostEqual(g, rgb[1])
        self.assertAlmostEqual(b, rgb[2])

    def test_rgbToYUV(self):
        rgb = (1, 0.5, 0)
        yuv = (0.59250000, -0.29156000, 0.35750500)
        y, u, v = grapefruit.rgbToYUV(*rgb)
        self.assertAlmostEqual(y, yuv[0])
        self.assertAlmostEqual(u, yuv[1])
        self.assertAlmostEqual(v, yuv[2])

    def test_yuvToRGB(self):
        yuv = (0.5925, -0.2916, 0.3575)
        rgb = (0.99998922, 0.50001544, -0.00006327)
        r, g, b = grapefruit.yuvToRGB(*yuv)
        self.assertAlmostEqual(r, rgb[0])
        self.assertAlmostEqual(g, rgb[1])
        self.assertAlmostEqual(b, rgb[2])

    def test_rgbToXYZ(self):
        rgb = (1, 0.5, 0)
        xyz = (0.48898983, 0.36574466, 0.04484620)
        x, y, z = grapefruit.rgbToXYZ(*rgb)
        self.assertAlmostEqual(x, xyz[0])
        self.assertAlmostEqual(y, xyz[1])
        self.assertAlmostEqual(z, xyz[2])

    def test_xyzToRGB(self):
        xyz = (0.48899, 0.3658, 0.04485)
        rgb = (0.99996178, 0.50011237, -0.00009322)
        r, g, b = grapefruit.xyzToRGB(*xyz)
        self.assertAlmostEqual(r, rgb[0])
        self.assertAlmostEqual(g, rgb[1])
        self.assertAlmostEqual(b, rgb[2])

    def test_xyzToLAB(self):
        xyz = (0.48899, 0.3658, 0.04485)
        lab = (0.66960728, 0.43053315, 0.73964466)
        l, a, b = grapefruit.xyzToLAB(*xyz)
        self.assertAlmostEqual(l, lab[0])
        self.assertAlmostEqual(a, lab[1])
        self.assertAlmostEqual(b, lab[2])

    def test_labToXYZ(self):
        lab = (0.6696, 0.4305, 0.7396)
        xyz = (0.48896636, 0.36579036, 0.04485625)
        x, y, z = grapefruit.labToXYZ(*lab)
        self.assertAlmostEqual(x, xyz[0])
        self.assertAlmostEqual(y, xyz[1])
        self.assertAlmostEqual(z, xyz[2])

    def test_cmyToCMYK(self):
        cmy = (1, 0.66, 0.5)
        cmyk = (1, 0.32, 0, 0.5)
        c, m, y, k = grapefruit.cmyToCMYK(*cmy)
        self.assertAlmostEqual(c, cmyk[0])
        self.assertAlmostEqual(m, cmyk[1])
        self.assertAlmostEqual(y, cmyk[2])
        self.assertAlmostEqual(k, cmyk[3])

    def test_cmykToCMY(self):
        cmyk = (1, 0.32, 0, 0.5)
        cmy = (1, 0.66, 0.5)
        c, m, y = grapefruit.cmykToCMY(*cmyk)
        self.assertAlmostEqual(c, cmy[0])
        self.assertAlmostEqual(m, cmy[1])
        self.assertAlmostEqual(y, cmy[2])

    def test_rgbToCMY(self):
        rgb = (1, 0.5, 0)
        cmy = (0, 0.5, 1)
        c, m, y = grapefruit.rgbToCMY(*rgb)
        self.assertAlmostEqual(c, cmy[0])
        self.assertAlmostEqual(m, cmy[1])
        self.assertAlmostEqual(y, cmy[2])

    def test_cmyToRGB(self):
        cmy = (0, 0.5, 1)
        rgb = (1, 0.5, 0)
        r, g, b = grapefruit.cmyToRGB(*cmy)
        self.assertAlmostEqual(r, rgb[0])
        self.assertAlmostEqual(g, rgb[1])
        self.assertAlmostEqual(b, rgb[2])

    def test_rgbToHTML(self):
        rgb = (1, 0.5, 0)
        html = "#ff8000"
        html = grapefruit.rgbToHTML(*rgb)
        self.assertEqual(html, html)

    def test_htmlToRGB(self):
        html = "#ff8000"
        rgb = (1.0, 0.50196078, 0)
        r, g, b = grapefruit.htmlToRGB(html)
        self.assertAlmostEqual(r, rgb[0])
        self.assertAlmostEqual(g, rgb[1])
        self.assertAlmostEqual(b, rgb[2])

    def test_htmlToRGB_bare(self):
        html = "ff8000"
        rgb = (1.0, 0.50196078, 0)
        r, g, b = grapefruit.htmlToRGB(html)
        self.assertAlmostEqual(r, rgb[0])
        self.assertAlmostEqual(g, rgb[1])
        self.assertAlmostEqual(b, rgb[2])

    def test_htmlToRGB_webSafe(self):
        html = "#f60"
        rgb= (1.0, 0.4, 0)
        r, g, b = grapefruit.htmlToRGB(html)
        self.assertAlmostEqual(r, rgb[0])
        self.assertAlmostEqual(g, rgb[1])
        self.assertAlmostEqual(b, rgb[2])

    def test_rgbToPIL(self):
        rgb = (1, 0.5, 0)
        pil = 0x0080ff
        self.assertEqual(pil, grapefruit.rgbToPIL(*rgb))

    def test_pilToRGB(self):
        pil = 0x0080ff
        rgb = (1.0, 0.50196078, 0.0)
        r, g, b = grapefruit.pilToRGB(pil)
        self.assertAlmostEqual(r, rgb[0])
        self.assertAlmostEqual(g, rgb[1])
        self.assertAlmostEqual(b, rgb[2])
    
    def test_rgbToWebSafe(self):
        rgb = (1, 0.5, 0.0)
        rgb_safe = (1.0, 0.4, 0.0)

        r, g, b = grapefruit.rgbToWebSafe(*rgb)
        self.assertAlmostEqual(r, rgb_safe[0])
        self.assertAlmostEqual(g, rgb_safe[1])
        self.assertAlmostEqual(b, rgb_safe[2])

    def test_rgbToWebSafe_alt(self):
        rgb = (1, 0.5, 0.0)
        rgb_safe = (1.0, 0.6, 0.0)

        r, g, b = grapefruit.rgbToWebSafe(alt=True, *rgb)
        self.assertAlmostEqual(r, rgb_safe[0])
        self.assertAlmostEqual(g, rgb_safe[1])
        self.assertAlmostEqual(b, rgb_safe[2])

    def test_rgbToGreyscale(self):
        rgb = (1, 0.8, 0)
        g1, g2, g3 = grapefruit.rgbToGreyscale(*rgb)
        self.assertEqual(g1, g2)
        self.assertEqual(g2, g3)
        self.assertAlmostEqual(g1, 0.6)
    
    def test_fromRGB(self):
        rgb = (1.0, 0.5, 0.0)
        c = grapefruit.fromRGB(rgb)
        self.assertEqual(c, rgb + (1.0,))

    def test_fromHSL(self):
        hsl = (30, 1, 0.5)
        rgba = (1, 0.5, 0, 1.0)
        c = grapefruit.fromHSL(hsl)
        self.assertEqual(c, rgba)

    def test_fromHSV(self):
        hsv = (30, 1, 1)
        rgba = (1, 0.5, 0, 1.0)
        c = grapefruit.fromHSV(hsv)
        self.assertEqual(c, rgba)

    def test_fromYIQ(self):
        yiq = (0.5922, 0.45885,-0.05)
        rgba = (0.99990237, 0.49995545, -0.00006690, 1.0)
        c = grapefruit.fromYIQ(yiq)
        map(self.assertAlmostEqual, c, rgba)

    def test_fromYUV(self):
        yuv = (0.5925, -0.2916, 0.3575)
        rgba = (0.99998922, 0.50001544, -0.00006327, 1.0)
        c = grapefruit.fromYUV(yuv)
        map(self.assertAlmostEqual, c, rgba)

    def test_fromXYZ(self):
        xyz = (0.48899, 0.3658, 0.04485)
        rgba = (0.99996178, 0.50011237, -0.00009322, 1.0)
        c = grapefruit.fromXYZ(xyz)
        map(self.assertAlmostEqual, c, rgba)

    def test_fromLAB(self):
        lab = (0.6696, 0.4305, 0.7396)
        rgba = (0.99993325, 0.50011787, 0.00000063, 1.0)
        c = grapefruit.fromLAB(lab)
        map(self.assertAlmostEqual, c, rgba)

    def test_fromCMY(self):
        cmy = (0, 0.5, 1)
        rgba = (1, 0.5, 0, 1.0)
        c = grapefruit.fromCMY(cmy)
        map(self.assertAlmostEqual, c, rgba)

    def test_fromCMYK(self):
        cmyk = (1, 0.32, 0, 0.5)
        rgba = (0, 0.33999999, 0.5, 1.0)
        c = grapefruit.fromCMYK(cmyk)
        map(self.assertAlmostEqual, c, rgba)

    def test_fromHTML(self):
        html = "#ff8000"
        rgba = (1, 0.50196078, 0, 1.0)
        c = grapefruit.fromHTML(html)
        map(self.assertAlmostEqual, c, rgba)

    def test_fromPIL(self):
        pil = 0x0080ff
        rgba = (1.0, 0.50196078, 0.0, 1.0)
        c = grapefruit.fromPIL(pil)
        map(self.assertAlmostEqual, c, rgba)

    def test_asRGB(self):
        rgb = (1, 0.5, 0)
        c = grapefruit.fromRGB(rgb)
        self.assertEqual(c.rgb, rgb)

    def test_asHSL(self):
        hsl = (30, 1, 0.5)
        c = grapefruit.fromHSL(hsl)
        self.assertEqual(c.hsl, hsl)
    
    def test_asHSV(self):
        hsv = (30, 1, 1)
        c = grapefruit.fromHSV(hsv)
        self.assertEqual(c.hsv, hsv)

    def test_asYIQ(self):
        yiq = (0.59213723, 0.45885,-0.05006816)
        c = grapefruit.fromYIQ(yiq)
        self.assertAlmostEqual(c.yiq[0], yiq[0], 3)
        self.assertAlmostEqual(c.yiq[1], yiq[1], 4)
        self.assertAlmostEqual(c.yiq[2], yiq[2], 3)
    
    def test_asYUV(self):
        yuv = (0.59249862, -0.29159046, 0.35749675)
        c = grapefruit.fromYUV(yuv)
        self.assertAlmostEqual(c.yuv[0], yuv[0], 4)
        self.assertAlmostEqual(c.yuv[1], yuv[1], 4)
        self.assertAlmostEqual(c.yuv[2], yuv[2], 4)
    
    def test_asXYZ(self):
        xyz = (0.48898986, 0.3658, 0.044850067)
        c = grapefruit.fromXYZ(xyz)
        self.assertAlmostEqual(c.xyz[0], xyz[0], 6)
        self.assertAlmostEqual(c.xyz[1], xyz[1])
        self.assertAlmostEqual(c.xyz[2], xyz[2], 5)
    
    def test_asLAB(self):
        lab = (0.6696, 0.43049948, 0.73959971)
        c = grapefruit.fromLAB(lab)
        self.assertAlmostEqual(c.lab[0], lab[0])
        self.assertAlmostEqual(c.lab[1], lab[1], 5)
        self.assertAlmostEqual(c.lab[2], lab[2], 6)
    
    def test_asCMY(self):
        cmy = (0, 0.5, 1)
        c = grapefruit.fromCMY(cmy)
        self.assertEqual(c.cmy, cmy)
    
    def test_asCMYK(self):
        cmyk = (1, 0.32, 0, 0.5)
        c = grapefruit.fromCMYK(cmyk)
        self.assertAlmostEqual(c.cmyk[0], cmyk[0])
        self.assertAlmostEqual(c.cmyk[1], cmyk[1])
        self.assertAlmostEqual(c.cmyk[2], cmyk[2])
        self.assertAlmostEqual(c.cmyk[3], cmyk[3])
    
    def test_asHTML(self):
        html = "#ff8000"
        c = grapefruit.fromHTML(html)
        self.assertEqual(c.html, html)
    
    def test_asPIL(self):
        pil = 0x0080ff
        c = grapefruit.fromPIL(pil)
        self.assertEqual(c.pil, pil)

    def test_asWebSafe(self):
        srgb = (1.0, 0.4, 0.0)
        c1 = grapefruit.fromRGB((1.0, 0.5, 0.0))
        self.assertAlmostEqual(c1.webSafe[0], srgb[0])
        self.assertAlmostEqual(c1.webSafe[1], srgb[1])
        self.assertAlmostEqual(c1.webSafe[2], srgb[2])

    def test_asGreyscale(self):
        c = grapefruit.fromRGB((1, 0.8, 0))
        self.assertAlmostEqual(c.greyscale[0], 0.6)
        self.assertAlmostEqual(c.greyscale[1], 0.6)
        self.assertAlmostEqual(c.greyscale[2], 0.6)

    def test_colorWitgAlpha(self):
        rgb = (1.0, 0.5, 0.0)
        c1 = grapefruit.fromRGB(rgb, 1)
        c2 = grapefruit.fromRGB(rgb, 0.5)
        c3 = c1.colorWitgAlpha(0.5)
        self.assertEqual(c2, c3)

    def test_colorWithHue(self):
        c1 = grapefruit.fromHSL((30, 1, 0.5))
        c2 = grapefruit.fromHSL((60, 1, 0.5))
        c3 = c1.colorWithHue(60)
        self.assertEqual(c2, c3)
    
    def test_colorWithSaturation(self):
        c1 = grapefruit.fromHSL((30, 1, 0.5))
        c2 = grapefruit.fromHSL((30, 0.5, 0.5))
        c3 = c1.colorWithSaturation(0.5)
        self.assertEqual(c2, c3)

    def test_colorWithLightness(self):
        c1 = grapefruit.fromHSL((30, 1, 1))
        c2 = grapefruit.fromHSL((30, 1, 0.5))
        c3 = c1.colorWithLightness(0.5)
        self.assertEqual(c2, c3)

    def test_darkerColor(self):
        c1 = grapefruit.fromHSL((30, 1, 1))
        c2 = grapefruit.fromHSL((30, 1, 0.7))
        c3 = c1.darkerColor(0.3)
        self.assertEqual(c2, c3)
    
    def test_lighterColor(self):
        c1 = grapefruit.fromHSL((30, 1, 0))
        c2 = grapefruit.fromHSL((30, 1, 0.3))
        c3 = c1.lighterColor(0.3)
        self.assertEqual(c2, c3)

    def test_complementaryColor(self):
        c1 = grapefruit.fromRGB((1.0, 0.5, 0.0))
        c2 = c1.complementaryColor()
        self.assertEqual(c2, (0, 0.5, 1, 1))

    def test_webSafeDither(self):
        rgb1 = (1.0, 0.4, 0.0, 1.0)
        rgb2 = (1.0, 0.6, 0.0, 1.0)
        c = grapefruit.fromRGB((1.0, 0.5, 0.0))
        c1, c2 = c.webSafeDither()
        map(self.assertEqual, c1, rgb1)
        map(self.assertEqual, c2, rgb2)

    def test_triadicScheme(self):
        rgb1 = (0.0, 1.0, 0.5, 1.0)
        rgb2 = (0.0, 0.0, 1.0, 1.0)
        c = grapefruit.fromRGB((1.0, 0.5, 0.0))
        c1, c2 = c.triadicScheme()
        self.assertEqual(c1, rgb1)
        self.assertEqual(c2, rgb2)

    def test_tetradicScheme(self):
        rgb1 = (0.0, 1.0, 0.0, 1.0)
        rgb2 = (0.0, 0.5, 1.0, 1.0)
        rgb3 = (0.0, 0.0, 1.0, 1.0)
        c = grapefruit.fromRGB((1.0, 0.5, 0.0))
        c1, c2, c3 = c.tetradicScheme()
        self.assertEqual(c1, rgb1)
        self.assertEqual(c2, rgb2)
        self.assertEqual(c3, rgb3)

    def test_analogousScheme(self):
        rgb1 = (0.0, 0.0, 0.5, 1.0)
        rgb2 = (0.5, 1.0, 0.0, 1.0)
        c = grapefruit.fromRGB((1.0, 0.5, 0.0))
        c1, c2 = c.analogousScheme()
        self.assertEqual(c1, rgb1)
        self.assertEqual(c2, rgb2)

    def test_alphaBlend(self):
        c1 = grapefruit.fromRGB((1, 0.5, 0), 0.2)
        c2 = grapefruit.fromRGB((1, 1, 1), 0.8)
        map(self.assertAlmostEqual, c1.alphaBlend(c2), (1, 0.875, 0.75, 0.83999999))

    def test_blend(self):
        c1 = grapefruit.fromRGB((1, 0.5, 0), 0.2)
        c2 = grapefruit.fromRGB((1, 1, 1), 0.6)
        self.assertEqual(c1.blend(c2), (1, 0.75, 0.5, 0.4))

if __name__ == '__main__':
    unittest.main()
