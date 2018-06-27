# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class CreateUserParameters(Model):
    """CreateUserParameters.

    :param country: The user's country of residence or association.
    :type country: str
    :param data:
    :type data: dict
    :param descriptor: The user's unique identifier, and the primary means by which the user is referenced.
    :type descriptor: :class:`str <user.v4_1.models.str>`
    :param display_name: The user's name, as displayed throughout the product.
    :type display_name: str
    :param mail: The user's preferred email address.
    :type mail: str
    :param region: The region in which the user resides or is associated.
    :type region: str
    """

    _attribute_map = {
        'country': {'key': 'country', 'type': 'str'},
        'data': {'key': 'data', 'type': '{object}'},
        'descriptor': {'key': 'descriptor', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'mail': {'key': 'mail', 'type': 'str'},
        'region': {'key': 'region', 'type': 'str'}
    }

    def __init__(self, country=None, data=None, descriptor=None, display_name=None, mail=None, region=None):
        super(CreateUserParameters, self).__init__()
        self.country = country
        self.data = data
        self.descriptor = descriptor
        self.display_name = display_name
        self.mail = mail
        self.region = region
