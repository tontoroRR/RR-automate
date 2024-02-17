import os
import glob
import re

import pdb

class BtnImage:
    menu = 'images/menuBtn.png'
    menuWithInfo = 'images/menuBtnInfo.png'
    backArrow = 'images/backarrowBtn.png'
    leaderBoards = 'images/leaderboards.png'
    close = 'images/closeBtn.png'
    maxCritTab = 'images/maxCritTab.png'
    totalTrophyTab = 'images/totalTrophyTab.png'
    bottomBattle = 'images/bottomBattleBtn.png'

class LabelImage:
    totalTrophy = 'images/totaltrophies.png'
    totalTrophyBadge1st = 'images/totalTrophyBadge1st.png'
    totalTrophyBadge1st_ALT = 'images/totalTrophyBadge1st_ALT_.png'
    maxCrit = 'images/maxCrit.png'
    maxCritBadge1st = 'images/maxCrit1stBadge.png'
    cards = 'images/cardsLabel.png'
    bestPlayer = 'images/bestPlayer.png'
    top90 = 'images/top90.png'

class HeroImage:
    all = []
    for _d in glob.glob('images/hero/*/*'):
        all.append(_d)

class UnitImage:
    all = []
    for _d in glob.glob('images/unit/*/*'):
        all.append(_d)
