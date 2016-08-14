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

"""Unit tests for the grapefruit module."""

import grapefruit
from nose.tools import *

def assert_items_almost_equal(first, second, places=3, msg=None, delta=None):
  """assert_almost_equal for iterables"""
  assert_equal(len(first), len(second))

  for f, s in zip(first, second):
    assert_almost_equal(f, s, places, msg, delta)

class TestConversion():
  """Test the static color conversion methods."""

  def test_rgb_to_hsl(self):
    assert_items_almost_equal((30.0, 1.0, 0.5), grapefruit.rgb_to_hsl(1, 0.5, 0))
    assert_items_almost_equal((20.0, 1.0, 0.625), grapefruit.rgb_to_hsl(1, 0.5, 0.25)) #ff8040
    assert_items_almost_equal((40.0, 1.0, 0.375), grapefruit.rgb_to_hsl(0.75, 0.5, 0)) #bf8000

  def test_hsl_to_rgb(self):
    assert_items_almost_equal((1, 0.5, 0), grapefruit.hsl_to_rgb(30.0, 1.0, 0.5))
    assert_items_almost_equal((1, 0.5, 0.25), grapefruit.hsl_to_rgb(20.0, 1.0, 0.625))
    assert_items_almost_equal((0.75, 0.5, 0), grapefruit.hsl_to_rgb(40.0, 1.0, 0.375))

  def test_rgb_to_hsv(self):
    assert_equal((30.0, 1.0, 1.0), grapefruit.rgb_to_hsv(1, 0.5, 0))
    assert_equal((1, 0.5, 0), grapefruit.hsv_to_rgb(30.0, 1.0, 1.0))

  def test_rgb_to_yiq(self):
    assert_items_almost_equal((0.5923, 0.4589, -0.05), grapefruit.rgb_to_yiq(1, 0.5, 0))
    assert_items_almost_equal((1, 0.5, 0), grapefruit.yiq_to_rgb(0.5923, 0.4589, -0.05))

  def test_rgb_to_yuv(self):
    assert_items_almost_equal((0.5925, -0.2916, 0.3575), grapefruit.rgb_to_yuv(1, 0.5, 0))
    assert_items_almost_equal((1, 0.5, 0), grapefruit.yuv_to_rgb(0.5925, -0.2916, 0.3575))

  def test_rgb_to_xyz(self):
    assert_items_almost_equal((0.4890, 0.3657, 0.04485), grapefruit.rgb_to_xyz(1, 0.5, 0))
    assert_items_almost_equal((1, 0.5, 0), grapefruit.xyz_to_rgb(0.488941, 0.365682, 0.0448137))

  def test_xyz_tolab(self):
    assert_items_almost_equal((66.9518, 0.4308, 0.7397), grapefruit.xyz_to_lab(0.488941, 0.365682, 0.0448137))
    assert_items_almost_equal((66.9518, 0.4117, 0.6728), grapefruit.xyz_to_lab(0.488941, 0.365682, 0.0448137, grapefruit.WHITE_REFERENCE["std_D50"]))

  def test_xyz_to_lab(self):
    assert_items_almost_equal((0.4890, 0.3657, 0.0449), grapefruit.lab_to_xyz(66.9518, 0.4308, 0.7397))
    assert_items_almost_equal((0.4890, 0.3657, 0.0449), grapefruit.lab_to_xyz(66.9518, 0.4117, 0.6728, grapefruit.WHITE_REFERENCE["std_D50"]))

  def test_cmyk_to_cmy(self):
    assert_items_almost_equal((1, 0.32, 0, 0.5), grapefruit.cmy_to_cmyk(1.0, 0.66, 0.5))
    assert_items_almost_equal((1.0, 0.66, 0.5), grapefruit.cmyk_to_cmy(1, 0.32, 0, 0.5))

  def test_rgb_to_cmy(self):
    assert_equal((0, 0.5, 1), grapefruit.rgb_to_cmy(1, 0.5, 0))
    assert_equal((1, 0.5, 0), grapefruit.cmy_to_rgb(0, 0.5, 1))

  def test_rgb_to_html(self):
    assert_equal("#ff8000", grapefruit.rgb_to_html(1, 0.5, 0))
    assert_items_almost_equal((1.0, 0.5020, 0.0), grapefruit.html_to_rgb("#ff8000"))
    assert_items_almost_equal((1.0, 0.5020, 0.0), grapefruit.html_to_rgb("ff8000"))
    assert_items_almost_equal((1.0, 0.4, 0.0), grapefruit.html_to_rgb("#f60"))
    assert_items_almost_equal((1.0, 0.4, 0.0), grapefruit.html_to_rgb("f60"))
    assert_items_almost_equal((1.000000, 0.980392, 0.803922), grapefruit.html_to_rgb("lemonchiffon"))

  def test_rgb_to_pil(self):
    assert_almost_equal(0x0080ff, grapefruit.rgb_to_pil(1, 0.5, 0))
    assert_items_almost_equal((1.0, 0.5020, 0), grapefruit.pil_to_rgb(0x0080ff))

  def test_websafe_component(self):
    assert_equal(0.2, grapefruit._websafe_component(0.2))
    assert_equal(0.2, grapefruit._websafe_component(0.25))
    assert_equal(0.4, grapefruit._websafe_component(0.3))
    assert_equal(0.4, grapefruit._websafe_component(0.25, True))
    assert_equal(0.2, grapefruit._websafe_component(0.2, True))
    assert_equal(0.2, grapefruit._websafe_component(0.3, True))

  def test_rgb_to_to_websafe(self):
    assert_equal((1.0, 0.6, 0.0), grapefruit.rgb_to_websafe(1, 0.55, 0.0))
    assert_equal((1.0, 0.4, 0.0), grapefruit.rgb_to_websafe(1, 0.55, 0.0, True))
    assert_equal((1.0, 0.4, 0.0), grapefruit.rgb_to_websafe(1, 0.5, 0.0, True))

  def test_rgb_to_greyscale(self):
    assert_equal((0.6, 0.6, 0.6), grapefruit.rgb_to_greyscale(1, 0.8, 0))


