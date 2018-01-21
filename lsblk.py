import os
from typing import Dict, Optional, Callable, Any, Union, Iterator, Tuple

from .kernel import DeviceRaw
from .to_type import to_bool, to_dev_path


class DeviceLsblk(DeviceRaw):
    __PROPS_ALL: Dict[str, Optional[Callable[[str], Any]]] = {}

    alignment: Optional[int]
    __PROPS_ALL['ALIGNMENT'] = int

    disc_aln: Optional[int]
    __PROPS_ALL['DISC-ALN'] = int

    disc_gran: Optional[int]
    __PROPS_ALL['DISC-GRAN'] = int

    disc_max: Optional[int]
    __PROPS_ALL['DISC-MAX'] = int

    disc_zero: Optional[int]
    __PROPS_ALL['DISC-ZERO'] = int

    fstype: Optional[str]
    __PROPS_ALL['FSTYPE'] = None

    group: Optional[str]
    __PROPS_ALL['GROUP'] = None

    hctl: Optional[str]
    __PROPS_ALL['HCTL'] = None

    hotplug: Optional[bool]
    __PROPS_ALL['HOTPLUG'] = to_bool

    kname: Optional[str]
    __PROPS_ALL['KNAME'] = None

    label: Optional[str]
    __PROPS_ALL['LABEL'] = None

    log_sec: Optional[int]
    __PROPS_ALL['LOG-SEC'] = int,

    maj_min: Optional[str]
    __PROPS_ALL['MAJ:MIN'] = None

    min_io: Optional[int]
    __PROPS_ALL['MIN-IO'] = int

    mode: Optional[str]
    __PROPS_ALL['MODE'] = None

    model: Optional[str]
    __PROPS_ALL['MODEL'] = None

    mountpoint: Optional[str]
    __PROPS_ALL['MOUNTPOINT'] = None

    name: Optional[str]
    __PROPS_ALL['NAME'] = None

    opt_io: Optional[int]
    __PROPS_ALL['OPT-IO'] = int

    owner: Optional[str]
    __PROPS_ALL['OWNER'] = None

    partflags: Optional[str]
    __PROPS_ALL['PARTFLAGS'] = None

    partlabel: Optional[str]
    __PROPS_ALL['PARTLABEL'] = None

    parttype: Optional[str]
    __PROPS_ALL['PARTTYPE'] = None

    partuuid: Optional[str]
    __PROPS_ALL['PARTUUID'] = None

    phy_sec: Optional[int]
    __PROPS_ALL['PHY-SEC'] = int

    pkname: Optional[str]
    __PROPS_ALL['PKNAME'] = None

    ra: Optional[int]
    __PROPS_ALL['RA'] = int

    rand: Optional[int]
    __PROPS_ALL['RAND'] = int

    rev: Optional[str]
    __PROPS_ALL['REV'] = None

    rm: Optional[bool]
    __PROPS_ALL['RM'] = to_bool

    ro: Optional[bool]
    __PROPS_ALL['RO'] = to_bool

    rota: Optional[bool]
    __PROPS_ALL['ROTA'] = to_bool

    rq_size: Optional[int]
    __PROPS_ALL['RQ-SIZE'] = int

    sched: Optional[str]
    __PROPS_ALL['SCHED'] = None

    serial: Optional[str]
    __PROPS_ALL['SERIAL'] = None

    size: Optional[int]
    __PROPS_ALL['SIZE'] = int

    state: Optional[str]
    __PROPS_ALL['STATE'] = None

    subsystems: Optional[str]
    __PROPS_ALL['SUBSYSTEMS'] = None

    tran: Optional[str]
    __PROPS_ALL['TRAN'] = None

    type: Optional[str]
    __PROPS_ALL['TYPE'] = None

    uuid: Optional[str]
    __PROPS_ALL['UUID'] = None

    vendor: Optional[str]
    __PROPS_ALL['VENDOR'] = None

    wsame: Optional[bool]
    __PROPS_ALL['WSAME'] = to_bool

    zoned: Optional[str]
    __PROPS_ALL['ZONED'] = None

    def __init__(self, dev: Union[str, bytes, os.PathLike]):
        self._add_props_all(self.__PROPS_ALL)

        dev = to_dev_path(dev)
        stdout = self._run_command(['lsblk', '-ndbaro', ','.join(self.__PROPS_ALL), dev], b' ')

        stdout = filter(lambda x: x[1] != '', zip(self.__PROPS_ALL, stdout))  # type: Iterator[Tuple[str, str]]

        DeviceRaw.__init__(self, stdout)
