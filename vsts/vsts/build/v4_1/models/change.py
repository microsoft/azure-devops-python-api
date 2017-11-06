# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class Change(Model):
    """Change.

    :param author: The author of the change.
    :type author: :class:`IdentityRef <build.v4_1.models.IdentityRef>`
    :param display_uri: The location of a user-friendly representation of the resource.
    :type display_uri: str
    :param id: The identifier for the change. For a commit, this would be the SHA1. For a TFVC changeset, this would be the changeset ID.
    :type id: str
    :param location: The location of the full representation of the resource.
    :type location: str
    :param message: The description of the change. This might be a commit message or changeset description.
    :type message: str
    :param message_truncated: Indicates whether the message was truncated.
    :type message_truncated: bool
    :param pusher: The person or process that pushed the change.
    :type pusher: str
    :param timestamp: The timestamp for the change.
    :type timestamp: datetime
    :param type: The type of change. "commit", "changeset", etc.
    :type type: str
    """

    _attribute_map = {
        'author': {'key': 'author', 'type': 'IdentityRef'},
        'display_uri': {'key': 'displayUri', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'message_truncated': {'key': 'messageTruncated', 'type': 'bool'},
        'pusher': {'key': 'pusher', 'type': 'str'},
        'timestamp': {'key': 'timestamp', 'type': 'iso-8601'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, author=None, display_uri=None, id=None, location=None, message=None, message_truncated=None, pusher=None, timestamp=None, type=None):
        super(Change, self).__init__()
        self.author = author
        self.display_uri = display_uri
        self.id = id
        self.location = location
        self.message = message
        self.message_truncated = message_truncated
        self.pusher = pusher
        self.timestamp = timestamp
        self.type = type
