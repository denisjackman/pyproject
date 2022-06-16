#!/usr/bin/env python
"""
test_bed.py
    this is a test bed for trying pytest out prior to folding it
    in elsewhere.

References:
            https://realpython.com/pytest-python-testing/
            https://www.tutorialspoint.com/pytest/index.htm
"""

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 0.0 $"
__date__ = "$Date: 2022/06/16 15:17:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"
import math


def test_sqrt():
    '''
        a test function
    '''
    num = 25
    assert math.sqrt(num) == 5


def testsquare():
    '''
        another test function
    '''
    num = 7
    assert num * num == 40


def tesequality():
    '''
        one last test function
    '''
    assert 10 == 11
