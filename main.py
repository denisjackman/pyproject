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
from slackclient import SlackClient


def credscheck():
    """ This function gathers the credentials for a user """

    credentials = 'secrets/credentials.json'
    try:
        with open(credentials, encoding="utf8") as creds_file:
            creds = json.load(creds_file)
    except OSError as err:
        message = f'Danger! Danger! Will Robinson!: {err}'
        print(message)
    else:
        print("Secrets loaded OK")

    return (creds)


def opendb(credid, database):
    """ This function opens the databse connection """
    username = credid["username"]
    password = credid["password"]
    hostname = credid["hostname"]

    try:
        my_db = mysql.connector.connect(
            host=hostname,
            user=username,
            password=password,
            database=database
        )
    except mysql.connector.Error as err:
        message = f'oops! I did it again: {err}'
        print(message)
    else:
        print("Connected OK")
    return my_db


def main():
    """ This is the main routine for the program """
    print("Starting the sequence:")
    credid = credscheck()

    use_db = opendb(credid, 'mydatabase')  # pylint: disable=W0612

    token = credid["SlackOAuthToken"]
    sc = SlackClient(token)
    print(sc.api_call("api.test"))
    print(sc.api_call("channels.info", channel="1234567890"))
    print(sc.api_call(
                        "chat.postMessage",
                        channel="#bottest",
                        text="Hello from Python! :tada:",
                        username='pybot',
                        icon_emoji=':robot_face:'
                        ))
    print("finishing up and closing down:")


if __name__ == '__main__':
    main()
