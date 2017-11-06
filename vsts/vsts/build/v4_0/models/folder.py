# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class Folder(Model):
    """Folder.

    :param created_by: Process or person who created the folder
    :type created_by: :class:`IdentityRef <build.v4_0.models.IdentityRef>`
    :param created_on: Creation date of the folder
    :type created_on: datetime
    :param description: The description of the folder
    :type description: str
    :param last_changed_by: Process or person that last changed the folder
    :type last_changed_by: :class:`IdentityRef <build.v4_0.models.IdentityRef>`
    :param last_changed_date: Date the folder was last changed
    :type last_changed_date: datetime
    :param path: The path of the folder
    :type path: str
    :param project: The project.
    :type project: :class:`TeamProjectReference <build.v4_0.models.TeamProjectReference>`
    """

    _attribute_map = {
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'description': {'key': 'description', 'type': 'str'},
        'last_changed_by': {'key': 'lastChangedBy', 'type': 'IdentityRef'},
        'last_changed_date': {'key': 'lastChangedDate', 'type': 'iso-8601'},
        'path': {'key': 'path', 'type': 'str'},
        'project': {'key': 'project', 'type': 'TeamProjectReference'}
    }

    def __init__(self, created_by=None, created_on=None, description=None, last_changed_by=None, last_changed_date=None, path=None, project=None):
        super(Folder, self).__init__()
        self.created_by = created_by
        self.created_on = created_on
        self.description = description
        self.last_changed_by = last_changed_by
        self.last_changed_date = last_changed_date
        self.path = path
        self.project = project
