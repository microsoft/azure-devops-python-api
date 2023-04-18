# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class ElasticNode(Model):
    """
    Data and settings for an elastic node

    :param agent_id: Distributed Task's Agent Id
    :type agent_id: int
    :param agent_state: Summary of the state of the agent
    :type agent_state: object
    :param compute_id: Compute Id.  VMSS's InstanceId
    :type compute_id: str
    :param compute_state: State of the compute host
    :type compute_state: object
    :param desired_state: Users can force state changes to specific states (ToReimage, ToDelete, Save)
    :type desired_state: object
    :param id: Unique identifier since the agent and/or VM may be null
    :type id: int
    :param name: Computer name. Used to match a scaleset VM with an agent
    :type name: str
    :param pool_id: Pool Id that this node belongs to
    :type pool_id: int
    :param request_id: Last job RequestId assigned to this agent
    :type request_id: long
    :param state: State of the ElasticNode
    :type state: object
    :param state_changed_on: Last state change. Only updated by SQL.
    :type state_changed_on: datetime
    """

    _attribute_map = {
        'agent_id': {'key': 'agentId', 'type': 'int'},
        'agent_state': {'key': 'agentState', 'type': 'object'},
        'compute_id': {'key': 'computeId', 'type': 'str'},
        'compute_state': {'key': 'computeState', 'type': 'object'},
        'desired_state': {'key': 'desiredState', 'type': 'object'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'pool_id': {'key': 'poolId', 'type': 'int'},
        'request_id': {'key': 'requestId', 'type': 'long'},
        'state': {'key': 'state', 'type': 'object'},
        'state_changed_on': {'key': 'stateChangedOn', 'type': 'iso-8601'}
    }

    def __init__(self, agent_id=None, agent_state=None, compute_id=None, compute_state=None, desired_state=None, id=None, name=None, pool_id=None, request_id=None, state=None, state_changed_on=None):
        super(ElasticNode, self).__init__()
        self.agent_id = agent_id
        self.agent_state = agent_state
        self.compute_id = compute_id
        self.compute_state = compute_state
        self.desired_state = desired_state
        self.id = id
        self.name = name
        self.pool_id = pool_id
        self.request_id = request_id
        self.state = state
        self.state_changed_on = state_changed_on


class ElasticNodeSettings(Model):
    """
    Class used for updating an elastic node where only certain members are populated

    :param state: State of the ElasticNode
    :type state: object
    """

    _attribute_map = {
        'state': {'key': 'state', 'type': 'object'}
    }

    def __init__(self, state=None):
        super(ElasticNodeSettings, self).__init__()
        self.state = state


class ElasticPool(Model):
    """
    Data and settings for an elastic pool

    :param agent_interactive_uI: Set whether agents should be configured to run with interactive UI
    :type agent_interactive_uI: bool
    :param azure_id: Azure string representing to location of the resource
    :type azure_id: str
    :param desired_idle: Number of agents to have ready waiting for jobs
    :type desired_idle: int
    :param desired_size: The desired size of the pool
    :type desired_size: int
    :param max_capacity: Maximum number of nodes that will exist in the elastic pool
    :type max_capacity: int
    :param max_saved_node_count: Keep nodes in the pool on failure for investigation
    :type max_saved_node_count: int
    :param offline_since: Timestamp the pool was first detected to be offline
    :type offline_since: datetime
    :param os_type: Operating system type of the nodes in the pool
    :type os_type: object
    :param pool_id: Id of the associated TaskAgentPool
    :type pool_id: int
    :param recycle_after_each_use: Discard node after each job completes
    :type recycle_after_each_use: bool
    :param service_endpoint_id: Id of the Service Endpoint used to connect to Azure
    :type service_endpoint_id: str
    :param service_endpoint_scope: Scope the Service Endpoint belongs to
    :type service_endpoint_scope: str
    :param sizing_attempts: The number of sizing attempts executed while trying to achieve a desired size
    :type sizing_attempts: int
    :param state: State of the pool
    :type state: object
    :param time_to_live_minutes: The minimum time in minutes to keep idle agents alive
    :type time_to_live_minutes: int
    """

    _attribute_map = {
        'agent_interactive_uI': {'key': 'agentInteractiveUI', 'type': 'bool'},
        'azure_id': {'key': 'azureId', 'type': 'str'},
        'desired_idle': {'key': 'desiredIdle', 'type': 'int'},
        'desired_size': {'key': 'desiredSize', 'type': 'int'},
        'max_capacity': {'key': 'maxCapacity', 'type': 'int'},
        'max_saved_node_count': {'key': 'maxSavedNodeCount', 'type': 'int'},
        'offline_since': {'key': 'offlineSince', 'type': 'iso-8601'},
        'os_type': {'key': 'osType', 'type': 'object'},
        'pool_id': {'key': 'poolId', 'type': 'int'},
        'recycle_after_each_use': {'key': 'recycleAfterEachUse', 'type': 'bool'},
        'service_endpoint_id': {'key': 'serviceEndpointId', 'type': 'str'},
        'service_endpoint_scope': {'key': 'serviceEndpointScope', 'type': 'str'},
        'sizing_attempts': {'key': 'sizingAttempts', 'type': 'int'},
        'state': {'key': 'state', 'type': 'object'},
        'time_to_live_minutes': {'key': 'timeToLiveMinutes', 'type': 'int'}
    }

    def __init__(self, agent_interactive_uI=None, azure_id=None, desired_idle=None, desired_size=None, max_capacity=None, max_saved_node_count=None, offline_since=None, os_type=None, pool_id=None, recycle_after_each_use=None, service_endpoint_id=None, service_endpoint_scope=None, sizing_attempts=None, state=None, time_to_live_minutes=None):
        super(ElasticPool, self).__init__()
        self.agent_interactive_uI = agent_interactive_uI
        self.azure_id = azure_id
        self.desired_idle = desired_idle
        self.desired_size = desired_size
        self.max_capacity = max_capacity
        self.max_saved_node_count = max_saved_node_count
        self.offline_since = offline_since
        self.os_type = os_type
        self.pool_id = pool_id
        self.recycle_after_each_use = recycle_after_each_use
        self.service_endpoint_id = service_endpoint_id
        self.service_endpoint_scope = service_endpoint_scope
        self.sizing_attempts = sizing_attempts
        self.state = state
        self.time_to_live_minutes = time_to_live_minutes


class ElasticPoolCreationResult(Model):
    """
    Returned result from creating a new elastic pool

    :param agent_pool: Created agent pool
    :type agent_pool: :class:`TaskAgentPool <azure.devops.v7_0.elastic.models.TaskAgentPool>`
    :param agent_queue: Created agent queue
    :type agent_queue: :class:`TaskAgentQueue <azure.devops.v7_0.elastic.models.TaskAgentQueue>`
    :param elastic_pool: Created elastic pool
    :type elastic_pool: :class:`ElasticPool <azure.devops.v7_0.elastic.models.ElasticPool>`
    """

    _attribute_map = {
        'agent_pool': {'key': 'agentPool', 'type': 'TaskAgentPool'},
        'agent_queue': {'key': 'agentQueue', 'type': 'TaskAgentQueue'},
        'elastic_pool': {'key': 'elasticPool', 'type': 'ElasticPool'}
    }

    def __init__(self, agent_pool=None, agent_queue=None, elastic_pool=None):
        super(ElasticPoolCreationResult, self).__init__()
        self.agent_pool = agent_pool
        self.agent_queue = agent_queue
        self.elastic_pool = elastic_pool


class ElasticPoolLog(Model):
    """
    Log data for an Elastic Pool

    :param id: Log Id
    :type id: long
    :param level: E.g. error, warning, info
    :type level: object
    :param message: Log contents
    :type message: str
    :param operation: Operation that triggered the message being logged
    :type operation: object
    :param pool_id: Id of the associated TaskAgentPool
    :type pool_id: int
    :param timestamp: Datetime that the log occurred
    :type timestamp: datetime
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'long'},
        'level': {'key': 'level', 'type': 'object'},
        'message': {'key': 'message', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'object'},
        'pool_id': {'key': 'poolId', 'type': 'int'},
        'timestamp': {'key': 'timestamp', 'type': 'iso-8601'}
    }

    def __init__(self, id=None, level=None, message=None, operation=None, pool_id=None, timestamp=None):
        super(ElasticPoolLog, self).__init__()
        self.id = id
        self.level = level
        self.message = message
        self.operation = operation
        self.pool_id = pool_id
        self.timestamp = timestamp


class ElasticPoolSettings(Model):
    """
    Class used for updating an elastic pool where only certain members are populated

    :param agent_interactive_uI: Set whether agents should be configured to run with interactive UI
    :type agent_interactive_uI: bool
    :param azure_id: Azure string representing to location of the resource
    :type azure_id: str
    :param desired_idle: Number of machines to have ready waiting for jobs
    :type desired_idle: int
    :param max_capacity: Maximum number of machines that will exist in the elastic pool
    :type max_capacity: int
    :param max_saved_node_count: Keep machines in the pool on failure for investigation
    :type max_saved_node_count: int
    :param os_type: Operating system type of the machines in the pool
    :type os_type: object
    :param recycle_after_each_use: Discard machines after each job completes
    :type recycle_after_each_use: bool
    :param service_endpoint_id: Id of the Service Endpoint used to connect to Azure
    :type service_endpoint_id: str
    :param service_endpoint_scope: Scope the Service Endpoint belongs to
    :type service_endpoint_scope: str
    :param time_to_live_minutes: The minimum time in minutes to keep idle agents alive
    :type time_to_live_minutes: int
    """

    _attribute_map = {
        'agent_interactive_uI': {'key': 'agentInteractiveUI', 'type': 'bool'},
        'azure_id': {'key': 'azureId', 'type': 'str'},
        'desired_idle': {'key': 'desiredIdle', 'type': 'int'},
        'max_capacity': {'key': 'maxCapacity', 'type': 'int'},
        'max_saved_node_count': {'key': 'maxSavedNodeCount', 'type': 'int'},
        'os_type': {'key': 'osType', 'type': 'object'},
        'recycle_after_each_use': {'key': 'recycleAfterEachUse', 'type': 'bool'},
        'service_endpoint_id': {'key': 'serviceEndpointId', 'type': 'str'},
        'service_endpoint_scope': {'key': 'serviceEndpointScope', 'type': 'str'},
        'time_to_live_minutes': {'key': 'timeToLiveMinutes', 'type': 'int'}
    }

    def __init__(self, agent_interactive_uI=None, azure_id=None, desired_idle=None, max_capacity=None, max_saved_node_count=None, os_type=None, recycle_after_each_use=None, service_endpoint_id=None, service_endpoint_scope=None, time_to_live_minutes=None):
        super(ElasticPoolSettings, self).__init__()
        self.agent_interactive_uI = agent_interactive_uI
        self.azure_id = azure_id
        self.desired_idle = desired_idle
        self.max_capacity = max_capacity
        self.max_saved_node_count = max_saved_node_count
        self.os_type = os_type
        self.recycle_after_each_use = recycle_after_each_use
        self.service_endpoint_id = service_endpoint_id
        self.service_endpoint_scope = service_endpoint_scope
        self.time_to_live_minutes = time_to_live_minutes


class GraphSubjectBase(Model):
    """
    :param _links: This field contains zero or more interesting links about the graph subject. These links may be invoked to obtain additional relationships or more detailed information about this graph subject.
    :type _links: :class:`ReferenceLinks <azure.devops.v7_0.microsoft._visual_studio._services._web_api.models.ReferenceLinks>`
    :param descriptor: The descriptor is the primary way to reference the graph subject while the system is running. This field will uniquely identify the same graph subject across both Accounts and Organizations.
    :type descriptor: str
    :param display_name: This is the non-unique display name of the graph subject. To change this field, you must alter its value in the source provider.
    :type display_name: str
    :param url: This url is the full route to the source resource of this graph subject.
    :type url: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'descriptor': {'key': 'descriptor', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, descriptor=None, display_name=None, url=None):
        super(GraphSubjectBase, self).__init__()
        self._links = _links
        self.descriptor = descriptor
        self.display_name = display_name
        self.url = url


class IdentityRef(GraphSubjectBase):
    """
    :param _links: This field contains zero or more interesting links about the graph subject. These links may be invoked to obtain additional relationships or more detailed information about this graph subject.
    :type _links: :class:`ReferenceLinks <azure.devops.v7_0.microsoft._visual_studio._services._web_api.models.ReferenceLinks>`
    :param descriptor: The descriptor is the primary way to reference the graph subject while the system is running. This field will uniquely identify the same graph subject across both Accounts and Organizations.
    :type descriptor: str
    :param display_name: This is the non-unique display name of the graph subject. To change this field, you must alter its value in the source provider.
    :type display_name: str
    :param url: This url is the full route to the source resource of this graph subject.
    :type url: str
    :param directory_alias: Deprecated - Can be retrieved by querying the Graph user referenced in the "self" entry of the IdentityRef "_links" dictionary
    :type directory_alias: str
    :param id:
    :type id: str
    :param image_url: Deprecated - Available in the "avatar" entry of the IdentityRef "_links" dictionary
    :type image_url: str
    :param inactive: Deprecated - Can be retrieved by querying the Graph membership state referenced in the "membershipState" entry of the GraphUser "_links" dictionary
    :type inactive: bool
    :param is_aad_identity: Deprecated - Can be inferred from the subject type of the descriptor (Descriptor.IsAadUserType/Descriptor.IsAadGroupType)
    :type is_aad_identity: bool
    :param is_container: Deprecated - Can be inferred from the subject type of the descriptor (Descriptor.IsGroupType)
    :type is_container: bool
    :param is_deleted_in_origin:
    :type is_deleted_in_origin: bool
    :param profile_url: Deprecated - not in use in most preexisting implementations of ToIdentityRef
    :type profile_url: str
    :param unique_name: Deprecated - use Domain+PrincipalName instead
    :type unique_name: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'descriptor': {'key': 'descriptor', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'directory_alias': {'key': 'directoryAlias', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'image_url': {'key': 'imageUrl', 'type': 'str'},
        'inactive': {'key': 'inactive', 'type': 'bool'},
        'is_aad_identity': {'key': 'isAadIdentity', 'type': 'bool'},
        'is_container': {'key': 'isContainer', 'type': 'bool'},
        'is_deleted_in_origin': {'key': 'isDeletedInOrigin', 'type': 'bool'},
        'profile_url': {'key': 'profileUrl', 'type': 'str'},
        'unique_name': {'key': 'uniqueName', 'type': 'str'}
    }

    def __init__(self, _links=None, descriptor=None, display_name=None, url=None, directory_alias=None, id=None, image_url=None, inactive=None, is_aad_identity=None, is_container=None, is_deleted_in_origin=None, profile_url=None, unique_name=None):
        super(IdentityRef, self).__init__(_links=_links, descriptor=descriptor, display_name=display_name, url=url)
        self.directory_alias = directory_alias
        self.id = id
        self.image_url = image_url
        self.inactive = inactive
        self.is_aad_identity = is_aad_identity
        self.is_container = is_container
        self.is_deleted_in_origin = is_deleted_in_origin
        self.profile_url = profile_url
        self.unique_name = unique_name


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


class TaskAgentPoolReference(Model):
    """
    :param id:
    :type id: int
    :param is_hosted: Gets or sets a value indicating whether or not this pool is managed by the service.
    :type is_hosted: bool
    :param is_legacy: Determines whether the pool is legacy.
    :type is_legacy: bool
    :param name:
    :type name: str
    :param options: Additional pool settings and details
    :type options: object
    :param pool_type: Gets or sets the type of the pool
    :type pool_type: object
    :param scope:
    :type scope: str
    :param size: Gets the current size of the pool.
    :type size: int
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'is_hosted': {'key': 'isHosted', 'type': 'bool'},
        'is_legacy': {'key': 'isLegacy', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'options': {'key': 'options', 'type': 'object'},
        'pool_type': {'key': 'poolType', 'type': 'object'},
        'scope': {'key': 'scope', 'type': 'str'},
        'size': {'key': 'size', 'type': 'int'}
    }

    def __init__(self, id=None, is_hosted=None, is_legacy=None, name=None, options=None, pool_type=None, scope=None, size=None):
        super(TaskAgentPoolReference, self).__init__()
        self.id = id
        self.is_hosted = is_hosted
        self.is_legacy = is_legacy
        self.name = name
        self.options = options
        self.pool_type = pool_type
        self.scope = scope
        self.size = size


class TaskAgentQueue(Model):
    """
    An agent queue.

    :param id: ID of the queue
    :type id: int
    :param name: Name of the queue
    :type name: str
    :param pool: Pool reference for this queue
    :type pool: :class:`TaskAgentPoolReference <azure.devops.v7_0.elastic.models.TaskAgentPoolReference>`
    :param project_id: Project ID
    :type project_id: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'pool': {'key': 'pool', 'type': 'TaskAgentPoolReference'},
        'project_id': {'key': 'projectId', 'type': 'str'}
    }

    def __init__(self, id=None, name=None, pool=None, project_id=None):
        super(TaskAgentQueue, self).__init__()
        self.id = id
        self.name = name
        self.pool = pool
        self.project_id = project_id


class TaskAgentPool(TaskAgentPoolReference):
    """
    An organization-level grouping of agents.

    :param id:
    :type id: int
    :param is_hosted: Gets or sets a value indicating whether or not this pool is managed by the service.
    :type is_hosted: bool
    :param is_legacy: Determines whether the pool is legacy.
    :type is_legacy: bool
    :param name:
    :type name: str
    :param options: Additional pool settings and details
    :type options: object
    :param pool_type: Gets or sets the type of the pool
    :type pool_type: object
    :param scope:
    :type scope: str
    :param size: Gets the current size of the pool.
    :type size: int
    :param agent_cloud_id: The ID of the associated agent cloud.
    :type agent_cloud_id: int
    :param auto_provision: Whether or not a queue should be automatically provisioned for each project collection.
    :type auto_provision: bool
    :param auto_size: Whether or not the pool should autosize itself based on the Agent Cloud Provider settings.
    :type auto_size: bool
    :param auto_update: Whether or not agents in this pool are allowed to automatically update
    :type auto_update: bool
    :param created_by: Creator of the pool. The creator of the pool is automatically added into the administrators group for the pool on creation.
    :type created_by: :class:`IdentityRef <azure.devops.v7_0.elastic.models.IdentityRef>`
    :param created_on: The date/time of the pool creation.
    :type created_on: datetime
    :param owner: Owner or administrator of the pool.
    :type owner: :class:`IdentityRef <azure.devops.v7_0.elastic.models.IdentityRef>`
    :param properties:
    :type properties: :class:`object <azure.devops.v7_0.elastic.models.object>`
    :param target_size: Target parallelism.
    :type target_size: int
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'is_hosted': {'key': 'isHosted', 'type': 'bool'},
        'is_legacy': {'key': 'isLegacy', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'options': {'key': 'options', 'type': 'object'},
        'pool_type': {'key': 'poolType', 'type': 'object'},
        'scope': {'key': 'scope', 'type': 'str'},
        'size': {'key': 'size', 'type': 'int'},
        'agent_cloud_id': {'key': 'agentCloudId', 'type': 'int'},
        'auto_provision': {'key': 'autoProvision', 'type': 'bool'},
        'auto_size': {'key': 'autoSize', 'type': 'bool'},
        'auto_update': {'key': 'autoUpdate', 'type': 'bool'},
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'owner': {'key': 'owner', 'type': 'IdentityRef'},
        'properties': {'key': 'properties', 'type': 'object'},
        'target_size': {'key': 'targetSize', 'type': 'int'}
    }

    def __init__(self, id=None, is_hosted=None, is_legacy=None, name=None, options=None, pool_type=None, scope=None, size=None, agent_cloud_id=None, auto_provision=None, auto_size=None, auto_update=None, created_by=None, created_on=None, owner=None, properties=None, target_size=None):
        super(TaskAgentPool, self).__init__(id=id, is_hosted=is_hosted, is_legacy=is_legacy, name=name, options=options, pool_type=pool_type, scope=scope, size=size)
        self.agent_cloud_id = agent_cloud_id
        self.auto_provision = auto_provision
        self.auto_size = auto_size
        self.auto_update = auto_update
        self.created_by = created_by
        self.created_on = created_on
        self.owner = owner
        self.properties = properties
        self.target_size = target_size


__all__ = [
    'ElasticNode',
    'ElasticNodeSettings',
    'ElasticPool',
    'ElasticPoolCreationResult',
    'ElasticPoolLog',
    'ElasticPoolSettings',
    'GraphSubjectBase',
    'IdentityRef',
    'ReferenceLinks',
    'TaskAgentPoolReference',
    'TaskAgentQueue',
    'TaskAgentPool',
]
