import os
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

SCOPES = 'https://www.googleapis.com/auth/spreadsheets'

def authenticate():
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    return build('sheets', 'v4', http=creds.authorize(Http()))

service = authenticate()
SPREADSHEET_ID = os.environ['SHEET_ID']


def get_item_codes():
    range_name = 'A2:A'
    result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
                                                range=range_name).execute()
    values = result.get('values', [])
    item_codes = []

    if not values:
        print('No data found.')
    else:
        for row in values:
            code = row[0]
            item_codes.append(code)
    return item_codes


def write_to_sheet(values):
    range_name = 'B2:B'
    body = {
        'values': values
    }
    result = service.spreadsheets().values().update(
      spreadsheetId=SPREADSHEET_ID, range=range_name,
      valueInputOption='RAW', body=body).execute()