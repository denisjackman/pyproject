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
import pyjokes
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.gameitems.gamefunctions import credscheck

credid = credscheck('Z:/pyproject/secrets/secrets.json')
SLACK_APP_TOKEN = credid["BoltKrakenToken"]
SLACK_BOT_TOKEN = credid["BoltKrakenBotToken"]
SLACK_CHANNELS = ['CJJ5NE54G', 'G0CNSJKED', 'C0CNN2UQM', 'C0CNNJEH5']

app = App(token=SLACK_BOT_TOKEN, name="Kraken")
logger = logging.getLogger(__name__)


@app.command("/denis")
def hello_command(ack, body):
    """ this is a hello command function """
    user_id = body["user_id"]
    ack(f"Hi <@{user_id}>! release the Kraken!")


@app.message(re.compile("^kraken$", re.IGNORECASE))  # type: ignore
def show_kraken(message, say):
    """ broadcast the message to the channels  """
    print(f'[-] [Kraken] {message}')
    channel_type = message["channel_type"]
    dm_channel = message["channel"]
    user_id = message["user"]
    broadcast = "Releasing the Kraken! Beware we are coming for you!\n 3 \n 2 \n 1 \n Kraken Released!"

    if channel_type != "im":
        say(text=f'DM: {broadcast}', channel=dm_channel)
    else:
        say(text=f'IM: {broadcast}', channel=dm_channel)

    for channel_id in SLACK_CHANNELS:
        say(f"[-] <@{user_id}> asked for the Kraken:\n[{broadcast}]\n {message}", channel=channel_id)


@app.message(re.compile("^marsys", re.IGNORECASE))  # type: ignore
def show_marsys(message, say):
    """ broadcast the message to the channels  """
    print(f'[-] [Marsys] {message}')
    channel_type = message["channel_type"]
    dm_channel = message["channel"]
    user_id = message["user"]
    broadcast = f'[-] Marsys message is : [{message["text"][6:]}]'

    if channel_type != "im":
        say(text=f'DM: {broadcast}', channel=dm_channel)
    else:
        say(text=f'IM: {broadcast}', channel=dm_channel)

    for channel_id in SLACK_CHANNELS:
        say(f"[-] <@{user_id}> asked for the Kraken:\n[{broadcast}]\n {message}", channel=channel_id)


@app.message(re.compile("^joke$", re.IGNORECASE))  # type: ignore
def show_random_joke(message, say):
    """Send a random pyjoke back """
    print(f'[-] [Joke] {message}')
    channel_type = message["channel_type"]
    dm_channel = message["channel"]
    user_id = message["user"]
    joke = pyjokes.get_joke()

    if channel_type != "im":
        say(text=f'[-] CH: {joke}', channel=dm_channel)
    else:
        say(text=f'[-] IM: {joke}', channel=dm_channel)

    for channel_id in SLACK_CHANNELS:
        say(f"[-] <@{user_id}> asked for a joke.:\n[{joke}]\n[{message}]",
            channel=channel_id)


def main():
    """ This is the main section """
    print("[-] releasing the Kraken")
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()
    print("[-] released the Kraken")


if __name__ == "__main__":
    main()
