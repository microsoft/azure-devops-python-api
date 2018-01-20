# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...vss_client import VssClient
from . import models


class TaskAgentClient(VssClient):
    """TaskAgent
    :param str base_url: Service URL
    :param Authentication creds: Authenticated credentials.
    """

    def __init__(self, base_url=None, creds=None):
        super(TaskAgentClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = 'a85b8835-c1a1-4aac-ae97-1c3d0ba72dbd'

    def add_agent(self, agent, pool_id):
        """AddAgent.
        [Preview API]
        :param :class:`<TaskAgent> <task-agent.v4_1.models.TaskAgent>` agent:
        :param int pool_id:
        :rtype: :class:`<TaskAgent> <task-agent.v4_1.models.TaskAgent>`
        """
        route_values = {}
        if pool_id is not None:
            route_values['poolId'] = self._serialize.url('pool_id', pool_id, 'int')
        content = self._serialize.body(agent, 'TaskAgent')
        response = self._send(http_method='POST',
                              location_id='e298ef32-5878-4cab-993c-043836571f42',
                              version='4.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TaskAgent', response)

    def delete_agent(self, pool_id, agent_id):
        """DeleteAgent.
        [Preview API]
        :param int pool_id:
        :param int agent_id:
        """
        route_values = {}
        if pool_id is not None:
            route_values['poolId'] = self._serialize.url('pool_id', pool_id, 'int')
        if agent_id is not None:
            route_values['agentId'] = self._serialize.url('agent_id', agent_id, 'int')
        self._send(http_method='DELETE',
                   location_id='e298ef32-5878-4cab-993c-043836571f42',
                   version='4.1-preview.1',
                   route_values=route_values)

    def get_agent(self, pool_id, agent_id, include_capabilities=None, include_assigned_request=None, property_filters=None):
        """GetAgent.
        [Preview API]
        :param int pool_id:
        :param int agent_id:
        :param bool include_capabilities:
        :param bool include_assigned_request:
        :param [str] property_filters:
        :rtype: :class:`<TaskAgent> <task-agent.v4_1.models.TaskAgent>`
        """
        route_values = {}
        if pool_id is not None:
            route_values['poolId'] = self._serialize.url('pool_id', pool_id, 'int')
        if agent_id is not None:
            route_values['agentId'] = self._serialize.url('agent_id', agent_id, 'int')
        query_parameters = {}
        if include_capabilities is not None:
            query_parameters['includeCapabilities'] = self._serialize.query('include_capabilities', include_capabilities, 'bool')
        if include_assigned_request is not None:
            query_parameters['includeAssignedRequest'] = self._serialize.query('include_assigned_request', include_assigned_request, 'bool')
        if property_filters is not None:
            property_filters = ",".join(property_filters)
            query_parameters['propertyFilters'] = self._serialize.query('property_filters', property_filters, 'str')
        response = self._send(http_method='GET',
                              location_id='e298ef32-5878-4cab-993c-043836571f42',
                              version='4.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TaskAgent', response)

    def get_agents(self, pool_id, agent_name=None, include_capabilities=None, include_assigned_request=None, property_filters=None, demands=None):
        """GetAgents.
        [Preview API]
        :param int pool_id:
        :param str agent_name:
        :param bool include_capabilities:
        :param bool include_assigned_request:
        :param [str] property_filters:
        :param [str] demands:
        :rtype: [TaskAgent]
        """
        route_values = {}
        if pool_id is not None:
            route_values['poolId'] = self._serialize.url('pool_id', pool_id, 'int')
        query_parameters = {}
        if agent_name is not None:
            query_parameters['agentName'] = self._serialize.query('agent_name', agent_name, 'str')
        if include_capabilities is not None:
            query_parameters['includeCapabilities'] = self._serialize.query('include_capabilities', include_capabilities, 'bool')
        if include_assigned_request is not None:
            query_parameters['includeAssignedRequest'] = self._serialize.query('include_assigned_request', include_assigned_request, 'bool')
        if property_filters is not None:
            property_filters = ",".join(property_filters)
            query_parameters['propertyFilters'] = self._serialize.query('property_filters', property_filters, 'str')
        if demands is not None:
            demands = ",".join(demands)
            query_parameters['demands'] = self._serialize.query('demands', demands, 'str')
        response = self._send(http_method='GET',
                              location_id='e298ef32-5878-4cab-993c-043836571f42',
                              version='4.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              returns_collection=True)
        return self._deserialize('[TaskAgent]', response)

    def replace_agent(self, agent, pool_id, agent_id):
        """ReplaceAgent.
        [Preview API]
        :param :class:`<TaskAgent> <task-agent.v4_1.models.TaskAgent>` agent:
        :param int pool_id:
        :param int agent_id:
        :rtype: :class:`<TaskAgent> <task-agent.v4_1.models.TaskAgent>`
        """
        route_values = {}
        if pool_id is not None:
            route_values['poolId'] = self._serialize.url('pool_id', pool_id, 'int')
        if agent_id is not None:
            route_values['agentId'] = self._serialize.url('agent_id', agent_id, 'int')
        content = self._serialize.body(agent, 'TaskAgent')
        response = self._send(http_method='PUT',
                              location_id='e298ef32-5878-4cab-993c-043836571f42',
                              version='4.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TaskAgent', response)

    def update_agent(self, agent, pool_id, agent_id):
        """UpdateAgent.
        [Preview API]
        :param :class:`<TaskAgent> <task-agent.v4_1.models.TaskAgent>` agent:
        :param int pool_id:
        :param int agent_id:
        :rtype: :class:`<TaskAgent> <task-agent.v4_1.models.TaskAgent>`
        """
        route_values = {}
        if pool_id is not None:
            route_values['poolId'] = self._serialize.url('pool_id', pool_id, 'int')
        if agent_id is not None:
            route_values['agentId'] = self._serialize.url('agent_id', agent_id, 'int')
        content = self._serialize.body(agent, 'TaskAgent')
        response = self._send(http_method='PATCH',
                              location_id='e298ef32-5878-4cab-993c-043836571f42',
                              version='4.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TaskAgent', response)

    def get_azure_subscriptions(self):
        """GetAzureSubscriptions.
        [Preview API] Returns list of azure subscriptions
        :rtype: :class:`<AzureSubscriptionQueryResult> <task-agent.v4_1.models.AzureSubscriptionQueryResult>`
        """
        response = self._send(http_method='GET',
                              location_id='bcd6189c-0303-471f-a8e1-acb22b74d700',
                              version='4.1-preview.1')
        return self._deserialize('AzureSubscriptionQueryResult', response)

    def generate_deployment_group_access_token(self, project, deployment_group_id):
        """GenerateDeploymentGroupAccessToken.
        [Preview API]
        :param str project: Project ID or project name
        :param int deployment_group_id:
        :rtype: str
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if deployment_group_id is not None:
            route_values['deploymentGroupId'] = self._serialize.url('deployment_group_id', deployment_group_id, 'int')
        response = self._send(http_method='POST',
                              location_id='3d197ba2-c3e9-4253-882f-0ee2440f8174',
                              version='4.1-preview.1',
                              route_values=route_values)
        return self._deserialize('str', response)

    def add_deployment_group(self, deployment_group, project):
        """AddDeploymentGroup.
        [Preview API]
        :param :class:`<DeploymentGroup> <task-agent.v4_1.models.DeploymentGroup>` deployment_group:
        :param str project: Project ID or project name
        :rtype: :class:`<DeploymentGroup> <task-agent.v4_1.models.DeploymentGroup>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(deployment_group, 'DeploymentGroup')
        response = self._send(http_method='POST',
                              location_id='083c4d89-ab35-45af-aa11-7cf66895c53e',
                              version='4.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('DeploymentGroup', response)

    def delete_deployment_group(self, project, deployment_group_id):
        """DeleteDeploymentGroup.
        [Preview API]
        :param str project: Project ID or project name
        :param int deployment_group_id:
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if deployment_group_id is not None:
            route_values['deploymentGroupId'] = self._serialize.url('deployment_group_id', deployment_group_id, 'int')
        self._send(http_method='DELETE',
                   location_id='083c4d89-ab35-45af-aa11-7cf66895c53e',
                   version='4.1-preview.1',
                   route_values=route_values)

    def get_deployment_group(self, project, deployment_group_id, action_filter=None, expand=None):
        """GetDeploymentGroup.
        [Preview API]
        :param str project: Project ID or project name
        :param int deployment_group_id:
        :param str action_filter:
        :param str expand:
        :rtype: :class:`<DeploymentGroup> <task-agent.v4_1.models.DeploymentGroup>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if deployment_group_id is not None:
            route_values['deploymentGroupId'] = self._serialize.url('deployment_group_id', deployment_group_id, 'int')
        query_parameters = {}
        if action_filter is not None:
            query_parameters['actionFilter'] = self._serialize.query('action_filter', action_filter, 'str')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='083c4d89-ab35-45af-aa11-7cf66895c53e',
                              version='4.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('DeploymentGroup', response)

    def get_deployment_groups(self, project, name=None, action_filter=None, expand=None, continuation_token=None, top=None, ids=None):
        """GetDeploymentGroups.
        [Preview API]
        :param str project: Project ID or project name
        :param str name:
        :param str action_filter:
        :param str expand:
        :param str continuation_token:
        :param int top:
        :param [int] ids:
        :rtype: [DeploymentGroup]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if name is not None:
            query_parameters['name'] = self._serialize.query('name', name, 'str')
        if action_filter is not None:
            query_parameters['actionFilter'] = self._serialize.query('action_filter', action_filter, 'str')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if ids is not None:
            ids = ",".join(map(str, ids))
            query_parameters['ids'] = self._serialize.query('ids', ids, 'str')
        response = self._send(http_method='GET',
                              location_id='083c4d89-ab35-45af-aa11-7cf66895c53e',
                              version='4.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              returns_collection=True)
        return self._deserialize('[DeploymentGroup]', response)

    def update_deployment_group(self, deployment_group, project, deployment_group_id):
        """UpdateDeploymentGroup.
        [Preview API]
        :param :class:`<DeploymentGroup> <task-agent.v4_1.models.DeploymentGroup>` deployment_group:
        :param str project: Project ID or project name
        :param int deployment_group_id:
        :rtype: :class:`<DeploymentGroup> <task-agent.v4_1.models.DeploymentGroup>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if deployment_group_id is not None:
            route_values['deploymentGroupId'] = self._serialize.url('deployment_group_id', deployment_group_id, 'int')
        content = self._serialize.body(deployment_group, 'DeploymentGroup')
        response = self._send(http_method='PATCH',
                              location_id='083c4d89-ab35-45af-aa11-7cf66895c53e',
                              version='4.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('DeploymentGroup', response)

    def get_deployment_groups_metrics(self, project, deployment_group_name=None, continuation_token=None, top=None):
        """GetDeploymentGroupsMetrics.
        [Preview API]
        :param str project: Project ID or project name
        :param str deployment_group_name:
        :param str continuation_token:
        :param int top:
        :rtype: [DeploymentGroupMetrics]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if deployment_group_name is not None:
            query_parameters['deploymentGroupName'] = self._serialize.query('deployment_group_name', deployment_group_name, 'str')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        response = self._send(http_method='GET',
                              location_id='281c6308-427a-49e1-b83a-dac0f4862189',
                              version='4.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              returns_collection=True)
        return self._deserialize('[DeploymentGroupMetrics]', response)

    def get_agent_requests_for_deployment_machine(self, project, deployment_group_id, machine_id, completed_request_count=None):
        """GetAgentRequestsForDeploymentMachine.
        [Preview API]
        :param str project: Project ID or project name
        :param int deployment_group_id:
        :param int machine_id:
        :param int completed_request_count:
        :rtype: [TaskAgentJobRequest]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if deployment_group_id is not None:
            route_values['deploymentGroupId'] = self._serialize.url('deployment_group_id', deployment_group_id, 'int')
        query_parameters = {}
        if machine_id is not None:
            query_parameters['machineId'] = self._serialize.query('machine_id', machine_id, 'int')
        if completed_request_count is not None:
            query_parameters['completedRequestCount'] = self._serialize.query('completed_request_count', completed_request_count, 'int')
        response = self._send(http_method='GET',
                              location_id='a3540e5b-f0dc-4668-963b-b752459be545',
                              version='4.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              returns_collection=True)
        return self._deserialize('[TaskAgentJobRequest]', response)

    def get_agent_requests_for_deployment_machines(self, project, deployment_group_id, machine_ids=None, completed_request_count=None):
        """GetAgentRequestsForDeploymentMachines.
        [Preview API]
        :param str project: Project ID or project name
        :param int deployment_group_id:
        :param [int] machine_ids:
        :param int completed_request_count:
        :rtype: [TaskAgentJobRequest]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if deployment_group_id is not None:
            route_values['deploymentGroupId'] = self._serialize.url('deployment_group_id', deployment_group_id, 'int')
        query_parameters = {}
        if machine_ids is not None:
            machine_ids = ",".join(map(str, machine_ids))
            query_parameters['machineIds'] = self._serialize.query('machine_ids', machine_ids, 'str')
        if completed_request_count is not None:
            query_parameters['completedRequestCount'] = self._serialize.query('completed_request_count', completed_request_count, 'int')
        response = self._send(http_method='GET',
                              location_id='a3540e5b-f0dc-4668-963b-b752459be545',
                              version='4.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              returns_collection=True)
        return self._deserialize('[TaskAgentJobRequest]', response)

    def refresh_deployment_machines(self, project, deployment_group_id):
        """RefreshDeploymentMachines.
        [Preview API]
        :param str project: Project ID or project name
        :param int deployment_group_id:
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if deployment_group_id is not None:
            route_values['deploymentGroupId'] = self._serialize.url('deployment_group_id', deployment_group_id, 'int')
        self._send(http_method='POST',
                   location_id='91006ac4-0f68-4d82-a2bc-540676bd73ce',
                   version='4.1-preview.1',
                   route_values=route_values)

    def generate_deployment_pool_access_token(self, pool_id):
        """GenerateDeploymentPoolAccessToken.
        [Preview API]
        :param int pool_id:
        :rtype: str
        """
        route_values = {}
        if pool_id is not None:
            route_values['poolId'] = self._serialize.url('pool_id', pool_id, 'int')
        response = self._send(http_method='POST',
                              location_id='e077ee4a-399b-420b-841f-c43fbc058e0b',
                              version='4.1-preview.1',
                              route_values=route_values)
        return self._deserialize('str', response)

    def get_deployment_pools_summary(self, pool_name=None, expands=None):
        """GetDeploymentPoolsSummary.
        [Preview API] Get the deployment pools summary.
        :param str pool_name: Get summary of deployment pools with name containing poolName.
        :param str expands: Populate Deployment groups references if set to DeploymentGroups. Default is **None**
        :rtype: [DeploymentPoolSummary]
        """
        query_parameters = {}
        if pool_name is not None:
            query_parameters['poolName'] = self._serialize.query('pool_name', pool_name, 'str')
        if expands is not None:
            query_parameters['expands'] = self._serialize.query('expands', expands, 'str')
        response = self._send(http_method='GET',
                              location_id='6525d6c6-258f-40e0-a1a9-8a24a3957625',
                              version='4.1-preview.1',
                              query_parameters=query_parameters,
                              returns_collection=True)
        return self._deserialize('[DeploymentPoolSummary]', response)

    def get_agent_requests_for_deployment_target(self, project, deployment_group_id, target_id, completed_request_count=None):
        """GetAgentRequestsForDeploymentTarget.
        [Preview API] Get agent requests for a deployment target.
        :param str project: Project ID or project name
        :param int deployment_group_id: Id of the deployment group to which target belongs.
        :param int target_id: Id of the deployment target to get.
        :param int completed_request_count: Maximum count of completed requests to get.
        :rtype: [TaskAgentJobRequest]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if deployment_group_id is not None:
            route_values['deploymentGroupId'] = self._serialize.url('deployment_group_id', deployment_group_id, 'int')
        query_parameters = {}
        if target_id is not None:
            query_parameters['targetId'] = self._serialize.query('target_id', target_id, 'int')
        if completed_request_count is not None:
            query_parameters['completedRequestCount'] = self._serialize.query('completed_request_count', completed_request_count, 'int')
        response = self._send(http_method='GET',
                              location_id='2fac0be3-8c8f-4473-ab93-c1389b08a2c9',
                              version='4.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              returns_collection=True)
        return self._deserialize('[TaskAgentJobRequest]', response)

    def get_agent_requests_for_deployment_targets(self, project, deployment_group_id, target_ids=None, completed_request_count=None):
        """GetAgentRequestsForDeploymentTargets.
        [Preview API] Get agent requests for deployment targets.
        :param str project: Project ID or project name
        :param int deployment_group_id: Id of the deployment group to which targets belongs.
        :param [int] target_ids: Ids of the deployment target to get.
        :param int completed_request_count: Maximum count of completed requests to get.
        :rtype: [TaskAgentJobRequest]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if deployment_group_id is not None:
            route_values['deploymentGroupId'] = self._serialize.url('deployment_group_id', deployment_group_id, 'int')
        query_parameters = {}
        if target_ids is not None:
            target_ids = ",".join(map(str, target_ids))
            query_parameters['targetIds'] = self._serialize.query('target_ids', target_ids, 'str')
        if completed_request_count is not None:
            query_parameters['completedRequestCount'] = self._serialize.query('completed_request_count', completed_request_count, 'int')
        response = self._send(http_method='GET',
                              location_id='2fac0be3-8c8f-4473-ab93-c1389b08a2c9',
                              version='4.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              returns_collection=True)
        return self._deserialize('[TaskAgentJobRequest]', response)

    def query_endpoint(self, endpoint):
        """QueryEndpoint.
        [Preview API] Proxy for a GET request defined by an 'endpoint'. The request is authorized using a service connection. The response is filtered using an XPath/Json based selector.
        :param :class:`<TaskDefinitionEndpoint> <task-agent.v4_1.models.TaskDefinitionEndpoint>` endpoint: Describes the URL to fetch.
        :rtype: [str]
        """
        content = self._serialize.body(endpoint, 'TaskDefinitionEndpoint')
        response = self._send(http_method='POST',
                              location_id='f223b809-8c33-4b7d-b53f-07232569b5d6',
                              version='4.1-preview.1',
                              content=content,
                              returns_collection=True)
        return self._deserialize('[str]', response)

    def get_service_endpoint_execution_records(self, project, endpoint_id, top=None):
        """GetServiceEndpointExecutionRecords.
        [Preview API]
        :param str project: Project ID or project name
        :param str endpoint_id:
        :param int top:
        :rtype: [ServiceEndpointExecutionRecord]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if endpoint_id is not None:
            route_values['endpointId'] = self._serialize.url('endpoint_id', endpoint_id, 'str')
        query_parameters = {}
        if top is not None:
            query_parameters['top'] = self._serialize.query('top', top, 'int')
        response = self._send(http_method='GET',
                              location_id='3ad71e20-7586-45f9-a6c8-0342e00835ac',
                              version='4.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              returns_collection=True)
        return self._deserialize('[ServiceEndpointExecutionRecord]', response)

    def add_service_endpoint_execution_records(self, input, project):
        """AddServiceEndpointExecutionRecords.
        [Preview API]
        :param :class:`<ServiceEndpointExecutionRecordsInput> <task-agent.v4_1.models.ServiceEndpointExecutionRecordsInput>` input:
        :param str project: Project ID or project name
        :rtype: [ServiceEndpointExecutionRecord]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(input, 'ServiceEndpointExecutionRecordsInput')
        response = self._send(http_method='POST',
                              location_id='11a45c69-2cce-4ade-a361-c9f5a37239ee',
                              version='4.1-preview.1',
                              route_values=route_values,
                              content=content,
                              returns_collection=True)
        return self._deserialize('[ServiceEndpointExecutionRecord]', response)

    def validate_inputs(self, input_validation_request):
        """ValidateInputs.
        [Preview API]
        :param :class:`<InputValidationRequest> <task-agent.v4_1.models.InputValidationRequest>` input_validation_request:
        :rtype: :class:`<InputValidationRequest> <task-agent.v4_1.models.InputValidationRequest>`
        """
        content = self._serialize.body(input_validation_request, 'InputValidationRequest')
        response = self._send(http_method='POST',
                              location_id='58475b1e-adaf-4155-9bc1-e04bf1fff4c2',
                              version='4.1-preview.1',
                              content=content)
        return self._deserialize('InputValidationRequest', response)

    def generate_deployment_machine_group_access_token(self, project, machine_group_id):
        """GenerateDeploymentMachineGroupAccessToken.
        [Preview API]
        :param str project: Project ID or project name
        :param int machine_group_id:
        :rtype: str
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if machine_group_id is not None:
            route_values['machineGroupId'] = self._serialize.url('machine_group_id', machine_group_id, 'int')
        response = self._send(http_method='POST',
                              location_id='f8c7c0de-ac0d-469b-9cb1-c21f72d67693',
                              version='4.1-preview.1',
                              route_values=route_values)
        return self._deserialize('str', response)

    def add_deployment_machine_group(self, machine_group, project):
        """AddDeploymentMachineGroup.
        [Preview API]
        :param :class:`<DeploymentMachineGroup> <task-agent.v4_1.models.DeploymentMachineGroup>` machine_group:
        :param str project: Project ID or project name
        :rtype: :class:`<DeploymentMachineGroup> <task-agent.v4_1.models.DeploymentMachineGroup>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(machine_group, 'DeploymentMachineGroup')
        response = self._send(http_method='POST',
                              location_id='d4adf50f-80c6-4ac8-9ca1-6e4e544286e9',
                              version='4.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('DeploymentMachineGroup', response)

    def delete_deployment_machine_group(self, project, machine_group_id):
        """DeleteDeploymentMachineGroup.
        [Preview API]
        :param str project: Project ID or project name
        :param int machine_group_id:
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if machine_group_id is not None:
            route_values['machineGroupId'] = self._serialize.url('machine_group_id', machine_group_id, 'int')
        self._send(http_method='DELETE',
                   location_id='d4adf50f-80c6-4ac8-9ca1-6e4e544286e9',
                   version='4.1-preview.1',
                   route_values=route_values)

    def get_deployment_machine_group(self, project, machine_group_id, action_filter=None):
        """GetDeploymentMachineGroup.
        [Preview API]
        :param str project: Project ID or project name
        :param int machine_group_id:
        :param str action_filter:
        :rtype: :class:`<DeploymentMachineGroup> <task-agent.v4_1.models.DeploymentMachineGroup>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if machine_group_id is not None:
            route_values['machineGroupId'] = self._serialize.url('machine_group_id', machine_group_id, 'int')
        query_parameters = {}
        if action_filter is not None:
            query_parameters['actionFilter'] = self._serialize.query('action_filter', action_filter, 'str')
        response = self._send(http_method='GET',
                              location_id='d4adf50f-80c6-4ac8-9ca1-6e4e544286e9',
                              version='4.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('DeploymentMachineGroup', response)

    def get_deployment_machine_groups(self, project, machine_group_name=None, action_filter=None):
        """GetDeploymentMachineGroups.
        [Preview API]
        :param str project: Project ID or project name
        :param str machine_group_name:
        :param str action_filter:
        :rtype: [DeploymentMachineGroup]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if machine_group_name is not None:
            query_parameters['machineGroupName'] = self._serialize.query('machine_group_name', machine_group_name, 'str')
        if action_filter is not None:
            query_parameters['actionFilter'] = self._serialize.query('action_filter', action_filter, 'str')
        response = self._send(http_method='GET',
                              location_id='d4adf50f-80c6-4ac8-9ca1-6e4e544286e9',
                              version='4.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              returns_collection=True)
        return self._deserialize('[DeploymentMachineGroup]', response)

    def update_deployment_machine_group(self, machine_group, project, machine_group_id):
        """UpdateDeploymentMachineGroup.
        [Preview API]
        :param :class:`<DeploymentMachineGroup> <task-agent.v4_1.models.DeploymentMachineGroup>` machine_group:
        :param str project: Project ID or project name
        :param int machine_group_id:
        :rtype: :class:`<DeploymentMachineGroup> <task-agent.v4_1.models.DeploymentMachineGroup>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if machine_group_id is not None:
            route_values['machineGroupId'] = self._serialize.url('machine_group_id', machine_group_id, 'int')
        content = self._serialize.body(machine_group, 'DeploymentMachineGroup')
        response = self._send(http_method='PATCH',
                              location_id='d4adf50f-80c6-4ac8-9ca1-6e4e544286e9',
                              version='4.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('DeploymentMachineGroup', response)

    def get_deployment_machine_group_machines(self, project, machine_group_id, tag_filters=None):
        """GetDeploymentMachineGroupMachines.
        [Preview API]
        :param str project: Project ID or project name
        :param int machine_group_id:
        :param [str] tag_filters:
        :rtype: [DeploymentMachine]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if machine_group_id is not None:
            route_values['machineGroupId'] = self._serialize.url('machine_group_id', machine_group_id, 'int')
        query_parameters = {}
        if tag_filters is not None:
            tag_filters = ",".join(tag_filters)
            query_parameters['tagFilters'] = self._serialize.query('tag_filters', tag_filters, 'str')
        response = self._send(http_method='GET',
                              location_id='966c3874-c347-4b18-a90c-d509116717fd',
                              version='4.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              returns_collection=True)
        return self._deserialize('[DeploymentMachine]', response)

    def update_deployment_machine_group_machines(self, deployment_machines, project, machine_group_id):
        """UpdateDeploymentMachineGroupMachines.
        [Preview API]
        :param [DeploymentMachine] deployment_machines:
        :param str project: Project ID or project name
        :param int machine_group_id:
        :rtype: [DeploymentMachine]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if machine_group_id is not None:
            route_values['machineGroupId'] = self._serialize.url('machine_group_id', machine_group_id, 'int')
        content = self._serialize.body(deployment_machines, '[DeploymentMachine]')
        response = self._send(http_method='PATCH',
                              location_id='966c3874-c347-4b18-a90c-d509116717fd',
                              version='4.1-preview.1',
                              route_values=route_values,
                              content=content,
                              returns_collection=True)
        return self._deserialize('[DeploymentMachine]', response)

    def add_deployment_machine(self, machine, project, deployment_group_id):
        """AddDeploymentMachine.
        [Preview API]
        :param :class:`<DeploymentMachine> <task-agent.v4_1.models.DeploymentMachine>` machine:
        :param str project: Project ID or project name
        :param int deployment_group_id:
        :rtype: :class:`<DeploymentMachine> <task-agent.v4_1.models.DeploymentMachine>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if deployment_group_id is not None:
            route_values['deploymentGroupId'] = self._serialize.url('deployment_group_id', deployment_group_id, 'int')
        content = self._serialize.body(machine, 'DeploymentMachine')
        response = self._send(http_method='POST',
                              location_id='6f6d406f-cfe6-409c-9327-7009928077e7',
                              version='4.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('DeploymentMachine', response)

    def delete_deployment_machine(self, project, deployment_group_id, machine_id):
        """DeleteDeploymentMachine.
        [Preview API]
        :param str project: Project ID or project name
        :param int deployment_group_id:
        :param int machine_id:
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if deployment_group_id is not None:
            route_values['deploymentGroupId'] = self._serialize.url('deployment_group_id', deployment_group_id, 'int')
        if machine_id is not None:
            route_values['machineId'] = self._serialize.url('machine_id', machine_id, 'int')
        self._send(http_method='DELETE',
                   location_id='6f6d406f-cfe6-409c-9327-7009928077e7',
                   version='4.1-preview.1',
                   route_values=route_values)

    def get_deployment_machine(self, project, deployment_group_id, machine_id, expand=None):
        """GetDeploymentMachine.
        [Preview API]
        :param str project: Project ID or project name
        :param int deployment_group_id:
        :param int machine_id:
        :param str expand:
        :rtype: :class:`<DeploymentMachine> <task-agent.v4_1.models.DeploymentMachine>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if deployment_group_id is not None:
            route_values['deploymentGroupId'] = self._serialize.url('deployment_group_id', deployment_group_id, 'int')
        if machine_id is not None:
            route_values['machineId'] = self._serialize.url('machine_id', machine_id, 'int')
        query_parameters = {}
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='6f6d406f-cfe6-409c-9327-7009928077e7',
                              version='4.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('DeploymentMachine', response)

    def get_deployment_machines(self, project, deployment_group_id, tags=None, name=None, expand=None):
        """GetDeploymentMachines.
        [Preview API]
        :param str project: Project ID or project name
        :param int deployment_group_id:
        :param [str] tags:
        :param str name:
        :param str expand:
        :rtype: [DeploymentMachine]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if deployment_group_id is not None:
            route_values['deploymentGroupId'] = self._serialize.url('deployment_group_id', deployment_group_id, 'int')
        query_parameters = {}
        if tags is not None:
            tags = ",".join(tags)
            query_parameters['tags'] = self._serialize.query('tags', tags, 'str')
        if name is not None:
            query_parameters['name'] = self._serialize.query('name', name, 'str')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='6f6d406f-cfe6-409c-9327-7009928077e7',
                              version='4.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              returns_collection=True)
        return self._deserialize('[DeploymentMachine]', response)

    def replace_deployment_machine(self, machine, project, deployment_group_id, machine_id):
        """ReplaceDeploymentMachine.
        [Preview API]
        :param :class:`<DeploymentMachine> <task-agent.v4_1.models.DeploymentMachine>` machine:
        :param str project: Project ID or project name
        :param int deployment_group_id:
        :param int machine_id:
        :rtype: :class:`<DeploymentMachine> <task-agent.v4_1.models.DeploymentMachine>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if deployment_group_id is not None:
            route_values['deploymentGroupId'] = self._serialize.url('deployment_group_id', deployment_group_id, 'int')
        if machine_id is not None:
            route_values['machineId'] = self._serialize.url('machine_id', machine_id, 'int')
        content = self._serialize.body(machine, 'DeploymentMachine')
        response = self._send(http_method='PUT',
                              location_id='6f6d406f-cfe6-409c-9327-7009928077e7',
                              version='4.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('DeploymentMachine', response)

    def update_deployment_machine(self, machine, project, deployment_group_id, machine_id):
        """UpdateDeploymentMachine.
        [Preview API]
        :param :class:`<DeploymentMachine> <task-agent.v4_1.models.DeploymentMachine>` machine:
        :param str project: Project ID or project name
        :param int deployment_group_id:
        :param int machine_id:
        :rtype: :class:`<DeploymentMachine> <task-agent.v4_1.models.DeploymentMachine>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if deployment_group_id is not None:
            route_values['deploymentGroupId'] = self._serialize.url('deployment_group_id', deployment_group_id, 'int')
        if machine_id is not None:
            route_values['machineId'] = self._serialize.url('machine_id', machine_id, 'int')
        content = self._serialize.body(machine, 'DeploymentMachine')
        response = self._send(http_method='PATCH',
                              location_id='6f6d406f-cfe6-409c-9327-7009928077e7',
                              version='4.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('DeploymentMachine', response)

    def update_deployment_machines(self, machines, project, deployment_group_id):
        """UpdateDeploymentMachines.
        [Preview API]
        :param [DeploymentMachine] machines:
        :param str project: Project ID or project name
        :param int deployment_group_id:
        :rtype: [DeploymentMachine]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if deployment_group_id is not None:
            route_values['deploymentGroupId'] = self._serialize.url('deployment_group_id', deployment_group_id, 'int')
        content = self._serialize.body(machines, '[DeploymentMachine]')
        response = self._send(http_method='PATCH',
                              location_id='6f6d406f-cfe6-409c-9327-7009928077e7',
                              version='4.1-preview.1',
                              route_values=route_values,
                              content=content,
                              returns_collection=True)
        return self._deserialize('[DeploymentMachine]', response)

    def create_agent_pool_maintenance_definition(self, definition, pool_id):
        """CreateAgentPoolMaintenanceDefinition.
        [Preview API]
        :param :class:`<TaskAgentPoolMaintenanceDefinition> <task-agent.v4_1.models.TaskAgentPoolMaintenanceDefinition>` definition:
        :param int pool_id:
        :rtype: :class:`<TaskAgentPoolMaintenanceDefinition> <task-agent.v4_1.models.TaskAgentPoolMaintenanceDefinition>`
        """
        route_values = {}
        if pool_id is not None:
            route_values['poolId'] = self._serialize.url('pool_id', pool_id, 'int')
        content = self._serialize.body(definition, 'TaskAgentPoolMaintenanceDefinition')
        response = self._send(http_method='POST',
                              location_id='80572e16-58f0-4419-ac07-d19fde32195c',
                              version='4.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TaskAgentPoolMaintenanceDefinition', response)

    def delete_agent_pool_maintenance_definition(self, pool_id, definition_id):
        """DeleteAgentPoolMaintenanceDefinition.
        [Preview API]
        :param int pool_id:
        :param int definition_id:
        """
        route_values = {}
        if pool_id is not None:
            route_values['poolId'] = self._serialize.url('pool_id', pool_id, 'int')
        if definition_id is not None:
            route_values['definitionId'] = self._serialize.url('definition_id', definition_id, 'int')
        self._send(http_method='DELETE',
                   location_id='80572e16-58f0-4419-ac07-d19fde32195c',
                   version='4.1-preview.1',
                   route_values=route_values)

    def get_agent_pool_maintenance_definition(self, pool_id, definition_id):
        """GetAgentPoolMaintenanceDefinition.
        [Preview API]
        :param int pool_id:
        :param int definition_id:
        :rtype: :class:`<TaskAgentPoolMaintenanceDefinition> <task-agent.v4_1.models.TaskAgentPoolMaintenanceDefinition>`
        """
        route_values = {}
        if pool_id is not None:
            route_values['poolId'] = self._serialize.url('pool_id', pool_id, 'int')
        if definition_id is not None:
            route_values['definitionId'] = self._serialize.url('definition_id', definition_id, 'int')
        response = self._send(http_method='GET',
                              location_id='80572e16-58f0-4419-ac07-d19fde32195c',
                              version='4.1-preview.1',
                              route_values=route_values)
        return self._deserialize('TaskAgentPoolMaintenanceDefinition', response)

    def get_agent_pool_maintenance_definitions(self, pool_id):
        """GetAgentPoolMaintenanceDefinitions.
        [Preview API]
        :param int pool_id:
        :rtype: [TaskAgentPoolMaintenanceDefinition]
        """
        route_values = {}
        if pool_id is not None:
            route_values['poolId'] = self._serialize.url('pool_id', pool_id, 'int')
        response = self._send(http_method='GET',
                              location_id='80572e16-58f0-4419-ac07-d19fde32195c',
                              version='4.1-preview.1',
                              route_values=route_values,
                              returns_collection=True)
        return self._deserialize('[TaskAgentPoolMaintenanceDefinition]', response)

    def update_agent_pool_maintenance_definition(self, definition, pool_id, definition_id):
        """UpdateAgentPoolMaintenanceDefinition.
        [Preview API]
        :param :class:`<TaskAgentPoolMaintenanceDefinition> <task-agent.v4_1.models.TaskAgentPoolMaintenanceDefinition>` definition:
        :param int pool_id:
        :param int definition_id:
        :rtype: :class:`<TaskAgentPoolMaintenanceDefinition> <task-agent.v4_1.models.TaskAgentPoolMaintenanceDefinition>`
        """
        route_values = {}
        if pool_id is not None:
            route_values['poolId'] = self._serialize.url('pool_id', pool_id, 'int')
        if definition_id is not None:
            route_values['definitionId'] = self._serialize.url('definition_id', definition_id, 'int')
        content = self._serialize.body(definition, 'TaskAgentPoolMaintenanceDefinition')
        response = self._send(http_method='PUT',
                              location_id='80572e16-58f0-4419-ac07-d19fde32195c',
                              version='4.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TaskAgentPoolMaintenanceDefinition', response)

    def delete_agent_pool_maintenance_job(self, pool_id, job_id):
        """DeleteAgentPoolMaintenanceJob.
        [Preview API]
        :param int pool_id:
        :param int job_id:
        """
        route_values = {}
        if pool_id is not None:
            route_values['poolId'] = self._serialize.url('pool_id', pool_id, 'int')
        if job_id is not None:
            route_values['jobId'] = self._serialize.url('job_id', job_id, 'int')
        self._send(http_method='DELETE',
                   location_id='15e7ab6e-abce-4601-a6d8-e111fe148f46',
                   version='4.1-preview.1',
                   route_values=route_values)

    def get_agent_pool_maintenance_job(self, pool_id, job_id):
        """GetAgentPoolMaintenanceJob.
        [Preview API]
        :param int pool_id:
        :param int job_id:
        :rtype: :class:`<TaskAgentPoolMaintenanceJob> <task-agent.v4_1.models.TaskAgentPoolMaintenanceJob>`
        """
        route_values = {}
        if pool_id is not None:
            route_values['poolId'] = self._serialize.url('pool_id', pool_id, 'int')
        if job_id is not None:
            route_values['jobId'] = self._serialize.url('job_id', job_id, 'int')
        response = self._send(http_method='GET',
                              location_id='15e7ab6e-abce-4601-a6d8-e111fe148f46',
                              version='4.1-preview.1',
                              route_values=route_values)
        return self._deserialize('TaskAgentPoolMaintenanceJob', response)

    def get_agent_pool_maintenance_job_logs(self, pool_id, job_id):
        """GetAgentPoolMaintenanceJobLogs.
        [Preview API]
        :param int pool_id:
        :param int job_id:
        :rtype: object
        """
        route_values = {}
        if pool_id is not None:
            route_values['poolId'] = self._serialize.url('pool_id', pool_id, 'int')
        if job_id is not None:
            route_values['jobId'] = self._serialize.url('job_id', job_id, 'int')
        response = self._send(http_method='GET',
                              location_id='15e7ab6e-abce-4601-a6d8-e111fe148f46',
                              version='4.1-preview.1',
                              route_values=route_values)
        return self._deserialize('object', response)

    def get_agent_pool_maintenance_jobs(self, pool_id, definition_id=None):
        """GetAgentPoolMaintenanceJobs.
        [Preview API]
        :param int pool_id:
        :param int definition_id:
        :rtype: [TaskAgentPoolMaintenanceJob]
        """
        route_values = {}
        if pool_id is not None:
            route_values['poolId'] = self._serialize.url('pool_id', pool_id, 'int')
        query_parameters = {}
        if definition_id is not None:
            query_parameters['definitionId'] = self._serialize.query('definition_id', definition_id, 'int')
        response = self._send(http_method='GET',
                              location_id='15e7ab6e-abce-4601-a6d8-e111fe148f46',
                              version='4.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              returns_collection=True)
        return self._deserialize('[TaskAgentPoolMaintenanceJob]', response)

    def queue_agent_pool_maintenance_job(self, job, pool_id):
        """QueueAgentPoolMaintenanceJob.
        [Preview API]
        :param :class:`<TaskAgentPoolMaintenanceJob> <task-agent.v4_1.models.TaskAgentPoolMaintenanceJob>` job:
        :param int pool_id:
        :rtype: :class:`<TaskAgentPoolMaintenanceJob> <task-agent.v4_1.models.TaskAgentPoolMaintenanceJob>`
        """
        route_values = {}
        if pool_id is not None:
            route_values['poolId'] = self._serialize.url('pool_id', pool_id, 'int')
        content = self._serialize.body(job, 'TaskAgentPoolMaintenanceJob')
        response = self._send(http_method='POST',
                              location_id='15e7ab6e-abce-4601-a6d8-e111fe148f46',
                              version='4.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TaskAgentPoolMaintenanceJob', response)

    def update_agent_pool_maintenance_job(self, job, pool_id, job_id):
        """UpdateAgentPoolMaintenanceJob.
        [Preview API]
        :param :class:`<TaskAgentPoolMaintenanceJob> <task-agent.v4_1.models.TaskAgentPoolMaintenanceJob>` job:
        :param int pool_id:
        :param int job_id:
        :rtype: :class:`<TaskAgentPoolMaintenanceJob> <task-agent.v4_1.models.TaskAgentPoolMaintenanceJob>`
        """
        route_values = {}
        if pool_id is not None:
            route_values['poolId'] = self._serialize.url('pool_id', pool_id, 'int')
        if job_id is not None:
            route_values['jobId'] = self._serialize.url('job_id', job_id, 'int')
        content = self._serialize.body(job, 'TaskAgentPoolMaintenanceJob')
        response = self._send(http_method='PATCH',
                              location_id='15e7ab6e-abce-4601-a6d8-e111fe148f46',
                              version='4.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TaskAgentPoolMaintenanceJob', response)

    def delete_message(self, pool_id, message_id, session_id):
        """DeleteMessage.
        [Preview API]
        :param int pool_id:
        :param long message_id:
        :param str session_id:
        """
        route_values = {}
        if pool_id is not None:
            route_values['poolId'] = self._serialize.url('pool_id', pool_id, 'int')
        if message_id is not None:
            route_values['messageId'] = self._serialize.url('message_id', message_id, 'long')
        query_parameters = {}
        if session_id is not None:
            query_parameters['sessionId'] = self._serialize.query('session_id', session_id, 'str')
        self._send(http_method='DELETE',
                   location_id='c3a054f6-7a8a-49c0-944e-3a8e5d7adfd7',
                   version='4.1-preview.1',
                   route_values=route_values,
                   query_parameters=query_parameters)

    def get_message(self, pool_id, session_id, last_message_id=None):
        """GetMessage.
        [Preview API]
        :param int pool_id:
        :param str session_id:
        :param long last_message_id:
        :rtype: :class:`<TaskAgentMessage> <task-agent.v4_1.models.TaskAgentMessage>`
        """
        route_values = {}
        if pool_id is not None:
            route_values['poolId'] = self._serialize.url('pool_id', pool_id, 'int')
        query_parameters = {}
        if session_id is not None:
            query_parameters['sessionId'] = self._serialize.query('session_id', session_id, 'str')
        if last_message_id is not None:
            query_parameters['lastMessageId'] = self._serialize.query('last_message_id', last_message_id, 'long')
        response = self._send(http_method='GET',
                              location_id='c3a054f6-7a8a-49c0-944e-3a8e5d7adfd7',
                              version='4.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TaskAgentMessage', response)

    def refresh_agent(self, pool_id, agent_id):
        """RefreshAgent.
        [Preview API]
        :param int pool_id:
        :param int agent_id:
        """
        route_values = {}
        if pool_id is not None:
            route_values['poolId'] = self._serialize.url('pool_id', pool_id, 'int')
        query_parameters = {}
        if agent_id is not None:
            query_parameters['agentId'] = self._serialize.query('agent_id', agent_id, 'int')
        self._send(http_method='POST',
                   location_id='c3a054f6-7a8a-49c0-944e-3a8e5d7adfd7',
                   version='4.1-preview.1',
                   route_values=route_values,
                   query_parameters=query_parameters)

    def refresh_agents(self, pool_id):
        """RefreshAgents.
        [Preview API]
        :param int pool_id:
        """
        route_values = {}
        if pool_id is not None:
            route_values['poolId'] = self._serialize.url('pool_id', pool_id, 'int')
        self._send(http_method='POST',
                   location_id='c3a054f6-7a8a-49c0-944e-3a8e5d7adfd7',
                   version='4.1-preview.1',
                   route_values=route_values)

    def send_message(self, message, pool_id, request_id):
        """SendMessage.
        [Preview API]
        :param :class:`<TaskAgentMessage> <task-agent.v4_1.models.TaskAgentMessage>` message:
        :param int pool_id:
        :param long request_id:
        """
        route_values = {}
        if pool_id is not None:
            route_values['poolId'] = self._serialize.url('pool_id', pool_id, 'int')
        query_parameters = {}
        if request_id is not None:
            query_parameters['requestId'] = self._serialize.query('request_id', request_id, 'long')
        content = self._serialize.body(message, 'TaskAgentMessage')
        self._send(http_method='POST',
                   location_id='c3a054f6-7a8a-49c0-944e-3a8e5d7adfd7',
                   version='4.1-preview.1',
                   route_values=route_values,
                   query_parameters=query_parameters,
                   content=content)

    def get_package(self, package_type, platform, version):
        """GetPackage.
        [Preview API]
        :param str package_type:
        :param str platform:
        :param str version:
        :rtype: :class:`<PackageMetadata> <task-agent.v4_1.models.PackageMetadata>`
        """
        route_values = {}
        if package_type is not None:
            route_values['packageType'] = self._serialize.url('package_type', package_type, 'str')
        if platform is not None:
            route_values['platform'] = self._serialize.url('platform', platform, 'str')
        if version is not None:
            route_values['version'] = self._serialize.url('version', version, 'str')
        response = self._send(http_method='GET',
                              location_id='8ffcd551-079c-493a-9c02-54346299d144',
                              version='4.1-preview.2',
                              route_values=route_values)
        return self._deserialize('PackageMetadata', response)

    def get_packages(self, package_type, platform=None, top=None):
        """GetPackages.
        [Preview API]
        :param str package_type:
        :param str platform:
        :param int top:
        :rtype: [PackageMetadata]
        """
        route_values = {}
        if package_type is not None:
            route_values['packageType'] = self._serialize.url('package_type', package_type, 'str')
        if platform is not None:
            route_values['platform'] = self._serialize.url('platform', platform, 'str')
        query_parameters = {}
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        response = self._send(http_method='GET',
                              location_id='8ffcd551-079c-493a-9c02-54346299d144',
                              version='4.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              returns_collection=True)
        return self._deserialize('[PackageMetadata]', response)

    def add_agent_queue(self, queue, project=None):
        """AddAgentQueue.
        [Preview API]
        :param :class:`<TaskAgentQueue> <task-agent.v4_1.models.TaskAgentQueue>` queue:
        :param str project: Project ID or project name
        :rtype: :class:`<TaskAgentQueue> <task-agent.v4_1.models.TaskAgentQueue>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(queue, 'TaskAgentQueue')
        response = self._send(http_method='POST',
                              location_id='900fa995-c559-4923-aae7-f8424fe4fbea',
                              version='4.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TaskAgentQueue', response)

    def create_team_project(self, project=None):
        """CreateTeamProject.
        [Preview API]
        :param str project: Project ID or project name
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        self._send(http_method='PUT',
                   location_id='900fa995-c559-4923-aae7-f8424fe4fbea',
                   version='4.1-preview.1',
                   route_values=route_values)

    def delete_agent_queue(self, queue_id, project=None):
        """DeleteAgentQueue.
        [Preview API]
        :param int queue_id:
        :param str project: Project ID or project name
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if queue_id is not None:
            route_values['queueId'] = self._serialize.url('queue_id', queue_id, 'int')
        self._send(http_method='DELETE',
                   location_id='900fa995-c559-4923-aae7-f8424fe4fbea',
                   version='4.1-preview.1',
                   route_values=route_values)

    def get_agent_queue(self, queue_id, project=None, action_filter=None):
        """GetAgentQueue.
        [Preview API]
        :param int queue_id:
        :param str project: Project ID or project name
        :param str action_filter:
        :rtype: :class:`<TaskAgentQueue> <task-agent.v4_1.models.TaskAgentQueue>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if queue_id is not None:
            route_values['queueId'] = self._serialize.url('queue_id', queue_id, 'int')
        query_parameters = {}
        if action_filter is not None:
            query_parameters['actionFilter'] = self._serialize.query('action_filter', action_filter, 'str')
        response = self._send(http_method='GET',
                              location_id='900fa995-c559-4923-aae7-f8424fe4fbea',
                              version='4.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TaskAgentQueue', response)

    def get_agent_queues(self, project=None, queue_name=None, action_filter=None):
        """GetAgentQueues.
        [Preview API]
        :param str project: Project ID or project name
        :param str queue_name:
        :param str action_filter:
        :rtype: [TaskAgentQueue]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if queue_name is not None:
            query_parameters['queueName'] = self._serialize.query('queue_name', queue_name, 'str')
        if action_filter is not None:
            query_parameters['actionFilter'] = self._serialize.query('action_filter', action_filter, 'str')
        response = self._send(http_method='GET',
                              location_id='900fa995-c559-4923-aae7-f8424fe4fbea',
                              version='4.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              returns_collection=True)
        return self._deserialize('[TaskAgentQueue]', response)

    def get_agent_queues_by_ids(self, queue_ids, project=None, action_filter=None):
        """GetAgentQueuesByIds.
        [Preview API]
        :param [int] queue_ids:
        :param str project: Project ID or project name
        :param str action_filter:
        :rtype: [TaskAgentQueue]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if queue_ids is not None:
            queue_ids = ",".join(map(str, queue_ids))
            query_parameters['queueIds'] = self._serialize.query('queue_ids', queue_ids, 'str')
        if action_filter is not None:
            query_parameters['actionFilter'] = self._serialize.query('action_filter', action_filter, 'str')
        response = self._send(http_method='GET',
                              location_id='900fa995-c559-4923-aae7-f8424fe4fbea',
                              version='4.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              returns_collection=True)
        return self._deserialize('[TaskAgentQueue]', response)

    def get_agent_queues_by_names(self, queue_names, project=None, action_filter=None):
        """GetAgentQueuesByNames.
        [Preview API]
        :param [str] queue_names:
        :param str project: Project ID or project name
        :param str action_filter:
        :rtype: [TaskAgentQueue]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if queue_names is not None:
            queue_names = ",".join(queue_names)
            query_parameters['queueNames'] = self._serialize.query('queue_names', queue_names, 'str')
        if action_filter is not None:
            query_parameters['actionFilter'] = self._serialize.query('action_filter', action_filter, 'str')
        response = self._send(http_method='GET',
                              location_id='900fa995-c559-4923-aae7-f8424fe4fbea',
                              version='4.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              returns_collection=True)
        return self._deserialize('[TaskAgentQueue]', response)

    def get_task_group_history(self, project, task_group_id):
        """GetTaskGroupHistory.
        [Preview API]
        :param str project: Project ID or project name
        :param str task_group_id:
        :rtype: [TaskGroupRevision]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if task_group_id is not None:
            route_values['taskGroupId'] = self._serialize.url('task_group_id', task_group_id, 'str')
        response = self._send(http_method='GET',
                              location_id='100cc92a-b255-47fa-9ab3-e44a2985a3ac',
                              version='4.1-preview.1',
                              route_values=route_values,
                              returns_collection=True)
        return self._deserialize('[TaskGroupRevision]', response)

    def delete_secure_file(self, project, secure_file_id):
        """DeleteSecureFile.
        [Preview API] Delete a secure file
        :param str project: Project ID or project name
        :param str secure_file_id: The unique secure file Id
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if secure_file_id is not None:
            route_values['secureFileId'] = self._serialize.url('secure_file_id', secure_file_id, 'str')
        self._send(http_method='DELETE',
                   location_id='adcfd8bc-b184-43ba-bd84-7c8c6a2ff421',
                   version='4.1-preview.1',
                   route_values=route_values)

    def download_secure_file(self, project, secure_file_id, ticket, download=None):
        """DownloadSecureFile.
        [Preview API] Download a secure file by Id
        :param str project: Project ID or project name
        :param str secure_file_id: The unique secure file Id
        :param str ticket: A valid download ticket
        :param bool download: If download is true, the file is sent as attachement in the response body. If download is false, the response body contains the file stream.
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if secure_file_id is not None:
            route_values['secureFileId'] = self._serialize.url('secure_file_id', secure_file_id, 'str')
        query_parameters = {}
        if ticket is not None:
            query_parameters['ticket'] = self._serialize.query('ticket', ticket, 'str')
        if download is not None:
            query_parameters['download'] = self._serialize.query('download', download, 'bool')
        response = self._send(http_method='GET',
                              location_id='adcfd8bc-b184-43ba-bd84-7c8c6a2ff421',
                              version='4.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('object', response)

    def get_secure_file(self, project, secure_file_id, include_download_ticket=None, action_filter=None):
        """GetSecureFile.
        [Preview API] Get a secure file
        :param str project: Project ID or project name
        :param str secure_file_id: The unique secure file Id
        :param bool include_download_ticket: If includeDownloadTicket is true and the caller has permissions, a download ticket is included in the response.
        :param str action_filter:
        :rtype: :class:`<SecureFile> <task-agent.v4_1.models.SecureFile>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if secure_file_id is not None:
            route_values['secureFileId'] = self._serialize.url('secure_file_id', secure_file_id, 'str')
        query_parameters = {}
        if include_download_ticket is not None:
            query_parameters['includeDownloadTicket'] = self._serialize.query('include_download_ticket', include_download_ticket, 'bool')
        if action_filter is not None:
            query_parameters['actionFilter'] = self._serialize.query('action_filter', action_filter, 'str')
        response = self._send(http_method='GET',
                              location_id='adcfd8bc-b184-43ba-bd84-7c8c6a2ff421',
                              version='4.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('SecureFile', response)

    def get_secure_files(self, project, name_pattern=None, include_download_tickets=None, action_filter=None):
        """GetSecureFiles.
        [Preview API] Get secure files
        :param str project: Project ID or project name
        :param str name_pattern: Name of the secure file to match. Can include wildcards to match multiple files.
        :param bool include_download_tickets: If includeDownloadTickets is true and the caller has permissions, a download ticket for each secure file is included in the response.
        :param str action_filter: Filter by secure file permissions for View, Manage or Use action. Defaults to View.
        :rtype: [SecureFile]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if name_pattern is not None:
            query_parameters['namePattern'] = self._serialize.query('name_pattern', name_pattern, 'str')
        if include_download_tickets is not None:
            query_parameters['includeDownloadTickets'] = self._serialize.query('include_download_tickets', include_download_tickets, 'bool')
        if action_filter is not None:
            query_parameters['actionFilter'] = self._serialize.query('action_filter', action_filter, 'str')
        response = self._send(http_method='GET',
                              location_id='adcfd8bc-b184-43ba-bd84-7c8c6a2ff421',
                              version='4.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              returns_collection=True)
        return self._deserialize('[SecureFile]', response)

    def get_secure_files_by_ids(self, project, secure_file_ids, include_download_tickets=None, action_filter=None):
        """GetSecureFilesByIds.
        [Preview API] Get secure files
        :param str project: Project ID or project name
        :param [str] secure_file_ids: A list of secure file Ids
        :param bool include_download_tickets: If includeDownloadTickets is true and the caller has permissions, a download ticket for each secure file is included in the response.
        :param str action_filter:
        :rtype: [SecureFile]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if secure_file_ids is not None:
            secure_file_ids = ",".join(secure_file_ids)
            query_parameters['secureFileIds'] = self._serialize.query('secure_file_ids', secure_file_ids, 'str')
        if include_download_tickets is not None:
            query_parameters['includeDownloadTickets'] = self._serialize.query('include_download_tickets', include_download_tickets, 'bool')
        if action_filter is not None:
            query_parameters['actionFilter'] = self._serialize.query('action_filter', action_filter, 'str')
        response = self._send(http_method='GET',
                              location_id='adcfd8bc-b184-43ba-bd84-7c8c6a2ff421',
                              version='4.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              returns_collection=True)
        return self._deserialize('[SecureFile]', response)

    def get_secure_files_by_names(self, project, secure_file_names, include_download_tickets=None, action_filter=None):
        """GetSecureFilesByNames.
        [Preview API] Get secure files
        :param str project: Project ID or project name
        :param [str] secure_file_names: A list of secure file Ids
        :param bool include_download_tickets: If includeDownloadTickets is true and the caller has permissions, a download ticket for each secure file is included in the response.
        :param str action_filter:
        :rtype: [SecureFile]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if secure_file_names is not None:
            secure_file_names = ",".join(secure_file_names)
            query_parameters['secureFileNames'] = self._serialize.query('secure_file_names', secure_file_names, 'str')
        if include_download_tickets is not None:
            query_parameters['includeDownloadTickets'] = self._serialize.query('include_download_tickets', include_download_tickets, 'bool')
        if action_filter is not None:
            query_parameters['actionFilter'] = self._serialize.query('action_filter', action_filter, 'str')
        response = self._send(http_method='GET',
                              location_id='adcfd8bc-b184-43ba-bd84-7c8c6a2ff421',
                              version='4.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              returns_collection=True)
        return self._deserialize('[SecureFile]', response)

    def query_secure_files_by_properties(self, condition, project, name_pattern=None):
        """QuerySecureFilesByProperties.
        [Preview API] Query secure files using a name pattern and a condition on file properties.
        :param str condition: The main condition syntax is described [here](https://go.microsoft.com/fwlink/?linkid=842996). Use the *property('property-name')* function to access the value of the specified property of a secure file. It returns null if the property is not set. E.g. ``` and( eq( property('devices'), '2' ), in( property('provisioning profile type'), 'ad hoc', 'development' ) ) ```
        :param str project: Project ID or project name
        :param str name_pattern: Name of the secure file to match. Can include wildcards to match multiple files.
        :rtype: [SecureFile]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if name_pattern is not None:
            query_parameters['namePattern'] = self._serialize.query('name_pattern', name_pattern, 'str')
        content = self._serialize.body(condition, 'str')
        response = self._send(http_method='POST',
                              location_id='adcfd8bc-b184-43ba-bd84-7c8c6a2ff421',
                              version='4.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content,
                              returns_collection=True)
        return self._deserialize('[SecureFile]', response)

    def update_secure_file(self, secure_file, project, secure_file_id):
        """UpdateSecureFile.
        [Preview API] Update the name or properties of an existing secure file
        :param :class:`<SecureFile> <task-agent.v4_1.models.SecureFile>` secure_file: The secure file with updated name and/or properties
        :param str project: Project ID or project name
        :param str secure_file_id: The unique secure file Id
        :rtype: :class:`<SecureFile> <task-agent.v4_1.models.SecureFile>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if secure_file_id is not None:
            route_values['secureFileId'] = self._serialize.url('secure_file_id', secure_file_id, 'str')
        content = self._serialize.body(secure_file, 'SecureFile')
        response = self._send(http_method='PATCH',
                              location_id='adcfd8bc-b184-43ba-bd84-7c8c6a2ff421',
                              version='4.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('SecureFile', response)

    def update_secure_files(self, secure_files, project):
        """UpdateSecureFiles.
        [Preview API] Update properties and/or names of a set of secure files. Files are identified by their IDs. Properties provided override the existing one entirely, i.e. do not merge.
        :param [SecureFile] secure_files: A list of secure file objects. Only three field must be populated Id, Name, and Properties. The rest of fields in the object are ignored.
        :param str project: Project ID or project name
        :rtype: [SecureFile]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(secure_files, '[SecureFile]')
        response = self._send(http_method='PATCH',
                              location_id='adcfd8bc-b184-43ba-bd84-7c8c6a2ff421',
                              version='4.1-preview.1',
                              route_values=route_values,
                              content=content,
                              returns_collection=True)
        return self._deserialize('[SecureFile]', response)

    def upload_secure_file(self, upload_stream, project, name):
        """UploadSecureFile.
        [Preview API] Upload a secure file, include the file stream in the request body
        :param object upload_stream: Stream to upload
        :param str project: Project ID or project name
        :param str name: Name of the file to upload
        :rtype: :class:`<SecureFile> <task-agent.v4_1.models.SecureFile>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if name is not None:
            query_parameters['name'] = self._serialize.query('name', name, 'str')
        content = self._serialize.body(upload_stream, 'object')
        response = self._send(http_method='POST',
                              location_id='adcfd8bc-b184-43ba-bd84-7c8c6a2ff421',
                              version='4.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content,
                              media_type='application/octet-stream')
        return self._deserialize('SecureFile', response)

    def execute_service_endpoint_request(self, service_endpoint_request, project, endpoint_id):
        """ExecuteServiceEndpointRequest.
        [Preview API]
        :param :class:`<ServiceEndpointRequest> <task-agent.v4_1.models.ServiceEndpointRequest>` service_endpoint_request:
        :param str project: Project ID or project name
        :param str endpoint_id:
        :rtype: :class:`<ServiceEndpointRequestResult> <task-agent.v4_1.models.ServiceEndpointRequestResult>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if endpoint_id is not None:
            query_parameters['endpointId'] = self._serialize.query('endpoint_id', endpoint_id, 'str')
        content = self._serialize.body(service_endpoint_request, 'ServiceEndpointRequest')
        response = self._send(http_method='POST',
                              location_id='f956a7de-d766-43af-81b1-e9e349245634',
                              version='4.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('ServiceEndpointRequestResult', response)

    def create_service_endpoint(self, endpoint, project):
        """CreateServiceEndpoint.
        [Preview API]
        :param :class:`<ServiceEndpoint> <task-agent.v4_1.models.ServiceEndpoint>` endpoint:
        :param str project: Project ID or project name
        :rtype: :class:`<ServiceEndpoint> <task-agent.v4_1.models.ServiceEndpoint>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(endpoint, 'ServiceEndpoint')
        response = self._send(http_method='POST',
                              location_id='dca61d2f-3444-410a-b5ec-db2fc4efb4c5',
                              version='4.1-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('ServiceEndpoint', response)

    def delete_service_endpoint(self, project, endpoint_id):
        """DeleteServiceEndpoint.
        [Preview API]
        :param str project: Project ID or project name
        :param str endpoint_id:
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if endpoint_id is not None:
            route_values['endpointId'] = self._serialize.url('endpoint_id', endpoint_id, 'str')
        self._send(http_method='DELETE',
                   location_id='dca61d2f-3444-410a-b5ec-db2fc4efb4c5',
                   version='4.1-preview.2',
                   route_values=route_values)

    def get_service_endpoint_details(self, project, endpoint_id):
        """GetServiceEndpointDetails.
        [Preview API]
        :param str project: Project ID or project name
        :param str endpoint_id:
        :rtype: :class:`<ServiceEndpoint> <task-agent.v4_1.models.ServiceEndpoint>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if endpoint_id is not None:
            route_values['endpointId'] = self._serialize.url('endpoint_id', endpoint_id, 'str')
        response = self._send(http_method='GET',
                              location_id='dca61d2f-3444-410a-b5ec-db2fc4efb4c5',
                              version='4.1-preview.2',
                              route_values=route_values)
        return self._deserialize('ServiceEndpoint', response)

    def get_service_endpoints(self, project, type=None, auth_schemes=None, endpoint_ids=None, include_failed=None):
        """GetServiceEndpoints.
        [Preview API]
        :param str project: Project ID or project name
        :param str type:
        :param [str] auth_schemes:
        :param [str] endpoint_ids:
        :param bool include_failed:
        :rtype: [ServiceEndpoint]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if type is not None:
            query_parameters['type'] = self._serialize.query('type', type, 'str')
        if auth_schemes is not None:
            auth_schemes = ",".join(auth_schemes)
            query_parameters['authSchemes'] = self._serialize.query('auth_schemes', auth_schemes, 'str')
        if endpoint_ids is not None:
            endpoint_ids = ",".join(endpoint_ids)
            query_parameters['endpointIds'] = self._serialize.query('endpoint_ids', endpoint_ids, 'str')
        if include_failed is not None:
            query_parameters['includeFailed'] = self._serialize.query('include_failed', include_failed, 'bool')
        response = self._send(http_method='GET',
                              location_id='dca61d2f-3444-410a-b5ec-db2fc4efb4c5',
                              version='4.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              returns_collection=True)
        return self._deserialize('[ServiceEndpoint]', response)

    def get_service_endpoints_by_names(self, project, endpoint_names, type=None, auth_schemes=None, include_failed=None):
        """GetServiceEndpointsByNames.
        [Preview API]
        :param str project: Project ID or project name
        :param [str] endpoint_names:
        :param str type:
        :param [str] auth_schemes:
        :param bool include_failed:
        :rtype: [ServiceEndpoint]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if endpoint_names is not None:
            endpoint_names = ",".join(endpoint_names)
            query_parameters['endpointNames'] = self._serialize.query('endpoint_names', endpoint_names, 'str')
        if type is not None:
            query_parameters['type'] = self._serialize.query('type', type, 'str')
        if auth_schemes is not None:
            auth_schemes = ",".join(auth_schemes)
            query_parameters['authSchemes'] = self._serialize.query('auth_schemes', auth_schemes, 'str')
        if include_failed is not None:
            query_parameters['includeFailed'] = self._serialize.query('include_failed', include_failed, 'bool')
        response = self._send(http_method='GET',
                              location_id='dca61d2f-3444-410a-b5ec-db2fc4efb4c5',
                              version='4.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              returns_collection=True)
        return self._deserialize('[ServiceEndpoint]', response)

    def update_service_endpoint(self, endpoint, project, endpoint_id, operation=None):
        """UpdateServiceEndpoint.
        [Preview API]
        :param :class:`<ServiceEndpoint> <task-agent.v4_1.models.ServiceEndpoint>` endpoint:
        :param str project: Project ID or project name
        :param str endpoint_id:
        :param str operation:
        :rtype: :class:`<ServiceEndpoint> <task-agent.v4_1.models.ServiceEndpoint>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if endpoint_id is not None:
            route_values['endpointId'] = self._serialize.url('endpoint_id', endpoint_id, 'str')
        query_parameters = {}
        if operation is not None:
            query_parameters['operation'] = self._serialize.query('operation', operation, 'str')
        content = self._serialize.body(endpoint, 'ServiceEndpoint')
        response = self._send(http_method='PUT',
                              location_id='dca61d2f-3444-410a-b5ec-db2fc4efb4c5',
                              version='4.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('ServiceEndpoint', response)

    def update_service_endpoints(self, endpoints, project):
        """UpdateServiceEndpoints.
        [Preview API]
        :param [ServiceEndpoint] endpoints:
        :param str project: Project ID or project name
        :rtype: [ServiceEndpoint]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(endpoints, '[ServiceEndpoint]')
        response = self._send(http_method='PUT',
                              location_id='dca61d2f-3444-410a-b5ec-db2fc4efb4c5',
                              version='4.1-preview.2',
                              route_values=route_values,
                              content=content,
                              returns_collection=True)
        return self._deserialize('[ServiceEndpoint]', response)

    def get_service_endpoint_types(self, type=None, scheme=None):
        """GetServiceEndpointTypes.
        [Preview API]
        :param str type:
        :param str scheme:
        :rtype: [ServiceEndpointType]
        """
        query_parameters = {}
        if type is not None:
            query_parameters['type'] = self._serialize.query('type', type, 'str')
        if scheme is not None:
            query_parameters['scheme'] = self._serialize.query('scheme', scheme, 'str')
        response = self._send(http_method='GET',
                              location_id='7c74af83-8605-45c1-a30b-7a05d5d7f8c1',
                              version='4.1-preview.1',
                              query_parameters=query_parameters,
                              returns_collection=True)
        return self._deserialize('[ServiceEndpointType]', response)

    def add_deployment_target(self, machine, project, deployment_group_id):
        """AddDeploymentTarget.
        [Preview API]
        :param :class:`<DeploymentMachine> <task-agent.v4_1.models.DeploymentMachine>` machine:
        :param str project: Project ID or project name
        :param int deployment_group_id:
        :rtype: :class:`<DeploymentMachine> <task-agent.v4_1.models.DeploymentMachine>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if deployment_group_id is not None:
            route_values['deploymentGroupId'] = self._serialize.url('deployment_group_id', deployment_group_id, 'int')
        content = self._serialize.body(machine, 'DeploymentMachine')
        response = self._send(http_method='POST',
                              location_id='2f0aa599-c121-4256-a5fd-ba370e0ae7b6',
                              version='4.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('DeploymentMachine', response)

    def delete_deployment_target(self, project, deployment_group_id, target_id):
        """DeleteDeploymentTarget.
        [Preview API]
        :param str project: Project ID or project name
        :param int deployment_group_id:
        :param int target_id:
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if deployment_group_id is not None:
            route_values['deploymentGroupId'] = self._serialize.url('deployment_group_id', deployment_group_id, 'int')
        if target_id is not None:
            route_values['targetId'] = self._serialize.url('target_id', target_id, 'int')
        self._send(http_method='DELETE',
                   location_id='2f0aa599-c121-4256-a5fd-ba370e0ae7b6',
                   version='4.1-preview.1',
                   route_values=route_values)

    def get_deployment_target(self, project, deployment_group_id, target_id, expand=None):
        """GetDeploymentTarget.
        [Preview API]
        :param str project: Project ID or project name
        :param int deployment_group_id:
        :param int target_id:
        :param str expand:
        :rtype: :class:`<DeploymentMachine> <task-agent.v4_1.models.DeploymentMachine>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if deployment_group_id is not None:
            route_values['deploymentGroupId'] = self._serialize.url('deployment_group_id', deployment_group_id, 'int')
        if target_id is not None:
            route_values['targetId'] = self._serialize.url('target_id', target_id, 'int')
        query_parameters = {}
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='2f0aa599-c121-4256-a5fd-ba370e0ae7b6',
                              version='4.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('DeploymentMachine', response)

    def get_deployment_targets(self, project, deployment_group_id, tags=None, name=None, partial_name_match=None, expand=None, agent_status=None, agent_job_result=None, continuation_token=None, top=None):
        """GetDeploymentTargets.
        [Preview API]
        :param str project: Project ID or project name
        :param int deployment_group_id:
        :param [str] tags:
        :param str name:
        :param bool partial_name_match:
        :param str expand:
        :param str agent_status:
        :param str agent_job_result:
        :param str continuation_token:
        :param int top:
        :rtype: [DeploymentMachine]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if deployment_group_id is not None:
            route_values['deploymentGroupId'] = self._serialize.url('deployment_group_id', deployment_group_id, 'int')
        query_parameters = {}
        if tags is not None:
            tags = ",".join(tags)
            query_parameters['tags'] = self._serialize.query('tags', tags, 'str')
        if name is not None:
            query_parameters['name'] = self._serialize.query('name', name, 'str')
        if partial_name_match is not None:
            query_parameters['partialNameMatch'] = self._serialize.query('partial_name_match', partial_name_match, 'bool')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        if agent_status is not None:
            query_parameters['agentStatus'] = self._serialize.query('agent_status', agent_status, 'str')
        if agent_job_result is not None:
            query_parameters['agentJobResult'] = self._serialize.query('agent_job_result', agent_job_result, 'str')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        response = self._send(http_method='GET',
                              location_id='2f0aa599-c121-4256-a5fd-ba370e0ae7b6',
                              version='4.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              returns_collection=True)
        return self._deserialize('[DeploymentMachine]', response)

    def replace_deployment_target(self, machine, project, deployment_group_id, target_id):
        """ReplaceDeploymentTarget.
        [Preview API]
        :param :class:`<DeploymentMachine> <task-agent.v4_1.models.DeploymentMachine>` machine:
        :param str project: Project ID or project name
        :param int deployment_group_id:
        :param int target_id:
        :rtype: :class:`<DeploymentMachine> <task-agent.v4_1.models.DeploymentMachine>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if deployment_group_id is not None:
            route_values['deploymentGroupId'] = self._serialize.url('deployment_group_id', deployment_group_id, 'int')
        if target_id is not None:
            route_values['targetId'] = self._serialize.url('target_id', target_id, 'int')
        content = self._serialize.body(machine, 'DeploymentMachine')
        response = self._send(http_method='PUT',
                              location_id='2f0aa599-c121-4256-a5fd-ba370e0ae7b6',
                              version='4.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('DeploymentMachine', response)

    def update_deployment_target(self, machine, project, deployment_group_id, target_id):
        """UpdateDeploymentTarget.
        [Preview API]
        :param :class:`<DeploymentMachine> <task-agent.v4_1.models.DeploymentMachine>` machine:
        :param str project: Project ID or project name
        :param int deployment_group_id:
        :param int target_id:
        :rtype: :class:`<DeploymentMachine> <task-agent.v4_1.models.DeploymentMachine>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if deployment_group_id is not None:
            route_values['deploymentGroupId'] = self._serialize.url('deployment_group_id', deployment_group_id, 'int')
        if target_id is not None:
            route_values['targetId'] = self._serialize.url('target_id', target_id, 'int')
        content = self._serialize.body(machine, 'DeploymentMachine')
        response = self._send(http_method='PATCH',
                              location_id='2f0aa599-c121-4256-a5fd-ba370e0ae7b6',
                              version='4.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('DeploymentMachine', response)

    def update_deployment_targets(self, machines, project, deployment_group_id):
        """UpdateDeploymentTargets.
        [Preview API]
        :param [DeploymentMachine] machines:
        :param str project: Project ID or project name
        :param int deployment_group_id:
        :rtype: [DeploymentMachine]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if deployment_group_id is not None:
            route_values['deploymentGroupId'] = self._serialize.url('deployment_group_id', deployment_group_id, 'int')
        content = self._serialize.body(machines, '[DeploymentMachine]')
        response = self._send(http_method='PATCH',
                              location_id='2f0aa599-c121-4256-a5fd-ba370e0ae7b6',
                              version='4.1-preview.1',
                              route_values=route_values,
                              content=content,
                              returns_collection=True)
        return self._deserialize('[DeploymentMachine]', response)

    def add_task_group(self, task_group, project):
        """AddTaskGroup.
        [Preview API] Create a task group.
        :param :class:`<TaskGroupCreateParameter> <task-agent.v4_1.models.TaskGroupCreateParameter>` task_group: Task group object to create.
        :param str project: Project ID or project name
        :rtype: :class:`<TaskGroup> <task-agent.v4_1.models.TaskGroup>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(task_group, 'TaskGroupCreateParameter')
        response = self._send(http_method='POST',
                              location_id='6c08ffbf-dbf1-4f9a-94e5-a1cbd47005e7',
                              version='4.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TaskGroup', response)

    def delete_task_group(self, project, task_group_id, comment=None):
        """DeleteTaskGroup.
        [Preview API] Delete a task group.
        :param str project: Project ID or project name
        :param str task_group_id: Id of the task group to be deleted.
        :param str comment: Comments to delete.
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if task_group_id is not None:
            route_values['taskGroupId'] = self._serialize.url('task_group_id', task_group_id, 'str')
        query_parameters = {}
        if comment is not None:
            query_parameters['comment'] = self._serialize.query('comment', comment, 'str')
        self._send(http_method='DELETE',
                   location_id='6c08ffbf-dbf1-4f9a-94e5-a1cbd47005e7',
                   version='4.1-preview.1',
                   route_values=route_values,
                   query_parameters=query_parameters)

    def get_task_groups(self, project, task_group_id=None, expanded=None, task_id_filter=None, deleted=None):
        """GetTaskGroups.
        [Preview API] Get a list of task groups.
        :param str project: Project ID or project name
        :param str task_group_id: Id of the task group.
        :param bool expanded: 'true' to recursively expand task groups. Default is 'false'.
        :param str task_id_filter: Guid of the taskId to filter.
        :param bool deleted: 'true'to include deleted task groups. Default is 'false'.
        :rtype: [TaskGroup]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if task_group_id is not None:
            route_values['taskGroupId'] = self._serialize.url('task_group_id', task_group_id, 'str')
        query_parameters = {}
        if expanded is not None:
            query_parameters['expanded'] = self._serialize.query('expanded', expanded, 'bool')
        if task_id_filter is not None:
            query_parameters['taskIdFilter'] = self._serialize.query('task_id_filter', task_id_filter, 'str')
        if deleted is not None:
            query_parameters['deleted'] = self._serialize.query('deleted', deleted, 'bool')
        response = self._send(http_method='GET',
                              location_id='6c08ffbf-dbf1-4f9a-94e5-a1cbd47005e7',
                              version='4.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              returns_collection=True)
        return self._deserialize('[TaskGroup]', response)

    def update_task_group(self, task_group, project, task_group_id=None):
        """UpdateTaskGroup.
        [Preview API] Update a task group.
        :param :class:`<TaskGroupUpdateParameter> <task-agent.v4_1.models.TaskGroupUpdateParameter>` task_group: Task group to update.
        :param str project: Project ID or project name
        :param str task_group_id: Id of the task group to update.
        :rtype: :class:`<TaskGroup> <task-agent.v4_1.models.TaskGroup>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if task_group_id is not None:
            route_values['taskGroupId'] = self._serialize.url('task_group_id', task_group_id, 'str')
        content = self._serialize.body(task_group, 'TaskGroupUpdateParameter')
        response = self._send(http_method='PUT',
                              location_id='6c08ffbf-dbf1-4f9a-94e5-a1cbd47005e7',
                              version='4.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TaskGroup', response)

    def delete_task_definition(self, task_id):
        """DeleteTaskDefinition.
        [Preview API]
        :param str task_id:
        """
        route_values = {}
        if task_id is not None:
            route_values['taskId'] = self._serialize.url('task_id', task_id, 'str')
        self._send(http_method='DELETE',
                   location_id='60aac929-f0cd-4bc8-9ce4-6b30e8f1b1bd',
                   version='4.1-preview.1',
                   route_values=route_values)

    def get_task_content_zip(self, task_id, version_string, visibility=None, scope_local=None):
        """GetTaskContentZip.
        [Preview API]
        :param str task_id:
        :param str version_string:
        :param [str] visibility:
        :param bool scope_local:
        :rtype: object
        """
        route_values = {}
        if task_id is not None:
            route_values['taskId'] = self._serialize.url('task_id', task_id, 'str')
        if version_string is not None:
            route_values['versionString'] = self._serialize.url('version_string', version_string, 'str')
        query_parameters = {}
        if visibility is not None:
            query_parameters['visibility'] = self._serialize.query('visibility', visibility, '[str]')
        if scope_local is not None:
            query_parameters['scopeLocal'] = self._serialize.query('scope_local', scope_local, 'bool')
        response = self._send(http_method='GET',
                              location_id='60aac929-f0cd-4bc8-9ce4-6b30e8f1b1bd',
                              version='4.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('object', response)

    def get_task_definition(self, task_id, version_string, visibility=None, scope_local=None):
        """GetTaskDefinition.
        [Preview API]
        :param str task_id:
        :param str version_string:
        :param [str] visibility:
        :param bool scope_local:
        :rtype: :class:`<TaskDefinition> <task-agent.v4_1.models.TaskDefinition>`
        """
        route_values = {}
        if task_id is not None:
            route_values['taskId'] = self._serialize.url('task_id', task_id, 'str')
        if version_string is not None:
            route_values['versionString'] = self._serialize.url('version_string', version_string, 'str')
        query_parameters = {}
        if visibility is not None:
            query_parameters['visibility'] = self._serialize.query('visibility', visibility, '[str]')
        if scope_local is not None:
            query_parameters['scopeLocal'] = self._serialize.query('scope_local', scope_local, 'bool')
        response = self._send(http_method='GET',
                              location_id='60aac929-f0cd-4bc8-9ce4-6b30e8f1b1bd',
                              version='4.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TaskDefinition', response)

    def get_task_definitions(self, task_id=None, visibility=None, scope_local=None):
        """GetTaskDefinitions.
        [Preview API]
        :param str task_id:
        :param [str] visibility:
        :param bool scope_local:
        :rtype: [TaskDefinition]
        """
        route_values = {}
        if task_id is not None:
            route_values['taskId'] = self._serialize.url('task_id', task_id, 'str')
        query_parameters = {}
        if visibility is not None:
            query_parameters['visibility'] = self._serialize.query('visibility', visibility, '[str]')
        if scope_local is not None:
            query_parameters['scopeLocal'] = self._serialize.query('scope_local', scope_local, 'bool')
        response = self._send(http_method='GET',
                              location_id='60aac929-f0cd-4bc8-9ce4-6b30e8f1b1bd',
                              version='4.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              returns_collection=True)
        return self._deserialize('[TaskDefinition]', response)

    def update_agent_update_state(self, pool_id, agent_id, current_state):
        """UpdateAgentUpdateState.
        [Preview API]
        :param int pool_id:
        :param int agent_id:
        :param str current_state:
        :rtype: :class:`<TaskAgent> <task-agent.v4_1.models.TaskAgent>`
        """
        route_values = {}
        if pool_id is not None:
            route_values['poolId'] = self._serialize.url('pool_id', pool_id, 'int')
        if agent_id is not None:
            route_values['agentId'] = self._serialize.url('agent_id', agent_id, 'int')
        query_parameters = {}
        if current_state is not None:
            query_parameters['currentState'] = self._serialize.query('current_state', current_state, 'str')
        response = self._send(http_method='PUT',
                              location_id='8cc1b02b-ae49-4516-b5ad-4f9b29967c30',
                              version='4.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TaskAgent', response)

    def update_agent_user_capabilities(self, user_capabilities, pool_id, agent_id):
        """UpdateAgentUserCapabilities.
        [Preview API]
        :param {str} user_capabilities:
        :param int pool_id:
        :param int agent_id:
        :rtype: :class:`<TaskAgent> <task-agent.v4_1.models.TaskAgent>`
        """
        route_values = {}
        if pool_id is not None:
            route_values['poolId'] = self._serialize.url('pool_id', pool_id, 'int')
        if agent_id is not None:
            route_values['agentId'] = self._serialize.url('agent_id', agent_id, 'int')
        content = self._serialize.body(user_capabilities, '{str}')
        response = self._send(http_method='PUT',
                              location_id='30ba3ada-fedf-4da8-bbb5-dacf2f82e176',
                              version='4.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TaskAgent', response)

    def add_variable_group(self, group, project):
        """AddVariableGroup.
        [Preview API]
        :param :class:`<VariableGroup> <task-agent.v4_1.models.VariableGroup>` group:
        :param str project: Project ID or project name
        :rtype: :class:`<VariableGroup> <task-agent.v4_1.models.VariableGroup>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(group, 'VariableGroup')
        response = self._send(http_method='POST',
                              location_id='f5b09dd5-9d54-45a1-8b5a-1c8287d634cc',
                              version='4.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('VariableGroup', response)

    def delete_variable_group(self, project, group_id):
        """DeleteVariableGroup.
        [Preview API]
        :param str project: Project ID or project name
        :param int group_id:
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if group_id is not None:
            route_values['groupId'] = self._serialize.url('group_id', group_id, 'int')
        self._send(http_method='DELETE',
                   location_id='f5b09dd5-9d54-45a1-8b5a-1c8287d634cc',
                   version='4.1-preview.1',
                   route_values=route_values)

    def get_variable_group(self, project, group_id):
        """GetVariableGroup.
        [Preview API]
        :param str project: Project ID or project name
        :param int group_id:
        :rtype: :class:`<VariableGroup> <task-agent.v4_1.models.VariableGroup>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if group_id is not None:
            route_values['groupId'] = self._serialize.url('group_id', group_id, 'int')
        response = self._send(http_method='GET',
                              location_id='f5b09dd5-9d54-45a1-8b5a-1c8287d634cc',
                              version='4.1-preview.1',
                              route_values=route_values)
        return self._deserialize('VariableGroup', response)

    def get_variable_groups(self, project, group_name=None, action_filter=None):
        """GetVariableGroups.
        [Preview API]
        :param str project: Project ID or project name
        :param str group_name:
        :param str action_filter:
        :rtype: [VariableGroup]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if group_name is not None:
            query_parameters['groupName'] = self._serialize.query('group_name', group_name, 'str')
        if action_filter is not None:
            query_parameters['actionFilter'] = self._serialize.query('action_filter', action_filter, 'str')
        response = self._send(http_method='GET',
                              location_id='f5b09dd5-9d54-45a1-8b5a-1c8287d634cc',
                              version='4.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              returns_collection=True)
        return self._deserialize('[VariableGroup]', response)

    def get_variable_groups_by_id(self, project, group_ids):
        """GetVariableGroupsById.
        [Preview API]
        :param str project: Project ID or project name
        :param [int] group_ids:
        :rtype: [VariableGroup]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if group_ids is not None:
            group_ids = ",".join(map(str, group_ids))
            query_parameters['groupIds'] = self._serialize.query('group_ids', group_ids, 'str')
        response = self._send(http_method='GET',
                              location_id='f5b09dd5-9d54-45a1-8b5a-1c8287d634cc',
                              version='4.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              returns_collection=True)
        return self._deserialize('[VariableGroup]', response)

    def update_variable_group(self, group, project, group_id):
        """UpdateVariableGroup.
        [Preview API]
        :param :class:`<VariableGroup> <task-agent.v4_1.models.VariableGroup>` group:
        :param str project: Project ID or project name
        :param int group_id:
        :rtype: :class:`<VariableGroup> <task-agent.v4_1.models.VariableGroup>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if group_id is not None:
            route_values['groupId'] = self._serialize.url('group_id', group_id, 'int')
        content = self._serialize.body(group, 'VariableGroup')
        response = self._send(http_method='PUT',
                              location_id='f5b09dd5-9d54-45a1-8b5a-1c8287d634cc',
                              version='4.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('VariableGroup', response)

    def acquire_access_token(self, authentication_request):
        """AcquireAccessToken.
        [Preview API]
        :param :class:`<AadOauthTokenRequest> <task-agent.v4_1.models.AadOauthTokenRequest>` authentication_request:
        :rtype: :class:`<AadOauthTokenResult> <task-agent.v4_1.models.AadOauthTokenResult>`
        """
        content = self._serialize.body(authentication_request, 'AadOauthTokenRequest')
        response = self._send(http_method='POST',
                              location_id='9c63205e-3a0f-42a0-ad88-095200f13607',
                              version='4.1-preview.1',
                              content=content)
        return self._deserialize('AadOauthTokenResult', response)

    def create_aad_oAuth_request(self, tenant_id, redirect_uri, prompt_option=None, complete_callback_payload=None):
        """CreateAadOAuthRequest.
        [Preview API]
        :param str tenant_id:
        :param str redirect_uri:
        :param str prompt_option:
        :param str complete_callback_payload:
        :rtype: str
        """
        query_parameters = {}
        if tenant_id is not None:
            query_parameters['tenantId'] = self._serialize.query('tenant_id', tenant_id, 'str')
        if redirect_uri is not None:
            query_parameters['redirectUri'] = self._serialize.query('redirect_uri', redirect_uri, 'str')
        if prompt_option is not None:
            query_parameters['promptOption'] = self._serialize.query('prompt_option', prompt_option, 'str')
        if complete_callback_payload is not None:
            query_parameters['completeCallbackPayload'] = self._serialize.query('complete_callback_payload', complete_callback_payload, 'str')
        response = self._send(http_method='POST',
                              location_id='9c63205e-3a0f-42a0-ad88-095200f13607',
                              version='4.1-preview.1',
                              query_parameters=query_parameters)
        return self._deserialize('str', response)

    def get_vsts_aad_tenant_id(self):
        """GetVstsAadTenantId.
        [Preview API]
        :rtype: str
        """
        response = self._send(http_method='GET',
                              location_id='9c63205e-3a0f-42a0-ad88-095200f13607',
                              version='4.1-preview.1')
        return self._deserialize('str', response)

