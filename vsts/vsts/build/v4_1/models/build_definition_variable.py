# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class BuildDefinitionVariable(Model):
    """BuildDefinitionVariable.

    :param allow_override: Indicates whether the value can be set at queue time.
    :type allow_override: bool
    :param is_secret: Indicates whether the variable's value is a secret.
    :type is_secret: bool
    :param value: The value of the variable.
    :type value: str
    """

    _attribute_map = {
        'allow_override': {'key': 'allowOverride', 'type': 'bool'},
        'is_secret': {'key': 'isSecret', 'type': 'bool'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, allow_override=None, is_secret=None, value=None):
        super(BuildDefinitionVariable, self).__init__()
        self.allow_override = allow_override
        self.is_secret = is_secret
        self.value = value
