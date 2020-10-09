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

#TODO(xnz): figure out a way to make argparse play nice on libs.
dry_run_flag = False
if '--dry_run' in sys.argv:
  dry_run_flag = True

# Any json we use should (for now) should not use spaces or - in the key
def dict_to_obj(blueprint_dict):
  blueprint_list = list(blueprint_dict.keys())
  proto = namedtuple('dynamic_holder', blueprint_list)
  result_dict = proto(**blueprint_dict)
  return result_dict

#TODO(xnz): Put BASE_DIR in other file , file_paths dict comp from it. if no file then use home
BASE_DIR = os.environ['HOME'] + '/dev/sandbox'
file_paths = {
  'base_dir': BASE_DIR,  # + is temps
  'addons_config': BASE_DIR + '/clither_custom/config.json',
  'rcs_path': BASE_DIR + '/clither_custom/rcs',
}

paths = dict_to_obj(file_paths)

def json_to_obj(json_file_path):
  """Experemental"""
  with open(json_file_path) as file:
    data = json.load(file)
  data = dict_to_obj(data)
  return data

def create_directory(dir):
  if os.path.exists(dir):
    return

  msg = 'mkdir ' + dir
  if dry_run(msg):
    return

  os.makedirs(dir)
  print(msg)

def mk_clither_custom_dirs():
  dirs = (
    '',  # base dir
    'rcs',
    'addons',
  )
  for dir in dirs:
    create_directory('{0}/clither_custom/{1}'.format(paths.base_dir, dir))


def backup_file(file_path):
  """Backup file at a given path.

  args:
    file_path: (str) Path to backup file.
  """
  # msg = 'backup_file: ' + file_path
  # if dry_run(msg):
  #   return

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
    # print('{0} backed up to: {1}'.format(file_name, dst_file_path))

    msg = 'backup_file: cp {0} {1}'.format(file_path, dst_file_path)
    if dry_run(msg):
      return
    os.rename(file_path, dst_file_path)
    print(msg)

def clear_file(file_path):
  msg = 'clear_file: ' + file_path
  if dry_run(msg):
    return

  #TODO(xnz): Check for better way to do this.
  with open(file_path, 'w') as file:
    file.write('')
  print(msg)

def append_to_file(file_path, string):
  msg = 'append_to_file: echo {0} >> {1}'.format(string, file_path)
  if dry_run(msg):
    return

  with open(file_path, 'a') as file:
    file.write(string + '\n')
  print(msg)

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
  msg = 'run cmd: ' + cmd
  if dry_run(msg):
    return
  #TODO(xnz): mv this to a subprocess
  os.system(cmd)
  print(msg)

def create_symlink(src, dst):
  # check if already exists
  msg = 'create symlink: ln -s {0} {1}'.format(src, dst)
  if dry_run(msg):
    return

  os.symlink(src, dst)
  print(msg)