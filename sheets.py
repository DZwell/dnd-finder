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


def get_item_codes(spreadsheet_id):
    service = authenticate()
    range_name = 'A2:A12'
    result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id,
                                                range=range_name).execute()
    values = result.get('values', [])
    item_codes = []

    if not values:
        print('No data found.')
    else:
        for row in values:
            if row:
                code = row[0]
                item_codes.append(code)
    print('Reading {} item codes from spreadsheet\n'.format(len(item_codes)))
    return item_codes


def write_to_sheet(values):
    range_name = 'Alliance project!C2:G'
    body = {
        'values': values,
        'majorDimension': 'ROWS',
    }
    result = service.spreadsheets().values().update(
      spreadsheetId=spreadsheet_id, range=range_name,
      valueInputOption='RAW', body=body).execute()