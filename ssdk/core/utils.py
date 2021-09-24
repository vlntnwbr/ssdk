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

"""Utilities for steam-scheduled-download-killer."""

import os


def get_abspath(path: str) -> str:
    """Return normalized absolute version of given path."""
    if not os.path.isabs(path):
        if path.startswith("~"):
            path = os.path.expanduser(path)
        else:
            path = os.path.abspath(path)
    return os.path.normpath(path)
