import glob
import re

import pdb


class BtnImage:
    menu = "images/menuBtn.png"
    menuWithInfo = "images/menuBtnInfo.png"
    backArrow = "images/backarrowBtn.png"
    leaderBoards = "images/leaderboards.png"
    close = "images/closeBtn.png"
    maxCritTab = "images/maxCritTab.png"
    totalTrophyTab = "images/totalTrophyTab.png"
    bottomBattle = "images/bottomBattleBtn.png"


class LabelImage:
    totalTrophy = "images/totaltrophies.png"
    totalTrophyBadge1st = "images/totalTrophyBadge1st.png"
    totalTrophyBadge1st_ALT = "images/totalTrophyBadge1st_ALT_.png"
    maxCrit = "images/maxCrit.png"
    maxCritBadge1st = "images/maxCrit1stBadge.png"
    cards = ["images/cardsLabel.png",
             "images/cardsLabel_ALT_.png",
             "images/cardsLabel_ALT__ALT_.png",
             ]
    bestPlayer = "images/bestPlayer.png"
    top90 = "images/top90.png"


class Converter:
    __CONVERTS: dict = {
        "_ALT_": "",
        # \1 = unit/hero, \2 = rareity, \3 = name
        "images/(.+)/(.+)/(.+).png": r"\3",
        "Max": "(Max)",
    }

    def convert_img_to_name(_name: str):
        name = _name
        for _reg, _str in Converter.__CONVERTS.items():
            name = re.sub(_reg, _str, name)
        return name


class HeroImage(Converter):
    all = {}
    for _d in glob.glob("images/hero/*/*"):
        _d = _d.replace("\\", "/")
        all[_d] = Converter.convert_img_to_name(_d)
    print(len(all))


class UnitImage(Converter):
    all = {}
    for _d in glob.glob("images/unit/*/*"):
        _d = _d.replace("\\", "/")
        all[_d] = Converter.convert_img_to_name(_d)
    print(len(all))
