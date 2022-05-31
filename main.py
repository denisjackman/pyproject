"""
main.py

This program is a template for python programs
All this stuff at the top of the script is just optional metadata;

"""

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 1.0 $"
__date__ = "$Date: 2022/05/31 00:31:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"

import json
import mysql.connector

credentials = 'client_secrets.json'
with open(credentials) as f:
    creds = json.load(f)

username = creds["username"]
password = creds["password"]
hostname = creds["hostname"]
database = 'mydatabase'

try:
    mydb = mysql.connector.connect(
                                    host=hostname,
                                    user=username,
                                    password=password,
                                    database=database
                                    )
except:
    print("oops! I did it again")
else:
    print("Connected OK")
