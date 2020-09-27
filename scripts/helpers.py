#!/bin/env python

# ===== Usage =====
# --- Import ---
# import helpers
#
# --- create_directory('DIRECTORY_NAME') ---
#
# --- backup_file('FILE_PATH') ---
#
# --- create_symlink('FILE_PATH') ---
# This will create a symlink inside the $HOME directory for a given file path.

import os
import time

def create_directory(dir):
  if not os.path.exists(dir):
    os.makedirs(dir)

def backup_file(file_path):
  if os.path.isfile(file_path):
    # get file name and containing directory
    dir_path = os.path.dirname(file_path)
    file_name = os.path.basename(file_path)

    # generate backup directory in file's directory (if one does not exist)
    backup_path = '{0}/backups_rcs'.format(dir_path)
    create_directory(backup_path)

    # move file to backup directory with epoch timestamp at end
    #   e.g. zshrc_1234567890
    timestamp = int(time.time())
    dst_file_path = '{0}/{1}_{2}'.format(backup_path, file_name, timestamp)
    print('{0} backed up to: {1}'.format(file_name, dst_file_path))
    os.rename(file_path, dst_file_path)

def create_symlink(file_path):
  # get home directory
  home_dir = os.environ['HOME']
  print('home_dir: {0}'.format(home_dir))
