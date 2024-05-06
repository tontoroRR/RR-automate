from modules.rushroyale_stats import RushRoyaleStats, Deck
from modules.summarizer import Summarizer
import yaml
import pytest

import pdb


@pytest.fixture
def decks():
    with open('tests/resources/summarize1.yml', 'r') as _yml:
        decks = yaml.safe_load(_yml)['decks']
    return decks


@pytest.fixture
def stats():
    rrs = RushRoyaleStats()
    rrs.setup()
    return rrs
    pass


class TestSummarization:
    def test__load_deck_yaml(self, decks, stats):
        assert 10 == len(decks)
        _d = Deck()
        _d.load(decks[0], stats)
        assert _d.hero.name == 'Zeus'
        assert _d.units[0].name == 'Riding Hood(Max)'

    def test__summarize_deck(self, decks, stats):
        my_decks = []
        for _d in decks:
            __d = Deck()
            __d.load(_d, stats)
            my_decks.append(__d)
        assert my_decks[0].hero.name == 'Zeus'
