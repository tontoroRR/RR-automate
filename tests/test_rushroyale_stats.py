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
            'images/unit/rare/AlchemistMax.png'.replace('/', '\\'),
            'images/unit/rare/AlchemistMax_ALT_.png'.replace('/', '\\'),
        ])


class TestRushRoyaleStats:
    # TODO
    def test_setup(self):
        rr = RushRoyaleStats()
        rr.setup()
        assert len(rr.heroes) == 13
        assert len(rr.units) == 67
