# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class Build(Model):
    """Build.

    :param _links:
    :type _links: :class:`ReferenceLinks <build.v4_0.models.ReferenceLinks>`
    :param build_number: Build number/name of the build
    :type build_number: str
    :param build_number_revision: Build number revision
    :type build_number_revision: int
    :param controller: The build controller. This should only be set if the definition type is Xaml.
    :type controller: :class:`BuildController <build.v4_0.models.BuildController>`
    :param definition: The definition associated with the build
    :type definition: :class:`DefinitionReference <build.v4_0.models.DefinitionReference>`
    :param deleted: Indicates whether the build has been deleted.
    :type deleted: bool
    :param deleted_by: Process or person that deleted the build
    :type deleted_by: :class:`IdentityRef <build.v4_0.models.IdentityRef>`
    :param deleted_date: Date the build was deleted
    :type deleted_date: datetime
    :param deleted_reason: Description of how the build was deleted
    :type deleted_reason: str
    :param demands: Demands
    :type demands: list of :class:`object <build.v4_0.models.object>`
    :param finish_time: Time that the build was completed
    :type finish_time: datetime
    :param id: Id of the build
    :type id: int
    :param keep_forever:
    :type keep_forever: bool
    :param last_changed_by: Process or person that last changed the build
    :type last_changed_by: :class:`IdentityRef <build.v4_0.models.IdentityRef>`
    :param last_changed_date: Date the build was last changed
    :type last_changed_date: datetime
    :param logs: Log location of the build
    :type logs: :class:`BuildLogReference <build.v4_0.models.BuildLogReference>`
    :param orchestration_plan: Orchestration plan for the build
    :type orchestration_plan: :class:`TaskOrchestrationPlanReference <build.v4_0.models.TaskOrchestrationPlanReference>`
    :param parameters: Parameters for the build
    :type parameters: str
    :param plans: Orchestration plans associated with the build (build, cleanup)
    :type plans: list of :class:`TaskOrchestrationPlanReference <build.v4_0.models.TaskOrchestrationPlanReference>`
    :param priority: The build's priority
    :type priority: object
    :param project: The team project
    :type project: :class:`TeamProjectReference <build.v4_0.models.TeamProjectReference>`
    :param properties:
    :type properties: :class:`object <build.v4_0.models.object>`
    :param quality: Quality of the xaml build (good, bad, etc.)
    :type quality: str
    :param queue: The queue. This should only be set if the definition type is Build.
    :type queue: :class:`AgentPoolQueue <build.v4_0.models.AgentPoolQueue>`
    :param queue_options: Queue option of the build.
    :type queue_options: object
    :param queue_position: The current position of the build in the queue
    :type queue_position: int
    :param queue_time: Time that the build was queued
    :type queue_time: datetime
    :param reason: Reason that the build was created
    :type reason: object
    :param repository: The repository
    :type repository: :class:`BuildRepository <build.v4_0.models.BuildRepository>`
    :param requested_by: The identity that queued the build
    :type requested_by: :class:`IdentityRef <build.v4_0.models.IdentityRef>`
    :param requested_for: The identity on whose behalf the build was queued
    :type requested_for: :class:`IdentityRef <build.v4_0.models.IdentityRef>`
    :param result: The build result
    :type result: object
    :param retained_by_release: Specifies if Build should be retained by Release
    :type retained_by_release: bool
    :param source_branch: Source branch
    :type source_branch: str
    :param source_version: Source version
    :type source_version: str
    :param start_time: Time that the build was started
    :type start_time: datetime
    :param status: Status of the build
    :type status: object
    :param tags:
    :type tags: list of str
    :param trigger_info: Sourceprovider-specific information about what triggered the build
    :type trigger_info: dict
    :param uri: Uri of the build
    :type uri: str
    :param url: REST url of the build
    :type url: str
    :param validation_results:
    :type validation_results: list of :class:`BuildRequestValidationResult <build.v4_0.models.BuildRequestValidationResult>`
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'build_number': {'key': 'buildNumber', 'type': 'str'},
        'build_number_revision': {'key': 'buildNumberRevision', 'type': 'int'},
        'controller': {'key': 'controller', 'type': 'BuildController'},
        'definition': {'key': 'definition', 'type': 'DefinitionReference'},
        'deleted': {'key': 'deleted', 'type': 'bool'},
        'deleted_by': {'key': 'deletedBy', 'type': 'IdentityRef'},
        'deleted_date': {'key': 'deletedDate', 'type': 'iso-8601'},
        'deleted_reason': {'key': 'deletedReason', 'type': 'str'},
        'demands': {'key': 'demands', 'type': '[object]'},
        'finish_time': {'key': 'finishTime', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'int'},
        'keep_forever': {'key': 'keepForever', 'type': 'bool'},
        'last_changed_by': {'key': 'lastChangedBy', 'type': 'IdentityRef'},
        'last_changed_date': {'key': 'lastChangedDate', 'type': 'iso-8601'},
        'logs': {'key': 'logs', 'type': 'BuildLogReference'},
        'orchestration_plan': {'key': 'orchestrationPlan', 'type': 'TaskOrchestrationPlanReference'},
        'parameters': {'key': 'parameters', 'type': 'str'},
        'plans': {'key': 'plans', 'type': '[TaskOrchestrationPlanReference]'},
        'priority': {'key': 'priority', 'type': 'object'},
        'project': {'key': 'project', 'type': 'TeamProjectReference'},
        'properties': {'key': 'properties', 'type': 'object'},
        'quality': {'key': 'quality', 'type': 'str'},
        'queue': {'key': 'queue', 'type': 'AgentPoolQueue'},
        'queue_options': {'key': 'queueOptions', 'type': 'object'},
        'queue_position': {'key': 'queuePosition', 'type': 'int'},
        'queue_time': {'key': 'queueTime', 'type': 'iso-8601'},
        'reason': {'key': 'reason', 'type': 'object'},
        'repository': {'key': 'repository', 'type': 'BuildRepository'},
        'requested_by': {'key': 'requestedBy', 'type': 'IdentityRef'},
        'requested_for': {'key': 'requestedFor', 'type': 'IdentityRef'},
        'result': {'key': 'result', 'type': 'object'},
        'retained_by_release': {'key': 'retainedByRelease', 'type': 'bool'},
        'source_branch': {'key': 'sourceBranch', 'type': 'str'},
        'source_version': {'key': 'sourceVersion', 'type': 'str'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'status': {'key': 'status', 'type': 'object'},
        'tags': {'key': 'tags', 'type': '[str]'},
        'trigger_info': {'key': 'triggerInfo', 'type': '{str}'},
        'uri': {'key': 'uri', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'validation_results': {'key': 'validationResults', 'type': '[BuildRequestValidationResult]'}
    }

    def __init__(self, _links=None, build_number=None, build_number_revision=None, controller=None, definition=None, deleted=None, deleted_by=None, deleted_date=None, deleted_reason=None, demands=None, finish_time=None, id=None, keep_forever=None, last_changed_by=None, last_changed_date=None, logs=None, orchestration_plan=None, parameters=None, plans=None, priority=None, project=None, properties=None, quality=None, queue=None, queue_options=None, queue_position=None, queue_time=None, reason=None, repository=None, requested_by=None, requested_for=None, result=None, retained_by_release=None, source_branch=None, source_version=None, start_time=None, status=None, tags=None, trigger_info=None, uri=None, url=None, validation_results=None):
        super(Build, self).__init__()
        self._links = _links
        self.build_number = build_number
        self.build_number_revision = build_number_revision
        self.controller = controller
        self.definition = definition
        self.deleted = deleted
        self.deleted_by = deleted_by
        self.deleted_date = deleted_date
        self.deleted_reason = deleted_reason
        self.demands = demands
        self.finish_time = finish_time
        self.id = id
        self.keep_forever = keep_forever
        self.last_changed_by = last_changed_by
        self.last_changed_date = last_changed_date
        self.logs = logs
        self.orchestration_plan = orchestration_plan
        self.parameters = parameters
        self.plans = plans
        self.priority = priority
        self.project = project
        self.properties = properties
        self.quality = quality
        self.queue = queue
        self.queue_options = queue_options
        self.queue_position = queue_position
        self.queue_time = queue_time
        self.reason = reason
        self.repository = repository
        self.requested_by = requested_by
        self.requested_for = requested_for
        self.result = result
        self.retained_by_release = retained_by_release
        self.source_branch = source_branch
        self.source_version = source_version
        self.start_time = start_time
        self.status = status
        self.tags = tags
        self.trigger_info = trigger_info
        self.uri = uri
        self.url = url
        self.validation_results = validation_results
