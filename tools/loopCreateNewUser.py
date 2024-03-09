from ctypes import windll as w
import time
import pyautogui
from modules.counter import Operation

print(1)
o = Operation()
print(o.wait('images/clanTab.png'))
