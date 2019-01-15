# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class RepositoryWebhook(Model):
    """RepositoryWebhook.

    :param name: The friendly name of the repository.
    :type name: str
    :param types:
    :type types: list of DefinitionTriggerType
    :param url: The URL of the repository.
    :type url: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'types': {'key': 'types', 'type': '[object]'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, name=None, types=None, url=None):
        super(RepositoryWebhook, self).__init__()
        self.name = name
        self.types = types
        self.url = url
