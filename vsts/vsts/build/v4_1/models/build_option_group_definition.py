# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class BuildOptionGroupDefinition(Model):
    """BuildOptionGroupDefinition.

    :param display_name: The name of the group to display in the UI.
    :type display_name: str
    :param is_expanded: Indicates whether the group is initially displayed as expanded in the UI.
    :type is_expanded: bool
    :param name: The internal name of the group.
    :type name: str
    """

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'is_expanded': {'key': 'isExpanded', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, display_name=None, is_expanded=None, name=None):
        super(BuildOptionGroupDefinition, self).__init__()
        self.display_name = display_name
        self.is_expanded = is_expanded
        self.name = name
