import os
import subprocess
from typing import TypeVar, Union, Generator, Optional, Tuple, List

from .lsblk import DeviceLsblk
from .partition_types import get_part_txt
from .to_type import to_dev_path
from .udevadm import DeviceUdevadm

BOOT_PARTFLAGS = ('21686148-6449-6e6f-744e-656564454649', '0x80', '0x8000000000000000')
BOOT_PARTTYPES = ('c12a7328-f81f-11d2-ba4b-00a0c93ec93b', '0xef')
SWAP_PARTTYPES = ('0x82', '0657fd6d-a4ab-43c4-84e5-0933c84b4f4f')

BOOT_PARTFLAGS: Tuple[str, ...] = tuple(map(str.lower, BOOT_PARTFLAGS))
BOOT_PARTTYPES: Tuple[str, ...] = tuple(map(str.lower, BOOT_PARTTYPES))
SWAP_PARTTYPES: Tuple[str, ...] = tuple(map(str.lower, SWAP_PARTTYPES))

DeviceType = TypeVar('DeviceType', bound='Device')


class Device(DeviceUdevadm, DeviceLsblk):
    __MY_PROPS = ('is_ssd', 'parttype_name', 'boot', 'swap',
                  'model_dec', 'can_be_formatted')

    def __init__(self, dev: Union[str, bytes, os.PathLike]):
        # self._duplicate = True
        DeviceUdevadm.__init__(self, dev)
        DeviceLsblk.__init__(self, dev)
        self._add_my_props(self.__MY_PROPS)

    @classmethod
    def get_devices(cls, ret_cls: bool = True) -> Generator[Union[DeviceType, str, bytes, os.PathLike], None, None]:
        ret = subprocess.run(['lsblk', '-nro', 'NAME'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        ret.check_returncode()

        stdout: bytes = ret.stdout
        stdout: List[bytes] = stdout.strip().split(b'\n')
        stdout: Generator[str, None, None] = (x.decode().strip() for x in stdout)
        for x in stdout:
            if ret_cls:
                yield cls(x)
            else:
                yield to_dev_path(x)

    @property
    def is_ssd(self) -> Optional[bool]:
        if not self.rota:
            return True
        if self.rm and self.tran == 'usb':
            return True
        value = self.pkname
        if value:
            try:
                tmp = self.__class__(value)
                return tmp.is_ssd
            except subprocess.CalledProcessError:
                pass

    @property
    def can_be_formatted(self) -> Optional[bool]:
        if self.mountpoint:
            return False
        if self.devtype == 'disk':
            for device in self.get_devices(False):
                if device.startswith(self.devname):
                    try:
                        device = self.__class__(device)
                        if device.mountpoint:
                            return False
                    except subprocess.CalledProcessError:
                        continue
        return True

    @property
    def parttype_name(self) -> Optional[str]:
        return get_part_txt(self.id_part_entry_type)

    @property
    def boot(self) -> Optional[str]:
        ret = '*'
        if self.id_part_entry_flags in BOOT_PARTFLAGS:
            ret += 'b'
        if self.id_part_entry_type in BOOT_PARTTYPES:
            ret += 'e'
        if len(ret) > 1:
            return ret

    @property
    def swap(self) -> Optional[bool]:
        if self.id_part_entry_type in SWAP_PARTTYPES:
            return True

    @property
    def model_dec(self) -> Optional[str]:
        return self._decode(self.id_model_enc)
