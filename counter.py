import pyautogui
import time

import asyncio
import threading
from collections import deque

from images import Converter as Cv

pyautogui.PAUSE = 0.2

class Deck:
    type = "PvP"
    hero = None
    units = []

class Counter:
    style = None
    op = None

    def __init__(self):
        self.op = Operation()
        pass

    def setStyle(self, _style):
        self.style = _style
        self.op.setLocation(self.style.location)
        self.op.setWait(self.style.wait)
        return self

    def openRanking(self):
        self.op.existClick(self.style.menu)
        self.op.existClick(self.style.lbBtn)
        self.op.existClick(self.style.tab)
        self.op.existClick(self.style.banner)
        self.op.wait(self.style.badge1st)
        pyautogui.move(0, 215) # move to first row

    def _filterFoundOnly(self, _dict):
        l = list(map(Cv.convert, filter(lambda k: _dict[k] == 1, _dict.keys())))
        return list(set(l))

    @staticmethod
    def convert(ary: list):
        l = list(map(Cv.convert, ary))
        return list(set(l))

    def getUserDeck(self, rank: int):
        m = 0
        # s = time.time()
        hero = []
        units = []
        if m == 1:
            # Normal
            hero = self.convert(self.op.findAny(self.style.heros))
            units = self.convert(self.op.findAny(self.style.units))
        elif m == 2:
            # Async
            hero = self.convert(asyncio.run(self.op.findAnyAsync(self.style.heros)))
            units = self.convert(asyncio.run(self.op.findAnyAsync(self.style.units)))
        else:
            # Threading
            hero = self.convert(self.op.findAnyThread(self.style.heros))
            units = self.convert(self.op.findAnyThread(self.style.units))
        # print(time.time() - s)
        return (rank, hero, units)

    def count(self):
        decks = []
        for i in range(self.style.linesInPage):
            pyautogui.click()
            decks.append(self.getUserDeck(i + 1))
            pyautogui.press('esc')
            pyautogui.move(0, self.style.lineHeight)
        for i in range(self.style.linesInPage, self.style.lastLine):
            pyautogui.click()
            decks.append(self.getUserDeck(i + 1))
            pyautogui.press('esc')
            self.op.scrollUp(self.style.lineHeight)
        return decks

    def backToTop(self):
        while not(self.op.exists(self.style.battleBtn)):
            pyautogui.press('esc')


class Operation:
    WAIT = 0.1
    LONG_WAIT = 10
    CONFIDENCE = 0.9
    LOCATION = (1275, 2, 647, 1020)
    DEBUG = False

    def __init__(self):
        pass

    def setLocation(self, _loc):
        self.LOCATION = _loc

    def setWait(self, _wait):
        self.WAIT = _wait

    def __los(self, img):
        return pyautogui.locateOnScreen(img, region = self.LOCATION, confidence = self.CONFIDENCE)

    def __dp(self, *values: object):
        if self.DEBUG:
            print(v)

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
                break

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

    def move(self, img):
        xy = self.__los(img)
        pyautogui.moveTo(pyautogui.center(xy))

    def scrollUp(self, _dy: int):
        dy = _dy + 15 # - 7
        pyautogui.mouseDown()
        pyautogui.move(0, -1 * dy, 0.2)
        time.sleep(0.1)
        pyautogui.mouseUp()
        pyautogui.move(0, dy)

    def findAny(self, imgs):
        q = deque()
        for i in imgs: q.append({i: 0})
        # res = {img: 0 for img in imgs}
        #for img in imgs:
        #    if self.__exists(img, 0.1): res[img] = 1
        for d in q:
            k = list(d.keys())[0]
            if self.__exists(k, 0.1): d[k] = 1
        res = []
        for d in q:
            for k, v in d.items():
                if v > 0: res.append(k)
        return res

    async def findAnyAsync(self, imgs):
        q = deque()
        for i in imgs: q.append({i: 0})
        async def afunc(_d:dict):
            k = list(_d.keys())[0]
            if self.__exists(k, 0.1): _d[k] = 1
        tasks = list(map(afunc, q))
        await asyncio.gather(*tasks)
        res = []
        for d in q:
            for k, v in d.items():
                if v > 0: res.append(k)
        return res

    def findAnyThread(self, imgs):
        q = deque()
        for i in imgs: q.append({i: 0})
        def tfunc(_d:dict):
            k = list(_d.keys())[0]
            if self.__exists(k, 0.1): _d[k] = 1
        ts = []
        for d in q: ts.append(
                    threading.Thread(target=tfunc, args=(d,))
                )
        for t in ts: t.start()
        for t in ts: t.join()
        res = []
        for d in q:
            for k, v in d.items():
                if v > 0: res.append(k)
        return res

