'''
    gmail-sender
    reference:
        https://towardsdatascience.com/automate-sending-emails-with-gmail-in-python-449cc0c3c317

    pip install yagmail
'''
from pathlib import Path
import json
import yagmail

FILEPATH = Path(__file__).parent

def main():
    ''' main function '''
    with open(f"{FILEPATH}/../secrets/client_secrets.json", "r", encoding='utf8') as file:
        cred_id = json.load(file)
    emailid = cred_id["gmail_username"]
    email_password = cred_id["gmail_token"]

    to = 'denis.jackman@gmail.com'

    subject = 'test subject 1'
    content = ['mail body content', 'pytest.ini', 'test.png']

    with yagmail.SMTP(emailid, email_password) as yag:
        yag.send(to, subject, content)
        print('Sent email successfully')

if __name__ == '__main__':
    main()