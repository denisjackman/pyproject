"""
examplemysql.py

This program is a template for python programs
All this stuff at the top of the script is just optional metadata;

"""
import os
import sys
import mysql.connector

# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.gameitems.gamefunctions import credscheck  # noqa: E402


def dockersqlmain():
    """ This is the main routine for the program """
    dsm_dbredid = credscheck('Z:/pyproject/secrets/secrets.json')
    dsm_mysqlusername = dsm_dbredid["BotUsername"]
    dsm_mysqlpassword = dsm_dbredid["BotPassword"]
    dsm_databasecount = 0

    dsm_use_db = mysql.connector.connect(host='127.0.0.1',
                                         username=dsm_mysqlusername,
                                         password=dsm_mysqlpassword,
                                         port=3307)
    if dsm_use_db is None:
        return None
    dsm_mycursor = dsm_use_db.cursor()
    dsm_mycursor.execute('SHOW DATABASES')
    print('[-] Looking at databases')
    for dsm_itemdatabase in dsm_mycursor:
        print(dsm_itemdatabase)
        dsm_databasecount += 1
    print(f'[-] There are {dsm_databasecount} databases')
    return None


if __name__ == '__main__':
    print("[+] Starting the sequence.")
    dockersqlmain()
    print("[+] Finishing up and closing down.")
