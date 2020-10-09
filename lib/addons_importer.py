#!/bin/env python
"""
"""

import json
import os
from helpers import run_cmd, create_directory, paths, mk_clither_custom_dirs

def clone_addons(addons):
  """Clone addons.

  args:
    addons: (list) Addons to clone.
  """
  print('Cloning addons...')
  for url in addons:
    # TODO(curtjen): Abstract references to 'clither_custom/addons' and similar stuff to helpers.
    run_cmd('cd {0}/clither_custom/addons; git clone {1}'.format(paths.base_dir, url))

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
  addons = get_json(paths.addons_config)
  clone_addons(addons)

  print('Finished addons_importer!')

if __name__ == '__main__':
  main()