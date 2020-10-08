#!/bin/env python
"""
"""

import json
import os
# from 'lib/helpers' import create_directory
import helpers
from helpers import dry_run

def get_json_data():
  with open(helper.CONFIG_FILE) as file:
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
    helpers.run_cmd('cd addons; git clone {0}; cd -'.format(url))

def main():
  addons, shell = get_json_data()

  # --- Create Addons Directory ---
  helpers.create_directory(helper.ADDONS_PATH)

  # _create_directory('addons')
  # os.system('mkdir addons')

  # print(data['addons'])
  # print(data['shell'])
  # print(addons)

  clone_addons(addons)

  print('Finished!')

if __name__ == '__main__':
  main()