import sys
from datetime import datetime
import subprocess
import pyautogui


pyautogui.PAUSE = 0.5
x: int = 45
y: int = 62
store_dir: str = 'D:/Users/masaaki/Desktop/greenshot/'

if len(sys.argv) == 3:
    x = int(sys.argv[1])
    y = int(sys.argv[2])
        
pos = pyautogui.position()
img = pyautogui.screenshot(region=(pos.x-1, pos.y-1, x, y))
name = store_dir + "scr_" + datetime.now().strftime('%Y-%m-%d_%H%M%S.%f.png')
img.save(name)
subprocess.call(["mspaint.exe", name.replace("/", "\\")])

# subprocess.run(("mspaint.exe", img))

# print(pos)
# pyautogui.moveTo(pos)
# pyautogui.press('f1')
# pyautogui.dragTo(pos 0.3)

"""
1473, 600
1487, 623
1528, 623
1528, 685
"""
