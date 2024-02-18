# stats information of Rush Royale, say Units, Heros, User Info, Event
from enum import Enum
from modules.styles import Style


class RushRoyaleStats:
    def __init__(self, style: Style, format: dict):
        self.style = style
        self.format = format
        pass


class UnitType(Enum):
    NONE = 0
    DAMAGE = 1
    DEBUFF = 2
    SUPPORT = 4
    SPECIAL = 8
    TOXIC = 16


# TODO: move them to JSON or Yaml
class UnitList:
    # Common 9 units
    common_name = [
        "Archer",
        "Bombardier",
        "Cold Mage",
        "Fier Mage",
        "Hunter",
        "Lightning Mage",
        "Poisoner",
        "Rogue",
        "Thrower",
    ]
    # Rare 9 units
    rare_names = [
        "Alchemist",
        "Banner",
        "Magic Cauldron",
        "Chemist",
        "Grindstone",
        "Priestess",
        "Sentry",
        "Sharpshooter" "Zealot",
    ]
    # Epic 17 units
    epic_names = [
        "Catapult",
        "Clown",
        "Crystalmancer",
        "Earth Elemental",
        "Cold Elemental",
        "Engineer",
        "Gargoyle",
        "Executionar",
        "Mime",
        "Plague Doctor",
        "Ivy" "Portal Keeper",
        "Pyrotechnic",
        "Portal Mage",
        "Thunderer",
        "Vampire",
        "Wind Archer",
    ]
    # Legendary 31 units
    legendary_names = [
        "Banshee",
        "Bruiser",
        "Blade Dancer",
        "Boreas",
        "Corsair",
        "Cultist",
        "Demon Hunter",
        "Demonologist",
        "Spirit Master",
        "Dryad",
        "Frost",
        "Harleyquin",
        "Inquisitor",
        "Genie",
        "Hex",
        "Knight Status",
        "Clock of Power",
        "Meteor",
        "Minotaur",
        "Monk",
        "Enchanted Sword",
        "Riding Hood",
        "Robot",
        "Scrapper",
        "Stasis",
        "Summoner",
        "Tesla",
        "Trapper",
        "Sea Dog",
        "Witch",
        "Shaman",
    ]


class Unit:
    name = None
    type = UnitType.NONE
    images = []
    order = -1
    talents = []
    max = False

    def __init__(self):
        # create all units
        pass

    @staticmethod
    def createAllUnits(u):
        u.append(1)


class TalentLeftRight(Enum):
    CENTER = 0
    LEFT = 1
    RIGHT = 2


class Talent:
    name = ""
    description = ""
    level = ""
    rightLeft = TalentLeftRight.LEFT


Units = []
Unit.createAllUnits(Units)
