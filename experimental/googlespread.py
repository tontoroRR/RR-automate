import os
import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv

# 設定ファイルを読み込む
load_dotenv(verbose=True)
load_dotenv(".env")

# ここでjsonfile名と2-2で用意したkeyを入力
jsonf = os.environ.get("jsonfile")
sheet_key = os.environ.get("leaderboards_secret_key")
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]
credentials = ServiceAccountCredentials.from_json_keyfile_name(jsonf, scope)
gc = gspread.authorize(credentials)
sheet = gc.open_by_key(sheet_key)

# (2) Google Spread Sheets上の値を更新
# (２−１)あるセルの値を更新（行と列を指定）
ws = sheet.sheet1
ws.update(range_name="A1", values=[[1, 2, 3, 4]])

"""
ws.update_cell(1,1,"test1")
ws.update_cell(2,1,1)
ws.update_cell(3,1,2)

#(２−２)あるセルの値を更新（ラベルを指定）
ws.update_acell('C1','test2')
ws.update_acell('C2',1)
ws.update_acell('C3',2)

#(2-3)ある範囲のセルの値を更新
ds= ws.range('E1:G3')
ds[0].value = 1
ds[1].value = 2
ds[2].value = 3
ds[3].value = 4
ds[4].value = 5
ds[5].value = 6
ds[6].value = 7
ds[7].value = 8
ds[8].value = 9
ws.update_cells(ds)
"""
