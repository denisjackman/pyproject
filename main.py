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


def credscheck():
    """ This function gathers the credentials for a user """

    credentials = 'secrets/credentials.json'
    try:
        with open(credentials) as credsfile:
            creds = json.load(credsfile)
    except OSError as err:
        print("Danger! Danger! Will Robinson!: {}".format(err))
    else:
        print("Secrets loaded OK")

    return (creds["username"], creds["password"], creds["hostname"])


def opendb(credid, database):
    """ This function opens the databse connection """
    username = credid[0]
    password = credid[1]
    hostname = credid[2]

    try:
        myDb = mysql.connector.connect(
                                        host=hostname,
                                        user=username,
                                        password=password,
                                        database=database
                                        )
    except mysql.connector.Error as err:
        print("oops! I did it again: {}".format(err))
    else:
        print("Connected OK")
    return myDb


def main():
    print("Starting the sequence:")
    credid = credscheck()
    useDB = opendb(credid, 'mydatabase')
    print("finishing up and closing down:")


if __name__ == '__main__':
    main()
