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

    :param type:
    :type type: int
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'int'}
    }

    def __init__(self, type=None):
        super(BuildProcess, self).__init__()
        self.type = type
