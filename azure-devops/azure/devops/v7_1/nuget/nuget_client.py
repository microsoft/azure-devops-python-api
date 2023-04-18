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


class NuGetClient(Client):
    """NuGet
    :param str base_url: Service URL
    :param Authentication creds: Authenticated credentials.
    """

    def __init__(self, base_url=None, creds=None):
        super(NuGetClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = 'b3be7473-68ea-4a81-bfc7-9530baaa19ad'

    def download_package(self, feed_id, package_name, package_version, project=None, source_protocol_version=None, **kwargs):
        """DownloadPackage.
        [Preview API] Download a package version directly.
        :param str feed_id: Name or ID of the feed.
        :param str package_name: Name of the package.
        :param str package_version: Version of the package.
        :param str project: Project ID or project name
        :param str source_protocol_version: Unused
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
        query_parameters = {}
        if source_protocol_version is not None:
            query_parameters['sourceProtocolVersion'] = self._serialize.query('source_protocol_version', source_protocol_version, 'str')
        response = self._send(http_method='GET',
                              location_id='6ea81b8c-7386-490b-a71f-6cf23c80b388',
                              version='7.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='application/octet-stream')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def update_package_versions(self, batch_request, feed_id, project=None):
        """UpdatePackageVersions.
        [Preview API] Update several packages from a single feed in a single request. The updates to the packages do not happen atomically.
        :param :class:`<NuGetPackagesBatchRequest> <azure.devops.v7_1.nuget.models.NuGetPackagesBatchRequest>` batch_request: Information about the packages to update, the operation to perform, and its associated data.
        :param str feed_id: Name or ID of the feed.
        :param str project: Project ID or project name
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        content = self._serialize.body(batch_request, 'NuGetPackagesBatchRequest')
        self._send(http_method='POST',
                   location_id='00c58ea7-d55f-49de-b59f-983533ae11dc',
                   version='7.1-preview.1',
                   route_values=route_values,
                   content=content)

    def update_recycle_bin_package_versions(self, batch_request, feed_id, project=None):
        """UpdateRecycleBinPackageVersions.
        [Preview API] Delete or restore several package versions from the recycle bin.
        :param :class:`<NuGetPackagesBatchRequest> <azure.devops.v7_1.nuget.models.NuGetPackagesBatchRequest>` batch_request: Information about the packages to update, the operation to perform, and its associated data. <c>Operation</c> must be <c>PermanentDelete</c> or <c>RestoreToFeed</c>
        :param str feed_id: Name or ID of the feed.
        :param str project: Project ID or project name
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        content = self._serialize.body(batch_request, 'NuGetPackagesBatchRequest')
        self._send(http_method='POST',
                   location_id='6479ac16-32f4-40f7-aa96-9414de861352',
                   version='7.1-preview.1',
                   route_values=route_values,
                   content=content)

    def delete_package_version_from_recycle_bin(self, feed_id, package_name, package_version, project=None):
        """DeletePackageVersionFromRecycleBin.
        [Preview API] Delete a package version from a feed's recycle bin.
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
                   location_id='07e88775-e3cb-4408-bbe1-628e036fac8c',
                   version='7.1-preview.1',
                   route_values=route_values)

    def get_package_version_metadata_from_recycle_bin(self, feed_id, package_name, package_version, project=None):
        """GetPackageVersionMetadataFromRecycleBin.
        [Preview API] View a package version's deletion/recycled status
        :param str feed_id: Name or ID of the feed.
        :param str package_name: Name of the package.
        :param str package_version: Version of the package.
        :param str project: Project ID or project name
        :rtype: :class:`<NuGetPackageVersionDeletionState> <azure.devops.v7_1.nuget.models.NuGetPackageVersionDeletionState>`
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
                              location_id='07e88775-e3cb-4408-bbe1-628e036fac8c',
                              version='7.1-preview.1',
                              route_values=route_values)
        return self._deserialize('NuGetPackageVersionDeletionState', response)

    def restore_package_version_from_recycle_bin(self, package_version_details, feed_id, package_name, package_version, project=None):
        """RestorePackageVersionFromRecycleBin.
        [Preview API] Restore a package version from a feed's recycle bin back into the active feed.
        :param :class:`<NuGetRecycleBinPackageVersionDetails> <azure.devops.v7_1.nuget.models.NuGetRecycleBinPackageVersionDetails>` package_version_details: Set the 'Deleted' member to 'false' to apply the restore operation
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
        content = self._serialize.body(package_version_details, 'NuGetRecycleBinPackageVersionDetails')
        self._send(http_method='PATCH',
                   location_id='07e88775-e3cb-4408-bbe1-628e036fac8c',
                   version='7.1-preview.1',
                   route_values=route_values,
                   content=content)

    def get_upstreaming_behavior(self, feed_id, package_name, project=None):
        """GetUpstreamingBehavior.
        [Preview API] Get the upstreaming behavior of a package within the context of a feed
        :param str feed_id: The name or id of the feed
        :param str package_name: The name of the package
        :param str project: Project ID or project name
        :rtype: :class:`<UpstreamingBehavior> <azure.devops.v7_1.nuget.models.UpstreamingBehavior>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_name is not None:
            route_values['packageName'] = self._serialize.url('package_name', package_name, 'str')
        response = self._send(http_method='GET',
                              location_id='b41eec47-6472-4efa-bcd5-a2c5607b66ec',
                              version='7.1-preview.1',
                              route_values=route_values)
        return self._deserialize('UpstreamingBehavior', response)

    def set_upstreaming_behavior(self, feed_id, package_name, behavior, project=None):
        """SetUpstreamingBehavior.
        [Preview API] Set the upstreaming behavior of a package within the context of a feed
        :param str feed_id: The name or id of the feed
        :param str package_name: The name of the package
        :param :class:`<UpstreamingBehavior> <azure.devops.v7_1.nuget.models.UpstreamingBehavior>` behavior: The behavior to apply to the package within the scope of the feed
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
                   location_id='b41eec47-6472-4efa-bcd5-a2c5607b66ec',
                   version='7.1-preview.1',
                   route_values=route_values,
                   content=content)

    def delete_package_version(self, feed_id, package_name, package_version, project=None):
        """DeletePackageVersion.
        [Preview API] Send a package version from the feed to its paired recycle bin.
        :param str feed_id: Name or ID of the feed.
        :param str package_name: Name of the package to delete.
        :param str package_version: Version of the package to delete.
        :param str project: Project ID or project name
        :rtype: :class:`<Package> <azure.devops.v7_1.nuget.models.Package>`
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
                              location_id='36c9353b-e250-4c57-b040-513c186c3905',
                              version='7.1-preview.1',
                              route_values=route_values)
        return self._deserialize('Package', response)

    def get_package_version(self, feed_id, package_name, package_version, project=None, show_deleted=None):
        """GetPackageVersion.
        [Preview API] Get information about a package version.
        :param str feed_id: Name or ID of the feed.
        :param str package_name: Name of the package.
        :param str package_version: Version of the package.
        :param str project: Project ID or project name
        :param bool show_deleted: True to include deleted packages in the response.
        :rtype: :class:`<Package> <azure.devops.v7_1.nuget.models.Package>`
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
                              location_id='36c9353b-e250-4c57-b040-513c186c3905',
                              version='7.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('Package', response)

    def update_package_version(self, package_version_details, feed_id, package_name, package_version, project=None):
        """UpdatePackageVersion.
        [Preview API] Set mutable state on a package version.
        :param :class:`<PackageVersionDetails> <azure.devops.v7_1.nuget.models.PackageVersionDetails>` package_version_details: New state to apply to the referenced package.
        :param str feed_id: Name or ID of the feed.
        :param str package_name: Name of the package to update.
        :param str package_version: Version of the package to update.
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
                   location_id='36c9353b-e250-4c57-b040-513c186c3905',
                   version='7.1-preview.1',
                   route_values=route_values,
                   content=content)

