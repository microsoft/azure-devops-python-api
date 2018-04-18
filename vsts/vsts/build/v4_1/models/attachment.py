# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class Attachment(Model):
    """Attachment.

    :param _links:
    :type _links: :class:`ReferenceLinks <build.v4_1.models.ReferenceLinks>`
    :param name: The name of the attachment.
    :type name: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, _links=None, name=None):
        super(Attachment, self).__init__()
        self._links = _links
        self.name = name
