# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from . import models


class ElasticClient(Client):
    """Elastic
    :param str base_url: Service URL
    :param Authentication creds: Authenticated credentials.
    """

    def __init__(self, base_url=None, creds=None):
        super(ElasticClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = None

    def get_elastic_pool_logs(self, pool_id, top=None):
        """GetElasticPoolLogs.
        Get elastic pool diagnostics logs for a specified Elastic Pool.
        :param int pool_id: Pool Id of the Elastic Pool
        :param int top: Number of elastic pool logs to retrieve
        :rtype: [ElasticPoolLog]
        """
        route_values = {}
        if pool_id is not None:
            route_values['poolId'] = self._serialize.url('pool_id', pool_id, 'int')
        query_parameters = {}
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        response = self._send(http_method='GET',
                              location_id='595b1769-61d5-4076-a72a-98a02105ca9a',
                              version='7.0',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[ElasticPoolLog]', self._unwrap_collection(response))

    def create_elastic_pool(self, elastic_pool, pool_name, authorize_all_pipelines=None, auto_provision_project_pools=None, project_id=None):
        """CreateElasticPool.
        Create a new elastic pool. This will create a new TaskAgentPool at the organization level. If a project id is provided, this will create a new TaskAgentQueue in the specified project.
        :param :class:`<ElasticPool> <azure.devops.v7_0.elastic.models.ElasticPool>` elastic_pool: Elastic pool to create. Contains the properties necessary for configuring a new ElasticPool.
        :param str pool_name: Name to use for the new TaskAgentPool
        :param bool authorize_all_pipelines: Setting to determine if all pipelines are authorized to use this TaskAgentPool by default.
        :param bool auto_provision_project_pools: Setting to automatically provision TaskAgentQueues in every project for the new pool.
        :param str project_id: Optional: If provided, a new TaskAgentQueue will be created in the specified project.
        :rtype: :class:`<ElasticPoolCreationResult> <azure.devops.v7_0.elastic.models.ElasticPoolCreationResult>`
        """
        query_parameters = {}
        if pool_name is not None:
            query_parameters['poolName'] = self._serialize.query('pool_name', pool_name, 'str')
        if authorize_all_pipelines is not None:
            query_parameters['authorizeAllPipelines'] = self._serialize.query('authorize_all_pipelines', authorize_all_pipelines, 'bool')
        if auto_provision_project_pools is not None:
            query_parameters['autoProvisionProjectPools'] = self._serialize.query('auto_provision_project_pools', auto_provision_project_pools, 'bool')
        if project_id is not None:
            query_parameters['projectId'] = self._serialize.query('project_id', project_id, 'str')
        content = self._serialize.body(elastic_pool, 'ElasticPool')
        response = self._send(http_method='POST',
                              location_id='dd3c938f-835b-4971-b99a-db75a47aad43',
                              version='7.0',
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('ElasticPoolCreationResult', response)

    def get_elastic_pool(self, pool_id):
        """GetElasticPool.
        Returns the Elastic Pool with the specified Pool Id.
        :param int pool_id: Pool Id of the associated TaskAgentPool
        :rtype: :class:`<ElasticPool> <azure.devops.v7_0.elastic.models.ElasticPool>`
        """
        route_values = {}
        if pool_id is not None:
            route_values['poolId'] = self._serialize.url('pool_id', pool_id, 'int')
        response = self._send(http_method='GET',
                              location_id='dd3c938f-835b-4971-b99a-db75a47aad43',
                              version='7.0',
                              route_values=route_values)
        return self._deserialize('ElasticPool', response)

    def get_elastic_pools(self):
        """GetElasticPools.
        Get a list of all Elastic Pools.
        :rtype: [ElasticPool]
        """
        response = self._send(http_method='GET',
                              location_id='dd3c938f-835b-4971-b99a-db75a47aad43',
                              version='7.0')
        return self._deserialize('[ElasticPool]', self._unwrap_collection(response))

    def update_elastic_pool(self, elastic_pool_settings, pool_id):
        """UpdateElasticPool.
        Update settings on a specified Elastic Pool.
        :param :class:`<ElasticPoolSettings> <azure.devops.v7_0.elastic.models.ElasticPoolSettings>` elastic_pool_settings: New Elastic Pool settings data
        :param int pool_id:
        :rtype: :class:`<ElasticPool> <azure.devops.v7_0.elastic.models.ElasticPool>`
        """
        route_values = {}
        if pool_id is not None:
            route_values['poolId'] = self._serialize.url('pool_id', pool_id, 'int')
        content = self._serialize.body(elastic_pool_settings, 'ElasticPoolSettings')
        response = self._send(http_method='PATCH',
                              location_id='dd3c938f-835b-4971-b99a-db75a47aad43',
                              version='7.0',
                              route_values=route_values,
                              content=content)
        return self._deserialize('ElasticPool', response)

    def get_elastic_nodes(self, pool_id, state=None):
        """GetElasticNodes.
        Get a list of ElasticNodes currently in the ElasticPool
        :param int pool_id: Pool id of the ElasticPool
        :param str state: Optional: Filter to only retrieve ElasticNodes in the given ElasticNodeState
        :rtype: [ElasticNode]
        """
        route_values = {}
        if pool_id is not None:
            route_values['poolId'] = self._serialize.url('pool_id', pool_id, 'int')
        query_parameters = {}
        if state is not None:
            query_parameters['$state'] = self._serialize.query('state', state, 'str')
        response = self._send(http_method='GET',
                              location_id='1b232402-5ff0-42ad-9703-d76497835eb6',
                              version='7.0',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[ElasticNode]', self._unwrap_collection(response))

    def update_elastic_node(self, elastic_node_settings, pool_id, elastic_node_id):
        """UpdateElasticNode.
        Update properties on a specified ElasticNode
        :param :class:`<ElasticNodeSettings> <azure.devops.v7_0.elastic.models.ElasticNodeSettings>` elastic_node_settings:
        :param int pool_id:
        :param int elastic_node_id:
        :rtype: :class:`<ElasticNode> <azure.devops.v7_0.elastic.models.ElasticNode>`
        """
        route_values = {}
        if pool_id is not None:
            route_values['poolId'] = self._serialize.url('pool_id', pool_id, 'int')
        if elastic_node_id is not None:
            route_values['elasticNodeId'] = self._serialize.url('elastic_node_id', elastic_node_id, 'int')
        content = self._serialize.body(elastic_node_settings, 'ElasticNodeSettings')
        response = self._send(http_method='PATCH',
                              location_id='1b232402-5ff0-42ad-9703-d76497835eb6',
                              version='7.0',
                              route_values=route_values,
                              content=content)
        return self._deserialize('ElasticNode', response)

