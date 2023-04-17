# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from . import models


class PyPiApiClient(Client):
    """PyPiApi
    :param str base_url: Service URL
    :param Authentication creds: Authenticated credentials.
    """

    def __init__(self, base_url=None, creds=None):
        super(PyPiApiClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = '92f0314b-06c5-46e0-abe7-15fd9d13276a'

    def download_package(self, feed_id, package_name, package_version, file_name, project=None, **kwargs):
        """DownloadPackage.
        [Preview API] Download a python package file directly. This API is intended for manual UI download options, not for programmatic access and scripting.
        :param str feed_id: Name or ID of the feed.
        :param str package_name: Name of the package.
        :param str package_version: Version of the package.
        :param str file_name: Name of the file in the package
        :param str project: Project ID or project name
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_name is not None:
            route_values['packageName'] = self._serialize.url('package_name', package_name, 'str')
        if package_version is not None:
            route_values['packageVersion'] = self._serialize.url('package_version', package_version, 'str')
        if file_name is not None:
            route_values['fileName'] = self._serialize.url('file_name', file_name, 'str')
        response = self._send(http_method='GET',
                              location_id='97218bae-a64d-4381-9257-b5b7951f0b98',
                              version='7.0-preview.1',
                              route_values=route_values,
                              accept_media_type='application/octet-stream')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def update_package_versions(self, batch_request, feed_id, project=None):
        """UpdatePackageVersions.
        [Preview API] Update several packages from a single feed in a single request. The updates to the packages do not happen atomically.
        :param :class:`<PyPiPackagesBatchRequest> <azure.devops.v7_0.py_pi_api.models.PyPiPackagesBatchRequest>` batch_request: Information about the packages to update, the operation to perform, and its associated data.
        :param str feed_id: Name or ID of the feed.
        :param str project: Project ID or project name
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        content = self._serialize.body(batch_request, 'PyPiPackagesBatchRequest')
        self._send(http_method='POST',
                   location_id='4e53d561-70c1-4c98-b937-0f22acb27b0b',
                   version='7.0-preview.1',
                   route_values=route_values,
                   content=content)

    def update_recycle_bin_package_versions(self, batch_request, feed_id, project=None):
        """UpdateRecycleBinPackageVersions.
        [Preview API] Delete or restore several package versions from the recycle bin.
        :param :class:`<PyPiPackagesBatchRequest> <azure.devops.v7_0.py_pi_api.models.PyPiPackagesBatchRequest>` batch_request: Information about the packages to update, the operation to perform, and its associated data. <c>Operation</c> must be <c>PermanentDelete</c> or <c>RestoreToFeed</c>
        :param str feed_id: Feed which contains the packages to update.
        :param str project: Project ID or project name
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        content = self._serialize.body(batch_request, 'PyPiPackagesBatchRequest')
        self._send(http_method='POST',
                   location_id='d2d89918-c69e-4ef4-b357-1c3ccb4d28d2',
                   version='7.0-preview.1',
                   route_values=route_values,
                   content=content)

    def delete_package_version_from_recycle_bin(self, feed_id, package_name, package_version, project=None):
        """DeletePackageVersionFromRecycleBin.
        [Preview API] Delete a package version from the feed, moving it to the recycle bin.
        :param str feed_id: Name or ID of the feed.
        :param str package_name: Name of the package.
        :param str package_version: Version of the package.
        :param str project: Project ID or project name
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_name is not None:
            route_values['packageName'] = self._serialize.url('package_name', package_name, 'str')
        if package_version is not None:
            route_values['packageVersion'] = self._serialize.url('package_version', package_version, 'str')
        self._send(http_method='DELETE',
                   location_id='07143752-3d94-45fd-86c2-0c77ed87847b',
                   version='7.0-preview.1',
                   route_values=route_values)

    def get_package_version_metadata_from_recycle_bin(self, feed_id, package_name, package_version, project=None):
        """GetPackageVersionMetadataFromRecycleBin.
        [Preview API] Get information about a package version in the recycle bin.
        :param str feed_id: Name or ID of the feed.
        :param str package_name: Name of the package.
        :param str package_version: Version of the package.
        :param str project: Project ID or project name
        :rtype: :class:`<PyPiPackageVersionDeletionState> <azure.devops.v7_0.py_pi_api.models.PyPiPackageVersionDeletionState>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_name is not None:
            route_values['packageName'] = self._serialize.url('package_name', package_name, 'str')
        if package_version is not None:
            route_values['packageVersion'] = self._serialize.url('package_version', package_version, 'str')
        response = self._send(http_method='GET',
                              location_id='07143752-3d94-45fd-86c2-0c77ed87847b',
                              version='7.0-preview.1',
                              route_values=route_values)
        return self._deserialize('PyPiPackageVersionDeletionState', response)

    def restore_package_version_from_recycle_bin(self, package_version_details, feed_id, package_name, package_version, project=None):
        """RestorePackageVersionFromRecycleBin.
        [Preview API] Restore a package version from the recycle bin to its associated feed.
        :param :class:`<PyPiRecycleBinPackageVersionDetails> <azure.devops.v7_0.py_pi_api.models.PyPiRecycleBinPackageVersionDetails>` package_version_details: Set the 'Deleted' state to 'false' to restore the package to its feed.
        :param str feed_id: Name or ID of the feed.
        :param str package_name: Name of the package.
        :param str package_version: Version of the package.
        :param str project: Project ID or project name
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_name is not None:
            route_values['packageName'] = self._serialize.url('package_name', package_name, 'str')
        if package_version is not None:
            route_values['packageVersion'] = self._serialize.url('package_version', package_version, 'str')
        content = self._serialize.body(package_version_details, 'PyPiRecycleBinPackageVersionDetails')
        self._send(http_method='PATCH',
                   location_id='07143752-3d94-45fd-86c2-0c77ed87847b',
                   version='7.0-preview.1',
                   route_values=route_values,
                   content=content)

    def get_upstreaming_behavior(self, feed_id, package_name, project=None):
        """GetUpstreamingBehavior.
        [Preview API] Get the upstreaming behavior of a package within the context of a feed
        :param str feed_id: The name or id of the feed
        :param str package_name: The name of the package
        :param str project: Project ID or project name
        :rtype: :class:`<UpstreamingBehavior> <azure.devops.v7_0.py_pi_api.models.UpstreamingBehavior>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_name is not None:
            route_values['packageName'] = self._serialize.url('package_name', package_name, 'str')
        response = self._send(http_method='GET',
                              location_id='21b8c9a7-7080-45be-a5ba-e50bb4c18130',
                              version='7.0-preview.1',
                              route_values=route_values)
        return self._deserialize('UpstreamingBehavior', response)

    def set_upstreaming_behavior(self, feed_id, package_name, behavior, project=None):
        """SetUpstreamingBehavior.
        [Preview API] Set the upstreaming behavior of a package within the context of a feed
        :param str feed_id: The name or id of the feed
        :param str package_name: The name of the package
        :param :class:`<UpstreamingBehavior> <azure.devops.v7_0.py_pi_api.models.UpstreamingBehavior>` behavior: The behavior to apply to the package within the scope of the feed
        :param str project: Project ID or project name
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_name is not None:
            route_values['packageName'] = self._serialize.url('package_name', package_name, 'str')
        content = self._serialize.body(behavior, 'UpstreamingBehavior')
        self._send(http_method='PATCH',
                   location_id='21b8c9a7-7080-45be-a5ba-e50bb4c18130',
                   version='7.0-preview.1',
                   route_values=route_values,
                   content=content)

    def delete_package_version(self, feed_id, package_name, package_version, project=None):
        """DeletePackageVersion.
        [Preview API] Delete a package version, moving it to the recycle bin.
        :param str feed_id: Name or ID of the feed.
        :param str package_name: Name of the package.
        :param str package_version: Version of the package.
        :param str project: Project ID or project name
        :rtype: :class:`<Package> <azure.devops.v7_0.py_pi_api.models.Package>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_name is not None:
            route_values['packageName'] = self._serialize.url('package_name', package_name, 'str')
        if package_version is not None:
            route_values['packageVersion'] = self._serialize.url('package_version', package_version, 'str')
        response = self._send(http_method='DELETE',
                              location_id='d146ac7e-9e3f-4448-b956-f9bb3bdf9b2e',
                              version='7.0-preview.1',
                              route_values=route_values)
        return self._deserialize('Package', response)

    def get_package_version(self, feed_id, package_name, package_version, project=None, show_deleted=None):
        """GetPackageVersion.
        [Preview API] Get information about a package version.
        :param str feed_id: Name or ID of the feed.
        :param str package_name: Name of the package.
        :param str package_version: Version of the package.
        :param str project: Project ID or project name
        :param bool show_deleted: True to show information for deleted package versions.
        :rtype: :class:`<Package> <azure.devops.v7_0.py_pi_api.models.Package>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_name is not None:
            route_values['packageName'] = self._serialize.url('package_name', package_name, 'str')
        if package_version is not None:
            route_values['packageVersion'] = self._serialize.url('package_version', package_version, 'str')
        query_parameters = {}
        if show_deleted is not None:
            query_parameters['showDeleted'] = self._serialize.query('show_deleted', show_deleted, 'bool')
        response = self._send(http_method='GET',
                              location_id='d146ac7e-9e3f-4448-b956-f9bb3bdf9b2e',
                              version='7.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('Package', response)

    def update_package_version(self, package_version_details, feed_id, package_name, package_version, project=None):
        """UpdatePackageVersion.
        [Preview API] Update state for a package version.
        :param :class:`<PackageVersionDetails> <azure.devops.v7_0.py_pi_api.models.PackageVersionDetails>` package_version_details: Details to be updated.
        :param str feed_id: Name or ID of the feed.
        :param str package_name: Name of the package.
        :param str package_version: Version of the package.
        :param str project: Project ID or project name
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_name is not None:
            route_values['packageName'] = self._serialize.url('package_name', package_name, 'str')
        if package_version is not None:
            route_values['packageVersion'] = self._serialize.url('package_version', package_version, 'str')
        content = self._serialize.body(package_version_details, 'PackageVersionDetails')
        self._send(http_method='PATCH',
                   location_id='d146ac7e-9e3f-4448-b956-f9bb3bdf9b2e',
                   version='7.0-preview.1',
                   route_values=route_values,
                   content=content)

