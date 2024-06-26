import os
import gspread
import datetime
from oauth2client.service_account import ServiceAccountCredentials as sac
from dotenv import load_dotenv

from modules.utils import Utils

import pdb


class Spreadsheet:
    sheet = None

    def __init__(self, _env: str = '.env'):
        load_dotenv(verbose=True)
        load_dotenv('.env')

        jsonf = os.environ.get('jsonfile')
        sheetKey = os.environ.get('leaderboards_secret_key')
        scope = [
            'https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive',
        ]
        credentials = sac.from_json_keyfile_name(jsonf, scope)
        gc = gspread.authorize(credentials)
        self.sheet = gc.open_by_key(sheetKey)

    def create_sheet(self, name: str):
        try:
            return Worksheet(self.sheet.add_worksheet(
                title=name, rows=306, cols=310, index=0))
        except gspread.exceptions.WorksheetNotFound:
            return False

    def get_sheet(self, name: str):
        try:
            return Worksheet(self.sheet.worksheet(name))
        except gspread.exceptions.WorksheetNotFound:
            return False


class Worksheet:
    ws = None
    start_column = -1
    end_column = -1
    columns = 10
    region = ''
    default_format = {'backgroundColor':
                      {'red': 1.0, 'green': 1.0, 'blue': 1.0}}

    def __init__(self, ws):
        self.ws = ws

    def update(self, range_name, values, format=default_format):
        self.ws.update(range_name=range_name, values=values)
        self.ws.format(range_name, format)

    def clear(self, range):
        self.ws.batch_clear(range)

    def clear_all(self):
        self.ws.clear()

    def find_cell(self, text: str):
        return self.ws.find(text)

    def prepare_sheet(self, dt=None):
        if not dt:
            dt = datetime.datetime.now().strftime('%Y%m%d')
        cellSameDay = self.find_cell(dt)
        if cellSameDay:
            col = cellSameDay.col
            self.start_column = Utils.convert_int_to_col(col)
            self.end_column = Utils.convert_int_to_col(col + self.columns)
        else:
            day = 1
            self.start_column = Utils.convert_int_to_col(
                (day - 1) * self.columns + 1)
            self.end_column = Utils.convert_int_to_col(
                (day - 1) * self.columns + 1 + self.columns
            )
        self.region = (
            self.start_column + '1:' + self.end_column + str(self.ws.row_count)
        )

    def clear_region(self):
        self.clear([self.region])

    def is_empty_cell(self, cell):
        if cell.value == 'None':
            return True
        else:
            return False

    # TODO: 一番最後のカラムを探す
    def find_last_header_col(self):
        for i in range(1, self.ws.col_count, self.columns):
            cell = self.ws.cell(1, i + 1)
            print(self.convert_int_to_col(i))
            if not self.is_empty_cell(cell):
                print(f'not empty cell {cell}')
                return i + self.columns
        return 1
