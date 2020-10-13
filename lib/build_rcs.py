#!/bin/env python
"""Build RC files."""

import json
import os
from helpers import create_directory, paths, mk_clither_custom_dirs, append_to_file, clear_file, get_dir_list



def _append_to_file(rc, addon_path, config_rc_path):
  rc_dir_path = '{0}/{1}'.format(paths.rcs_path, rc)
  new_rc_path = '{0}/{1}'.format(addon_path, config_rc_path)
  import_cmd = 'source {0}'.format(new_rc_path)

  clear_file(rc_dir_path)
  append_to_file(rc_dir_path, import_cmd)

def _build_rc_files(config, addon_path):
  # TODO(curjten): Account for appending bins to the PATH

  for rc, config_rc_path in config.items():
    _append_to_file(rc, addon_path, config_rc_path)

# TODO(curtjen): Create function for getting clither.config.json
#   - Add helpful errors like when the config file is not found.

def build_rcs():
  addon_dirs = get_dir_list(paths.addons_path)

  for dir in addon_dirs:
    print('Run rcs on: ' + dir)
    addon_path = '{0}/{1}'.format(paths.addons_path, dir)
    config_path = addon_path + '/clither.config.json'

    if os.path.exists(config_path):
      with open(config_path) as file:
        config = json.load(file)
      rcs = config.setdefault('rcs')

      if not rcs:
        print('File does not have rcs section: ' + config_path)
        return

      _build_rc_files(rcs, addon_path)
    else:
      pass  #TODO(xnz): look for an override

  """ Alternative
  addon_dirs_patter = paths.addons_path + '/*'
  addon_paths = get_globed_dirs(addon_dirs_patter)

  for addon_path in addon_paths:
    print('Run rcs on: ' + dir)
    config_path = addon_path + '/clither.config.json'

    if os.path.exists(config_path):
      with open(config_path) as file:
        config = json.load(file)
      _build_rc_files(config, addon_path)
    else:
      pass  #TODO(xnz): look for an override
  """



def main():
  print('-' * 40)
  print('Start build_rcs...')

  mk_clither_custom_dirs()
  build_rcs()

  print('Finished build_rcs!')

if __name__ == '__main__':
  main()
