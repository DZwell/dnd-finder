import os
import json


def set_creds(creds_file):
    creds = {}
    creds['site'] = input('Website: ')
    creds['username'] = input('Username: ')
    creds['password'] = input('Password: ')
    creds['sheet_id'] = input('Sheet Id: ')
    json.dump(creds, creds_file)
    creds_file.close()


def get_creds(creds_file):
    if creds_file.closed or not creds_file.readable():
        open(creds_file, 'r')
    creds_file.seek(0)
    creds = json.load(creds_file)
    creds_file.close()
    return creds
