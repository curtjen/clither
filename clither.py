#!/usr/bin/env python
"""

$./clither.py --addons_import --dry_run
----------------------------------------
Start addons_importer...
        dry_run: mkdir ../i_danno
Cloning addons...
        dry_run: run cmd: cd addons; git clone https://github.com/curtjen/rcs
Finished addons_importer!
"""

# --- Compile list of files ---
# TODO: Get Base.
# -- Check "shell" in config. Default to bash.
#
# TODO: Get Addons.
# --- Import Addons ---
# python ./scripts/addons_importer.py;

# --- Build RCs ---
# TODO: Write files to bin/ directory
# python ./scripts/build_rcs.py;

# # --- Create Aliases ---
# python ./scripts/generate_symlinks.py;
# TODO: Create aliases for new RC file.
# TODO: Backup existing and move old/existing RCs.

import argparse
import os

# Pather Imports
import pather  # run first
import addons_importer
import build_rcs
import backup_rcs
# import generate_symlinks

FLAGS = argparse.ArgumentParser(__doc__)
FLAGS.add_argument('--dry_run', action='store_true', help='Run without doing anything.')
FLAGS.add_argument('--addons_import', action='store_true', help='Run addons import.')
FLAGS.add_argument('--build_rcs', action='store_true', help='Run build_rcs import.')
FLAGS.add_argument('--install', action='store_true', help='Run install.')
FLAGS.add_argument('--backup_rcs', action='store_true', help='Run backup of existing RCs.')
FLAGS.add_argument('--generate_symlinks', action='store_true', help='Run generating symlinks.')
# clither.sh install
FLAGS = FLAGS.parse_args()

def main():
  # print(FLAGS)
  if FLAGS.install:
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

  # if FLAGS.generate_symlinks:
  #   generate_symlinks.main()

if __name__ == '__main__':
  main()