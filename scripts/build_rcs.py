#!/bin/env python

import json
import os
from helpers import create_directory

# get list of addon directories
addons_dirs = os.listdir('addons')
current_dir = os.getcwd()

def _append_to_file(rc, addon_path, config_rc_path):
  bin_rc_path = './bin/{0}'.format(rc)
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
  with open(bin_rc_path, 'a') as file:
    file.write(import_cmd)

def _build_rc_files(config, addon_path):
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

create_directory('bin')
build_rcs()
