# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class DefinitionReference(Model):
    """DefinitionReference.

    :param created_date: The date the definition was created.
    :type created_date: datetime
    :param id: The ID of the referenced definition.
    :type id: int
    :param name: The name of the referenced definition.
    :type name: str
    :param path: The folder path of the definition.
    :type path: str
    :param project: A reference to the project.
    :type project: :class:`TeamProjectReference <build.v4_1.models.TeamProjectReference>`
    :param queue_status: A value that indicates whether builds can be queued against this definition.
    :type queue_status: object
    :param revision: The definition revision number.
    :type revision: int
    :param type: The type of the definition.
    :type type: object
    :param uri: The definition's URI.
    :type uri: str
    :param url: The REST URL of the definition.
    :type url: str
    """

    _attribute_map = {
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'path': {'key': 'path', 'type': 'str'},
        'project': {'key': 'project', 'type': 'TeamProjectReference'},
        'queue_status': {'key': 'queueStatus', 'type': 'object'},
        'revision': {'key': 'revision', 'type': 'int'},
        'type': {'key': 'type', 'type': 'object'},
        'uri': {'key': 'uri', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, created_date=None, id=None, name=None, path=None, project=None, queue_status=None, revision=None, type=None, uri=None, url=None):
        super(DefinitionReference, self).__init__()
        self.created_date = created_date
        self.id = id
        self.name = name
        self.path = path
        self.project = project
        self.queue_status = queue_status
        self.revision = revision
        self.type = type
        self.uri = uri
        self.url = url
