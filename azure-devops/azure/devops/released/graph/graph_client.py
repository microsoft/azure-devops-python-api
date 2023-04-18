# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from ...v7_0.graph import models


class GraphClient(Client):
    """Graph
    :param str base_url: Service URL
    :param Authentication creds: Authenticated credentials.
    """

    def __init__(self, base_url=None, creds=None):
        super(GraphClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = 'bb1e7ec9-e901-4b68-999a-de7012b920f8'

    def delete_avatar(self, subject_descriptor):
        """DeleteAvatar.
        :param str subject_descriptor:
        """
        route_values = {}
        if subject_descriptor is not None:
            route_values['subjectDescriptor'] = self._serialize.url('subject_descriptor', subject_descriptor, 'str')
        self._send(http_method='DELETE',
                   location_id='801eaf9c-0585-4be8-9cdb-b0efa074de91',
                   version='7.0',
                   route_values=route_values)

    def get_avatar(self, subject_descriptor, size=None, format=None):
        """GetAvatar.
        :param str subject_descriptor:
        :param str size:
        :param str format:
        :rtype: :class:`<Avatar> <azure.devops.v7_0.graph.models.Avatar>`
        """
        route_values = {}
        if subject_descriptor is not None:
            route_values['subjectDescriptor'] = self._serialize.url('subject_descriptor', subject_descriptor, 'str')
        query_parameters = {}
        if size is not None:
            query_parameters['size'] = self._serialize.query('size', size, 'str')
        if format is not None:
            query_parameters['format'] = self._serialize.query('format', format, 'str')
        response = self._send(http_method='GET',
                              location_id='801eaf9c-0585-4be8-9cdb-b0efa074de91',
                              version='7.0',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('Avatar', response)

    def set_avatar(self, avatar, subject_descriptor):
        """SetAvatar.
        :param :class:`<Avatar> <azure.devops.v7_0.graph.models.Avatar>` avatar:
        :param str subject_descriptor:
        """
        route_values = {}
        if subject_descriptor is not None:
            route_values['subjectDescriptor'] = self._serialize.url('subject_descriptor', subject_descriptor, 'str')
        content = self._serialize.body(avatar, 'Avatar')
        self._send(http_method='PUT',
                   location_id='801eaf9c-0585-4be8-9cdb-b0efa074de91',
                   version='7.0',
                   route_values=route_values,
                   content=content)

    def get_descriptor(self, storage_key):
        """GetDescriptor.
        Resolve a storage key to a descriptor
        :param str storage_key: Storage key of the subject (user, group, scope, etc.) to resolve
        :rtype: :class:`<GraphDescriptorResult> <azure.devops.v7_0.graph.models.GraphDescriptorResult>`
        """
        route_values = {}
        if storage_key is not None:
            route_values['storageKey'] = self._serialize.url('storage_key', storage_key, 'str')
        response = self._send(http_method='GET',
                              location_id='048aee0a-7072-4cde-ab73-7af77b1e0b4e',
                              version='7.0',
                              route_values=route_values)
        return self._deserialize('GraphDescriptorResult', response)

    def get_provider_info(self, user_descriptor):
        """GetProviderInfo.
        :param str user_descriptor:
        :rtype: :class:`<GraphProviderInfo> <azure.devops.v7_0.graph.models.GraphProviderInfo>`
        """
        route_values = {}
        if user_descriptor is not None:
            route_values['userDescriptor'] = self._serialize.url('user_descriptor', user_descriptor, 'str')
        response = self._send(http_method='GET',
                              location_id='1e377995-6fa2-4588-bd64-930186abdcfa',
                              version='7.0',
                              route_values=route_values)
        return self._deserialize('GraphProviderInfo', response)

    def get_storage_key(self, subject_descriptor):
        """GetStorageKey.
        Resolve a descriptor to a storage key.
        :param str subject_descriptor:
        :rtype: :class:`<GraphStorageKeyResult> <azure.devops.v7_0.graph.models.GraphStorageKeyResult>`
        """
        route_values = {}
        if subject_descriptor is not None:
            route_values['subjectDescriptor'] = self._serialize.url('subject_descriptor', subject_descriptor, 'str')
        response = self._send(http_method='GET',
                              location_id='eb85f8cc-f0f6-4264-a5b1-ffe2e4d4801f',
                              version='7.0',
                              route_values=route_values)
        return self._deserialize('GraphStorageKeyResult', response)

