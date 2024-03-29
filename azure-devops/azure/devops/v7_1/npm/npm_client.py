﻿# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from . import models


class NpmClient(Client):
    """Npm
    :param str base_url: Service URL
    :param Authentication creds: Authenticated credentials.
    """

    def __init__(self, base_url=None, creds=None):
        super(NpmClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = '4c83cfc1-f33a-477e-a789-29d38ffca52e'

    def get_content_scoped_package(self, feed_id, package_scope, unscoped_package_name, package_version, project=None, **kwargs):
        """GetContentScopedPackage.
        [Preview API]
        :param str feed_id:
        :param str package_scope:
        :param str unscoped_package_name:
        :param str package_version:
        :param str project: Project ID or project name
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_scope is not None:
            route_values['packageScope'] = self._serialize.url('package_scope', package_scope, 'str')
        if unscoped_package_name is not None:
            route_values['unscopedPackageName'] = self._serialize.url('unscoped_package_name', unscoped_package_name, 'str')
        if package_version is not None:
            route_values['packageVersion'] = self._serialize.url('package_version', package_version, 'str')
        response = self._send(http_method='GET',
                              location_id='09a4eafd-123a-495c-979c-0eda7bdb9a14',
                              version='7.1-preview.1',
                              route_values=route_values,
                              accept_media_type='application/octet-stream')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_content_unscoped_package(self, feed_id, package_name, package_version, project=None, **kwargs):
        """GetContentUnscopedPackage.
        [Preview API] Get an unscoped npm package.
        :param str feed_id: Name or ID of the feed.
        :param str package_name: Name of the package.
        :param str package_version: Version of the package.
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
        response = self._send(http_method='GET',
                              location_id='75caa482-cb1e-47cd-9f2c-c048a4b7a43e',
                              version='7.1-preview.1',
                              route_values=route_values,
                              accept_media_type='application/octet-stream')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def update_packages(self, batch_request, feed_id, project=None):
        """UpdatePackages.
        [Preview API] Update several packages from a single feed in a single request. The updates to the packages do not happen atomically.
        :param :class:`<NpmPackagesBatchRequest> <azure.devops.v7_1.npm.models.NpmPackagesBatchRequest>` batch_request: Information about the packages to update, the operation to perform, and its associated data.
        :param str feed_id: Name or ID of the feed.
        :param str project: Project ID or project name
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        content = self._serialize.body(batch_request, 'NpmPackagesBatchRequest')
        self._send(http_method='POST',
                   location_id='06f34005-bbb2-41f4-88f5-23e03a99bb12',
                   version='7.1-preview.1',
                   route_values=route_values,
                   content=content)

    def get_readme_scoped_package(self, feed_id, package_scope, unscoped_package_name, package_version, project=None, **kwargs):
        """GetReadmeScopedPackage.
        [Preview API] Get the Readme for a package version with an npm scope.
        :param str feed_id: Name or ID of the feed.
        :param str package_scope: Scope of the package (the 'scope' part of @scope\name)
        :param str unscoped_package_name: Name of the package (the 'name' part of @scope\name)
        :param str package_version: Version of the package.
        :param str project: Project ID or project name
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_scope is not None:
            route_values['packageScope'] = self._serialize.url('package_scope', package_scope, 'str')
        if unscoped_package_name is not None:
            route_values['unscopedPackageName'] = self._serialize.url('unscoped_package_name', unscoped_package_name, 'str')
        if package_version is not None:
            route_values['packageVersion'] = self._serialize.url('package_version', package_version, 'str')
        response = self._send(http_method='GET',
                              location_id='6d4db777-7e4a-43b2-afad-779a1d197301',
                              version='7.1-preview.1',
                              route_values=route_values,
                              accept_media_type='text/plain')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_readme_unscoped_package(self, feed_id, package_name, package_version, project=None, **kwargs):
        """GetReadmeUnscopedPackage.
        [Preview API] Get the Readme for a package version that has no npm scope.
        :param str feed_id: Name or ID of the feed.
        :param str package_name: Name of the package.
        :param str package_version: Version of the package.
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
        response = self._send(http_method='GET',
                              location_id='1099a396-b310-41d4-a4b6-33d134ce3fcf',
                              version='7.1-preview.1',
                              route_values=route_values,
                              accept_media_type='text/plain')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def update_recycle_bin_packages(self, batch_request, feed_id, project=None):
        """UpdateRecycleBinPackages.
        [Preview API] Delete or restore several package versions from the recycle bin.
        :param :class:`<NpmPackagesBatchRequest> <azure.devops.v7_1.npm.models.NpmPackagesBatchRequest>` batch_request: Information about the packages to update, the operation to perform, and its associated data.
        :param str feed_id: Name or ID of the feed.
        :param str project: Project ID or project name
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        content = self._serialize.body(batch_request, 'NpmPackagesBatchRequest')
        self._send(http_method='POST',
                   location_id='eefe03ef-a6a2-4a7a-a0ec-2e65a5efd64c',
                   version='7.1-preview.1',
                   route_values=route_values,
                   content=content)

    def delete_scoped_package_version_from_recycle_bin(self, feed_id, package_scope, unscoped_package_name, package_version, project=None):
        """DeleteScopedPackageVersionFromRecycleBin.
        [Preview API] Delete a package version with an npm scope from the recycle bin.
        :param str feed_id: Name or ID of the feed.
        :param str package_scope: Scope of the package (the 'scope' part of @scope/name).
        :param str unscoped_package_name: Name of the package (the 'name' part of @scope/name).
        :param str package_version: Version of the package.
        :param str project: Project ID or project name
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_scope is not None:
            route_values['packageScope'] = self._serialize.url('package_scope', package_scope, 'str')
        if unscoped_package_name is not None:
            route_values['unscopedPackageName'] = self._serialize.url('unscoped_package_name', unscoped_package_name, 'str')
        if package_version is not None:
            route_values['packageVersion'] = self._serialize.url('package_version', package_version, 'str')
        self._send(http_method='DELETE',
                   location_id='220f45eb-94a5-432c-902a-5b8c6372e415',
                   version='7.1-preview.1',
                   route_values=route_values)

    def get_scoped_package_version_metadata_from_recycle_bin(self, feed_id, package_scope, unscoped_package_name, package_version, project=None):
        """GetScopedPackageVersionMetadataFromRecycleBin.
        [Preview API] Get information about a scoped package version in the recycle bin.
        :param str feed_id: Name or ID of the feed.
        :param str package_scope: Scope of the package (the 'scope' part of @scope/name)
        :param str unscoped_package_name: Name of the package (the 'name' part of @scope/name).
        :param str package_version: Version of the package.
        :param str project: Project ID or project name
        :rtype: :class:`<NpmPackageVersionDeletionState> <azure.devops.v7_1.npm.models.NpmPackageVersionDeletionState>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_scope is not None:
            route_values['packageScope'] = self._serialize.url('package_scope', package_scope, 'str')
        if unscoped_package_name is not None:
            route_values['unscopedPackageName'] = self._serialize.url('unscoped_package_name', unscoped_package_name, 'str')
        if package_version is not None:
            route_values['packageVersion'] = self._serialize.url('package_version', package_version, 'str')
        response = self._send(http_method='GET',
                              location_id='220f45eb-94a5-432c-902a-5b8c6372e415',
                              version='7.1-preview.1',
                              route_values=route_values)
        return self._deserialize('NpmPackageVersionDeletionState', response)

    def restore_scoped_package_version_from_recycle_bin(self, package_version_details, feed_id, package_scope, unscoped_package_name, package_version, project=None):
        """RestoreScopedPackageVersionFromRecycleBin.
        [Preview API] Restore a package version with an npm scope from the recycle bin to its feed.
        :param :class:`<NpmRecycleBinPackageVersionDetails> <azure.devops.v7_1.npm.models.NpmRecycleBinPackageVersionDetails>` package_version_details:
        :param str feed_id: Name or ID of the feed.
        :param str package_scope: Scope of the package (the 'scope' part of @scope/name).
        :param str unscoped_package_name: Name of the package (the 'name' part of @scope/name).
        :param str package_version: Version of the package.
        :param str project: Project ID or project name
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_scope is not None:
            route_values['packageScope'] = self._serialize.url('package_scope', package_scope, 'str')
        if unscoped_package_name is not None:
            route_values['unscopedPackageName'] = self._serialize.url('unscoped_package_name', unscoped_package_name, 'str')
        if package_version is not None:
            route_values['packageVersion'] = self._serialize.url('package_version', package_version, 'str')
        content = self._serialize.body(package_version_details, 'NpmRecycleBinPackageVersionDetails')
        self._send(http_method='PATCH',
                   location_id='220f45eb-94a5-432c-902a-5b8c6372e415',
                   version='7.1-preview.1',
                   route_values=route_values,
                   content=content)

    def delete_package_version_from_recycle_bin(self, feed_id, package_name, package_version, project=None):
        """DeletePackageVersionFromRecycleBin.
        [Preview API] Delete a package version without an npm scope from the recycle bin.
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
                   location_id='63a4f31f-e92b-4ee4-bf92-22d485e73bef',
                   version='7.1-preview.1',
                   route_values=route_values)

    def get_package_version_metadata_from_recycle_bin(self, feed_id, package_name, package_version, project=None):
        """GetPackageVersionMetadataFromRecycleBin.
        [Preview API] Get information about an unscoped package version in the recycle bin.
        :param str feed_id: Name or ID of the feed.
        :param str package_name: Name of the package.
        :param str package_version: Version of the package.
        :param str project: Project ID or project name
        :rtype: :class:`<NpmPackageVersionDeletionState> <azure.devops.v7_1.npm.models.NpmPackageVersionDeletionState>`
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
                              location_id='63a4f31f-e92b-4ee4-bf92-22d485e73bef',
                              version='7.1-preview.1',
                              route_values=route_values)
        return self._deserialize('NpmPackageVersionDeletionState', response)

    def restore_package_version_from_recycle_bin(self, package_version_details, feed_id, package_name, package_version, project=None):
        """RestorePackageVersionFromRecycleBin.
        [Preview API] Restore a package version without an npm scope from the recycle bin to its feed.
        :param :class:`<NpmRecycleBinPackageVersionDetails> <azure.devops.v7_1.npm.models.NpmRecycleBinPackageVersionDetails>` package_version_details:
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
        content = self._serialize.body(package_version_details, 'NpmRecycleBinPackageVersionDetails')
        self._send(http_method='PATCH',
                   location_id='63a4f31f-e92b-4ee4-bf92-22d485e73bef',
                   version='7.1-preview.1',
                   route_values=route_values,
                   content=content)

    def get_scoped_upstreaming_behavior(self, feed_id, package_scope, unscoped_package_name, project=None):
        """GetScopedUpstreamingBehavior.
        [Preview API] Get the upstreaming behavior of the (scoped) package within the context of a feed
        :param str feed_id: The name or id of the feed
        :param str package_scope: The scope of the package
        :param str unscoped_package_name: The name of the scoped package
        :param str project: Project ID or project name
        :rtype: :class:`<UpstreamingBehavior> <azure.devops.v7_1.npm.models.UpstreamingBehavior>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_scope is not None:
            route_values['packageScope'] = self._serialize.url('package_scope', package_scope, 'str')
        if unscoped_package_name is not None:
            route_values['unscopedPackageName'] = self._serialize.url('unscoped_package_name', unscoped_package_name, 'str')
        response = self._send(http_method='GET',
                              location_id='9859c187-f6ec-41b0-862d-8003b3b404e0',
                              version='7.1-preview.1',
                              route_values=route_values)
        return self._deserialize('UpstreamingBehavior', response)

    def set_scoped_upstreaming_behavior(self, feed_id, package_scope, unscoped_package_name, behavior, project=None):
        """SetScopedUpstreamingBehavior.
        [Preview API] Set the upstreaming behavior of a (scoped) package within the context of a feed
        :param str feed_id: The name or id of the feed
        :param str package_scope: The scope of the package
        :param str unscoped_package_name: The name of the scoped package
        :param :class:`<UpstreamingBehavior> <azure.devops.v7_1.npm.models.UpstreamingBehavior>` behavior: The behavior to apply to the scoped package within the scope of the feed
        :param str project: Project ID or project name
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_scope is not None:
            route_values['packageScope'] = self._serialize.url('package_scope', package_scope, 'str')
        if unscoped_package_name is not None:
            route_values['unscopedPackageName'] = self._serialize.url('unscoped_package_name', unscoped_package_name, 'str')
        content = self._serialize.body(behavior, 'UpstreamingBehavior')
        self._send(http_method='PATCH',
                   location_id='9859c187-f6ec-41b0-862d-8003b3b404e0',
                   version='7.1-preview.1',
                   route_values=route_values,
                   content=content)

    def get_upstreaming_behavior(self, feed_id, package_name, project=None):
        """GetUpstreamingBehavior.
        [Preview API] Get the upstreaming behavior of the (unscoped) package within the context of a feed
        :param str feed_id: The name or id of the feed
        :param str package_name: The name of the package
        :param str project: Project ID or project name
        :rtype: :class:`<UpstreamingBehavior> <azure.devops.v7_1.npm.models.UpstreamingBehavior>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_name is not None:
            route_values['packageName'] = self._serialize.url('package_name', package_name, 'str')
        response = self._send(http_method='GET',
                              location_id='e27a45d3-711b-41cb-a47a-ae669b6e9076',
                              version='7.1-preview.1',
                              route_values=route_values)
        return self._deserialize('UpstreamingBehavior', response)

    def set_upstreaming_behavior(self, feed_id, package_name, behavior, project=None):
        """SetUpstreamingBehavior.
        [Preview API] Set the upstreaming behavior of a (scoped) package within the context of a feed
        :param str feed_id: The name or id of the feed
        :param str package_name: The name of the package
        :param :class:`<UpstreamingBehavior> <azure.devops.v7_1.npm.models.UpstreamingBehavior>` behavior: The behavior to apply to the scoped package within the scope of the feed
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
                   location_id='e27a45d3-711b-41cb-a47a-ae669b6e9076',
                   version='7.1-preview.1',
                   route_values=route_values,
                   content=content)

    def get_scoped_package_info(self, feed_id, package_scope, unscoped_package_name, package_version, project=None):
        """GetScopedPackageInfo.
        [Preview API] Get information about a scoped package version (such as @scope/name).
        :param str feed_id: Name or ID of the feed.
        :param str package_scope: Scope of the package (the 'scope' part of @scope/name).
        :param str unscoped_package_name: Name of the package (the 'name' part of @scope/name).
        :param str package_version: Version of the package.
        :param str project: Project ID or project name
        :rtype: :class:`<Package> <azure.devops.v7_1.npm.models.Package>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_scope is not None:
            route_values['packageScope'] = self._serialize.url('package_scope', package_scope, 'str')
        if unscoped_package_name is not None:
            route_values['unscopedPackageName'] = self._serialize.url('unscoped_package_name', unscoped_package_name, 'str')
        if package_version is not None:
            route_values['packageVersion'] = self._serialize.url('package_version', package_version, 'str')
        response = self._send(http_method='GET',
                              location_id='e93d9ec3-4022-401e-96b0-83ea5d911e09',
                              version='7.1-preview.1',
                              route_values=route_values)
        return self._deserialize('Package', response)

    def unpublish_scoped_package(self, feed_id, package_scope, unscoped_package_name, package_version, project=None):
        """UnpublishScopedPackage.
        [Preview API] Unpublish a scoped package version (such as @scope/name).
        :param str feed_id: Name or ID of the feed.
        :param str package_scope: Scope of the package (the 'scope' part of @scope/name).
        :param str unscoped_package_name: Name of the package (the 'name' part of @scope/name).
        :param str package_version: Version of the package.
        :param str project: Project ID or project name
        :rtype: :class:`<Package> <azure.devops.v7_1.npm.models.Package>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_scope is not None:
            route_values['packageScope'] = self._serialize.url('package_scope', package_scope, 'str')
        if unscoped_package_name is not None:
            route_values['unscopedPackageName'] = self._serialize.url('unscoped_package_name', unscoped_package_name, 'str')
        if package_version is not None:
            route_values['packageVersion'] = self._serialize.url('package_version', package_version, 'str')
        response = self._send(http_method='DELETE',
                              location_id='e93d9ec3-4022-401e-96b0-83ea5d911e09',
                              version='7.1-preview.1',
                              route_values=route_values)
        return self._deserialize('Package', response)

    def update_scoped_package(self, package_version_details, feed_id, package_scope, unscoped_package_name, package_version, project=None):
        """UpdateScopedPackage.
        [Preview API]
        :param :class:`<PackageVersionDetails> <azure.devops.v7_1.npm.models.PackageVersionDetails>` package_version_details:
        :param str feed_id:
        :param str package_scope:
        :param str unscoped_package_name:
        :param str package_version:
        :param str project: Project ID or project name
        :rtype: :class:`<Package> <azure.devops.v7_1.npm.models.Package>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_scope is not None:
            route_values['packageScope'] = self._serialize.url('package_scope', package_scope, 'str')
        if unscoped_package_name is not None:
            route_values['unscopedPackageName'] = self._serialize.url('unscoped_package_name', unscoped_package_name, 'str')
        if package_version is not None:
            route_values['packageVersion'] = self._serialize.url('package_version', package_version, 'str')
        content = self._serialize.body(package_version_details, 'PackageVersionDetails')
        response = self._send(http_method='PATCH',
                              location_id='e93d9ec3-4022-401e-96b0-83ea5d911e09',
                              version='7.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Package', response)

    def get_package_info(self, feed_id, package_name, package_version, project=None):
        """GetPackageInfo.
        [Preview API] Get information about an unscoped package version.
        :param str feed_id: Name or ID of the feed.
        :param str package_name: Name of the package.
        :param str package_version: Version of the package.
        :param str project: Project ID or project name
        :rtype: :class:`<Package> <azure.devops.v7_1.npm.models.Package>`
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
                              location_id='ed579d62-67c9-4271-be66-9b029af5bcf9',
                              version='7.1-preview.1',
                              route_values=route_values)
        return self._deserialize('Package', response)

    def unpublish_package(self, feed_id, package_name, package_version, project=None):
        """UnpublishPackage.
        [Preview API] Unpublish an unscoped package version.
        :param str feed_id: Name or ID of the feed.
        :param str package_name: Name of the package.
        :param str package_version: Version of the package.
        :param str project: Project ID or project name
        :rtype: :class:`<Package> <azure.devops.v7_1.npm.models.Package>`
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
                              location_id='ed579d62-67c9-4271-be66-9b029af5bcf9',
                              version='7.1-preview.1',
                              route_values=route_values)
        return self._deserialize('Package', response)

    def update_package(self, package_version_details, feed_id, package_name, package_version, project=None):
        """UpdatePackage.
        [Preview API]
        :param :class:`<PackageVersionDetails> <azure.devops.v7_1.npm.models.PackageVersionDetails>` package_version_details:
        :param str feed_id:
        :param str package_name:
        :param str package_version:
        :param str project: Project ID or project name
        :rtype: :class:`<Package> <azure.devops.v7_1.npm.models.Package>`
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
        response = self._send(http_method='PATCH',
                              location_id='ed579d62-67c9-4271-be66-9b029af5bcf9',
                              version='7.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Package', response)

