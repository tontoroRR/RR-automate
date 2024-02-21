# stats information of Rush Royale, say Units, Heros, User Info, Event
from enum import Enum

import yaml
import glob

import pdb


class RushRoyaleStats:
    units = {}

    def __init__(self):
        pass

    def read_style(self):
        pass

    def read_format(self):
        pass

    def setup(self):
        self.create_units()
        self.read_images()

    def create_units(self):
        with open('resources/units.yml', 'r') as _f:
            _us = yaml.safe_load(_f)
            for _k, _d in _us['unit'].items():
                self.units[_k] = Unit(_k, _d)

    def read_images(self):
        for _u in self.units.values():
            _u.read_images()



class UnitType(Enum):
    NONE = 0
    DAMAGE = 1
    DEBUFF = 2
    SUPPORT = 4
    SPECIAL = 8
    TOXIC = 16

    @staticmethod
    def read(_v: str) -> 'UnitType':
        match _v:
            case 'Damage':
                return UnitType.DAMAGE
            case 'Debuff':
                return UnitType.DEBUFF
            case 'Support':
                return UnitType.SUPPORT
            case 'SPECIAL':
                return UnitType.SPECIAL
        return UnitType.NONE


class Rarity(Enum):
    NONE = 0
    COMMON = 1
    RARE = 2
    EPIC = 4
    LEGENDARY = 8

    @staticmethod
    def read(_v: str) -> 'Rarity':
        match _v:
            case 'common':
                return Rarity.COMMON
            case 'rare':
                return Rarity.RARE
            case 'epic':
                return Rarity.EPIC
            case 'legendary':
                return Rarity.LEGENDARY
        return Rarity.NONE


class Unit:
    key: str = None
    rarity: Rarity = Rarity.NONE
    name: str = None
    name_jp: str = None
    type: UnitType = UnitType.NONE
    toxic: bool = False
    images = None

    def read_images(self):
        globname = f"images/unit/*/*{self.key}*.png"
        for _i in glob.glob(globname):
            self.images.append(_i)

    def __init__(self, _key: str, _d: dict):
        self.images = list()
        self.key = _key
        for _k, _v in _d.items():
            setattr(self, _k, _v)
