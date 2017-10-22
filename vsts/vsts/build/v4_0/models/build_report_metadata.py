# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class BuildReportMetadata(Model):
    """BuildReportMetadata.

    :param build_id:
    :type build_id: int
    :param content:
    :type content: str
    :param type:
    :type type: str
    """

    _attribute_map = {
        'build_id': {'key': 'buildId', 'type': 'int'},
        'content': {'key': 'content', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, build_id=None, content=None, type=None):
        super(BuildReportMetadata, self).__init__()
        self.build_id = build_id
        self.content = content
        self.type = type
