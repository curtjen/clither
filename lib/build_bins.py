#!/bin/env python
"""Build bins."""
import json
import re
import shutil
import time
import os
from helpers import (paths, mk_clither_custom_dirs, append_to_file, 
  process_area, get_dir_list, create_symlink, create_directory, get_epoc_time)

def get_new_path(path, prefix):
    #TODO(xnz): not system portable...
    new_path = prefix
    new_path += path.replace('/', '+')
    new_path = os.path.join(paths.bin_path, new_path)
    return new_path

def _build_paths(config, addon_path):
  direct_link_dict = {}
  # if the paths file does not exists
  # verify that the shellrc has a connection to paths file
  for bin_path in config:
    bin_path = os.path.join(addon_path, bin_path)
    new_path = get_new_path(bin_path, 'addon')

    src_dir_path = os.path.join(addon_path, bin_path)
    create_symlink(src_dir_path, new_path)

    file_names = get_dir_list(src_dir_path)

    for file_name in file_names:
      if file_name.startswith('.'):
        continue

      src_full_path = os.path.join(src_dir_path, file_name)
      if os.path.isdir(src_full_path):
        continue

      dst_full_path = os.path.join(paths.bin_path, file_name)

      result = direct_link_dict.setdefault(dst_full_path, [])
      result.append(src_full_path)

    for dst, src_list in direct_link_dict.items():
      # This is a bit nasty for 2.7, 3.x can use first, *remander syntax
      first = True
      for src in src_list:
        if first:
          create_symlink(src, dst)
          first = False
          continue

        create_directory(paths.bin_conflicts_path)
        epoch_time = get_epoc_time()
        src_base = os.path.basename(src)
        conflict_dst = '{0}_{1}'.format(epoch_time, src_base)
        conflict_dst = os.path.join(paths.bin_conflicts_path, conflict_dst)
        create_symlink(src, conflict_dst)

def _override(dir):
  pass

def mk_paths_links():

  sys_bin_paths = os.environ["PATH"]
  sys_bin_paths = sys_bin_paths.split(':')

  # use this later
  log_index = len(str(len(sys_bin_paths)))

  for index, sys_bin_path in enumerate(sys_bin_paths):
    if sys_bin_path == paths.bin_path:
      # not sure this is right? but ok for now
      continue

    index = str(index)
    new_path = get_new_path(sys_bin_path, 'path_' + index.zfill(log_index))
    create_symlink(sys_bin_path, new_path)

def main():
  print('-' * 40)
  print('Start build_bins...')

  if os.path.exists(paths.bin_path):
    shutil.rmtree(paths.bin_path)
  mk_clither_custom_dirs()
  mk_paths_links()
  print('TODO: make sure clither_custom/bin is in $PATH')

  process_area('bins', _build_paths, _override)

  print('Finished build_bins!')

if __name__ == '__main__':
  main()
