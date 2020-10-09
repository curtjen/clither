#!/bin/env python

# ===== Usage =====
# --- Import ---
# import helpers
#
# --- create_directory("DIRECTORY_NAME") ---
#
# --- backup_file("FILE_PATH") ---
#
# --- create_symlink("FILE_PATH") ---
# This will create a symlink inside the $HOME directory for a given file path.

import os
import json
import sys
import time

from collections import namedtuple

constants = namedtuple('consts', ['config_file', 'addons_path'])

#TODO(xnz): We need these paths
consts = constants(
  config_file='path',
  addons_path='path'
  )

# def mk_obj_from_dict(blueprint_dict):
#   class blankClass:
#     pass

#   used_obj = blankClass()
#   used_obj._dict__ = blueprint_dict
#   return used_obj

#TODO(xnz): figure out a way to make argparse play nice on libs.
dry_run_flag = False
if '--dry_run' in sys.argv:
  dry_run_flag = True

def create_directory(dir):
  if dry_run('create dir ' + dir):
    return

  if not os.path.exists(dir):
    os.makedirs(dir)

def backup_file(file_path):
  """Backup file at a given path.

  args:
    file_path: (str) Path to backup file.
  """
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

def dry_run(msg):
  """Return True and print msg if dry_run flag is set, else return False."""
  if dry_run_flag:
    print('dry_run: ' + msg)
    return True
  return

def run_cmd(cmd):
  """Desc

  args:
    cmd: (str) The command to run.
  """
  if dry_run('run cmd: ' + cmd):
    return
  #TODO(xnz): mv this to a subprocess
  os.system(cmd)
