''' mysql functions '''
import mysql.connector


def open_mysql(mysqlusername,
               mysqlpassword,
               mysqlhostname,
               dbdatabase=None,
               mysqlport=3306):
    ''' open mysql db '''
    try:
        client = mysql.connector.connect(
            host=mysqlhostname,
            user=mysqlusername,
            password=mysqlpassword,
            database=dbdatabase,
            port=mysqlport
            )
    except mysql.connector.errors.ProgrammingError as err:
        print(f" Error: {err}")
        return None
    print(f"[-] {client} Connected OK")
    return client


def mysqlquery(querydb, query):
    ''' mysql query'''
    resultcursor = querydb.cursor()
    resultcursor.execute(query)
    return resultcursor


def main():
    ''' main function '''


if __name__ == '__main__':
    print("[+] Starting MySQL Test")
    main()
    print("[+] MySQL Test Complete")
