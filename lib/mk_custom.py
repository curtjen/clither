#!/bin/env python
"""Backup current RC files in the HOME directory."""

from helpers import create_directory, copy_file, paths, mk_clither_custom_dirs

def main():
  print('-' * 40)
  print('Start mk_custom...')
  create_directory(paths.custom_path)
  copy_file(paths.tmp_config, paths.custom_path)

  print('Finished mk_custom!')

if __name__ == "__main__":
  main()