# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class BuildSettings(Model):
    """BuildSettings.

    :param days_to_keep_deleted_builds_before_destroy:
    :type days_to_keep_deleted_builds_before_destroy: int
    :param default_retention_policy:
    :type default_retention_policy: :class:`RetentionPolicy <build.v4_0.models.RetentionPolicy>`
    :param maximum_retention_policy:
    :type maximum_retention_policy: :class:`RetentionPolicy <build.v4_0.models.RetentionPolicy>`
    """

    _attribute_map = {
        'days_to_keep_deleted_builds_before_destroy': {'key': 'daysToKeepDeletedBuildsBeforeDestroy', 'type': 'int'},
        'default_retention_policy': {'key': 'defaultRetentionPolicy', 'type': 'RetentionPolicy'},
        'maximum_retention_policy': {'key': 'maximumRetentionPolicy', 'type': 'RetentionPolicy'}
    }

    def __init__(self, days_to_keep_deleted_builds_before_destroy=None, default_retention_policy=None, maximum_retention_policy=None):
        super(BuildSettings, self).__init__()
        self.days_to_keep_deleted_builds_before_destroy = days_to_keep_deleted_builds_before_destroy
        self.default_retention_policy = default_retention_policy
        self.maximum_retention_policy = maximum_retention_policy
