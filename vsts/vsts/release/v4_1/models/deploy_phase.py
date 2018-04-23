# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class DeployPhase(Model):
    """DeployPhase.

    :param name:
    :type name: str
    :param phase_type:
    :type phase_type: object
    :param rank:
    :type rank: int
    :param workflow_tasks:
    :type workflow_tasks: list of :class:`WorkflowTask <release.v4_1.models.WorkflowTask>`
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'phase_type': {'key': 'phaseType', 'type': 'object'},
        'rank': {'key': 'rank', 'type': 'int'},
        'workflow_tasks': {'key': 'workflowTasks', 'type': '[WorkflowTask]'}
    }

    def __init__(self, name=None, phase_type=None, rank=None, workflow_tasks=None):
        super(DeployPhase, self).__init__()
        self.name = name
        self.phase_type = phase_type
        self.rank = rank
        self.workflow_tasks = workflow_tasks
