# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class Issue(Model):
    """
    An issue (error, warning) associated with a pipeline run.

    :param category: The category of the issue. <br />Example: Code - refers to compilation errors <br />Example: General - refers to generic errors
    :type category: str
    :param data: A dictionary containing details about the issue.
    :type data: dict
    :param message: A description of issue.
    :type message: str
    :param type: The type (error, warning) of the issue.
    :type type: object
    """

    _attribute_map = {
        'category': {'key': 'category', 'type': 'str'},
        'data': {'key': 'data', 'type': '{str}'},
        'message': {'key': 'message', 'type': 'str'},
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, category=None, data=None, message=None, type=None):
        super(Issue, self).__init__()
        self.category = category
        self.data = data
        self.message = message
        self.type = type


class JobEvent(Model):
    """
    A pipeline job event to be processed by the execution plan.

    :param job_id: The ID of the pipeline job affected by the event.
    :type job_id: str
    :param name: The name of the pipeline job event.
    :type name: str
    """

    _attribute_map = {
        'job_id': {'key': 'jobId', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, job_id=None, name=None):
        super(JobEvent, self).__init__()
        self.job_id = job_id
        self.name = name


class JobOption(Model):
    """
    Represents an option that may affect the way an agent runs the job.

    :param data:
    :type data: dict
    :param id: Gets the id of the option.
    :type id: str
    """

    _attribute_map = {
        'data': {'key': 'data', 'type': '{str}'},
        'id': {'key': 'id', 'type': 'str'}
    }

    def __init__(self, data=None, id=None):
        super(JobOption, self).__init__()
        self.data = data
        self.id = id


class MaskHint(Model):
    """
    :param type:
    :type type: object
    :param value:
    :type value: str
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'object'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, type=None, value=None):
        super(MaskHint, self).__init__()
        self.type = type
        self.value = value


class PlanEnvironment(Model):
    """
    :param mask:
    :type mask: list of :class:`MaskHint <azure.devops.v7_1.task.models.MaskHint>`
    :param options:
    :type options: dict
    :param variables:
    :type variables: dict
    """

    _attribute_map = {
        'mask': {'key': 'mask', 'type': '[MaskHint]'},
        'options': {'key': 'options', 'type': '{JobOption}'},
        'variables': {'key': 'variables', 'type': '{str}'}
    }

    def __init__(self, mask=None, options=None, variables=None):
        super(PlanEnvironment, self).__init__()
        self.mask = mask
        self.options = options
        self.variables = variables


class ProjectReference(Model):
    """
    :param id:
    :type id: str
    :param name:
    :type name: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, id=None, name=None):
        super(ProjectReference, self).__init__()
        self.id = id
        self.name = name


class ReferenceLinks(Model):
    """
    The class to represent a collection of REST reference links.

    :param links: The readonly view of the links.  Because Reference links are readonly, we only want to expose them as read only.
    :type links: dict
    """

    _attribute_map = {
        'links': {'key': 'links', 'type': '{object}'}
    }

    def __init__(self, links=None):
        super(ReferenceLinks, self).__init__()
        self.links = links


