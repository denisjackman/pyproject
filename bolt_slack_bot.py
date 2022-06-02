# https://www.youtube.com/watch?v=oDoFvpDftBA
import logging
import re
import json
import pyjokes
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler


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
SLACK_APP_TOKEN = credid["BoltAppToken"]
SLACK_BOT_TOKEN = credid["BoltBotToken"]

app = App(token=SLACK_BOT_TOKEN, name="Joke Bot")
logger = logging.getLogger(__name__)


@app.message(re.compile("^joke$"))  # type: ignore
def show_random_joke(message, say):
    """Send a random pyjoke back """
    channel_type = message["channel_type"]
    if channel_type != "im":
        return

    dm_channel = message["channel"]
    user_id = message["user"]

    joke = pyjokes.get_joke()
    logger.info(f"Sent joke < {joke} > to user {user_id}")

    say(text=joke, channel=dm_channel)


def main():
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()


if __name__ == "__main__":
    main()
