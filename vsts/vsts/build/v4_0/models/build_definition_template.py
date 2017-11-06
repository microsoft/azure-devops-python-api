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

    :param can_delete:
    :type can_delete: bool
    :param category:
    :type category: str
    :param description:
    :type description: str
    :param icons:
    :type icons: dict
    :param icon_task_id:
    :type icon_task_id: str
    :param id:
    :type id: str
    :param name:
    :type name: str
    :param template:
    :type template: :class:`BuildDefinition <build.v4_0.models.BuildDefinition>`
    """

    _attribute_map = {
        'can_delete': {'key': 'canDelete', 'type': 'bool'},
        'category': {'key': 'category', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'icons': {'key': 'icons', 'type': '{str}'},
        'icon_task_id': {'key': 'iconTaskId', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'template': {'key': 'template', 'type': 'BuildDefinition'}
    }

    def __init__(self, can_delete=None, category=None, description=None, icons=None, icon_task_id=None, id=None, name=None, template=None):
        super(BuildDefinitionTemplate, self).__init__()
        self.can_delete = can_delete
        self.category = category
        self.description = description
        self.icons = icons
        self.icon_task_id = icon_task_id
        self.id = id
        self.name = name
        self.template = template
