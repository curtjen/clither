#!/bin/env python

import json
import os
from helpers import create_directory
# import subprocess

# # addons_dirs = os.system('ls addons')
# addons_dirs = subprocess.run('ls', 'addons')
# print(addons_dirs)
# # with open('')

zshrc_list = []
configs_list = []

addons_dirs = os.listdir('addons')

# print(addons_dirs)

# TODO(curtjen): Change this to be dynamic based on keys in the retrieved config file.

def create_rcs_lists():
  for dir in addons_dirs:
    config_path = 'addons/{0}/clither.config.json'.format(dir)
    if os.path.exists(config_path):
      print('config_path found: {0}'.format(config_path))
      with open(config_path) as file:
        config = json.load(file)
        zshrc_list.append('{0}/{1}'.format(dir, config['zshrc']))

    else:
      print('config_path NOT found: {0}'.format(config_path))

create_rcs_lists()

print('zshrc_list: {0}'.format(zshrc_list))
print('zshrc_list[0]: {0}'.format(zshrc_list[0]))

create_directory('bin')

def get_file_contents(path):
  with open(path) as file:
    return file.read()

def append_to_rc(rc, addon_rc):
  rc_path = './bin/{0}'.format(rc)
  file_contents = get_file_contents(addon_rc)
  # print('file_contents: {0}'.format(file_contents))
  with open(rc_path, 'a') as file:
    file.write(file_contents)

append_to_rc('zshrc', 'addons/{0}'.format(zshrc_list[0]))
