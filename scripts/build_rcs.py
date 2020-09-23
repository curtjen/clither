#!/bin/env python

import json
# import os
import subprocess

# addons_dirs = os.system('ls addons')
addons_dirs = subprocess.run('ls', 'addons')
print(addons_dirs)
# with open('')