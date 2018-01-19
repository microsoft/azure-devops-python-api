# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class ExtensionFile(Model):
    """ExtensionFile.

    :param asset_type:
    :type asset_type: str
    :param content_type:
    :type content_type: str
    :param file_id:
    :type file_id: int
    :param is_default:
    :type is_default: bool
    :param is_public:
    :type is_public: bool
    :param language:
    :type language: str
    :param short_description:
    :type short_description: str
    :param source:
    :type source: str
    :param version:
    :type version: str
    """

    _attribute_map = {
        'asset_type': {'key': 'assetType', 'type': 'str'},
        'content_type': {'key': 'contentType', 'type': 'str'},
        'file_id': {'key': 'fileId', 'type': 'int'},
        'is_default': {'key': 'isDefault', 'type': 'bool'},
        'is_public': {'key': 'isPublic', 'type': 'bool'},
        'language': {'key': 'language', 'type': 'str'},
        'short_description': {'key': 'shortDescription', 'type': 'str'},
        'source': {'key': 'source', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, asset_type=None, content_type=None, file_id=None, is_default=None, is_public=None, language=None, short_description=None, source=None, version=None):
        super(ExtensionFile, self).__init__()
        self.asset_type = asset_type
        self.content_type = content_type
        self.file_id = file_id
        self.is_default = is_default
        self.is_public = is_public
        self.language = language
        self.short_description = short_description
        self.source = source
        self.version = version
