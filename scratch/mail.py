<<<<<<< Updated upstream
'''
    write emails
    # 2022 07 27 - NO LONGER WORKS THIS WAY AND NEEDS REDOING
'''

import smtplib
import json
from email.message import EmailMessage

CREDENTIALS = 'y:/pyproject/secrets/client_secrets.json'
with open(CREDENTIALS, 'r', encoding='utf8') as filereader:
    creds = json.load(filereader)

GMAIL_USER = creds['gmail_username']
GMAIL_PASSWORD = creds['gmail_password']

msg = EmailMessage()
msg['Subject'] = 'Hey!'
msg['From'] = GMAIL_USER
msg['To'] = 'denis_jackman@hotmail.com'


msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h3 style="color:Black;">Hi</h3>
        <h3 style="color:Black;"> How are you ?</h3>
        
    </body>
</html>
""", subtype='html')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(GMAIL_USER, GMAIL_PASSWORD)
    smtp.send_message(msg)
=======
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
>>>>>>> Stashed changes
