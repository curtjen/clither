#!/bin/env python
"""Build RC files."""

import json
import os
from helpers import paths, mk_clither_custom_dirs, append_to_file, clear_file, process_area

#TODO(xnz): deal with name colltions.
def _build_rc_files(rc_dict, addon_path):
  for rc, config_rc_path in rc_dict.items():
    rc_dir_path = '{0}/{1}'.format(paths.rcs_path, rc)
    new_rc_path = '{0}/{1}'.format(addon_path, config_rc_path)
    import_cmd = 'source {0}'.format(new_rc_path)

    #TODO(xnz): if 2 addons address the same rc file, this is a problem.
    # we may want to do this at the start of the script.
    clear_file(rc_dir_path)
    append_to_file(rc_dir_path, import_cmd)

def _override(dir):
  pass

def main():
  print('-' * 40)
  print('Start build_rcs...')

  mk_clither_custom_dirs()
  process_area('rcs', _build_rc_files, _override)

  print('Finished build_rcs!')

if __name__ == '__main__':
  main()
