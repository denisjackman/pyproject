"""
main.py

This program is a template for python programs
All this stuff at the top of the script is just optional metadata;

"""
import sys
import os

# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.gameitems.gamefunctions import credscheck

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 1.10 $"
__date__ = "$Date: 2022/05/31 00:31:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"


def main():
    """ This is the main routine for the program """
    print("Starting the sequence:")
    credid = credscheck('Z:/pyproject/secrets/secrets.json')
    print("finishing up and closing down:")
    print(credid)


if __name__ == '__main__':
    main()
