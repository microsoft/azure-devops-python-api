# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class LanguageStatistics(Model):
    """LanguageStatistics.

    :param bytes:
    :type bytes: long
    :param files:
    :type files: int
    :param files_percentage:
    :type files_percentage: number
    :param language_percentage:
    :type language_percentage: number
    :param name:
    :type name: str
    """

    _attribute_map = {
        'bytes': {'key': 'bytes', 'type': 'long'},
        'files': {'key': 'files', 'type': 'int'},
        'files_percentage': {'key': 'filesPercentage', 'type': 'number'},
        'language_percentage': {'key': 'languagePercentage', 'type': 'number'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, bytes=None, files=None, files_percentage=None, language_percentage=None, name=None):
        super(LanguageStatistics, self).__init__()
        self.bytes = bytes
        self.files = files
        self.files_percentage = files_percentage
        self.language_percentage = language_percentage
        self.name = name
