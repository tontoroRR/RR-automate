import pytest
from modules.gsheet import Spreadsheet


@pytest.mark.gsheet
class TestSpreadsheet:
    def test__init__(self):
        assert 1 == 1
