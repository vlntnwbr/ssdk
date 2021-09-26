# Steam Scheduled Download Killer ![pipeline-badge][badge-checks]
This tool makes it possible to set the auto-update behavior for all installed
Steam games found in specified Steam Library Folders. This is done by setting
the value for the `AutoUpdateBehavior` key found in the appmanifest of each
installed games to a specified value. For more details see usage of entry point
[ssdk][toc-ep-ssdk].

This tool also provides a second entry point [ssdk-lib][toc-ep-ssdk-lib] for
writing, removing, adding and listing all Steam Library Folder(s) whose games
are affected by the main tool.

## Installation
Install using pip:
```
pip install steam-scheduled-download-killer
```
Recommended install using [pipx][pipx]
```
pipx install steam-scheduled-download-killer
```
## Entry Point: ssdk
```
usage: ssdk [-h] [-c CONFIG] [--update-priority PRIO]

Ensure all Steam Games have high priority auto updates.
Manage Steam Library Folder(s) with entry point 'ssdk-lib'

optional arguments:
  -h, --help                  show this help message and exit
  -c CONFIG, --config CONFIG  path to config file containing Steam Library Folder(s)
  --update-priority PRIO      value the update priority should be set to (default: 2)

priority values:
  0                           always keep this game updated
  1                           only update this game when I launch it
  2                           high priority - always auto-update this game before others
```

## Entry Point: ssdk-lib
```
usage: ssdk-lib [-h] [-c CONFIG] [--ignore-existing] COMMAND [LIBRARY ...]

Manage file listing Steam Library Folders.
Use 'ssdk' entry point for managing Steam Applications.

positional arguments:
  COMMAND                     action to be executed (see allowed commands for details)   
  LIBRARY                     path(s) to Steam Library Folders (not needed for 'list')   

optional arguments:
  -h, --help                  show this help message and exit
  -c CONFIG, --config CONFIG  path to config file containing Steam Library Folder(s)     
  --ignore-existing           set this to overwrite existing file for 'make' command     

allowed commands:
  make                        create a config file with all given Steam Library Folder(s)
  list                        show a list of all Steam Library Folder(s)
  rm                          remove the given Steam Library Folder(s) from config file  
  add                         add given Steam Library Folder(s) to config file
```

[badge-checks]: https://github.com/vlntnwbr/ssdk/workflows/Tests/badge.svg

[toc-ep-ssdk]: #entry-point-ssdk
[toc-ep-ssdk-lib]: #entry-point-ssdk-lib

[pipx]: https://pypi.org/project/pipx/
