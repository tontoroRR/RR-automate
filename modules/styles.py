from modules.images import *
from modules.utils import Constatns as Const

class Style:
    appName = "Rush Royale"
    location = Const.LOCATION

    menus = [BtnImage.menuWithInfo, BtnImage.menu]
    battleBtn = BtnImage.bottomBattle
    lbBtn = BtnImage.leaderBoards
    cards = LabelImage.cards
    wait = 1
    pause = 0.2
    heros = HeroImage.all
    units = UnitImage.all
    dryRun = False

    # need to set at child class
    styleType = None 

    tab = None
    banner = None
    badge1st = None

    lineHeight = None
    linesInPage = None
    lastLineYpos = None
    lastLine = None

    # need to inject from outside
    targets = []

    # [LabelImage.maxCritBadge1st, LabelImage.totalTrophyBadge1st]

class TopTrophy(Style):
    styleType = "Top Trophy" 

    tab = BtnImage.totalTrophyTab
    banner = LabelImage.totalTrophy
    badge1st = LabelImage.totalTrophyBadge1st

    lineHeight = 71
    linesInPage = 6
    lastLineYpos = 810
    lastLine = 22

class MaxCrit(Style):
    styleType = "Max Crit" 

    tab = BtnImage.maxCritTab
    banner = LabelImage.maxCrit
    badge1st = LabelImage.maxCritBadge1st

    lineHeight = 67
    linesInPage = 7
    lastLineYpos = 860
    lastLine = 22
