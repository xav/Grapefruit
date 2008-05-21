#!/usr/bin/python
# -*- coding: utf-8 -*-#

# 
# Copyright (c) 2008, Xavier Basty
# All rights reserved.
# 

'''Unit tests for the grapefruit.py module.'''

__author__ = 'xbasty@gmail.com'
__version__ = '0.1-devel'

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
                    raise self.failureException, (msg or 'The difference between %r and %r is more than %f.' % (f, s, diff))
        elif abs(second-first) > diff:
            raise self.failureException, (msg or 'The difference between %r and %r is more than %f.' % (first, second, diff))
    assertNear = failUnlessNear

class ConversionTest(GrapeFruitTestCase):
    '''Test the static color conversion methods.'''

    def testRgbHsl(self):
        self.assertEqual((30.0, 1.0, 0.5), grapefruit.Color.RgbToHsl(1, 0.5, 0))
        self.assertEqual((1, 0.5, 0), grapefruit.Color.HslToRgb(30.0, 1.0, 0.5))
    
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

    def testInit(self):
        pass
    
    def testEq(self):
        pass
        
    def testRepr(self):
        pass
    
    def testStr(self):
        pass
    
    def testIter(self):
        pass
    
    def testGetters(self):
        pass
        
    def testProperties(self):
        pass
    
    def testColorWitgAlpha(self):
        pass
    
    def testColorWithWhiteRef(self):
        pass
    
    def testColorWithHue(self):
        pass
    
    def testColorWithSaturation(self):
        pass
    
    def testColorWithLightness(self):
        pass
    
    def testDarkerColor(self):
        pass
    
    def testLighterColor(self):
        pass
    
    def testComplementaryColor(self):
        pass
    
    def testWebSafeDither(self):
        pass
    
    def testTriadicScheme(self):
        pass
    
    def testTetradicScheme(self):
        pass
    
    def testAnalogousScheme(self):
        pass
    
    def testAlphaBlend(self):
        pass
    
    def testBlend(self):
        pass
    

if __name__ == '__main__':
    unittest.main()
    pass
