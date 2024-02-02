import time
import datetime
import easygui

import modules.windows as windows
from modules.images import *
from modules.counter import Counter
from modules.gsheet import *

APPNAME = 'Rush Royale'
LOCATION = (1275, 2, 647, 1020)
# LOCATION_L = (1275, 2, 647, 4200)

# make RR screen to front and fix position
def activateRR():
    windows.moveApp(APPNAME, LOCATION)
    time.sleep(0.2)
    windows.activateApp(APPNAME)
    time.sleep(0.2)

class Style:
    menu = BtnImage.menuWithInfo
    battleBtn = BtnImage.bottomBattle
    lbBtn = BtnImage.leaderBoards
    tab = BtnImage.maxCritTab
    banner = LabelImage.maxCrit #totalTrophy
    badge1st = LabelImage.maxCritBadge1st
    cards = LabelImage.cards
    wait = 1 # wait for 1 sec
    pause = 0.2
    location = LOCATION
    lineHeight = 67
    linesInPage = 7
    lastLine = 10
    heros = HeroImage.all
    units = UnitImage.all

s = Style()

activateRR()
c = Counter()
c.setStyle(s)
c.openRanking()

ds = c.count()
c.backToTop()

path = datetime.datetime.now().strftime("%Y%m%d-%H%M%S.csv")

# create google sheet
name = datetime.datetime.now().strftime("%Y%m%d")
ss = Spreadsheet()
ws = ss.getSheet(name) or ss.createSheet(name)

with open(path, mode='x') as f:
    l = 1
    for _d in ds:
        d = []
        for e in _d:
            d += e if type(e).__name__ == 'list' else [e]
        if len(_d[1]) != 1 or len(_d[2]) != 5: d += ["error"]
        d = list(map(str, d))
        ws.update("A" + str(l), [d])
        l += 1
        # f.write(",".join(d) + "\n")
            
# easygui.msgbox("データ取得完了!")
