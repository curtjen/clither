#!/usr/bin/env python
import os
import sys

import pather  # Run before lib imports
from helpers import cd, run_cmd, paths


def get_clither():
  """Get clither."""
  print('Getting clither...')

  if os.path.exists(paths.clither_path):
    run_cmd(cd(paths.clither_path), 'git pull')
    return

  run_cmd(cd(paths.base_dir), 'git clone ' + paths.clither_base_repo)

def run_clither():
  run_cmd(cd(paths.clither_path), './clither.py --install')

def main():
  get_clither()
  run_clither()

if __name__ == "__main__":
    main()


