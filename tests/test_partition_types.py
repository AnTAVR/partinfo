from ..partition_types import get_part_txt


def test_get_part_txt_ok1():
    assert get_part_txt('0xc7') == 'Syrinx'


def test_get_part_txt_ok2():
    assert get_part_txt('3CB8E202-3B7E-47DD-8A3C-7FF2A13CFCEC') == 'ChromeOS root fs'


def test_get_part_txt_space():
    assert get_part_txt('') is None


def test_get_part_txt_none():
    assert get_part_txt(None) is None


def test_get_part_txt_int_ok():
    assert get_part_txt(12) == 'W95 FAT32 (LBA)'


def test_get_part_txt_int():
    assert get_part_txt(124536346) is None


def test_get_part_txt_float():
    assert get_part_txt(124536346.076) is None
