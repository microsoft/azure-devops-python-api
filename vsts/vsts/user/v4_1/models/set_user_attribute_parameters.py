# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class SetUserAttributeParameters(Model):
    """SetUserAttributeParameters.

    :param last_modified: The date/time at which the attribute was last modified.
    :type last_modified: datetime
    :param name: The unique group-prefixed name of the attribute, e.g. "TFS.TimeZone".
    :type name: str
    :param revision: The attribute's revision, for change tracking.
    :type revision: int
    :param value: The value of the attribute.
    :type value: str
    """

    _attribute_map = {
        'last_modified': {'key': 'lastModified', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'revision': {'key': 'revision', 'type': 'int'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, last_modified=None, name=None, revision=None, value=None):
        super(SetUserAttributeParameters, self).__init__()
        self.last_modified = last_modified
        self.name = name
        self.revision = revision
        self.value = value
