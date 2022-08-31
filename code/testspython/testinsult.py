#!/usr/bin/env python
"""
scratch.py
    this is a scratch utility for trying stuff out prior to folding it
    in elsewhere.
"""

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 0.0 $"
__date__ = "$Date: 2022/06/14 16:38:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"
from djgamemodule import dice as dn


def main():
    '''
        main function
    '''
    print("Insult generator test")
    loop = 0
    while loop < 101:
        print(str(loop) + ": " + dn.insult_generator())
        loop = loop + 1


if __name__ == '__main__':
    main()
