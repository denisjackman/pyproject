#!/usr/bin/python
"""
pyproject.py

This program is a catch all for the pyproject project

"""

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 0.00 $"
__date__ = "$Date: 2022/06/28 00:00:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"
from jackmanimation.jackmanimation import credscheck

def main():
    """ This is the main routine for the program """
    print("Starting the sequence:")
    credid = credscheck('secrets/credentials.json')
    print("finishing up and closing down:")


if __name__ == '__main__':
    main()
