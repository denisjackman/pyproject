#!/usr/bin/env python
"""
test_compare.py
    this is a test bed for trying pytest out prior to folding it
    in elsewhere.

References:
            https://realpython.com/pytest-python-testing/
            https://www.tutorialspoint.com/pytest/index.htm
"""

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 0.0 $"
__date__ = "$Date: 2022/06/17 06:17:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"


def test_greater():
    '''
        a test function
    '''
    num = 100
    assert num > 100


def test_greater_equal():
    '''
        a test function
    '''
    num = 100
    assert num >= 100


def test_less():
    '''
        a test function
    '''
    num = 100
    assert num < 200
