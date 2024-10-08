# import pdb
from modules.images import BtnImage, LabelImage


class Style:
    app_name = "Rush Royale"
    app_region = (1275, 2, 647, 1020)

    menus = [BtnImage.menuWithInfo, BtnImage.menu]
    btn_battle = BtnImage.bottomBattle
    btn_leaderboards = BtnImage.leaderBoards
    cards = LabelImage.cards

    wait = 1
    pause = 0.2
    heroes = None
    units = None

    buttonSeq = [menus, btn_leaderboards]

    # need to set at child class
    style_type = None

    tab = None
    banner = None
    badge1st = None

    line_height = None
    lines_per_page = None
    last_line_y = None
    adjust_scroll_up = 0
    total_line = 0
    card_y = 565

    card_tab = None  # No need to click
    cards_region = (-225, 40, 450, 330)

    # need to inject from outside
    lines_only = []

    do_scroll_not_found = False

    dryrun = False
    DEBUG = False
    use_sec = True
    sleep_at_end = 0  # todo)) what's this?

    title_deck_table = [
        ["Rank", "Hero", "Unit1", "Unit2", "Unit3", "Unit4", "Unit5"]
    ]

    def import_from(self, yml: dict):
        for k, v in yml.items():
            setattr(self, k, v)
        if hasattr(self, "lines_range"):
            min, max = self.lines_range["min"], self.lines_range["max"]
            if any([0 < min, 0 < max]):
                self.lines_only = list(min, max)

    def special_operation(self):
        pass
        return None


class TopTrophy(Style):
    style_type = "Top Trophy"

    tab = BtnImage.totalTrophyTab
    banner = LabelImage.totalTrophy
    badge1st = LabelImage.totalTrophyBadge1st

    line_height = 71
    lines_per_page = 7
    last_line_y = 810
    total_line = 1
    adjust_scroll_up = 0.0925

    def __init__(self):
        self.buttonSeq.append(self.tab)
        self.buttonSeq.append(self.banner)


class PastSeasonLeader(TopTrophy):
    style_type = "Past Season Leader"

    tab = "resources/images/pastLeadersBtn.png"
    banner = "resources/images/pastTotalTrophies.png"

    lines_per_page = 9
    last_line_y = 904

    def __init__(self):
        super().__init__()


class MaxCrit(Style):
    style_type = "Max Crit"

    tab = BtnImage.maxCritTab
    banner = LabelImage.maxCrit
    badge1st = LabelImage.maxCritBadge1st

    line_height = 67
    lines_per_page = 8
    last_line_y = 860
    total_line = 1
    adjust_scroll_up = 0.11

    def __init__(self):
        self.buttonSeq.append(self.tab)
        self.buttonSeq.append(self.banner)


class RhandumLeague(Style):
    style_type = "Rhandum League"
    badge1st = "resources/images/rhandumLeague1stBadge.png"

    line_height = 86
    lines_per_page = 4
    last_line_y = 480
    total_line = 1
    adjust_scroll_up = 0.08
    do_scroll_not_found = True

    card_tab = "resources/images/rhandumLeagueTab.png"

    def __init__(self):
        self.buttonSeq = [
            "resources/images/eventTab.png",
            [
                "resources/images/rhandumLeagueCard.png",
                "resources/images/rhandumLeagueCard_ALT_.png"
            ],
            "resources/images/rhandumLeagueLabel.png",
        ]

    def special_operation(self):
        return "click_top100_for_RL"
