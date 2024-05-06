import re
import pyautogui
from datetime import datetime


class Utils:
    ERROR_IMAGE_PATH = None
    REGION = None

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
    def log_exception(_num: int = 0, _region=None):
        print("mouse poistion: ", pyautogui.position())
        Utils.take_screenshot(_num, True, _region)

    @staticmethod
    def take_screenshot(_num: int = 0, _cursor: bool = False, _region=None):
        region = _region if _region else Utils.REGION
        path = Utils.ERROR_IMAGE_PATH or r'.\errors'
        if _region:
            _img = pyautogui.screenshot(region=region)
        else:
            _img = pyautogui.screenshot(region=region)
        dt = datetime.now().strftime('%Y%m%d_%H%M%S')
        name = rf"{path}\{dt}_{str(_num).zfill(4)}.png"
        _img.save(name)
