''' pd sql connection '''
import os
import sys
import pandas as pd
# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.gameitems.gamefunctions import credscheck
from jackmanimation.dbfunctions.mysqlfunctions import open_mysql
from jackmanimation.dbfunctions.mysqlfunctions import mysqlquery


def main():
    ''' main function '''
    ps_creds = credscheck('Z:/pyproject/secrets/secrets.json')
    ps_username = ps_creds["BotUsername"]
    ps_password = ps_creds["BotPassword"]
    ps_hostname = ps_creds["hostname2"]
    ps_database = 'test'
    ps_db = open_mysql(ps_username,
                       ps_password,
                       ps_hostname,
                       ps_database)
    ps_query = "SELECT * FROM fruit"

    if ps_db is None:
        print("[-] database issues closing")
        return None

    pd_query_result = pd.read_sql(ps_query, ps_db)
    pd_query_result['name'].hist()
    print(pd_query_result.info())

if __name__ == '__main__':
    main()
