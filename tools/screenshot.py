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
x, y, w, h = 0, 0, 45, 62
mode = "--mspaint"
store_dir: str = os.environ.get("save_path")
print(store_dir)

pos = pyautogui.position()
x = pos.x - 1
y = pos.y - 1

if len(sys.argv) in [3, 4]:
    w = int(sys.argv[1]) or w
    h = int(sys.argv[2]) or h
elif len(sys.argv) in [5, 6]:
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    w = int(sys.argv[3])
    h = int(sys.argv[4])

if len(sys.argv) in [4, 6]:
    mode = sys.argv[len(sys.argv) - 1]

img = pyautogui.screenshot(region=(x, y, w, h))
name = store_dir + "scr_" + datetime.now().strftime("%Y-%m-%d_%H%M%S.%f.png")
img.save(name)

if mode == "--mspaint":
    subprocess.call(["mspaint.exe", name.replace("/", "\\")])
