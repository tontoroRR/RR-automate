import time
import windows
from images import *
from counter import Counter


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
    wait = 1 # wait for 1 sec
    pause = 0.2
    location = LOCATION
    lineHeight = 68
    linesInPage = 7
    lastLine = 1
    heros = HeroImage.all
    units = UnitImage.all

s = Style()

start = time.time()
activateRR()
c = Counter().setStyle(s)
c.openRanking()
ds = c.count()
c.backToTop()
for d in ds:
    print(d)

for d in ds:
    if len(d[1]) != 1 or len(d[2]) != 5:
        print(error, d)

print(time.time() - start)
