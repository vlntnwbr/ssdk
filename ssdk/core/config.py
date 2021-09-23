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

from typing import Optional


class Config:
    """Config Handler."""

    FILE_LOC = "~/AppData/Local/python-ssdk"

    def __init__(self, fp: Optional[str] = None) -> None:
        self.fp = self.FILE_LOC if fp is None else fp
        self._check_cfg_file()

    def read(self):
        """Read list of Steam Library Directories from config file."""
        ...

    def write(self):
        """Write list of Steam Library Directories from config file."""
        ...

    def remove(self):
        """Remove Steam Library Directory from config file."""
        ...

    def add(self):
        """Add Steam Library Directory to config file."""
        ...

    def _check_cfg_file(self):
        """Check whether config dir and file exist."""
        ...
