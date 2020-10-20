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

import calendar
import json
import os
import sys
import time

from collections import namedtuple
from glob import glob
from shutil import copy

#TODO(xnz): figure out a way to make argparse play nice on libs.
dry_run_flag = False
if '--dry_run' in sys.argv:
  dry_run_flag = True

# Any json we use should (for now) should not use spaces or - in the key
def dict_to_obj(blueprint_dict):
  blueprint_list = list(blueprint_dict.keys())
  proto = namedtuple('dynamicHolder', blueprint_list)
  result_dict = proto(**blueprint_dict)
  return result_dict

BASE_DIR = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

# post 3.4 use:
# from pathlib import Path
# path = Path("/here/your/path/file.txt")
# print(path.parent)

#TODO(xnz): mk naming consistent.
file_paths = {
  'base_dir': '',  # + is temps
  'clither_path': '/clither',
  'clither_lib_path': '/clither/template_files',
  'clither_tmp_files_path': '/clither/lib',
  'clither_pather': '/clither/pather.py',
  'clither_run': '/clither/template_files/run.py',
  'clither_run_help': '/clither/template_files/helper.py',  # may fold this into lib/helper
  'clither_tmp_config': '/clither/template_files/config.json',

  'custom_path':  '/clither_custom/',
  'custom_lib_path': '/clither_custom/lib',
  'custom_rcs_path':  '/clither_custom/rcs',
  'custom_addons_path': '/clither_custom/addons',
  'custom_bin_path': '/clither_custom/bins',
  'custom_bin_conflicts_path': '/clither_custom/bins/conflicts',
  'custom_addons_config': '/clither_custom/config.json',
}

file_paths = {key: BASE_DIR + value for key, value in file_paths.items()}

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
    'bins',
    'bins/conflicts'
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
    print(msg)
    os.rename(file_path, dst_file_path)

def clear_file(file_path):
  msg = 'clear_file: ' + file_path
  if dry_run(msg):
    return

  #TODO(xnz): Check for better way to do this.
  print(msg)
  with open(file_path, 'w') as file:
    file.write('')

def append_to_file(file_path, string):
  msg = 'append_to_file: echo {0} >> {1}'.format(string, file_path)
  if dry_run(msg):
    return

  print(msg)
  with open(file_path, 'a') as file:
    file.write(string + '\n')

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
  print(msg)
  os.system(cmd)

def create_symlink(src, dst):
  # check if already exists
  msg = 'create symlink: ln -s {0} {1}'.format(src, dst)
  if dry_run(msg):
    return

  print(msg)

  if os.path.exists(dst):
    os.remove(dst)

  os.symlink(src, dst)

def copy_file(src_file, dst):
  dst = os.path.join(dst, os.path.basename(src_file))

  if os.path.exists(dst):
    print('copy_file: dst already exists: ' + dst)
    return

  msg = 'cp {0} {1}'.format(src_file, dst)
  if dry_run(msg):
    return

  print(msg)
  copy(src_file, dst)

def get_dir_list(dir_path):
  # os.listdir(dir_path)
  try:
    return os.listdir(dir_path)
  except OSError as err:
    if dry_run_flag:
      return []
    raise OSError(err)

def get_globed_dirs(pattern):
  return [dir for dir in glob(pattern) if os.path.isdir(dir)]

def process_area(area_of_interest, process_func, missing_config_func):
  addon_dirs = get_dir_list(paths.custom_addons_path)
  for dir in addon_dirs:
    print('Run {0} on: {1}'.format(area_of_interest, dir))
  
    addon_path = '{0}/{1}'.format(paths.custom_addons_path, dir)
    config_path = addon_path + '/clither.config.json'

    if os.path.exists(config_path):
      with open(config_path) as file:
        try:  #TODO(xnz): ask cjensen if we want this to crash or not
          config = json.load(file)
        except ValueError:
          print('file format was not a json:', config_path) # mark better
          continue

      result = config.setdefault(area_of_interest)

      if not result:
        msg = 'File does not have {0} section: {1}'
        print(msg.format(area_of_interest, config_path))
        return
      
      process_func(result, addon_path)
    else:
      missing_config_func(dir)

def get_epoc_time():
  return str(calendar.timegm(time.gmtime()))