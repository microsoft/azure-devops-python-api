# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from .timeline_reference import TimelineReference


class Timeline(TimelineReference):
    """Timeline.

    :param change_id: The change ID.
    :type change_id: int
    :param id: The ID of the timeline.
    :type id: str
    :param url: The REST URL of the timeline.
    :type url: str
    :param last_changed_by: The process or person that last changed the timeline.
    :type last_changed_by: str
    :param last_changed_on: The time the timeline was last changed.
    :type last_changed_on: datetime
    :param records:
    :type records: list of :class:`TimelineRecord <build.v4_1.models.TimelineRecord>`
    """

    _attribute_map = {
        'change_id': {'key': 'changeId', 'type': 'int'},
        'id': {'key': 'id', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'last_changed_by': {'key': 'lastChangedBy', 'type': 'str'},
        'last_changed_on': {'key': 'lastChangedOn', 'type': 'iso-8601'},
        'records': {'key': 'records', 'type': '[TimelineRecord]'}
    }

    def __init__(self, change_id=None, id=None, url=None, last_changed_by=None, last_changed_on=None, records=None):
        super(Timeline, self).__init__(change_id=change_id, id=id, url=url)
        self.last_changed_by = last_changed_by
        self.last_changed_on = last_changed_on
        self.records = records
