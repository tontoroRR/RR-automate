from modules.utils import Utils


class TestUtils:
    def test__can_convert_int_to_col(self):
        assert Utils.convert_int_to_col(1) == 'A'
        assert Utils.convert_int_to_col(26) == 'Z'
        assert Utils.convert_int_to_col(27) == 'AA'
        assert Utils.convert_int_to_col(702) == 'ZZ'

    def test__can_convert_col_to_int(self):
        assert Utils.convert_col_to_int('A') == 1
        assert Utils.convert_col_to_int('Z') == 26
        assert Utils.convert_col_to_int('AA') == 27
        assert Utils.convert_col_to_int('ZZ') == 702
