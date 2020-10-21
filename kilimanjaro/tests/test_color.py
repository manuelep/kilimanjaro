# -*- coding: utf-8 -*-

from unittest import TestCase

from kilimanjaro.color.loader import colors
from kilimanjaro.color.feader import colorScaleFader, parse

class FaderTestCase(TestCase):

    def test_with_colortona(self):

        myscale = colors["colortona"]["Hold"]["5"]
        for value in [.12, .93]:
            res = colorScaleFader(value, myscale)
            self.assertIsInstance(res, str)

    def test_with_colorbrewer(self):

        myscale = list(map(parse, colors["colorbrewer"]["Spectral"]["5"]))
        for value in [.12, .93]:
            res = colorScaleFader(value, myscale)
            self.assertIsInstance(res, str)
