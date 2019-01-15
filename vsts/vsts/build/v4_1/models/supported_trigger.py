# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class SupportedTrigger(Model):
    """SupportedTrigger.

    :param default_polling_interval: The default interval to wait between polls (only relevant when NotificationType is Polling).
    :type default_polling_interval: int
    :param notification_type: How the trigger is notified of changes.
    :type notification_type: str
    :param supported_capabilities: The capabilities supported by this trigger.
    :type supported_capabilities: dict
    :param type: The type of trigger.
    :type type: object
    """

    _attribute_map = {
        'default_polling_interval': {'key': 'defaultPollingInterval', 'type': 'int'},
        'notification_type': {'key': 'notificationType', 'type': 'str'},
        'supported_capabilities': {'key': 'supportedCapabilities', 'type': '{object}'},
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, default_polling_interval=None, notification_type=None, supported_capabilities=None, type=None):
        super(SupportedTrigger, self).__init__()
        self.default_polling_interval = default_polling_interval
        self.notification_type = notification_type
        self.supported_capabilities = supported_capabilities
        self.type = type
