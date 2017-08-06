import time
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

try :
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/calendar'
store = file.Storage('storage.json')
creds = store.get()

if not creds or creds.invalid:
    print("make new storage data file ")
    flow = client.flow_from_clientsecrets('client_secret_api.json', SCOPES)
    creds = tools.run_flow(flow, store, flags) \
            if flags else tools.run(flow, store)

DRIVE = build('calendar', 'v3', http=creds.authorize(Http()))
'''
calendarlist = DRIVE.calendarList().list(
    calendarId='primary', maxResults=10, singleEvents=True,
        orderBy='startTime'
)
print(calendarlist)
'''

eventsResult = DRIVE.events().list(
        calendarId='primary', maxResults=10, singleEvents=True,
        orderBy='startTime').execute()
#print(eventsResult['items'])
for item in eventsResult['items'] :
    print(item['summary'])
    print(item['start'])
