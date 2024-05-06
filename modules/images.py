import re


class BtnImage:
    menu = "resources/images/menuBtn.png"
    menuWithInfo = "resources/images/menuBtnInfo.png"
    backArrow = "resources/images/backarrowBtn.png"
    leaderBoards = "resources/images/leaderboards.png"
    close = "resources/images/closeBtn.png"
    maxCritTab = "resources/images/maxCritTab.png"
    totalTrophyTab = "resources/images/totalTrophyTab.png"
    bottomBattle = "resources/images/bottomBattleBtn.png"


class LabelImage:
    totalTrophy = "resources/images/totaltrophies.png"
    totalTrophyBadge1st = "resources/images/totalTrophyBadge1st.png"
    totalTrophyBadge1st_ALT = "resources/images/totalTrophyBadge1st_ALT_.png"
    maxCrit = "resources/images/maxCrit.png"
    maxCritBadge1st = "resources/images/maxCrit1stBadge.png"
    cards = ["resources/images/cardsLabel.png",
             "resources/images/cardsLabel_ALT_.png",
             "resources/images/cardsLabel_ALT__ALT_.png",
             ]
    bestPlayer = "resources/images/bestPlayer.png"
    top90 = "resources/images/top90.png"


class Converter:
    __CONVERTS: dict = {
        "_ALT_": "",
        # \1 = unit/hero, \2 = rarity, \3 = name
        "resources/images/(.+)/(.+)/(.+).png": r"\3",
        "Max": "(Max)",
    }

    def convert_img_to_name(_name: str):
        name = _name
        for _reg, _str in Converter.__CONVERTS.items():
            name = re.sub(_reg, _str, name)
        return name
