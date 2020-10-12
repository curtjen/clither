#!/usr/bin/env python
"""

First time run:
$ ./clither.py --mk_custom && ./clither.py --install
...
$ tree
.
├── clither
│   ├── LICENSE
│   ├── README.md
│   ├── clither.py
│   ├── config.json
│   ├── init
│   ├── lib
│   │   ├── addons_importer.py
│   │   ├── addons_importer.pyc
│   │   ├── backup_rcs.py
│   │   ├── backup_rcs.pyc
│   │   ├── build_rcs.py
│   │   ├── build_rcs.pyc
│   │   ├── generate_config.py
│   │   ├── generate_symlinks.py
│   │   ├── generate_symlinks.pyc
│   │   ├── helpers.py
│   │   ├── helpers.pyc
│   │   ├── mk_custom.py
│   │   └── mk_custom.pyc
│   ├── pather.py
│   ├── pather.pyc
│   └── scripts
│       └── helpers.pyc
├── clither_custom
│   ├── addons
│   │   └── clither_addon_example
│   │       ├── clither.config.json
│   │       └── rcs
│   │           ├── vimrc
│   │           └── zshrc
│   ├── config.json
│   └── rcs
│       ├── vimrc
│       └── zshrc
├── vimrc -> ./clither_custom/rcs/./clither_custom/rcs
└── zshrc -> ./clither_custom/rcs/./clither_custom/rcs

10 directories, 33 files
"""
import argparse
import os

# Pather Imports
import pather  # run first only works if run from ./
import addons_importer
import build_rcs
import backup_rcs
import mk_custom
import generate_symlinks

FLAGS = argparse.ArgumentParser(__doc__)
FLAGS.add_argument('--dry_run', action='store_true', help='Run without doing anything.')
FLAGS.add_argument('--mk_custom', action='store_true', help='sets up ../clither_custom.')
FLAGS.add_argument('--addons_import', action='store_true', help='Run addons import.')
FLAGS.add_argument('--build_rcs', action='store_true', help='Run build_rcs import.')
FLAGS.add_argument('--install', action='store_true', help='Run install.')
FLAGS.add_argument('--backup_rcs', action='store_true', help='Run backup of existing RCs.')
FLAGS.add_argument('--generate_symlinks', action='store_true', help='Run generating symlinks.')
# clither.sh install
FLAGS = FLAGS.parse_args()

def main():
  if FLAGS.mk_custom:
    mk_custom.main()
    return

  if FLAGS.install:
    #TODO(xnz): add in halt logic, maybe a for?
    print('Install all...')
    addons_importer.main()
    build_rcs.main()
    backup_rcs.main()
    # generate_symlinks.main()
    #   - rename/backup
    # - dry run
    # - update any paths that come from helpers
    print('Finished install!')

    return

  if FLAGS.addons_import:
    addons_importer.main()

  if FLAGS.build_rcs:
    build_rcs.main()

  if FLAGS.backup_rcs:
    backup_rcs.main()

  if FLAGS.generate_symlinks:
    generate_symlinks.main()

if __name__ == '__main__':
  main()