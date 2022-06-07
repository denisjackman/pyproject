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


@app.message(":wave:")
def say_hello(message, say):
    """ reponse to reaction """
    user = message['user']
    say(f"Hi there, <@{user}>!")


@app.message("knock knock")
def ask_who(message, say):
    """ KNOCK KNOCK """
    user = message['user']
    say(f"_who's there?_, <@{user}>!")


@app.command("/echo")
def repeat_text(ack, respond, command):
    """ echo slash command """
    # Acknowledge command request
    ack()
    respond(f"{command['text']}")


@app.message(re.compile("^joke$"))  # type: ignore
def show_random_joke(message, say):
    """Send a random pyjoke back """
    channel_type = message["channel_type"]
    if channel_type != "im":
        return

    dm_channel = message["channel"]
    user_id = message["user"]

    joke = pyjokes.get_joke()
    logger.info('Sent joke < %s > to user %s', joke, user_id)

    say(text=joke, channel=dm_channel)


@app.command("/kraken")
def hello_command(ack, body):
    """ this is a hello command function """
    user_id = body["user_id"]
    ack(f"Hi <@{user_id}>!")


def main():
    """ This is the main section """
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()


if __name__ == "__main__":
    main()
