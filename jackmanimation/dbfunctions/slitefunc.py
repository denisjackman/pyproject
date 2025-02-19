''' sqllitedbfucntions '''
import sqlite3


def open_sqllite(os_database):
    ''' open sqlite db '''
    try:
        os_client = sqlite3.connect(os_database)
    except sqlite3.Error as err:
        print(f" Error: {err}")
        return None
    print(f"[-] {os_client} Connected OK")
    return os_client


def sqllitequery(os_querydb, os_query):
    ''' mysql query'''
    try:
        os_resultcursor = os_querydb.cursor()
        os_resultcursor.execute(os_query)
    except sqlite3.Error as err:
        print(f" Error: {err}")
        return None
    print(f"[-] {os_query} Query OK")
    return os_resultcursor


def main():
    ''' main function '''
    print("[+] Starting SQLite Test")
    print("[+] SQLite Test Complete")


if __name__ == '__main__':
    main()
