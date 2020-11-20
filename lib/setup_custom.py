#!/bin/env python
"""Backup current RC files in the HOME directory."""
import os
from helpers import create_directory, copy_file, paths, mk_clither_custom_dirs, clean_dir



def main():
  print('-' * 40)
  print('Start mk_custom...')
  create_directory(paths.custom_path)
  copy_file(paths.clither_tmp_config, paths.custom_path)

  create_directory(paths.custom_lib_path)
  copy_file(paths.clither_run, paths.custom_path, write_over=True) # may want another lvl deep?
  copy_file(paths.clither_pather, paths.custom_path, write_over=True)
  copy_file(paths.clither_run_help, paths.custom_lib_path, write_over=True)

  # create_directory(paths.custom_default_addon_path)
  # copy_file(paths.clither_default_json, paths.custom_default_addon_path, write_over=True)
  # create_directory(paths.custom_default_addon_rcs_path)
  # copy_file(paths.clither_default_addons_rc, paths.custom_default_addon_rcs_path, write_over=True)

  create_directory(paths.custom_configs_path)
  create_directory(paths.custom_overrides_path)
  create_directory(paths.custom_fallbacks_path)
  create_directory(paths.custom_lockfile_path)

  print('Finished mk_custom!')

if __name__ == "__main__":
  main()