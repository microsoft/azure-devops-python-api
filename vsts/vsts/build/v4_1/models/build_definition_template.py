# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class BuildDefinitionTemplate(Model):
    """BuildDefinitionTemplate.

    :param can_delete: Indicates whether the template can be deleted.
    :type can_delete: bool
    :param category: The template category.
    :type category: str
    :param default_hosted_queue: An optional hosted agent queue for the template to use by default.
    :type default_hosted_queue: str
    :param description: A description of the template.
    :type description: str
    :param icons:
    :type icons: dict
    :param icon_task_id: The ID of the task whose icon is used when showing this template in the UI.
    :type icon_task_id: str
    :param id: The ID of the template.
    :type id: str
    :param name: The name of the template.
    :type name: str
    :param template: The actual template.
    :type template: :class:`BuildDefinition <build.v4_1.models.BuildDefinition>`
    """

    _attribute_map = {
        'can_delete': {'key': 'canDelete', 'type': 'bool'},
        'category': {'key': 'category', 'type': 'str'},
        'default_hosted_queue': {'key': 'defaultHostedQueue', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'icons': {'key': 'icons', 'type': '{str}'},
        'icon_task_id': {'key': 'iconTaskId', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'template': {'key': 'template', 'type': 'BuildDefinition'}
    }

    def __init__(self, can_delete=None, category=None, default_hosted_queue=None, description=None, icons=None, icon_task_id=None, id=None, name=None, template=None):
        super(BuildDefinitionTemplate, self).__init__()
        self.can_delete = can_delete
        self.category = category
        self.default_hosted_queue = default_hosted_queue
        self.description = description
        self.icons = icons
        self.icon_task_id = icon_task_id
        self.id = id
        self.name = name
        self.template = template
