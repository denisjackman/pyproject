# https://www.youtube.com/watch?v=09GG8GzfWhs

def send_slack_message(message: str):
    '''
    send message to slack
    '''
    import requests
    payload = '{"text": "%s"}' % message
    response = requests.post(
        'https://hooks.slack.com/services/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',
        data=payload
    )
    print(response.text)


def main(message_text: str):
    '''
    Main function for our logic
    '''
    send_slack_message(message=message_text)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Send Messages to Slack')
    parser.add_argument('--message', '-m', type=str, default='')
    args = parser.parse_args()
    msg = args.message
    if len(msg) > 0:
        main(message_text=msg)
    else:
        print('Give me a message!')