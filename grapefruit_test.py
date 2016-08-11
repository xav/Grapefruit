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

import grapefruit
from nose.tools import *

def assert_items_almost_equal(first, second, places=3, msg=None, delta=None):
  """assert_almost_equal for iterables"""
  assert_equal(len(first), len(second))

  for f, s in zip(first, second):
    assert_almost_equal(f, s, places, msg, delta)

class TestConversion():
  '''Test the static color conversion methods.'''

  def test_RgbHsl(self):
    assert_items_almost_equal((30.0, 1.0, 0.5), grapefruit.Color.RgbToHsl(1, 0.5, 0))
    assert_items_almost_equal((20.0, 1.0, 0.625), grapefruit.Color.RgbToHsl(1, 0.5, 0.25)) #ff8040
    assert_items_almost_equal((40.0, 1.0, 0.375), grapefruit.Color.RgbToHsl(0.75, 0.5, 0)) #bf8000

    assert_items_almost_equal((1, 0.5, 0), grapefruit.Color.HslToRgb(30.0, 1.0, 0.5))
    assert_items_almost_equal((1, 0.5, 0.25), grapefruit.Color.HslToRgb(20.0, 1.0, 0.625))
    assert_items_almost_equal((0.75, 0.5, 0), grapefruit.Color.HslToRgb(40.0, 1.0, 0.375))

  def test_RgbHsv(self):
    assert_equal((30.0, 1.0, 1.0), grapefruit.Color.RgbToHsv(1, 0.5, 0))
    assert_equal((1, 0.5, 0), grapefruit.Color.HsvToRgb(30.0, 1.0, 1.0))

  def test_RgbYiq(self):
    assert_items_almost_equal((0.5923, 0.4589, -0.05), grapefruit.Color.RgbToYiq(1, 0.5, 0))
    assert_items_almost_equal((1, 0.5, 0), grapefruit.Color.YiqToRgb(0.5923, 0.4589, -0.05))

  def test_RgbYuv(self):
    assert_items_almost_equal((0.5925, -0.2916, 0.3575), grapefruit.Color.RgbToYuv(1, 0.5, 0))
    assert_items_almost_equal((1, 0.5, 0), grapefruit.Color.YuvToRgb(0.5925, -0.2916, 0.3575))

  def test_RgbXyz(self):
    assert_items_almost_equal((0.4890, 0.3657, 0.04485), grapefruit.Color.RgbToXyz(1, 0.5, 0))
    assert_items_almost_equal((1, 0.5, 0), grapefruit.Color.XyzToRgb(0.488941, 0.365682, 0.0448137))

  def test_XyzLab(self):
    assert_items_almost_equal((66.9518, 0.4308, 0.7397), grapefruit.Color.XyzToLab(0.488941, 0.365682, 0.0448137))
    assert_items_almost_equal((0.4890, 0.3657, 0.0449), grapefruit.Color.LabToXyz(66.9518, 0.4308, 0.7397))
    assert_items_almost_equal((66.9518, 0.4117, 0.6728), grapefruit.Color.XyzToLab(0.488941, 0.365682, 0.0448137, grapefruit.Color.WHITE_REFERENCE["std_D50"]))
    assert_items_almost_equal((0.4890, 0.3657, 0.0449), grapefruit.Color.LabToXyz(66.9518, 0.4117, 0.6728, grapefruit.Color.WHITE_REFERENCE["std_D50"]))

  def test_CmykCmy(self):
    assert_items_almost_equal((1, 0.32, 0, 0.5), grapefruit.Color.CmyToCmyk(1.0, 0.66, 0.5))
    assert_items_almost_equal((1.0, 0.66, 0.5), grapefruit.Color.CmykToCmy(1, 0.32, 0, 0.5))

  def test_RgbCmy(self):
    assert_equal((0, 0.5, 1), grapefruit.Color.RgbToCmy(1, 0.5, 0))
    assert_equal((1, 0.5, 0), grapefruit.Color.CmyToRgb(0, 0.5, 1))

  def test_RgbHtml(self):
    assert_equal("#ff8000", grapefruit.Color.RgbToHtml(1, 0.5, 0))
    assert_items_almost_equal((1.0, 0.5020, 0.0), grapefruit.Color.HtmlToRgb("#ff8000"))
    assert_items_almost_equal((1.0, 0.5020, 0.0), grapefruit.Color.HtmlToRgb("ff8000"))
    assert_items_almost_equal((1.0, 0.4, 0.0), grapefruit.Color.HtmlToRgb("#f60"))
    assert_items_almost_equal((1.0, 0.4, 0.0), grapefruit.Color.HtmlToRgb("f60"))
    assert_items_almost_equal((1.000000, 0.980392, 0.803922), grapefruit.Color.HtmlToRgb("lemonchiffon"))

  def test_RgbPil(self):
    assert_almost_equal(0x0080ff, grapefruit.Color.RgbToPil(1, 0.5, 0))
    assert_items_almost_equal((1.0, 0.5020, 0), grapefruit.Color.PilToRgb(0x0080ff))

  def test_WebSafeComponent(self):
    assert_equal(0.2, grapefruit.Color._WebSafeComponent(0.2))
    assert_equal(0.2, grapefruit.Color._WebSafeComponent(0.25))
    assert_equal(0.4, grapefruit.Color._WebSafeComponent(0.3))
    assert_equal(0.4, grapefruit.Color._WebSafeComponent(0.25, True))
    assert_equal(0.2, grapefruit.Color._WebSafeComponent(0.2, True))
    assert_equal(0.2, grapefruit.Color._WebSafeComponent(0.3, True))

  def test_RgbToWebSafe(self):
    assert_equal((1.0, 0.6, 0.0), grapefruit.Color.RgbToWebSafe(1, 0.55, 0.0))
    assert_equal((1.0, 0.4, 0.0), grapefruit.Color.RgbToWebSafe(1, 0.55, 0.0, True))
    assert_equal((1.0, 0.4, 0.0), grapefruit.Color.RgbToWebSafe(1, 0.5, 0.0, True))

  def test_RgbToGreyscale(self):
    assert_equal((0.6, 0.6, 0.6), grapefruit.Color.RgbToGreyscale(1, 0.8, 0))


