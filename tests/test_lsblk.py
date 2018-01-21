from ..lsblk import DeviceLsblk


def test_device():
    dev = DeviceLsblk('/dev/sda')
    assert dev
