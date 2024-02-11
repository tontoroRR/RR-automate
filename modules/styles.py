from modules.images import *
from modules.utils import Constatns as Const

import pdb

class Style:
    app_name = "Rush Royale"
    location = Const.LOCATION

    menus = [BtnImage.menuWithInfo, BtnImage.menu]
    btn_battle = BtnImage.bottomBattle
    btn_leaderboards = BtnImage.leaderBoards

    cards = LabelImage.cards
    wait = 1
    pause = 0.2
    heros = HeroImage.all
    units = UnitImage.all
    dryrun = False

    buttonSeq = [menus, btn_leaderboards]

    # need to set at child class
    style_type = None 

    tab = None
    banner = None
    badge1st = None

    line_height = None
    lines_per_page = None
    last_line_y= None
    line_count = 0
    card_y = 565

    card_tab = None # No need to click

    # need to inject from outside
    targets = []

    # [LabelImage.maxCritBadge1st, LabelImage.totalTrophyBadge1st]
    def import_from(self, yml:dict):
        for k, v in yml.items(): setattr(self, k, v)


class TopTrophy(Style):
    style_type = "Top Trophy" 

    tab = BtnImage.totalTrophyTab
    banner = LabelImage.totalTrophy
    badge1st = LabelImage.totalTrophyBadge1st

    line_height= 71
    lines_per_page = 6
    last_line_y = 810
    line_count = 1

    def __init__(self):
        self.buttonSeq.append(self.tab)
        self.buttonSeq.append(self.banner)

class MaxCrit(Style):
    style_type = "Max Crit" 

    tab = BtnImage.maxCritTab
    banner = LabelImage.maxCrit
    badge1st = LabelImage.maxCritBadge1st

    line_height= 67
    lines_per_page = 7
    last_line_y = 860
    line_count = 1

    def __init__(self):
        self.buttonSeq.append(self.tab)
        self.buttonSeq.append(self.banner)

class RhandumLeague(Style):
    style_type = "Rhandum League"
    badge1st = 'images/rhandumLeague1stBadge.png'

    line_height= 86
    lines_per_page = 5
    last_line_y = 480
    line_count = 1
    dryrun = True

    card_tab = 'images/rhandumLeagueTab.png'
    def __init__(self):
        self.buttonSeq = [
                "images/eventTab.png",
                "images/rhandumLeagueCard.png",
                'images/rhandumLeagueLabel.png'
                ]
