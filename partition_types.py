from typing import Dict

PARTITION_TYPES = {
    # https://raw.githubusercontent.com/karelzak/util-linux/master/include/pt-mbr-partnames.h
    # http://git.kernel.org/cgit/utils/util-linux/util-linux.git/tree/include/pt-mbr-partnames.h
    '0x00': 'Empty',
    '0x01': 'FAT12',
    '0x02': 'XENIX root',
    '0x03': 'XENIX usr',
    '0x04': 'FAT16 <32M',
    '0x05': 'Extended',  # DOS 3.3+ extended partition
    '0x06': 'FAT16',  # DOS 16-bit >=32M
    '0x07': 'HPFS/NTFS/exFAT',  # OS/2 IFS, eg, HPFS or NTFS or QNX or exFAT
    '0x08': 'AIX',  # AIX boot (AIX -- PS/2 port) or SplitDrive
    '0x09': 'AIX bootable',  # AIX data or Coherent
    '0x0a': 'OS/2 Boot Manager',  # OS/2 Boot Manager
    '0x0b': 'W95 FAT32',
    '0x0c': 'W95 FAT32 (LBA)',  # LBA really is `Extended Int 13h'
    '0x0e': 'W95 FAT16 (LBA)',
    '0x0f': 'W95 Ext\'d (LBA)',
    '0x10': 'OPUS',
    '0x11': 'Hidden FAT12',
    '0x12': 'Compaq diagnostics',
    '0x14': 'Hidden FAT16 <32M',
    '0x16': 'Hidden FAT16',
    '0x17': 'Hidden HPFS/NTFS',
    '0x18': 'AST SmartSleep',
    '0x1b': 'Hidden W95 FAT32',
    '0x1c': 'Hidden W95 FAT32 (LBA)',
    '0x1e': 'Hidden W95 FAT16 (LBA)',
    '0x24': 'NEC DOS',
    '0x27': 'Hidden NTFS WinRE',
    '0x39': 'Plan 9',
    '0x3c': 'PartitionMagic recovery',
    '0x40': 'Venix 80286',
    '0x41': 'PPC PReP Boot',
    '0x42': 'SFS',
    '0x4d': 'QNX4.x',
    '0x4e': 'QNX4.x 2nd part',
    '0x4f': 'QNX4.x 3rd part',
    '0x50': 'OnTrack DM',
    '0x51': 'OnTrack DM6 Aux1',  # (or Novell)
    '0x52': 'CP/M',  # CP/M or Microport SysV/AT
    '0x53': 'OnTrack DM6 Aux3',
    '0x54': 'OnTrackDM6',
    '0x55': 'EZ-Drive',
    '0x56': 'Golden Bow',
    '0x5c': 'Priam Edisk',
    '0x61': 'SpeedStor',
    '0x63': 'GNU HURD or SysV',  # GNU HURD or Mach or Sys V/386 (such as ISC UNIX)
    '0x64': 'Novell Netware 286',
    '0x65': 'Novell Netware 386',
    '0x70': 'DiskSecure Multi-Boot',
    '0x75': 'PC/IX',
    '0x80': 'Old Minix',  # Minix 1.4a and earlier
    '0x81': 'Minix / old Linux',  # Minix 1.4b and later
    '0x82': 'Linux swap / Solaris',
    '0x83': 'Linux',
    '0x84': 'OS/2 hidden or Intel hibernation',  # OS/2 hidden C: drive, hibernation type Microsoft APM
    #  or hibernation Intel Rapid Start
    '0x85': 'Linux extended',
    '0x86': 'NTFS volume set',
    '0x87': 'NTFS volume set',
    '0x88': 'Linux plaintext',
    '0x8e': 'Linux LVM',
    '0x93': 'Amoeba',
    '0x94': 'Amoeba BBT',  # (bad block table)
    '0x9f': 'BSD/OS',  # BSDI
    '0xa0': 'IBM Thinkpad hibernation',
    '0xa5': 'FreeBSD',  # various BSD flavours
    '0xa6': 'OpenBSD',
    '0xa7': 'NeXTSTEP',
    '0xa8': 'Darwin UFS',
    '0xa9': 'NetBSD',
    '0xab': 'Darwin boot',
    '0xaf': 'HFS / HFS+',
    '0xb7': 'BSDI fs',
    '0xb8': 'BSDI swap',
    '0xbb': 'Boot Wizard hidden',
    '0xbc': 'Acronis FAT32 LBA',  # hidden (+0xb0) Acronis Secure Zone (backup software)
    '0xbe': 'Solaris boot',
    '0xbf': 'Solaris',
    '0xc1': 'DRDOS/sec (FAT-12)',
    '0xc4': 'DRDOS/sec (FAT-16 < 32M)',
    '0xc6': 'DRDOS/sec (FAT-16)',
    '0xc7': 'Syrinx',
    '0xda': 'Non-FS data',
    '0xdb': 'CP/M / CTOS / ...',  # CP/M or Concurrent CP/M or Concurrent DOS or CTOS
    '0xde': 'Dell Utility',  # Dell PowerEdge Server utilities
    '0xdf': 'BootIt',  # BootIt EMBRM
    '0xe1': 'DOS access',  # DOS access or SpeedStor 12-bit FAT extended partition
    '0xe3': 'DOS R/O',  # DOS R/O or SpeedStor
    '0xe4': 'SpeedStor',  # SpeedStor 16-bit FAT extended partition < 1024 cyl.
    '0xea': 'Rufus alignment',  # Rufus extra partition for alignment
    '0xeb': 'BeOS fs',
    '0xee': 'GPT',  # Intel EFI GUID Partition Table
    '0xef': 'EFI (FAT-12/16/32)',  # Intel EFI System Partition
    '0xf0': 'Linux/PA-RISC boot',  # Linux/PA-RISC boot loader
    '0xf1': 'SpeedStor',
    '0xf4': 'SpeedStor',  # SpeedStor large partition
    '0xf2': 'DOS secondary',  # DOS 3.3+ secondary
    '0xfb': 'VMware VMFS',
    '0xfc': 'VMware VMKCORE',  # VMware kernel dump partition
    '0xfd': 'Linux raid autodetect',  # Linux raid partition with autodetect using persistent superblock
    '0xfe': 'LANstep',  # SpeedStor >1024 cyl. or LANstep
    '0xff': 'BBT',  # Xenix Bad Block Table

    # https://github.com/karelzak/util-linux/blob/cbebd20d26b8d06e28e67a07050967668af7ce08/libfdisk/src/gpt.c
    # http://git.kernel.org/cgit/utils/util-linux/util-linux.git/tree/libfdisk/src/gpt.c
    # Generic OS
    'C12A7328-F81F-11D2-BA4B-00A0C93EC93B': 'EFI System',

    '024DEE41-33E7-11D3-9D69-0008C781F39F': 'MBR partition scheme',
    'D3BFE2DE-3DAF-11DF-BA40-E3A556D89593': 'Intel Fast Flash',

    # Hah!IdontneedEFI
    '21686148-6449-6E6F-744E-656564454649': 'BIOS boot',

    # NIH syndrome
    'F4019732-066E-4E12-8273-346C5641494F': 'Sony boot partition',
    'BFBFAFE7-A34F-448A-9A5B-6213EB736C22': 'Lenovo boot partition',

    # PowerPC reference platform boot partition
    '9E1A2D38-C612-4316-AA26-8B49521E5A8B': 'PowerPC PReP boot',

    # Open Network Install Environment
    '7412F7D5-A156-4B13-81DC-867174929325': 'ONIE boot',
    'D4E6E2CD-4469-46F3-B5CB-1BFF57AFC149': 'ONIE config',

    # Windows
    'E3C9E316-0B5C-4DB8-817D-F92DF00215AE': 'Microsoft reserved',
    'EBD0A0A2-B9E5-4433-87C0-68B6B72699C7': 'Microsoft basic data',
    '5808C8AA-7E8F-42E0-85D2-E1E90434CFB3': 'Microsoft LDM metadata',
    'AF9B60A0-1431-4F62-BC68-3311714A69AD': 'Microsoft LDM data',
    'DE94BBA4-06D1-4D40-A16A-BFD50179D6AC': 'Windows recovery environment',
    '37AFFC90-EF7D-4E96-91C3-2D7AE055B174': 'IBM General Parallel Fs',
    'E75CAF8F-F680-4CEE-AFA3-B001E56EFC2D': 'Microsoft Storage Spaces',
    # HP-UX
    '75894C1E-3AEB-11D3-B7C1-7B03A0000000': 'HP-UX data',
    'E2A1E728-32E3-11D6-A682-7B03A0000000': 'HP-UX service',

    # Linux (http://www.freedesktop.org/wiki/Specifications/DiscoverablePartitionsSpec)
    '0657FD6D-A4AB-43C4-84E5-0933C84B4F4F': 'Linux swap',
    '0FC63DAF-8483-4772-8E79-3D69D8477DE4': 'Linux filesystem',
    '3B8F8425-20E0-4F3B-907F-1A25A76F98E8': 'Linux server data',
    '44479540-F297-41B2-9AF7-D131D5F0458A': 'Linux root (x86)',
    '69DAD710-2CE4-4E3C-B16C-21A1D49ABED3': 'Linux root (ARM)',
    '4F68BCE3-E8CD-4DB1-96E7-FBCAF984B709': 'Linux root (x86-64)',
    'B921B045-1DF0-41C3-AF44-4C6F280D3FAE': 'Linux root (ARM-64)',
    '993D8D3D-F80E-4225-855A-9DAF8ED7EA97': 'Linux root	(IA-64)',
    '8DA63339-0007-60C0-C436-083AC8230908': 'Linux reserved',
    '933AC7E1-2EB4-4F13-B844-0E14E2AEF915': 'Linux home',
    'A19D880F-05FC-4D3B-A006-743F0F84911E': 'Linux RAID',
    'BC13C2FF-59E6-4262-A352-B275FD6F7172': 'Linux extended boot',
    'E6D6D379-F507-44C2-A23C-238F2A3DF928': 'Linux LVM',
    # ... too crazy, ignore for now:
    #    '7FFEC5C9-2D00-49B7-8941-3EA10A5586B7': 'Linux plain dm-crypt',
    #    'CA7D7CCB-63ED-4C53-861C-1742536059CC': 'Linux LUKS',
    # FreeBSD
    '516E7CB4-6ECF-11D6-8FF8-00022D09712B': 'FreeBSD data',
    '83BD6B9D-7F41-11DC-BE0B-001560B84F0F': 'FreeBSD boot',
    '516E7CB5-6ECF-11D6-8FF8-00022D09712B': 'FreeBSD swap',
    '516E7CB6-6ECF-11D6-8FF8-00022D09712B': 'FreeBSD UFS',
    '516E7CBA-6ECF-11D6-8FF8-00022D09712B': 'FreeBSD ZFS',
    '516E7CB8-6ECF-11D6-8FF8-00022D09712B': 'FreeBSD Vinum',

    # Apple OSX
    '48465300-0000-11AA-AA11-00306543ECAC': 'Apple HFS/HFS+',
    '55465300-0000-11AA-AA11-00306543ECAC': 'Apple UFS',
    '52414944-0000-11AA-AA11-00306543ECAC': 'Apple RAID',
    '52414944-5F4F-11AA-AA11-00306543ECAC': 'Apple RAID offline',
    '426F6F74-0000-11AA-AA11-00306543ECAC': 'Apple boot',
    '4C616265-6C00-11AA-AA11-00306543ECAC': 'Apple label',
    '5265636F-7665-11AA-AA11-00306543ECAC': 'Apple TV recovery',
    '53746F72-6167-11AA-AA11-00306543ECAC': 'Apple Core storage',

    # Solaris
    '6A82CB45-1DD2-11B2-99A6-080020736631': 'Solaris boot',
    '6A85CF4D-1DD2-11B2-99A6-080020736631': 'Solaris root',
    # same as Apple ZFS
    '6A898CC3-1DD2-11B2-99A6-080020736631': 'Solaris /usr & Apple ZFS',
    '6A87C46F-1DD2-11B2-99A6-080020736631': 'Solaris swap',
    '6A8B642B-1DD2-11B2-99A6-080020736631': 'Solaris backup',
    '6A8EF2E9-1DD2-11B2-99A6-080020736631': 'Solaris /var',
    '6A90BA39-1DD2-11B2-99A6-080020736631': 'Solaris /home',
    '6A9283A5-1DD2-11B2-99A6-080020736631': 'Solaris alternate sector',
    '6A945A3B-1DD2-11B2-99A6-080020736631': 'Solaris reserved 1',
    '6A9630D1-1DD2-11B2-99A6-080020736631': 'Solaris reserved 2',
    '6A980767-1DD2-11B2-99A6-080020736631': 'Solaris reserved 3',
    '6A96237F-1DD2-11B2-99A6-080020736631': 'Solaris reserved 4',
    '6A8D2AC7-1DD2-11B2-99A6-080020736631': 'Solaris reserved 5',

    # NetBSD
    '49F48D32-B10E-11DC-B99B-0019D1879648': 'NetBSD swap',
    '49F48D5A-B10E-11DC-B99B-0019D1879648': 'NetBSD FFS',
    '49F48D82-B10E-11DC-B99B-0019D1879648': 'NetBSD LFS',
    '2DB519C4-B10E-11DC-B99B-0019D1879648': 'NetBSD concatenated',
    '2DB519EC-B10E-11DC-B99B-0019D1879648': 'NetBSD encrypted',
    '49F48DAA-B10E-11DC-B99B-0019D1879648': 'NetBSD RAID',

    # ChromeOS
    'FE3A2A5D-4F32-41A7-B725-ACCC3285A309': 'ChromeOS kernel',
    '3CB8E202-3B7E-47DD-8A3C-7FF2A13CFCEC': 'ChromeOS root fs',
    '2E0A753D-9E48-43B0-8337-B15192CB1B5E': 'ChromeOS reserved',

    # MidnightBSD
    '85D5E45A-237C-11E1-B4B3-E89A8F7FC3A7': 'MidnightBSD data',
    '85D5E45E-237C-11E1-B4B3-E89A8F7FC3A7': 'MidnightBSD boot',
    '85D5E45B-237C-11E1-B4B3-E89A8F7FC3A7': 'MidnightBSD swap',
    '0394EF8B-237E-11E1-B4B3-E89A8F7FC3A7': 'MidnightBSD UFS',
    '85D5E45D-237C-11E1-B4B3-E89A8F7FC3A7': 'MidnightBSD ZFS',
    '85D5E45C-237C-11E1-B4B3-E89A8F7FC3A7': 'MidnightBSD Vinum',

    # Ceph
    '45B0969E-9B03-4F30-B4C6-B4B80CEFF106': 'Ceph Journal',
    '45B0969E-9B03-4F30-B4C6-5EC00CEFF106': 'Ceph Encrypted Journal',
    '4FBD7E29-9D25-41B8-AFD0-062C0CEFF05D': 'Ceph OSD',
    '4FBD7E29-9D25-41B8-AFD0-5EC00CEFF05D': 'Ceph crypt OSD',
    '89C57F98-2FE5-4DC0-89C1-F3AD0CEFF2BE': 'Ceph disk in creation',
    '89C57F98-2FE5-4DC0-89C1-5EC00CEFF2BE': 'Ceph crypt disk in creation',

    # OpenBSD
    '824CC7A0-36A8-11E3-890A-952519AD3F61': 'OpenBSD data',

    # QNX
    'CEF5A9AD-73BC-4601-89F3-CDEEEEE321A1': 'QNX6 file system',

    # Plan 9
    'C91818F9-8025-47AF-89D2-F030D7000C2C': 'Plan 9 partition',
}  # type: Dict[str, str]

PARTITION_TYPES = {x[0].lower(): x[1] for x in PARTITION_TYPES.items()}


def get_part_txt(val):
    """
    :rtype: str | None
    """
    val = str(val)

    try:
        val = int(val)
    except (ValueError, TypeError):
        pass

    if isinstance(val, int):
        val = '{:#04x}'.format(val)

    try:
        val = PARTITION_TYPES[val.lower()]
    except KeyError:
        val = None

    return val
