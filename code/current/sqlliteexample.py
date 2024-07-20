"""
    SQLite example
    This takes a firefox sqllite database and counts the number of urls in the history
    The database is located at FILE_LOCATION
    The query is SELECT count(1) from moz_places
    Moz_places is a table in the database that contains the urls
    reference link
    https://medium.com/@jsaxena017/web-browser-forensics-part-2-firefox-browser-3dc6ef104607#:~:text=sqlite%20which%20is%20located%20in,are%20associated%20with%20browsing%20history.  # noqa: E501
"""
import sqlite3

FIREFOX_FILE_LOCATION = "Z:/Data/Firefox/places.sqlite"
CHROME_LOCATION = "Z:/Data/Chrome/History"
EDGE_LOCATION = "Z:/Data/Edge/History"


def firefox_history_scan(fhs_file):
    ''' this utility function scans the firefox history '''
    try:
        fhs_connection = sqlite3.connect(fhs_file)
    except sqlite3.Error as err:
        message = f'[o] oops! I did it again: {err}'
        return False, message
    finally:
        print("[+] Connection made")

    try:
        fhs_cursor = fhs_connection.cursor()
    except sqlite3.Error as err:
        message = f'[o] oops! I did it again: {err}'
        return False, message
    finally:
        print("[+] Cursor set up")

    try:
        fhs_query = fhs_cursor.execute('SELECT * from moz_places').fetchall()
    except sqlite3.Error as err:
        message = f'[o] oops! I did it again: {err}'
        return False, message
    finally:
        print("[+] Query ran")
    return True, fhs_query


def chrome_history_scan(chs_file):
    ''' this utility function scans the chrome history '''
    try:
        chs_connection = sqlite3.connect(chs_file)
    except sqlite3.Error as err:
        message = f'[o] oops! I did it again: {err}'
        return False, message
    finally:
        print("[+] Connection made")
    try:
        chs_cursor = chs_connection.cursor()
    except sqlite3.Error as err:
        message = f'[o] oops! I did it again: {err}'
        return False, message
    finally:
        print("[+] Cursor set up")
    try:
        chs_query = chs_cursor.execute('SELECT * from urls')
        chs_query = chs_query.fetchall()
    except sqlite3.Error as err:
        message = f'[o] oops! I did it again: {err}'
        return False, message
    finally:
        print("[+] Query ran")
    return True, chs_query


def edge_history_scan(ehs_file):
    ''' this utility function scans the edge history '''
    try:
        ehs_connection = sqlite3.connect(ehs_file)
    except sqlite3.Error as err:
        message = f'[o] oops! I did it again: {err}'
        print(message)
        return False, message
    finally:
        print("[+] Connection made")

    try:
        ehs_cursor = ehs_connection.cursor()
    except sqlite3.Error as err:
        message = f'[o] oops! I did it again: {err}'
        print(message)
        return False, message
    finally:
        print("[+] Cursor set up")

    try:
        ehs_query = ehs_cursor.execute('SELECT * from urls')
        ehs_query = ehs_query.fetchall()
    except sqlite3.Error as err:
        message = f'[o] oops! I did it again: {err}'
        print(message)
        return False, message
    finally:
        print("[+] Query ran")
    return True, ehs_query


def main():
    ''' main function '''
    print("[-] Starting the sequence.")
    firefox_result = firefox_history_scan(FIREFOX_FILE_LOCATION)
    if firefox_result[0]:
        print(f"[=] Firefox history length {firefox_result[0]} : {len(firefox_result[1])}")
    else:
        print(f"[=] Firefox Error message  {firefox_result[1]}")
    chrome_result = chrome_history_scan(CHROME_LOCATION)
    if chrome_result[0]:
        print(f"[=] Chrome history length {chrome_result[0]} : {len(chrome_result[1])}")
    else:
        print(f"[=] Chrome Error message  {chrome_result[1]}")
    edge_result = edge_history_scan(EDGE_LOCATION)
    if edge_result[0]:
        print(f"[=] Edge history length {edge_result[0]} : {len(edge_result[1])}")
    else:
        print(f"[=] Edge Error message  {edge_result[1]}")
    print("[-] Finished the sequence.")


if __name__ == '__main__':
    main()
