##
#   Copyright (c) 2021 Valentin Weber
#
#   This file is part of the software steam-scheduled-download-killer.
#
#   The software is licensed under the European Union Public License
#   (EUPL) version 1.2 or later. You should have received a copy of
#   the english license text with the software. For your rights and
#   obligations under this license refer to the file LICENSE or visit
#   https://joinup.ec.europa.eu/community/eupl/og_page/eupl to view
#   official translations of the licence in another language of the EU.
##

"""Module for interacting with csv-config."""

import os
from typing import IO, List, Optional, Union

from .models import SteamLibrary
from .utils import get_abspath


class ConfigFileError(Exception):
    """Exception for interacting with config file."""


class Config:
    """Config Handler."""

    FILE_LOC = "~/AppData/Local/python-ssdk"

    def __init__(self, file: Optional[str] = None) -> None:
        """Initialize handler for given config file."""
        self.file = self.FILE_LOC if file is None else file

    def read(self) -> List[SteamLibrary]:
        """Read list of Steam Libraries from config file."""
        return [SteamLibrary(lib) for lib in self._read()]

    def write(
        self,
        lib_dirs: Union[str, List[str]],
        overwrite_existing: bool = True
    ) -> None:
        """Write list of Steam Library Directories to config file."""
        if os.path.isfile(self.file) and not overwrite_existing:
            raise ConfigFileError("config file already exists", self.file)
        libs = [get_abspath(lib) for lib in self._get_lib_dir_list(lib_dirs)]
        self._write(libs)

    def remove(self, lib_dirs: Union[str, List[str]]):
        """Remove Steam Library Directory from config file."""
        cfg_libs = self._read()
        lib_dirs = self._get_lib_dir_list(lib_dirs)
        for lib in lib_dirs:
            lib_path = get_abspath(lib)
            if lib_path not in cfg_libs:
                print(f"Unable to find '{lib_path}' in config")
            else:
                cfg_libs.remove(lib_path)
                print(f"Removing '{lib_path}' from config")
        self._write(cfg_libs)

    def add(self, lib_dirs: Union[str, List[str]]) -> None:
        """Add Steam Library Directory to config file."""
        cfg_libs = self._read()
        lib_dirs = self._get_lib_dir_list(lib_dirs)
        for lib in lib_dirs:
            lib_path = get_abspath(lib)
            if lib_path in cfg_libs:
                print(f"'{lib_path}' is already in config")
            else:
                cfg_libs.append(lib_path)
                print(f"Adding '{lib_path}' to config")
        self._write(cfg_libs)

    def _open(self, filemode="r", encoding="utf-8") -> IO:
        """Open config file with specified mode and encoding."""
        try:
            return open(self.file, filemode, encoding=encoding)
        except OSError as exc:
            raise ConfigFileError("unable to access config", self.file) from exc

    def _read(self) -> List[str]:
        """Read list of Steam Library Directories from config file."""
        with self._open() as cfg_file:
            lib_dirs = [
                line.strip() for line in cfg_file.readlines()
                if line and not line.startswith("#")
            ]
        return lib_dirs

    def _write(self, lib_dirs: List[str]):
        """Write list of Steam Library Directories to config file."""
        if not os.path.isdir(cfg_dir := os.path.dirname(self.file)):
            os.makedirs(cfg_dir)
        with self._open("w") as cfg_file:
            cfg_file.write("\n".join(lib_dirs))

    @staticmethod
    def _get_lib_dir_list(lib_dirs: Union[str, List[str]]) -> List[str]:
        """Return lib_dirs as single element list if given as str."""
        if isinstance(lib_dirs, list):
            return lib_dirs
        return [lib_dirs]


if __name__ == "__main__":
    cfg = Config(".conf/test.csv")

    # cfg.write([r"G:\SteamLibrary", r"D:\SteamLibrary"], False)
    # cfg.remove(r"D:\SteamLibrary")
    # cfg.add(r"D:\SteamLibrary")
    # cfg.add([r"G:\SteamLibrary", r"C:\Program Files (x86)\Steam\steamapps"])

    libraries = cfg.read()
    print(libraries)
 