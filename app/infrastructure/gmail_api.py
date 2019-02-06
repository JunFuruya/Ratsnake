# -*- coding: UTF-8 -*-

from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from app.infrastructure.base_api import BaseApi

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

'''
Gmail Api module
'''
class GmailApi(BaseApi):
    def __init__(self):
        dirpath = os.path.abspath('./resources/gmail/credentials.json')
        flow = InstalledAppFlow.from_client_secrets_file(dirpath, SCOPES)
        creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

        self.__service = build('gmail', 'v1', credentials=creds)

        pass
    
    def get_mails_by_label(self, label):
        # Call the Gmail API
        results = self.__service.users().messages().list(userId='me', labelIds=['Label_3322926682986175335']).execute()
        labels = results.get('messages', [])
       	return labels if labels else None
