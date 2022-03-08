from __future__ import print_function

import datetime
import json
import os.path
from tkinter import X

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/calendar']
# Available_Slots = main()
slots_history = []
def get_credentials():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 7 events on the user's calendar.
    """
    
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret_credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds


def create_file():
    
    creds = get_credentials()
    try:
        service = build('calendar', 'v3', credentials=creds)
        events = service.events().list(calendarId='primary',).execute()
        

        with open ("events.json","w") as file:
            file.write(json.dumps(events["items"],indent=2))


   

    except HttpError as error:
            print('An error occurred: %s' % error)


if __name__ == '__main__':
    create_file()
    

  