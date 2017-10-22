# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from .change import Change


class GitChange(Change):
    """GitChange.

    :param change_id: Id of the change within the group.  For example, within the iteration
    :type change_id: int
    :param new_content_template: New Content template to be used
    :type new_content_template: :class:`GitTemplate <git.models.GitTemplate>`
    :param original_path: Original path of item if different from current path
    :type original_path: str
    """

    _attribute_map = {
        'change_id': {'key': 'changeId', 'type': 'int'},
        'new_content_template': {'key': 'newContentTemplate', 'type': 'GitTemplate'},
        'original_path': {'key': 'originalPath', 'type': 'str'}
    }

    def __init__(self, change_id=None, new_content_template=None, original_path=None):
        super(GitChange, self).__init__()
        self.change_id = change_id
        self.new_content_template = new_content_template
        self.original_path = original_path
