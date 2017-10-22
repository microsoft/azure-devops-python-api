# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class BuildProcess(Model):
    """BuildProcess.

    :param repositories:
    :type repositories: dict
    :param type:
    :type type: int
    """

    _attribute_map = {
        'repositories': {'key': 'repositories', 'type': '{BuildRepository}'},
        'type': {'key': 'type', 'type': 'int'}
    }

    def __init__(self, repositories=None, type=None):
        super(BuildProcess, self).__init__()
        self.repositories = repositories
        self.type = type
