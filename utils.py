import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials
import settings
import uuid

def get_sheet(credential_file):
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(credential_file, scope)
    sheet_client = gspread.authorize(credentials)
    sheet = sheet_client.open_by_key(settings.sheet_id).sheet1
    return sheet


def populate_ids(credential_file):
    sheet = get_sheet(credential_file)
    #sheets are 1-indexed, so row 1 is the header row
    id_index = sheet.row_values(1).index('ID')+1
    row_num = 1
    for row in sheet.get_all_records():
        row_num += 1

        if row['Name'] and not row['ID']:
            row_id = uuid.uuid4()
            sheet.update_cell(row_num, id_index, row_id)


def populate_lat_long():
    #TODO cron job to populate lat/long cols of sheet
    pass