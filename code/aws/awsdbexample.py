
"""
examplemysql.py

This program is a template for python programs
All this stuff at the top of the script is just optional metadata;

"""
import mysql.connector
import os
import sys

# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.gameitems.gamefunctions import credscheck


def main():
    """ This is the main routine for the program """
    dbredid = credscheck('Z:/pyproject/secrets/secrets.json')
    endpoint = dbredid["AWSRDSHost"]
    password = dbredid["AWSRDSPassword"]
    database = dbredid["AWSRDSDBName"]
    username = dbredid["MySQLUsername"]
    # Connect to the database
    connection = mysql.connector.connect(user=username,
                                         password=password,
                                         host=endpoint,
                                         database=database)
    # Create a cursor object
    cursor = connection.cursor()
    create_table_query = '''
    CREATE TABLE users (
    id INT(11) NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
    )
    '''

    cursor.execute(create_table_query)
    connection.commit()
    cursor.close()
    connection.close()


if __name__ == '__main__':
    print("[+] Starting the sequence.")
    main()
    print("[+] Finishing up and closing down.")
