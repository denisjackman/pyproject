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
import os
import sys
# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.DndProject.dndinsult import shakespearean_insult_generator
from jackmanimation.DndProject.dndinsult import dwarven_insult_generator


def main():
    '''
        main function
    '''
    print("Insult generator test")
    loop = 0
    while loop < 101:
        print(f" {str(loop)} : {shakespearean_insult_generator()}")
        print(f" {str(loop)} : {dwarven_insult_generator()}")
        loop = loop + 1


if __name__ == '__main__':
    main()
