#!/bin/env python

import json
import os
# from 'lib/helpers' import create_directory
import helpers

with open('./config.json') as file:
  data = json.load(file)
  addons = data['addons']
  shell = data['shell']

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