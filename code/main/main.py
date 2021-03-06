#!/usr/bin/python
"""
main.py

This program is a template for python programs
All this stuff at the top of the script is just optional metadata;

"""

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 1.10 $"
__date__ = "$Date: 2022/05/31 00:31:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"

import mysql.connector
from djgamemodule import security as sec


def opendb(credid, database):
    """ This function opens the database connection """
    username = credid["username"]
    password = credid["password"]
    hostname = credid["hostname"]

    try:
        my_db = mysql.connector.connect(
            host=hostname,
            user=username,
            password=password,
            database=database
        )
    except mysql.connector.Error as err:
        message = f'oops! I did it again: {err}'
        print(message)
    else:
        print("Connected OK")
    return my_db


def main():
    """ This is the main routine for the program """
    print("Starting the sequence:")
    credid = sec.credscheck('y:/pyproject/secrets/credentials.json')
    use_db = opendb(credid, 'testdb')  # pylint: disable=W0612
    print("finishing up and closing down:")


if __name__ == '__main__':
    main()
