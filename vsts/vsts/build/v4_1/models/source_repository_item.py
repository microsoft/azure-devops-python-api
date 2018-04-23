# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class SourceRepositoryItem(Model):
    """SourceRepositoryItem.

    :param is_container: Whether the item is able to have sub-items (e.g., is a folder).
    :type is_container: bool
    :param path: The full path of the item, relative to the root of the repository.
    :type path: str
    :param type: The type of the item (folder, file, etc).
    :type type: str
    :param url: The URL of the item.
    :type url: str
    """

    _attribute_map = {
        'is_container': {'key': 'isContainer', 'type': 'bool'},
        'path': {'key': 'path', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, is_container=None, path=None, type=None, url=None):
        super(SourceRepositoryItem, self).__init__()
        self.is_container = is_container
        self.path = path
        self.type = type
        self.url = url
