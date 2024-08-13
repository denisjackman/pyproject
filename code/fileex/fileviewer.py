"""
fileviewer.py

Walk through a chosen directory. from the
designated top to the bottom looking for files .

"""
import os
import sys
# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.utilities.fileutility import walk_through
from jackmanimation.utilities.fileutility import getargs

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 1.0 $"
__date__ = "$Date: 2019/04/23 00:00:00 $"
__copyright__ = "Copyright (c) 2019 Denis J Jackman"
__license__ = "Python"

if __name__ == "__main__":
    commands = getargs()
    print(walk_through(commands))
