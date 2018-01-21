import os
from typing import Dict, Optional, Callable, Any, List, Union, Generator, Tuple, Iterator

from .kernel import DeviceRaw
from .to_type import to_partition_type, to_bool, to_split, to_dev_path


class DeviceUdevadm(DeviceRaw):
    __PROPS_ALL: Dict[str, Optional[Callable[[str], Any]]] = {}

    devlinks: Optional[List[str]]
    __PROPS_ALL['DEVLINKS'] = to_split

    devname: Optional[str]
    __PROPS_ALL['DEVNAME'] = None

    devpath: Optional[str]
    __PROPS_ALL['DEVPATH'] = None

    devtype: Optional[str]
    __PROPS_ALL['DEVTYPE'] = None

    id_ata: Optional[str]
    __PROPS_ALL['ID_ATA'] = None

    id_ata_download_microcode: Optional[bool]
    __PROPS_ALL['ID_ATA_DOWNLOAD_MICROCODE'] = to_bool

    id_ata_feature_set_apm: Optional[str]
    __PROPS_ALL['ID_ATA_FEATURE_SET_APM'] = None

    id_ata_feature_set_apm_current_value: Optional[int]
    __PROPS_ALL['ID_ATA_FEATURE_SET_APM_CURRENT_VALUE'] = int

    id_ata_feature_set_apm_enabled: Optional[bool]
    __PROPS_ALL['ID_ATA_FEATURE_SET_APM_ENABLED'] = to_bool

    id_ata_feature_set_hpa: Optional[str]
    __PROPS_ALL['ID_ATA_FEATURE_SET_HPA'] = None

    id_ata_feature_set_hpa_enabled: Optional[bool]
    __PROPS_ALL['ID_ATA_FEATURE_SET_HPA_ENABLED'] = to_bool

    id_ata_feature_set_pm: Optional[str]
    __PROPS_ALL['ID_ATA_FEATURE_SET_PM'] = None

    id_ata_feature_set_pm_enabled: Optional[bool]
    __PROPS_ALL['ID_ATA_FEATURE_SET_PM_ENABLED'] = to_bool

    id_ata_feature_set_puis: Optional[str]
    __PROPS_ALL['ID_ATA_FEATURE_SET_PUIS'] = None

    id_ata_feature_set_puis_enabled: Optional[bool]
    __PROPS_ALL['ID_ATA_FEATURE_SET_PUIS_ENABLED'] = to_bool

    id_ata_feature_set_security: Optional[str]
    __PROPS_ALL['ID_ATA_FEATURE_SET_SECURITY'] = None

    id_ata_feature_set_security_enabled: Optional[bool]
    __PROPS_ALL['ID_ATA_FEATURE_SET_SECURITY_ENABLED'] = to_bool

    id_ata_feature_set_security_enhanced_erase_unit_min: Optional[int]
    __PROPS_ALL['ID_ATA_FEATURE_SET_SECURITY_ENHANCED_ERASE_UNIT_MIN'] = int

    id_ata_feature_set_security_erase_unit_min: Optional[int]
    __PROPS_ALL['ID_ATA_FEATURE_SET_SECURITY_ERASE_UNIT_MIN'] = int

    id_ata_feature_set_security_frozen: Optional[str]
    __PROPS_ALL['ID_ATA_FEATURE_SET_SECURITY_FROZEN'] = None

    id_ata_feature_set_smart: Optional[str]
    __PROPS_ALL['ID_ATA_FEATURE_SET_SMART'] = None

    id_ata_feature_set_smart_enabled: Optional[bool]
    __PROPS_ALL['ID_ATA_FEATURE_SET_SMART_ENABLED'] = to_bool

    id_ata_rotation_rate_rpm: Optional[int]
    __PROPS_ALL['ID_ATA_ROTATION_RATE_RPM'] = int

    id_ata_sata: Optional[str]
    __PROPS_ALL['ID_ATA_SATA'] = None

    id_ata_sata_signal_rate_gen1: Optional[str]
    __PROPS_ALL['ID_ATA_SATA_SIGNAL_RATE_GEN1'] = None

    id_ata_sata_signal_rate_gen2: Optional[str]
    __PROPS_ALL['ID_ATA_SATA_SIGNAL_RATE_GEN2'] = None

    id_ata_write_cache: Optional[str]
    __PROPS_ALL['ID_ATA_WRITE_CACHE'] = None

    id_ata_write_cache_enabled: Optional[bool]
    __PROPS_ALL['ID_ATA_WRITE_CACHE_ENABLED'] = to_bool

    id_bus: Optional[str]
    __PROPS_ALL['ID_BUS'] = None

    id_fs_label: Optional[str]
    __PROPS_ALL['ID_FS_LABEL'] = None

    id_fs_label_enc: Optional[str]
    __PROPS_ALL['ID_FS_LABEL_ENC'] = None

    id_fs_type: Optional[str]
    __PROPS_ALL['ID_FS_TYPE'] = None

    id_fs_usage: Optional[str]
    __PROPS_ALL['ID_FS_USAGE'] = None

    id_fs_uuid: Optional[str]
    __PROPS_ALL['ID_FS_UUID'] = None

    id_fs_uuid_enc: Optional[str]
    __PROPS_ALL['ID_FS_UUID_ENC'] = None

    id_fs_uuid_sub: Optional[str]
    __PROPS_ALL['ID_FS_UUID_SUB'] = None

    id_fs_uuid_sub_enc: Optional[str]
    __PROPS_ALL['ID_FS_UUID_SUB_ENC'] = None

    id_fs_version: Optional[str]
    __PROPS_ALL['ID_FS_VERSION'] = None

    id_instance: Optional[str]
    __PROPS_ALL['ID_INSTANCE'] = None

    id_model: Optional[str]
    __PROPS_ALL['ID_MODEL'] = None

    id_model_enc: Optional[str]
    __PROPS_ALL['ID_MODEL_ENC'] = None

    id_model_id: Optional[str]
    __PROPS_ALL['ID_MODEL_ID'] = None

    id_part_entry_disk: Optional[str]
    __PROPS_ALL['ID_PART_ENTRY_DISK'] = None

    id_part_entry_flags: Optional[str]
    __PROPS_ALL['ID_PART_ENTRY_FLAGS'] = None

    id_part_entry_name: Optional[str]
    __PROPS_ALL['ID_PART_ENTRY_NAME'] = None

    id_part_entry_number: Optional[str]
    __PROPS_ALL['ID_PART_ENTRY_NUMBER'] = None

    id_part_entry_offset: Optional[str]
    __PROPS_ALL['ID_PART_ENTRY_OFFSET'] = None

    id_part_entry_scheme: Optional[str]
    __PROPS_ALL['ID_PART_ENTRY_SCHEME'] = None

    id_part_entry_size: Optional[str]
    __PROPS_ALL['ID_PART_ENTRY_SIZE'] = None

    id_part_entry_type: Optional[str]
    __PROPS_ALL['ID_PART_ENTRY_TYPE'] = to_partition_type

    id_part_entry_uuid: Optional[str]
    __PROPS_ALL['ID_PART_ENTRY_UUID'] = None

    id_part_table_type: Optional[str]
    __PROPS_ALL['ID_PART_TABLE_TYPE'] = None

    id_part_table_uuid: Optional[str]
    __PROPS_ALL['ID_PART_TABLE_UUID'] = None

    id_path: Optional[str]
    __PROPS_ALL['ID_PATH'] = None

    id_path_tag: Optional[str]
    __PROPS_ALL['ID_PATH_TAG'] = None

    id_revision: Optional[str]
    __PROPS_ALL['ID_REVISION'] = None

    id_serial: Optional[str]
    __PROPS_ALL['ID_SERIAL'] = None

    id_serial_short: Optional[str]
    __PROPS_ALL['ID_SERIAL_SHORT'] = None

    id_type: Optional[str]
    __PROPS_ALL['ID_TYPE'] = None

    id_usb_driver: Optional[str]
    __PROPS_ALL['ID_USB_DRIVER'] = None

    id_usb_interfaces: Optional[str]
    __PROPS_ALL['ID_USB_INTERFACES'] = None

    id_usb_interface_num: Optional[str]
    __PROPS_ALL['ID_USB_INTERFACE_NUM'] = None

    id_vendor: Optional[str]
    __PROPS_ALL['ID_VENDOR'] = None

    id_vendor_enc: Optional[str]
    __PROPS_ALL['ID_VENDOR_ENC'] = None

    id_vendor_id: Optional[str]
    __PROPS_ALL['ID_VENDOR_ID'] = None

    id_wwn: Optional[str]
    __PROPS_ALL['ID_WWN'] = None

    id_wwn_with_extension: Optional[str]
    __PROPS_ALL['ID_WWN_WITH_EXTENSION'] = None

    major: Optional[int]
    __PROPS_ALL['MAJOR'] = int

    minor: Optional[int]
    __PROPS_ALL['MINOR'] = int

    partn: Optional[str]
    __PROPS_ALL['PARTN'] = None

    partname: Optional[str]
    __PROPS_ALL['PARTNAME'] = None

    subsystem: Optional[str]
    __PROPS_ALL['SUBSYSTEM'] = None

    systemd_wants: Optional[str]
    __PROPS_ALL['SYSTEMD_WANTS'] = None

    tags: Optional[str]
    __PROPS_ALL['TAGS'] = None

    udisks_ignore: Optional[str]
    __PROPS_ALL['UDISKS_IGNORE'] = None

    usec_initialized: Optional[str]
    __PROPS_ALL['USEC_INITIALIZED'] = None

    def __init__(self, dev: Union[str, bytes, os.PathLike]):
        self._add_props_all(self.__PROPS_ALL)

        dev = to_dev_path(dev)
        tmp = self._run_command(['udevadm', 'info', '--query=property', '-x', '--name={}'.format(dev)], b'\n')

        stdout = (x.split('=', 1) for x in tmp)  # type: Generator[List[str, str], None, None]
        stdout = ((x[0], x[1].strip("'").strip()) for x in stdout)  # type: Generator[Tuple[str, str], None, None]
        stdout = filter(lambda x: x[1] != '', stdout)  # type: Iterator[Tuple[str, str]]

        DeviceRaw.__init__(self, stdout)
