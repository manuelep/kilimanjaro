# -*- coding: utf-8 -*-

from unittest import TestCase

from kilimanjaro.color.loader import colors
from kilimanjaro.color.feader import colorScaleFader, parse

class FaderTestCase(TestCase):

    # def test_with_colortona(self):
    #
    #     myscale = colors["colortona"]["Hold"]["5"]
    #     res = colorScaleFader(.25437, myscale)
    #
    #     self.assertIsInstance(res, str)

    def test_with_brewer(self):

        myscale = list(map(parse, colors["colorbrewer"]["Spectral"]["5"]))
        res = colorScaleFader(.25437, myscale)

        self.assertIsInstance(res, str)
