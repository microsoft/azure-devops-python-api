# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class XamlBuildControllerReference(Model):
    """XamlBuildControllerReference.

    :param id: Id of the resource
    :type id: int
    :param name: Name of the linked resource (definition name, controller name, etc.)
    :type name: str
    :param url: Full http link to the resource
    :type url: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, name=None, url=None):
        super(XamlBuildControllerReference, self).__init__()
        self.id = id
        self.name = name
        self.url = url
