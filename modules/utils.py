import re

class Utils:

    @staticmethod
    def convert_int_to_col(n: int) -> str:
        ai = ord('A')
        (f, s) = divmod(n-1, 26)
        fc = chr(ai + f - 1) if f > 0 else ''
        sc = chr(ai + s)
        return fc + sc
    #('' if di == 0 else chr(alphaCode + di)) + chr(alphaCode + mo + 1)

    @staticmethod
    def convert_col_to_int(c: str) -> int:
        lcols = list(re.sub(r"[0-9]", "", c))
        col = 0
        for l in lcols:
            col = col * 26 + ord(l) - 64
        return col
