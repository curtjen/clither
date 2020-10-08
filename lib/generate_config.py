#!/bin/env python

# import os
import json

# THIS WORKS BUT IS NOT PREFERRED
# with open('./scripts/assets/example_config.json') as file:
#   base_config = json.loads(file)

# os.system('echo {0} >> TEST_EXAMPLE_CONFIG.json'.format(base_config))
# # print(base_config)

base_config = ({
  "addons": ["https://EXAMPLE.COM",],
  "shell": "zsh"
})

with open('TEST_EXAMPLE_CONFIG_2.json', 'w') as json_file:
  json.dump(base_config, json_file)