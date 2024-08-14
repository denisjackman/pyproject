'''
    SLACK Bot example
'''
import logging
import os
import sys
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

# SLACK_APP_TOKEN = os.environ["SLACK_APP_TOKEN"]
# SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]

app = App(token=SLACK_BOT_TOKEN, name="Jokes")
logger = logging.getLogger(__name__)


@app.message(re.compile("^joke$"))  # type: ignore
def show_random_joke(message, say):
    """Send a random pyjoke back"""
    channel_type = message["channel_type"]
    if channel_type != "im":
        return

    dm_channel = message["channel"]
    user_id = message["user"]

    joke = pyjokes.get_joke()
    logger.info(f"Sent joke < {joke} > to user {user_id}")  # pylint: disable=logging-fstring-interpolation

    say(text=joke, channel=dm_channel)


def main():
    '''Main function'''
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()


if __name__ == "__main__":
    main()
