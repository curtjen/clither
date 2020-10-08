#!/bin/env python
"""Build RC files."""

import json
import os
from helpers import create_directory

ADDON_DIRS = os.listdir('addons')
CURRENT_DIR = os.getcwd()
HOME_DIR = os.environ['HOME']

def _append_to_file(rc, addon_path, config_rc_path):
  rc_dir_path = '{0}/clither_custom/rcs/{1}'.format(home_dir, rc)
  # TODO(xnz): Strings with variables this way?
  # rc_dir_path = home_dir + '/clither_custom/rcs/' + rc
  new_rc_path = '{0}/{1}'.format(addon_path, config_rc_path)

  # FOR TROUBLESHOOTING
  # print('\n####################')
  # print('rc: {0}'.format(rc))
  # print('addon_path: {0}'.format(addon_path))
  # print('new_rc_path: {0}'.format(new_rc_path))
  # print('bin_rc_path: {0}'.format(bin_rc_path))

  # link to the addon's respective rc file
  import_cmd = 'source {0}\n'.format(new_rc_path)

  # append to respective rc file
  with open(rc_dir_path, 'a') as file:
    file.write(import_cmd)

def _build_rc_files(config, addon_path):
  # TODO(curjten): Account for appending bins to the PATH
  for rc in config:
    _append_to_file(rc, addon_path, config[rc])

def build_rcs():
  # Loop over each addon config
  for dir in addons_dirs:
    addon_path = '{0}/addons/{1}'.format(current_dir, dir)
    config_path = '{0}/clither.config.json'.format(addon_path)

    # Do stuff with the config
    if os.path.exists(config_path):
      with open(config_path) as file:
        config = json.load(file)
        _build_rc_files(config, addon_path)

def main():
  # get list of addon directories

  create_directory(home_dir + '/clither_custom')
  create_directory(home_dir + '/clither_custom/rcs')
  build_rcs()

if __name__ == '__main__':
  main()
