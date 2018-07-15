# This file was generated automatically from conda-smithy. To update this configuration,
# update the conda-forge.yml and/or the recipe/meta.yaml.

from yaml import safe_load
import subprocess
import json
import sys

global_config = json.loads('''
{"sources": ["conda-forge", "defaults"], "targets": [["conda-forge", "main"]]}''')
call = subprocess.check_call


def upload_package(recipe_root, config_file):
    specific_config = safe_load(open(config_file))
    if 'channel_targets' in specific_config:
        channels = [c.trim().split(' ') for c in specific_config['channel_targets'].split(',')]
    else:
        channels = global_config['targets']

    for owner, channel in channels:
        call(['upload_or_check_non_existence', recipe_root, owner, '--channel=%s' % channel, '-m', config_file])


if __name__ == '__main__':
    upload_package(sys.argv[1], sys.argv[2])