class TestNewFrom():
  def test_NewFromRgb(self):
    c = grapefruit.Color.NewFromRgb(1.0, 0.5, 0.0)
    assert_equal(c, (1.0, 0.5, 0.0, 1.0))
    c = grapefruit.Color.NewFromRgb(1.0, 0.5, 0.0, 0.5)
    assert_equal(c, (1.0, 0.5, 0.0, 0.5))

  def test_NewFromHsl(self):
    c = grapefruit.Color.NewFromHsl(30, 1, 0.5)
    assert_equal(c, (1.0, 0.5, 0.0, 1.0))
    c = grapefruit.Color.NewFromHsl(30, 1, 0.5, 0.5)
    assert_equal(c, (1.0, 0.5, 0.0, 0.5))

  def test_NewFromHsv(self):
    c = grapefruit.Color.NewFromHsv(30, 1, 1)
    assert_equal(c, (1.0, 0.5, 0.0, 1.0))
    c = grapefruit.Color.NewFromHsv(30, 1, 1, 0.5)
    assert_equal(c, (1.0, 0.5, 0.0, 0.5))

  def test_NewFromYiq(self):
    c = grapefruit.Color.NewFromYiq(0.5923, 0.4589, -0.0499818)
    assert_items_almost_equal(c, (1, 0.5, 0, 1))
    c = grapefruit.Color.NewFromYiq(0.5923, 0.4589,-0.05, 0.5)
    assert_items_almost_equal(c, (1, 0.5, 0, 0.5))

  def test_NewFromYuv(self):
    c = grapefruit.Color.NewFromYuv(0.5925, -0.2916, 0.3575)
    assert_items_almost_equal(c, (1, 0.5, 0, 1))
    c = grapefruit.Color.NewFromYuv(0.5925, -0.2916, 0.3575, 0.5)
    assert_items_almost_equal(c, (1, 0.5, 0, 0.5))

  def test_NewFromXyz(self):
    c = grapefruit.Color.NewFromXyz(0.488941, 0.365682, 0.0448137)
    assert_items_almost_equal(c, (1, 0.5, 0, 1))
    c = grapefruit.Color.NewFromXyz(0.488941, 0.365682, 0.0448137, 0.5)
    assert_items_almost_equal(c, (1, 0.5, 0, 0.5))

  def test_NewFromLab(self):
    c = grapefruit.Color.NewFromLab(66.9518, 0.43084, 0.739692)
    assert_items_almost_equal(c, (1, 0.5, 0, 1))
    c = grapefruit.Color.NewFromLab(66.9518, 0.43084, 0.739692, wref=grapefruit.Color.WHITE_REFERENCE["std_D50"])
    assert_items_almost_equal(c, (1.0123754, 0.492012, -0.143110, 1))
    c = grapefruit.Color.NewFromLab(66.9518, 0.43084, 0.739692, 0.5)
    assert_items_almost_equal(c, (1, 0.5, 0, 0.5))
    c = grapefruit.Color.NewFromLab(66.9518, 0.43084, 0.739692, 0.5, grapefruit.Color.WHITE_REFERENCE["std_D50"])
    assert_items_almost_equal(c, (1.0123754, 0.492012, -0.143110, 0.5))

  def test_NewFromLabInteger(self):
      # Allow specifying lightness as an integer.
      lab = (60, 0.3, 0.3)
      c = grapefruit.Color.NewFromLab(*lab)
      assert_items_almost_equal(c.lab, lab)
      assert_true(c.isLegal)

  def test_NewFromCmy(self):
    c = grapefruit.Color.NewFromCmy(0, 0.5, 1)
    assert_equal(c, (1, 0.5, 0, 1.0))
    c = grapefruit.Color.NewFromCmy(0, 0.5, 1, 0.5)
    assert_equal(c, (1, 0.5, 0, 0.5))

  def test_NewFromCmyk(self):
    c = grapefruit.Color.NewFromCmyk(1, 0.32, 0, 0.5)
    assert_items_almost_equal(c, (0, 0.34, 0.5, 1))
    c = grapefruit.Color.NewFromCmyk(1, 0.32, 0, 0.5, 0.5)
    assert_items_almost_equal(c, (0, 0.34, 0.5, 0.5))

  def test_NewFromHtml(self):
    c = grapefruit.Color.NewFromHtml("#ff8000")
    assert_items_almost_equal(c, (1, 0.5020, 0, 1))
    c = grapefruit.Color.NewFromHtml("ff8000")
    assert_items_almost_equal(c, (1, 0.5020, 0, 1))
    c = grapefruit.Color.NewFromHtml("#f60")
    assert_items_almost_equal(c, (1, 0.4, 0, 1))
    c = grapefruit.Color.NewFromHtml("f60")
    assert_items_almost_equal(c, (1, 0.4, 0, 1))
    c = grapefruit.Color.NewFromHtml("lemonchiffon")
    assert_items_almost_equal(c, (1, 0.9804, 0.8039, 1))
    c = grapefruit.Color.NewFromHtml("#ff8000", 0.5)
    assert_items_almost_equal(c, (1, 0.5020, 0, 0.5))

  def test_NewFromPil(self):
    c = grapefruit.Color.NewFromPil(0x0080ff)
    assert_items_almost_equal(c, (1, 0.5020, 0, 1))
    c = grapefruit.Color.NewFromPil(0x0080ff, 0.5)
    assert_items_almost_equal(c, (1, 0.5020, 0, 0.5))


