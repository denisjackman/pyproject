"""
messageBot.py

This program is slack bot to post a message to multiple channels
All this stuff at the top of the script is just optional metadata;

"""

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 1.0 $"
__date__ = "$Date: 2022/06/01 00:31:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"

import json
from slack_bolt import App


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


credid = credscheck()
app = App(
          token=credid["BotToken"],
          signing_secret=credid["SigningSecret"])


# Add functionality here
# @app.event("app_home_opened") etc

@app.command("/kraken")
def hello_command(ack, body):
    user_id = body["user_id"]
    ack(f"Hi <@{user_id}>!")


# Start your app

if __name__ == '__main__':
    app.start(port=3000)