# coding=utf-8
# --------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class SubjectDescriptor(Model):
    """SubjectDescriptor.

    :param identifier:
    :type identifier: str
    :param subject_type:
    :type subject_type: str
    """

    _attribute_map = {
        'identifier': {'key': 'identifier', 'type': 'str'},
        'subject_type': {'key': 'subjectType', 'type': 'str'}
    }

    def __init__(self, identifier=None, subject_type=None):
        super(SubjectDescriptor, self).__init__()
        self.identifier = identifier
        self.subject_type = subject_type
