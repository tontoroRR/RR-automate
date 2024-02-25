# stats information of Rush Royale, say Units, Heroes, User Info, Event
import yaml
import glob
import pdb


class RushRoyaleStats:
    units = {}
    heroes = {}

    def __init__(self):
        pass

    def setup(self):
        self.create_units()
        self.create_heroes()
        self.read_images()

    def create_units(self):
        with open('resources/units.yml', 'r') as _f:
            _us = yaml.safe_load(_f)
            for _k, _d in _us['unit'].items():
                self.units[_k] = Unit(_k, _d)

    def create_heroes(self):
        with open('resources/heroes.yml', 'r') as _f:
            _us = yaml.safe_load(_f)
            for _k, _d in _us['hero'].items():
                self.heroes[_k] = Hero(_k, _d)

    def read_images(self):
        for _u in self.units.values():
            _u.read_images()
        for _h in self.heroes.values():
            _h.read_images()


class CardBase:
    key: str = None
    key_max: str = None
    rarity: str = None
    name: str = None
    name_jp: str = None
    images: [] = None
    image_path: str = None

    def __init__(self, _key: str, _dict: dict):
        self.images = list()
        self.key = _key
        for _k, _v in _dict.items():
            setattr(self, _k, _v)
        self.key_max = f"{self.key}(Max)"

    def read_images(self):
        self.images = list()
        globname = f"{self.image_path}/**/*{self.key}*.png"
        for _i in glob.glob(globname):
            self.images.append(_i)


class Unit(CardBase):
    type: str = None
    toxic: bool = False
    image_path: str = "images/unit"

    def __init__(self, _key: str, _dict: dict):
        super().__init__(_key, _dict)

    def read_images(self):
        super().read_images()


class Hero(CardBase):
    image_path: str = "images/hero"

    def __init__(self, _key: str, _dict: dict):
        super().__init__(_key, _dict)

    def read_images(self):
        super().read_images()


class MyUnit(Unit):
    level: int = None
    pos = None

    def __init__(self):
        pass


class MyHero(Hero):
    level: int = None

    def __init__(self):
        pass


class Deck:
    hero = None
    units: list = None
    name: str = None
    critical: int = None
    trophy: int = None
