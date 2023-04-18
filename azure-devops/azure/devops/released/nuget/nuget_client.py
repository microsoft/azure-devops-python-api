# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from ...v7_0.nuget import models


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

    def get_upstreaming_behavior(self, feed_id, package_name, project=None):
        """GetUpstreamingBehavior.
        Get the upstreaming behavior of a package within the context of a feed
        :param str feed_id: The name or id of the feed
        :param str package_name: The name of the package
        :param str project: Project ID or project name
        :rtype: :class:`<UpstreamingBehavior> <azure.devops.v7_0.nuget.models.UpstreamingBehavior>`
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
                              version='7.0',
                              route_values=route_values)
        return self._deserialize('UpstreamingBehavior', response)

    def set_upstreaming_behavior(self, feed_id, package_name, behavior, project=None):
        """SetUpstreamingBehavior.
        Set the upstreaming behavior of a package within the context of a feed
        :param str feed_id: The name or id of the feed
        :param str package_name: The name of the package
        :param :class:`<UpstreamingBehavior> <azure.devops.v7_0.nuget.models.UpstreamingBehavior>` behavior: The behavior to apply to the package within the scope of the feed
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
                   version='7.0',
                   route_values=route_values,
                   content=content)

    def delete_package_version(self, feed_id, package_name, package_version, project=None):
        """DeletePackageVersion.
        Send a package version from the feed to its paired recycle bin.
        :param str feed_id: Name or ID of the feed.
        :param str package_name: Name of the package to delete.
        :param str package_version: Version of the package to delete.
        :param str project: Project ID or project name
        :rtype: :class:`<Package> <azure.devops.v7_0.nuget.models.Package>`
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
                              version='7.0',
                              route_values=route_values)
        return self._deserialize('Package', response)

    def get_package_version(self, feed_id, package_name, package_version, project=None, show_deleted=None):
        """GetPackageVersion.
        Get information about a package version.
        :param str feed_id: Name or ID of the feed.
        :param str package_name: Name of the package.
        :param str package_version: Version of the package.
        :param str project: Project ID or project name
        :param bool show_deleted: True to include deleted packages in the response.
        :rtype: :class:`<Package> <azure.devops.v7_0.nuget.models.Package>`
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
                              version='7.0',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('Package', response)

    def update_package_version(self, package_version_details, feed_id, package_name, package_version, project=None):
        """UpdatePackageVersion.
        Set mutable state on a package version.
        :param :class:`<PackageVersionDetails> <azure.devops.v7_0.nuget.models.PackageVersionDetails>` package_version_details: New state to apply to the referenced package.
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
                   version='7.0',
                   route_values=route_values,
                   content=content)

