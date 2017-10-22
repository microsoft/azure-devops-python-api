# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class BuildResourceUsage(Model):
    """BuildResourceUsage.

    :param distributed_task_agents:
    :type distributed_task_agents: int
    :param paid_private_agent_slots:
    :type paid_private_agent_slots: int
    :param total_usage:
    :type total_usage: int
    :param xaml_controllers:
    :type xaml_controllers: int
    """

    _attribute_map = {
        'distributed_task_agents': {'key': 'distributedTaskAgents', 'type': 'int'},
        'paid_private_agent_slots': {'key': 'paidPrivateAgentSlots', 'type': 'int'},
        'total_usage': {'key': 'totalUsage', 'type': 'int'},
        'xaml_controllers': {'key': 'xamlControllers', 'type': 'int'}
    }

    def __init__(self, distributed_task_agents=None, paid_private_agent_slots=None, total_usage=None, xaml_controllers=None):
        super(BuildResourceUsage, self).__init__()
        self.distributed_task_agents = distributed_task_agents
        self.paid_private_agent_slots = paid_private_agent_slots
        self.total_usage = total_usage
        self.xaml_controllers = xaml_controllers
