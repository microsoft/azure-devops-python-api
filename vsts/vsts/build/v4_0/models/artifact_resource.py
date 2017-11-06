# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class ArtifactResource(Model):
    """ArtifactResource.

    :param _links:
    :type _links: :class:`ReferenceLinks <build.v4_0.models.ReferenceLinks>`
    :param data: The type-specific resource data. For example, "#/10002/5/drop", "$/drops/5", "\\myshare\myfolder\mydrops\5"
    :type data: str
    :param download_url: Link to the resource. This might include things like query parameters to download as a zip file
    :type download_url: str
    :param properties: Properties of Artifact Resource
    :type properties: dict
    :param type: The type of the resource: File container, version control folder, UNC path, etc.
    :type type: str
    :param url: Link to the resource
    :type url: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'data': {'key': 'data', 'type': 'str'},
        'download_url': {'key': 'downloadUrl', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '{str}'},
        'type': {'key': 'type', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, data=None, download_url=None, properties=None, type=None, url=None):
        super(ArtifactResource, self).__init__()
        self._links = _links
        self.data = data
        self.download_url = download_url
        self.properties = properties
        self.type = type
        self.url = url
