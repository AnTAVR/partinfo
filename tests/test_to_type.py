from ..to_type import to_partition_type, to_bool, to_split, to_dev_path


def test_to_partition_type():
    assert to_partition_type('') == ''
    assert to_partition_type('234') == '0x234'
    assert to_partition_type('0x234') == '0x234'
    assert to_partition_type('ashgd') == 'ashgd'


def test_to_bool():
    assert to_bool(1) is True
    assert to_bool('1') is True
    assert to_bool('-100') is True
    assert to_bool(-100) is True
    assert to_bool(0) is False
    assert to_bool('0') is False
    assert to_bool(None) is None
    assert to_bool('121dgh') is None


def test_to_split():
    assert to_split('') == []
    assert to_split('a b1 \n b2 c ') == ['a', 'b1', 'b2', 'c']


def test_to_dev_path():
    assert to_dev_path('') == '/dev/'
    assert to_dev_path('/dev/ddd') == '/dev/ddd'
    assert to_dev_path('/de/dv/ddd') == '/de/dv/ddd'
    assert to_dev_path('de/dv/ddd') == '/dev/de/dv/ddd'
    assert to_dev_path('ddd/dev/') == '/dev/ddd/dev/'
