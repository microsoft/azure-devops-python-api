# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class SourceProviderAttributes(Model):
    """SourceProviderAttributes.

    :param name: The name of the source provider.
    :type name: str
    :param supported_capabilities: The capabilities supported by this source provider.
    :type supported_capabilities: dict
    :param supported_triggers: The types of triggers supported by this source provider.
    :type supported_triggers: list of :class:`SupportedTrigger <build.v4_1.models.SupportedTrigger>`
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'supported_capabilities': {'key': 'supportedCapabilities', 'type': '{bool}'},
        'supported_triggers': {'key': 'supportedTriggers', 'type': '[SupportedTrigger]'}
    }

    def __init__(self, name=None, supported_capabilities=None, supported_triggers=None):
        super(SourceProviderAttributes, self).__init__()
        self.name = name
        self.supported_capabilities = supported_capabilities
        self.supported_triggers = supported_triggers
