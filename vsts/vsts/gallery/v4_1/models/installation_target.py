# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class InstallationTarget(Model):
    """InstallationTarget.

    :param max_inclusive:
    :type max_inclusive: bool
    :param max_version:
    :type max_version: str
    :param min_inclusive:
    :type min_inclusive: bool
    :param min_version:
    :type min_version: str
    :param target:
    :type target: str
    :param target_version:
    :type target_version: str
    """

    _attribute_map = {
        'max_inclusive': {'key': 'maxInclusive', 'type': 'bool'},
        'max_version': {'key': 'maxVersion', 'type': 'str'},
        'min_inclusive': {'key': 'minInclusive', 'type': 'bool'},
        'min_version': {'key': 'minVersion', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'target_version': {'key': 'targetVersion', 'type': 'str'}
    }

    def __init__(self, max_inclusive=None, max_version=None, min_inclusive=None, min_version=None, target=None, target_version=None):
        super(InstallationTarget, self).__init__()
        self.max_inclusive = max_inclusive
        self.max_version = max_version
        self.min_inclusive = min_inclusive
        self.min_version = min_version
        self.target = target
        self.target_version = target_version
