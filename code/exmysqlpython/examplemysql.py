
"""
examplemysql.py

This program is a template for python programs
All this stuff at the top of the script is just optional metadata;

"""
import os
import sys

# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.gameitems.gamefunctions import credscheck
from jackmanimation.dbfunctions.mysqlfunctions import open_mysql
from jackmanimation.dbfunctions.mysqlfunctions import mysqlquery

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 0.01 $"
__date__ = "$Date: 2022/07/31 19:19:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"


def sqlmain():
    """ This is the main routine for the program """
    dbredid = credscheck('Z:/pyproject/secrets/secrets.json')
    mysqlusername = dbredid["BotUsername"]
    mysqlpassword = dbredid["BotPassword"]
    mysqlhostname = dbredid["hostname2"]

    use_db = open_mysql(mysqlusername,
                        mysqlpassword,
                        mysqlhostname,
                        'test')
    if use_db is None:
        return None
    examplecursor = mysqlquery(use_db, "SELECT * FROM fruit")

    counter = 0
    databasecount = 0
    tablecount = 0

    for (fruit_id, fruit_name, fruit_variety) in examplecursor:
        counter += 1
        print(f"{fruit_id}, {fruit_name} is {fruit_variety}")

    mycursor = mysqlquery(use_db, "SHOW DATABASES")
    print('[-] Looking at databases')
    for itemdatabase in mycursor:
        print(itemdatabase)
        databasecount += 1

    mycursor = mysqlquery(use_db, "SHOW TABLES")
    print('[-] Looking at tables now')
    for itemtable in mycursor:
        print(itemtable)
        tablecount += 1

    print(f"[-] I counted {counter} employee records that satisfied the query")
    print(f'[-] I counted {databasecount} databases')
    print(f'[-] I counted {tablecount} tables ')
    return None


if __name__ == '__main__':
    print("[+] Starting the sequence.")
    sqlmain()
    print("[+] Finishing up and closing down.")
