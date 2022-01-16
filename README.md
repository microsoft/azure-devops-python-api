# This is a public forked repo of microsoft's [azure-devops-python-api](https://github.com/microsoft/azure-devops-python-api)!

This repository contains Python APIs for interacting with and managing Azure DevOps.

## Changes, Fixes & Enhancements

following is a list of changes on top of original repository

1. update setup.py file
2. deleted scripts directory
3. removed v5_1 clients package`
4. added 'DetailedResponse' class to return end point returned values and pagination token (bug fix for 6.0 clients)
5. Some 'get' functions in git_client_base return FullResponse object instead of only deserialized response


## installation and packaging
change version inside setup.py file <br>
execute the following from setup.py directory:
```
python setup.py sdist upload -r local
```