class TaskAgentJob(Model):
    """
    :param container:
    :type container: str
    :param id:
    :type id: str
    :param name:
    :type name: str
    :param sidecar_containers:
    :type sidecar_containers: dict
    :param steps:
    :type steps: list of :class:`TaskAgentJobStep <azure.devops.v7_1.task.models.TaskAgentJobStep>`
    :param variables:
    :type variables: list of :class:`TaskAgentJobVariable <azure.devops.v7_1.task.models.TaskAgentJobVariable>`
    """

    _attribute_map = {
        'container': {'key': 'container', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'sidecar_containers': {'key': 'sidecarContainers', 'type': '{str}'},
        'steps': {'key': 'steps', 'type': '[TaskAgentJobStep]'},
        'variables': {'key': 'variables', 'type': '[TaskAgentJobVariable]'}
    }

    def __init__(self, container=None, id=None, name=None, sidecar_containers=None, steps=None, variables=None):
        super(TaskAgentJob, self).__init__()
        self.container = container
        self.id = id
        self.name = name
        self.sidecar_containers = sidecar_containers
        self.steps = steps
        self.variables = variables


class TaskAgentJobStep(Model):
    """
    :param condition:
    :type condition: str
    :param continue_on_error:
    :type continue_on_error: bool
    :param enabled:
    :type enabled: bool
    :param env:
    :type env: dict
    :param id:
    :type id: str
    :param inputs:
    :type inputs: dict
    :param name:
    :type name: str
    :param retry_count_on_task_failure:
    :type retry_count_on_task_failure: int
    :param task:
    :type task: :class:`TaskAgentJobTask <azure.devops.v7_1.task.models.TaskAgentJobTask>`
    :param timeout_in_minutes:
    :type timeout_in_minutes: int
    :param type:
    :type type: object
    """

    _attribute_map = {
        'condition': {'key': 'condition', 'type': 'str'},
        'continue_on_error': {'key': 'continueOnError', 'type': 'bool'},
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'env': {'key': 'env', 'type': '{str}'},
        'id': {'key': 'id', 'type': 'str'},
        'inputs': {'key': 'inputs', 'type': '{str}'},
        'name': {'key': 'name', 'type': 'str'},
        'retry_count_on_task_failure': {'key': 'retryCountOnTaskFailure', 'type': 'int'},
        'task': {'key': 'task', 'type': 'TaskAgentJobTask'},
        'timeout_in_minutes': {'key': 'timeoutInMinutes', 'type': 'int'},
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, condition=None, continue_on_error=None, enabled=None, env=None, id=None, inputs=None, name=None, retry_count_on_task_failure=None, task=None, timeout_in_minutes=None, type=None):
        super(TaskAgentJobStep, self).__init__()
        self.condition = condition
        self.continue_on_error = continue_on_error
        self.enabled = enabled
        self.env = env
        self.id = id
        self.inputs = inputs
        self.name = name
        self.retry_count_on_task_failure = retry_count_on_task_failure
        self.task = task
        self.timeout_in_minutes = timeout_in_minutes
        self.type = type


class TaskAgentJobTask(Model):
    """
    :param id:
    :type id: str
    :param name:
    :type name: str
    :param version:
    :type version: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, id=None, name=None, version=None):
        super(TaskAgentJobTask, self).__init__()
        self.id = id
        self.name = name
        self.version = version


class TaskAgentJobVariable(Model):
    """
    :param name:
    :type name: str
    :param secret:
    :type secret: bool
    :param value:
    :type value: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'secret': {'key': 'secret', 'type': 'bool'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, name=None, secret=None, value=None):
        super(TaskAgentJobVariable, self).__init__()
        self.name = name
        self.secret = secret
        self.value = value


class TaskAttachment(Model):
    """
    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v7_1.task.models.ReferenceLinks>`
    :param created_on:
    :type created_on: datetime
    :param last_changed_by:
    :type last_changed_by: str
    :param last_changed_on:
    :type last_changed_on: datetime
    :param name:
    :type name: str
    :param record_id:
    :type record_id: str
    :param timeline_id:
    :type timeline_id: str
    :param type:
    :type type: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'last_changed_by': {'key': 'lastChangedBy', 'type': 'str'},
        'last_changed_on': {'key': 'lastChangedOn', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'record_id': {'key': 'recordId', 'type': 'str'},
        'timeline_id': {'key': 'timelineId', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, _links=None, created_on=None, last_changed_by=None, last_changed_on=None, name=None, record_id=None, timeline_id=None, type=None):
        super(TaskAttachment, self).__init__()
        self._links = _links
        self.created_on = created_on
        self.last_changed_by = last_changed_by
        self.last_changed_on = last_changed_on
        self.name = name
        self.record_id = record_id
        self.timeline_id = timeline_id
        self.type = type


class TaskHubOidcToken(Model):
    """
    :param oidc_token:
    :type oidc_token: str
    """

    _attribute_map = {
        'oidc_token': {'key': 'oidcToken', 'type': 'str'}
    }

    def __init__(self, oidc_token=None):
        super(TaskHubOidcToken, self).__init__()
        self.oidc_token = oidc_token


class TaskLogReference(Model):
    """
    A reference to a task log. This class contains information about the output printed to the timeline record's logs console during pipeline run.

    :param id: The ID of the task log.
    :type id: int
    :param location: The REST URL of the task log.
    :type location: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'location': {'key': 'location', 'type': 'str'}
    }

    def __init__(self, id=None, location=None):
        super(TaskLogReference, self).__init__()
        self.id = id
        self.location = location


