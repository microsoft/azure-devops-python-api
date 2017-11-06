# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from .xaml_build_controller_reference import XamlBuildControllerReference


class BuildController(XamlBuildControllerReference):
    """BuildController.

    :param id: Id of the resource
    :type id: int
    :param name: Name of the linked resource (definition name, controller name, etc.)
    :type name: str
    :param url: Full http link to the resource
    :type url: str
    :param _links:
    :type _links: :class:`ReferenceLinks <build.v4_0.models.ReferenceLinks>`
    :param created_date: The date the controller was created.
    :type created_date: datetime
    :param description: The description of the controller.
    :type description: str
    :param enabled: Indicates whether the controller is enabled.
    :type enabled: bool
    :param status: The status of the controller.
    :type status: object
    :param updated_date: The date the controller was last updated.
    :type updated_date: datetime
    :param uri: The controller's URI.
    :type uri: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'description': {'key': 'description', 'type': 'str'},
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'status': {'key': 'status', 'type': 'object'},
        'updated_date': {'key': 'updatedDate', 'type': 'iso-8601'},
        'uri': {'key': 'uri', 'type': 'str'}
    }

    def __init__(self, id=None, name=None, url=None, _links=None, created_date=None, description=None, enabled=None, status=None, updated_date=None, uri=None):
        super(BuildController, self).__init__(id=id, name=name, url=url)
        self._links = _links
        self.created_date = created_date
        self.description = description
        self.enabled = enabled
        self.status = status
        self.updated_date = updated_date
        self.uri = uri
