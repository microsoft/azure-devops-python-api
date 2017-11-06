# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class BuildOption(Model):
    """BuildOption.

    :param definition:
    :type definition: :class:`BuildOptionDefinitionReference <build.v4_0.models.BuildOptionDefinitionReference>`
    :param enabled:
    :type enabled: bool
    :param inputs:
    :type inputs: dict
    """

    _attribute_map = {
        'definition': {'key': 'definition', 'type': 'BuildOptionDefinitionReference'},
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'inputs': {'key': 'inputs', 'type': '{str}'}
    }

    def __init__(self, definition=None, enabled=None, inputs=None):
        super(BuildOption, self).__init__()
        self.definition = definition
        self.enabled = enabled
        self.inputs = inputs
