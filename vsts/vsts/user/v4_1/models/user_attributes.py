# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class UserAttributes(Model):
    """UserAttributes.

    :param attributes: Collection of attributes
    :type attributes: list of :class:`UserAttribute <user.v4_1.models.UserAttribute>`
    :param continuation_token: Opaque string to get the next chunk of results Server would return non-null string here if there is more data Client will need then to pass it to the server to get more results
    :type continuation_token: str
    """

    _attribute_map = {
        'attributes': {'key': 'attributes', 'type': '[UserAttribute]'},
        'continuation_token': {'key': 'continuationToken', 'type': 'str'}
    }

    def __init__(self, attributes=None, continuation_token=None):
        super(UserAttributes, self).__init__()
        self.attributes = attributes
        self.continuation_token = continuation_token
