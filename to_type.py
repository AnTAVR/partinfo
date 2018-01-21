import os


def to_partition_type(x: str) -> str:
    """
    :type x: str
    :rtype: str
    """
    try:
        tmp = int(x, 16)
        tmp = '{:#04x}'.format(tmp)
    except ValueError:
        tmp = str(x)
    return tmp


def to_bool(x):
    """
    :type x: str | int | any
    :rtype: bool | None
    """
    try:
        tmp = int(x)
    except (ValueError, TypeError):
        return

    return bool(tmp)


def to_split(x):
    """
    :type x: str
    :rtype: list[str]
    """
    return x.split()


_DEV_PATH = '/dev'


def to_dev_path(dev):
    """
    :type dev: str | bytes | os.PathLike
    :rtype: str | bytes
    """
    if dev.startswith(_DEV_PATH):
        return dev
    return os.path.join(_DEV_PATH, dev)
