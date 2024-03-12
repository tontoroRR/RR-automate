import time
import pyautogui
from ctypes import windll

from typing import overload

import threading
from collections import deque

from modules.styles import Style
from modules.utils import Utils as ut

import pdb

pyautogui.PAUSE = 0.2


class Counter:
    style = None
    op = None
    card_y = 565
    _line_num = 0
    cards_region = None

    def __init__(self, _s: Style = None):
        self.op = Operation()
        if _s:
            self.set_style(_s)
            self.op.set_style(_s)

    def focus_app(self, _region=None, _app_name: set = None):
        (left, top, width, height) = _region or self.style.app_region
        h = windll.user32.FindWindowW(0, _app_name or self.style.app_name)
        windll.user32.MoveWindow(h, left, top, width, height)
        self.op.sleep(0.2)
        windll.user32.SetForegroundWindow(h)
        self.op.sleep(0.2)

    def set_style(self, _style):
        self.style = _style

    def open_ranking(self):
        for btn in self.style.buttonSeq:
            self.op.exist_click(btn, 1)
        self.op.wait(self.style.badge1st, 5)
        _x = pyautogui.position()[0]
        _y = self.op.get_center(self.style.badge1st)[1]
        self.op.first_line_pos = (_x, _y)
        self.op.moveTo_first_line()
        if self.style.special_operation():
            print(self.style.special_operation())

    def _unique(self, _units: list):
        _units = list(set(_units))
        _maxed = [_u.replace("(Max)", "") for _u in _units if "Max" in _u]
        return [_u for _u in _units if _u not in _maxed]

    def _find_cards(self, _dict: dict, _count: int) -> list:
        _cards, _retry, _save_confidence = [], 0, self.op.CONFIDENCE
        for _retry in range(3):
            _cards = self._unique([
                _dict[k]
                for k in self.op.find_any_thread(list(_dict.keys()))
            ])
            if len(_cards) == _count:
                break
            else:
                print(f"\033[33mMissing some: \033[41m{_cards}\033[0m")
            self.op.CONFIDENCE -= 0.1
        if 0 < _retry:
            print(f"\033[33mError count: \033[41m{_retry}\033[0m")
        self.op.CONFIDENCE = _save_confidence
        return _cards

    def _get_user_deck(self):
        _save_region = self.op.REGION
        self.op.set_region(self.cards_region or self.style.app_region)
        hero = self._find_cards(self.style.heros, 1)
        units = self._find_cards(self.style.units, 5)
        self.op.set_region(_save_region)
        if len(hero) != 1 or len(units) != 5:
            ut.take_screenshot(self._line_num, _region=self.style.app_region)
        return (hero, sorted(units))

    def _open_profile(self):
        pyautogui.click()
        if self.style.card_tab:
            _pos = pyautogui.position()
            self.op.exist_click(self.style.card_tab, 1)
            pyautogui.moveTo(_pos)
        _xy = self.op.wait(self.style.cards, 2)
        if _xy is not None:
            _cur_xy = self.op.drag_image_to(-1, self.card_y, _xy)
            (_dx, _dy, _w, _h) = self.style.cards_region
            self.cards_region = (_cur_xy[0] + _dx, _cur_xy[1] + _dy, _w, _h)
        else:
            print(f"{self.style.cards} NOT FOUND")

    def count(self):
        cur_l = 1
        plus_ls = 0
        for _n in range(1, self.style.total_line + 1):
            self._line_num = _n
            cur_l = self._line_num % self.style.lines_per_page
            if cur_l == 0:
                cur_l = self.style.lines_per_page
            cur_l = cur_l + plus_ls
            # 1. get deck
            if all(
                [
                    len(self.style.lines_only),
                    (self._line_num not in self.style.lines_only),
                ]
            ):
                yield ([])
            elif self.style.dryrun:
                yield ((["hero"], ["unit", "unit", "unit", "unit", "unit"]))
            else:
                self._open_profile()
                self.op.sleep(0.5)
                _save_xy = pyautogui.position()
                pyautogui.moveTo((_save_xy[0], 0))
                yield (self._get_user_deck())
                pyautogui.moveTo(_save_xy)
                pyautogui.press("esc")
            # 2. move or scroll up
            if cur_l < self.style.lines_per_page:
                self.op.moveTo_line_n(cur_l + 1)
            elif self._line_num == self.style.total_line:
                pass
            else:
                # 3. scroll up if at last line of page
                ls_remained = self.style.total_line - self._line_num
                if self.style.lines_per_page <= ls_remained:
                    self.op.scrollup_slow(self.style.lines_per_page)
                    self.op.moveTo_first_line()
                else:
                    self.op.scrollup_slow(ls_remained)
                    plus_ls = self.style.lines_per_page - ls_remained
                    self.op.moveTo_line_n(
                        self.style.lines_per_page - ls_remained + 1
                    )
            if self._line_num == self.style.total_line:
                self.op.sleep(self.style.sleep_at_end)

    def back_to_top(self):
        while not (self.op.exists(self.style.btn_battle)):
            pyautogui.press("esc")


