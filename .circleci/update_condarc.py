# This file was generated automatically from conda-smithy. To update this configuration,
# update the conda-forge.yml and/or the recipe/meta.yaml.

from yaml import safe_load
import subprocess
import json
import sys

global_config = json.loads('''
{"sources": ["conda-forge", "defaults"], "targets": [["conda-forge", "main"]]}''')
call = subprocess.check_call


def setup_conda_rc(config_file):
    specific_config = safe_load(open(config_file))
    if 'channel_sources' in specific_config:
        channels = [c.trim() for c in specific_config['channel_sources'].split(',')]
    else:
        channels  = global_config['sources']

    call(['conda', 'config', '--remove', 'channels' 'defaults'])
    for c in reversed(channels):
        call(['conda', 'config', '--add', 'channels', c])

    call(['conda', 'config' '--set', 'show_channel_urls', 'true'])


if __name__ == '__main__':
    setup_conda_rc(sys.argv[1])
