# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class UPackLimitedPackageMetadata(Model):
    """
    :param description:
    :type description: str
    :param version:
    :type version: str
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, description=None, version=None):
        super(UPackLimitedPackageMetadata, self).__init__()
        self.description = description
        self.version = version


class UPackLimitedPackageMetadataListResponse(Model):
    """
    :param count:
    :type count: int
    :param value:
    :type value: list of :class:`UPackLimitedPackageMetadata <azure.devops.v7_0.upack.models.UPackLimitedPackageMetadata>`
    """

    _attribute_map = {
        'count': {'key': 'count', 'type': 'int'},
        'value': {'key': 'value', 'type': '[UPackLimitedPackageMetadata]'}
    }

    def __init__(self, count=None, value=None):
        super(UPackLimitedPackageMetadataListResponse, self).__init__()
        self.count = count
        self.value = value


class UPackPackageMetadata(Model):
    """
    :param description:
    :type description: str
    :param manifest_id:
    :type manifest_id: str
    :param package_size:
    :type package_size: long
    :param super_root_id:
    :type super_root_id: str
    :param version:
    :type version: str
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'manifest_id': {'key': 'manifestId', 'type': 'str'},
        'package_size': {'key': 'packageSize', 'type': 'long'},
        'super_root_id': {'key': 'superRootId', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, description=None, manifest_id=None, package_size=None, super_root_id=None, version=None):
        super(UPackPackageMetadata, self).__init__()
        self.description = description
        self.manifest_id = manifest_id
        self.package_size = package_size
        self.super_root_id = super_root_id
        self.version = version


class UPackPackagePushMetadata(Model):
    """
    Contains the parameters for adding a new Universal Package to the feed, except for name and version which are transmitted in the URL

    :param description:
    :type description: str
    :param manifest_id:
    :type manifest_id: str
    :param proof_nodes:
    :type proof_nodes: list of str
    :param super_root_id:
    :type super_root_id: str
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'manifest_id': {'key': 'manifestId', 'type': 'str'},
        'proof_nodes': {'key': 'proofNodes', 'type': '[str]'},
        'super_root_id': {'key': 'superRootId', 'type': 'str'}
    }

    def __init__(self, description=None, manifest_id=None, proof_nodes=None, super_root_id=None):
        super(UPackPackagePushMetadata, self).__init__()
        self.description = description
        self.manifest_id = manifest_id
        self.proof_nodes = proof_nodes
        self.super_root_id = super_root_id


class UPackPackageVersionDeletionState(Model):
    """
    Deletion state of a Universal package.

    :param deleted_date: UTC date the package was deleted.
    :type deleted_date: datetime
    :param name: Name of the package.
    :type name: str
    :param version: Version of the package.
    :type version: str
    """

    _attribute_map = {
        'deleted_date': {'key': 'deletedDate', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, deleted_date=None, name=None, version=None):
        super(UPackPackageVersionDeletionState, self).__init__()
        self.deleted_date = deleted_date
        self.name = name
        self.version = version


__all__ = [
    'UPackLimitedPackageMetadata',
    'UPackLimitedPackageMetadataListResponse',
    'UPackPackageMetadata',
    'UPackPackagePushMetadata',
    'UPackPackageVersionDeletionState',
]
