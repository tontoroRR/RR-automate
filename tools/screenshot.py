import os
import sys
from datetime import datetime
import subprocess
import pyautogui

from dotenv import load_dotenv

scr_path = os.path.dirname(__file__)
load_dotenv(verbose=True)
res = load_dotenv(scr_path + "\\.env_screenshot")
print(res)

pyautogui.PAUSE = 0.5
x: int = 45
y: int = 62
store_dir: str = os.environ.get("save_path")
print(store_dir)

if len(sys.argv) == 3:
    x = int(sys.argv[1])
    y = int(sys.argv[2])

pos = pyautogui.position()
img = pyautogui.screenshot(region=(pos.x - 1, pos.y - 1, x, y))
name = store_dir + "scr_" + datetime.now().strftime("%Y-%m-%d_%H%M%S.%f.png")
img.save(name)
subprocess.call(["mspaint.exe", name.replace("/", "\\")])
