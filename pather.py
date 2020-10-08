# TODO(curtjen): Fix this import mess.
import os
import sys

CURRENT_DIR = os.getcwd()

def run_pathing_injections():
  paths = (
    CURRENT_DIR + '/lib',
  )

  for path in paths:
    if path not in sys.path:
      sys.path.append(path)


run_pathing_injections()