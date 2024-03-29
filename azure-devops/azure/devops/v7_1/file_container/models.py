﻿# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class ContainerItemBlobReference(Model):
    """
    Represents an reference to a file in Blobstore

    :param artifact_hash:
    :type artifact_hash: str
    :param artifact_id:
    :type artifact_id: long
    :param compression_type:
    :type compression_type: object
    :param scope_identifier:
    :type scope_identifier: str
    :param session_id:
    :type session_id: str
    """

    _attribute_map = {
        'artifact_hash': {'key': 'artifactHash', 'type': 'str'},
        'artifact_id': {'key': 'artifactId', 'type': 'long'},
        'compression_type': {'key': 'compressionType', 'type': 'object'},
        'scope_identifier': {'key': 'scopeIdentifier', 'type': 'str'},
        'session_id': {'key': 'sessionId', 'type': 'str'}
    }

    def __init__(self, artifact_hash=None, artifact_id=None, compression_type=None, scope_identifier=None, session_id=None):
        super(ContainerItemBlobReference, self).__init__()
        self.artifact_hash = artifact_hash
        self.artifact_id = artifact_id
        self.compression_type = compression_type
        self.scope_identifier = scope_identifier
        self.session_id = session_id


class FileContainer(Model):
    """
    Represents a container that encapsulates a hierarchical file system.

    :param artifact_uri: Uri of the artifact associated with the container.
    :type artifact_uri: str
    :param content_location: Download Url for the content of this item.
    :type content_location: str
    :param created_by: Owner.
    :type created_by: str
    :param date_created: Creation date.
    :type date_created: datetime
    :param description: Description.
    :type description: str
    :param id: Id.
    :type id: long
    :param item_location: Location of the item resource.
    :type item_location: str
    :param locator_path: ItemStore Locator for this container.
    :type locator_path: str
    :param name: Name.
    :type name: str
    :param options: Options the container can have.
    :type options: object
    :param scope_identifier: Project Id.
    :type scope_identifier: str
    :param security_token: Security token of the artifact associated with the container.
    :type security_token: str
    :param signing_key_id: Identifier of the optional encryption key.
    :type signing_key_id: str
    :param size: Total size of the files in bytes.
    :type size: long
    """

    _attribute_map = {
        'artifact_uri': {'key': 'artifactUri', 'type': 'str'},
        'content_location': {'key': 'contentLocation', 'type': 'str'},
        'created_by': {'key': 'createdBy', 'type': 'str'},
        'date_created': {'key': 'dateCreated', 'type': 'iso-8601'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'long'},
        'item_location': {'key': 'itemLocation', 'type': 'str'},
        'locator_path': {'key': 'locatorPath', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'options': {'key': 'options', 'type': 'object'},
        'scope_identifier': {'key': 'scopeIdentifier', 'type': 'str'},
        'security_token': {'key': 'securityToken', 'type': 'str'},
        'signing_key_id': {'key': 'signingKeyId', 'type': 'str'},
        'size': {'key': 'size', 'type': 'long'}
    }

    def __init__(self, artifact_uri=None, content_location=None, created_by=None, date_created=None, description=None, id=None, item_location=None, locator_path=None, name=None, options=None, scope_identifier=None, security_token=None, signing_key_id=None, size=None):
        super(FileContainer, self).__init__()
        self.artifact_uri = artifact_uri
        self.content_location = content_location
        self.created_by = created_by
        self.date_created = date_created
        self.description = description
        self.id = id
        self.item_location = item_location
        self.locator_path = locator_path
        self.name = name
        self.options = options
        self.scope_identifier = scope_identifier
        self.security_token = security_token
        self.signing_key_id = signing_key_id
        self.size = size


class FileContainerItem(Model):
    """
    Represents an item in a container.

    :param artifact_id: Id for Blobstore reference
    :type artifact_id: long
    :param blob_metadata:
    :type blob_metadata: :class:`ContainerItemBlobReference <azure.devops.v7_1.file_container.models.ContainerItemBlobReference>`
    :param container_id: Container Id.
    :type container_id: long
    :param content_id:
    :type content_id: str
    :param content_location: Download Url for the content of this item.
    :type content_location: str
    :param created_by: Creator.
    :type created_by: str
    :param date_created: Creation date.
    :type date_created: datetime
    :param date_last_modified: Last modified date.
    :type date_last_modified: datetime
    :param file_encoding: Encoding of the file. Zero if not a file.
    :type file_encoding: int
    :param file_hash: Hash value of the file. Null if not a file.
    :type file_hash: str
    :param file_id: Id of the file content.
    :type file_id: int
    :param file_length: Length of the file. Zero if not of a file.
    :type file_length: long
    :param file_type: Type of the file. Zero if not a file.
    :type file_type: int
    :param item_location: Location of the item resource.
    :type item_location: str
    :param item_type: Type of the item: Folder, File or String.
    :type item_type: object
    :param last_modified_by: Modifier.
    :type last_modified_by: str
    :param path: Unique path that identifies the item.
    :type path: str
    :param scope_identifier: Project Id.
    :type scope_identifier: str
    :param status: Status of the item: Created or Pending Upload.
    :type status: object
    :param ticket:
    :type ticket: str
    """

    _attribute_map = {
        'artifact_id': {'key': 'artifactId', 'type': 'long'},
        'blob_metadata': {'key': 'blobMetadata', 'type': 'ContainerItemBlobReference'},
        'container_id': {'key': 'containerId', 'type': 'long'},
        'content_id': {'key': 'contentId', 'type': 'str'},
        'content_location': {'key': 'contentLocation', 'type': 'str'},
        'created_by': {'key': 'createdBy', 'type': 'str'},
        'date_created': {'key': 'dateCreated', 'type': 'iso-8601'},
        'date_last_modified': {'key': 'dateLastModified', 'type': 'iso-8601'},
        'file_encoding': {'key': 'fileEncoding', 'type': 'int'},
        'file_hash': {'key': 'fileHash', 'type': 'str'},
        'file_id': {'key': 'fileId', 'type': 'int'},
        'file_length': {'key': 'fileLength', 'type': 'long'},
        'file_type': {'key': 'fileType', 'type': 'int'},
        'item_location': {'key': 'itemLocation', 'type': 'str'},
        'item_type': {'key': 'itemType', 'type': 'object'},
        'last_modified_by': {'key': 'lastModifiedBy', 'type': 'str'},
        'path': {'key': 'path', 'type': 'str'},
        'scope_identifier': {'key': 'scopeIdentifier', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'},
        'ticket': {'key': 'ticket', 'type': 'str'}
    }

    def __init__(self, artifact_id=None, blob_metadata=None, container_id=None, content_id=None, content_location=None, created_by=None, date_created=None, date_last_modified=None, file_encoding=None, file_hash=None, file_id=None, file_length=None, file_type=None, item_location=None, item_type=None, last_modified_by=None, path=None, scope_identifier=None, status=None, ticket=None):
        super(FileContainerItem, self).__init__()
        self.artifact_id = artifact_id
        self.blob_metadata = blob_metadata
        self.container_id = container_id
        self.content_id = content_id
        self.content_location = content_location
        self.created_by = created_by
        self.date_created = date_created
        self.date_last_modified = date_last_modified
        self.file_encoding = file_encoding
        self.file_hash = file_hash
        self.file_id = file_id
        self.file_length = file_length
        self.file_type = file_type
        self.item_location = item_location
        self.item_type = item_type
        self.last_modified_by = last_modified_by
        self.path = path
        self.scope_identifier = scope_identifier
        self.status = status
        self.ticket = ticket


__all__ = [
    'ContainerItemBlobReference',
    'FileContainer',
    'FileContainerItem',
]
