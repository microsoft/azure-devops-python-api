# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class BuildOptionInputDefinition(Model):
    """BuildOptionInputDefinition.

    :param default_value: The default value.
    :type default_value: str
    :param group_name: The name of the input group that this input belongs to.
    :type group_name: str
    :param help:
    :type help: dict
    :param label: The label for the input.
    :type label: str
    :param name: The name of the input.
    :type name: str
    :param options:
    :type options: dict
    :param required: Indicates whether the input is required to have a value.
    :type required: bool
    :param type: Indicates the type of the input value.
    :type type: object
    :param visible_rule: The rule that is applied to determine whether the input is visible in the UI.
    :type visible_rule: str
    """

    _attribute_map = {
        'default_value': {'key': 'defaultValue', 'type': 'str'},
        'group_name': {'key': 'groupName', 'type': 'str'},
        'help': {'key': 'help', 'type': '{str}'},
        'label': {'key': 'label', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'options': {'key': 'options', 'type': '{str}'},
        'required': {'key': 'required', 'type': 'bool'},
        'type': {'key': 'type', 'type': 'object'},
        'visible_rule': {'key': 'visibleRule', 'type': 'str'}
    }

    def __init__(self, default_value=None, group_name=None, help=None, label=None, name=None, options=None, required=None, type=None, visible_rule=None):
        super(BuildOptionInputDefinition, self).__init__()
        self.default_value = default_value
        self.group_name = group_name
        self.help = help
        self.label = label
        self.name = name
        self.options = options
        self.required = required
        self.type = type
        self.visible_rule = visible_rule
