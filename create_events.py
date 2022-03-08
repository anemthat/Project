

from __future__ import print_function
from asyncio import events
from calendar import calendar

import datetime
# import email
# import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from pathlib  import Path
from calendar_table import *


def create_volunteer():
    SCOPES = ['https://www.googleapis.com/auth/calendar']
    API_NAME = 'calendar'
    API_VERSION = 'v3'

    token_path = Path.cwd() /"token.json"


    creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    service = build( API_NAME,API_VERSION, credentials = creds)
    Description = input('what do you need help with: ')
    date = input('enter the date of the event: ')
    start_time = input('enter the start time of the event: ')

    e = datetime.datetime.strptime(start_time, '%H:%M')
    end_time = (e + datetime.timedelta(minutes=30)).strftime('%H:%M')
    # end_time = input('enter the end time of event(event should be 30 minutes: ')
    location = input('enter your preferred location: ')

    event = {
      'summary': Description,
      'location': location ,
      'description': 'Tutoring  .',
      'colorId' : 5,
      'visibility': 'public',
      'start': { 
        'dateTime': f'{date}T{start_time}:00+02:00',  #2022-05-28T09:00:00+02:00',
        'timeZone': 'Africa/Johannesburg',
      },
      'end': {
        'dateTime': f'{date}T{end_time}:00+02:00',  #2022-05-28T09:30:00+02:00',
        'timeZone': 'Africa/Johannesburg',
      },
                
        #  {'email': 'sbrin@example.com'},
      
      
    }
    
    calendar_id = 'primary'



    response = service.events().insert(
      calendarId = calendar_id, body = event).execute()

    print (f'Event created: {response}')
    create_file()

if __name__ == '__main__':
    create_volunteer()