class TaskOrchestrationItem(Model):
    """
    :param item_type:
    :type item_type: object
    """

    _attribute_map = {
        'item_type': {'key': 'itemType', 'type': 'object'}
    }

    def __init__(self, item_type=None):
        super(TaskOrchestrationItem, self).__init__()
        self.item_type = item_type


class TaskOrchestrationOwner(Model):
    """
    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v7_1.task.models.ReferenceLinks>`
    :param id:
    :type id: int
    :param name:
    :type name: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, _links=None, id=None, name=None):
        super(TaskOrchestrationOwner, self).__init__()
        self._links = _links
        self.id = id
        self.name = name


class TaskOrchestrationPlanGroupsQueueMetrics(Model):
    """
    :param count:
    :type count: int
    :param status:
    :type status: object
    """

    _attribute_map = {
        'count': {'key': 'count', 'type': 'int'},
        'status': {'key': 'status', 'type': 'object'}
    }

    def __init__(self, count=None, status=None):
        super(TaskOrchestrationPlanGroupsQueueMetrics, self).__init__()
        self.count = count
        self.status = status


class TaskOrchestrationPlanReference(Model):
    """
    :param artifact_location:
    :type artifact_location: str
    :param artifact_uri:
    :type artifact_uri: str
    :param definition:
    :type definition: :class:`TaskOrchestrationOwner <azure.devops.v7_1.task.models.TaskOrchestrationOwner>`
    :param owner:
    :type owner: :class:`TaskOrchestrationOwner <azure.devops.v7_1.task.models.TaskOrchestrationOwner>`
    :param plan_group:
    :type plan_group: str
    :param plan_id:
    :type plan_id: str
    :param plan_type:
    :type plan_type: str
    :param scope_identifier:
    :type scope_identifier: str
    :param version:
    :type version: int
    """

    _attribute_map = {
        'artifact_location': {'key': 'artifactLocation', 'type': 'str'},
        'artifact_uri': {'key': 'artifactUri', 'type': 'str'},
        'definition': {'key': 'definition', 'type': 'TaskOrchestrationOwner'},
        'owner': {'key': 'owner', 'type': 'TaskOrchestrationOwner'},
        'plan_group': {'key': 'planGroup', 'type': 'str'},
        'plan_id': {'key': 'planId', 'type': 'str'},
        'plan_type': {'key': 'planType', 'type': 'str'},
        'scope_identifier': {'key': 'scopeIdentifier', 'type': 'str'},
        'version': {'key': 'version', 'type': 'int'}
    }

    def __init__(self, artifact_location=None, artifact_uri=None, definition=None, owner=None, plan_group=None, plan_id=None, plan_type=None, scope_identifier=None, version=None):
        super(TaskOrchestrationPlanReference, self).__init__()
        self.artifact_location = artifact_location
        self.artifact_uri = artifact_uri
        self.definition = definition
        self.owner = owner
        self.plan_group = plan_group
        self.plan_id = plan_id
        self.plan_type = plan_type
        self.scope_identifier = scope_identifier
        self.version = version


class TaskOrchestrationQueuedPlan(Model):
    """
    :param assign_time:
    :type assign_time: datetime
    :param definition:
    :type definition: :class:`TaskOrchestrationOwner <azure.devops.v7_1.task.models.TaskOrchestrationOwner>`
    :param owner:
    :type owner: :class:`TaskOrchestrationOwner <azure.devops.v7_1.task.models.TaskOrchestrationOwner>`
    :param plan_group:
    :type plan_group: str
    :param plan_id:
    :type plan_id: str
    :param pool_id:
    :type pool_id: int
    :param queue_position:
    :type queue_position: int
    :param queue_time:
    :type queue_time: datetime
    :param scope_identifier:
    :type scope_identifier: str
    """

    _attribute_map = {
        'assign_time': {'key': 'assignTime', 'type': 'iso-8601'},
        'definition': {'key': 'definition', 'type': 'TaskOrchestrationOwner'},
        'owner': {'key': 'owner', 'type': 'TaskOrchestrationOwner'},
        'plan_group': {'key': 'planGroup', 'type': 'str'},
        'plan_id': {'key': 'planId', 'type': 'str'},
        'pool_id': {'key': 'poolId', 'type': 'int'},
        'queue_position': {'key': 'queuePosition', 'type': 'int'},
        'queue_time': {'key': 'queueTime', 'type': 'iso-8601'},
        'scope_identifier': {'key': 'scopeIdentifier', 'type': 'str'}
    }

    def __init__(self, assign_time=None, definition=None, owner=None, plan_group=None, plan_id=None, pool_id=None, queue_position=None, queue_time=None, scope_identifier=None):
        super(TaskOrchestrationQueuedPlan, self).__init__()
        self.assign_time = assign_time
        self.definition = definition
        self.owner = owner
        self.plan_group = plan_group
        self.plan_id = plan_id
        self.pool_id = pool_id
        self.queue_position = queue_position
        self.queue_time = queue_time
        self.scope_identifier = scope_identifier


class TaskOrchestrationQueuedPlanGroup(Model):
    """
    :param definition:
    :type definition: :class:`TaskOrchestrationOwner <azure.devops.v7_1.task.models.TaskOrchestrationOwner>`
    :param owner:
    :type owner: :class:`TaskOrchestrationOwner <azure.devops.v7_1.task.models.TaskOrchestrationOwner>`
    :param plan_group:
    :type plan_group: str
    :param plans:
    :type plans: list of :class:`TaskOrchestrationQueuedPlan <azure.devops.v7_1.task.models.TaskOrchestrationQueuedPlan>`
    :param project:
    :type project: :class:`ProjectReference <azure.devops.v7_1.task.models.ProjectReference>`
    :param queue_position:
    :type queue_position: int
    """

    _attribute_map = {
        'definition': {'key': 'definition', 'type': 'TaskOrchestrationOwner'},
        'owner': {'key': 'owner', 'type': 'TaskOrchestrationOwner'},
        'plan_group': {'key': 'planGroup', 'type': 'str'},
        'plans': {'key': 'plans', 'type': '[TaskOrchestrationQueuedPlan]'},
        'project': {'key': 'project', 'type': 'ProjectReference'},
        'queue_position': {'key': 'queuePosition', 'type': 'int'}
    }

    def __init__(self, definition=None, owner=None, plan_group=None, plans=None, project=None, queue_position=None):
        super(TaskOrchestrationQueuedPlanGroup, self).__init__()
        self.definition = definition
        self.owner = owner
        self.plan_group = plan_group
        self.plans = plans
        self.project = project
        self.queue_position = queue_position


class TaskReference(Model):
    """
    A reference to a task.

    :param id: The ID of the task definition. Corresponds to the id value of task.json file. <br />Example: CmdLineV2 { "id": "D9BAFED4-0B18-4F58-968D-86655B4D2CE9" }
    :type id: str
    :param inputs: A dictionary of inputs specific to a task definition. Corresponds to inputs value of task.json file.
    :type inputs: dict
    :param name: The name of the task definition. Corresponds to the name value of task.json file. <br />Example: CmdLineV2 { "name": "CmdLine" }
    :type name: str
    :param version: The version of the task definition. Corresponds to the version value of task.json file. <br />Example: CmdLineV2 { "version": { "Major": 2, "Minor": 212, "Patch": 0 } }
    :type version: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'inputs': {'key': 'inputs', 'type': '{str}'},
        'name': {'key': 'name', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, id=None, inputs=None, name=None, version=None):
        super(TaskReference, self).__init__()
        self.id = id
        self.inputs = inputs
        self.name = name
        self.version = version


