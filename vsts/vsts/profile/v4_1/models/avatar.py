# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class Avatar(Model):
    """Avatar.

    :param is_auto_generated:
    :type is_auto_generated: bool
    :param size:
    :type size: object
    :param time_stamp:
    :type time_stamp: datetime
    :param value:
    :type value: str
    """

    _attribute_map = {
        'is_auto_generated': {'key': 'isAutoGenerated', 'type': 'bool'},
        'size': {'key': 'size', 'type': 'object'},
        'time_stamp': {'key': 'timeStamp', 'type': 'iso-8601'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, is_auto_generated=None, size=None, time_stamp=None, value=None):
        super(Avatar, self).__init__()
        self.is_auto_generated = is_auto_generated
        self.size = size
        self.time_stamp = time_stamp
        self.value = value
