#!/bin/env python
"""
"""
import json
import re
import os
from helpers import (run_cmd, create_directory, paths, mk_clither_custom_dirs,
  get_dir_list, get_epoc_time, get_new_path, cd)

EXCEPTION_TMP = """Config file does not exist: {0}

To generate, then edit, a template config.json try running: 
    $ ./clither --mk_custom; vi ../clither_custom/config.json"""

def clone_addons(addons):
  """Clone addons.

  args:
    addons: (list) Addons to clone.
  """
  print('Cloning addons...')

  used_addons = set()
  for url in addons:
    addon_name = os.path.basename(url)

    git_repo_comp = re.compile(r'https?://(.+?)(.git)*$')
    match = git_repo_comp.match(url)

    trucated_url = addon_name
    if match:
      trucated_url , _ = match.groups()

    new_addon_name = get_new_path(
       trucated_url, paths.custom_addons_path, '')

    print('add ' + new_addon_name)
    used_addons.add(new_addon_name)
    if os.path.exists(new_addon_name):
      run_cmd(cd(new_addon_name), 'git pull')
      continue

    run_cmd(cd(paths.custom_addons_path), 'git clone ' +  url)
    addon_path = os.path.join(paths.custom_addons_path, addon_name)

    os.rename(addon_path, new_addon_name)  #TODO(xnz): absract to helper
    print('rename {0} to {1}'.format(addon_path, new_addon_name))

  existing_addons = set(
    os.path.join(paths.custom_addons_path, entry) 
    for entry in get_dir_list(paths.custom_addons_path))

  extra_addons = existing_addons - used_addons
  if extra_addons:
    print('You have untracked addons: ' + ', '.join(extra_addons))

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
    addons = get_json(paths.custom_addons_config)
  except IOError:
    msg = EXCEPTION_TMP.format(paths.custom_addons_config)
    raise Exception(msg)

  clone_addons(addons)

  print('Finished addons_importer!')

if __name__ == '__main__':
  main()