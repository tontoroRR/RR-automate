import os
import gspread
import json
import datetime
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv

from modules.utils import Utils

import pdb

class Spreadsheet:
    sheet = None

    def __init__(self):
        load_dotenv(verbose=True)
        load_dotenv(".env")

        jsonf = os.environ.get('jsonfile')
        sheetKey = os.environ.get('leaderboards_secret_key')
        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(jsonf, scope)
        gc = gspread.authorize(credentials)
        self.sheet = gc.open_by_key(sheetKey)

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
    startColumn = -1
    endColumn = -1
    columns = 10
    region = ""


    def __init__(self, ws):
        self.ws = ws
    
    def update(self, range_name, values):
        self.ws.update(range_name=range_name, values=values)
    
    def clear(self, range):
        self.ws.batch_clear(range)
    
    def clearAll(self):
        self.ws.clear()

    def findCell(self, text: str):
        return self.ws.find(text)

    def prepareSheet(self, dt = None):
        if not dt:
            dt = datetime.datetime.now().strftime("%Y%m%d")
        cellSameDay = self.findCell(dt)
        if cellSameDay:
            col = cellSameDay.col
            self.startColumn = Utils.convertIntToCol(col)
            self.endColumn = Utils.convertIntToCol(col + self.columns)
        else:
            day = 1
            self.startColumn = Utils.convertIntToCol((day - 1) * self.columns + 1)
            self.endColumn = Utils.convertIntToCol((day - 1) * self.columns + 1 + self.columns)
        self.region = self.startColumn + "1:" + self.endColumn + str(self.ws.row_count)
        self.clear([self.region])

    def isEmptyCell(self, cell):
        if cell.value == "None":
            return True
        else:
            return False

    def findLastHeaderCol(self):
        for i in range(1, self.ws.col_count, self.columns):
            # pdb.set_trace()
            cell = self.ws.cell(1, i+1)
            print(self.convertIntToCol(i))
            if not self.isEmptyCell(cell):
                print("not empty cell", cell)
                return i + self.columns
        return 1


