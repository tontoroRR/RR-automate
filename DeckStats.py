import time
import datetime
import easygui
import threading
import yaml

from modules.images import *
from modules.counter import Counter
from modules.gsheet import *
from modules.styles import TopTrophy, MaxCrit, RhandumLeague
from modules.rushroyale_stats import RushRoyaleStats

def get_format():
    with open('setting.yml', 'r') as yml:
        data = yaml.safe_load(yml)
    return data['format']

def set_style():
    with open('setting.yml', 'r') as yml:
        data = yaml.safe_load(yml)
    s = RhandumLeague() #  TopTrophy()
    s.import_from(data['style'])
    return s

def main():
    # 1. catalogue decks of
    #   a. Top Trophy
    #   b. Rhandum League
    #   c. Tournament
    # 2. Summary
    # 3. Do all if no parameters given
    #
    s = set_style()
    f = get_format()

    rr = RushRoyaleStats(s, f)
    # rr.connect_googlesheet()

    # set timer
    chk = []
    lap(chk)

    # connect to Google sheet, then open/create sheet
    ws = None if s.dryrun else connect_sheet(s.style_type)
    lap(chk)
    print(f"Phase1(connecting to Googlesheet): {fmt(chk[-1], chk[-2])} sec.")

    if not s.dryrun:
        _today = datetime.datetime.now().strftime("%Y%m%d")
        ws.prepare_sheet(_today)
        if not s.targets: ws.clear_region()
        ws.update(ws.start_column+"1", [[_today, s.style_type]])
        print(f"Phase2(prepare sheet as of {_today}): {fmt(chk[-1], chk[-2])} sec.")
    lap(chk)

    # open App
    c = Counter(s)
    c.focus_app()
    c.open_ranking()
    lap(chk)
    print(f"Phase3(Open RushRoyale app): {fmt(chk[-1], chk[-2])} sec.")

    log_decks_to_gsheet(c, ws, f)
    lap(chk)
    c.back_to_top()
    print(f"Phase4(Catalogue Decks): {fmt(chk[-1], chk[-2])} sec.")

    # Wrap up
    last_msg = "Completed!!"
    print(f"Total time: {fmt(chk[-1], chk[0])} sec.")
    print(last_msg)
    # easygui.msgbox(lastMsg)
    pass

def connect_sheet(_sheet_type: str) -> Worksheet:
    print("connecting google sheet....")
    _ss = Spreadsheet()
    _sheet_name = f"{datetime.datetime.now().strftime("%Y%m%d")}-{_sheet_type}"
    ws = _ss.get_sheet(_sheet_name) or _ss.create_sheet(_sheet_name)
    print("connected sheet and created '" + _sheet_name + "'!")
    return ws

def lap(chk: list):
    chk.append(time.time())

def fmt(et: float, st: float) -> str:
    return str(round(et - st, 3))

def log_decks_to_gsheet(c: Counter, ws: Worksheet, f:dict):
    ts = []
    s = c.style
    for i, _d in enumerate(c.count()):
        d = [i+1]
        if s.targets and (i+1 not in s.targets): continue
        format = f['normal']
        if len(_d[0]) != 1 or len(_d[1]) != 5:
            d[0] = f"!ERROR! - {d[0]}"
            format = f['error']
        d += ["-"] if len(_d[0]) != 1 else _d[0]
        d += _d[1] + ["-"] * (5 - len(_d[1]))
        if not s.dryrun:
            t = threading.Thread(target=ws.update, args=(ws.start_column + str(i+2), [d], format,))
            t.start()
    for t in ts: t.join() # wait all thread finished

if __name__ == "__main__":
    main()
