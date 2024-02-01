# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from azure.core.rest import HttpRequest, HttpResponse
from ...client import Client
from . import models


class FileContainerClient(Client):
    """FileContainer
    :param str base_url: Service URL
    :param Authentication creds: Authenticated credentials.
    """

    def __init__(self, base_url=None, creds=None):
        super(FileContainerClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = None

    def create_items(self, items, container_id, scope=None):
        """CreateItems.
        [Preview API] Creates the specified items in the referenced container.
        :param :class:`<VssJsonCollectionWrapper> <azure.devops.v7_2.file_container.models.VssJsonCollectionWrapper>` items:
        :param int container_id:
        :param str scope: A guid representing the scope of the container. This is often the project id.
        :rtype: [FileContainerItem]
        """
        route_values = {}
        if container_id is not None:
            route_values['containerId'] = self._serialize.url('container_id', container_id, 'int')
        query_parameters = {}
        if scope is not None:
            query_parameters['scope'] = self._serialize.query('scope', scope, 'str')
        content = self._serialize.body(items, 'VssJsonCollectionWrapper')
        response = self._send(http_method='POST',
                              location_id='e4f5c81e-e250-447b-9fef-bd48471bea5e',
                              version='7.2-preview.4',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('[FileContainerItem]', self._unwrap_collection(response))

    def delete_item(self, container_id, item_path, scope=None):
        """DeleteItem.
        [Preview API] Deletes the specified items in a container.
        :param long container_id: Container Id.
        :param str item_path: Path to delete.
        :param str scope: A guid representing the scope of the container. This is often the project id.
        """
        route_values = {}
        if container_id is not None:
            route_values['containerId'] = self._serialize.url('container_id', container_id, 'long')
        query_parameters = {}
        if item_path is not None:
            query_parameters['itemPath'] = self._serialize.query('item_path', item_path, 'str')
        if scope is not None:
            query_parameters['scope'] = self._serialize.query('scope', scope, 'str')
        self._send(http_method='DELETE',
                   location_id='e4f5c81e-e250-447b-9fef-bd48471bea5e',
                   version='7.2-preview.4',
                   route_values=route_values,
                   query_parameters=query_parameters)

    def get_containers(self, scope=None, artifact_uris=None):
        """GetContainers.
        [Preview API] Gets containers filtered by a comma separated list of artifact uris within the same scope, if not specified returns all containers
        :param str scope: A guid representing the scope of the container. This is often the project id.
        :param str artifact_uris:
        :rtype: [FileContainer]
        """
        query_parameters = {}
        if scope is not None:
            query_parameters['scope'] = self._serialize.query('scope', scope, 'str')
        if artifact_uris is not None:
            query_parameters['artifactUris'] = self._serialize.query('artifact_uris', artifact_uris, 'str')
        response = self._send(http_method='GET',
                              location_id='e4f5c81e-e250-447b-9fef-bd48471bea5e',
                              version='7.2-preview.4',
                              query_parameters=query_parameters)
        return self._deserialize('[FileContainer]', self._unwrap_collection(response))

    def get_items(self, container_id, scope=None, item_path=None, metadata=None, format=None, download_file_name=None, include_download_tickets=None, is_shallow=None, ignore_requested_media_type=None, include_blob_metadata=None, save_absolute_path=None, prefer_redirect=None):
        """GetItems.
        [Preview API] Gets the specified file container object in a format dependent upon the given parameters or HTTP Accept request header
        :param long container_id: The requested container Id
        :param str scope: A guid representing the scope of the container. This is often the project id.
        :param str item_path: The path to the item of interest
        :param bool metadata: If true, this overrides any specified format parameter or HTTP Accept request header to provide non-recursive information for the given itemPath
        :param str format: If specified, this overrides the HTTP Accept request header to return either 'json' or 'zip'.  If $format is specified, then api-version should also be specified as a query parameter.
        :param str download_file_name: If specified and returning other than JSON format, then this download name will be used (else defaults to itemPath)
        :param bool include_download_tickets:
        :param bool is_shallow: If true, returns only immediate children(files & folders) for the given itemPath. False will return all items recursively within itemPath.
        :param bool ignore_requested_media_type: Set to true to ignore the HTTP Accept request header. Default is false.
        :param bool include_blob_metadata:
        :param bool save_absolute_path: Set to false to not save the absolute path to the specified directory of the artifact in the returned archive. Works only for artifact directories. Default is true.
        :param bool prefer_redirect: Set to true to get the redirect response which leads to the stream with content. Default is false.
        :rtype: [FileContainerItem]
        """
        route_values = {}
        if container_id is not None:
            route_values['containerId'] = self._serialize.url('container_id', container_id, 'long')
        query_parameters = {}
        if scope is not None:
            query_parameters['scope'] = self._serialize.query('scope', scope, 'str')
        if item_path is not None:
            query_parameters['itemPath'] = self._serialize.query('item_path', item_path, 'str')
        if metadata is not None:
            query_parameters['metadata'] = self._serialize.query('metadata', metadata, 'bool')
        if format is not None:
            query_parameters['$format'] = self._serialize.query('format', format, 'str')
        if download_file_name is not None:
            query_parameters['downloadFileName'] = self._serialize.query('download_file_name', download_file_name, 'str')
        if include_download_tickets is not None:
            query_parameters['includeDownloadTickets'] = self._serialize.query('include_download_tickets', include_download_tickets, 'bool')
        if is_shallow is not None:
            query_parameters['isShallow'] = self._serialize.query('is_shallow', is_shallow, 'bool')
        if ignore_requested_media_type is not None:
            query_parameters['ignoreRequestedMediaType'] = self._serialize.query('ignore_requested_media_type', ignore_requested_media_type, 'bool')
        if include_blob_metadata is not None:
            query_parameters['includeBlobMetadata'] = self._serialize.query('include_blob_metadata', include_blob_metadata, 'bool')
        if save_absolute_path is not None:
            query_parameters['saveAbsolutePath'] = self._serialize.query('save_absolute_path', save_absolute_path, 'bool')
        if prefer_redirect is not None:
            query_parameters['preferRedirect'] = self._serialize.query('prefer_redirect', prefer_redirect, 'bool')
        response = self._send(http_method='GET',
                              location_id='e4f5c81e-e250-447b-9fef-bd48471bea5e',
                              version='7.2-preview.4',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[FileContainerItem]', self._unwrap_collection(response))

