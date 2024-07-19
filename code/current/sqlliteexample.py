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

FILE_LOCATION = "C:/Users/Denis/AppData/Roaming/Mozilla/Firefox/Profiles/bg26yjup.default-release-1632146279182/places.sqlite"  # noqa: E501


try:
    conn = sqlite3.connect(FILE_LOCATION)
except sqlite3.Error as err:
    message = f'oops! I did it again: {err}'
    print(message)
finally:
    print("Connection made")

try:
    c = conn.cursor()
except sqlite3.Error as err:
    message = f'oops! I did it again: {err}'
    print(message)
finally:
    print("Cursor set up")

try:
    url_number = c.execute('SELECT count(1) from moz_places').fetchone()[0]
except sqlite3.Error as err:
    message = f'oops! I did it again: {err}'
    print(message)
finally:
    print("Query ran")
print(f"history length  {url_number}")
