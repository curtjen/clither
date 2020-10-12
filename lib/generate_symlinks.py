#!/bin/env python

import os
import backup_rcs
from helpers import create_symlink, get_dir_list, paths

def main():
  backup_rcs.main()
  print('-' * 40)
  print('Start generate_symlinks...')
  #TODO(xnz): glob?
  rc_files = get_dir_list(paths.rcs_path)
  for rc_file in rc_files:
    src = '{0}/{1}'.format(paths.rcs_path, rc_file)
    dst = '{0}/{1}'.format(paths.base_dir, rc_file)
    create_symlink(src, dst)

  print('Finished generate_symlinks!')

if __name__ == '__main__':
  main()
