import time
import datetime
# import easygui
import threading
import yaml
from importlib import import_module
# import argparse

from modules.counter import Counter
from modules.gsheet import Worksheet, Spreadsheet
from modules.utils import Utils as ut
# from modules.rushroyale_stats import RushRoyaleStats

import pdb


def set_argument_parser():
    pass
    """
    _parser = argparse.ArgumentParser()
    return _parser
    """


def get_format():
    # for google spreadsheet
    data = None
    with open('setting.yml', 'r') as _yml:
        data = yaml.safe_load(_yml)['format']
    return data


def set_style():
    # for rust royale
    with open('setting.yml', 'r') as _yml:
        _d = yaml.safe_load(_yml)
    _m = import_module('modules.styles')
    style = getattr(_m, _d['style']['target_module'])()
    style.import_from(_d['style'])
    return style


def main():
    s, f = set_style(), get_format()
    # parser = set_argument_parser()
    # rr = RushRoyaleStats()
    # pdb.set_trace()

    print(f"Start to catalogue {s.style_type} deck")

    # set timer
    chk = lap()
    # pdb.set_trace()

    # connect to Google sheet, then open/create sheet
    ws = None if s.dryrun else connect_sheet(s.style_type)
    lap(chk)

    print(f"Phase1(connecting to Googlesheet): {fmt_l(chk)} sec.")

    if not s.dryrun:
        _today = datetime.datetime.now().strftime("%Y%m%d")
        ws.prepare_sheet(_today)
        if not s.lines_only:
            ws.clear_region()
        ws.update(ws.start_column+"1", [[_today, s.style_type]])
        print(f"Phase2(prepare sheet as of {_today}): {fmt_l(chk)} sec.")
    lap(chk)

    # open App
    try:
        c = Counter(s)
        c.focus_app()
        c.open_ranking()
        lap(chk)
        print(f"Phase3(Open RushRoyale app): {fmt_l(chk)} sec.")
        error_count = log_decks_to_gsheet(c, ws, f)
        lap(chk)
        c.back_to_top()
        print(f"Phase4(Catalogue Decks): {fmt_l(chk)} sec.")
        if 0 < error_count:
            print(f"\033[33mError count: \033[41m{error_count}\033[0m")
        else:
            print("\033[36mNo error found\033[0m")
    except Exception as e:
        ut.log_exception()
        raise e

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


def lap(chk: list = []):
    chk.append(time.time())
    return chk


def fmt_l(chk: list) -> str:
    return fmt(chk[-1], chk[-2])


def fmt(et: float, st: float) -> str:
    return str(round(et - st, 3))


def log_decks_to_gsheet(c: Counter, ws: Worksheet, _f: dict):
    error_count, ts, _s, _ln = 0, [], c.style, 0
    # ts = []
    # _s = c.style
    # _ln = 0
    if not _s.dryrun:
        ws.update(f"{ws.start_column}2", _s.title_deck_table)
    try:
        for _i, _d in enumerate(c.count()):
            _ln = _i + 1
            _deck = [_ln]
            if _s.lines_only and (_ln not in _s.lines_only):
                continue
            _format = _f['normal']
            if len(_d[0]) != 1 or len(_d[1]) != 5:
                error_count += 1
                _deck[0], _format = f"!ERROR! - {_deck[0]}", _f['error']
            _deck += ["-"] if len(_d[0]) != 1 else _d[0]
            _deck += _d[1] + ["-"] * (5 - len(_d[1]))
            print(_deck)
            if not _s.dryrun:
                _t = threading.Thread(
                    target=ws.update,
                    args=(ws.start_column + str(_ln+2), [_deck], _format,))
                _t.start()
                ts.append(_t)
    except Exception as e:
        ut.log_exception(_ln)
        raise e
    for t in ts:
        t.join()
    return error_count


if __name__ == "__main__":
    main()
