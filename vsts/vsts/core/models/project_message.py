# coding=utf-8
# --------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ProjectMessage(Model):
    """ProjectMessage.

    :param project:
    :type project: :class:`ProjectInfo <core.models.ProjectInfo>`
    :param project_change_type:
    :type project_change_type: object
    :param should_invalidate_system_store:
    :type should_invalidate_system_store: bool
    """

    _attribute_map = {
        'project': {'key': 'project', 'type': 'ProjectInfo'},
        'project_change_type': {'key': 'projectChangeType', 'type': 'object'},
        'should_invalidate_system_store': {'key': 'shouldInvalidateSystemStore', 'type': 'bool'}
    }

    def __init__(self, project=None, project_change_type=None, should_invalidate_system_store=None):
        super(ProjectMessage, self).__init__()
        self.project = project
        self.project_change_type = project_change_type
        self.should_invalidate_system_store = should_invalidate_system_store
