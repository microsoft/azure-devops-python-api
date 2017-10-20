# coding=utf-8
# --------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class TemporaryDataDTO(Model):
    """TemporaryDataDTO.

    :param expiration_seconds:
    :type expiration_seconds: int
    :param origin:
    :type origin: str
    :param value:
    :type value: object
    """

    _attribute_map = {
        'expiration_seconds': {'key': 'expirationSeconds', 'type': 'int'},
        'origin': {'key': 'origin', 'type': 'str'},
        'value': {'key': 'value', 'type': 'object'}
    }

    def __init__(self, expiration_seconds=None, origin=None, value=None):
        super(TemporaryDataDTO, self).__init__()
        self.expiration_seconds = expiration_seconds
        self.origin = origin
        self.value = value
