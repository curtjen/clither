#!/bin/env python

import os
from helpers import backup_file

# get list of rcs in bin
bin_files = os.listdir('bin')

# get home directory
home_dir = os.environ['HOME']

# for each file in bin, backup the same file name in home
def backup_rc_files():
  for rc in bin_files:
    backup_file_path = '{0}/{1}'.format(home_dir, rc)
    print('backup_file_path: {0}'.format(backup_file_path))
    backup_file(backup_file_path)

backup_rc_files()
