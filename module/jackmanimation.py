"""
jackmanimation.py

This program is a template for python programs
All this stuff at the top of the script is just optional metadata;

"""

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 1.0 $"
__date__ = "$Date: 2022/06/04 00:00:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"

import json


def credscheck(file_details):
    """ This function gathers the credentials needed to open anything """

    credentials = file_details
    try:
        with open(credentials, encoding="utf8") as creds_file:
            creds = json.load(creds_file)
    except OSError as err:
        message = f'Danger! Danger! Will Robinson!: {err}'
        print(message)
    else:
        print("Secrets loaded OK")

    return creds


def main():
    """ This is the main routine for the program """
    print("Starting the sequence:")
    print("finishing up and closing down:")


if __name__ == '__main__':
    main()
