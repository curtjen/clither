#!/bin/env python
"""
"""

import json
import os
from helpers import dry_run, run_cmd, create_directory, consts

def get_json_data():
  with open(consts.config_file) as file:
    data = json.load(file)
    addons = data['addons']
    shell = data['shell']
  return addons, shell

def clone_addons(addons):
  """Clone addons.

  args:
    addons: (list) Addons to clone.
  """
  print('Cloning addons...')
  for url in addons:
    run_cmd('cd addons; git clone {0}; cd -'.format(url))

def main():
  addons, shell = get_json_data()

  # --- Create Addons Directory ---
  create_directory(consts.addons_path)

  # _create_directory('addons')
  # os.system('mkdir addons')

  # print(data['addons'])
  # print(data['shell'])
  # print(addons)

  clone_addons(addons)

  print('Finished!')

if __name__ == '__main__':
  main()