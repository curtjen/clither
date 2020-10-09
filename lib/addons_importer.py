#!/bin/env python
"""
"""

import json
import os
from helpers import dry_run, run_cmd, create_directory, paths

def clone_addons(addons):
  """Clone addons.

  args:
    addons: (list) Addons to clone.
  """
  print('Cloning addons...')
  for url in addons:
    run_cmd('cd addons; git clone {0}; cd -'.format(url))

def get_json(json_file_path):
  with open(json_file_path) as file:
    data = json.load(file)
  addons_path = data['addons_path']
  config_file = data['config_file']
  return addons_path, config_file

def main():
  addons_path, config_file = get_json(paths.config_file)

  # --- Create Addons Directory ---
  create_directory(configs.addons_path)

  # _create_directory('addons')
  # os.system('mkdir addons')

  # print(data['addons'])
  # print(data['shell'])
  # print(addons)

  clone_addons(addons)

  print('Finished!')

if __name__ == '__main__':
  main()