# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class BuildArtifact(Model):
    """BuildArtifact.

    :param id: The artifact id
    :type id: int
    :param name: The name of the artifact
    :type name: str
    :param resource: The actual resource
    :type resource: :class:`ArtifactResource <build.v4_0.models.ArtifactResource>`
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'ArtifactResource'}
    }

    def __init__(self, id=None, name=None, resource=None):
        super(BuildArtifact, self).__init__()
        self.id = id
        self.name = name
        self.resource = resource
