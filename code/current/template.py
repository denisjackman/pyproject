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


def usage():
    '''
        usage
    '''
    return


def version():
    '''
        version
    '''
    print("This is the Veriosn piece")


def main(argv):
    '''
        main function
    '''
    # grammar = "kant.xml"
    try:
        opts, args = getopt.getopt(argv,
                                   "hvg:d",
                                   ["help",
                                    "version",
                                    "grammar="])
        print(f"Done {opts} {args}")
    except getopt.GetoptError:
        usage()
        sys.exit(2)


if __name__ == "__main__":
    main(sys.argv[1:])
