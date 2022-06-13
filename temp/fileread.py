#!/usr/bin/python
"""
fileread.py


"""
__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 1.00 $"
__date__ = "$Date: 2022/06/11 08:31:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"
import sys


def fileread(filename):
    """ this is a file read function """
    result = []
    with open(filename, 'r',  encoding="utf8") as inputfile:
        for item in inputfile:
            result.append(item)
    inputfile.close()
    return result


print(len(fileread('example.txt')))
print(sys.path)
