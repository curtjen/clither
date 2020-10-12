#!/bin/env python
"""
"""
import json
import os
from helpers import run_cmd, create_directory, paths, mk_clither_custom_dirs

EXCEPTION_TMP = """Config file does not exist: {0}

To generate, then edit, a template config.json try running: 
    $ ./clither --mk_custom; vi ../clither_custom/config.json"""

def clone_addons(addons):
  """Clone addons.

  args:
    addons: (list) Addons to clone.
  """
  print('Cloning addons...')
  for url in addons:
    run_cmd('cd {0}; git clone {1}'.format(paths.addons_path, url))

def get_json(json_file_path):
  # TODO(curtjen): Try and fail safely for when no config exists
  with open(json_file_path) as file:
    data = json.load(file)
  addons = data['addons']
  return addons

def main():
  print('-' * 40)
  print('Start addons_importer...')
  mk_clither_custom_dirs()
  try:
    addons = get_json(paths.addons_config)
  except IOError:
    msg = EXCEPTION_TMP.format(paths.addons_config)
    raise Exception(msg)

  clone_addons(addons)

  print('Finished addons_importer!')

if __name__ == '__main__':
  main()