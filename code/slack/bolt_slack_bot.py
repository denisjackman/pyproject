"""
    This is a slack bot item
    Based on the tutorial at https://www.youtube.com/watch?v=oDoFvpDftBA
"""
import os
import sys
import logging
import re
import pyjokes
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.gameitems.gamefunctions import credscheck


credid = credscheck('Z:/pyproject/secrets/secrets.json')
SLACK_APP_TOKEN = credid["BoltAppToken"]
SLACK_BOT_TOKEN = credid["BoltBotToken"]
SLACK_CHANNELS = ['CJJ5NE54G', 'G0CNSJKED', 'C0CNN2UQM', 'C0CNNJEH5']

app = App(token=SLACK_BOT_TOKEN, name="Joke Bot")
logger = logging.getLogger(__name__)


@app.message(re.compile("^knock knock$"))
def ask_who(message, say):
    """ KNOCK KNOCK """
    user = message['user']
    say(f"_who's there?_, <@{user}>!")
    for channel_id in SLACK_CHANNELS:
        say(f"<@{user}> called the bot.", channel=channel_id)


@app.message(re.compile("^joke$"))  # type: ignore
def show_random_joke(message, say):
    """Send a random pyjoke back """
    channel_type = message["channel_type"]
    if channel_type != "im":
        return

    dm_channel = message["channel"]
    user_id = message["user"]

    joke = pyjokes.get_joke()

    say(text=joke, channel=dm_channel)
    for channel_id in SLACK_CHANNELS:
        say(f"<@{user_id}> asked for a joke.:\n[{joke}]", channel=channel_id)


@app.message(re.compile("^kraken"))  # type: ignore
def show_release_the_kraken(message, say):
    """ broadcast the message to the channels  """

    broadcast = message["text"][6:]
    for channel_id in SLACK_CHANNELS:
        say(f"{broadcast}", channel=channel_id)


def main():
    """ This is the main section """
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()


if __name__ == "__main__":
    main()
