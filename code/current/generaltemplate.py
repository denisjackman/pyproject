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
    return


def version():
    ''' this is a function to show version'''
    return


def main(argv):
    '''this is a function to handle main'''
    grammar = "y:/Resources/xml/kant.xml"
    gt_opts = []
    gt_args = []
    try:
        gt_opts, gt_args = getopt.getopt(argv,
                                         "hvg:d",
                                         ["help",
                                          "version",
                                          "grammar="])
        print("Done")
        usage()
        sys.exit(2)
    except getopt.GetoptError:
        print(f"gt_opts: {gt_opts} gt_args: {gt_args} grammar: {grammar}")


if __name__ == "__main__":
    main(sys.argv[1:])