class TestNewFrom():
  def test_from_rgb(self):
    c = grapefruit.Color.from_rgb(1.0, 0.5, 0.0)
    assert_equal(c, (1.0, 0.5, 0.0, 1.0))
    c = grapefruit.Color.from_rgb(1.0, 0.5, 0.0, 0.5)
    assert_equal(c, (1.0, 0.5, 0.0, 0.5))

  def test_from_hsl(self):
    c = grapefruit.Color.from_hsl(30, 1, 0.5)
    assert_equal(c, (1.0, 0.5, 0.0, 1.0))
    c = grapefruit.Color.from_hsl(30, 1, 0.5, 0.5)
    assert_equal(c, (1.0, 0.5, 0.0, 0.5))

  def test_from_hsv(self):
    c = grapefruit.Color.from_hsv(30, 1, 1)
    assert_equal(c, (1.0, 0.5, 0.0, 1.0))
    c = grapefruit.Color.from_hsv(30, 1, 1, 0.5)
    assert_equal(c, (1.0, 0.5, 0.0, 0.5))

  def test_from_yiq(self):
    c = grapefruit.Color.from_yiq(0.5923, 0.4589, -0.0499818)
    assert_items_almost_equal(c, (1, 0.5, 0, 1))
    c = grapefruit.Color.from_yiq(0.5923, 0.4589,-0.05, 0.5)
    assert_items_almost_equal(c, (1, 0.5, 0, 0.5))

  def test_from_yuv(self):
    c = grapefruit.Color.from_yuv(0.5925, -0.2916, 0.3575)
    assert_items_almost_equal(c, (1, 0.5, 0, 1))
    c = grapefruit.Color.from_yuv(0.5925, -0.2916, 0.3575, 0.5)
    assert_items_almost_equal(c, (1, 0.5, 0, 0.5))

  def test_from_xyz(self):
    c = grapefruit.Color.from_xyz(0.488941, 0.365682, 0.0448137)
    assert_items_almost_equal(c, (1, 0.5, 0, 1))
    c = grapefruit.Color.from_xyz(0.488941, 0.365682, 0.0448137, 0.5)
    assert_items_almost_equal(c, (1, 0.5, 0, 0.5))

  def test_from_lab(self):
    c = grapefruit.Color.from_lab(66.9518, 0.43084, 0.739692)
    assert_items_almost_equal(c, (1, 0.5, 0, 1))
    c = grapefruit.Color.from_lab(66.9518, 0.43084, 0.739692, wref=grapefruit.WHITE_REFERENCE["std_D50"])
    assert_items_almost_equal(c, (1.0123754, 0.492012, -0.143110, 1))
    c = grapefruit.Color.from_lab(66.9518, 0.43084, 0.739692, 0.5)
    assert_items_almost_equal(c, (1, 0.5, 0, 0.5))
    c = grapefruit.Color.from_lab(66.9518, 0.43084, 0.739692, 0.5, grapefruit.WHITE_REFERENCE["std_D50"])
    assert_items_almost_equal(c, (1.0123754, 0.492012, -0.143110, 0.5))

  def test_from_labInteger(self):
      # Allow specifying lightness as an integer.
      lab = (60, 0.3, 0.3)
      c = grapefruit.Color.from_lab(*lab)
      assert_items_almost_equal(c.lab, lab)
      assert_true(c.is_legal)

  def test_from_cmy(self):
    c = grapefruit.Color.from_cmy(0, 0.5, 1)
    assert_equal(c, (1, 0.5, 0, 1.0))
    c = grapefruit.Color.from_cmy(0, 0.5, 1, 0.5)
    assert_equal(c, (1, 0.5, 0, 0.5))

  def test_from_cmyk(self):
    c = grapefruit.Color.from_cmyk(1, 0.32, 0, 0.5)
    assert_items_almost_equal(c, (0, 0.34, 0.5, 1))
    c = grapefruit.Color.from_cmyk(1, 0.32, 0, 0.5, 0.5)
    assert_items_almost_equal(c, (0, 0.34, 0.5, 0.5))

  def test_from_html(self):
    c = grapefruit.Color.from_html("#ff8000")
    assert_items_almost_equal(c, (1, 0.5020, 0, 1))
    c = grapefruit.Color.from_html("ff8000")
    assert_items_almost_equal(c, (1, 0.5020, 0, 1))
    c = grapefruit.Color.from_html("#f60")
    assert_items_almost_equal(c, (1, 0.4, 0, 1))
    c = grapefruit.Color.from_html("f60")
    assert_items_almost_equal(c, (1, 0.4, 0, 1))
    c = grapefruit.Color.from_html("lemonchiffon")
    assert_items_almost_equal(c, (1, 0.9804, 0.8039, 1))
    c = grapefruit.Color.from_html("#ff8000", 0.5)
    assert_items_almost_equal(c, (1, 0.5020, 0, 0.5))

  def test_from_pil(self):
    c = grapefruit.Color.from_pil(0x0080ff)
    assert_items_almost_equal(c, (1, 0.5020, 0, 1))
    c = grapefruit.Color.from_pil(0x0080ff, 0.5)
    assert_items_almost_equal(c, (1, 0.5020, 0, 0.5))


