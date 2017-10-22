# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from .build_log_reference import BuildLogReference


class BuildLog(BuildLogReference):
    """BuildLog.

    :param id: The id of the log.
    :type id: int
    :param type: The type of the log location.
    :type type: str
    :param url: Full link to the log resource.
    :type url: str
    :param created_on: The date the log was created.
    :type created_on: datetime
    :param last_changed_on: The date the log was last changed.
    :type last_changed_on: datetime
    :param line_count: The number of lines in the log.
    :type line_count: long
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'type': {'key': 'type', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'last_changed_on': {'key': 'lastChangedOn', 'type': 'iso-8601'},
        'line_count': {'key': 'lineCount', 'type': 'long'}
    }

    def __init__(self, id=None, type=None, url=None, created_on=None, last_changed_on=None, line_count=None):
        super(BuildLog, self).__init__(id=id, type=type, url=url)
        self.created_on = created_on
        self.last_changed_on = last_changed_on
        self.line_count = line_count
