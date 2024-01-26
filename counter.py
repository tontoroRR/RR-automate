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

    def setWait(self, _wait):
        pyautogui.PAUSE = _wait

    def setStyle(self, _style):
        self.style = _style
        self.op.setLocation(self.style.location)
        self.op.setWait(self.style.wait)
        return self

    def existClick(self, img):
        if self.op.exists(img): self.op.click(img)

    def openRanking(self):
        self.existClick(self.style.menu)
        self.existClick(self.style.tab)
        self.existClick(self.style.banner)

    def count(self):
        pprint.pprint(self.style)

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

    def exists(self, img):
        wait = self.WAIT
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

    def click(self, img):
        try:
            xy = self.los(img)
            pyautogui.click(pyautogui.center(xy))
        except pyautogui.useImageNotFoundException:
            print(img, " not found in click")
            raise pyautogui.useImageNotFoundException

    def moveTo(self, img):
        xy = self.los(img)
        pyautogui.moveTo(pyautogui.center(xy))

    def scrollUp():
        pyautogui.drag(0, -68*3, 1, button = "left")
        pyautogui.drag(0, -68*3, 0.65, button = "left")
        time.sleep(1)
