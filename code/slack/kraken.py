#!/usr/bin/python
"""
    This is a slack bot item
    Based on the tutorial at https://www.youtube.com/watch?v=oDoFvpDftBA
"""

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 1.10 $"
__date__ = "$Date: 2022/06/10 13:31:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"
import os
import sys
import logging
import re
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.gameitems.gamefunctions import credscheck  # noqa: E402

credid = credscheck('y:/pyproject/secrets/secrets.json')
SLACK_APP_TOKEN = credid["BoltKrakenToken"]
SLACK_BOT_TOKEN = credid["BoltKrakenBotToken"]

app = App(token=SLACK_BOT_TOKEN, name="Kraken")
logger = logging.getLogger(__name__)


@app.message(re.compile("^kraken"))  # type: ignore
def show_release_the_kraken(message, say):
    """ broadcast the message to the channels  """

    broadcast = message["text"][6:]
    for channel_id in ['CJJ5NE54G', 'G0CNSJKED', 'C0CNN2UQM', 'C0CNNJEH5']:
        say(f"{broadcast}", channel=channel_id)


def main():
    """ This is the main section """
    print("releasing the Kraken")
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()
    print("released the Kraken")


if __name__ == "__main__":
    main()
