#!/bin/env python

import os
from backup_rcs import backup_rc_files

bin_files = os.listdir('bin')
home_dir = os.environ['HOME']
current_dir = os.getcwd()

def _create_symlink(src, dst):
  os.symlink(src, dst)

def generate_symlinks():
  backup_rc_files()
  for rc in bin_files:
    src = '{0}/{1}/{2}'.format(current_dir, 'bin', rc)
    dst = '{0}/{1}'.format(home_dir, rc)
    _create_symlink(src, dst)

generate_symlinks()
