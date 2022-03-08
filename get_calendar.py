from __future__ import print_function
from asyncio import events

import datetime
from distutils.log import error
# import email
import os.path
from tkinter import X
from create_events import *
from calendar_table import *


from prettytable import PrettyTable


from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/calendar']
# Available_Slots = main()

events_data = []
serv = []

def     generate_token():
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

    # try:
    service = build('calendar', 'v3', credentials=creds)
    serv.append(service)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    print('Getting events for the upcoming 7 days')
    
    events_result = service.events().list(calendarId='synigency@gmail.com', timeMin=now,
                                          maxResults=10, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
        print("\ncreate events\n")
        create_volunteer()
        return


    myTable = PrettyTable(["Event_id", "Email", "Date", "Start_time",])
    

    events_data.append(events)

    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
       
        myTable.add_row([event['id'], event['creator']['email'], event['start']['dateTime'][:10], event['start']['dateTime'][11:]])
        
    print(myTable)
    
def delete_token():
    T_D = "token.json"
    if os.path.exists(T_D):
        os.remove(T_D)



def get_id():
    
    date = input("Enter date: ")
    time =  input("Enter time: ")

    for t in events_data:
        for event in t:
            start_date = event["start"].get("dateTime")[:10]
            start_time = event["start"].get("dateTime")[11:16]
            if date == start_date and time == start_time:
                return event["id"]
    
def booking(id, email):

    id= get_id() 
   
    event = serv[0].events().get(calendarId='synigency@gmail.com', eventId=id).execute()
    try:
        if len(event["attendees"][0].get("email"))!=0:
            print("slot already booked")

            
    except KeyError:
            event["attendees"] = email

            updated_event = serv[0].events().patch(calendarId='synigency@gmail.com', eventId=event['id'], body={"attendees":[{'email': email}]}).execute()
            print("Successfully Booked")
            create_file()
            print(updated_event)
            return

        
def cancel_booking(id):
    id= get_id()
    event = serv[0].events().get(calendarId='synigency@gmail.com', eventId=id).execute()
    try:
        event['attendees']
        event["attendees"]= 'open slots'
        updated_event= serv[0].events().patch(calendarId='synigency@gmail.com', eventId= event["id"], body=event).execute()
        print('The Booking has been cancelled')
        create_file()
        print(updated_event)
    
    except KeyError:
        print (" There slot is empty, you can not cancel")
        return "","",""
        


if __name__ == '__main__':
    generate_token()
    id_ = input('id: ')
    email_ = input('email:')
    booking(id_,email_)
    cancel_booking(id)

       

  