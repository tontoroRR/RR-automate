import pprint
import pyautogui
import time

pyautogui.PAUSE = 0.2

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

    def _filterFoundOnly(self, _dict):
        return list(filter(lambda k: _dict[k] == 1, _dict.keys()))

    def count(self):
        pyautogui.move(0, 215) # move to first row
        pyautogui.click()
        hero = self._filterFoundOnly(self.op.findAny(self.style.heros))
        # self._filterFoundOnly(hero)
        units = self._filterFoundOnly(self.op.findAny(self.style.units))
        print(hero)
        print(units)
        pyautogui.press('esc')

class Operation:
    WAIT = 0.1
    LONG_WAIT = 10
    CONFIDENCE = 0.9
    LOCATION = (1275, 2, 647, 1020)

    def __init__(self):
        pass

    def setLocation(self, _loc):
        self.LOCATION = _loc

    def setWait(self, _wait):
        self.WAIT = _wait

    def los(self, img):
        return pyautogui.locateOnScreen(img, region = self.LOCATION, confidence = self.CONFIDENCE)

    def wait(self, img): # default wait for 10 sec
        wait = self.LONG_WAIT
        xy = None
        start = time.time()
        while (xy == None):
            try:
                xy = self.los(img)
            except pyautogui.ImageNotFoundException:
                pass
            if ((time.time() - start) > wait):
                print("not fount ", img, " after ", wait, "(s)")
                break

    def __exists(self, img, wait = None):
        if (wait is None): wait = self.WAIT
        print(wait)
        for i in range(int(wait*10)):
            try:
                xy = self.los(img)
                print(img, " found")
                return True
            except pyautogui.ImageNotFoundException:
                print(img, " not found ", i)
                pass

        return False

    def __click(self, img):
        try:
            xy = self.los(img)
            pyautogui.click(pyautogui.center(xy))
        except pyautogui.useImageNotFoundException:
            print(img, " not found in click")
            raise pyautogui.useImageNotFoundException

    def existClick(self, img):
        if self.__exists(img): self.__click(img)

    def move(self, img):
        xy = self.los(img)
        pyautogui.moveTo(pyautogui.center(xy))

    

    def findAny(self, imgs):
        res = {h: 0 for h in imgs}
        for img in imgs:
            if self.__exists(img, 0.1): res[img] = 1
        return res

    @staticmethod
    def scrollUp():
        pyautogui.drag(0, -68*3, 1, button = "left")
        pyautogui.drag(0, -68*3, 0.65, button = "left")
        time.sleep(1)