class TimelineAttempt(Model):
    """
    An attempt to update a TimelineRecord.

    :param attempt: The attempt of the record.
    :type attempt: int
    :param identifier: The unique identifier for the record.
    :type identifier: str
    :param record_id: The record identifier located within the specified timeline.
    :type record_id: str
    :param timeline_id: The timeline identifier which owns the record representing this attempt.
    :type timeline_id: str
    """

    _attribute_map = {
        'attempt': {'key': 'attempt', 'type': 'int'},
        'identifier': {'key': 'identifier', 'type': 'str'},
        'record_id': {'key': 'recordId', 'type': 'str'},
        'timeline_id': {'key': 'timelineId', 'type': 'str'}
    }

    def __init__(self, attempt=None, identifier=None, record_id=None, timeline_id=None):
        super(TimelineAttempt, self).__init__()
        self.attempt = attempt
        self.identifier = identifier
        self.record_id = record_id
        self.timeline_id = timeline_id


class TimelineRecord(Model):
    """
    Detailed information about the execution of different operations during pipeline run.

    :param agent_specification: The specification of an agent running a pipeline job, in binary format. Applicable when record is of type Job. <br />Example: { "VMImage" : "windows-2019" }
    :type agent_specification: :class:`object <azure.devops.v7_1.task.models.object>`
    :param attempt: The number of record attempts.
    :type attempt: int
    :param current_operation: A string that indicates the current operation.
    :type current_operation: str
    :param details: A reference to a sub-timeline.
    :type details: :class:`TimelineReference <azure.devops.v7_1.task.models.TimelineReference>`
    :param error_count: The number of errors produced by this operation.
    :type error_count: int
    :param finish_time: The finish time of the record.
    :type finish_time: datetime
    :param change_id: The ID connecting all records updated at the same time. This value is taken from timeline's ChangeId.
    :type change_id: int
    :param id: The ID of the record.
    :type id: str
    :param identifier: String identifier that is consistent across attempts.
    :type identifier: str
    :param issues: The list of issues produced by this operation.
    :type issues: list of :class:`Issue <azure.devops.v7_1.task.models.Issue>`
    :param last_modified: The time the record was last modified.
    :type last_modified: datetime
    :param location: The REST URL of the record.
    :type location: str
    :param log: A reference to the log produced by this operation.
    :type log: :class:`TaskLogReference <azure.devops.v7_1.task.models.TaskLogReference>`
    :param name: The name of the record.
    :type name: str
    :param order: An ordinal value relative to other records within the timeline.
    :type order: int
    :param parent_id: The ID of the record's parent. <br />Example: Stage is a parent of a Phase, Phase is a parent of a Job, Job is a parent of a Task.
    :type parent_id: str
    :param percent_complete: The percentage of record completion.
    :type percent_complete: int
    :param previous_attempts: The previous record attempts.
    :type previous_attempts: list of :class:`TimelineAttempt <azure.devops.v7_1.task.models.TimelineAttempt>`
    :param queue_id: The ID of the queue which connects projects to agent pools on which the operation ran on. Applicable when record is of type Job.
    :type queue_id: int
    :param ref_name: Name of the referenced record.
    :type ref_name: str
    :param result: The result of the record.
    :type result: object
    :param result_code: Evaluation of predefined conditions upon completion of record's operation. <br />Example: Evaluating `succeeded()`, Result = True <br />Example: Evaluating `and(succeeded(), eq(variables['system.debug'], False))`, Result = False
    :type result_code: str
    :param start_time: The start time of the record.
    :type start_time: datetime
    :param state: The state of the record.
    :type state: object
    :param task: A reference to the task. Applicable when record is of type Task.
    :type task: :class:`TaskReference <azure.devops.v7_1.task.models.TaskReference>`
    :param type: The type of operation being tracked by the record. <br />Example: Stage, Phase, Job, Task...
    :type type: str
    :param variables: The variables of the record.
    :type variables: dict
    :param warning_count: The number of warnings produced by this operation.
    :type warning_count: int
    :param worker_name: The name of the agent running the operation. Applicable when record is of type Job.
    :type worker_name: str
    """

    _attribute_map = {
        'agent_specification': {'key': 'agentSpecification', 'type': 'object'},
        'attempt': {'key': 'attempt', 'type': 'int'},
        'current_operation': {'key': 'currentOperation', 'type': 'str'},
        'details': {'key': 'details', 'type': 'TimelineReference'},
        'error_count': {'key': 'errorCount', 'type': 'int'},
        'finish_time': {'key': 'finishTime', 'type': 'iso-8601'},
        'change_id': {'key': 'changeId', 'type': 'int'},
        'id': {'key': 'id', 'type': 'str'},
        'identifier': {'key': 'identifier', 'type': 'str'},
        'issues': {'key': 'issues', 'type': '[Issue]'},
        'last_modified': {'key': 'lastModified', 'type': 'iso-8601'},
        'location': {'key': 'location', 'type': 'str'},
        'log': {'key': 'log', 'type': 'TaskLogReference'},
        'name': {'key': 'name', 'type': 'str'},
        'order': {'key': 'order', 'type': 'int'},
        'parent_id': {'key': 'parentId', 'type': 'str'},
        'percent_complete': {'key': 'percentComplete', 'type': 'int'},
        'previous_attempts': {'key': 'previousAttempts', 'type': '[TimelineAttempt]'},
        'queue_id': {'key': 'queueId', 'type': 'int'},
        'ref_name': {'key': 'refName', 'type': 'str'},
        'result': {'key': 'result', 'type': 'object'},
        'result_code': {'key': 'resultCode', 'type': 'str'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'state': {'key': 'state', 'type': 'object'},
        'task': {'key': 'task', 'type': 'TaskReference'},
        'type': {'key': 'type', 'type': 'str'},
        'variables': {'key': 'variables', 'type': '{VariableValue}'},
        'warning_count': {'key': 'warningCount', 'type': 'int'},
        'worker_name': {'key': 'workerName', 'type': 'str'}
    }

    def __init__(self, agent_specification=None, attempt=None, current_operation=None, details=None, error_count=None, finish_time=None, change_id=None, id=None, identifier=None, issues=None, last_modified=None, location=None, log=None, name=None, order=None, parent_id=None, percent_complete=None, previous_attempts=None, queue_id=None, ref_name=None, result=None, result_code=None, start_time=None, state=None, task=None, type=None, variables=None, warning_count=None, worker_name=None):
        super(TimelineRecord, self).__init__()
        self.agent_specification = agent_specification
        self.attempt = attempt
        self.current_operation = current_operation
        self.details = details
        self.error_count = error_count
        self.finish_time = finish_time
        self.change_id = change_id
        self.id = id
        self.identifier = identifier
        self.issues = issues
        self.last_modified = last_modified
        self.location = location
        self.log = log
        self.name = name
        self.order = order
        self.parent_id = parent_id
        self.percent_complete = percent_complete
        self.previous_attempts = previous_attempts
        self.queue_id = queue_id
        self.ref_name = ref_name
        self.result = result
        self.result_code = result_code
        self.start_time = start_time
        self.state = state
        self.task = task
        self.type = type
        self.variables = variables
        self.warning_count = warning_count
        self.worker_name = worker_name


class TimelineRecordFeedLinesWrapper(Model):
    """
    :param count:
    :type count: int
    :param end_line:
    :type end_line: long
    :param start_line:
    :type start_line: long
    :param step_id:
    :type step_id: str
    :param value:
    :type value: list of str
    """

    _attribute_map = {
        'count': {'key': 'count', 'type': 'int'},
        'end_line': {'key': 'endLine', 'type': 'long'},
        'start_line': {'key': 'startLine', 'type': 'long'},
        'step_id': {'key': 'stepId', 'type': 'str'},
        'value': {'key': 'value', 'type': '[str]'}
    }

    def __init__(self, count=None, end_line=None, start_line=None, step_id=None, value=None):
        super(TimelineRecordFeedLinesWrapper, self).__init__()
        self.count = count
        self.end_line = end_line
        self.start_line = start_line
        self.step_id = step_id
        self.value = value


class TimelineReference(Model):
    """
    A reference to a timeline.

    :param change_id: The change ID.
    :type change_id: int
    :param id: The ID of the timeline.
    :type id: str
    :param location: The REST URL of the timeline.
    :type location: str
    """

    _attribute_map = {
        'change_id': {'key': 'changeId', 'type': 'int'},
        'id': {'key': 'id', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'}
    }

    def __init__(self, change_id=None, id=None, location=None):
        super(TimelineReference, self).__init__()
        self.change_id = change_id
        self.id = id
        self.location = location


class VariableValue(Model):
    """
    A wrapper class for a generic variable.

    :param is_read_only: Indicates whether the variable can be changed during script's execution runtime.
    :type is_read_only: bool
    :param is_secret: Indicates whether the variable should be encrypted at rest.
    :type is_secret: bool
    :param value: The value of the variable.
    :type value: str
    """

    _attribute_map = {
        'is_read_only': {'key': 'isReadOnly', 'type': 'bool'},
        'is_secret': {'key': 'isSecret', 'type': 'bool'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, is_read_only=None, is_secret=None, value=None):
        super(VariableValue, self).__init__()
        self.is_read_only = is_read_only
        self.is_secret = is_secret
        self.value = value


class TaskLog(TaskLogReference):
    """
    A task log connected to a timeline record.

    :param id: The ID of the task log.
    :type id: int
    :param location: The REST URL of the task log.
    :type location: str
    :param created_on: The time of the task log creation.
    :type created_on: datetime
    :param index_location: The REST URL of the task log when indexed.
    :type index_location: str
    :param last_changed_on: The time of the last modification of the task log.
    :type last_changed_on: datetime
    :param line_count: The number of the task log lines.
    :type line_count: long
    :param path: The path of the task log.
    :type path: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'location': {'key': 'location', 'type': 'str'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'index_location': {'key': 'indexLocation', 'type': 'str'},
        'last_changed_on': {'key': 'lastChangedOn', 'type': 'iso-8601'},
        'line_count': {'key': 'lineCount', 'type': 'long'},
        'path': {'key': 'path', 'type': 'str'}
    }

    def __init__(self, id=None, location=None, created_on=None, index_location=None, last_changed_on=None, line_count=None, path=None):
        super(TaskLog, self).__init__(id=id, location=location)
        self.created_on = created_on
        self.index_location = index_location
        self.last_changed_on = last_changed_on
        self.line_count = line_count
        self.path = path


class TaskOrchestrationContainer(TaskOrchestrationItem):
    """
    :param item_type:
    :type item_type: object
    :param continue_on_error:
    :type continue_on_error: bool
    :param data:
    :type data: dict
    :param children:
    :type children: list of :class:`TaskOrchestrationItem <azure.devops.v7_1.task.models.TaskOrchestrationItem>`
    :param max_concurrency:
    :type max_concurrency: int
    :param parallel:
    :type parallel: bool
    :param rollback:
    :type rollback: :class:`TaskOrchestrationContainer <azure.devops.v7_1.task.models.TaskOrchestrationContainer>`
    """

    _attribute_map = {
        'item_type': {'key': 'itemType', 'type': 'object'},
        'continue_on_error': {'key': 'continueOnError', 'type': 'bool'},
        'data': {'key': 'data', 'type': '{str}'},
        'children': {'key': 'children', 'type': '[TaskOrchestrationItem]'},
        'max_concurrency': {'key': 'maxConcurrency', 'type': 'int'},
        'parallel': {'key': 'parallel', 'type': 'bool'},
        'rollback': {'key': 'rollback', 'type': 'TaskOrchestrationContainer'}
    }

    def __init__(self, item_type=None, continue_on_error=None, data=None, children=None, max_concurrency=None, parallel=None, rollback=None):
        super(TaskOrchestrationContainer, self).__init__(item_type=item_type)
        self.continue_on_error = continue_on_error
        self.data = data
        self.children = children
        self.max_concurrency = max_concurrency
        self.parallel = parallel
        self.rollback = rollback


class TaskOrchestrationPlan(TaskOrchestrationPlanReference):
    """
    :param artifact_location:
    :type artifact_location: str
    :param artifact_uri:
    :type artifact_uri: str
    :param definition:
    :type definition: :class:`TaskOrchestrationOwner <azure.devops.v7_1.task.models.TaskOrchestrationOwner>`
    :param owner:
    :type owner: :class:`TaskOrchestrationOwner <azure.devops.v7_1.task.models.TaskOrchestrationOwner>`
    :param plan_group:
    :type plan_group: str
    :param plan_id:
    :type plan_id: str
    :param plan_type:
    :type plan_type: str
    :param scope_identifier:
    :type scope_identifier: str
    :param version:
    :type version: int
    :param environment:
    :type environment: :class:`PlanEnvironment <azure.devops.v7_1.task.models.PlanEnvironment>`
    :param expanded_yaml:
    :type expanded_yaml: :class:`TaskLogReference <azure.devops.v7_1.task.models.TaskLogReference>`
    :param finish_time:
    :type finish_time: datetime
    :param implementation:
    :type implementation: :class:`TaskOrchestrationContainer <azure.devops.v7_1.task.models.TaskOrchestrationContainer>`
    :param initialization_log:
    :type initialization_log: :class:`TaskLogReference <azure.devops.v7_1.task.models.TaskLogReference>`
    :param requested_by_id:
    :type requested_by_id: str
    :param requested_for_id:
    :type requested_for_id: str
    :param result:
    :type result: object
    :param result_code:
    :type result_code: str
    :param start_time:
    :type start_time: datetime
    :param state:
    :type state: object
    :param timeline:
    :type timeline: :class:`TimelineReference <azure.devops.v7_1.task.models.TimelineReference>`
    """

    _attribute_map = {
        'artifact_location': {'key': 'artifactLocation', 'type': 'str'},
        'artifact_uri': {'key': 'artifactUri', 'type': 'str'},
        'definition': {'key': 'definition', 'type': 'TaskOrchestrationOwner'},
        'owner': {'key': 'owner', 'type': 'TaskOrchestrationOwner'},
        'plan_group': {'key': 'planGroup', 'type': 'str'},
        'plan_id': {'key': 'planId', 'type': 'str'},
        'plan_type': {'key': 'planType', 'type': 'str'},
        'scope_identifier': {'key': 'scopeIdentifier', 'type': 'str'},
        'version': {'key': 'version', 'type': 'int'},
        'environment': {'key': 'environment', 'type': 'PlanEnvironment'},
        'expanded_yaml': {'key': 'expandedYaml', 'type': 'TaskLogReference'},
        'finish_time': {'key': 'finishTime', 'type': 'iso-8601'},
        'implementation': {'key': 'implementation', 'type': 'TaskOrchestrationContainer'},
        'initialization_log': {'key': 'initializationLog', 'type': 'TaskLogReference'},
        'requested_by_id': {'key': 'requestedById', 'type': 'str'},
        'requested_for_id': {'key': 'requestedForId', 'type': 'str'},
        'result': {'key': 'result', 'type': 'object'},
        'result_code': {'key': 'resultCode', 'type': 'str'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'state': {'key': 'state', 'type': 'object'},
        'timeline': {'key': 'timeline', 'type': 'TimelineReference'}
    }

    def __init__(self, artifact_location=None, artifact_uri=None, definition=None, owner=None, plan_group=None, plan_id=None, plan_type=None, scope_identifier=None, version=None, environment=None, expanded_yaml=None, finish_time=None, implementation=None, initialization_log=None, requested_by_id=None, requested_for_id=None, result=None, result_code=None, start_time=None, state=None, timeline=None):
        super(TaskOrchestrationPlan, self).__init__(artifact_location=artifact_location, artifact_uri=artifact_uri, definition=definition, owner=owner, plan_group=plan_group, plan_id=plan_id, plan_type=plan_type, scope_identifier=scope_identifier, version=version)
        self.environment = environment
        self.expanded_yaml = expanded_yaml
        self.finish_time = finish_time
        self.implementation = implementation
        self.initialization_log = initialization_log
        self.requested_by_id = requested_by_id
        self.requested_for_id = requested_for_id
        self.result = result
        self.result_code = result_code
        self.start_time = start_time
        self.state = state
        self.timeline = timeline


class Timeline(TimelineReference):
    """
    :param change_id: The change ID.
    :type change_id: int
    :param id: The ID of the timeline.
    :type id: str
    :param location: The REST URL of the timeline.
    :type location: str
    :param last_changed_by:
    :type last_changed_by: str
    :param last_changed_on:
    :type last_changed_on: datetime
    :param records:
    :type records: list of :class:`TimelineRecord <azure.devops.v7_1.task.models.TimelineRecord>`
    """

    _attribute_map = {
        'change_id': {'key': 'changeId', 'type': 'int'},
        'id': {'key': 'id', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'last_changed_by': {'key': 'lastChangedBy', 'type': 'str'},
        'last_changed_on': {'key': 'lastChangedOn', 'type': 'iso-8601'},
        'records': {'key': 'records', 'type': '[TimelineRecord]'}
    }

    def __init__(self, change_id=None, id=None, location=None, last_changed_by=None, last_changed_on=None, records=None):
        super(Timeline, self).__init__(change_id=change_id, id=id, location=location)
        self.last_changed_by = last_changed_by
        self.last_changed_on = last_changed_on
        self.records = records


__all__ = [
    'Issue',
    'JobEvent',
    'JobOption',
    'MaskHint',
    'PlanEnvironment',
    'ProjectReference',
    'ReferenceLinks',
    'TaskAgentJob',
    'TaskAgentJobStep',
    'TaskAgentJobTask',
    'TaskAgentJobVariable',
    'TaskAttachment',
    'TaskHubOidcToken',
    'TaskLogReference',
    'TaskOrchestrationItem',
    'TaskOrchestrationOwner',
    'TaskOrchestrationPlanGroupsQueueMetrics',
    'TaskOrchestrationPlanReference',
    'TaskOrchestrationQueuedPlan',
    'TaskOrchestrationQueuedPlanGroup',
    'TaskReference',
    'TimelineAttempt',
    'TimelineRecord',
    'TimelineRecordFeedLinesWrapper',
    'TimelineReference',
    'VariableValue',
    'TaskLog',
    'TaskOrchestrationContainer',
    'TaskOrchestrationPlan',
    'Timeline',
]
