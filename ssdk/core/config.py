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
from typing import IO, List, Optional


class CfgFileError(Exception):
    """Raised instead of 'OSError' during config file interaction."""


class Config:
    """Config Handler."""

    FILE_LOC = "~/AppData/Local/python-ssdk"

    def __init__(self, file: Optional[str] = None) -> None:
        self.file = self.FILE_LOC if file is None else file

    def read(self) -> List[str]:
        """Read list of Steam Library Directories from config file."""
        with self._open() as cfg_file:
            lib_dirs = [
                line.strip() for line in cfg_file.readlines()
                if line and not line.startswith("#")
            ]
        return lib_dirs

    def write(self, *lib_dirs: str):
        """Write list of Steam Library Directories from config file."""
        if not os.path.isdir(cfg_dir := os.path.dirname(self.file)):
            os.makedirs(cfg_dir)
        with self._open("w") as cfg_file:
            cfg_file.write("\n".join(lib_dirs))

    def remove(self):
        """Remove Steam Library Directory from config file."""
        ...

    def add(self):
        """Add Steam Library Directory to config file."""
        ...

    def _open(self, filemode="r", encoding="utf-8") -> IO:
        """Open config file with specified mode and encoding."""
        try:
            return open(self.file, filemode, encoding=encoding)
        except OSError as exc:
            raise CfgFileError("unable to access config", self.file) from exc

if __name__ == "__main__":
    cfg = Config(".conf/test.csv")

    # cfg.write(r"G:\SteamLibrary", r"D:\SteamLibrary")

    libraries = cfg.read()
    print(libraries)
 