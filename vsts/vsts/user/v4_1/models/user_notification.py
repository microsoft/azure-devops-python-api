# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class UserNotification(Model):
    """UserNotification.

    :param event_id: Unique notification id (must be idempotent)
    :type event_id: str
    :param time_stamp: Time at which notification was posted (must be idempotent)
    :type time_stamp: datetime
    """

    _attribute_map = {
        'event_id': {'key': 'eventId', 'type': 'str'},
        'time_stamp': {'key': 'timeStamp', 'type': 'iso-8601'}
    }

    def __init__(self, event_id=None, time_stamp=None):
        super(UserNotification, self).__init__()
        self.event_id = event_id
        self.time_stamp = time_stamp
