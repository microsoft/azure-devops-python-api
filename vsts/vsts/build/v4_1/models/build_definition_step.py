# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class BuildDefinitionStep(Model):
    """BuildDefinitionStep.

    :param always_run: Indicates whether this step should run even if a previous step fails.
    :type always_run: bool
    :param condition: A condition that determines whether this step should run.
    :type condition: str
    :param continue_on_error: Indicates whether the phase should continue even if this step fails.
    :type continue_on_error: bool
    :param display_name: The display name for this step.
    :type display_name: str
    :param enabled: Indicates whether the step is enabled.
    :type enabled: bool
    :param environment:
    :type environment: dict
    :param inputs:
    :type inputs: dict
    :param ref_name: The reference name for this step.
    :type ref_name: str
    :param task: The task associated with this step.
    :type task: :class:`TaskDefinitionReference <build.v4_1.models.TaskDefinitionReference>`
    :param timeout_in_minutes: The time, in minutes, that this step is allowed to run.
    :type timeout_in_minutes: int
    """

    _attribute_map = {
        'always_run': {'key': 'alwaysRun', 'type': 'bool'},
        'condition': {'key': 'condition', 'type': 'str'},
        'continue_on_error': {'key': 'continueOnError', 'type': 'bool'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'environment': {'key': 'environment', 'type': '{str}'},
        'inputs': {'key': 'inputs', 'type': '{str}'},
        'ref_name': {'key': 'refName', 'type': 'str'},
        'task': {'key': 'task', 'type': 'TaskDefinitionReference'},
        'timeout_in_minutes': {'key': 'timeoutInMinutes', 'type': 'int'}
    }

    def __init__(self, always_run=None, condition=None, continue_on_error=None, display_name=None, enabled=None, environment=None, inputs=None, ref_name=None, task=None, timeout_in_minutes=None):
        super(BuildDefinitionStep, self).__init__()
        self.always_run = always_run
        self.condition = condition
        self.continue_on_error = continue_on_error
        self.display_name = display_name
        self.enabled = enabled
        self.environment = environment
        self.inputs = inputs
        self.ref_name = ref_name
        self.task = task
        self.timeout_in_minutes = timeout_in_minutes