class Operation:
    WTA = 1  # wait_time_adjust
    WAIT = 0.1
    LONG_WAIT = 10
    CONFIDENCE = 0.9
    DEBUG = False
    TOOLOW = 600
    REGION = None
    first_line_pos = (-1, -1)
    line_height = 0
    adjust_scroll_up = 0
    do_scroll_not_found = False

    def __init__(self):
        pass

    def __dp(self, *values: object):
        if self.DEBUG:
            print(values)

    def sleep(self, _count: int, _wta: int = WTA):
        time.sleep(_count * _wta)

    @overload
    def __los(self, _img: list, _region=REGION):
        pass

    @overload
    def __los(self, _img: str, _region=REGION):
        pass

    def __los(self, _img, _region=REGION):
        xy = None
        _imgs = _img if isinstance(_img, list) else [_img]
        for _img in _imgs:
            try:
                xy = pyautogui.locateOnScreen(
                    _img, region=_region, confidence=self.CONFIDENCE
                )
                if xy is not None:
                    break
            except pyautogui.ImageNotFoundException:
                pass
        if xy is not None:
            return xy
        else:
            raise pyautogui.ImageNotFoundException(_imgs, _img)

    def __exists(self, _img: str, _wait=WAIT, _region=REGION) -> bool:
        _wait = _wait * self.WTA
        self.__dp(_wait)
        for _i in range(int(_wait * 10)):
            try:
                xy = self.__los(_img, _region)
                self.__dp(_img, f" found at {xy}")
                return True
            except pyautogui.ImageNotFoundException:
                self.__dp(_img, f" not found {_i}")
                pass
        return False

    def __click(self, _img: str, _shift: tuple = (0, 0)):
        try:
            xy = self.__los(_img)
            pos = pyautogui.center(xy)
            pyautogui.click(pos.x + _shift[0], pos.y + _shift[1])
        except pyautogui.useImageNotFoundException:
            self.__dp(_img, " not found in click")
            raise pyautogui.useImageNotFoundException

    @overload
    def wait(self, _img: str, _wait=LONG_WAIT) -> ((int, int), str):
        pass

    @overload
    def wait(self, _img: list, _wait=LONG_WAIT) -> ((int, int), str):
        pass

    def wait(self, _img, _wait=LONG_WAIT) -> ((int, int), str):
        _wait = _wait * self.WTA
        _imgs = _img if isinstance(_img, list) else [_img]
        xy = None
        for _img in _imgs:
            start = time.time()
            is_timeout = False
            while xy is None and not is_timeout:
                try:
                    xy = self.__los(_img)
                    if xy is not None:
                        break
                except pyautogui.ImageNotFoundException:
                    pass
                if (time.time() - start) > _wait:
                    self.__dp("not found ", _img, " after ", _wait, "(s)")
                    is_timeout = True
        return pyautogui.center(xy) if xy else None

    @overload
    def exists(self, _img: str, _wait: float = WAIT) -> bool:
        pass

    @overload
    def exists(self, _img: list, _wait: float = WAIT) -> bool:
        pass

    def exists(self, _img, _wait: float = WAIT) -> bool:
        res = False
        _imgs = _img if isinstance(_img, list) else [_img]
        for _img in _imgs:
            try:
                res = res or self.__exists(_img, _wait)
                if res:
                    return res
            except Exception as e:
                print(e)
        return res

    @overload
    def exist_click(self,
                    _img: list,
                    _wait: float = WAIT,
                    _shift: tuple = (0, 0)):
        pass

    @overload
    def exist_click(self,
                    _img: str,
                    _wait: float = WAIT,
                    _shift: tuple = (0, 0)):
        pass

    def exist_click(self, _img, _wait: float = WAIT, _shift: tuple = (0, 0)):
        _imgs = _img if isinstance(_img, list) else [_img]
        es = []
        for _img in _imgs:
            try:
                if self.__exists(_img, _wait):
                    self.__click(_img, _shift)
                    return
            except Exception as e:
                es.append(e)
        raise Exception(es)

    def drag_image_to(self,
                      _x: int = -1,
                      _y: int = -1,
                      _xy: (int, int) = None) -> (int, int):
        start_pos = pyautogui.position()
        if _xy[1] <= self.TOOLOW:
            return _xy
        else:
            _x = _xy[0] if (_x == -1) else _x
            _y = _xy[1] if (_y == -1) else _y
            pyautogui.mouseDown(_xy)
            pyautogui.moveTo(_x, _y, 0.3 * self.WTA)
            self.sleep(0.3)
            pyautogui.mouseUp()
            res = pyautogui.position()
            pyautogui.moveTo(start_pos)
            return res

    def scrollup_slow(self, lines: int):
        dy = -1 * int(self.line_height * lines * (1 + self.adjust_scroll_up / (self.WTA * 0.4)))
        pyautogui.mouseDown()
        self.sleep(0.2)
        pyautogui.move(0, dy, 0.6 * self.WTA)  # , pyautogui.easeInQuad)
        self.sleep(0.35)
        pyautogui.mouseUp()

    @overload
    def find_any_thread(self, _img: list, _wait: float = WAIT) -> list:
        pass

    @overload
    def find_any_thread(self, _img: str, _wait: float = WAIT) -> list:
        pass

    def find_any_thread(self, _img, _wait: float = WAIT) -> list:
        _imgs = _img if isinstance(_img, list) else [_img]

        def find_worker(_i: str, _d: list):
            if self.__exists(_i, _wait, self.REGION):
                _d[_i] = 1

        ts, q = [], deque()
        for _i in _imgs:
            q.append({_i: 0})
        for _d in q:
            _i = list(_d.keys())[0]
            t = threading.Thread(
                target=find_worker,
                args=(_i, _d, ),
                daemon=True,
            )
            t.start()
            ts.append(t)
        for t in ts:
            t.join()
        res = []
        for _d in q:
            for k, v in _d.items():
                if v > 0:
                    res.append(k)
        return res

    def get_top_left(self, _img):
        return None
        xywh = self.__los(_img)
        (x, y) = (xywh[0], xywh[1])
        return (x, y)

    def get_bottom_right(self, _img):
        return None

    def get_center(self, _img):
        xy = pyautogui.center(self.__los(_img))
        return xy

    def moveTo_line_n(self, n: int):
        diff = self.line_height * (n - 1)
        (x, y) = self.first_line_pos
        y += diff
        pyautogui.moveTo(x, y)

    def moveTo_first_line(self):
        self.moveTo_line_n(1)

    def set_region(self, _region):
        self.REGION = _region

    def set_style(self, _style):
        self.WAIT = _style.wait
        self.WTA = _style.wait_time_adjust
        self.DEBUG = _style.DEBUG
        self.line_height = _style.line_height
        self.adjust_scroll_up = _style.adjust_scroll_up
        self.set_region(_style.app_region)
