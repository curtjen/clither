"""Run Intalls."""
# import json
import os

from glob import glob
from helpers import paths, mk_clither_custom_dirs, run_cmd, process_area, clear_file

def get_installed_exe():
  path_exe_path = paths.custom_bin_path + '/path_*/*'
  addon_exe_path = paths.custom_bin_path + '/addon_*/*'
  all_exe = glob(path_exe_path) + glob(addon_exe_path)
  exes = {os.path.basename(x) for x in all_exe if not os.path.isdir(x)}
  return exes

def installer(desired_cmds, addon_path):

  has_been_processed = []
  def process_node(cmd_name):
    if cmd_name not in desired_cmds:
      raise Exception('{0} is not defined.'.format(cmd_name))
    
    if cmd_name in has_been_processed:
      return

    _type, deps, to_install, to_update =  desired_cmds[cmd_name]

    if not any([deps, to_install, to_update]):
      return

    for dep in deps:
      if dep not in has_been_processed:
        process_node(dep)
    
    run_install = True  # tmp until get logic for script

    if _type == 'path':
      path_exes = get_installed_exe()
      run_install = cmd_name not in path_exes

    lock_file = os.path.basename(addon_path)
    lock_file += '.installed'
    lock_file = os.path.join(paths.custom_lockfile_path, lock_file)
    if _type == 'install' and os.path.exists(lock_file):
      run_install = False

    cmd = None
    if run_install and to_install:
      cmd = to_install

    if not run_install and to_update:
      cmd = to_update

    if not cmd and _type == 'install':
      return

    if not cmd:
      msg = ('{0} line is malformed. Look into it.')
      raise Exception(msg.format(cmd_name))

    cmd = cmd.format(addon_path)

    run_cmd(cmd)
    has_been_processed.append(cmd_name)

    if _type == 'install' and not os.path.exists(lock_file):
      clear_file(lock_file)

  for cmd in desired_cmds:
    process_node(cmd)

def _override(dir):
  pass

def main():
  print('-' * 40)
  print('Start run_installs...')
  mk_clither_custom_dirs()
  process_area('installs', installer, _override)

  print('Finished run_installs!')

if __name__ == "__main__":
  main(DESIRED_CMDS)