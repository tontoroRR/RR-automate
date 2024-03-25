import time
import datetime
import yaml
from importlib import import_module

from modules.counter import Counter
from modules.gsheet import Worksheet, Spreadsheet
from modules.utils import Utils as ut
from modules.rushroyale_stats import RushRoyaleStats

# import pdb


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


def set_style(_rr: RushRoyaleStats = None):
    # for rust royale
    with open('setting.yml', 'r') as _yml:
        _d = yaml.safe_load(_yml)
    _m = import_module('modules.styles')
    style = getattr(_m, _d['style']['target_module'])()
    style.import_from(_d['style'])
    style.units, style.heroes = _rr.units, _rr.heroes
    return style


def main():
    rr = RushRoyaleStats()
    rr.setup()
    s, f = set_style(rr), get_format()
    # parser = set_argument_parser()

    print(f"Start to catalogue {s.style_type} deck")

    # set timer
    chk = lap()
    # connect to Google sheet, then open/create sheet
    _now = datetime.datetime.now().strftime("%Y%m%d %H%M")
    if not s.use_sec:
        _now = datetime.datetime.now().strftime("%Y%m%d")
    ws = None if s.dryrun else connect_sheet(s.style_type, _now)
    lap(chk)

    print(f"Phase1(connecting to Googlesheet): {fmt_l(chk)} sec.")

    if not s.dryrun:
        ws.prepare_sheet(_now)
        if not s.lines_only:
            ws.clear_region()
        ws.update(ws.start_column+"1", [[_now, s.style_type]])
        lap(chk)
        print(f"Phase2(prepare sheet as of {_now}): {fmt_l(chk)} sec.")

    # open App
    try:
        c = Counter(s)
        c.focus_app()
        c.open_ranking()
        lap(chk)
        print(f"Phase3(Open RushRoyale app): {fmt_l(chk)} sec.")
        (error_count, all_decks) = log_decks_to_gsheet(c, ws, f)
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


def connect_sheet(_sheet_type: str, _now: str) -> Worksheet:
    print("connecting google sheet....")
    _ss = Spreadsheet()
    _sheet_name = f"{_now}-{_sheet_type}"
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


def log_decks_to_gsheet(c: Counter, ws: Worksheet, _f: dict) -> (int, list):
    error_count, _s, _ln = 0, c.style, 0
    _all_for_gsheet, all_deck = [], []
    if not _s.dryrun:
        ws.update(f"{ws.start_column}2", _s.title_deck_table)
    try:
        for _i, _d in enumerate(c.count()):
            # pdb.set_trace()
            _ln = _i + 1
            _deck = [_ln]
            if _s.lines_only and (_ln not in _s.lines_only):
                continue
            if len(_d[0]) != 1 or len(_d[1]) != 5:
                error_count += 1
                _deck[0] = f"!ERROR! - {_deck[0]}"
            all_deck.append([_deck[0], _d[0], _d[1]])
            _deck += [str(_e) for _e in (["-"] if len(_d[0]) != 1 else _d[0])]
            _deck += [str(_e) for _e in _d[1] + ["-"] * (5 - len(_d[1]))]
            print(_deck)
            _all_for_gsheet.append(_deck)
        if not _s.dryrun:
            ws.update(ws.start_column + '3', _all_for_gsheet)
    except Exception as e:
        ut.log_exception(_ln)
        raise e
    return (error_count, all_deck)


if __name__ == "__main__":
    main()
