"""Run Intalls."""
# import json
import os

from glob import glob
from helpers import paths, mk_clither_custom_dirs, run_cmd

#TODO(xnz): mv to json, maybe addons lvl?
#TODO(xnz): What about running scrips? can't use get_installed_exe...
DESIRED_CMDS = {
  #name: (
  # (full_name, desc),
  # [deps,],
  # to_install,
  # to_update);
  'ag': (
    ('Silver Searcher', 'a tool for fast searches'),
    ['brew'],
    'brew install the_silver_searcher',
    'brew upgrade the_silver_searcher'),
  'brew': (
    ('Homebrew', 'a software package management system'),
    ['curl', 'bash'],
    'bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"',
    'brew update'),
  'curl': (
    ('client url', 'a tool to get content from url'),
    [],
    '',
    ''),
  'bash': (
    ('Bourne Again Shell', 'a *nix shell'),
    [],
    '',
    ''),
  'youtube-dl' : (
    ('Youtube downloader', 'downloads videos primarily from YouTube'),
    ['brew'],
    'brew install youtube-dl',
    'brew upgrade youtube-dl'),
  'ffmpeg' : (
    ('', 'a suite of media libraries'),
    ['brew'],
    'brew install ffmpeg',
    'brew upgrade ffmpeg'),
}
"""
brew install wget
brew install tree
brew install meld
brew install jupyter ?

"""

def get_installed_exe():
  path_exe_path = paths.custom_bin_path + '/path_*/*'
  addon_exe_path = paths.custom_bin_path + '/addon_*/*'
  all_exe = glob(path_exe_path) + glob(addon_exe_path)
  exes = {os.path.basename(x) for x in all_exe if not os.path.isdir(x)}
  return exes

def installer(installed_exe, desired_cmds):
  has_been_processed = []
  def process_node(cmd_name):
    if cmd_name not in desired_cmds:
      raise Exception('{0} is not defined.'.format(cmd_name))
    
    if cmd_name in has_been_processed:
      return

    (full_name, desc), deps, to_install, to_update =  desired_cmds[cmd_name]

    for dep in deps:
      if dep not in has_been_processed:
        process_node(dep)
    
    if not (cmd_name in installed_exe or (to_update and to_install)):
        name_element = '{0} ({1})'.format(full_name, cmd_name)
        if not full_name:
          name_element = cmd_name
        msg = (
          '{0}, {1}, was expected but not found. '
          'Install it or update desired_osx_cmds')
        raise Exception(msg.format(name_element, desc))

    cmd = to_install
    if cmd_name in installed_exe:
        cmd = to_update

    run_cmd(cmd)
    has_been_processed.append(cmd_name)
      
  for cmd in desired_cmds:
    process_node(cmd)

def main():
  print('-' * 40)
  print('Start run_installs...')
  desired_cmds = DESIRED_CMDS
  mk_clither_custom_dirs()
  installed_exe = get_installed_exe()
  installer(installed_exe, desired_cmds)
  print('Finished run_installs!')

if __name__ == "__main__":
    main(DESIRED_CMDS)