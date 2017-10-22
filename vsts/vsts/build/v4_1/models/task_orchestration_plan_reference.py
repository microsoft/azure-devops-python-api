# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class TaskOrchestrationPlanReference(Model):
    """TaskOrchestrationPlanReference.

    :param orchestration_type: Orchestration Type for Build (build, cleanup etc.)
    :type orchestration_type: int
    :param plan_id:
    :type plan_id: str
    """

    _attribute_map = {
        'orchestration_type': {'key': 'orchestrationType', 'type': 'int'},
        'plan_id': {'key': 'planId', 'type': 'str'}
    }

    def __init__(self, orchestration_type=None, plan_id=None):
        super(TaskOrchestrationPlanReference, self).__init__()
        self.orchestration_type = orchestration_type
        self.plan_id = plan_id
