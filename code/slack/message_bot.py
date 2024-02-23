#!/usr/bin/python
"""
message_bot.py

This program is slack bot to post a message to multiple channels
All this stuff at the top of the script is just optional metadata;

"""

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 1.0 $"
__date__ = "$Date: 2022/06/01 00:31:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"
import os
import sys
from slack_bolt import App

# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.gameitems.gamefunctions import credscheck # noqa: E402

credid = credscheck('y:/pyproject/secrets/secrets.json')

app = App(
          token=credid["BotToken"],
          signing_secret=credid["SigningSecret"])

# Add functionality here
# @app.event("app_home_opened") etc

@app.command("/kraken")
def hello_command(ack, body):
    """ this is a hello command function """
    user_id = body["user_id"]
    ack(f"Hi <@{user_id}>!")

# Start your app


if __name__ == '__main__':
    app.start(port=3000)
