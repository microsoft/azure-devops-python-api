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

    :param created_date: The date the definition was created
    :type created_date: datetime
    :param id: Id of the resource
    :type id: int
    :param name: Name of the linked resource (definition name, controller name, etc.)
    :type name: str
    :param path: The path this definitions belongs to
    :type path: str
    :param project: The project.
    :type project: :class:`TeamProjectReference <build.v4_0.models.TeamProjectReference>`
    :param queue_status: If builds can be queued from this definition
    :type queue_status: object
    :param revision: The definition revision number.
    :type revision: int
    :param type: The type of the definition.
    :type type: object
    :param uri: The Uri of the definition
    :type uri: str
    :param url: Full http link to the resource
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
