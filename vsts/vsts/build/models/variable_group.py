# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from .variable_group_reference import VariableGroupReference


class VariableGroup(VariableGroupReference):
    """VariableGroup.

    :param id:
    :type id: int
    :param description:
    :type description: str
    :param name:
    :type name: str
    :param type:
    :type type: str
    :param variables:
    :type variables: dict
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'description': {'key': 'description', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'variables': {'key': 'variables', 'type': '{BuildDefinitionVariable}'}
    }

    def __init__(self, id=None, description=None, name=None, type=None, variables=None):
        super(VariableGroup, self).__init__(id=id)
        self.description = description
        self.name = name
        self.type = type
        self.variables = variables
