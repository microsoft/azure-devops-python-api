# coding=utf-8
# --------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class WrappedException(Model):
    """WrappedException.
    :param exception_id:
    :type exception_id: str
    :param inner_exception:
    :type inner_exception: :class:`WrappedException <vsts.WrappedException>`
    :param message:
    :type message: str
    :param type_name:
    :type type_name: str
    :param type_key:
    :type type_key: str
    :param error_code:
    :type error_code: int
    :param event_id:
    :type event_id: int
    """

    _attribute_map = {
        'exception_id': {'key': '$id', 'type': 'str'},
        'inner_exception': {'key': 'innerException', 'type': 'WrappedException'},
        'message': {'key': 'message', 'type': 'str'},
        'type_name': {'key': 'typeName', 'type': 'str'},
        'type_key': {'key': 'typeKey', 'type': 'str'},
        'error_code': {'key': 'errorCode', 'type': 'int'},
        'event_id': {'key': 'eventId', 'type': 'int'}
    }

    def __init__(self, exception_id=None, inner_exception=None, message=None,
                 type_name=None, type_key=None, error_code=None, event_id=None):
        super(WrappedException, self).__init__()
        self.exception_id = exception_id
        self.inner_exception = inner_exception
        self.message = message
        self.type_name = type_name
        self.type_key = type_key
        self.error_code = error_code
        self.event_id = event_id
