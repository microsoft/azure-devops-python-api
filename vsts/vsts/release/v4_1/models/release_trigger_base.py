# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class ReleaseTriggerBase(Model):
    """ReleaseTriggerBase.

    :param trigger_type:
    :type trigger_type: object
    """

    _attribute_map = {
        'trigger_type': {'key': 'triggerType', 'type': 'object'}
    }

    def __init__(self, trigger_type=None):
        super(ReleaseTriggerBase, self).__init__()
        self.trigger_type = trigger_type
