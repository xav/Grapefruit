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

'''Unit tests for the grapefruit module.'''

# $Id$
__author__ = 'xbasty@gmail.com'
__version__ = '0.1a3'

import unittest
import grapefruit

class GrapeFruitTestCase(unittest.TestCase):
  def failUnlessNear(self, first, second, diff=9e-5, msg=None):
    '''
    Fail if the difference between the two objects is greater
    than a certain amout (default 9e-5).
    '''
    if hasattr(first,'__iter__') and hasattr(second,'__iter__'):
      if len(first) != len(second):
        raise self.failureException, (msg or "%r != %r" % (first, second))
      
      for f, s in zip(first, second):
        if abs(s-f) > diff:
          raise self.failureException, (msg or "%r != %r @ %f" % (first, second, diff))
    elif abs(second-first) > diff:
      raise self.failureException, (msg or "%r != %r @ %f" % (first, second, diff))
  assertNear = failUnlessNear

class ConversionTest(GrapeFruitTestCase):
  '''Test the static color conversion methods.'''

  def testRgbHsl(self):
    self.assertNear((30.0, 1.0, 0.5), grapefruit.Color.RgbToHsl(1, 0.5, 0))
    self.assertNear((20.0, 1.0, 0.625), grapefruit.Color.RgbToHsl(1, 0.5, 0.25)) #ff8040
    self.assertNear((40.0, 1.0, 0.375), grapefruit.Color.RgbToHsl(0.75, 0.5, 0)) #bf8000

    self.assertNear((1, 0.5, 0), grapefruit.Color.HslToRgb(30.0, 1.0, 0.5))
    self.assertNear((1, 0.5, 0.25), grapefruit.Color.HslToRgb(20.0, 1.0, 0.625))
    self.assertNear((0.75, 0.5, 0), grapefruit.Color.HslToRgb(40.0, 1.0, 0.375))
  
  def testRgbHsv(self):
    self.assertEqual((30.0, 1.0, 1.0), grapefruit.Color.RgbToHsv(1, 0.5, 0))
    self.assertEqual((1, 0.5, 0), grapefruit.Color.HsvToRgb(30.0, 1.0, 1.0))
  
  def testRgbYiq(self):
    self.assertNear((0.5923, 0.4589, -0.05), grapefruit.Color.RgbToYiq(1, 0.5, 0))
    self.assertNear((1, 0.5, 0), grapefruit.Color.YiqToRgb(0.5923, 0.4589, -0.05))
  
  def testRgbYuv(self):
    self.assertNear((0.5925, -0.2916, 0.3575), grapefruit.Color.RgbToYuv(1, 0.5, 0))
    self.assertNear((1, 0.5, 0), grapefruit.Color.YuvToRgb(0.5925, -0.2916, 0.3575))
  
  def testRgbXyz(self):
    self.assertNear((0.4890, 0.3657, 0.04485), grapefruit.Color.RgbToXyz(1, 0.5, 0))
    self.assertNear((1, 0.5, 0), grapefruit.Color.XyzToRgb(0.488941, 0.365682, 0.0448137))
  
  def testXyzLab(self):
    self.assertNear((66.9518, 0.4308, 0.7397), grapefruit.Color.XyzToLab(0.488941, 0.365682, 0.0448137))
    self.assertNear((0.4890, 0.3657, 0.0449), grapefruit.Color.LabToXyz(66.9518, 0.4308, 0.7397))
    self.assertNear((66.9518, 0.4117, 0.6728), grapefruit.Color.XyzToLab(0.488941, 0.365682, 0.0448137, grapefruit.Color.WHITE_REFERENCE["std_D50"]))
    self.assertNear((0.4890, 0.3657, 0.0449), grapefruit.Color.LabToXyz(66.9518, 0.4117, 0.6728, grapefruit.Color.WHITE_REFERENCE["std_D50"]))
  
  def testCmykCmy(self):
    self.assertNear((1, 0.32, 0, 0.5), grapefruit.Color.CmyToCmyk(1.0, 0.66, 0.5))
    self.assertNear((1.0, 0.66, 0.5), grapefruit.Color.CmykToCmy(1, 0.32, 0, 0.5))
  
  def testRgbCmy(self):
    self.assertEqual((0, 0.5, 1), grapefruit.Color.RgbToCmy(1, 0.5, 0))
    self.assertEqual((1, 0.5, 0), grapefruit.Color.CmyToRgb(0, 0.5, 1))
  
  def testRgbHtml(self):
    self.assertEqual("#ff8000", grapefruit.Color.RgbToHtml(1, 0.5, 0))
    self.assertNear((1.0, 0.5020, 0.0), grapefruit.Color.HtmlToRgb("#ff8000"))
    self.assertNear((1.0, 0.5020, 0.0), grapefruit.Color.HtmlToRgb("ff8000"))
    self.assertNear((1.0, 0.4, 0.0), grapefruit.Color.HtmlToRgb("#f60"))
    self.assertNear((1.0, 0.4, 0.0), grapefruit.Color.HtmlToRgb("f60"))
    self.assertNear((1.000000, 0.980392, 0.803922), grapefruit.Color.HtmlToRgb("lemonchiffon"))
  
  def testRgbPil(self):
    self.assertNear(0x0080ff, grapefruit.Color.RgbToPil(1, 0.5, 0))
    self.assertNear((1.0, 0.5020, 0), grapefruit.Color.PilToRgb(0x0080ff))
  
  def testWebSafeComponent(self):
    self.assertEqual(0.2, grapefruit.Color._WebSafeComponent(0.2))
    self.assertEqual(0.2, grapefruit.Color._WebSafeComponent(0.25))
    self.assertEqual(0.4, grapefruit.Color._WebSafeComponent(0.3))
    self.assertEqual(0.4, grapefruit.Color._WebSafeComponent(0.25, True))
    self.assertEqual(0.2, grapefruit.Color._WebSafeComponent(0.2, True))
    self.assertEqual(0.2, grapefruit.Color._WebSafeComponent(0.3, True))

  def testRgbToWebSafe(self):
    self.assertEqual((1.0, 0.6, 0.0), grapefruit.Color.RgbToWebSafe(1, 0.55, 0.0))
    self.assertEqual((1.0, 0.4, 0.0), grapefruit.Color.RgbToWebSafe(1, 0.55, 0.0, True))
    self.assertEqual((1.0, 0.4, 0.0), grapefruit.Color.RgbToWebSafe(1, 0.5, 0.0, True))
  
  def testRgbToGreyscale(self):
    self.assertEqual((0.6, 0.6, 0.6), grapefruit.Color.RgbToGreyscale(1, 0.8, 0))

