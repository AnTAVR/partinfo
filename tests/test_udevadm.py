from ..udevadm import DeviceUdevadm


def test_device():
    dev = DeviceUdevadm('/dev/sda')
    assert dev