class TestColor():
  @classmethod
  def setup_class(self):
    self.rgb_col = grapefruit.Color.from_rgb(1.0, 0.5, 0.0)
    self.hsl_col = grapefruit.Color.from_hsl(30, 1, 0.5)
    self.hsl_col2 = grapefruit.Color.from_hsl(30, 0.5, 0.5)

  def test_Init(self):
    assert_equal(grapefruit.Color((1.0, 0.5, 0.0)), (1.0, 0.5, 0.0, 1.0))
    assert_equal(grapefruit.Color((1.0, 0.5, 0.0), mode='rgb'), (1.0, 0.5, 0.0, 1.0))
    assert_equal(grapefruit.Color((30, 1, 0.5), mode='hsl'), (1.0, 0.5, 0.0, 1.0))

    assert_raises(ValueError, grapefruit.Color, (30, 1, 0.5), 'hsv')

  def test_Eq(self):
    assert_equal(self.rgb_col, self.hsl_col)
    assert_equal(self.rgb_col, (1.0, 0.5, 0.0, 1.0))
    assert_equal(self.rgb_col, [1.0, 0.5, 0.0, 1.0])
    assert_equal([1.0, 0.5, 0.0, 1.0], self.rgb_col)
    assert_not_equal(self.rgb_col, '(1.0, 0.5, 0.0, 1.0)')

  def test_Repr(self):
    assert_equal(repr(self.rgb_col), 'Color(1.0, 0.5, 0.0, 1.0)')
    assert_equal(repr(self.hsl_col), 'Color(1.0, 0.5, 0.0, 1.0)')

  def test_Str(self):
    assert_equal(str(self.rgb_col), '(1.0, 0.5, 0.0, 1.0)')
    assert_equal(str(self.hsl_col), '(1.0, 0.5, 0.0, 1.0)')

  def test_Iter(self):
    assert_equal([1, 0.5, 0, 1], list(iter(self.rgb_col)))

  def test_Properties(self):
    assert_equal(self.rgb_col.alpha, 1.0)
    assert_equal(self.rgb_col.white_ref, grapefruit.WHITE_REFERENCE['std_D65'])
    assert_equal(self.rgb_col.rgb, (1, 0.5, 0))
    assert_equal(self.hsl_col.hsl_hue, 30)
    assert_equal(self.rgb_col.hsl, (30, 1, 0.5))
    assert_equal(self.rgb_col.hsv, (30, 1, 1))
    assert_items_almost_equal(self.rgb_col.yiq, (0.5923, 0.4589, -0.05))
    assert_items_almost_equal(self.rgb_col.yuv, (0.5925, -0.2916, 0.3575))
    assert_items_almost_equal(self.rgb_col.xyz, (0.4890, 0.3657, 0.04485))
    assert_items_almost_equal(self.rgb_col.lab, (66.9518, 0.4308, 0.7397))
    assert_equal(self.rgb_col.cmy, (0, 0.5, 1))
    assert_equal(self.rgb_col.cmyk, (0, 0.5, 1, 0))
    assert_equal(self.rgb_col.ints, (255, 128, 0))
    assert_equal(self.rgb_col.html, '#ff8000')
    assert_equal(self.rgb_col.pil, 0x0080ff)
    assert_equal(self.rgb_col.websafe, (1, 0.6, 0))
    assert_equal(self.rgb_col.greyscale, (0.5, 0.5, 0.5))

    c = grapefruit.Color.from_rgb(1, 0.5, 0, wref=grapefruit.WHITE_REFERENCE['std_D50'])
    assert_items_almost_equal(c.lab, (66.9518, 0.4117, 0.6728))

  def test_with_alpha(self):
    assert_equal(self.rgb_col.with_alpha(0.5), (1, 0.5, 0, 0.5))

  def test_with_white_ref(self):
    assert_equal(self.hsl_col.with_white_ref((0.1, 0.2, 0.3)).white_ref, (0.1, 0.2, 0.3))

  def test_with_hue(self):
    assert_equal(self.hsl_col.with_hue(60), (1.0, 1.0, 0.0, 1.0))
    assert_equal(self.hsl_col.with_hue(60).hsl, (60, 1, 0.5))

  def test_with_saturation(self):
    assert_equal(self.hsl_col.with_saturation(0.5), (0.75, 0.5, 0.25, 1.0))
    assert_equal(self.hsl_col.with_saturation(0.5).hsl, (30, 0.5, 0.5))

  def test_with_lightness(self):
    assert_equal(self.hsl_col.with_lightness(1), (1.0, 1.0, 1.0, 1.0))
    assert_equal(self.hsl_col.with_lightness(1).hsl, (30, 1.0, 1.0))

  def test_darker(self):
    assert_items_almost_equal(self.hsl_col.darker(0.2), (0.6, 0.3, 0.0, 1.0))
    assert_items_almost_equal(self.hsl_col.darker(0.2).hsl, (30, 1, 0.3))

  def test_lighter(self):
    assert_items_almost_equal(self.hsl_col.lighter(0.2), (1.0, 0.7, 0.4, 1.0))
    assert_items_almost_equal(self.hsl_col.lighter(0.2).hsl, (30, 1, 0.7))

  def test_saturate(self):
    assert_items_almost_equal(self.hsl_col2.saturate(0.25), (0.875, 0.5, 0.125, 1.0))
    assert_items_almost_equal(self.hsl_col2.saturate(0.25).hsl, (30, 0.75, 0.5))

  def test_desaturate(self):
    assert_items_almost_equal(self.hsl_col2.desaturate(0.25), (0.625, 0.5, 0.375, 1.0))
    assert_items_almost_equal(self.hsl_col2.desaturate(0.25).hsl, (30, 0.25, 0.5))

  def test_websafe_dither(self):
    dithered = (
      (1.0, 0.6, 0.0, 1.0),
      (1.0, 0.4, 0.0, 1.0))
    assert_equal(self.rgb_col.websafe_dither(), dithered)

  def test_make_gradient(self):
    gradient = [
      (0.75, 0.25, 0.0, 1.0),
      (0.5, 0.5, 0.0, 1.0),
      (0.25, 0.75, 0.0, 1.0)]
    c1 = grapefruit.Color.from_rgb(1.0, 0.0, 0.0)
    c2 = grapefruit.Color.from_rgb(0.0, 1.0, 0.0)
    assert_equal(gradient, c1.make_gradient(c2, 3))

  def test_complementary_color(self):
    assert_equal(self.hsl_col.complementary_color(mode='rgb').hsl, (210, 1, 0.5))

  def test_make_monochrome_scheme(self):
    monochrome = (
      (0.94, 0.8, 0.66, 1.0), # hsl(30, 0.7, 0.8)
      (0.6, 0.3, 0.0, 1.0),   # hsl(30, 1, 0.3)
      (0.88, 0.6, 0.32, 1.0), # hsl(30, 0.7, 0.6)
      (1.0, 0.8, 0.6, 1.0))   # hsl(30, 1, 0.8)
    scheme = self.rgb_col.make_monochrome_scheme()
    for i in range(len(monochrome)):
      assert_items_almost_equal(scheme[i], monochrome[i])

  def test_make_triadic_scheme(self):
    triad = (
      (0.0, 1.0, 0.5, 1.0),
      (0.5, 0.0, 1.0, 1.0))
    assert_equal(self.rgb_col.make_triadic_scheme(mode='rgb'), triad)

  def test_make_tetradic_scheme(self):
    tetrad = (
      (0.5, 1.0, 0.0, 1.0),
      (0.0, 0.5, 1.0, 1.0),
      (0.5, 0.0, 1.0, 1.0))
    assert_equal(self.rgb_col.make_tetradic_scheme(mode='rgb'), tetrad)

  def test_make_analogous_scheme(self):
    scheme = (
      (1.0, 0.0, 0.0, 1.0),
      (1.0, 1.0, 0.0, 1.0))
    assert_equal(self.rgb_col.make_analogous_scheme(mode='rgb'), scheme)

  def test_alpha_blend(self):
    c1 = grapefruit.Color.from_rgb(1, 0.5, 0, alpha = 0.2)
    c2 = grapefruit.Color.from_rgb(1, 1, 1, alpha = 0.8)
    assert_items_almost_equal(c1.alpha_blend(c2), (1, 0.875, 0.75, 0.84))

  def test_blend(self):
    c1 = grapefruit.Color.from_rgb(1, 0.5, 0, alpha = 0.2)
    c2 = grapefruit.Color.from_rgb(1, 1, 1, alpha = 0.6)
    assert_equal(c1.blend(c2), (1, 0.75, 0.5, 0.4))

  def test_nearest_legal(self):
      c = grapefruit.Color.from_rgb(1.1, -0.1, 0.5, alpha=1.1)
      assert_false(c.is_legal)
      assert_items_almost_equal(c.nearest_legal().rgb, (1.0, 0.0, 0.5))
      assert_almost_equal(c.nearest_legal().alpha, 1.0)
