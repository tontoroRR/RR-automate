import re
import cv2
import numpy as np
import pyautogui

from datetime import datetime

class Utils:
    @staticmethod
    def convert_int_to_col(n: int) -> str:
        ai = ord('A')
        f, s = divmod(n-1, 26)
        fc = chr(ai + f - 1) if f > 0 else ''
        sc = chr(ai + s)
        return fc + sc

    @staticmethod
    def convert_col_to_int(c: str) -> int:
        lcols = list(re.sub(r"[0-9]", "", c))
        col = 0
        for l in lcols:
            col = col * 26 + ord(l) - 64
        return col

    @staticmethod
    def convert(ary: list):
        l = list(map(UnitConverter.convert_img_to_name, ary))
        return list(set(l))

    @staticmethod
    def log_exception():
        print("mouse poistion: ", pyautogui.position())
        Utils.take_screenshot(0, True)
        
    @staticmethod
    def take_screenshot(_num:int = 0, _cursor:bool = False, _region = None):
        if _region:
            _img = pyautogui.screenshot(region=_region)
        else:
            _img = pyautogui.screenshot(region=_region)
        name = f"U:\\home\\phoi\\errors\\{datetime.now().strftime('%Y-%m-%d_%H%M%S')}_#{str(_num).zfill(4)}.png"
        _img.save(name)


class UnitConverter:
    __DICT: dict = {
            '\\\\': '/',
            '_ALT_' : '',
            'images/(.+)/(.+)/(.+).png': r'\3', # \1 = unit/hero, \2 = rareity, \3 = name
            'Max' : '(Max)',
            }

    @staticmethod
    def convert_img_to_name(_name: str):
        name = _name
        for _reg, _str in UnitConverter.__DICT.items():
            print(name)
            name = re.sub(_reg, _str, name)
        return name
