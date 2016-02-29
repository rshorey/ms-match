import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials
import settings

def get_sheet(credential_file):
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(credential_file, scope)
    sheet_client = gspread.authorize(credentials)
    sheet = sheet_client.open_by_key(settings.sheet_id).sheet1
    return sheet
    

