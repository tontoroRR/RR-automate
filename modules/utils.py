import re

class Utils:

    @staticmethod
    def convertIntToCol(n: int) -> str:
        ai = ord('A')
        (f, s) = divmod(n-1, 26)
        fc = chr(ai + f - 1) if f > 0 else ''
        sc = chr(ai + s)
        return fc + sc
    #('' if di == 0 else chr(alphaCode + di)) + chr(alphaCode + mo + 1)

    @staticmethod
    def convertColToInt(c: str) -> int:
        lcols = list(re.sub(r"[0-9]", "", c))
        col = 0
        for l in lcols:
            col = col * 26 + ord(l) - 64
        return col

class Constatns:
    LOCATION = (1275, 2, 647, 1020)
