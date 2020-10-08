#!/bin/env python
"""
"""

import json
import os
# from 'lib/helpers' import create_directory
import helpers
from helpers import dry_run

def get_data():
  with open('./config.json') as file:
    data = json.load(file)
    addons = data['addons']
    shell = data['shell']
  return data, addons, shell



def main():
  if not dry_run('do this would happen now'):
    print('do this')

  data, addons, shell = get_data()

  # --- Create Addons Directory ---
  helpers.create_directory('addons')

  # _create_directory('addons')
  # os.system('mkdir addons')

  # print(data['addons'])
  # print(data['shell'])
  # print(addons)

  # --- Clone Addons ---
  for url in addons:
    print('url: ' + url)
    # os.system('cd addons; git clone ' + url + '; cd -')
    # os.system(f'cd addons; git clone {url}; cd -')
    os.system('cd addons; git clone {0}; cd -'.format(url))

  print('Finished!')

if __name__ == '__main__':
  main()