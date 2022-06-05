"""
    SQLite example
"""
import sqlite3


try:
    conn = sqlite3.connect('data/History')
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
    url_number = c.execute('SELECT count(1) from urls').fetchone()[0]
except sqlite3.Error as err:
    message = f'oops! I did it again: {err}'
    print(message)
finally:
    print("Query ran")
print("history length ", url_number)
