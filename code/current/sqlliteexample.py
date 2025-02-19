"""
    SQLite example
    This takes a firefox sqllite database and counts the number of urls in the history
    The database is located at FILE_LOCATION
    The query is SELECT count(1) from moz_places
    Moz_places is a table in the database that contains the urls
    reference link
    https://medium.com/@jsaxena017/web-browser-forensics-part-2-firefox-browser-3dc6ef104607#:~:text=sqlite%20which%20is%20located%20in,are%20associated%20with%20browsing%20history.
"""
import os
import sys

# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.dbfunctions.slitefunc import open_sqllite
from jackmanimation.dbfunctions.slitefunc import sqllitequery

FIREFOX_FILE_LOCATION = "Z:/Data/Firefox/places.sqlite"
CHROME_LOCATION = "Z:/Data/Chrome/History"
EDGE_LOCATION = "Z:/Data/Edge/History"


def firefox_history_scan(fhs_file):
    ''' this utility function scans the firefox history '''
    fhs_connection = open_sqllite(fhs_file)
    if fhs_connection is None:
        return False, "[-] Connection failed"
    fhs_query = sqllitequery(fhs_connection, 'SELECT count(1) from moz_places')
    if fhs_query is None:
        return False, "[-] Query failed"
    return True, fhs_query


def chrome_history_scan(chs_file):
    ''' this utility function scans the chrome history '''
    chs_connection = open_sqllite(chs_file)
    if chs_connection is None:
        return False, "[-] Connection failed"
    chs_query = sqllitequery(chs_connection, 'SELECT * from urls')
    if chs_query is None:
        return False, "[-] Query failed"
    return True, chs_query


def edge_history_scan(ehs_file):
    ''' this utility function scans the edge history '''
    ehs_connection = open_sqllite(ehs_file)
    if ehs_connection is None:
        return False, "[-] Connection failed"
    ehs_query = sqllitequery(ehs_connection, 'SELECT * from urls')
    if ehs_query is None:
        return False, "[-] Query failed"
    return True, ehs_query


def main():
    ''' main function '''
    print("[-] Starting the sequence.")
    firefox_result = firefox_history_scan(FIREFOX_FILE_LOCATION)
    chrome_result = chrome_history_scan(CHROME_LOCATION)
    edge_result = edge_history_scan(EDGE_LOCATION)
    print(firefox_result)
    print(chrome_result)
    print(edge_result)


if __name__ == '__main__':
    main()
