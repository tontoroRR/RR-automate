# stats information of Rush Royale, say Units, Heroes, User Info, Event
import yaml
import glob


rarity = {"legendary": 1, "epic": 2, "rare": 3, "common": 4}
type = {"Damage": 1, "Support": 2, "Debuff": 3, "Special": 4}


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
        with open('resources/units.yml', 'r', encoding='utf-8') as _f:
            _us = yaml.safe_load(_f)
            for _k, _d in _us['unit'].items():
                self.units[_k] = Unit(_k, _d)

    def create_heroes(self):
        with open('resources/heroes.yml', 'r', encoding='utf-8') as _f:
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
        self.images, self.key = list(), _key
        for _k, _v in _dict.items():
            setattr(self, _k, _v)
        self.key_max = f"{self.key}(Max)"

    def __lt__(self, other) -> bool:
        if self.rating() == other.rating():
            return self.name < other.name
        else:
            return self.rating() < other.rating()

    def __gt__(self, other) -> bool:
        return not self.__lt__(self, other)

    def __str__(self) -> str:
        return f"{self.name}"

    def read_images(self):
        self.images = list()
        globname = f"{self.image_path}/**/*{self.key}*.png"
        for _i in glob.glob(globname):
            self.images.append(_i.replace('/', '\\'))
        sorted(self.images)

    def rating(self) -> int:
        return 0

    def create_my_card(self, _imgs: list) -> 'CardBase':
        pass


class Unit(CardBase):
    type: str = None
    toxic: bool = False
    image_path: str = "images/unit"
    mana_max: int = 5

    def rating(self) -> int:
        # 1. Legendary * Damage -> Mana(Rariry -> Type) -> NoMana(R -> T)
        # 2. Type : Damage -> Support -> Debuff -> Special
        # 3. No Mana Legies : Scrapper, Summoner
        _rate = 20000
        if all([self.rarity == 'legendary', self.type == 'Damage']):
            _rate = 10000
        elif 2 < self.mana_max:
            _rate += rarity[self.rarity] * 10
            _rate += type[self.type]
        else:
            _rate += rarity[self.rarity] * 1000
            _rate += type[self.type] * 10
        return _rate

    def create_my_card(self, _imgs: list) -> 'Unit':
        _m = MyUnit()
        _m.create_from(self, _imgs)
        return _m


class Hero(CardBase):
    image_path: str = "images/hero"

    def rating(self) -> int:
        # 1. By rarity
        return rarity[self.rarity]

    def create_my_card(self, _imgs: list) -> 'Hero':
        _m = MyHero()
        _m.create_from(self, _imgs)
        return _m


class MyUnit(Unit):
    level: int = None
    pos = None

    def __init__(self):
        self.__name = ''
        self.__name_jp = ''
        pass

    @property
    def name(self):
        if self.level == 15:
            return f"{self.__name}(Max)"
        else:
            return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def name_jp(self):
        if self.level == 15:
            return f"{self.__name_jp}(Max)"
        else:
            return self.__name_jp

    @name_jp.setter
    def name_jp(self, name_jp):
        self.__name_jp = name_jp

    def create_from(self, _c: CardBase, _imgs: list) -> 'MyUnit':
        for _k, _v in vars(_c).items():
            setattr(self, _k, _v)
        if [_i for _i in _imgs if ("Max" in _i) & (_i in self.images)]:
            self.level = 15


class MyHero(Hero):
    level: int = None

    def __init__(self):
        pass

    def name(self):
        if self.level == 20:
            return f"{self.name}(Max)"
        else:
            return self.name

    def name_jp(self):
        pass

    def create_from(self, _c: CardBase, _imgs: list) -> 'MyHero':
        for _k, _v in vars(_c).items():
            setattr(self, _k, _v)


class Deck:
    hero = None
    units: list = None
    name: str = None
    critical: int = None
    trophy: int = None
