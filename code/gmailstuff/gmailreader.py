'''
gmail reader module

based on the gmail api quickstart example
https://www.youtube.com/watch?v=Px7Ts3y-aWc

project name:  jackmaninationgmail
'''
import os.path
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import gspread
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these SCOPES, delete the file TOKEN_FILE.
MAIL_SCOPES = ['https://www.googleapis.com/auth/gmail.readonly',
               'https://www.googleapis.com/auth/gmail.send']
SPRD_SCOPES = ['https://www.googleapis.com/auth/drive',
               'https://www.googleapis.com/auth/spreadsheets']
DOCS_SCOPES = ['https://www.googleapis.com/auth/documents',
               'https://www.googleapis.com/auth/drive']

TOKEN_FILE = 'Z:/pyproject/secrets/token.json'
CREDENTIALS_FILE = 'Z:/pyproject/secrets/gmail.json'


def get_google_credentials(ggc_scope):
    '''get gmail credentials'''
    ggc_creds = None
    # The file TOKEN_FILE stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(TOKEN_FILE):
        ggc_creds = Credentials.from_authorized_user_file(TOKEN_FILE,
                                                          ggc_scope)
    # If there are no (valid) credentials available, let the user log in.
    if not ggc_creds or not ggc_creds.valid:
        if ggc_creds and ggc_creds.expired and ggc_creds.refresh_token:
            ggc_creds.refresh(Request())
        else:
            ggc_flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE,
                                                                 ggc_scope)
            ggc_creds = ggc_flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(TOKEN_FILE, 'w') as ggc_token:  # pylint: disable=w1514
            ggc_token.write(ggc_creds.to_json())
    return ggc_creds


def get_gmail_messages(ggm_creds):
    '''get gmail messages'''
    ggm_service = build('gmail', 'v1', credentials=ggm_creds)

    # Call the Gmail API
    ggm_results = ggm_service.users().messages().list(userId='me',
                                                      maxResults=10).execute()
    ggm_messages = ggm_results.get('messages', [])
    return ggm_messages


def get_gmail_message(ggm_creds, ggm_message_id):
    '''get gmail message'''
    ggm_service = build('gmail', 'v1', credentials=ggm_creds)
    ggm_message = ggm_service.users().messages().get(userId='me',
                                                     id=ggm_message_id).execute()
    return ggm_message


def create_message(cm_sender, cm_to, cm_subject, cm_message_text):
    """Create a message for an email."""
    cm_message = MIMEText(cm_message_text)
    cm_message['to'] = cm_to
    cm_message['from'] = cm_sender
    cm_message['subject'] = cm_subject
    cm_raw = base64.urlsafe_b64encode(cm_message.as_bytes())
    cm_raw = cm_raw.decode()
    return {'raw': cm_raw}


def send_gmail_message(sgm_creds,
                       sgm_sender,
                       sgm_to,
                       sgm_subject,
                       sgm_message_text,
                       sgm_file_path=None):
    """Send an email message."""
    sgm_service = build('gmail',
                        'v1',
                        credentials=sgm_creds)
    if sgm_file_path:
        sgm_message = create_message_with_attachment(sgm_sender,
                                                     sgm_to,
                                                     sgm_subject,
                                                     sgm_message_text,
                                                     sgm_file_path)
    else:
        sgm_message = create_message(sgm_sender,
                                     sgm_to,
                                     sgm_subject,
                                     sgm_message_text)
    sgm_sent_message = sgm_service.users().messages().send(userId='me',
                                                           body=sgm_message).execute()
    return sgm_sent_message


def create_message_with_attachment(cmwa_sender,
                                   cmwa_to,
                                   cmwa_subject,
                                   cmwa_message_text,
                                   cmwa_file_path):
    """Create a message for an email with an attachment."""
    cmwa_message = MIMEMultipart()
    cmwa_message['to'] = cmwa_to
    cmwa_message['from'] = cmwa_sender
    cmwa_message['subject'] = cmwa_subject

    cmwa_msg = MIMEText(cmwa_message_text)
    cmwa_message.attach(cmwa_msg)

    # Attach the file
    with open(cmwa_file_path, 'rb') as cmwa_file:
        cmwa_mime_base = MIMEBase('application',
                                  'octet-stream')
        cmwa_mime_base.set_payload(cmwa_file.read())
        encoders.encode_base64(cmwa_mime_base)
        cmwa_mime_base.add_header('Content-Disposition',
                                  f'attachment; filename={os.path.basename(cmwa_file_path)}')
        cmwa_message.attach(cmwa_mime_base)

    cmwa_raw = base64.urlsafe_b64encode(cmwa_message.as_bytes())
    cmwa_raw = cmwa_raw.decode()
    return {'raw': cmwa_raw}


def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    print('[-] Gmail utility starting')
    creds = get_google_credentials(SPRD_SCOPES)
    # messages = get_gmail_messages(creds)
    messages = None
    print('[-] Gmail messages starting')
    if not messages:
        print('[o] No messages found.')
    else:
        print(f'[-] Messages: {len(messages)}')
        # for message in messages:
        #     message_detail = get_gmail_message(creds, message['id'])
        #     print(f'[+] {message_detail["snippet"]}')
    print('[-] Gmail sender starting')
    # sent_message = send_gmail_message(creds,
    #                                   'me',
    #                                   'denis.jackman@gmail.com',
    #                                   'Test',
    #                                   'Test message')

    # print(f'[+] Message sent: {sent_message["id"]}')
    # sent_message = send_gmail_message(creds,
    #                                  'me',
    #                                   'denis.jackman@gmail.com',
    #                                  'Test 2',
    #                                  'Test message2',
    #                                  'Z:/Resources/text/stuff.txt')

    print('[-] Gmail sender complete.')
    print('[-] Google Sheets Test Start')
    client = gspread.authorize(creds)
    spreadsheet = client.open('Test')
    worksheet = spreadsheet.get_worksheet(0)
    worksheet.update_cell(1, 1, 'Updated Value')
    worksheet.append_row(['New Value 1',
                          'New Value 2',
                          'New Value 3',
                          'New Value 4',
                          'New Value 5',
                          'New Value 6'])
    print('[-] Google Sheets Test Complete')
    print('[-] Gmail utility complete.')


if __name__ == '__main__':
    main()
