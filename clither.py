#!/usr/bin/env python
"""

The first time run:
$ ./clither.py --mk_custom --install

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
import build_bins

FLAGS = argparse.ArgumentParser(__doc__)
FLAGS.add_argument('--dry_run', action='store_true',
  help='Run without doing anything.')
FLAGS.add_argument('--mk_custom', action='store_true',
  help='sets up ../clither_custom.')
FLAGS.add_argument('--addons_import', action='store_true',
  help='Run addons import.')
FLAGS.add_argument('--build_rcs', action='store_true',
  help='Run build_rcs import.')
FLAGS.add_argument('--install', action='store_true',
  help='Run install.')
FLAGS.add_argument('--backup_rcs', action='store_true',
  help='Run backup of existing RCs.')
FLAGS.add_argument('--generate_symlinks', action='store_true',
  help='Run generating symlinks.')
FLAGS.add_argument('--build_bins', action='store_true',
  help='Run build_bins.')
FLAGS = FLAGS.parse_args()

def main():
  if FLAGS.mk_custom:
    mk_custom.main()

  if FLAGS.install:
    #TODO(xnz): add in halt logic, maybe a for?
    print('Install all...')
    addons_importer.main()
    build_rcs.main()
    backup_rcs.main()
    generate_symlinks.main()
    #   - rename/backup
    # - dry run
    # - update any paths that come from helpers
    build_bins.main()
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

  if FLAGS.build_bins:
    build_bins.main()

if __name__ == '__main__':
  main()
