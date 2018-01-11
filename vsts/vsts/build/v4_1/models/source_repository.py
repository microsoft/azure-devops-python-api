# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class SourceRepository(Model):
    """SourceRepository.

    :param default_branch: The name of the default branch.
    :type default_branch: str
    :param full_name: The full name of the repository.
    :type full_name: str
    :param id: The ID of the repository.
    :type id: str
    :param name: The friendly name of the repository.
    :type name: str
    :param properties:
    :type properties: dict
    :param source_provider_name: The name of the source provider the repository is from.
    :type source_provider_name: str
    :param url: The URL of the repository.
    :type url: str
    """

    _attribute_map = {
        'default_branch': {'key': 'defaultBranch', 'type': 'str'},
        'full_name': {'key': 'fullName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '{str}'},
        'source_provider_name': {'key': 'sourceProviderName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, default_branch=None, full_name=None, id=None, name=None, properties=None, source_provider_name=None, url=None):
        super(SourceRepository, self).__init__()
        self.default_branch = default_branch
        self.full_name = full_name
        self.id = id
        self.name = name
        self.properties = properties
        self.source_provider_name = source_provider_name
        self.url = url
