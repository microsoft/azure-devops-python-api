# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class BuildDefinitionRevision(Model):
    """BuildDefinitionRevision.

    :param changed_by:
    :type changed_by: :class:`IdentityRef <build.v4_0.models.IdentityRef>`
    :param changed_date:
    :type changed_date: datetime
    :param change_type:
    :type change_type: object
    :param comment:
    :type comment: str
    :param definition_url:
    :type definition_url: str
    :param name:
    :type name: str
    :param revision:
    :type revision: int
    """

    _attribute_map = {
        'changed_by': {'key': 'changedBy', 'type': 'IdentityRef'},
        'changed_date': {'key': 'changedDate', 'type': 'iso-8601'},
        'change_type': {'key': 'changeType', 'type': 'object'},
        'comment': {'key': 'comment', 'type': 'str'},
        'definition_url': {'key': 'definitionUrl', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'revision': {'key': 'revision', 'type': 'int'}
    }

    def __init__(self, changed_by=None, changed_date=None, change_type=None, comment=None, definition_url=None, name=None, revision=None):
        super(BuildDefinitionRevision, self).__init__()
        self.changed_by = changed_by
        self.changed_date = changed_date
        self.change_type = change_type
        self.comment = comment
        self.definition_url = definition_url
        self.name = name
        self.revision = revision
