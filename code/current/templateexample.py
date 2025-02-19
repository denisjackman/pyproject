"""
template.py

This program is a template for python programs

All this stuff at the top of the script is just optional metadata;
the real code starts on the "if __name__" line
"""

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 1.0 $"
__date__ = "$Date: 2013/09/09 13:00:00 $"
__copyright__ = "Copyright (c) 2013 Denis J Jackman"
__license__ = "Python"

# System imports
import sys
import getopt


def procDefiniton(params):
    """Does stuff
    Returns string.
    """
    print(f"params: {params}")
    return "done!"


def usage():
    '''this is a function to show usage'''
    print("usage: template.py [-h] [-v] [-g grammar]")


def version():
    ''' this is a function to show version'''
    print(f"version: {__version__}")


def main(argv):
    '''this is a function to handle main'''
    grammar = "y:/Resources/xml/kant.xml"
    try:
        opts, args = getopt.getopt(argv,
                                   "hvg:d",
                                   ["help",
                                    "version",
                                    "grammar="])
        print("Done")
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    print(f"opts: {opts} args: {args} grammar: {grammar}")


if __name__ == "__main__":
    main(sys.argv[1:])
