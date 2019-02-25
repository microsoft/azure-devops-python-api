# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from __future__ import print_function

import sys
import glob
import os
from subprocess import check_call, CalledProcessError

def exec_command(command):
    try:
        print('Executing: ' + command)
        check_call(command.split(), cwd=root_dir)
        print()
    except CalledProcessError as err:
        print(err, file=sys.stderr)
        sys.exit(1)


print('Running dev setup...')

root_dir = os.path.abspath(os.path.join(os.path.abspath(__file__), '..', '..'))
print('Root directory \'{}\'\n'.format(root_dir))

exec_command('python -m pip install --upgrade pip')
exec_command('python -m pip install --upgrade wheel')

# install general requirements
if os.path.isfile('./requirements.txt'):
    exec_command('pip install -r requirements.txt')

# install dev packages
exec_command('pip install -e azure-devops')

# install packaging requirements
if os.path.isfile('./scripts/packaging_requirements.txt'):
    exec_command('pip install -r scripts/packaging_requirements.txt')
