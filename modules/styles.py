from modules.images import *

import pdb

class Style:
    app_name = "Rush Royale"
    app_region = (1275, 2, 647, 1020)

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
    adjust_scroll_up = 0
    total_line = 0
    card_y = 565

    card_tab = None # No need to click
    cards_region = (-225, 40, 450, 330)

    # need to inject from outside
    lines_only = []

    title_deck_table = [["Rank", "Hero", "Unit1", "Unit2", "Unit3", "Unit4", "Unit5"]]
    # [LabelImage.maxCritBadge1st, LabelImage.totalTrophyBadge1st]
    def import_from(self, yml:dict):
        for k, v in yml.items(): setattr(self, k, v)
        if hasattr(self, 'lines_range') and 'min' in self.lines_range and 'max' in self.lines_range:
            self.lines_only = list(range(self.lines_range['min'], self.lines_range['max'] + 1))

    def special_operation(self):
        return None

class TopTrophy(Style):
    style_type = "Top Trophy" 
        
    tab = BtnImage.totalTrophyTab
    banner = LabelImage.totalTrophy
    badge1st = [LabelImage.totalTrophyBadge1st, LabelImage.totalTrophyBadge1st_ALT]

    line_height= 71
    lines_per_page = 7
    last_line_y = 810
    total_line = 1

    def __init__(self):
        self.buttonSeq.append(self.tab)
        self.buttonSeq.append(self.banner)

class MaxCrit(Style):
    style_type = "Max Crit" 

    tab = BtnImage.maxCritTab
    banner = LabelImage.maxCrit
    badge1st = LabelImage.maxCritBadge1st

    line_height= 67
    lines_per_page = 8
    last_line_y = 860
    total_line = 1

    def __init__(self):
        self.buttonSeq.append(self.tab)
        self.buttonSeq.append(self.banner)

class RhandumLeague(Style):
    style_type = "Rhandum League"
    badge1st = 'images/rhandumLeague1stBadge.png'

    line_height= 86
    lines_per_page = 5
    last_line_y = 480
    total_line = 1

    card_tab = 'images/rhandumLeagueTab.png'
    adjust_scroll_up = 1.08

    def __init__(self):
        self.buttonSeq = [
                "images/eventTab.png",
                "images/rhandumLeagueCard.png",
                'images/rhandumLeagueLabel.png'
                ]
    def special_operation(self):
        return "click_top100_for_RL"
