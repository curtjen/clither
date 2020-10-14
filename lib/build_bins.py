#!/bin/env python
"""Build bins."""
import json
import os
from helpers import paths, mk_clither_custom_dirs, append_to_file, clear_file, process_area

def _build_paths(config, addon_path):
  # if the paths file does not exists
  # verify that the shellrc has a connection to paths file
  for bin_path in config:
    pass
    # mk link for real location of bin_path, call it rbin_path
    # mk simlink from the rbin_path to paths.bin_path, call it end_path for now.
    # Add a PATHS+=:end_path to paths file
  

def _override(dir):
  pass

def main():
  print('-' * 40)
  print('Start build_bins...')

  mk_clither_custom_dirs()
  process_area('bins', _build_paths, _override)

  print('Finished build_bins!')

if __name__ == '__main__':
  main()
