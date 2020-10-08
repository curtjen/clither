# TODO(curtjen): Fix this import mess.
import os
import sys

def run_pathing_injections():
  CURRENT_DIR = os.getcwd()
  lib_path = CURRENT_DIR + '/lib'
  if lib_path not in sys.path:
    sys.path.append(lib_path)

run_pathing_injections()