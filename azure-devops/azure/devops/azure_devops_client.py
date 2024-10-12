# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.core import PipelineClient
from azure.core.pipeline.policies import UserAgentPolicy, HeadersPolicy
from .version import VERSION


class AzureDevOpsClient(PipelineClient):
    def __init__(self, base_url=None, credentials=None, user_agent=None):
        if not base_url:
            raise ValueError('base_url is required.')
        if not credentials:
            raise ValueError('credentials is required.')
        base_url = base_url.rstrip('/')
        user_agent_policy = UserAgentPolicy('azure-devops/{}'.format(VERSION))
        if user_agent is not None:
            user_agent_policy.add_user_agent(user_agent)
        headers_policy = HeadersPolicy()
        headers_policy.add_header('Authentication', credentials)
        policies = [user_agent_policy, headers_policy]
        super(AzureDevOpsClient, self).__init__(base_url=base_url, policies=policies)
