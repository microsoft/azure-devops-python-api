# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class BuildDefinitionCounter(Model):
    """BuildDefinitionCounter.

    :param id: The unique Id of the Counter.
    :type id: int
    :param seed: This is the original counter value.
    :type seed: long
    :param value: This is the current counter value.
    :type value: long
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'seed': {'key': 'seed', 'type': 'long'},
        'value': {'key': 'value', 'type': 'long'}
    }

    def __init__(self, id=None, seed=None, value=None):
        super(BuildDefinitionCounter, self).__init__()
        self.id = id
        self.seed = seed
        self.value = value
