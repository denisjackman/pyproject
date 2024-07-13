#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
examplemysql.py

This program is a template for python programs
All this stuff at the top of the script is just optional metadata;

"""
import json
import mysql.connector

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 0.01 $"
__date__ = "$Date: 2022/07/31 19:19:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"


def dsm_credscheck(file_details):
    """
        This function gathers the credentials needed to open anything
    """

    credentials = file_details
    try:
        with open(credentials, encoding="utf8") as creds_file:
            creds = json.load(creds_file)
    except Exception as err:
        message = f'[-] Danger! Danger! Will Robinson!: {err}'
        print(message)
        return []
    print("[-] Secrets loaded OK")
    creds_file.close()
    return creds


def dockersqlmain():
    """ This is the main routine for the program """
    dsm_dbredid = dsm_credscheck('Z:/pyproject/secrets/secrets.json')
    dsm_mysqlusername = dsm_dbredid["Botusername"]
    dsm_mysqlpassword = dsm_dbredid["Botpassword"]

    dsm_use_db = mysql.connector.connect(host='127.0.0.1',
                                         username=dsm_mysqlusername,
                                         password=dsm_mysqlpassword,
                                         port=3307)
    if dsm_use_db is None:
        return None
    mycursor = dsm_use_db.cursor()
    mycursor.execute('SHOW DATABASES')
    print('[-] Looking at databases')
    for itemdatabase in mycursor:
        print(itemdatabase)
        databasecount += 1

    return None


if __name__ == '__main__':
    print("[+] Starting the sequence.")
    dockersqlmain()
    print("[+] Finishing up and closing down.")
