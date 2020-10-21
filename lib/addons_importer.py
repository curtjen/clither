#!/bin/env python
"""
"""
import json
import os
from helpers import (run_cmd, create_directory, paths, mk_clither_custom_dirs,
  get_dir_list, get_epoc_time, get_new_path)

EXCEPTION_TMP = """Config file does not exist: {0}

To generate, then edit, a template config.json try running: 
    $ ./clither --mk_custom; vi ../clither_custom/config.json"""

def clone_addons(addons):
  """Clone addons.

  args:
    addons: (list) Addons to clone.
  """
  print('Cloning addons...')
  # pre_install_addons = set(get_dir_list(paths.custom_addons_path))

  used_addons = set()
  for url in addons:
    addon_name = os.path.basename(url)
    new_addon_name = get_new_path(url[8:],paths.custom_addons_path, '')

    if new_addon_name.endswith('.git'):
      new_addon_name = new_addon_name[:-4]

    used_addons.add(new_addon_name)
    if os.path.exists(new_addon_name):
      run_cmd('cd {0}; git pull'.format(paths.custom_addons_path))
      continue

    run_cmd('cd {0}; git clone {1}'.format(paths.custom_addons_path, url))
    addon_path = os.path.join(paths.custom_addons_path, addon_name)
    print(addon_path)
    os.rename(addon_path, new_addon_name)
    print('rename {0} to {1}'.format(addon_path, new_addon_name))

  existing_addons = set(
    os.path.join(paths.custom_addons_path, entry) 
    for entry in get_dir_list(paths.custom_addons_path))

  extra_addons = existing_addons - used_addons
  if extra_addons:
    print('you have extra addons, do something with them: ' + str(extra_addons))



  # post_install_addons = set(get_dir_list(paths.custom_addons_path))

  # new_addons = post_install_addons - pre_install_addons

  # for addon in new_addons:
  #   src = os.path.join(paths.custom_addons_path, addon)
  #   epoc = get_epoc_time()
  #   dst = os.path.join(paths.custom_addons_path, '{0}_{1}'.format(epoc, addon))
  #   os.rename(src, dst)


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