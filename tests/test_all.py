from ..all import Device


def test_device():
    dev = Device('/dev/sda')
    assert dev
