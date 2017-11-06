# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from .build_option_definition_reference import BuildOptionDefinitionReference


class BuildOptionDefinition(BuildOptionDefinitionReference):
    """BuildOptionDefinition.

    :param id: The ID of the referenced build option.
    :type id: str
    :param description: The description.
    :type description: str
    :param groups: The list of input groups defined for the build option.
    :type groups: list of :class:`BuildOptionGroupDefinition <build.v4_1.models.BuildOptionGroupDefinition>`
    :param inputs: The list of inputs defined for the build option.
    :type inputs: list of :class:`BuildOptionInputDefinition <build.v4_1.models.BuildOptionInputDefinition>`
    :param name: The name of the build option.
    :type name: str
    :param ordinal: A value that indicates the relative order in which the behavior should be applied.
    :type ordinal: int
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'groups': {'key': 'groups', 'type': '[BuildOptionGroupDefinition]'},
        'inputs': {'key': 'inputs', 'type': '[BuildOptionInputDefinition]'},
        'name': {'key': 'name', 'type': 'str'},
        'ordinal': {'key': 'ordinal', 'type': 'int'}
    }

    def __init__(self, id=None, description=None, groups=None, inputs=None, name=None, ordinal=None):
        super(BuildOptionDefinition, self).__init__(id=id)
        self.description = description
        self.groups = groups
        self.inputs = inputs
        self.name = name
        self.ordinal = ordinal
