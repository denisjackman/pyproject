"""
    This is a slack bot item
    Based on the tutorial at https://www.youtube.com/watch?v=oDoFvpDftBA
"""

import logging
import re
import os
import sys

#pylint: disable=wrong-import-position
MODULE_PATH = "../module/"
sys.path.append(os.path.abspath(MODULE_PATH))
from jackmanimation import credscheck
#pylint: enable=wrong-import-position
import pyjokes
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

credid = credscheck()
SLACK_APP_TOKEN = credid["BoltJokesToken"]
SLACK_BOT_TOKEN = credid["BoltBotToken"]

app = App(token=SLACK_BOT_TOKEN, name="Joke Bot")
logger = logging.getLogger(__name__)


@app.message(re.compile("^knock knock$"))
def ask_who(message, say):
    """ KNOCK KNOCK """
    user = message['user']
    say(f"_who's there?_, <@{user}>!")
    for channel_id in ['CJJ5NE54G', 'G0CNSJKED', 'C0CNN2UQM', 'C0CNNJEH5']:
        say(f"<@{user}> called the bot.", channel=channel_id)


@app.message(re.compile("^duck$"))  # type: ignore
def show_random_joke(message, say):
    """Send a random pyjoke back """
    channel_type = message["channel_type"]
    if channel_type != "im":
        return

    dm_channel = message["channel"]
    user_id = message["user"]

    joke = pyjokes.get_joke()

    say(text=joke, channel=dm_channel)
    for channel_id in ['CJJ5NE54G', 'G0CNSJKED', 'C0CNN2UQM', 'C0CNNJEH5']:
        say(f"<@{user_id}> asked for a joke.", channel=channel_id)


@app.message(re.compile("^kraken"))  # type: ignore
def show_release_the_kraken(message, say):
    """ broadcast the message to the channels  """

    broadcast = message["text"][6:]
    for channel_id in ['CJJ5NE54G', 'G0CNSJKED', 'C0CNN2UQM', 'C0CNNJEH5']:
        say(f"{broadcast}", channel=channel_id)


def main():
    """ This is the main section """
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()


if __name__ == "__main__":
    main()