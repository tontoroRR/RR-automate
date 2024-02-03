import os
import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv

class Spreadsheet:
    sheet = None

    def __init__(self):
        load_dotenv(verbose=True)
        load_dotenv(".env")

        jsonf = os.environ.get('jsonfile')
        sheet_key = os.environ.get('leaderboards_secret_key')
        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(jsonf, scope)
        gc = gspread.authorize(credentials)
        self.sheet = gc.open_by_key(sheet_key)

    def createSheet(self, name: str):
        try:
            return Worksheet(self.sheet.add_worksheet(title=name, rows=306, cols=310))
        except gspread.exceptions.WorksheetNotFound:
            return False

    def getSheet(self, name: str):
        try:
            return Worksheet(self.sheet.worksheet(name))
        except gspread.exceptions.WorksheetNotFound:
            return False

class Worksheet:
    ws = None

    def __init__(self, ws):
        self.ws = ws
    
    def update(self, range_name, values):
        self.ws.update(range_name=range_name, values=values)
    
    def clear(self, range):
        self.ws.batch_clear(range)
    
    def clearAll(self):
        self.ws.clear()
