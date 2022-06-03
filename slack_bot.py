"""
    This is another slackbot module
    and it is based on  https://www.youtube.com/watch?v=09GG8GzfWhs
"""
import argparse
import json
import requests


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

    return creds


def send_slack_message(message: str):
    '''
    send message to slack
    '''
    webhook = credid["SlackWebHook"]
    payload = '{"text": "{%s}"}' % message  # pylint: disable=C0209
    response = requests.post(
        webhook,
        data=payload
    )
    print(response.text)


def main(message_text: str):
    '''
    Main function for our logic
    '''
    send_slack_message(message=message_text)


if __name__ == '__main__':
    credid = credscheck()
    parser = argparse.ArgumentParser(description='Send Messages to Slack')
    parser.add_argument('--message', '-m', type=str, default='')
    args = parser.parse_args()
    msg = args.message
    if len(msg) > 0:
        main(message_text=msg)
    else:
        print('Give me a message!')
