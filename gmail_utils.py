from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import base64
import email
from dotenv import load_dotenv
load_dotenv()
import os
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly',
          'https://www.googleapis.com/auth/calendar',
          'https://www.googleapis.com/auth/gmail.send']

def authenticate_gmail():
    flow = InstalledAppFlow.from_client_secrets_file(os.getenv("GOOGLE_CLIENT_SECRET_FILE"), SCOPES)
    creds = flow.run_local_server(port=0)
    return build('gmail', 'v1', credentials=creds)

def get_recent_emails(service, max_results=5):
    results = service.users().messages().list(userId='me', maxResults=max_results).execute()
    messages = results.get('messages', [])
    emails = []

    for msg in messages:
        msg_data = service.users().messages().get(userId='me', id=msg['id']).execute()
        payload = msg_data['payload']
        headers = payload['headers']
        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), '')
        sender = next((h['value'] for h in headers if h['name'] == 'From'), '')
        body = ''

        def extract_body(payload):
            if 'parts' in payload:
                for part in payload['parts']:
                    if part['mimeType'] == 'text/plain' and 'data' in part['body']:
                        return base64.urlsafe_b64decode(part['body']['data']).decode()
                    elif 'parts' in part:
                        result = extract_body(part)
                        if result:
                            return result
            elif 'body' in payload and 'data' in payload['body']:
                return base64.urlsafe_b64decode(payload['body']['data']).decode()
            return ''

        body = extract_body(payload)
        emails.append({'sender': sender, 'subject': subject, 'body': body})

    return emails
