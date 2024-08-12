"""
oneliner.py

This program is a template for python programs
All this stuff at the top of the script is just optional metadata;

"""
import os
import sys
import wifi_qrcode_generator as qr

# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.gameitems.gamefunctions import credscheck


__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 0.00 $"
__date__ = "$Date: 2022/09/12 09:00:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"


def main():
    """ This is the main routine for the program """
    print("Starting the sequence:")
    credid = credscheck('Z:/pyproject/secrets/secrets.json')
    qr.wifi_qrcode(credid["wifi"], False, 'WPA', credid["wifi_password"])
    print("finishing up and closing down:")
    # TODO: change this export to a file instead of stdout


if __name__ == '__main__':
    main()
