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


class MavenClient(Client):
    """Maven
    :param str base_url: Service URL
    :param Authentication creds: Authenticated credentials.
    """

    def __init__(self, base_url=None, creds=None):
        super(MavenClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = '6f7f8c07-ff36-473c-bcf3-bd6cc9b6c066'

    def download_package(self, feed_id, group_id, artifact_id, version, file_name, project=None, **kwargs):
        """DownloadPackage.
        [Preview API] Fulfills Maven package file download requests by either returning the URL of the requested package file or, in the case of Azure DevOps Server (OnPrem), returning the content as a stream.
        :param str feed_id: Name or ID of the feed.
        :param str group_id: GroupId of the maven package
        :param str artifact_id: ArtifactId of the maven package
        :param str version: Version of the package
        :param str file_name: File name to download
        :param str project: Project ID or project name
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if group_id is not None:
            route_values['groupId'] = self._serialize.url('group_id', group_id, 'str')
        if artifact_id is not None:
            route_values['artifactId'] = self._serialize.url('artifact_id', artifact_id, 'str')
        if version is not None:
            route_values['version'] = self._serialize.url('version', version, 'str')
        if file_name is not None:
            route_values['fileName'] = self._serialize.url('file_name', file_name, 'str')
        response = self._send(http_method='GET',
                              location_id='c338d4b5-d30a-47e2-95b7-f157ef558833',
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
        :param :class:`<MavenPackagesBatchRequest> <azure.devops.v7_0.maven.models.MavenPackagesBatchRequest>` batch_request: Information about the packages to update, the operation to perform, and its associated data.
        :param str feed_id: Feed which contains the packages to update.
        :param str project: Project ID or project name
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        content = self._serialize.body(batch_request, 'MavenPackagesBatchRequest')
        self._send(http_method='POST',
                   location_id='b7c586b0-d947-4d35-811a-f1161de80e6c',
                   version='7.0-preview.1',
                   route_values=route_values,
                   content=content)

    def update_recycle_bin_packages(self, batch_request, feed, project=None):
        """UpdateRecycleBinPackages.
        [Preview API] Delete or restore several package versions from the recycle bin.
        :param :class:`<MavenPackagesBatchRequest> <azure.devops.v7_0.maven.models.MavenPackagesBatchRequest>` batch_request: Information about the packages to update, the operation to perform, and its associated data.
        :param str feed:
        :param str project: Project ID or project name
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed is not None:
            route_values['feed'] = self._serialize.url('feed', feed, 'str')
        content = self._serialize.body(batch_request, 'MavenPackagesBatchRequest')
        self._send(http_method='POST',
                   location_id='5dd6f547-c76f-4d9d-b2ec-4720feda641f',
                   version='7.0-preview.1',
                   route_values=route_values,
                   content=content)

    def delete_package_version_from_recycle_bin(self, feed, group_id, artifact_id, version, project=None):
        """DeletePackageVersionFromRecycleBin.
        [Preview API] Permanently delete a package from a feed's recycle bin.
        :param str feed: Name or ID of the feed.
        :param str group_id: Group ID of the package.
        :param str artifact_id: Artifact ID of the package.
        :param str version: Version of the package.
        :param str project: Project ID or project name
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed is not None:
            route_values['feed'] = self._serialize.url('feed', feed, 'str')
        if group_id is not None:
            route_values['groupId'] = self._serialize.url('group_id', group_id, 'str')
        if artifact_id is not None:
            route_values['artifactId'] = self._serialize.url('artifact_id', artifact_id, 'str')
        if version is not None:
            route_values['version'] = self._serialize.url('version', version, 'str')
        self._send(http_method='DELETE',
                   location_id='f67e10eb-1254-4953-add7-d49b83a16c9f',
                   version='7.0-preview.1',
                   route_values=route_values)

    def get_package_version_metadata_from_recycle_bin(self, feed, group_id, artifact_id, version, project=None):
        """GetPackageVersionMetadataFromRecycleBin.
        [Preview API] Get information about a package version in the recycle bin.
        :param str feed: Name or ID of the feed.
        :param str group_id: Group ID of the package.
        :param str artifact_id: Artifact ID of the package.
        :param str version: Version of the package.
        :param str project: Project ID or project name
        :rtype: :class:`<MavenPackageVersionDeletionState> <azure.devops.v7_0.maven.models.MavenPackageVersionDeletionState>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed is not None:
            route_values['feed'] = self._serialize.url('feed', feed, 'str')
        if group_id is not None:
            route_values['groupId'] = self._serialize.url('group_id', group_id, 'str')
        if artifact_id is not None:
            route_values['artifactId'] = self._serialize.url('artifact_id', artifact_id, 'str')
        if version is not None:
            route_values['version'] = self._serialize.url('version', version, 'str')
        response = self._send(http_method='GET',
                              location_id='f67e10eb-1254-4953-add7-d49b83a16c9f',
                              version='7.0-preview.1',
                              route_values=route_values)
        return self._deserialize('MavenPackageVersionDeletionState', response)

    def restore_package_version_from_recycle_bin(self, package_version_details, feed, group_id, artifact_id, version, project=None):
        """RestorePackageVersionFromRecycleBin.
        [Preview API] Restore a package version from the recycle bin to its associated feed.
        :param :class:`<MavenRecycleBinPackageVersionDetails> <azure.devops.v7_0.maven.models.MavenRecycleBinPackageVersionDetails>` package_version_details: Set the 'Deleted' property to false to restore the package.
        :param str feed: Name or ID of the feed.
        :param str group_id: Group ID of the package.
        :param str artifact_id: Artifact ID of the package.
        :param str version: Version of the package.
        :param str project: Project ID or project name
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed is not None:
            route_values['feed'] = self._serialize.url('feed', feed, 'str')
        if group_id is not None:
            route_values['groupId'] = self._serialize.url('group_id', group_id, 'str')
        if artifact_id is not None:
            route_values['artifactId'] = self._serialize.url('artifact_id', artifact_id, 'str')
        if version is not None:
            route_values['version'] = self._serialize.url('version', version, 'str')
        content = self._serialize.body(package_version_details, 'MavenRecycleBinPackageVersionDetails')
        self._send(http_method='PATCH',
                   location_id='f67e10eb-1254-4953-add7-d49b83a16c9f',
                   version='7.0-preview.1',
                   route_values=route_values,
                   content=content)

    def get_upstreaming_behavior(self, feed, group_id, artifact_id, project=None):
        """GetUpstreamingBehavior.
        [Preview API] Get the upstreaming behavior of a package within the context of a feed
        :param str feed: The name or id of the feed
        :param str group_id: The group id of the package
        :param str artifact_id: The artifact id of the package
        :param str project: Project ID or project name
        :rtype: :class:`<UpstreamingBehavior> <azure.devops.v7_0.maven.models.UpstreamingBehavior>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed is not None:
            route_values['feed'] = self._serialize.url('feed', feed, 'str')
        if group_id is not None:
            route_values['groupId'] = self._serialize.url('group_id', group_id, 'str')
        if artifact_id is not None:
            route_values['artifactId'] = self._serialize.url('artifact_id', artifact_id, 'str')
        response = self._send(http_method='GET',
                              location_id='fba7ba8c-d1f5-4aeb-8f5d-f017a7d5e719',
                              version='7.0-preview.1',
                              route_values=route_values)
        return self._deserialize('UpstreamingBehavior', response)

    def set_upstreaming_behavior(self, feed, group_id, artifact_id, behavior, project=None):
        """SetUpstreamingBehavior.
        [Preview API] Set the upstreaming behavior of a package within the context of a feed
        :param str feed: The name or id of the feed
        :param str group_id:
        :param str artifact_id:
        :param :class:`<UpstreamingBehavior> <azure.devops.v7_0.maven.models.UpstreamingBehavior>` behavior: The behavior to apply to the package within the scope of the feed
        :param str project: Project ID or project name
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed is not None:
            route_values['feed'] = self._serialize.url('feed', feed, 'str')
        if group_id is not None:
            route_values['groupId'] = self._serialize.url('group_id', group_id, 'str')
        if artifact_id is not None:
            route_values['artifactId'] = self._serialize.url('artifact_id', artifact_id, 'str')
        content = self._serialize.body(behavior, 'UpstreamingBehavior')
        self._send(http_method='PATCH',
                   location_id='fba7ba8c-d1f5-4aeb-8f5d-f017a7d5e719',
                   version='7.0-preview.1',
                   route_values=route_values,
                   content=content)

    def get_package_version(self, feed, group_id, artifact_id, version, project=None, show_deleted=None):
        """GetPackageVersion.
        [Preview API] Get information about a package version.
        :param str feed: Name or ID of the feed.
        :param str group_id: Group ID of the package.
        :param str artifact_id: Artifact ID of the package.
        :param str version: Version of the package.
        :param str project: Project ID or project name
        :param bool show_deleted: True to show information for deleted packages.
        :rtype: :class:`<Package> <azure.devops.v7_0.maven.models.Package>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed is not None:
            route_values['feed'] = self._serialize.url('feed', feed, 'str')
        if group_id is not None:
            route_values['groupId'] = self._serialize.url('group_id', group_id, 'str')
        if artifact_id is not None:
            route_values['artifactId'] = self._serialize.url('artifact_id', artifact_id, 'str')
        if version is not None:
            route_values['version'] = self._serialize.url('version', version, 'str')
        query_parameters = {}
        if show_deleted is not None:
            query_parameters['showDeleted'] = self._serialize.query('show_deleted', show_deleted, 'bool')
        response = self._send(http_method='GET',
                              location_id='180ed967-377a-4112-986b-607adb14ded4',
                              version='7.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('Package', response)

    def package_delete(self, feed, group_id, artifact_id, version, project=None):
        """PackageDelete.
        [Preview API] Delete a package version from the feed and move it to the feed's recycle bin.
        :param str feed: Name or ID of the feed.
        :param str group_id: Group ID of the package.
        :param str artifact_id: Artifact ID of the package.
        :param str version: Version of the package.
        :param str project: Project ID or project name
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed is not None:
            route_values['feed'] = self._serialize.url('feed', feed, 'str')
        if group_id is not None:
            route_values['groupId'] = self._serialize.url('group_id', group_id, 'str')
        if artifact_id is not None:
            route_values['artifactId'] = self._serialize.url('artifact_id', artifact_id, 'str')
        if version is not None:
            route_values['version'] = self._serialize.url('version', version, 'str')
        self._send(http_method='DELETE',
                   location_id='180ed967-377a-4112-986b-607adb14ded4',
                   version='7.0-preview.1',
                   route_values=route_values)

    def update_package_version(self, package_version_details, feed, group_id, artifact_id, version, project=None):
        """UpdatePackageVersion.
        [Preview API] Update state for a package version.
        :param :class:`<PackageVersionDetails> <azure.devops.v7_0.maven.models.PackageVersionDetails>` package_version_details: Details to be updated.
        :param str feed: Name or ID of the feed.
        :param str group_id: Group ID of the package.
        :param str artifact_id: Artifact ID of the package.
        :param str version: Version of the package.
        :param str project: Project ID or project name
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed is not None:
            route_values['feed'] = self._serialize.url('feed', feed, 'str')
        if group_id is not None:
            route_values['groupId'] = self._serialize.url('group_id', group_id, 'str')
        if artifact_id is not None:
            route_values['artifactId'] = self._serialize.url('artifact_id', artifact_id, 'str')
        if version is not None:
            route_values['version'] = self._serialize.url('version', version, 'str')
        content = self._serialize.body(package_version_details, 'PackageVersionDetails')
        self._send(http_method='PATCH',
                   location_id='180ed967-377a-4112-986b-607adb14ded4',
                   version='7.0-preview.1',
                   route_values=route_values,
                   content=content)

