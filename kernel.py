import subprocess
from collections import Mapping
from typing import Dict, Optional, Callable, Any, Set, Generator, Tuple, Union, List


class DeviceAttributeError(Exception):
    def __init__(self, obj, item: str):
        super().__init__("{!r} object has no attribute {!r}".format(obj.__class__.__name__, item))


class DuplicatePropertyError(Exception):
    def __init__(self, prop: str):
        super().__init__('Property already exists: {!r}'.format(prop))


class DeviceRaw(Mapping):
    __hash: int = None
    __props_all: Dict[str, Optional[Callable[[str], Any]]] = {}
    __dict: Dict[str, str] = {}
    __my_props: Set[str] = set()
    _duplicate: bool = False

    def __init__(self, *args, **kwargs):
        if not self.__dict:
            self.__dict = dict(*args, **kwargs)
            return
        for key, value in dict(*args, **kwargs).items():  # type: str, str
            if not self._duplicate and key in self:
                raise DuplicatePropertyError(key)
            self.__dict[key] = value

    @property
    def __my_props__(self) -> Generator[str, None, None]:
        for key in self:  # type: str
            yield self.key2attr(key)
        for key in self.__my_props:  # type: str
            if getattr(self, key) is not None:
                yield key

    def _add_my_props(self, value: Tuple[str, ...]):
        if not self.__my_props:
            self.__my_props = set()  # type: Set[str]

        for key in value:
            if not self._duplicate and key in self.__my_props:
                raise DuplicatePropertyError(key)
            self.__my_props.add(key)

    def _add_props_all(self, value: Dict[str, Optional[Callable[[str], Any]]]):
        if not self.__props_all:
            self.__props_all = {}  # type: Dict[str, Optional[Callable[[str], Any]]]

        for key, value_ in value.items():
            if not self._duplicate and key in self.__props_all:
                raise DuplicatePropertyError(key)
            self.__props_all[key] = value_

    def __getitem__(self, key: str) -> Union[str, Any]:
        try:
            return self.__dict[key]
        except KeyError as e:
            if key not in self.__props_all:
                # @todo: return super().__getitem__(key)
                raise e

    def __contains__(self, key: str) -> bool:
        return key in self.__dict

    def __iter__(self):
        return iter(self.__dict)

    def __len__(self):
        return len(self.__dict)

    def __repr__(self) -> str:
        txt = []
        for attr in self.__my_props__:
            txt.append('{}: {!r}'.format(attr, getattr(self, attr)))
        return '{}({})'.format(self.__class__.__name__, ',\n'.join(txt))

    def __hash__(self) -> int:
        if self.__hash is not None:
            return self.__hash
        h = 0
        for key, value in self.__dict.items():  # type: str, str
            h ^= hash((key, value))
        self.__hash: int = h
        return h

    def __getattr__(self, item: str) -> Union[str, Any]:
        for key in self:  # type: str
            if item == self.key2attr(key):
                break
        else:
            if item in (self.key2attr(x) for x in self.__props_all):
                return
            raise DeviceAttributeError(self, item)

        value: str = self[key]

        try:
            funct = self.__props_all[key]
        except KeyError:
            return value

        if callable(funct):
            return funct(value)

        return value

    def __setattr__(self, key: str, value: Any):
        if key in (self.key2attr(x) for x in self.__props_all.keys()):
            raise DeviceAttributeError(self, key)
        object.__setattr__(self, key, value)

    @staticmethod
    def _run_command(command: Union[List[str], str], split_str: bytes) -> Generator[str, None, None]:
        ret = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        ret.check_returncode()

        stdout: bytes = ret.stdout

        stdout: List[bytes] = stdout.strip().split(split_str)
        stdout: Generator[str, None, None] = (x.decode().strip() for x in stdout)
        # stdout = (self._decode(x) for x in stdout)

        return stdout

    @staticmethod
    def _decode(string: Optional[Union[str, bytes, bytearray]]) -> Optional[str]:
        if string is None:
            return string
        if isinstance(string, str):
            string = string.encode()
        return string.decode('unicode_escape').encode('latin1').decode().strip()

    @staticmethod
    def key2attr(string: str) -> str:
        return string.lower().replace('-', '_').replace(':', '_')
