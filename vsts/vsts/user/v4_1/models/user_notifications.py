# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class UserNotifications(Model):
    """UserNotifications.

    :param continuation_token: Continuation token to query the next segment
    :type continuation_token: str
    :param notifications: Collection of notifications
    :type notifications: list of :class:`UserNotification <user.v4_1.models.UserNotification>`
    """

    _attribute_map = {
        'continuation_token': {'key': 'continuationToken', 'type': 'str'},
        'notifications': {'key': 'notifications', 'type': '[UserNotification]'}
    }

    def __init__(self, continuation_token=None, notifications=None):
        super(UserNotifications, self).__init__()
        self.continuation_token = continuation_token
        self.notifications = notifications
