import re
# import pyautogui
from datetime import datetime


class Utils:
    @staticmethod
    def convert_int_to_col(n: int) -> str:
        ai = ord("A")
        f, s = divmod(n - 1, 26)
        fc = chr(ai + f - 1) if f > 0 else ""
        sc = chr(ai + s)
        return fc + sc

    @staticmethod
    def convert_col_to_int(c: str) -> int:
        lcols = list(re.sub(r"[0-9]", "", c))
        col = 0
        for _l in lcols:
            col = col * 26 + ord(_l) - 64
        return col

    @staticmethod
    def log_exception(_num: int = 0):
        print("mouse poistion: ", pyautogui.position())
        Utils.take_screenshot(_num, True)

    @staticmethod
    def take_screenshot(_num: int = 0, _cursor: bool = False, _region=None):
        if _region:
            _img = pyautogui.screenshot(region=_region)
        else:
            _img = pyautogui.screenshot(region=_region)
        dt = datetime.now().strftime('%Y%m%d_%H%M%S')
        name = f"U:\\home\\phoi\\errors\\{dt}_{str(_num).zfill(4)}.png"
        _img.save(name)
