'''
    write emails
'''
import smtplib
import json

credentials = 'y:/pyproject/secrets/client_secrets.json'
with open(credentials, 'r', encoding='utf8') as f:
    creds = json.load(f)

gmail_user = creds['gmail_user']
gmail_password = creds['pass_word']

sent_from = gmail_user
to = ['denis_jackman@hotmail.com', 'denis.jackman@gmail.com']
receiver = ",".join(to)
subject = 'OMG Super Important Message'
body = 'test message'

email_text = f"From: {sent_from}\nTo: {receiver}\nSubject: {subject}\n\n{body}\n"

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print('Email sent!')
except smtplib.SMTPException as ex:
    print('Something went wrong...', ex)
