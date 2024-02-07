import time
import datetime
import easygui
import threading

import modules.windows as windows
from modules.images import *
from modules.counter import Counter
from modules.gsheet import *
from modules.styles import TopTrophy, MaxCrit

APPNAME = 'Rush Royale'

def connectSheet() -> Worksheet:
    print("connecting google sheet....")
    ss = Spreadsheet()
    sheetName = datetime.datetime.now().strftime("%Y%m") + "-test"
    ws = ss.getSheet(sheetName) or ss.createSheet(sheetName)
    print("connected sheet and created '" + sheetName + "'!")
    return ws

def fmt(et: int, st: int) -> str:
    return str(round(et - st, 3))

s = TopTrophy() # MaxCrit()
s.lastLine = 84
s.targets = [79]
chk = []

start = time.time()
chk.append(start)

# prepare worksheet
ws = None if s.dryRun else connectSheet()

chk.append(time.time())
print("Phase1(connecting to Googlesheet): " + fmt(chk[-1], chk[-2]) + " sec.")

if not s.dryRun:
    today = datetime.datetime.now().strftime("%Y%m%d")
    ws.prepareSheet(today)
    ws.update(ws.startColumn+"1", [[today, s.styleType]])

chk.append(time.time())
print("Phase2(prepare today's section): " + fmt(chk[-1], chk[-2]) + " sec.")

# Set app
c = Counter()

c.setStyle(s)
c.focusApp()
c.openRanking()

chk.append(time.time())
print("Phase3(open RushRoyale app): " + fmt(chk[-1], chk[-2]) + " sec.")

ts = []
for i, _d in enumerate(c.count()):
    d = [i+1]
    # print("In loop", i+1, s.targets) # for partial log
    if s.targets and (i+1 not in s.targets): continue
    error = len(_d[0]) != 1 or len(_d[1]) != 5
    d += ["-"] if len(_d[0]) != 1 else _d[0]
    d += _d[1] + ["-"] * (5 - len(_d[1]))
    d += ["Error!! Some unit(s) missing"] if error else []
    if not s.dryRun:
        t = threading.Thread(target=ws.update, args=(ws.startColumn + str(i+2), [d],))
        t.start()

for t in ts: t.join() # wait all thread finished
c.backToTop()

chk.append(time.time())
print("Phase4(catalogue decks): " + fmt(chk[-1], chk[-2]) + " sec.")

lastMsg = "Completed!!"
print("Total time: " + fmt(chk[-1], chk[0]) + " sec.")
print(lastMsg)
# easygui.msgbox(lastMsg)