class TestColor():
  @classmethod
  def setup_class(self):
    self.rgbCol = grapefruit.Color.NewFromRgb(1.0, 0.5, 0.0)
    self.hslCol = grapefruit.Color.NewFromHsl(30, 1, 0.5)
    self.hslCol2 = grapefruit.Color.NewFromHsl(30, 0.5, 0.5)

  def test_Init(self):
    assert_equal(grapefruit.Color((1.0, 0.5, 0.0)), (1.0, 0.5, 0.0, 1.0))
    assert_equal(grapefruit.Color((1.0, 0.5, 0.0), mode='rgb'), (1.0, 0.5, 0.0, 1.0))
    assert_equal(grapefruit.Color((30, 1, 0.5), mode='hsl'), (1.0, 0.5, 0.0, 1.0))

    assert_raises(ValueError, grapefruit.Color, (30, 1, 0.5), 'hsv')

  def test_Eq(self):
    assert_equal(self.rgbCol, self.hslCol)
    assert_equal(self.rgbCol, (1.0, 0.5, 0.0, 1.0))
    assert_equal(self.rgbCol, [1.0, 0.5, 0.0, 1.0])
    assert_equal([1.0, 0.5, 0.0, 1.0], self.rgbCol)
    assert_not_equal(self.rgbCol, '(1.0, 0.5, 0.0, 1.0)')

  def test_Repr(self):
    assert_equal(repr(self.rgbCol), '(1.0, 0.5, 0.0, 1.0)')
    assert_equal(repr(self.hslCol), '(1.0, 0.5, 0.0, 1.0)')

  def test_Str(self):
    assert_equal(str(self.rgbCol), '(1, 0.5, 0, 1)')
    assert_equal(str(self.hslCol), '(1, 0.5, 0, 1)')

  def test_Iter(self):
    assert_equal([1, 0.5, 0, 1], list(iter(self.rgbCol)))

  def test_Properties(self):
    assert_equal(self.rgbCol.alpha, 1.0)
    assert_equal(self.rgbCol.whiteRef, grapefruit.Color.WHITE_REFERENCE['std_D65'])
    assert_equal(self.rgbCol.rgb, (1, 0.5, 0))
    assert_equal(self.hslCol.hue, 30)
    assert_equal(self.rgbCol.hsl, (30, 1, 0.5))
    assert_equal(self.rgbCol.hsv, (30, 1, 1))
    assert_items_almost_equal(self.rgbCol.yiq, (0.5923, 0.4589, -0.05))
    assert_items_almost_equal(self.rgbCol.yuv, (0.5925, -0.2916, 0.3575))
    assert_items_almost_equal(self.rgbCol.xyz, (0.4890, 0.3657, 0.04485))
    assert_items_almost_equal(self.rgbCol.lab, (66.9518, 0.4308, 0.7397))
    assert_equal(self.rgbCol.cmy, (0, 0.5, 1))
    assert_equal(self.rgbCol.cmyk, (0, 0.5, 1, 0))
    assert_equal(self.rgbCol.intTuple, (255, 128, 0))
    assert_equal(self.rgbCol.html, '#ff8000')
    assert_equal(self.rgbCol.pil, 0x0080ff)
    assert_equal(self.rgbCol.webSafe, (1, 0.6, 0))
    assert_equal(self.rgbCol.greyscale, (0.5, 0.5, 0.5))

    c = grapefruit.Color.NewFromRgb(1, 0.5, 0, wref=grapefruit.Color.WHITE_REFERENCE['std_D50'])
    assert_items_almost_equal(c.lab, (66.9518, 0.4117, 0.6728))

  def test_ColorWitgAlpha(self):
    assert_equal(self.rgbCol.ColorWithAlpha(0.5), (1, 0.5, 0, 0.5))

  def test_ColorWithWhiteRef(self):
    assert_equal(self.hslCol.ColorWithWhiteRef((0.1, 0.2, 0.3)).whiteRef, (0.1, 0.2, 0.3))

  def test_ColorWithHue(self):
    assert_equal(self.hslCol.ColorWithHue(60), (1.0, 1.0, 0.0, 1.0))
    assert_equal(self.hslCol.ColorWithHue(60).hsl, (60, 1, 0.5))

  def test_ColorWithSaturation(self):
    assert_equal(self.hslCol.ColorWithSaturation(0.5), (0.75, 0.5, 0.25, 1.0))
    assert_equal(self.hslCol.ColorWithSaturation(0.5).hsl, (30, 0.5, 0.5))

  def test_ColorWithLightness(self):
    assert_equal(self.hslCol.ColorWithLightness(1), (1.0, 1.0, 1.0, 1.0))
    assert_equal(self.hslCol.ColorWithLightness(1).hsl, (30, 1.0, 1.0))

  def test_DarkerColor(self):
    assert_items_almost_equal(self.hslCol.DarkerColor(0.2), (0.6, 0.3, 0.0, 1.0))
    assert_items_almost_equal(self.hslCol.DarkerColor(0.2).hsl, (30, 1, 0.3))

  def test_LighterColor(self):
    assert_items_almost_equal(self.hslCol.LighterColor(0.2), (1.0, 0.7, 0.4, 1.0))
    assert_items_almost_equal(self.hslCol.LighterColor(0.2).hsl, (30, 1, 0.7))

  def test_Saturate(self):
    assert_items_almost_equal(self.hslCol2.Saturate(0.25), (0.875, 0.5, 0.125, 1.0))
    assert_items_almost_equal(self.hslCol2.Saturate(0.25).hsl, (30, 0.75, 0.5))

  def test_Desaturate(self):
    assert_items_almost_equal(self.hslCol2.Desaturate(0.25), (0.625, 0.5, 0.375, 1.0))
    assert_items_almost_equal(self.hslCol2.Desaturate(0.25).hsl, (30, 0.25, 0.5))

  def test_WebSafeDither(self):
    dithered = (
      (1.0, 0.6, 0.0, 1.0),
      (1.0, 0.4, 0.0, 1.0))
    assert_equal(self.rgbCol.WebSafeDither(), dithered)

  def test_Gradient(self):
    gradient = [
      (0.75, 0.25, 0.0, 1.0),
      (0.5, 0.5, 0.0, 1.0),
      (0.25, 0.75, 0.0, 1.0)]
    c1 = grapefruit.Color.NewFromRgb(1.0, 0.0, 0.0)
    c2 = grapefruit.Color.NewFromRgb(0.0, 1.0, 0.0)
    assert_equal(gradient, c1.Gradient(c2, 3))

  def test_ComplementaryColor(self):
    assert_equal(self.hslCol.ComplementaryColor(mode='rgb').hsl, (210, 1, 0.5))

  def test_MonochromeScheme(self):
    monochrome = (
      (0.94, 0.8, 0.66, 1.0), # hsl(30, 0.7, 0.8)
      (0.6, 0.3, 0.0, 1.0),   # hsl(30, 1, 0.3)
      (0.88, 0.6, 0.32, 1.0), # hsl(30, 0.7, 0.6)
      (1.0, 0.8, 0.6, 1.0))   # hsl(30, 1, 0.8)
    scheme = self.rgbCol.MonochromeScheme()
    for i in range(len(monochrome)):
      assert_items_almost_equal(scheme[i], monochrome[i])

  def test_TriadicScheme(self):
    triad = (
      (0.0, 1.0, 0.5, 1.0),
      (0.5, 0.0, 1.0, 1.0))
    assert_equal(self.rgbCol.TriadicScheme(mode='rgb'), triad)

  def test_TetradicScheme(self):
    tetrad = (
      (0.5, 1.0, 0.0, 1.0),
      (0.0, 0.5, 1.0, 1.0),
      (0.5, 0.0, 1.0, 1.0))
    assert_equal(self.rgbCol.TetradicScheme(mode='rgb'), tetrad)

  def test_AnalogousScheme(self):
    scheme = (
      (1.0, 0.0, 0.0, 1.0),
      (1.0, 1.0, 0.0, 1.0))
    assert_equal(self.rgbCol.AnalogousScheme(mode='rgb'), scheme)

  def test_AlphaBlend(self):
    c1 = grapefruit.Color.NewFromRgb(1, 0.5, 0, alpha = 0.2)
    c2 = grapefruit.Color.NewFromRgb(1, 1, 1, alpha = 0.8)
    assert_items_almost_equal(c1.AlphaBlend(c2), (1, 0.875, 0.75, 0.84))

  def test_Blend(self):
    c1 = grapefruit.Color.NewFromRgb(1, 0.5, 0, alpha = 0.2)
    c2 = grapefruit.Color.NewFromRgb(1, 1, 1, alpha = 0.6)
    assert_equal(c1.Blend(c2), (1, 0.75, 0.5, 0.4))

  def test_NearestLegal(self):
      c = grapefruit.Color.NewFromRgb(1.1, -0.1, 0.5, alpha=1.1)
      assert_false(c.isLegal)
      assert_items_almost_equal(c.nearestLegal.rgb, (1.0, 0.0, 0.5))
      assert_almost_equal(c.nearestLegal.alpha, 1.0)
