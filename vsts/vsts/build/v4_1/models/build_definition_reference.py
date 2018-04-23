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
    :param _links:
    :type _links: :class:`ReferenceLinks <build.v4_1.models.ReferenceLinks>`
    :param authored_by: The author of the definition.
    :type authored_by: :class:`IdentityRef <build.v4_1.models.IdentityRef>`
    :param draft_of: A reference to the definition that this definition is a draft of, if this is a draft definition.
    :type draft_of: :class:`DefinitionReference <build.v4_1.models.DefinitionReference>`
    :param drafts: The list of drafts associated with this definition, if this is not a draft definition.
    :type drafts: list of :class:`DefinitionReference <build.v4_1.models.DefinitionReference>`
    :param latest_build:
    :type latest_build: :class:`Build <build.v4_1.models.Build>`
    :param latest_completed_build:
    :type latest_completed_build: :class:`Build <build.v4_1.models.Build>`
    :param metrics:
    :type metrics: list of :class:`BuildMetric <build.v4_1.models.BuildMetric>`
    :param quality: The quality of the definition document (draft, etc.)
    :type quality: object
    :param queue: The default queue for builds run against this definition.
    :type queue: :class:`AgentPoolQueue <build.v4_1.models.AgentPoolQueue>`
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
        'drafts': {'key': 'drafts', 'type': '[DefinitionReference]'},
        'latest_build': {'key': 'latestBuild', 'type': 'Build'},
        'latest_completed_build': {'key': 'latestCompletedBuild', 'type': 'Build'},
        'metrics': {'key': 'metrics', 'type': '[BuildMetric]'},
        'quality': {'key': 'quality', 'type': 'object'},
        'queue': {'key': 'queue', 'type': 'AgentPoolQueue'}
    }

    def __init__(self, created_date=None, id=None, name=None, path=None, project=None, queue_status=None, revision=None, type=None, uri=None, url=None, _links=None, authored_by=None, draft_of=None, drafts=None, latest_build=None, latest_completed_build=None, metrics=None, quality=None, queue=None):
        super(BuildDefinitionReference, self).__init__(created_date=created_date, id=id, name=name, path=path, project=project, queue_status=queue_status, revision=revision, type=type, uri=uri, url=url)
        self._links = _links
        self.authored_by = authored_by
        self.draft_of = draft_of
        self.drafts = drafts
        self.latest_build = latest_build
        self.latest_completed_build = latest_completed_build
        self.metrics = metrics
        self.quality = quality
        self.queue = queue
