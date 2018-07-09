# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class SendUserNotificationParameters(Model):
    """SendUserNotificationParameters.

    :param notification: Notification to be delivered
    :type notification: :class:`UserNotification <user.v4_1.models.UserNotification>`
    :param recipients: Users whom this notification is addressed to
    :type recipients: list of :class:`str <user.v4_1.models.str>`
    """

    _attribute_map = {
        'notification': {'key': 'notification', 'type': 'UserNotification'},
        'recipients': {'key': 'recipients', 'type': '[str]'}
    }

    def __init__(self, notification=None, recipients=None):
        super(SendUserNotificationParameters, self).__init__()
        self.notification = notification
        self.recipients = recipients
