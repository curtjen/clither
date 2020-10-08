#!/bin/env python
"""Backup current RC files in the HOME directory."""

import os
from helpers import backup_file

rc_files = os.listdir('~/clither_custom/rcs')

def backup_rc_files(rc_files, home_dir):
  """For each file in bin, backup the same file name in home.

  args:
    rc_files: (list) List of existing Clither RC files.
    home_dir: (str) Path to home directory e.g. ~
  """
  for rc in rc_files:
    backup_file_path = "{0}/{1}".format(home_dir, rc)
    print("backup_file_path: " + backup_file_path)
    backup_file(backup_file_path)

def main():
  rc_files = os.listdir("bin")
  home_dir = os.environ["HOME"]
  backup_rc_files(rc_files, home_dir)

if __name__ == "__main__":
  main()
