#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
examplemysql.py

This program is a template for python programs
All this stuff at the top of the script is just optional metadata;

"""

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 0.01 $"
__date__ = "$Date: 2022/07/31 19:19:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"

import mysql.connector
from djgamemodule import security as sec
SECRETSFILE = 'y:/pyproject/secrets/secrets.json'

def opendb(credid, database):
    """ This function opens the database connection """
    username = credid["username"]
    password = credid["password"]
    hostname = credid["hostname2"]
    try:
        my_db = mysql.connector.connect(
            host=hostname,
            user=username,
            password=password,
            database=database
            )
    except mysql.connector.errors.ProgrammingError as err:
        print(f" Error: {err}")
        return None
    print(f"[-] {my_db} Connected OK")
    return my_db


def sqlmain():
    """ This is the main routine for the program """
    credid = sec.credscheck(SECRETSFILE)
    use_db = opendb(credid, 'test')
    if use_db is None:
        return None
    cursor = use_db.cursor()
    query = "SELECT * FROM fruit"

    counter = 0
    databasecount = 0
    tablecount = 0

    cursor.execute(query)
    for (fruit_id, fruit_name,fruit_variety) in cursor:
        counter += 1
        print(f"{fruit_id}, {fruit_name} is {fruit_variety}")

    mycursor = use_db.cursor()
    mycursor.execute("SHOW DATABASES")
    print ('[-] Looking at databases')
    for itemdatabase in mycursor:
        print(itemdatabase)
        databasecount += 1

    mycursor.execute("SHOW TABLES")
    print('[-] Looking at tables now')
    for itemtable in mycursor:
        print(itemtable)
        tablecount += 1

    cursor.close()
    mycursor.close()
    use_db.close()

    print(f"[-] I counted {counter} employee records that satisfied the query")
    print(f'[-] I counted {databasecount} databases')
    print(f'[-] I counted {tablecount} tables ')
    return None

if __name__ == '__main__':
    print("[+] Starting the sequence.")
    sqlmain()
    print("[+] Finishing up and closing down.")
