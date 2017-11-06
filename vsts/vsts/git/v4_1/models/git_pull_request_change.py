# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from .git_change import GitChange


class GitPullRequestChange(GitChange):
    """GitPullRequestChange.

    :param change_id: ID of the change within the group of changes.
    :type change_id: int
    :param new_content_template: New Content template to be used when pushing new changes.
    :type new_content_template: :class:`GitTemplate <git.v4_1.models.GitTemplate>`
    :param original_path: Original path of item if different from current path.
    :type original_path: str
    :param change_tracking_id: ID used to track files through multiple changes.
    :type change_tracking_id: int
    """

    _attribute_map = {
        'change_id': {'key': 'changeId', 'type': 'int'},
        'new_content_template': {'key': 'newContentTemplate', 'type': 'GitTemplate'},
        'original_path': {'key': 'originalPath', 'type': 'str'},
        'change_tracking_id': {'key': 'changeTrackingId', 'type': 'int'}
    }

    def __init__(self, change_id=None, new_content_template=None, original_path=None, change_tracking_id=None):
        super(GitPullRequestChange, self).__init__(change_id=change_id, new_content_template=new_content_template, original_path=original_path)
        self.change_tracking_id = change_tracking_id
