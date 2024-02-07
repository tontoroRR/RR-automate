import time
import pyautogui
import ctypes

import asyncio
import threading
from collections import deque

from modules.images import Converter as Cv

import pdb

pyautogui.PAUSE = 0.2

class Deck:
    type = "PvP"
    hero = None
    units = []

class Counter:
    style = None
    op = None
    cardY = 565

    @staticmethod
    def convert(ary: list):
        l = list(map(Cv.convert, ary))
        return list(set(l))

    def __init__(self):
        self.op = Operation()
        pass

    def focusApp(self):
        self.__moveApp()
        time.sleep(0.2)
        self.__activateApp()
        time.sleep(0.2)

    def setStyle(self, _style):
        self.style = _style
        self.op.setLocation(self.style.location)
        self.op.setWait(self.style.wait)

    def openRanking(self):
        res = self.op.findAnyThread(self.style.menus)
        if res:
            self.op.existClick(res.pop())
        else:
            pass
        self.op.existClick(self.style.lbBtn)
        self.op.existClick(self.style.tab)
        self.op.existClick(self.style.banner)
        self.op.wait(self.style.badge1st)

        # set start/end line position
        posX = pyautogui.position()[0]
        posY = self.op.getCenter(self.style.badge1st)[1]
        self.op.firstLinePos = (posX, posY)
        self.op.lastLinePos = (posX, posY + self.style.lineHeight * self.style.linesInPage)
        self.op.moveToFirstLine()

    def _filterFoundOnly(self, _dict):
        l = list(map(Cv.convert, filter(lambda k: _dict[k] == 1, _dict.keys())))
        return list(set(l))

    def getUserDeck(self):
        hero = []
        units = []
        hero = self.convert(self.op.findAnyThread(self.style.heros))
        units = self.convert(self.op.findAnyThread(self.style.units))
        return (hero, sorted(units))

    def count(self):
        for n in range(1, self.style.lastLine + 1):
            posY = pyautogui.position()[1]

            if (self.style.lastLineYpos < posY and n != self.style.lastLine):
                # linesScrollUp = self.style.linesInPage 
                if (self.style.lastLine - n) > self.style.linesInPage:
                    linesScrollUp = self.style.linesInPage 
                else:
                    linesScrollUp = self.style.lastLine - n
                # print("y = ", posY, ";  sup = ", linesScrollUp, ";  n = ", n)
                self.op.scrollUpSlow(self.style.lineHeight, linesScrollUp)

            # print(n, self.style.targets) # for partial log
            if not (self.style.targets) or (self.style.targets and (n in self.style.targets)):
                pyautogui.click()
                self.op.dragImageTo(-1, self.cardY, self.style.cards)
                if self.style.dryRun:
                    yield((['hero'], ['unit1', 'unit2', 'unit3', 'unit4', 'unit5']))
                else:
                    yield(self.getUserDeck())
                pyautogui.press('esc')
            else:
                yield([])

            if (n != self.style.lastLine):
                pyautogui.move(0, self.style.lineHeight)

    def backToTop(self):
        while not(self.op.exists(self.style.battleBtn)):
            pyautogui.press('esc')

    def __moveApp(self):
        (left, top, width, height) = self.style.location
        h = ctypes.windll.user32.FindWindowW(0, self.style.appName)
        ctypes.windll.user32.MoveWindow(h, left, top, width, height)

    def __activateApp(self):
        h = ctypes.windll.user32.FindWindowW(0, self.style.appName)
        ctypes.windll.user32.SetForegroundWindow(h)


class Operation:
    WAIT = 0.1
    LONG_WAIT = 10
    CONFIDENCE = 0.9
    DEBUG = False
    TOOLOW = 650
    LOCATION = None
    firstLinePos= (-1, -1)
    lastLinePos= (-1, -1)

    def __init__(self):
        pass

    def moveToFirstLine(self):
        pyautogui.moveTo(self.firstLinePos)
        # pyautogui.move(0, 215)
    
    def moveToLastLine(self):
        pyautogui.moveTo(self.lastLinePos)
        # pyautogui.move(0, 684)

    def setLocation(self, _loc):
        self.LOCATION = _loc

    def setWait(self, _wait):
        self.WAIT = _wait

    def __los(self, img):
        return pyautogui.locateOnScreen(img, region = self.LOCATION, confidence = self.CONFIDENCE)

    def __dp(self, *values: object):
        if self.DEBUG:
            print(values)

    def wait(self, img, _wait = None): # default wait for 10 sec
        wait = self.LONG_WAIT if (_wait is None) else _wait
        xy = None
        start = time.time()
        while (xy == None):
            try:
                xy = self.__los(img)
            except pyautogui.ImageNotFoundException:
                pass
            if ((time.time() - start) > wait):
                self.__dp("not fount ", img, " after ", wait, "(s)")
                raise pyautogui.ImageNotFoundException

    def __exists(self, img, wait = None):
        if (wait is None): wait = self.WAIT
        self.__dp(wait)
        for i in range(int(wait*10)):
            try:
                xy = self.__los(img)
                self.__dp(img, " found")
                return True
            except pyautogui.ImageNotFoundException:
                self.__dp(img, " not found ", i)
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

    def existClick(self, img):
        if self.__exists(img): self.__click(img)

    def dragImageTo(self, x, y, img):
        startPos = pyautogui.position()
        self.wait(img)
        xy = pyautogui.center(self.__los(img))
        if xy[1] <= self.TOOLOW:
            return
        else:
            pyautogui.mouseDown(xy)
            if (x == -1): x = xy[0]
            if (y == -1): y = xy[1]
            pyautogui.moveTo(x, y, 0.3)
            time.sleep(0.3)
            pyautogui.mouseUp()
            pyautogui.moveTo(startPos)


    def scrollUpSlow(self, lineHeight: int, lines: int):
        dy = lineHeight * lines
        diff = lines * lines
        pyautogui.mouseDown()
        pyautogui.move(0, -1 * dy - diff, 0.6)
        time.sleep(0.3)
        pyautogui.mouseUp()
        pyautogui.move(0, diff)

    def findAnyThread(self, imgs):
        q = deque()
        for i in imgs: q.append({i: 0})
        def tfunc(_d:dict):
            k = list(_d.keys())[0]
            if self.__exists(k, 0.1): _d[k] = 1
        ts = []
        for d in q: 
            t = threading.Thread(target=tfunc, args=(d,))
            ts.append(t)
            t.start()
        for t in ts: t.join()
        res = []
        for d in q:
            for k, v in d.items():
                if v > 0: res.append(k)
        return res

    def getTopLeft(self, img):
        return None
        xywh = self.__los(img)
        x = xywh[0]
        y = xywh[1]
        return (x, y)

    def getBottomRight(self, img):
        return None

    def getCenter(self, img):
        xy = pyautogui.center(self.__los(img))
        return xy

