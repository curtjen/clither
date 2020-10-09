#!/bin/env python

import os
import backup_rcs
from helpers import create_symlink, paths

bin_files = os.listdir('bin')
current_dir = os.getcwd()

def main():
  backup_rcs.main()
  print('-' * 40)
  print('Start generate_symlinks...')
  for rc in bin_files:
    src = '{0}/{1}/{2}'.format(paths.base_dir, 'bin', rc)
    dst = '{0}/{1}'.format(paths.base_dir, rc)
    create_symlink(src, dst)

  print('Finished generate_symlinks!')

if __name__ == '__main__':
  main()