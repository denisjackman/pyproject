#!/usr/bin/env python
"""
testcolour.py
    this is a scratch utility for trying stuff out prior to folding it
    in elsewhere.
"""

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 0.0 $"
__date__ = "$Date: 2022/06/14 16:38:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"
from djgamemodule import colours

print(colours.WHITE)
for color, rgbcode in colours.COLOURS_RGB_LIST.items():
    print(color, rgbcode)
