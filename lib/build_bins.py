#!/bin/env python
"""Build bins."""
import json
import os
from helpers import paths, mk_clither_custom_dirs, append_to_file, clear_file, process_area, get_dir_list

def _build_paths(config, addon_path):
  # if the paths file does not exists
  # verify that the shellrc has a connection to paths file
  for bin_path in config:
    src_dir_path = os.path.join(addon_path, bin_path)
    file_names = get_dir_list(src_dir_path)

    # Oprion 1
    for file_name in file_names:
      src_full_path = os.path.join(src_dir_path, file_name)
      dst_full_path = os.path.join(paths.bin_path, file_name)

      print('will need to check if dst_full_path exists, if so do something dope')
      print('could do file: create_symlink({0}, {1})'.format(src_full_path, dst_full_path))

    # Option 2
    print('  or just the dir: create_symlink({0}, {1})'.format(src_dir_path, paths.bin_path))
    print('  in this case you will need to add {0} to PATH'.format(src_dir_path))

def _override(dir):
  pass

def main():
  print('-' * 40)
  print('Start build_bins...')

  #print(os.environ)
  print('Get content for $PATH, and make sure you dont have clither_custom in there')  # will look like:
  sys_bin_paths = '/Users/phuntzinger/.nvm/versions/node/v10.15.0/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/sbin:/usr/local/munki:/Users/phuntzinger/bin'
  sys_bin_paths = sys_bin_paths.split(':')
  print('clear out everyting in clither_custom/bin')
  for sys_bin_path in sys_bin_paths:
    print('create_symlink(({0}, {1})'.format(sys_bin_path, paths.bin_path))
  print('make sure clither_custom/bin is in $PATH')

  # mk_clither_custom_dirs()
  process_area('bins', _build_paths, _override)

  print('Finished build_bins!')

if __name__ == '__main__':
  main()
