import ctypes
import time

def moveApp(appname, location):
    (left, top, width, height) = location #(1275, 2, 647, 1020)
    h = ctypes.windll.user32.FindWindowW(0, appname)
    ctypes.windll.user32.MoveWindow(h, left, top, width, height)
    time.sleep(0.2)

def activateApp(appname):
    h = ctypes.windll.user32.FindWindowW(0, appname)
    ctypes.windll.user32.SetForegroundWindow(h)
    time.sleep(0.2)
