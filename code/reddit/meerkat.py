''' this is a reddit bit to monitor posting '''
import os
import sys
from datetime import datetime
import praw
import mysql.connector

# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.gameitems.gamefunctions import credscheck


def check_database(checkdb, checkusername):
    ''' check the database for the last time we checked '''
    result = False
    cursor = checkdb.cursor()
    query = f"SELECT * FROM posts WHERE username = '{checkusername}'"
    try:
        cursor.execute(query)
        records = cursor.fetchall()
        if records is None:
            result = False
        else:
            result = True
    except mysql.connector.errors.ProgrammingError as err:
        print(f"[-] Error: {err} \n Query: {query}")
        result = False
    return result


def insert_row(insertdb, insertusername, insertdate):
    ''' insert the row into the database'''
    result = False
    cursor = insertdb.cursor()
    query = f"INSERT INTO posts(postdate, username) VALUES ('{insertdate}', '{insertusername}')"
    try:
        cursor.execute(query)
        insertdb.commit()
        result = True
    except mysql.connector.errors.ProgrammingError as err:
        print(f"[-] Error: {err} \n Query: {query}")
        result = False
    return result


def opendb(credid, database):
    """ This function opens the database connection """
    username = credid["BotUsername"]
    password = credid["BotPassword"]
    hostname = credid["hostname2"]
    try:
        my_db = mysql.connector.connect(
            host=hostname,
            user=username,
            password=password,
            database=database
            )
    except mysql.connector.errors.ProgrammingError as err:
        print(f" Error: {err}")
        return None
    print(f"[-] {my_db} Connected OK")
    return my_db


def main():
    ''' main function '''
    print("[+] Meerkatbot is starting up")

    credid = credscheck('Z:/pyproject/secrets/secrets.json')
    use_db = opendb(credid, 'meerkatbot')

    if use_db is None:
        print("[-] Database connection failed")
    else:
        print("[+] Database connection OK")

    try:
        reddit = praw.Reddit(
            client_id='Meerkatbot by jackmanimation',
            client_secret=credid['RedditSecret'],
            password=credid['OredditPassword'],
            user_agent='Meerkatbot by jackmanimation',
            username=credid['OredditUsername'])
        # pylint: disable=W0702
    except:
        print("Reddit login failed")
        sys.exit(1)

    print(f"[-] {reddit.user.me()} is logged in")
    subreddit = reddit.subreddit('funny')
    print(f"[-] {subreddit.display_name} is being monitored")
    user = reddit.redditor(credid['OredditUsername'])
    print(f"[-] {user.name} is Mod: {user.is_mod} and Gold: {user.is_gold}")

    for submission in subreddit.stream.submissions():
        author = submission.author
        itemdate = datetime.utcfromtimestamp(submission.created_utc).strftime('%Y-%m-%d')
        submissiondate = datetime.utcfromtimestamp(submission.created_utc)
        timenow = datetime.utcnow()
        timenow = timenow.replace(hour=0, minute=0, second=0, microsecond=0)
        submissiondate = submissiondate.replace(hour=0,
                                                minute=0,
                                                second=0,
                                                microsecond=0)
        timediff = timenow - submissiondate
        if author is None:
            print(f"[-] '{submission.title}' Author: None created: {itemdate} ago: {timediff.days}")
        else:
            if check_database(use_db, author.name):
                print(f"[-] Author: {submission.author.name} Created: {itemdate} - NOT ADDED")
            else:
                insert_row(use_db, author.name, itemdate)
                print(f"[-] Author: {submission.author.name} Created: {itemdate} - ADDED")
    print("[+] Meerkatbot is shutting down")


if __name__ == '__main__':
    main()
