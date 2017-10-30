# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class BuildMetric(Model):
    """BuildMetric.

    :param date: The date for the scope.
    :type date: datetime
    :param int_value: The value.
    :type int_value: int
    :param name: The name of the metric.
    :type name: str
    :param scope: The scope.
    :type scope: str
    """

    _attribute_map = {
        'date': {'key': 'date', 'type': 'iso-8601'},
        'int_value': {'key': 'intValue', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'scope': {'key': 'scope', 'type': 'str'}
    }

    def __init__(self, date=None, int_value=None, name=None, scope=None):
        super(BuildMetric, self).__init__()
        self.date = date
        self.int_value = int_value
        self.name = name
        self.scope = scope
