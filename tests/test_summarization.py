from modules.rushroyale_stats import RushRoyaleStats
import yaml
import pytest


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


class TestSummarization:
    def test__load_deck_yaml(self, decks):
        assert 10 == len(decks)

    def test__apply_unit_stats(self, decks, stats):
        pass

    def test__summarize_deck(self, decks):
        assert 10 == len(decks)
