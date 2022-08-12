'''
    write emails
    # 2022 07 27 - NO LONGER WORKS THIS WAY AND NEEDS REDOING
'''

import smtplib
import json

CREDENTIALS = 'y:/pyproject/secrets/client_secrets.json'
with open(CREDENTIALS, 'r', encoding='utf8') as f:
    creds = json.load(f)

GMAIL_USER = creds['gmail_user']
GMAIL_PASSWORD = creds['pass_word']

sent_from = GMAIL_USER
to = ['denis_jackman@hotmail.com', 'denis.jackman@gmail.com']
RECEIVER = ",".join(to)
SUBJECT = 'OMG Super Important Message'
BODY = 'test message'

email_text = f"From: {sent_from}\nTo: {RECEIVER}\nSubject: {SUBJECT}\n\n{BODY}\n"

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(GMAIL_USER, GMAIL_PASSWORD)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print('Email sent!')
except smtplib.SMTPException as ex:
    print('Something went wrong...', ex)
