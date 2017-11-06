# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from .definition_reference import DefinitionReference


class BuildDefinitionReference(DefinitionReference):
    """BuildDefinitionReference.

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
    :param _links:
    :type _links: :class:`ReferenceLinks <build.v4_0.models.ReferenceLinks>`
    :param authored_by: The author of the definition.
    :type authored_by: :class:`IdentityRef <build.v4_0.models.IdentityRef>`
    :param draft_of: If this is a draft definition, it might have a parent
    :type draft_of: :class:`DefinitionReference <build.v4_0.models.DefinitionReference>`
    :param metrics:
    :type metrics: list of :class:`BuildMetric <build.v4_0.models.BuildMetric>`
    :param quality: The quality of the definition document (draft, etc.)
    :type quality: object
    :param queue: The default queue which should be used for requests.
    :type queue: :class:`AgentPoolQueue <build.v4_0.models.AgentPoolQueue>`
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
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'authored_by': {'key': 'authoredBy', 'type': 'IdentityRef'},
        'draft_of': {'key': 'draftOf', 'type': 'DefinitionReference'},
        'metrics': {'key': 'metrics', 'type': '[BuildMetric]'},
        'quality': {'key': 'quality', 'type': 'object'},
        'queue': {'key': 'queue', 'type': 'AgentPoolQueue'}
    }

    def __init__(self, created_date=None, id=None, name=None, path=None, project=None, queue_status=None, revision=None, type=None, uri=None, url=None, _links=None, authored_by=None, draft_of=None, metrics=None, quality=None, queue=None):
        super(BuildDefinitionReference, self).__init__(created_date=created_date, id=id, name=name, path=path, project=project, queue_status=queue_status, revision=revision, type=type, uri=uri, url=url)
        self._links = _links
        self.authored_by = authored_by
        self.draft_of = draft_of
        self.metrics = metrics
        self.quality = quality
        self.queue = queue
