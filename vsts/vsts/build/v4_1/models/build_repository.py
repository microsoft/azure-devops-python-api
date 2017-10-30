# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class BuildRepository(Model):
    """BuildRepository.

    :param checkout_submodules: Indicates whether to checkout submodules.
    :type checkout_submodules: bool
    :param clean: Indicates whether to clean the target folder when getting code from the repository.
    :type clean: str
    :param default_branch: The name of the default branch.
    :type default_branch: str
    :param id: The ID of the repository.
    :type id: str
    :param name: The friendly name of the repository.
    :type name: str
    :param properties:
    :type properties: dict
    :param root_folder: The root folder.
    :type root_folder: str
    :param type: The type of the repository.
    :type type: str
    :param url: The URL of the repository.
    :type url: str
    """

    _attribute_map = {
        'checkout_submodules': {'key': 'checkoutSubmodules', 'type': 'bool'},
        'clean': {'key': 'clean', 'type': 'str'},
        'default_branch': {'key': 'defaultBranch', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '{str}'},
        'root_folder': {'key': 'rootFolder', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, checkout_submodules=None, clean=None, default_branch=None, id=None, name=None, properties=None, root_folder=None, type=None, url=None):
        super(BuildRepository, self).__init__()
        self.checkout_submodules = checkout_submodules
        self.clean = clean
        self.default_branch = default_branch
        self.id = id
        self.name = name
        self.properties = properties
        self.root_folder = root_folder
        self.type = type
        self.url = url