class NewFromTest(GrapeFruitTestCase):
  '''Test the static color instanciation methods.'''
  def testNewFromRgb(self):
    c = grapefruit.Color.NewFromRgb(1.0, 0.5, 0.0)
    self.assertEqual(c, (1.0, 0.5, 0.0, 1.0))
    c = grapefruit.Color.NewFromRgb(1.0, 0.5, 0.0, 0.5)
    self.assertEqual(c, (1.0, 0.5, 0.0, 0.5))

  def testNewFromHsl(self):
    c = grapefruit.Color.NewFromHsl(30, 1, 0.5)
    self.assertEqual(c, (1.0, 0.5, 0.0, 1.0))
    c = grapefruit.Color.NewFromHsl(30, 1, 0.5, 0.5)
    self.assertEqual(c, (1.0, 0.5, 0.0, 0.5))
  
  def testNewFromHsv(self):
    c = grapefruit.Color.NewFromHsv(30, 1, 1)
    self.assertEqual(c, (1.0, 0.5, 0.0, 1.0))
    c = grapefruit.Color.NewFromHsv(30, 1, 1, 0.5)
    self.assertEqual(c, (1.0, 0.5, 0.0, 0.5))
  
  def testNewFromYiq(self):
    c = grapefruit.Color.NewFromYiq(0.5923, 0.4589, -0.0499818)
    self.assertNear(c, (1, 0.5, 0, 1))
    c = grapefruit.Color.NewFromYiq(0.5923, 0.4589,-0.05, 0.5)
    self.assertNear(c, (1, 0.5, 0, 0.5))
  
  def testNewFromYuv(self):
    c = grapefruit.Color.NewFromYuv(0.5925, -0.2916, 0.3575)
    self.assertNear(c, (1, 0.5, 0, 1))
    c = grapefruit.Color.NewFromYuv(0.5925, -0.2916, 0.3575, 0.5)
    self.assertNear(c, (1, 0.5, 0, 0.5))
  
  def testNewFromXyz(self):
    c = grapefruit.Color.NewFromXyz(0.488941, 0.365682, 0.0448137)
    self.assertNear(c, (1, 0.5, 0, 1))
    c = grapefruit.Color.NewFromXyz(0.488941, 0.365682, 0.0448137, 0.5)
    self.assertNear(c, (1, 0.5, 0, 0.5))
  
  def testNewFromLab(self):
    c = grapefruit.Color.NewFromLab(66.9518, 0.43084, 0.739692)
    self.assertNear(c, (1, 0.5, 0, 1))
    c = grapefruit.Color.NewFromLab(66.9518, 0.43084, 0.739692, wref=grapefruit.Color.WHITE_REFERENCE["std_D50"])
    self.assertNear(c, (1.0123754, 0.492012, -0.143110, 1))
    c = grapefruit.Color.NewFromLab(66.9518, 0.43084, 0.739692, 0.5)
    self.assertNear(c, (1, 0.5, 0, 0.5))
    c = grapefruit.Color.NewFromLab(66.9518, 0.43084, 0.739692, 0.5, grapefruit.Color.WHITE_REFERENCE["std_D50"])
    self.assertNear(c, (1.0123754, 0.492012, -0.143110, 0.5))
  
  def testNewFromCmy(self):
    c = grapefruit.Color.NewFromCmy(0, 0.5, 1)
    self.assertEqual(c, (1, 0.5, 0, 1.0))
    c = grapefruit.Color.NewFromCmy(0, 0.5, 1, 0.5)
    self.assertEqual(c, (1, 0.5, 0, 0.5))
  
  def testNewFromCmyk(self):
    c = grapefruit.Color.NewFromCmyk(1, 0.32, 0, 0.5)
    self.assertNear(c, (0, 0.34, 0.5, 1))
    c = grapefruit.Color.NewFromCmyk(1, 0.32, 0, 0.5, 0.5)
    self.assertNear(c, (0, 0.34, 0.5, 0.5))
  
  def testNewFromHtml(self):
    c = grapefruit.Color.NewFromHtml("#ff8000")
    self.assertNear(c, (1, 0.5020, 0, 1))
    c = grapefruit.Color.NewFromHtml("ff8000")
    self.assertNear(c, (1, 0.5020, 0, 1))
    c = grapefruit.Color.NewFromHtml("#f60")
    self.assertNear(c, (1, 0.4, 0, 1))
    c = grapefruit.Color.NewFromHtml("f60")
    self.assertNear(c, (1, 0.4, 0, 1))
    c = grapefruit.Color.NewFromHtml("lemonchiffon")
    self.assertNear(c, (1, 0.9804, 0.8039, 1))
    c = grapefruit.Color.NewFromHtml("#ff8000", 0.5)
    self.assertNear(c, (1, 0.5020, 0, 0.5))
  
  def testNewFromPil(self):
    c = grapefruit.Color.NewFromPil(0x0080ff)
    self.assertNear(c, (1, 0.5020, 0, 1))
    c = grapefruit.Color.NewFromPil(0x0080ff, 0.5)
    self.assertNear(c, (1, 0.5020, 0, 0.5))
  

