# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class UpdateUserParameters(Model):
    """UpdateUserParameters.

    :param properties: The collection of properties to set.  See "User" for valid fields.
    :type properties: :class:`object <user.v4_1.models.object>`
    """

    _attribute_map = {
        'properties': {'key': 'properties', 'type': 'object'}
    }

    def __init__(self, properties=None):
        super(UpdateUserParameters, self).__init__()
        self.properties = properties
