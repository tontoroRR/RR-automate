from modules.rushroyale_stats import Hero, Unit, RushRoyaleStats


class TestHero:
    def test__init__(self):
        dict = {
            'key': 'Gadget',
            'name': 'Gadget',
            'rarity': 'epic',
            'name_jp': 'ガジェット',
            'unlock': {'arena': 7}
        }
        h = Hero('Gadget', dict)
        h.read_images()
        assert h.key == 'Gadget'
        assert h.name == 'Gadget'
        assert h.rarity == 'epic'
        assert h.name_jp == 'ガジェット'
        assert h.unlock == {'arena': 7}
        assert h.images == [
            'images/hero/epic/Gadget.png'.replace('/', '\\'),
        ]

    def test__rating(self):
        gadget = Hero('Gadget', {'key': 'Gadget', 'rarity': 'epic'})
        zeus = Hero('Zeus', {'key': 'Zeus', 'rarity': 'legendary'})
        assert gadget.rating() == 2
        assert zeus.rating() == 1

    def test_sorted(self):
        gadget = Hero('Gadget', {'key': 'Gadget', 'rarity': 'epic'})
        zeus = Hero('Zeus', {'key': 'Zeus', 'rarity': 'legendary'})
        heroes = [gadget, zeus]
        h = sorted(heroes)
        assert h[0] == zeus

    def test__create_my_card(self):
        gadget = Hero('Gadget', {'key': 'Gadget', 'rarity': 'epic'})
        gadget.read_images()


class TestUnit:
    def test__init__(self):
        dict = {
            'key': 'Alchemist',
            'name': 'Alchemist',
            'rarity': 'rare',
            'type': 'Damage',
            'name_jp': 'アルケミスト'
        }
        h = Unit('Alchemist', dict)
        h.read_images()
        assert h.key == 'Alchemist'
        assert h.name == 'Alchemist'
        assert h.rarity == 'rare'
        assert h.type == 'Damage'
        assert h.name_jp == 'アルケミスト'
        assert h.images == sorted([
            r'images\unit\rare\Alchemist.png',
            r'images\unit\rare\AlchemistMax.png',
            r'images\unit\rare\AlchemistMax_ALT_.png',
        ])

    def test__rating(self):
        _d1 = {'key': 'Rogue', 'name': 'Rogue',
               'rarity': 'common', 'type': 'Damage'}
        rogue = Unit('Rogue', _d1)
        _d2 = {'key': 'Shaman', 'name': 'Shaman',
               'rarity': 'legendary', 'type': 'Special',
               'toxic': True}
        shaman = Unit('Shaman', _d2)
        _d3 = {'key': 'Monk', 'name': 'Monk',
               'rarity': 'legendary', 'type': 'Damage',
               'toxic': False}
        monk = Unit('Monk', _d3)
        assert rogue.rating() == 10041
        assert shaman.rating() == 20014
        assert monk.rating() == 10011

    def test_sorted(self):
        _d1 = {'key': 'KnightStatue', 'name': 'Knight Statue',
               'rarity': 'legendary', 'type': 'Support'}
        ks = Unit('KnightStatue', _d1)
        _d2 = {'key': 'Chemist', 'name': 'Chemist',
               'rarity': 'rare', 'type': 'Debuff'}
        chem = Unit('Shaman', _d2)
        _d3 = {'key': 'Harleyquin', 'name': 'Harleyquin',
               'rarity': 'legendary', 'type': 'Special'}
        hq = Unit('Harleyquin', _d3)
        _d4 = {'key': 'Scrapper', 'name': 'Scrapper',
               'rarity': 'legendary', 'type': 'Support',
               'mana_max': 2}
        scr = Unit('Harleyquin', _d4)
        _d5 = {'key': 'SpiritMaster', 'name': 'Spirit Master',
               'rarity': 'legendary', 'type': 'Damage',
               'mana_max': 11}
        sm = Unit('SpiritMaster', _d5)

        units = [chem, ks, hq, scr, sm]
        u = sorted(units)

        assert u[0] == sm
        assert u[1] == ks
        assert u[2] == hq
        assert u[3] == chem
        assert u[4] == scr
        assert u == [sm, ks, hq, chem, scr]


class TestMyHero:
    def test__init__(self):
        _d = {'key': 'KnightStatue', 'name': 'Knight Statue',
              'name_jp': '騎士像', 'rarity': 'legendary', 'type': 'Support'}
        ks = Unit('KnightStatue', _d)
        ks.read_images()
        _imgs = [
                    r"images\unit\legendary\KnightStatue.png",
                    r"images\unit\legendary\KnightStatueMax.png",
                    r"images\unit\legendary\SpiritMasterMax.png",
                ]
        my_ks = ks.create_my_card(_imgs)
        my_ks.level = 15
        assert my_ks.name == "Knight Statue(Max)"
        assert str(my_ks) == "Knight Statue(Max)"
        assert my_ks.name_jp == "騎士像(Max)"
        assert my_ks.level == 15


class TestMyUnit:
    def test__init__(self):
        gadget = Hero('Gadget',
                      {'key': 'Gadget', 'name': 'Gadget',
                       'name_jp': 'ガジェット', 'rarity': 'epic'})
        gadget.read_images()
        _imgs = [
                    r"images\hero\epic\Gadget.png",
                ]
        my_hero = gadget.create_my_card(_imgs)
        assert my_hero.name == "Gadget"
        assert str(my_hero) == "Gadget"
        assert my_hero.name_jp == "ガジェット"
        assert my_hero.level is None
    pass


class TestRushRoyaleStats:
    def test_setup(self):
        rr = RushRoyaleStats()
        rr.setup()
        assert len(rr.heroes) == 14
        for h in rr.heroes.values():
            for img in h.images:
                assert rf"{h.rarity}\{h.name.replace(' ', '')}" in img
        assert len(rr.units) == 67
        for u in rr.units.values():
            for img in u.images:
                assert rf"{u.rarity}\{u.name.replace(' ', '')}" in img
