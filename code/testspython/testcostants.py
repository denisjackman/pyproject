#!/usr/bin/env python
"""
testconstants.py
    this is a scratch utility for trying stuff out prior to folding it
    in elsewhere.
"""

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 0.0 $"
__date__ = "$Date: 2022/06/14 16:38:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"
from djgamemodule import constants as cn

def main():
    '''
        main function
    '''
    for day in cn.DAYS:
        print(f"Today is {day}")

    for month in cn.MONTHS:
        print(f"This month is {month}")

    for season in cn.SEASONS:
        print(f"This season is {season}")

    for letter, phonetic in cn.PHONETIC_ALPHABET.items():
        print(phonetic)

if __name__ == '__main__':
    main()
