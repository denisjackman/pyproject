"""
    This is another slackbot module
    and it is based on  https://www.youtube.com/watch?v=09GG8GzfWhs
"""
import os
import sys
import argparse
import requests


#pylint: disable=wrong-import-position
MODULE_PATH = "../module/"
sys.path.append(os.path.abspath(MODULE_PATH))
from jackmanimation import credscheck
#pylint: enable=wrong-import-position


def send_slack_message(message: str, channels: str):
    '''
    send message to slack
    '''
    for webhook in channels["Channels"]:
        payload = '{"text": "{%s}"}' % message  # pylint: disable=C0209
        response = requests.post(
            webhook["Webhook"],
            data=payload
            )
        print(response.text)


def send_slack_file(file: str, channels: str):
    """
    Send file function
    """
    # response = client.files_upload(
    #          channels='#Random',
    #          filetype='pdf',
    #          filename='sampleReport.pdf',
    #          title='Sample Report',
    #          file='sample.pdf')
    print(file)
    print(channels)


def main():
    '''
    Main function for our logic
    '''
    channelslist = credscheck('credentials.json')
    parser = argparse.ArgumentParser(description='Send Messages to Slack')
    parser.add_argument('--message', '-m', type=str, default='')
    parser.add_argument('--file', '-f', type=str, default='')
    args = parser.parse_args()

    msg = args.message
    if args.file == '':
        if len(msg) > 0:
            send_slack_message(message=msg, channels=channelslist)
        else:
            print('Give me a message!')
    else:
        print(args.file)
        send_slack_file(file=args.file, channels=channelslist)


if __name__ == '__main__':
    main()
