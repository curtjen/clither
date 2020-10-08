#!/bin/env python
"""
# #!/bin/bash

# # --- Compile list of files ---
# # TODO: Get Base.
# # -- Check "shell" in config. Default to bash.
# #
# # TODO: Get Addons.
# # --- Import Addons ---
# python ./scripts/addons_importer.py;

# # --- Build RCs ---
# # TODO: Write files to bin/ directory
# python ./scripts/build_rcs.py;

# # --- Create Aliases ---
# python ./scripts/generate_symlinks.py;
# # TODO: Create aliases for new RC file.
# # TODO: Backup existing and move old/existing RCs.
"""

import argparse
import os
# TODO(curtjen): Fix this import mess.
CURRENT_DIR = os.getcwd()
lib_path = CURRENT_DIR + '/lib'
import sys
if lib_path not in sys.path:
  sys.path.append(lib_path)
import addons_importer
import os

FLAGS = argparse.ArgumentParser(__doc__)
FLAGS.add_argument('--dry_run', action='store_true', help='Run without doing anything.')
FLAGS.add_argument('--addons_import', action='store_true', help='Run addons import.')
FLAGS.add_argument('--install', nargs='?', help='Run install.')
# clither.sh install
FLAGS = FLAGS.parse_args()

def _addons_importer(args):
  print('...help is on the way')
  print(args)
  addons_importer.main()

def main():
  # print(FLAGS)
  if FLAGS.install:
    print(FLAGS)
    print('install hit')
    # _addons_importer
    # _build_rcs
    # _rename
    return

  if FLAGS.addons_import:
    _addons_importer(FLAGS)
    return

if __name__ == '__main__':
  main()