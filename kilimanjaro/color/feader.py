# -*- coding: utf-8 -*-

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import re

def colorFader(c1,c2,mix=0):
    """ Courtesy of: https://www.xspdf.com/help/50784012.html
    Fade (linear interpolate) from color c1 (at mix=0) to c2 (mix=1)
    c1 @string : Hexadecimal color
    c2 @string : Hexadecimal color
    mix @float : A float value between 0 and 1

    returns @string:
        color code resulting from interpolation
    """

    c1=np.array(mpl.colors.to_rgb(c1))
    c2=np.array(mpl.colors.to_rgb(c2))
    return mpl.colors.to_hex((1-mix)*c1 + mix*c2)

def colorScaleFader(value, color_scale):
    """
    value @float : [0,1]
    color_scale @string[] :
    """

    unit = 1./len(color_scale)
    idx = int(value//unit)
    c1, c2 = color_scale[idx:idx+2]

    return colorFader(c1, c2, (value/unit)-idx)

def parse(value):
    red, green, blue = map(int, re.findall(r'\d+', value))
    return f"#{red:02x}{green:02x}{blue:02x}"
