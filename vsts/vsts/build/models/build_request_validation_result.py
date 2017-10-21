# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class BuildRequestValidationResult(Model):
    """BuildRequestValidationResult.

    :param message:
    :type message: str
    :param result:
    :type result: object
    """

    _attribute_map = {
        'message': {'key': 'message', 'type': 'str'},
        'result': {'key': 'result', 'type': 'object'}
    }

    def __init__(self, message=None, result=None):
        super(BuildRequestValidationResult, self).__init__()
        self.message = message
        self.result = result
