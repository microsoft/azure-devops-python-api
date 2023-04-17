# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from ...v7_0.build import models


class BuildClient(Client):
    """Build
    :param str base_url: Service URL
    :param Authentication creds: Authenticated credentials.
    """

    def __init__(self, base_url=None, creds=None):
        super(BuildClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = '965220d5-5bb9-42cf-8d67-9b146df2a5a4'

    def create_artifact(self, artifact, project, build_id):
        """CreateArtifact.
        Associates an artifact with a build.
        :param :class:`<BuildArtifact> <azure.devops.v7_0.build.models.BuildArtifact>` artifact: The artifact.
        :param str project: Project ID or project name
        :param int build_id: The ID of the build.
        :rtype: :class:`<BuildArtifact> <azure.devops.v7_0.build.models.BuildArtifact>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        content = self._serialize.body(artifact, 'BuildArtifact')
        response = self._send(http_method='POST',
                              location_id='1db06c96-014e-44e1-ac91-90b2d4b3e984',
                              version='7.0',
                              route_values=route_values,
                              content=content)
        return self._deserialize('BuildArtifact', response)

    def get_artifact(self, project, build_id, artifact_name):
        """GetArtifact.
        Gets a specific artifact for a build.
        :param str project: Project ID or project name
        :param int build_id: The ID of the build.
        :param str artifact_name: The name of the artifact.
        :rtype: :class:`<BuildArtifact> <azure.devops.v7_0.build.models.BuildArtifact>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        query_parameters = {}
        if artifact_name is not None:
            query_parameters['artifactName'] = self._serialize.query('artifact_name', artifact_name, 'str')
        response = self._send(http_method='GET',
                              location_id='1db06c96-014e-44e1-ac91-90b2d4b3e984',
                              version='7.0',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('BuildArtifact', response)

    def get_artifact_content_zip(self, project, build_id, artifact_name, **kwargs):
        """GetArtifactContentZip.
        Gets a specific artifact for a build.
        :param str project: Project ID or project name
        :param int build_id: The ID of the build.
        :param str artifact_name: The name of the artifact.
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        query_parameters = {}
        if artifact_name is not None:
            query_parameters['artifactName'] = self._serialize.query('artifact_name', artifact_name, 'str')
        response = self._send(http_method='GET',
                              location_id='1db06c96-014e-44e1-ac91-90b2d4b3e984',
                              version='7.0',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='application/zip')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_artifacts(self, project, build_id):
        """GetArtifacts.
        Gets all artifacts for a build.
        :param str project: Project ID or project name
        :param int build_id: The ID of the build.
        :rtype: [BuildArtifact]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        response = self._send(http_method='GET',
                              location_id='1db06c96-014e-44e1-ac91-90b2d4b3e984',
                              version='7.0',
                              route_values=route_values)
        return self._deserialize('[BuildArtifact]', self._unwrap_collection(response))

    def get_file(self, project, build_id, artifact_name, file_id, file_name, **kwargs):
        """GetFile.
        Gets a file from the build.
        :param str project: Project ID or project name
        :param int build_id: The ID of the build.
        :param str artifact_name: The name of the artifact.
        :param str file_id: The primary key for the file.
        :param str file_name: The name that the file will be set to.
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        query_parameters = {}
        if artifact_name is not None:
            query_parameters['artifactName'] = self._serialize.query('artifact_name', artifact_name, 'str')
        if file_id is not None:
            query_parameters['fileId'] = self._serialize.query('file_id', file_id, 'str')
        if file_name is not None:
            query_parameters['fileName'] = self._serialize.query('file_name', file_name, 'str')
        response = self._send(http_method='GET',
                              location_id='1db06c96-014e-44e1-ac91-90b2d4b3e984',
                              version='7.0',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='application/octet-stream')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_attachments(self, project, build_id, type):
        """GetAttachments.
        Gets the list of attachments of a specific type that are associated with a build.
        :param str project: Project ID or project name
        :param int build_id: The ID of the build.
        :param str type: The type of attachment.
        :rtype: [Attachment]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        if type is not None:
            route_values['type'] = self._serialize.url('type', type, 'str')
        response = self._send(http_method='GET',
                              location_id='f2192269-89fa-4f94-baf6-8fb128c55159',
                              version='7.0',
                              route_values=route_values)
        return self._deserialize('[Attachment]', self._unwrap_collection(response))

    def get_attachment(self, project, build_id, timeline_id, record_id, type, name, **kwargs):
        """GetAttachment.
        Gets a specific attachment.
        :param str project: Project ID or project name
        :param int build_id: The ID of the build.
        :param str timeline_id: The ID of the timeline.
        :param str record_id: The ID of the timeline record.
        :param str type: The type of the attachment.
        :param str name: The name of the attachment.
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        if timeline_id is not None:
            route_values['timelineId'] = self._serialize.url('timeline_id', timeline_id, 'str')
        if record_id is not None:
            route_values['recordId'] = self._serialize.url('record_id', record_id, 'str')
        if type is not None:
            route_values['type'] = self._serialize.url('type', type, 'str')
        if name is not None:
            route_values['name'] = self._serialize.url('name', name, 'str')
        response = self._send(http_method='GET',
                              location_id='af5122d3-3438-485e-a25a-2dbbfde84ee6',
                              version='7.0',
                              route_values=route_values,
                              accept_media_type='application/octet-stream')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def list_branches(self, project, provider_name, service_endpoint_id=None, repository=None, branch_name=None):
        """ListBranches.
        Gets a list of branches for the given source code repository.
        :param str project: Project ID or project name
        :param str provider_name: The name of the source provider.
        :param str service_endpoint_id: If specified, the ID of the service endpoint to query. Can only be omitted for providers that do not use service endpoints, e.g. TFVC or TFGit.
        :param str repository: The vendor-specific identifier or the name of the repository to get branches. Can only be omitted for providers that do not support multiple repositories.
        :param str branch_name: If supplied, the name of the branch to check for specifically.
        :rtype: [str]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if provider_name is not None:
            route_values['providerName'] = self._serialize.url('provider_name', provider_name, 'str')
        query_parameters = {}
        if service_endpoint_id is not None:
            query_parameters['serviceEndpointId'] = self._serialize.query('service_endpoint_id', service_endpoint_id, 'str')
        if repository is not None:
            query_parameters['repository'] = self._serialize.query('repository', repository, 'str')
        if branch_name is not None:
            query_parameters['branchName'] = self._serialize.query('branch_name', branch_name, 'str')
        response = self._send(http_method='GET',
                              location_id='e05d4403-9b81-4244-8763-20fde28d1976',
                              version='7.0',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[str]', self._unwrap_collection(response))

    def get_retention_leases_for_build(self, project, build_id):
        """GetRetentionLeasesForBuild.
        Gets all retention leases that apply to a specific build.
        :param str project: Project ID or project name
        :param int build_id: The ID of the build.
        :rtype: [RetentionLease]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        response = self._send(http_method='GET',
                              location_id='3da19a6a-f088-45c4-83ce-2ad3a87be6c4',
                              version='7.0',
                              route_values=route_values)
        return self._deserialize('[RetentionLease]', self._unwrap_collection(response))

    def delete_build(self, project, build_id):
        """DeleteBuild.
        Deletes a build.
        :param str project: Project ID or project name
        :param int build_id: The ID of the build.
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        self._send(http_method='DELETE',
                   location_id='0cd358e1-9217-4d94-8269-1c1ee6f93dcf',
                   version='7.0',
                   route_values=route_values)

    def get_build(self, project, build_id, property_filters=None):
        """GetBuild.
        Gets a build
        :param str project: Project ID or project name
        :param int build_id:
        :param str property_filters:
        :rtype: :class:`<Build> <azure.devops.v7_0.build.models.Build>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        query_parameters = {}
        if property_filters is not None:
            query_parameters['propertyFilters'] = self._serialize.query('property_filters', property_filters, 'str')
        response = self._send(http_method='GET',
                              location_id='0cd358e1-9217-4d94-8269-1c1ee6f93dcf',
                              version='7.0',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('Build', response)

    def get_builds(self, project, definitions=None, queues=None, build_number=None, min_time=None, max_time=None, requested_for=None, reason_filter=None, status_filter=None, result_filter=None, tag_filters=None, properties=None, top=None, continuation_token=None, max_builds_per_definition=None, deleted_filter=None, query_order=None, branch_name=None, build_ids=None, repository_id=None, repository_type=None):
        """GetBuilds.
        Gets a list of builds.
        :param str project: Project ID or project name
        :param [int] definitions: A comma-delimited list of definition IDs. If specified, filters to builds for these definitions.
        :param [int] queues: A comma-delimited list of queue IDs. If specified, filters to builds that ran against these queues.
        :param str build_number: If specified, filters to builds that match this build number. Append * to do a prefix search.
        :param datetime min_time: If specified, filters to builds that finished/started/queued after this date based on the queryOrder specified.
        :param datetime max_time: If specified, filters to builds that finished/started/queued before this date based on the queryOrder specified.
        :param str requested_for: If specified, filters to builds requested for the specified user.
        :param str reason_filter: If specified, filters to builds that match this reason.
        :param str status_filter: If specified, filters to builds that match this status.
        :param str result_filter: If specified, filters to builds that match this result.
        :param [str] tag_filters: A comma-delimited list of tags. If specified, filters to builds that have the specified tags.
        :param [str] properties: A comma-delimited list of properties to retrieve.
        :param int top: The maximum number of builds to return.
        :param str continuation_token: A continuation token, returned by a previous call to this method, that can be used to return the next set of builds.
        :param int max_builds_per_definition: The maximum number of builds to return per definition.
        :param str deleted_filter: Indicates whether to exclude, include, or only return deleted builds.
        :param str query_order: The order in which builds should be returned.
        :param str branch_name: If specified, filters to builds that built branches that built this branch.
        :param [int] build_ids: A comma-delimited list that specifies the IDs of builds to retrieve.
        :param str repository_id: If specified, filters to builds that built from this repository.
        :param str repository_type: If specified, filters to builds that built from repositories of this type.
        :rtype: :class:`<[Build]> <azure.devops.v7_0.build.models.[Build]>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if definitions is not None:
            definitions = ",".join(map(str, definitions))
            query_parameters['definitions'] = self._serialize.query('definitions', definitions, 'str')
        if queues is not None:
            queues = ",".join(map(str, queues))
            query_parameters['queues'] = self._serialize.query('queues', queues, 'str')
        if build_number is not None:
            query_parameters['buildNumber'] = self._serialize.query('build_number', build_number, 'str')
        if min_time is not None:
            query_parameters['minTime'] = self._serialize.query('min_time', min_time, 'iso-8601')
        if max_time is not None:
            query_parameters['maxTime'] = self._serialize.query('max_time', max_time, 'iso-8601')
        if requested_for is not None:
            query_parameters['requestedFor'] = self._serialize.query('requested_for', requested_for, 'str')
        if reason_filter is not None:
            query_parameters['reasonFilter'] = self._serialize.query('reason_filter', reason_filter, 'str')
        if status_filter is not None:
            query_parameters['statusFilter'] = self._serialize.query('status_filter', status_filter, 'str')
        if result_filter is not None:
            query_parameters['resultFilter'] = self._serialize.query('result_filter', result_filter, 'str')
        if tag_filters is not None:
            tag_filters = ",".join(tag_filters)
            query_parameters['tagFilters'] = self._serialize.query('tag_filters', tag_filters, 'str')
        if properties is not None:
            properties = ",".join(properties)
            query_parameters['properties'] = self._serialize.query('properties', properties, 'str')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        if max_builds_per_definition is not None:
            query_parameters['maxBuildsPerDefinition'] = self._serialize.query('max_builds_per_definition', max_builds_per_definition, 'int')
        if deleted_filter is not None:
            query_parameters['deletedFilter'] = self._serialize.query('deleted_filter', deleted_filter, 'str')
        if query_order is not None:
            query_parameters['queryOrder'] = self._serialize.query('query_order', query_order, 'str')
        if branch_name is not None:
            query_parameters['branchName'] = self._serialize.query('branch_name', branch_name, 'str')
        if build_ids is not None:
            build_ids = ",".join(map(str, build_ids))
            query_parameters['buildIds'] = self._serialize.query('build_ids', build_ids, 'str')
        if repository_id is not None:
            query_parameters['repositoryId'] = self._serialize.query('repository_id', repository_id, 'str')
        if repository_type is not None:
            query_parameters['repositoryType'] = self._serialize.query('repository_type', repository_type, 'str')
        response = self._send(http_method='GET',
                              location_id='0cd358e1-9217-4d94-8269-1c1ee6f93dcf',
                              version='7.0',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[Build]', self._unwrap_collection(response))

    def queue_build(self, build, project, ignore_warnings=None, check_in_ticket=None, source_build_id=None, definition_id=None):
        """QueueBuild.
        Queues a build
        :param :class:`<Build> <azure.devops.v7_0.build.models.Build>` build:
        :param str project: Project ID or project name
        :param bool ignore_warnings:
        :param str check_in_ticket:
        :param int source_build_id:
        :param int definition_id: Optional definition id to queue a build without a body. Ignored if there's a valid body
        :rtype: :class:`<Build> <azure.devops.v7_0.build.models.Build>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if ignore_warnings is not None:
            query_parameters['ignoreWarnings'] = self._serialize.query('ignore_warnings', ignore_warnings, 'bool')
        if check_in_ticket is not None:
            query_parameters['checkInTicket'] = self._serialize.query('check_in_ticket', check_in_ticket, 'str')
        if source_build_id is not None:
            query_parameters['sourceBuildId'] = self._serialize.query('source_build_id', source_build_id, 'int')
        if definition_id is not None:
            query_parameters['definitionId'] = self._serialize.query('definition_id', definition_id, 'int')
        content = self._serialize.body(build, 'Build')
        response = self._send(http_method='POST',
                              location_id='0cd358e1-9217-4d94-8269-1c1ee6f93dcf',
                              version='7.0',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('Build', response)

    def update_build(self, build, project, build_id, retry=None):
        """UpdateBuild.
        Updates a build.
        :param :class:`<Build> <azure.devops.v7_0.build.models.Build>` build: The build.
        :param str project: Project ID or project name
        :param int build_id: The ID of the build.
        :param bool retry:
        :rtype: :class:`<Build> <azure.devops.v7_0.build.models.Build>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        query_parameters = {}
        if retry is not None:
            query_parameters['retry'] = self._serialize.query('retry', retry, 'bool')
        content = self._serialize.body(build, 'Build')
        response = self._send(http_method='PATCH',
                              location_id='0cd358e1-9217-4d94-8269-1c1ee6f93dcf',
                              version='7.0',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('Build', response)

    def update_builds(self, builds, project):
        """UpdateBuilds.
        Updates multiple builds.
        :param [Build] builds: The builds to update.
        :param str project: Project ID or project name
        :rtype: [Build]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(builds, '[Build]')
        response = self._send(http_method='PATCH',
                              location_id='0cd358e1-9217-4d94-8269-1c1ee6f93dcf',
                              version='7.0',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[Build]', self._unwrap_collection(response))

    def get_build_controller(self, controller_id):
        """GetBuildController.
        Gets a controller
        :param int controller_id:
        :rtype: :class:`<BuildController> <azure.devops.v7_0.build.models.BuildController>`
        """
        route_values = {}
        if controller_id is not None:
            route_values['controllerId'] = self._serialize.url('controller_id', controller_id, 'int')
        response = self._send(http_method='GET',
                              location_id='fcac1932-2ee1-437f-9b6f-7f696be858f6',
                              version='7.0',
                              route_values=route_values)
        return self._deserialize('BuildController', response)

    def get_build_controllers(self, name=None):
        """GetBuildControllers.
        Gets controller, optionally filtered by name
        :param str name:
        :rtype: [BuildController]
        """
        query_parameters = {}
        if name is not None:
            query_parameters['name'] = self._serialize.query('name', name, 'str')
        response = self._send(http_method='GET',
                              location_id='fcac1932-2ee1-437f-9b6f-7f696be858f6',
                              version='7.0',
                              query_parameters=query_parameters)
        return self._deserialize('[BuildController]', self._unwrap_collection(response))

    def create_definition(self, definition, project, definition_to_clone_id=None, definition_to_clone_revision=None):
        """CreateDefinition.
        Creates a new definition.
        :param :class:`<BuildDefinition> <azure.devops.v7_0.build.models.BuildDefinition>` definition: The definition.
        :param str project: Project ID or project name
        :param int definition_to_clone_id:
        :param int definition_to_clone_revision:
        :rtype: :class:`<BuildDefinition> <azure.devops.v7_0.build.models.BuildDefinition>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if definition_to_clone_id is not None:
            query_parameters['definitionToCloneId'] = self._serialize.query('definition_to_clone_id', definition_to_clone_id, 'int')
        if definition_to_clone_revision is not None:
            query_parameters['definitionToCloneRevision'] = self._serialize.query('definition_to_clone_revision', definition_to_clone_revision, 'int')
        content = self._serialize.body(definition, 'BuildDefinition')
        response = self._send(http_method='POST',
                              location_id='dbeaf647-6167-421a-bda9-c9327b25e2e6',
                              version='7.0',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('BuildDefinition', response)

    def delete_definition(self, project, definition_id):
        """DeleteDefinition.
        Deletes a definition and all associated builds.
        :param str project: Project ID or project name
        :param int definition_id: The ID of the definition.
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if definition_id is not None:
            route_values['definitionId'] = self._serialize.url('definition_id', definition_id, 'int')
        self._send(http_method='DELETE',
                   location_id='dbeaf647-6167-421a-bda9-c9327b25e2e6',
                   version='7.0',
                   route_values=route_values)

    def get_definition(self, project, definition_id, revision=None, min_metrics_time=None, property_filters=None, include_latest_builds=None):
        """GetDefinition.
        Gets a definition, optionally at a specific revision.
        :param str project: Project ID or project name
        :param int definition_id: The ID of the definition.
        :param int revision: The revision number to retrieve. If this is not specified, the latest version will be returned.
        :param datetime min_metrics_time: If specified, indicates the date from which metrics should be included.
        :param [str] property_filters: A comma-delimited list of properties to include in the results.
        :param bool include_latest_builds:
        :rtype: :class:`<BuildDefinition> <azure.devops.v7_0.build.models.BuildDefinition>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if definition_id is not None:
            route_values['definitionId'] = self._serialize.url('definition_id', definition_id, 'int')
        query_parameters = {}
        if revision is not None:
            query_parameters['revision'] = self._serialize.query('revision', revision, 'int')
        if min_metrics_time is not None:
            query_parameters['minMetricsTime'] = self._serialize.query('min_metrics_time', min_metrics_time, 'iso-8601')
        if property_filters is not None:
            property_filters = ",".join(property_filters)
            query_parameters['propertyFilters'] = self._serialize.query('property_filters', property_filters, 'str')
        if include_latest_builds is not None:
            query_parameters['includeLatestBuilds'] = self._serialize.query('include_latest_builds', include_latest_builds, 'bool')
        response = self._send(http_method='GET',
                              location_id='dbeaf647-6167-421a-bda9-c9327b25e2e6',
                              version='7.0',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('BuildDefinition', response)

    def get_definitions(self, project, name=None, repository_id=None, repository_type=None, query_order=None, top=None, continuation_token=None, min_metrics_time=None, definition_ids=None, path=None, built_after=None, not_built_after=None, include_all_properties=None, include_latest_builds=None, task_id_filter=None, process_type=None, yaml_filename=None):
        """GetDefinitions.
        Gets a list of definitions.
        :param str project: Project ID or project name
        :param str name: If specified, filters to definitions whose names match this pattern.
        :param str repository_id: A repository ID. If specified, filters to definitions that use this repository.
        :param str repository_type: If specified, filters to definitions that have a repository of this type.
        :param str query_order: Indicates the order in which definitions should be returned.
        :param int top: The maximum number of definitions to return.
        :param str continuation_token: A continuation token, returned by a previous call to this method, that can be used to return the next set of definitions.
        :param datetime min_metrics_time: If specified, indicates the date from which metrics should be included.
        :param [int] definition_ids: A comma-delimited list that specifies the IDs of definitions to retrieve.
        :param str path: If specified, filters to definitions under this folder.
        :param datetime built_after: If specified, filters to definitions that have builds after this date.
        :param datetime not_built_after: If specified, filters to definitions that do not have builds after this date.
        :param bool include_all_properties: Indicates whether the full definitions should be returned. By default, shallow representations of the definitions are returned.
        :param bool include_latest_builds: Indicates whether to return the latest and latest completed builds for this definition.
        :param str task_id_filter: If specified, filters to definitions that use the specified task.
        :param int process_type: If specified, filters to definitions with the given process type.
        :param str yaml_filename: If specified, filters to YAML definitions that match the given filename. To use this filter includeAllProperties should be set to true
        :rtype: :class:`<[BuildDefinitionReference]> <azure.devops.v7_0.build.models.[BuildDefinitionReference]>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if name is not None:
            query_parameters['name'] = self._serialize.query('name', name, 'str')
        if repository_id is not None:
            query_parameters['repositoryId'] = self._serialize.query('repository_id', repository_id, 'str')
        if repository_type is not None:
            query_parameters['repositoryType'] = self._serialize.query('repository_type', repository_type, 'str')
        if query_order is not None:
            query_parameters['queryOrder'] = self._serialize.query('query_order', query_order, 'str')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        if min_metrics_time is not None:
            query_parameters['minMetricsTime'] = self._serialize.query('min_metrics_time', min_metrics_time, 'iso-8601')
        if definition_ids is not None:
            definition_ids = ",".join(map(str, definition_ids))
            query_parameters['definitionIds'] = self._serialize.query('definition_ids', definition_ids, 'str')
        if path is not None:
            query_parameters['path'] = self._serialize.query('path', path, 'str')
        if built_after is not None:
            query_parameters['builtAfter'] = self._serialize.query('built_after', built_after, 'iso-8601')
        if not_built_after is not None:
            query_parameters['notBuiltAfter'] = self._serialize.query('not_built_after', not_built_after, 'iso-8601')
        if include_all_properties is not None:
            query_parameters['includeAllProperties'] = self._serialize.query('include_all_properties', include_all_properties, 'bool')
        if include_latest_builds is not None:
            query_parameters['includeLatestBuilds'] = self._serialize.query('include_latest_builds', include_latest_builds, 'bool')
        if task_id_filter is not None:
            query_parameters['taskIdFilter'] = self._serialize.query('task_id_filter', task_id_filter, 'str')
        if process_type is not None:
            query_parameters['processType'] = self._serialize.query('process_type', process_type, 'int')
        if yaml_filename is not None:
            query_parameters['yamlFilename'] = self._serialize.query('yaml_filename', yaml_filename, 'str')
        response = self._send(http_method='GET',
                              location_id='dbeaf647-6167-421a-bda9-c9327b25e2e6',
                              version='7.0',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[BuildDefinitionReference]', self._unwrap_collection(response))

    def restore_definition(self, project, definition_id, deleted):
        """RestoreDefinition.
        Restores a deleted definition
        :param str project: Project ID or project name
        :param int definition_id: The identifier of the definition to restore.
        :param bool deleted: When false, restores a deleted definition.
        :rtype: :class:`<BuildDefinition> <azure.devops.v7_0.build.models.BuildDefinition>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if definition_id is not None:
            route_values['definitionId'] = self._serialize.url('definition_id', definition_id, 'int')
        query_parameters = {}
        if deleted is not None:
            query_parameters['deleted'] = self._serialize.query('deleted', deleted, 'bool')
        response = self._send(http_method='PATCH',
                              location_id='dbeaf647-6167-421a-bda9-c9327b25e2e6',
                              version='7.0',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('BuildDefinition', response)

    def update_definition(self, definition, project, definition_id, secrets_source_definition_id=None, secrets_source_definition_revision=None):
        """UpdateDefinition.
        Updates an existing build definition.  In order for this operation to succeed, the value of the "Revision" property of the request body must match the existing build definition's. It is recommended that you obtain the existing build definition by using GET, modify the build definition as necessary, and then submit the modified definition with PUT.
        :param :class:`<BuildDefinition> <azure.devops.v7_0.build.models.BuildDefinition>` definition: The new version of the definition. Its "Revision" property must match the existing definition for the update to be accepted.
        :param str project: Project ID or project name
        :param int definition_id: The ID of the definition.
        :param int secrets_source_definition_id:
        :param int secrets_source_definition_revision:
        :rtype: :class:`<BuildDefinition> <azure.devops.v7_0.build.models.BuildDefinition>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if definition_id is not None:
            route_values['definitionId'] = self._serialize.url('definition_id', definition_id, 'int')
        query_parameters = {}
        if secrets_source_definition_id is not None:
            query_parameters['secretsSourceDefinitionId'] = self._serialize.query('secrets_source_definition_id', secrets_source_definition_id, 'int')
        if secrets_source_definition_revision is not None:
            query_parameters['secretsSourceDefinitionRevision'] = self._serialize.query('secrets_source_definition_revision', secrets_source_definition_revision, 'int')
        content = self._serialize.body(definition, 'BuildDefinition')
        response = self._send(http_method='PUT',
                              location_id='dbeaf647-6167-421a-bda9-c9327b25e2e6',
                              version='7.0',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('BuildDefinition', response)

    def get_file_contents(self, project, provider_name, service_endpoint_id=None, repository=None, commit_or_branch=None, path=None, **kwargs):
        """GetFileContents.
        Gets the contents of a file in the given source code repository.
        :param str project: Project ID or project name
        :param str provider_name: The name of the source provider.
        :param str service_endpoint_id: If specified, the ID of the service endpoint to query. Can only be omitted for providers that do not use service endpoints, e.g. TFVC or TFGit.
        :param str repository: If specified, the vendor-specific identifier or the name of the repository to get branches. Can only be omitted for providers that do not support multiple repositories.
        :param str commit_or_branch: The identifier of the commit or branch from which a file's contents are retrieved.
        :param str path: The path to the file to retrieve, relative to the root of the repository.
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if provider_name is not None:
            route_values['providerName'] = self._serialize.url('provider_name', provider_name, 'str')
        query_parameters = {}
        if service_endpoint_id is not None:
            query_parameters['serviceEndpointId'] = self._serialize.query('service_endpoint_id', service_endpoint_id, 'str')
        if repository is not None:
            query_parameters['repository'] = self._serialize.query('repository', repository, 'str')
        if commit_or_branch is not None:
            query_parameters['commitOrBranch'] = self._serialize.query('commit_or_branch', commit_or_branch, 'str')
        if path is not None:
            query_parameters['path'] = self._serialize.query('path', path, 'str')
        response = self._send(http_method='GET',
                              location_id='29d12225-b1d9-425f-b668-6c594a981313',
                              version='7.0',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='text/plain')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_build_general_settings(self, project):
        """GetBuildGeneralSettings.
        Gets pipeline general settings.
        :param str project: Project ID or project name
        :rtype: :class:`<PipelineGeneralSettings> <azure.devops.v7_0.build.models.PipelineGeneralSettings>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        response = self._send(http_method='GET',
                              location_id='c4aefd19-30ff-405b-80ad-aca021e7242a',
                              version='7.0',
                              route_values=route_values)
        return self._deserialize('PipelineGeneralSettings', response)

    def update_build_general_settings(self, new_settings, project):
        """UpdateBuildGeneralSettings.
        Updates pipeline general settings.
        :param :class:`<PipelineGeneralSettings> <azure.devops.v7_0.build.models.PipelineGeneralSettings>` new_settings:
        :param str project: Project ID or project name
        :rtype: :class:`<PipelineGeneralSettings> <azure.devops.v7_0.build.models.PipelineGeneralSettings>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(new_settings, 'PipelineGeneralSettings')
        response = self._send(http_method='PATCH',
                              location_id='c4aefd19-30ff-405b-80ad-aca021e7242a',
                              version='7.0',
                              route_values=route_values,
                              content=content)
        return self._deserialize('PipelineGeneralSettings', response)

    def get_retention_history(self, days_to_lookback=None):
        """GetRetentionHistory.
        Returns the retention history for the project collection. This includes pipelines that have custom retention rules that may prevent the retention job from cleaning them up, runs per pipeline with retention type, files associated with pipelines owned by the collection with retention type, and the number of files per pipeline.
        :param int days_to_lookback:
        :rtype: :class:`<BuildRetentionHistory> <azure.devops.v7_0.build.models.BuildRetentionHistory>`
        """
        query_parameters = {}
        if days_to_lookback is not None:
            query_parameters['daysToLookback'] = self._serialize.query('days_to_lookback', days_to_lookback, 'int')
        response = self._send(http_method='GET',
                              location_id='1a9c48be-0ef5-4ec2-b94f-f053bdd2d3bf',
                              version='7.0',
                              query_parameters=query_parameters)
        return self._deserialize('BuildRetentionHistory', response)

    def get_build_changes(self, project, build_id, continuation_token=None, top=None, include_source_change=None):
        """GetBuildChanges.
        Gets the changes associated with a build
        :param str project: Project ID or project name
        :param int build_id:
        :param str continuation_token:
        :param int top: The maximum number of changes to return
        :param bool include_source_change:
        :rtype: :class:`<[Change]> <azure.devops.v7_0.build.models.[Change]>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        query_parameters = {}
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if include_source_change is not None:
            query_parameters['includeSourceChange'] = self._serialize.query('include_source_change', include_source_change, 'bool')
        response = self._send(http_method='GET',
                              location_id='54572c7b-bbd3-45d4-80dc-28be08941620',
                              version='7.0',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[Change]', self._unwrap_collection(response))

    def get_changes_between_builds(self, project, from_build_id=None, to_build_id=None, top=None):
        """GetChangesBetweenBuilds.
        Gets the changes made to the repository between two given builds.
        :param str project: Project ID or project name
        :param int from_build_id: The ID of the first build.
        :param int to_build_id: The ID of the last build.
        :param int top: The maximum number of changes to return.
        :rtype: [Change]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if from_build_id is not None:
            query_parameters['fromBuildId'] = self._serialize.query('from_build_id', from_build_id, 'int')
        if to_build_id is not None:
            query_parameters['toBuildId'] = self._serialize.query('to_build_id', to_build_id, 'int')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        response = self._send(http_method='GET',
                              location_id='f10f0ea5-18a1-43ec-a8fb-2042c7be9b43',
                              version='7.0',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[Change]', self._unwrap_collection(response))

    def add_retention_leases(self, new_leases, project):
        """AddRetentionLeases.
        Adds new leases for pipeline runs.
        :param [NewRetentionLease] new_leases:
        :param str project: Project ID or project name
        :rtype: [RetentionLease]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(new_leases, '[NewRetentionLease]')
        response = self._send(http_method='POST',
                              location_id='272051e4-9af1-45b5-ae22-8d960a5539d4',
                              version='7.0',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[RetentionLease]', self._unwrap_collection(response))

    def delete_retention_leases_by_id(self, project, ids):
        """DeleteRetentionLeasesById.
        Removes specific retention leases.
        :param str project: Project ID or project name
        :param [int] ids:
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if ids is not None:
            ids = ",".join(map(str, ids))
            query_parameters['ids'] = self._serialize.query('ids', ids, 'str')
        self._send(http_method='DELETE',
                   location_id='272051e4-9af1-45b5-ae22-8d960a5539d4',
                   version='7.0',
                   route_values=route_values,
                   query_parameters=query_parameters)

    def get_retention_lease(self, project, lease_id):
        """GetRetentionLease.
        Returns the details of the retention lease given a lease id.
        :param str project: Project ID or project name
        :param int lease_id:
        :rtype: :class:`<RetentionLease> <azure.devops.v7_0.build.models.RetentionLease>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if lease_id is not None:
            route_values['leaseId'] = self._serialize.url('lease_id', lease_id, 'int')
        response = self._send(http_method='GET',
                              location_id='272051e4-9af1-45b5-ae22-8d960a5539d4',
                              version='7.0',
                              route_values=route_values)
        return self._deserialize('RetentionLease', response)

    def get_retention_leases_by_minimal_retention_leases(self, project, leases_to_fetch):
        """GetRetentionLeasesByMinimalRetentionLeases.
        Returns any leases matching the specified MinimalRetentionLeases
        :param str project: Project ID or project name
        :param [MinimalRetentionLease] leases_to_fetch: List of JSON-serialized MinimalRetentionLeases separated by '|'
        :rtype: [RetentionLease]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if leases_to_fetch is not None:
            leases_to_fetch = "|".join(map(str, leases_to_fetch))
            query_parameters['leasesToFetch'] = self._serialize.query('leases_to_fetch', leases_to_fetch, 'str')
        response = self._send(http_method='GET',
                              location_id='272051e4-9af1-45b5-ae22-8d960a5539d4',
                              version='7.0',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[RetentionLease]', self._unwrap_collection(response))

    def get_retention_leases_by_owner_id(self, project, owner_id=None, definition_id=None, run_id=None):
        """GetRetentionLeasesByOwnerId.
        Returns any leases owned by the specified entity, optionally scoped to a single pipeline definition and run.
        :param str project: Project ID or project name
        :param str owner_id:
        :param int definition_id: An optional parameter to limit the search to a specific pipeline definition.
        :param int run_id: An optional parameter to limit the search to a single pipeline run. Requires definitionId.
        :rtype: [RetentionLease]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if owner_id is not None:
            query_parameters['ownerId'] = self._serialize.query('owner_id', owner_id, 'str')
        if definition_id is not None:
            query_parameters['definitionId'] = self._serialize.query('definition_id', definition_id, 'int')
        if run_id is not None:
            query_parameters['runId'] = self._serialize.query('run_id', run_id, 'int')
        response = self._send(http_method='GET',
                              location_id='272051e4-9af1-45b5-ae22-8d960a5539d4',
                              version='7.0',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[RetentionLease]', self._unwrap_collection(response))

    def get_retention_leases_by_user_id(self, project, user_owner_id, definition_id=None, run_id=None):
        """GetRetentionLeasesByUserId.
        Returns any leases owned by the specified user, optionally scoped to a single pipeline definition and run.
        :param str project: Project ID or project name
        :param str user_owner_id: The user id to search for.
        :param int definition_id: An optional parameter to limit the search to a specific pipeline definition.
        :param int run_id: An optional parameter to limit the search to a single pipeline run. Requires definitionId.
        :rtype: [RetentionLease]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if user_owner_id is not None:
            query_parameters['userOwnerId'] = self._serialize.query('user_owner_id', user_owner_id, 'str')
        if definition_id is not None:
            query_parameters['definitionId'] = self._serialize.query('definition_id', definition_id, 'int')
        if run_id is not None:
            query_parameters['runId'] = self._serialize.query('run_id', run_id, 'int')
        response = self._send(http_method='GET',
                              location_id='272051e4-9af1-45b5-ae22-8d960a5539d4',
                              version='7.0',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[RetentionLease]', self._unwrap_collection(response))

    def update_retention_lease(self, lease_update, project, lease_id):
        """UpdateRetentionLease.
        Updates the duration or pipeline protection status of a retention lease.
        :param :class:`<RetentionLeaseUpdate> <azure.devops.v7_0.build.models.RetentionLeaseUpdate>` lease_update: The new data for the retention lease.
        :param str project: Project ID or project name
        :param int lease_id: The ID of the lease to update.
        :rtype: :class:`<RetentionLease> <azure.devops.v7_0.build.models.RetentionLease>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if lease_id is not None:
            route_values['leaseId'] = self._serialize.url('lease_id', lease_id, 'int')
        content = self._serialize.body(lease_update, 'RetentionLeaseUpdate')
        response = self._send(http_method='PATCH',
                              location_id='272051e4-9af1-45b5-ae22-8d960a5539d4',
                              version='7.0',
                              route_values=route_values,
                              content=content)
        return self._deserialize('RetentionLease', response)

    def get_build_log(self, project, build_id, log_id, start_line=None, end_line=None, **kwargs):
        """GetBuildLog.
        Gets an individual log file for a build.
        :param str project: Project ID or project name
        :param int build_id: The ID of the build.
        :param int log_id: The ID of the log file.
        :param long start_line: The start line.
        :param long end_line: The end line.
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        if log_id is not None:
            route_values['logId'] = self._serialize.url('log_id', log_id, 'int')
        query_parameters = {}
        if start_line is not None:
            query_parameters['startLine'] = self._serialize.query('start_line', start_line, 'long')
        if end_line is not None:
            query_parameters['endLine'] = self._serialize.query('end_line', end_line, 'long')
        response = self._send(http_method='GET',
                              location_id='35a80daf-7f30-45fc-86e8-6b813d9c90df',
                              version='7.0',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='text/plain')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_build_log_lines(self, project, build_id, log_id, start_line=None, end_line=None):
        """GetBuildLogLines.
        Gets an individual log file for a build.
        :param str project: Project ID or project name
        :param int build_id: The ID of the build.
        :param int log_id: The ID of the log file.
        :param long start_line: The start line.
        :param long end_line: The end line.
        :rtype: [str]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        if log_id is not None:
            route_values['logId'] = self._serialize.url('log_id', log_id, 'int')
        query_parameters = {}
        if start_line is not None:
            query_parameters['startLine'] = self._serialize.query('start_line', start_line, 'long')
        if end_line is not None:
            query_parameters['endLine'] = self._serialize.query('end_line', end_line, 'long')
        response = self._send(http_method='GET',
                              location_id='35a80daf-7f30-45fc-86e8-6b813d9c90df',
                              version='7.0',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[str]', self._unwrap_collection(response))

    def get_build_logs(self, project, build_id):
        """GetBuildLogs.
        Gets the logs for a build.
        :param str project: Project ID or project name
        :param int build_id: The ID of the build.
        :rtype: [BuildLog]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        response = self._send(http_method='GET',
                              location_id='35a80daf-7f30-45fc-86e8-6b813d9c90df',
                              version='7.0',
                              route_values=route_values)
        return self._deserialize('[BuildLog]', self._unwrap_collection(response))

    def get_build_logs_zip(self, project, build_id, **kwargs):
        """GetBuildLogsZip.
        Gets the logs for a build.
        :param str project: Project ID or project name
        :param int build_id: The ID of the build.
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        response = self._send(http_method='GET',
                              location_id='35a80daf-7f30-45fc-86e8-6b813d9c90df',
                              version='7.0',
                              route_values=route_values,
                              accept_media_type='application/zip')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_build_log_zip(self, project, build_id, log_id, start_line=None, end_line=None, **kwargs):
        """GetBuildLogZip.
        Gets an individual log file for a build.
        :param str project: Project ID or project name
        :param int build_id: The ID of the build.
        :param int log_id: The ID of the log file.
        :param long start_line: The start line.
        :param long end_line: The end line.
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        if log_id is not None:
            route_values['logId'] = self._serialize.url('log_id', log_id, 'int')
        query_parameters = {}
        if start_line is not None:
            query_parameters['startLine'] = self._serialize.query('start_line', start_line, 'long')
        if end_line is not None:
            query_parameters['endLine'] = self._serialize.query('end_line', end_line, 'long')
        response = self._send(http_method='GET',
                              location_id='35a80daf-7f30-45fc-86e8-6b813d9c90df',
                              version='7.0',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='application/zip')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_build_option_definitions(self, project=None):
        """GetBuildOptionDefinitions.
        Gets all build definition options supported by the system.
        :param str project: Project ID or project name
        :rtype: [BuildOptionDefinition]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        response = self._send(http_method='GET',
                              location_id='591cb5a4-2d46-4f3a-a697-5cd42b6bd332',
                              version='7.0',
                              route_values=route_values)
        return self._deserialize('[BuildOptionDefinition]', self._unwrap_collection(response))

    def get_path_contents(self, project, provider_name, service_endpoint_id=None, repository=None, commit_or_branch=None, path=None):
        """GetPathContents.
        Gets the contents of a directory in the given source code repository.
        :param str project: Project ID or project name
        :param str provider_name: The name of the source provider.
        :param str service_endpoint_id: If specified, the ID of the service endpoint to query. Can only be omitted for providers that do not use service endpoints, e.g. TFVC or TFGit.
        :param str repository: If specified, the vendor-specific identifier or the name of the repository to get branches. Can only be omitted for providers that do not support multiple repositories.
        :param str commit_or_branch: The identifier of the commit or branch from which a file's contents are retrieved.
        :param str path: The path contents to list, relative to the root of the repository.
        :rtype: [SourceRepositoryItem]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if provider_name is not None:
            route_values['providerName'] = self._serialize.url('provider_name', provider_name, 'str')
        query_parameters = {}
        if service_endpoint_id is not None:
            query_parameters['serviceEndpointId'] = self._serialize.query('service_endpoint_id', service_endpoint_id, 'str')
        if repository is not None:
            query_parameters['repository'] = self._serialize.query('repository', repository, 'str')
        if commit_or_branch is not None:
            query_parameters['commitOrBranch'] = self._serialize.query('commit_or_branch', commit_or_branch, 'str')
        if path is not None:
            query_parameters['path'] = self._serialize.query('path', path, 'str')
        response = self._send(http_method='GET',
                              location_id='7944d6fb-df01-4709-920a-7a189aa34037',
                              version='7.0',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[SourceRepositoryItem]', self._unwrap_collection(response))

    def get_build_properties(self, project, build_id, filter=None):
        """GetBuildProperties.
        Gets properties for a build.
        :param str project: Project ID or project name
        :param int build_id: The ID of the build.
        :param [str] filter: A comma-delimited list of properties. If specified, filters to these specific properties.
        :rtype: :class:`<object> <azure.devops.v7_0.build.models.object>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        query_parameters = {}
        if filter is not None:
            filter = ",".join(filter)
            query_parameters['filter'] = self._serialize.query('filter', filter, 'str')
        response = self._send(http_method='GET',
                              location_id='0a6312e9-0627-49b7-8083-7d74a64849c9',
                              version='7.0',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('object', response)

    def update_build_properties(self, document, project, build_id):
        """UpdateBuildProperties.
        Updates properties for a build.
        :param :class:`<[JsonPatchOperation]> <azure.devops.v7_0.build.models.[JsonPatchOperation]>` document: A json-patch document describing the properties to update.
        :param str project: Project ID or project name
        :param int build_id: The ID of the build.
        :rtype: :class:`<object> <azure.devops.v7_0.build.models.object>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        content = self._serialize.body(document, '[JsonPatchOperation]')
        response = self._send(http_method='PATCH',
                              location_id='0a6312e9-0627-49b7-8083-7d74a64849c9',
                              version='7.0',
                              route_values=route_values,
                              content=content,
                              media_type='application/json-patch+json')
        return self._deserialize('object', response)

    def get_definition_properties(self, project, definition_id, filter=None):
        """GetDefinitionProperties.
        Gets properties for a definition.
        :param str project: Project ID or project name
        :param int definition_id: The ID of the definition.
        :param [str] filter: A comma-delimited list of properties. If specified, filters to these specific properties.
        :rtype: :class:`<object> <azure.devops.v7_0.build.models.object>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if definition_id is not None:
            route_values['definitionId'] = self._serialize.url('definition_id', definition_id, 'int')
        query_parameters = {}
        if filter is not None:
            filter = ",".join(filter)
            query_parameters['filter'] = self._serialize.query('filter', filter, 'str')
        response = self._send(http_method='GET',
                              location_id='d9826ad7-2a68-46a9-a6e9-677698777895',
                              version='7.0',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('object', response)

    def update_definition_properties(self, document, project, definition_id):
        """UpdateDefinitionProperties.
        Updates properties for a definition.
        :param :class:`<[JsonPatchOperation]> <azure.devops.v7_0.build.models.[JsonPatchOperation]>` document: A json-patch document describing the properties to update.
        :param str project: Project ID or project name
        :param int definition_id: The ID of the definition.
        :rtype: :class:`<object> <azure.devops.v7_0.build.models.object>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if definition_id is not None:
            route_values['definitionId'] = self._serialize.url('definition_id', definition_id, 'int')
        content = self._serialize.body(document, '[JsonPatchOperation]')
        response = self._send(http_method='PATCH',
                              location_id='d9826ad7-2a68-46a9-a6e9-677698777895',
                              version='7.0',
                              route_values=route_values,
                              content=content,
                              media_type='application/json-patch+json')
        return self._deserialize('object', response)

    def get_pull_request(self, project, provider_name, pull_request_id, repository_id=None, service_endpoint_id=None):
        """GetPullRequest.
        Gets a pull request object from source provider.
        :param str project: Project ID or project name
        :param str provider_name: The name of the source provider.
        :param str pull_request_id: Vendor-specific id of the pull request.
        :param str repository_id: Vendor-specific identifier or the name of the repository that contains the pull request.
        :param str service_endpoint_id: If specified, the ID of the service endpoint to query. Can only be omitted for providers that do not use service endpoints, e.g. TFVC or TFGit.
        :rtype: :class:`<PullRequest> <azure.devops.v7_0.build.models.PullRequest>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if provider_name is not None:
            route_values['providerName'] = self._serialize.url('provider_name', provider_name, 'str')
        if pull_request_id is not None:
            route_values['pullRequestId'] = self._serialize.url('pull_request_id', pull_request_id, 'str')
        query_parameters = {}
        if repository_id is not None:
            query_parameters['repositoryId'] = self._serialize.query('repository_id', repository_id, 'str')
        if service_endpoint_id is not None:
            query_parameters['serviceEndpointId'] = self._serialize.query('service_endpoint_id', service_endpoint_id, 'str')
        response = self._send(http_method='GET',
                              location_id='d8763ec7-9ff0-4fb4-b2b2-9d757906ff14',
                              version='7.0',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('PullRequest', response)

    def get_build_report(self, project, build_id, type=None):
        """GetBuildReport.
        Gets a build report.
        :param str project: Project ID or project name
        :param int build_id: The ID of the build.
        :param str type:
        :rtype: :class:`<BuildReportMetadata> <azure.devops.v7_0.build.models.BuildReportMetadata>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        query_parameters = {}
        if type is not None:
            query_parameters['type'] = self._serialize.query('type', type, 'str')
        response = self._send(http_method='GET',
                              location_id='45bcaa88-67e1-4042-a035-56d3b4a7d44c',
                              version='7.0',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('BuildReportMetadata', response)

    def get_build_report_html_content(self, project, build_id, type=None, **kwargs):
        """GetBuildReportHtmlContent.
        Gets a build report.
        :param str project: Project ID or project name
        :param int build_id: The ID of the build.
        :param str type:
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        query_parameters = {}
        if type is not None:
            query_parameters['type'] = self._serialize.query('type', type, 'str')
        response = self._send(http_method='GET',
                              location_id='45bcaa88-67e1-4042-a035-56d3b4a7d44c',
                              version='7.0',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='text/html')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def list_repositories(self, project, provider_name, service_endpoint_id=None, repository=None, result_set=None, page_results=None, continuation_token=None):
        """ListRepositories.
        Gets a list of source code repositories.
        :param str project: Project ID or project name
        :param str provider_name: The name of the source provider.
        :param str service_endpoint_id: If specified, the ID of the service endpoint to query. Can only be omitted for providers that do not use service endpoints, e.g. TFVC or TFGit.
        :param str repository: If specified, the vendor-specific identifier or the name of a single repository to get.
        :param str result_set: 'top' for the repositories most relevant for the endpoint. If not set, all repositories are returned. Ignored if 'repository' is set.
        :param bool page_results: If set to true, this will limit the set of results and will return a continuation token to continue the query.
        :param str continuation_token: When paging results, this is a continuation token, returned by a previous call to this method, that can be used to return the next set of repositories.
        :rtype: :class:`<SourceRepositories> <azure.devops.v7_0.build.models.SourceRepositories>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if provider_name is not None:
            route_values['providerName'] = self._serialize.url('provider_name', provider_name, 'str')
        query_parameters = {}
        if service_endpoint_id is not None:
            query_parameters['serviceEndpointId'] = self._serialize.query('service_endpoint_id', service_endpoint_id, 'str')
        if repository is not None:
            query_parameters['repository'] = self._serialize.query('repository', repository, 'str')
        if result_set is not None:
            query_parameters['resultSet'] = self._serialize.query('result_set', result_set, 'str')
        if page_results is not None:
            query_parameters['pageResults'] = self._serialize.query('page_results', page_results, 'bool')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        response = self._send(http_method='GET',
                              location_id='d44d1680-f978-4834-9b93-8c6e132329c9',
                              version='7.0',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('SourceRepositories', response)

    def get_retention_settings(self, project):
        """GetRetentionSettings.
        Gets the project's retention settings.
        :param str project: Project ID or project name
        :rtype: :class:`<ProjectRetentionSetting> <azure.devops.v7_0.build.models.ProjectRetentionSetting>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        response = self._send(http_method='GET',
                              location_id='dadb46e7-5851-4c72-820e-ae8abb82f59f',
                              version='7.0',
                              route_values=route_values)
        return self._deserialize('ProjectRetentionSetting', response)

    def update_retention_settings(self, update_model, project):
        """UpdateRetentionSettings.
        Updates the project's retention settings.
        :param :class:`<UpdateProjectRetentionSettingModel> <azure.devops.v7_0.build.models.UpdateProjectRetentionSettingModel>` update_model:
        :param str project: Project ID or project name
        :rtype: :class:`<ProjectRetentionSetting> <azure.devops.v7_0.build.models.ProjectRetentionSetting>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(update_model, 'UpdateProjectRetentionSettingModel')
        response = self._send(http_method='PATCH',
                              location_id='dadb46e7-5851-4c72-820e-ae8abb82f59f',
                              version='7.0',
                              route_values=route_values,
                              content=content)
        return self._deserialize('ProjectRetentionSetting', response)

    def get_definition_revisions(self, project, definition_id):
        """GetDefinitionRevisions.
        Gets all revisions of a definition.
        :param str project: Project ID or project name
        :param int definition_id: The ID of the definition.
        :rtype: [BuildDefinitionRevision]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if definition_id is not None:
            route_values['definitionId'] = self._serialize.url('definition_id', definition_id, 'int')
        response = self._send(http_method='GET',
                              location_id='7c116775-52e5-453e-8c5d-914d9762d8c4',
                              version='7.0',
                              route_values=route_values)
        return self._deserialize('[BuildDefinitionRevision]', self._unwrap_collection(response))

    def get_build_settings(self, project=None):
        """GetBuildSettings.
        Gets the build settings.
        :param str project: Project ID or project name
        :rtype: :class:`<BuildSettings> <azure.devops.v7_0.build.models.BuildSettings>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        response = self._send(http_method='GET',
                              location_id='aa8c1c9c-ef8b-474a-b8c4-785c7b191d0d',
                              version='7.0',
                              route_values=route_values)
        return self._deserialize('BuildSettings', response)

    def update_build_settings(self, settings, project=None):
        """UpdateBuildSettings.
        Updates the build settings.
        :param :class:`<BuildSettings> <azure.devops.v7_0.build.models.BuildSettings>` settings: The new settings.
        :param str project: Project ID or project name
        :rtype: :class:`<BuildSettings> <azure.devops.v7_0.build.models.BuildSettings>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(settings, 'BuildSettings')
        response = self._send(http_method='PATCH',
                              location_id='aa8c1c9c-ef8b-474a-b8c4-785c7b191d0d',
                              version='7.0',
                              route_values=route_values,
                              content=content)
        return self._deserialize('BuildSettings', response)

    def list_source_providers(self, project):
        """ListSourceProviders.
        Get a list of source providers and their capabilities.
        :param str project: Project ID or project name
        :rtype: [SourceProviderAttributes]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        response = self._send(http_method='GET',
                              location_id='3ce81729-954f-423d-a581-9fea01d25186',
                              version='7.0',
                              route_values=route_values)
        return self._deserialize('[SourceProviderAttributes]', self._unwrap_collection(response))

    def update_stage(self, update_parameters, build_id, stage_ref_name, project=None):
        """UpdateStage.
        Update a build stage
        :param :class:`<UpdateStageParameters> <azure.devops.v7_0.build.models.UpdateStageParameters>` update_parameters:
        :param int build_id:
        :param str stage_ref_name:
        :param str project: Project ID or project name
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        if stage_ref_name is not None:
            route_values['stageRefName'] = self._serialize.url('stage_ref_name', stage_ref_name, 'str')
        content = self._serialize.body(update_parameters, 'UpdateStageParameters')
        self._send(http_method='PATCH',
                   location_id='b8aac6c9-744b-46e1-88fc-3550969f9313',
                   version='7.0',
                   route_values=route_values,
                   content=content)

    def add_build_tag(self, project, build_id, tag):
        """AddBuildTag.
        Adds a tag to a build.
        :param str project: Project ID or project name
        :param int build_id: The ID of the build.
        :param str tag: The tag to add.
        :rtype: [str]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        if tag is not None:
            route_values['tag'] = self._serialize.url('tag', tag, 'str')
        response = self._send(http_method='PUT',
                              location_id='6e6114b2-8161-44c8-8f6c-c5505782427f',
                              version='7.0',
                              route_values=route_values)
        return self._deserialize('[str]', self._unwrap_collection(response))

    def add_build_tags(self, tags, project, build_id):
        """AddBuildTags.
        Adds tags to a build.
        :param [str] tags: The tags to add.
        :param str project: Project ID or project name
        :param int build_id: The ID of the build.
        :rtype: [str]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        content = self._serialize.body(tags, '[str]')
        response = self._send(http_method='POST',
                              location_id='6e6114b2-8161-44c8-8f6c-c5505782427f',
                              version='7.0',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[str]', self._unwrap_collection(response))

    def delete_build_tag(self, project, build_id, tag):
        """DeleteBuildTag.
        Removes a tag from a build. NOTE: This API will not work for tags with special characters. To remove tags with special characters, use the PATCH method instead (in 6.0+)
        :param str project: Project ID or project name
        :param int build_id: The ID of the build.
        :param str tag: The tag to remove.
        :rtype: [str]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        if tag is not None:
            route_values['tag'] = self._serialize.url('tag', tag, 'str')
        response = self._send(http_method='DELETE',
                              location_id='6e6114b2-8161-44c8-8f6c-c5505782427f',
                              version='7.0',
                              route_values=route_values)
        return self._deserialize('[str]', self._unwrap_collection(response))

    def get_build_tags(self, project, build_id):
        """GetBuildTags.
        Gets the tags for a build.
        :param str project: Project ID or project name
        :param int build_id: The ID of the build.
        :rtype: [str]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        response = self._send(http_method='GET',
                              location_id='6e6114b2-8161-44c8-8f6c-c5505782427f',
                              version='7.0',
                              route_values=route_values)
        return self._deserialize('[str]', self._unwrap_collection(response))

    def update_build_tags(self, update_parameters, project, build_id):
        """UpdateBuildTags.
        Adds/Removes tags from a build.
        :param :class:`<UpdateTagParameters> <azure.devops.v7_0.build.models.UpdateTagParameters>` update_parameters: The tags to add/remove.
        :param str project: Project ID or project name
        :param int build_id: The ID of the build.
        :rtype: [str]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        content = self._serialize.body(update_parameters, 'UpdateTagParameters')
        response = self._send(http_method='PATCH',
                              location_id='6e6114b2-8161-44c8-8f6c-c5505782427f',
                              version='7.0',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[str]', self._unwrap_collection(response))

    def add_definition_tag(self, project, definition_id, tag):
        """AddDefinitionTag.
        Adds a tag to a definition
        :param str project: Project ID or project name
        :param int definition_id: The ID of the definition.
        :param str tag: The tag to add.
        :rtype: [str]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if definition_id is not None:
            route_values['definitionId'] = self._serialize.url('definition_id', definition_id, 'int')
        if tag is not None:
            route_values['tag'] = self._serialize.url('tag', tag, 'str')
        response = self._send(http_method='PUT',
                              location_id='cb894432-134a-4d31-a839-83beceaace4b',
                              version='7.0',
                              route_values=route_values)
        return self._deserialize('[str]', self._unwrap_collection(response))

    def add_definition_tags(self, tags, project, definition_id):
        """AddDefinitionTags.
        Adds multiple tags to a definition.
        :param [str] tags: The tags to add.
        :param str project: Project ID or project name
        :param int definition_id: The ID of the definition.
        :rtype: [str]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if definition_id is not None:
            route_values['definitionId'] = self._serialize.url('definition_id', definition_id, 'int')
        content = self._serialize.body(tags, '[str]')
        response = self._send(http_method='POST',
                              location_id='cb894432-134a-4d31-a839-83beceaace4b',
                              version='7.0',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[str]', self._unwrap_collection(response))

    def delete_definition_tag(self, project, definition_id, tag):
        """DeleteDefinitionTag.
        Removes a tag from a definition. NOTE: This API will not work for tags with special characters. To remove tags with special characters, use the PATCH method instead (in 6.0+)
        :param str project: Project ID or project name
        :param int definition_id: The ID of the definition.
        :param str tag: The tag to remove.
        :rtype: [str]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if definition_id is not None:
            route_values['definitionId'] = self._serialize.url('definition_id', definition_id, 'int')
        if tag is not None:
            route_values['tag'] = self._serialize.url('tag', tag, 'str')
        response = self._send(http_method='DELETE',
                              location_id='cb894432-134a-4d31-a839-83beceaace4b',
                              version='7.0',
                              route_values=route_values)
        return self._deserialize('[str]', self._unwrap_collection(response))

    def get_definition_tags(self, project, definition_id, revision=None):
        """GetDefinitionTags.
        Gets the tags for a definition.
        :param str project: Project ID or project name
        :param int definition_id: The ID of the definition.
        :param int revision: The definition revision number. If not specified, uses the latest revision of the definition.
        :rtype: [str]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if definition_id is not None:
            route_values['definitionId'] = self._serialize.url('definition_id', definition_id, 'int')
        query_parameters = {}
        if revision is not None:
            query_parameters['revision'] = self._serialize.query('revision', revision, 'int')
        response = self._send(http_method='GET',
                              location_id='cb894432-134a-4d31-a839-83beceaace4b',
                              version='7.0',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[str]', self._unwrap_collection(response))

    def update_definition_tags(self, update_parameters, project, definition_id):
        """UpdateDefinitionTags.
        Adds/Removes tags from a definition.
        :param :class:`<UpdateTagParameters> <azure.devops.v7_0.build.models.UpdateTagParameters>` update_parameters: The tags to add/remove.
        :param str project: Project ID or project name
        :param int definition_id: The ID of the definition.
        :rtype: [str]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if definition_id is not None:
            route_values['definitionId'] = self._serialize.url('definition_id', definition_id, 'int')
        content = self._serialize.body(update_parameters, 'UpdateTagParameters')
        response = self._send(http_method='PATCH',
                              location_id='cb894432-134a-4d31-a839-83beceaace4b',
                              version='7.0',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[str]', self._unwrap_collection(response))

    def delete_tag(self, project, tag):
        """DeleteTag.
        Removes a tag from builds, definitions, and from the tag store
        :param str project: Project ID or project name
        :param str tag: The tag to remove.
        :rtype: [str]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if tag is not None:
            route_values['tag'] = self._serialize.url('tag', tag, 'str')
        response = self._send(http_method='DELETE',
                              location_id='d84ac5c6-edc7-43d5-adc9-1b34be5dea09',
                              version='7.0',
                              route_values=route_values)
        return self._deserialize('[str]', self._unwrap_collection(response))

    def get_tags(self, project):
        """GetTags.
        Gets a list of all build tags in the project.
        :param str project: Project ID or project name
        :rtype: [str]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        response = self._send(http_method='GET',
                              location_id='d84ac5c6-edc7-43d5-adc9-1b34be5dea09',
                              version='7.0',
                              route_values=route_values)
        return self._deserialize('[str]', self._unwrap_collection(response))

    def delete_template(self, project, template_id):
        """DeleteTemplate.
        Deletes a build definition template.
        :param str project: Project ID or project name
        :param str template_id: The ID of the template.
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if template_id is not None:
            route_values['templateId'] = self._serialize.url('template_id', template_id, 'str')
        self._send(http_method='DELETE',
                   location_id='e884571e-7f92-4d6a-9274-3f5649900835',
                   version='7.0',
                   route_values=route_values)

    def get_template(self, project, template_id):
        """GetTemplate.
        Gets a specific build definition template.
        :param str project: Project ID or project name
        :param str template_id: The ID of the requested template.
        :rtype: :class:`<BuildDefinitionTemplate> <azure.devops.v7_0.build.models.BuildDefinitionTemplate>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if template_id is not None:
            route_values['templateId'] = self._serialize.url('template_id', template_id, 'str')
        response = self._send(http_method='GET',
                              location_id='e884571e-7f92-4d6a-9274-3f5649900835',
                              version='7.0',
                              route_values=route_values)
        return self._deserialize('BuildDefinitionTemplate', response)

    def get_templates(self, project):
        """GetTemplates.
        Gets all definition templates.
        :param str project: Project ID or project name
        :rtype: [BuildDefinitionTemplate]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        response = self._send(http_method='GET',
                              location_id='e884571e-7f92-4d6a-9274-3f5649900835',
                              version='7.0',
                              route_values=route_values)
        return self._deserialize('[BuildDefinitionTemplate]', self._unwrap_collection(response))

    def save_template(self, template, project, template_id):
        """SaveTemplate.
        Updates an existing build definition template.
        :param :class:`<BuildDefinitionTemplate> <azure.devops.v7_0.build.models.BuildDefinitionTemplate>` template: The new version of the template.
        :param str project: Project ID or project name
        :param str template_id: The ID of the template.
        :rtype: :class:`<BuildDefinitionTemplate> <azure.devops.v7_0.build.models.BuildDefinitionTemplate>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if template_id is not None:
            route_values['templateId'] = self._serialize.url('template_id', template_id, 'str')
        content = self._serialize.body(template, 'BuildDefinitionTemplate')
        response = self._send(http_method='PUT',
                              location_id='e884571e-7f92-4d6a-9274-3f5649900835',
                              version='7.0',
                              route_values=route_values,
                              content=content)
        return self._deserialize('BuildDefinitionTemplate', response)

    def get_build_timeline(self, project, build_id, timeline_id=None, change_id=None, plan_id=None):
        """GetBuildTimeline.
        Gets details for a build
        :param str project: Project ID or project name
        :param int build_id:
        :param str timeline_id:
        :param int change_id:
        :param str plan_id:
        :rtype: :class:`<Timeline> <azure.devops.v7_0.build.models.Timeline>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        if timeline_id is not None:
            route_values['timelineId'] = self._serialize.url('timeline_id', timeline_id, 'str')
        query_parameters = {}
        if change_id is not None:
            query_parameters['changeId'] = self._serialize.query('change_id', change_id, 'int')
        if plan_id is not None:
            query_parameters['planId'] = self._serialize.query('plan_id', plan_id, 'str')
        response = self._send(http_method='GET',
                              location_id='8baac422-4c6e-4de5-8532-db96d92acffa',
                              version='7.0',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('Timeline', response)

    def restore_webhooks(self, trigger_types, project, provider_name, service_endpoint_id=None, repository=None):
        """RestoreWebhooks.
        Recreates the webhooks for the specified triggers in the given source code repository.
        :param [DefinitionTriggerType] trigger_types: The types of triggers to restore webhooks for.
        :param str project: Project ID or project name
        :param str provider_name: The name of the source provider.
        :param str service_endpoint_id: If specified, the ID of the service endpoint to query. Can only be omitted for providers that do not use service endpoints, e.g. TFVC or TFGit.
        :param str repository: If specified, the vendor-specific identifier or the name of the repository to get webhooks. Can only be omitted for providers that do not support multiple repositories.
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if provider_name is not None:
            route_values['providerName'] = self._serialize.url('provider_name', provider_name, 'str')
        query_parameters = {}
        if service_endpoint_id is not None:
            query_parameters['serviceEndpointId'] = self._serialize.query('service_endpoint_id', service_endpoint_id, 'str')
        if repository is not None:
            query_parameters['repository'] = self._serialize.query('repository', repository, 'str')
        content = self._serialize.body(trigger_types, '[DefinitionTriggerType]')
        self._send(http_method='POST',
                   location_id='793bceb8-9736-4030-bd2f-fb3ce6d6b478',
                   version='7.0',
                   route_values=route_values,
                   query_parameters=query_parameters,
                   content=content)

    def list_webhooks(self, project, provider_name, service_endpoint_id=None, repository=None):
        """ListWebhooks.
        Gets a list of webhooks installed in the given source code repository.
        :param str project: Project ID or project name
        :param str provider_name: The name of the source provider.
        :param str service_endpoint_id: If specified, the ID of the service endpoint to query. Can only be omitted for providers that do not use service endpoints, e.g. TFVC or TFGit.
        :param str repository: If specified, the vendor-specific identifier or the name of the repository to get webhooks. Can only be omitted for providers that do not support multiple repositories.
        :rtype: [RepositoryWebhook]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if provider_name is not None:
            route_values['providerName'] = self._serialize.url('provider_name', provider_name, 'str')
        query_parameters = {}
        if service_endpoint_id is not None:
            query_parameters['serviceEndpointId'] = self._serialize.query('service_endpoint_id', service_endpoint_id, 'str')
        if repository is not None:
            query_parameters['repository'] = self._serialize.query('repository', repository, 'str')
        response = self._send(http_method='GET',
                              location_id='8f20ff82-9498-4812-9f6e-9c01bdc50e99',
                              version='7.0',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[RepositoryWebhook]', self._unwrap_collection(response))

    def get_build_work_items_refs(self, project, build_id, top=None):
        """GetBuildWorkItemsRefs.
        Gets the work items associated with a build. Only work items in the same project are returned.
        :param str project: Project ID or project name
        :param int build_id: The ID of the build.
        :param int top: The maximum number of work items to return.
        :rtype: [ResourceRef]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        query_parameters = {}
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        response = self._send(http_method='GET',
                              location_id='5a21f5d2-5642-47e4-a0bd-1356e6731bee',
                              version='7.0',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[ResourceRef]', self._unwrap_collection(response))

    def get_build_work_items_refs_from_commits(self, commit_ids, project, build_id, top=None):
        """GetBuildWorkItemsRefsFromCommits.
        Gets the work items associated with a build, filtered to specific commits.
        :param [str] commit_ids: A comma-delimited list of commit IDs.
        :param str project: Project ID or project name
        :param int build_id: The ID of the build.
        :param int top: The maximum number of work items to return, or the number of commits to consider if no commit IDs are specified.
        :rtype: [ResourceRef]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        query_parameters = {}
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        content = self._serialize.body(commit_ids, '[str]')
        response = self._send(http_method='POST',
                              location_id='5a21f5d2-5642-47e4-a0bd-1356e6731bee',
                              version='7.0',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('[ResourceRef]', self._unwrap_collection(response))

    def get_work_items_between_builds(self, project, from_build_id, to_build_id, top=None):
        """GetWorkItemsBetweenBuilds.
        Gets all the work items between two builds.
        :param str project: Project ID or project name
        :param int from_build_id: The ID of the first build.
        :param int to_build_id: The ID of the last build.
        :param int top: The maximum number of work items to return.
        :rtype: [ResourceRef]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if from_build_id is not None:
            query_parameters['fromBuildId'] = self._serialize.query('from_build_id', from_build_id, 'int')
        if to_build_id is not None:
            query_parameters['toBuildId'] = self._serialize.query('to_build_id', to_build_id, 'int')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        response = self._send(http_method='GET',
                              location_id='52ba8915-5518-42e3-a4bb-b0182d159e2d',
                              version='7.0',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[ResourceRef]', self._unwrap_collection(response))

    def get_definition_yaml(self, project, definition_id, revision=None, min_metrics_time=None, property_filters=None, include_latest_builds=None):
        """GetDefinitionYaml.
        Converts a definition to YAML, optionally at a specific revision.
        :param str project: Project ID or project name
        :param int definition_id: The ID of the definition.
        :param int revision: The revision number to retrieve. If this is not specified, the latest version will be returned.
        :param datetime min_metrics_time: If specified, indicates the date from which metrics should be included.
        :param [str] property_filters: A comma-delimited list of properties to include in the results.
        :param bool include_latest_builds:
        :rtype: :class:`<YamlBuild> <azure.devops.v7_0.build.models.YamlBuild>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if definition_id is not None:
            route_values['definitionId'] = self._serialize.url('definition_id', definition_id, 'int')
        query_parameters = {}
        if revision is not None:
            query_parameters['revision'] = self._serialize.query('revision', revision, 'int')
        if min_metrics_time is not None:
            query_parameters['minMetricsTime'] = self._serialize.query('min_metrics_time', min_metrics_time, 'iso-8601')
        if property_filters is not None:
            property_filters = ",".join(property_filters)
            query_parameters['propertyFilters'] = self._serialize.query('property_filters', property_filters, 'str')
        if include_latest_builds is not None:
            query_parameters['includeLatestBuilds'] = self._serialize.query('include_latest_builds', include_latest_builds, 'bool')
        response = self._send(http_method='GET',
                              location_id='7c3df3a1-7e51-4150-8cf7-540347f8697f',
                              version='7.0',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('YamlBuild', response)

