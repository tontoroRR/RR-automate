from ctypes import windll as win
from time import sleep


app_name = "Rush Royale"
(left, top, width, height) = (1275, 2, 647, 1020)

h = win.user32.FindWindowW(0, app_name)
win.user32.MoveWindow(h, left, top, width, height)
sleep(0.2)
win.user32.SetForegroundWindow(h)
sleep(0.2)

