
import os
import sys

from collections import namedtuple

CLITHER_REPO = 'https://github.com/curtjen/clither.git'
PARENT_DIR = os.path.join(os.getcwd(), '..')
CLITHER_DIR = os.path.join(PARENT_DIR, 'clither')
cd = lambda path: 'cd ' + path

#TODO(xnz): figure out a way to make argparse play nice on libs.
dry_run_flag = False
if '--dry_run' in sys.argv:
  dry_run_flag = True

def dry_run(msg):
  """Return True and print msg if dry_run flag is set, else return False."""
  if dry_run_flag:
    print('dry_run: ' + msg)
    return True
  return

# Any json we use should (for now) should not use spaces or - in the key
def dict_to_obj(blueprint_dict):
  blueprint_list = list(blueprint_dict.keys())
  proto = namedtuple('dynamicHolder', blueprint_list)
  result_dict = proto(**blueprint_dict)
  return result_dict

PARENT_DIR = os.path.join(os.getcwd(), '..')

file_paths = {
  'clither_base_repo': 'https://github.com/curtjen/clither.git',
  'parent_dir':  PARENT_DIR,
  'clither_dir':  os.path.join(PARENT_DIR, 'clither'),
}

paths = dict_to_obj(file_paths)


def run_cmd(*cmd_list):
  """Desc

  args:
    cmd: (list) The commands to run.
  """
  cmd = '; '.join(cmd_list)
  msg = 'run cmd: ' + cmd
  if dry_run(msg):
    return
  #TODO(xnz): mv this to a subprocess
  print(msg)
  os.system(cmd)