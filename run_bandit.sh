#!/usr/bin/env bash

# this script runs bandit (https://pypi.org/project/bandit/) in order
# to find security issues in python code.

# set working directory to script's dir
cd "$(dirname "$0")" || exit 1

# execute bandit with medium severity level
bandit -r ./azure-devops -ll

if [ $? -eq 0 ]; then
    echo "Security check passed"
    exit 0
else
    echo "Security check failed"
    exit 1
fi