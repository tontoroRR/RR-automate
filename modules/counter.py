import time
import pyautogui
import ctypes

import asyncio
import threading
from collections import deque

from modules.styles import Style
from modules.images import UnitConverter as uc

import pdb

pyautogui.PAUSE = 0.2

class Counter:
    style = None
    op = None
    card_y = 565

    def convert(self, ary: list):
        l = list(map(uc.convert_img_to_name, ary))
        return list(set(l))

    def __init__(self, s: Style = None):
        self.op = Operation()
        if s:
            self.set_style(s)
            self.op.line_height = s.line_height
            self.op.adjust_scroll_up = s.adjust_scroll_up

    def focus_app(self):
        (left, top, width, height) = self.style.location
        h = ctypes.windll.user32.FindWindowW(0, self.style.app_name)
        ctypes.windll.user32.MoveWindow(h, left, top, width, height)
        time.sleep(0.2)
        ctypes.windll.user32.SetForegroundWindow(h)
        time.sleep(0.2)

    def set_style(self, _style):
        self.style = _style
        self.op.set_location(self.style.location)
        self.op.set_wait(self.style.wait)

    def open_ranking(self):
        for btn in self.style.buttonSeq:
            if isinstance(btn, list):
                res = self.op.find_any_thread(btn)
                if res: self.op.exist_click(res.pop(), 1)
            else:
                self.op.exist_click(btn, 1)
        self.op.wait(self.style.badge1st, 1)
        x = pyautogui.position()[0]
        y = self.op.get_center(self.style.badge1st)[1]
        self.op.first_line_pos= (x, y)
        self.op.moveTo_first_line()
        if self.style.special_operation():
            print(self.style.special_operation())

    def get_user_deck(self):
        hero = []
        units = []
        hero = self.convert(self.op.find_any_thread(self.style.heros))
        units = self.convert(self.op.find_any_thread(self.style.units))
        return (hero, sorted(units))

    def click_top100_for_RL(self):
        pass

    def open_and_get_deck(self):
        pass

    def count(self):
        cur_line = 1
        plus_lines = 0
        for _n in range(1, self.style.total_line + 1):
            pos_y = pyautogui.position()[1]
            cur_line = _n % self.style.lines_per_page
            if cur_line == 0:
                cur_line = self.style.lines_per_page
            old_cur_line = cur_line
            cur_line = cur_line + plus_lines
            print(_n, pos_y, old_cur_line, cur_line, plus_lines)
            # first get deck
            if 0 < len(self.style.lines_only) and (_n not in self.style.lines_only):
                yield([])
            elif self.style.dryrun:
                yield((['hero'], ['unit1', 'unit2', 'unit3', 'unit4', 'unit5']))
            else:
                pyautogui.click()
                if self.style.card_tab:
                    _pos = pyautogui.position()
                    self.op.exist_click(self.style.card_tab, 1)
                    pyautogui.moveTo(_pos)
                self.op.drag_image_to(-1, self.card_y, self.style.cards)
                yield(self.get_user_deck())
                pyautogui.press('esc')
            # next, move or scroll up
            if cur_line < self.style.lines_per_page:
                pyautogui.move(0, self.style.line_height)
            elif _n == self.style.total_line:
                pass
            else:
                lines_remained = self.style.total_line - _n
                print(_n, pos_y, cur_line, lines_remained)
                if self.style.lines_per_page <= lines_remained:
                    self.op.scrollup_slow(self.style.lines_per_page)
                    self.op.moveTo_first_line()
                else:
                    self.op.scrollup_slow(lines_remained)
                    self.op.moveTo_line_n(self.style.lines_per_page - lines_remained + 1)
                    plus_lines = self.style.lines_per_page - lines_remained
            if (_n == self.style.total_line): time.sleep(5)

    def back_to_top(self):
        while not(self.op.exists(self.style.btn_battle)):
            pyautogui.press('esc')

