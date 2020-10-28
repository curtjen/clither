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

def run_clither(args):
  flags = ' '.join(args)
  if not args:
    flags = '--setup_custom --install'
  run_cmd(cd(paths.clither_path), './clither.py ' + flags)

def main(args):
  get_clither()
  run_clither(args)

if __name__ == "__main__":
    main(sys.argv[1:])


