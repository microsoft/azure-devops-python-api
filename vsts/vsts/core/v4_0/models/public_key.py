# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class PublicKey(Model):
    """PublicKey.

    :param exponent: Gets or sets the exponent for the public key.
    :type exponent: list of int
    :param modulus: Gets or sets the modulus for the public key.
    :type modulus: list of int
    """

    _attribute_map = {
        'exponent': {'key': 'exponent', 'type': '[int]'},
        'modulus': {'key': 'modulus', 'type': '[int]'}
    }

    def __init__(self, exponent=None, modulus=None):
        super(PublicKey, self).__init__()
        self.exponent = exponent
        self.modulus = modulus
