'''
swisstool.py

This is a os utility tool

'''
import os
import sys
# pylint: disable=C0413
sys.path.append(os.path.realpath('..\\..'))
from jackmanimation.utilities.fileutility import walk_through
from jackmanimation.utilities.fileutility import getargs

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 0.01 $"
__date__ = "$Date: 2022/07/28 01:17:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"


def swissmain():
    '''
        this is the main function
    '''
    mainargs = getargs()
    filelist = walk_through(mainargs)
    print(mainargs)
    print(filelist)


if __name__ == '__main__':
    swissmain()
