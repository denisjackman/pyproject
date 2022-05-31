"""
main.py

This program is a template for python programs
All this stuff at the top of the script is just optional metadata;

"""

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 1.0 $"
__date__ = "$Date: 2022/05/31 00:31:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"

import json
import mysql.connector


def creds():
    global username
    global password
    global hostname
    credentials = 'secrets/credentials.json'
    try:
        with open(credentials) as f:
            creds = json.load(f)
    except OSError as err:
        print("Danger! Danger! Will Robinson!: {}".format(err))
    else:
        print("Secrets loaded OK")
    username = creds["username"]
    password = creds["password"]
    hostname = creds["hostname"]
    return


def opendb(database):
    global mydb
    try:
        mydb = mysql.connector.connect(
                                        host=hostname,
                                        user=username,
                                        password=password,
                                        database=database
                                        )
    except mysql.connector.Error as err:
        print("oops! I did it again: {}".format(err))
    else:
        print("Connected OK")
    return


if __name__ == '__main__':
    creds()
    opendb('mydatabase')