class ColorTest(GrapeFruitTestCase):
  def setUp(self):
    self.rgbCol = grapefruit.Color.NewFromRgb(1.0, 0.5, 0.0)
    self.hslCol = grapefruit.Color.NewFromHsl(30, 1, 0.5)
    self.hslCol2 = grapefruit.Color.NewFromHsl(30, 0.5, 0.5)

  def testInit(self):
    self.assertEqual(grapefruit.Color((1.0, 0.5, 0.0)), (1.0, 0.5, 0.0, 1.0))
    self.assertEqual(grapefruit.Color((1.0, 0.5, 0.0), mode='rgb'), (1.0, 0.5, 0.0, 1.0))
    self.assertEqual(grapefruit.Color((30, 1, 0.5), mode='hsl'), (1.0, 0.5, 0.0, 1.0))
    
    self.assertRaises(ValueError, grapefruit.Color, (30, 1, 0.5), 'hsv')
  
  def testEq(self):
    self.assertEqual(self.rgbCol, self.hslCol)
    self.assertEqual(self.rgbCol, (1.0, 0.5, 0.0, 1.0))
    self.assertEqual(self.rgbCol, [1.0, 0.5, 0.0, 1.0])
    self.assertEqual([1.0, 0.5, 0.0, 1.0], self.rgbCol)
    self.assertNotEqual(self.rgbCol, '(1.0, 0.5, 0.0, 1.0)')
    
  def testRepr(self):
    self.assertEqual(repr(self.rgbCol), '(1.0, 0.5, 0.0, 1.0)')
    self.assertEqual(repr(self.hslCol), '(1.0, 0.5, 0.0, 1.0)')
  
  def testStr(self):
    self.assertEqual(str(self.rgbCol), '(1, 0.5, 0, 1)')
    self.assertEqual(str(self.hslCol), '(1, 0.5, 0, 1)')
  
  def testIter(self):
    self.assertEqual([1, 0.5, 0, 1], list(iter(self.rgbCol)))
  
  def testProperties(self):
    self.assertEqual(self.rgbCol.alpha, 1.0)
    self.assertEqual(self.rgbCol.whiteRef, grapefruit.Color.WHITE_REFERENCE['std_D65'])
    self.assertEqual(self.rgbCol.rgb, (1, 0.5, 0))
    self.assertEqual(self.hslCol.hue, 30)
    self.assertEqual(self.rgbCol.hsl, (30, 1, 0.5))
    self.assertEqual(self.rgbCol.hsv, (30, 1, 1))
    self.assertNear(self.rgbCol.yiq, (0.5923, 0.4589, -0.05))
    self.assertNear(self.rgbCol.yuv, (0.5925, -0.2916, 0.3575))
    self.assertNear(self.rgbCol.xyz, (0.4890, 0.3657, 0.04485))
    self.assertNear(self.rgbCol.lab, (66.9518, 0.4308, 0.7397))
    self.assertEqual(self.rgbCol.cmy, (0, 0.5, 1))
    self.assertEqual(self.rgbCol.cmyk, (0, 0.5, 1, 0))
    self.assertEqual(self.rgbCol.html, '#ff8000')
    self.assertEqual(self.rgbCol.pil, 0x0080ff)
    self.assertEqual(self.rgbCol.webSafe, (1, 0.6, 0))
    self.assertEqual(self.rgbCol.greyscale, (0.5, 0.5, 0.5))
    
    c = grapefruit.Color.NewFromRgb(1, 0.5, 0, wref=grapefruit.Color.WHITE_REFERENCE['std_D50'])
    self.assertNear(c.lab, (66.9518, 0.4117, 0.6728))
  
  def testColorWitgAlpha(self):
    self.assertEqual(self.rgbCol.ColorWithAlpha(0.5), (1, 0.5, 0, 0.5))
  
  def testColorWithWhiteRef(self):
    self.assertEqual(self.hslCol.ColorWithWhiteRef((0.1, 0.2, 0.3)).whiteRef, (0.1, 0.2, 0.3))
  
  def testColorWithHue(self):
    self.assertEqual(self.hslCol.ColorWithHue(60), (1.0, 1.0, 0.0, 1.0))
    self.assertEqual(self.hslCol.ColorWithHue(60).hsl, (60, 1, 0.5))
  
  def testColorWithSaturation(self):
    self.assertEqual(self.hslCol.ColorWithSaturation(0.5), (0.75, 0.5, 0.25, 1.0))
    self.assertEqual(self.hslCol.ColorWithSaturation(0.5).hsl, (30, 0.5, 0.5))
  
  def testColorWithLightness(self):
    self.assertEqual(self.hslCol.ColorWithLightness(1), (1.0, 1.0, 1.0, 1.0))
    self.assertEqual(self.hslCol.ColorWithLightness(1).hsl, (30, 1.0, 1.0))
  
  def testDarkerColor(self):
    self.assertNear(self.hslCol.DarkerColor(0.2), (0.6, 0.3, 0.0, 1.0))
    self.assertNear(self.hslCol.DarkerColor(0.2).hsl, (30, 1, 0.3))
  
  def testLighterColor(self):
    self.assertNear(self.hslCol.LighterColor(0.2), (1.0, 0.7, 0.4, 1.0))
    self.assertNear(self.hslCol.LighterColor(0.2).hsl, (30, 1, 0.7))
  
  def testSaturate(self):
    self.assertNear(self.hslCol2.Saturate(0.25), (0.875, 0.5, 0.125, 1.0))
    self.assertNear(self.hslCol2.Saturate(0.25).hsl, (30, 0.75, 0.5))
  
  def testDesaturate(self):
    self.assertNear(self.hslCol2.Desaturate(0.25), (0.625, 0.5, 0.375, 1.0))
    self.assertNear(self.hslCol2.Desaturate(0.25).hsl, (30, 0.25, 0.5))
  
  def testWebSafeDither(self):
    dithered = (
      (1.0, 0.6, 0.0, 1.0),
      (1.0, 0.4, 0.0, 1.0))
    self.assertEqual(self.rgbCol.WebSafeDither(), dithered)
  
  def testGradient(self):
    gradient = [
      (0.75, 0.25, 0.0, 1.0),
      (0.5, 0.5, 0.0, 1.0),
      (0.25, 0.75, 0.0, 1.0)]
    c1 = grapefruit.Color.NewFromRgb(1.0, 0.0, 0.0)
    c2 = grapefruit.Color.NewFromRgb(0.0, 1.0, 0.0)
    self.assertEqual(gradient, c1.Gradient(c2, 3))
  
  def testComplementaryColor(self):
    self.assertEqual(self.hslCol.ComplementaryColor(mode='rgb').hsl, (210, 1, 0.5))
  
  def testMonochromeScheme(self):
    monochrome = (
      (0.94, 0.8, 0.66, 1.0), # hsl(30, 0.7, 0.8)
      (0.6, 0.3, 0.0, 1.0),   # hsl(30, 1, 0.3)
      (0.88, 0.6, 0.32, 1.0), # hsl(30, 0.7, 0.6)
      (1.0, 0.8, 0.6, 1.0))   # hsl(30, 1, 0.8)
    scheme = self.rgbCol.MonochromeScheme()
    for i in xrange(len(monochrome)):
      self.assertNear(scheme[i], monochrome[i])
  
  def testTriadicScheme(self):
    triad = (
      (0.0, 1.0, 0.5, 1.0),
      (0.5, 0.0, 1.0, 1.0))
    self.assertEqual(self.rgbCol.TriadicScheme(mode='rgb'), triad)
  
  def testTetradicScheme(self):
    tetrad = (
      (0.5, 1.0, 0.0, 1.0),
      (0.0, 0.5, 1.0, 1.0),
      (0.5, 0.0, 1.0, 1.0))
    self.assertEqual(self.rgbCol.TetradicScheme(mode='rgb'), tetrad)
  
  def testAnalogousScheme(self):
    scheme = (
      (1.0, 0.0, 0.0, 1.0),
      (1.0, 1.0, 0.0, 1.0))
    self.assertEqual(self.rgbCol.AnalogousScheme(mode='rgb'), scheme)
  
  def testAlphaBlend(self):
    c1 = grapefruit.Color.NewFromRgb(1, 0.5, 0, alpha = 0.2)
    c2 = grapefruit.Color.NewFromRgb(1, 1, 1, alpha = 0.8)
    self.assertNear(c1.AlphaBlend(c2), (1, 0.875, 0.75, 0.84))
  
  def testBlend(self):
    c1 = grapefruit.Color.NewFromRgb(1, 0.5, 0, alpha = 0.2)
    c2 = grapefruit.Color.NewFromRgb(1, 1, 1, alpha = 0.6)
    self.assertEqual(c1.Blend(c2), (1, 0.75, 0.5, 0.4))
  

if __name__ == '__main__':
  unittest.main()
  pass
