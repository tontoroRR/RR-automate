import pprint
import asyncio
import pyautogui
import time
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

    def getUserDeck(self, rank: int):
        hero = []
        units = []
        # hero = self._filterFoundOnly(self.op.findAny(self.style.heros))
        # units = self._filterFoundOnly(self.op.findAny(self.style.units))
        hero = self._filterFoundOnly(asyncio.run(self.op.findAnyAsync(self.style.heros)))
        units = self._filterFoundOnly(asyncio.run(self.op.findAnyAsync(self.style.units)))
        return (rank, hero, units)

    def count(self):
        decks = []
        for i in range(self.style.linesInPage):
            pyautogui.click()
            decks.append(self.getUserDeck(i + 1))
            pyautogui.press('esc')
            pyautogui.move(0, self.style.lineHeight)
            print(i + 1)

        for i in range(self.style.linesInPage, self.style.lastLine):
            pyautogui.click()
            decks.append(self.getUserDeck(i + 1))
            pyautogui.press('esc')
            print(i + 1)
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
        # , pyautogui.easeOutQuad)
        time.sleep(0.1)
        pyautogui.mouseUp()
        pyautogui.move(0, dy)

    async def findAnyAsync(self, imgs):
        res = {h: 0 for h in imgs}
        async def afunc(_img, _res: dict = res):
            if self.__exists(_img, 0.1): _res[_img] = 1
        tasks = list(map(afunc, imgs))
        await asyncio.gather(*tasks)
        return res

    def findAny(self, imgs):
        res = {h: 0 for h in imgs}
        for img in imgs:
            if self.__exists(img, 0.1): res[img] = 1
        return res
