# coding=utf-8
# --------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .temporary_data_d_t_o import TemporaryDataDTO


class TemporaryDataCreatedDTO(TemporaryDataDTO):
    """TemporaryDataCreatedDTO.

    :param expiration_seconds:
    :type expiration_seconds: int
    :param origin:
    :type origin: str
    :param value:
    :type value: object
    :param expiration_date:
    :type expiration_date: datetime
    :param id:
    :type id: str
    :param url:
    :type url: str
    """

    _attribute_map = {
        'expiration_seconds': {'key': 'expirationSeconds', 'type': 'int'},
        'origin': {'key': 'origin', 'type': 'str'},
        'value': {'key': 'value', 'type': 'object'},
        'expiration_date': {'key': 'expirationDate', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, expiration_seconds=None, origin=None, value=None, expiration_date=None, id=None, url=None):
        super(TemporaryDataCreatedDTO, self).__init__(expiration_seconds=expiration_seconds, origin=origin, value=value)
        self.expiration_date = expiration_date
        self.id = id
        self.url = url
