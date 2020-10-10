#!/bin/env python
"""Backup current RC files in the HOME directory."""

import os
from helpers import backup_file, paths

# rc_files = os.listdir('~/clither_custom/rcs')

def main():
  print('-' * 40)
  print('Start backup_rcs...')
  dot_files = {x[1:] for x in os.listdir(paths.base_dir) if x.startswith('.')}
  #TODO(xnz): same a build_rcs, we should put this kind of thing in helper.
  try:
    rc_files = os.listdir(paths.rcs_path)
  except OSError:
    rc_files = []

  rc_files = set(rc_files)
  dot_files_to_backup = dot_files.intersection(rc_files)

  for dot_file in dot_files_to_backup:
    backup_file_path = "{0}/.{1}".format(paths.base_dir, dot_file)
    backup_file(backup_file_path)

  print('Finished backup_rcs!')

if __name__ == "__main__":
  main()
