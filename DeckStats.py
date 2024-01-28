import time
import windows
from images import *
from counter import Counter


APPNAME = 'Rush Royale'
LOCATION = (1275, 2, 647, 1020)
# LOCATION_L = (1275, 2, 647, 4200)

heroCounts = {h: 0 for h in HeroImage.all}

def findAny(ary, counts):
    res = []
    for img in ary:
        if exists(img): counts[img] += 1
    return res

def countHero():
    pyautogui.click(pyautogui.position())
    res = findAny(HeroImage.all, heroCounts)
    click(BtnImage.close)
    return res

# make RR screen to front and fix position
def activateRR():
    windows.moveApp(APPNAME, LOCATION)
    time.sleep(0.2)
    windows.activateApp(APPNAME)
    time.sleep(0.2)

def countLeaderBoard(img):
    if exists(img):
        moveTo(img)
        pyautogui.move(0, 215)
        first_pos = pyautogui.position()
        pyautogui.PAUSE = 0.1
        for s in range(1):
            for l in range(7):
                pos = pyautogui.position()
                res = countHero()
                pyautogui.moveTo(pos)
                if l == 6:
                    pyautogui.scroll(68*7)
                    pyautogui.moveTo(first_pos)
                else:
                    pyautogui.move(0, 68)
                time.sleep(0.3)

    print(heroCounts)
    pyautogui.PAUSE = 0.1

class Style:
    pass
    menu = BtnImage.menuWithInfo
    lbBtn = BtnImage.leaderBoards
    tab = BtnImage.maxCritTab
    banner = LabelImage.maxCrit #totalTrophy
    wait = 1 # wait for 1 sec
    pause = 0.2
    location = LOCATION
    rowHeight = 68
    heros = HeroImage.all
    units = UnitImage.all

s = Style()

activateRR()
c = Counter().setStyle(s)
c.openRanking()
c.count()