class Operation:
    WAIT = 0.1
    LONG_WAIT = 10
    CONFIDENCE = 0.9
    DEBUG = False
    TOOLOW = 650
    LOCATION = None
    first_line_pos= (-1, -1)
    line_height = 0
    adjust_scroll_up = 0

    def __init__(self):
        pass

    def moveTo_line_n(self, n: int):
        diff = self.line_height * (n - 1)
        (x, y) = self.first_line_pos
        y += diff
        pyautogui.moveTo(x, y)

    def moveTo_first_line(self):
        self.moveTo_line_n(1)
    
    def set_location(self, _loc):
        self.LOCATION = _loc

    def set_wait(self, _wait):
        self.WAIT = _wait

    def __los(self, _img, _region = LOCATION):
        return pyautogui.locateOnScreen(_img, region = _region, confidence = self.CONFIDENCE)

    def __dp(self, *values: object):
        if self.DEBUG:
            print(values)

    def wait(self, img, _wait = LONG_WAIT): # default wait for 10 sec
        # wait = self.LONG_WAIT if (_wait is None) else _wait
        xy = None
        start = time.time()
        while (xy == None):
            try:
                xy = self.__los(img)
            except pyautogui.ImageNotFoundException:
                pass
            if ((time.time() - start) > _wait):
                self.__dp("not fount ", img, " after ", _wait, "(s)")
                raise pyautogui.ImageNotFoundException

    def __exists(self, _img, _wait = WAIT, _region = LOCATION):
        self.__dp(_wait)
        for i in range(int(_wait*10)):
            try:
                xy = self.__los(_img, _region)
                self.__dp(_img, " found")
                return True
            except pyautogui.ImageNotFoundException:
                self.__dp(_img, " not found ", i)
                pass
        return False

    def __click(self, img):
        try:
            xy = self.__los(img)
            pyautogui.click(pyautogui.center(xy))
        except pyautogui.useImageNotFoundException:
            self.__dp(img, " not found in click")
            raise pyautogui.useImageNotFoundException

    def exists(self, img):
        return self.__exists(img)

    def exist_click(self, _img, _wait = WAIT):
        if self.__exists(_img, _wait): self.__click(_img)

    def drag_image_to(self, _x:int = -1, _y:int = -1, _img:str = ""):
        start_pos = pyautogui.position()
        self.wait(_img)
        xy = pyautogui.center(self.__los(_img))
        if xy[1] <= self.TOOLOW:
            pass
        else:
            pyautogui.mouseDown(xy)
            x = xy[0] if (_x == -1) else _x
            y = xy[1] if (_y == -1) else _y
            pyautogui.moveTo(x, y, 0.3)
            time.sleep(0.3)
            pyautogui.mouseUp()
            pyautogui.moveTo(start_pos)

    def scrollup_slow(self, lines: int):
        dy = -1 * int(self.line_height * lines * self.adjust_scroll_up)
        pyautogui.mouseDown()
        time.sleep(0.2)
        pyautogui.move(0, dy, 0.6) #, pyautogui.easeInQuad)
        time.sleep(0.25)
        pyautogui.mouseUp()

    def find_any_thread(self, imgs: list):
        def find_worker(_i:str, _d:list):
            if self.__exists(_i, 0.1): _d[_i] = 1

        ts = []
        q = deque()
        for _i in imgs: q.append({_i: 0})

        for _d in q: 
            _i = list(_d.keys())[0]
            t = threading.Thread(target=find_worker, args=(_i, _d,), daemon=True)
            ts.append(t)
            t.start()
        for t in ts: t.join()

        res = []
        for _d in q:
            for k, v in _d.items():
                if v > 0: res.append(k)

        return res

    def get_top_left(self, img):
        return None
        xywh = self.__los(img)
        (x, y) = (xywh[0], xywh[1])
        return (x, y)

    def get_bottom_right(self, img):
        return None

    def get_center(self, img):
        xy = pyautogui.center(self.__los(img))
        return xy

