# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ..vss_client import VssClient
from . import models


class BuildClient(VssClient):
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

    def create_artifact(self, artifact, build_id, project=None):
        """CreateArtifact.
        [Preview API] Associates an artifact with a vsts_cli_build
        :param :class:`<BuildArtifact> <vsts_cli_build.models.BuildArtifact>` artifact:
        :param int build_id:
        :param str project: Project ID or project name
        :rtype: :class:`<BuildArtifact> <vsts_cli_build.models.BuildArtifact>`
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str'),
            'buildId': self._serialize.url('build_id', build_id, 'int')
        }
        content = self._serialize.body(artifact, 'BuildArtifact')
        response = self._send(http_method='POST',
                              location_id='1db06c96-014e-44e1-ac91-90b2d4b3e984',
                              version='4.1-preview.3',
                              route_values=route_values,
                              content=content)
        return self._deserialize('BuildArtifact', response)

    def get_artifact(self, build_id, artifact_name, project=None):
        """GetArtifact.
        [Preview API] Gets a specific artifact for a vsts_cli_build
        :param int build_id:
        :param str artifact_name:
        :param str project: Project ID or project name
        :rtype: :class:`<BuildArtifact> <vsts_cli_build.models.BuildArtifact>`
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str'),
            'buildId': self._serialize.url('build_id', build_id, 'int')
        }
        query_parameters = {}
        if artifact_name is not None:
            query_parameters['artifactName'] = self._serialize.query('artifact_name', artifact_name, 'str')
        response = self._send(http_method='GET',
                              location_id='1db06c96-014e-44e1-ac91-90b2d4b3e984',
                              version='4.1-preview.3',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('BuildArtifact', response)

    def get_artifact_content_zip(self, build_id, artifact_name, project=None):
        """GetArtifactContentZip.
        [Preview API] Gets a specific artifact for a vsts_cli_build
        :param int build_id:
        :param str artifact_name:
        :param str project: Project ID or project name
        :rtype: object
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str'),
            'buildId': self._serialize.url('build_id', build_id, 'int')
        }
        query_parameters = {}
        if artifact_name is not None:
            query_parameters['artifactName'] = self._serialize.query('artifact_name', artifact_name, 'str')
        response = self._send(http_method='GET',
                              location_id='1db06c96-014e-44e1-ac91-90b2d4b3e984',
                              version='4.1-preview.3',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('object', response)

    def get_artifacts(self, build_id, project=None):
        """GetArtifacts.
        [Preview API] Gets all artifacts for a vsts_cli_build
        :param int build_id:
        :param str project: Project ID or project name
        :rtype: [BuildArtifact]
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str'),
            'buildId': self._serialize.url('build_id', build_id, 'int')
        }
        response = self._send(http_method='GET',
                              location_id='1db06c96-014e-44e1-ac91-90b2d4b3e984',
                              version='4.1-preview.3',
                              route_values=route_values,
                              returns_collection=True)
        return self._deserialize('[BuildArtifact]', response)

    def get_badge(self, project, definition_id, branch_name=None):
        """GetBadge.
        [Preview API]
        :param str project:
        :param int definition_id:
        :param str branch_name:
        :rtype: str
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str'),
            'definitionId': self._serialize.url('definition_id', definition_id, 'int')
        }
        query_parameters = {}
        if branch_name is not None:
            query_parameters['branchName'] = self._serialize.query('branch_name', branch_name, 'str')
        response = self._send(http_method='GET',
                              location_id='de6a4df8-22cd-44ee-af2d-39f6aa7a4261',
                              version='4.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('str', response)

    def get_build_badge(self, project, repo_type, repo_id=None, branch_name=None):
        """GetBuildBadge.
        [Preview API]
        :param str project: Project ID or project name
        :param str repo_type:
        :param str repo_id:
        :param str branch_name:
        :rtype: :class:`<BuildBadge> <vsts_cli_build.models.BuildBadge>`
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str'),
            'repoType': self._serialize.url('repo_type', repo_type, 'str')
        }
        query_parameters = {}
        if repo_id is not None:
            query_parameters['repoId'] = self._serialize.query('repo_id', repo_id, 'str')
        if branch_name is not None:
            query_parameters['branchName'] = self._serialize.query('branch_name', branch_name, 'str')
        response = self._send(http_method='GET',
                              location_id='21b3b9ce-fad5-4567-9ad0-80679794e003',
                              version='4.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('BuildBadge', response)

    def get_build_badge_data(self, project, repo_type, repo_id=None, branch_name=None):
        """GetBuildBadgeData.
        [Preview API]
        :param str project: Project ID or project name
        :param str repo_type:
        :param str repo_id:
        :param str branch_name:
        :rtype: str
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str'),
            'repoType': self._serialize.url('repo_type', repo_type, 'str')
        }
        query_parameters = {}
        if repo_id is not None:
            query_parameters['repoId'] = self._serialize.query('repo_id', repo_id, 'str')
        if branch_name is not None:
            query_parameters['branchName'] = self._serialize.query('branch_name', branch_name, 'str')
        response = self._send(http_method='GET',
                              location_id='21b3b9ce-fad5-4567-9ad0-80679794e003',
                              version='4.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('str', response)

    def delete_build(self, build_id, project=None):
        """DeleteBuild.
        [Preview API] Deletes a vsts_cli_build
        :param int build_id:
        :param str project: Project ID or project name
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str'),
            'buildId': self._serialize.url('build_id', build_id, 'int')
        }
        self._send(http_method='DELETE',
                   location_id='0cd358e1-9217-4d94-8269-1c1ee6f93dcf',
                   version='4.1-preview.3',
                   route_values=route_values)

    def get_build(self, build_id, project=None, property_filters=None):
        """GetBuild.
        [Preview API] Gets a vsts_cli_build
        :param int build_id:
        :param str project: Project ID or project name
        :param str property_filters: A comma-delimited list of properties to include in the results
        :rtype: :class:`<Build> <vsts_cli_build.models.Build>`
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str'),
            'buildId': self._serialize.url('build_id', build_id, 'int')
        }
        query_parameters = {}
        if property_filters is not None:
            query_parameters['propertyFilters'] = self._serialize.query('property_filters', property_filters, 'str')
        response = self._send(http_method='GET',
                              location_id='0cd358e1-9217-4d94-8269-1c1ee6f93dcf',
                              version='4.1-preview.3',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('Build', response)

    def get_builds(self, project=None, definitions=None, queues=None, build_number=None, min_finish_time=None, max_finish_time=None, requested_for=None, reason_filter=None, status_filter=None, result_filter=None, tag_filters=None, properties=None, top=None, continuation_token=None, max_builds_per_definition=None, deleted_filter=None, query_order=None, branch_name=None, build_ids=None, repository_id=None, repository_type=None):
        """GetBuilds.
        [Preview API] Gets builds
        :param str project: Project ID or project name
        :param [int] definitions: A comma-delimited list of definition ids
        :param [int] queues: A comma-delimited list of queue ids
        :param str build_number:
        :param datetime min_finish_time:
        :param datetime max_finish_time:
        :param str requested_for:
        :param BuildReason reason_filter:
        :param BuildStatus status_filter:
        :param BuildResult result_filter:
        :param [str] tag_filters: A comma-delimited list of tags
        :param [str] properties: A comma-delimited list of properties to include in the results
        :param int top: The maximum number of builds to retrieve
        :param str continuation_token:
        :param int max_builds_per_definition:
        :param QueryDeletedOption deleted_filter:
        :param BuildQueryOrder query_order:
        :param str branch_name:
        :param [int] build_ids:
        :param str repository_id:
        :param str repository_type:
        :rtype: [Build]
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str')
        }
        query_parameters = {}
        if definitions is not None:
            definitions = ",".join(map(str, definitions))
            query_parameters['definitions'] = self._serialize.query('definitions', definitions, 'str')
        if queues is not None:
            queues = ",".join(map(str, queues))
            query_parameters['queues'] = self._serialize.query('queues', queues, 'str')
        if build_number is not None:
            query_parameters['buildNumber'] = self._serialize.query('build_number', build_number, 'str')
        if min_finish_time is not None:
            query_parameters['minFinishTime'] = self._serialize.query('min_finish_time', min_finish_time, 'datetime')
        if max_finish_time is not None:
            query_parameters['maxFinishTime'] = self._serialize.query('max_finish_time', max_finish_time, 'datetime')
        if requested_for is not None:
            query_parameters['requestedFor'] = self._serialize.query('requested_for', requested_for, 'str')
        if reason_filter is not None:
            query_parameters['reasonFilter'] = self._serialize.query('reason_filter', reason_filter, 'BuildReason')
        if status_filter is not None:
            query_parameters['statusFilter'] = self._serialize.query('status_filter', status_filter, 'BuildStatus')
        if result_filter is not None:
            query_parameters['resultFilter'] = self._serialize.query('result_filter', result_filter, 'BuildResult')
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
            query_parameters['deletedFilter'] = self._serialize.query('deleted_filter', deleted_filter, 'QueryDeletedOption')
        if query_order is not None:
            query_parameters['queryOrder'] = self._serialize.query('query_order', query_order, 'BuildQueryOrder')
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
                              version='4.1-preview.3',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              returns_collection=True)
        return self._deserialize('[Build]', response)

    def queue_build(self, build, project=None, ignore_warnings=None, check_in_ticket=None):
        """QueueBuild.
        [Preview API] Queues a vsts_cli_build
        :param :class:`<Build> <vsts_cli_build.models.Build>` build:
        :param str project: Project ID or project name
        :param bool ignore_warnings:
        :param str check_in_ticket:
        :rtype: :class:`<Build> <vsts_cli_build.models.Build>`
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str')
        }
        query_parameters = {}
        if ignore_warnings is not None:
            query_parameters['ignoreWarnings'] = self._serialize.query('ignore_warnings', ignore_warnings, 'bool')
        if check_in_ticket is not None:
            query_parameters['checkInTicket'] = self._serialize.query('check_in_ticket', check_in_ticket, 'str')
        content = self._serialize.body(build, 'Build')
        response = self._send(http_method='POST',
                              location_id='0cd358e1-9217-4d94-8269-1c1ee6f93dcf',
                              version='4.1-preview.3',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('Build', response)

    def update_build(self, build, build_id, project=None):
        """UpdateBuild.
        [Preview API] Updates a vsts_cli_build
        :param :class:`<Build> <vsts_cli_build.models.Build>` build:
        :param int build_id:
        :param str project: Project ID or project name
        :rtype: :class:`<Build> <vsts_cli_build.models.Build>`
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str'),
            'buildId': self._serialize.url('build_id', build_id, 'int')
        }
        content = self._serialize.body(build, 'Build')
        response = self._send(http_method='PATCH',
                              location_id='0cd358e1-9217-4d94-8269-1c1ee6f93dcf',
                              version='4.1-preview.3',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Build', response)

    def update_builds(self, builds, project=None):
        """UpdateBuilds.
        [Preview API] Update a batch of builds
        :param [Build] builds:
        :param str project: Project ID or project name
        :rtype: [Build]
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str')
        }
        content = self._serialize.body(builds, '[Build]')
        response = self._send(http_method='PATCH',
                              location_id='0cd358e1-9217-4d94-8269-1c1ee6f93dcf',
                              version='4.1-preview.3',
                              route_values=route_values,
                              content=content,
                              returns_collection=True)
        return self._deserialize('[Build]', response)

    def get_build_changes(self, project, build_id, continuation_token=None, top=None, include_source_change=None):
        """GetBuildChanges.
        [Preview API] Gets the changes associated with a vsts_cli_build
        :param str project: Project ID or project name
        :param int build_id:
        :param str continuation_token:
        :param int top: The maximum number of changes to return
        :param bool include_source_change:
        :rtype: [Change]
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str'),
            'buildId': self._serialize.url('build_id', build_id, 'int')
        }
        query_parameters = {}
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if include_source_change is not None:
            query_parameters['includeSourceChange'] = self._serialize.query('include_source_change', include_source_change, 'bool')
        response = self._send(http_method='GET',
                              location_id='54572c7b-bbd3-45d4-80dc-28be08941620',
                              version='4.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              returns_collection=True)
        return self._deserialize('[Change]', response)

    def get_changes_between_builds(self, project, from_build_id=None, to_build_id=None, top=None):
        """GetChangesBetweenBuilds.
        [Preview API] Gets the changes associated between given builds
        :param str project: Project ID or project name
        :param int from_build_id:
        :param int to_build_id:
        :param int top: The maximum number of changes to return
        :rtype: [Change]
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str')
        }
        query_parameters = {}
        if from_build_id is not None:
            query_parameters['fromBuildId'] = self._serialize.query('from_build_id', from_build_id, 'int')
        if to_build_id is not None:
            query_parameters['toBuildId'] = self._serialize.query('to_build_id', to_build_id, 'int')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        response = self._send(http_method='GET',
                              location_id='f10f0ea5-18a1-43ec-a8fb-2042c7be9b43',
                              version='4.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              returns_collection=True)
        return self._deserialize('[Change]', response)

    def get_build_controller(self, controller_id):
        """GetBuildController.
        [Preview API] Gets a controller
        :param int controller_id:
        :rtype: :class:`<BuildController> <vsts_cli_build.models.BuildController>`
        """
        route_values = {
            'controllerId': self._serialize.url('controller_id', controller_id, 'int')
        }
        response = self._send(http_method='GET',
                              location_id='fcac1932-2ee1-437f-9b6f-7f696be858f6',
                              version='4.1-preview.2',
                              route_values=route_values)
        return self._deserialize('BuildController', response)

    def get_build_controllers(self, name=None):
        """GetBuildControllers.
        [Preview API] Gets controller, optionally filtered by name
        :param str name:
        :rtype: [BuildController]
        """
        query_parameters = {}
        if name is not None:
            query_parameters['name'] = self._serialize.query('name', name, 'str')
        response = self._send(http_method='GET',
                              location_id='fcac1932-2ee1-437f-9b6f-7f696be858f6',
                              version='4.1-preview.2',
                              query_parameters=query_parameters,
                              returns_collection=True)
        return self._deserialize('[BuildController]', response)

    def create_definition(self, definition, project=None, definition_to_clone_id=None, definition_to_clone_revision=None):
        """CreateDefinition.
        [Preview API] Creates a new definition
        :param :class:`<BuildDefinition> <vsts_cli_build.models.BuildDefinition>` definition:
        :param str project: Project ID or project name
        :param int definition_to_clone_id:
        :param int definition_to_clone_revision:
        :rtype: :class:`<BuildDefinition> <vsts_cli_build.models.BuildDefinition>`
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str')
        }
        query_parameters = {}
        if definition_to_clone_id is not None:
            query_parameters['definitionToCloneId'] = self._serialize.query('definition_to_clone_id', definition_to_clone_id, 'int')
        if definition_to_clone_revision is not None:
            query_parameters['definitionToCloneRevision'] = self._serialize.query('definition_to_clone_revision', definition_to_clone_revision, 'int')
        content = self._serialize.body(definition, 'BuildDefinition')
        response = self._send(http_method='POST',
                              location_id='dbeaf647-6167-421a-bda9-c9327b25e2e6',
                              version='4.1-preview.6',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('BuildDefinition', response)

    def delete_definition(self, definition_id, project=None):
        """DeleteDefinition.
        [Preview API] Deletes a definition and all associated builds
        :param int definition_id:
        :param str project: Project ID or project name
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str'),
            'definitionId': self._serialize.url('definition_id', definition_id, 'int')
        }
        self._send(http_method='DELETE',
                   location_id='dbeaf647-6167-421a-bda9-c9327b25e2e6',
                   version='4.1-preview.6',
                   route_values=route_values)

    def get_definition(self, definition_id, project=None, revision=None, min_metrics_time=None, property_filters=None, include_latest_builds=None):
        """GetDefinition.
        [Preview API] Gets a definition, optionally at a specific revision
        :param int definition_id:
        :param str project: Project ID or project name
        :param int revision:
        :param datetime min_metrics_time:
        :param [str] property_filters:
        :param bool include_latest_builds:
        :rtype: :class:`<BuildDefinition> <vsts_cli_build.models.BuildDefinition>`
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str'),
            'definitionId': self._serialize.url('definition_id', definition_id, 'int')
        }
        query_parameters = {}
        if revision is not None:
            query_parameters['revision'] = self._serialize.query('revision', revision, 'int')
        if min_metrics_time is not None:
            query_parameters['minMetricsTime'] = self._serialize.query('min_metrics_time', min_metrics_time, 'datetime')
        if property_filters is not None:
            property_filters = ",".join(property_filters)
            query_parameters['propertyFilters'] = self._serialize.query('property_filters', property_filters, 'str')
        if include_latest_builds is not None:
            query_parameters['includeLatestBuilds'] = self._serialize.query('include_latest_builds', include_latest_builds, 'bool')
        response = self._send(http_method='GET',
                              location_id='dbeaf647-6167-421a-bda9-c9327b25e2e6',
                              version='4.1-preview.6',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('BuildDefinition', response)

    def get_definitions(self, project=None, name=None, repository_id=None, repository_type=None, query_order=None, top=None, continuation_token=None, min_metrics_time=None, definition_ids=None, path=None, built_after=None, not_built_after=None, include_all_properties=None, include_latest_builds=None, task_id_filter=None):
        """GetDefinitions.
        [Preview API] Gets definitions, optionally filtered by name
        :param str project: Project ID or project name
        :param str name:
        :param str repository_id:
        :param str repository_type:
        :param DefinitionQueryOrder query_order:
        :param int top:
        :param str continuation_token:
        :param datetime min_metrics_time:
        :param [int] definition_ids:
        :param str path:
        :param datetime built_after:
        :param datetime not_built_after:
        :param bool include_all_properties:
        :param bool include_latest_builds:
        :param str task_id_filter:
        :rtype: [BuildDefinitionReference]
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str')
        }
        query_parameters = {}
        if name is not None:
            query_parameters['name'] = self._serialize.query('name', name, 'str')
        if repository_id is not None:
            query_parameters['repositoryId'] = self._serialize.query('repository_id', repository_id, 'str')
        if repository_type is not None:
            query_parameters['repositoryType'] = self._serialize.query('repository_type', repository_type, 'str')
        if query_order is not None:
            query_parameters['queryOrder'] = self._serialize.query('query_order', query_order, 'DefinitionQueryOrder')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        if min_metrics_time is not None:
            query_parameters['minMetricsTime'] = self._serialize.query('min_metrics_time', min_metrics_time, 'datetime')
        if definition_ids is not None:
            definition_ids = ",".join(map(str, definition_ids))
            query_parameters['definitionIds'] = self._serialize.query('definition_ids', definition_ids, 'str')
        if path is not None:
            query_parameters['path'] = self._serialize.query('path', path, 'str')
        if built_after is not None:
            query_parameters['builtAfter'] = self._serialize.query('built_after', built_after, 'datetime')
        if not_built_after is not None:
            query_parameters['notBuiltAfter'] = self._serialize.query('not_built_after', not_built_after, 'datetime')
        if include_all_properties is not None:
            query_parameters['includeAllProperties'] = self._serialize.query('include_all_properties', include_all_properties, 'bool')
        if include_latest_builds is not None:
            query_parameters['includeLatestBuilds'] = self._serialize.query('include_latest_builds', include_latest_builds, 'bool')
        if task_id_filter is not None:
            query_parameters['taskIdFilter'] = self._serialize.query('task_id_filter', task_id_filter, 'str')
        response = self._send(http_method='GET',
                              location_id='dbeaf647-6167-421a-bda9-c9327b25e2e6',
                              version='4.1-preview.6',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              returns_collection=True)
        return self._deserialize('[BuildDefinitionReference]', response)

    def update_definition(self, definition, definition_id, project=None, secrets_source_definition_id=None, secrets_source_definition_revision=None):
        """UpdateDefinition.
        [Preview API] Updates an existing definition
        :param :class:`<BuildDefinition> <vsts_cli_build.models.BuildDefinition>` definition:
        :param int definition_id:
        :param str project: Project ID or project name
        :param int secrets_source_definition_id:
        :param int secrets_source_definition_revision:
        :rtype: :class:`<BuildDefinition> <vsts_cli_build.models.BuildDefinition>`
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str'),
            'definitionId': self._serialize.url('definition_id', definition_id, 'int')
        }
        query_parameters = {}
        if secrets_source_definition_id is not None:
            query_parameters['secretsSourceDefinitionId'] = self._serialize.query('secrets_source_definition_id', secrets_source_definition_id, 'int')
        if secrets_source_definition_revision is not None:
            query_parameters['secretsSourceDefinitionRevision'] = self._serialize.query('secrets_source_definition_revision', secrets_source_definition_revision, 'int')
        content = self._serialize.body(definition, 'BuildDefinition')
        response = self._send(http_method='PUT',
                              location_id='dbeaf647-6167-421a-bda9-c9327b25e2e6',
                              version='4.1-preview.6',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('BuildDefinition', response)

    def create_folder(self, folder, project, path):
        """CreateFolder.
        [Preview API] Creates a new folder
        :param :class:`<Folder> <vsts_cli_build.models.Folder>` folder:
        :param str project: Project ID or project name
        :param str path:
        :rtype: :class:`<Folder> <vsts_cli_build.models.Folder>`
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str'),
            'path': self._serialize.url('path', path, 'str')
        }
        content = self._serialize.body(folder, 'Folder')
        response = self._send(http_method='PUT',
                              location_id='a906531b-d2da-4f55-bda7-f3e676cc50d9',
                              version='4.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Folder', response)

    def delete_folder(self, project, path):
        """DeleteFolder.
        [Preview API] Deletes a definition folder for given folder name and path and all it's existing definitions and it's corresponding builds
        :param str project: Project ID or project name
        :param str path:
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str'),
            'path': self._serialize.url('path', path, 'str')
        }
        self._send(http_method='DELETE',
                   location_id='a906531b-d2da-4f55-bda7-f3e676cc50d9',
                   version='4.1-preview.1',
                   route_values=route_values)

    def get_folders(self, project, path=None, query_order=None):
        """GetFolders.
        [Preview API] Gets folders
        :param str project: Project ID or project name
        :param str path:
        :param FolderQueryOrder query_order:
        :rtype: [Folder]
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str'),
            'path': self._serialize.url('path', path, 'str')
        }
        query_parameters = {}
        if query_order is not None:
            query_parameters['queryOrder'] = self._serialize.query('query_order', query_order, 'FolderQueryOrder')
        response = self._send(http_method='GET',
                              location_id='a906531b-d2da-4f55-bda7-f3e676cc50d9',
                              version='4.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              returns_collection=True)
        return self._deserialize('[Folder]', response)

    def update_folder(self, folder, project, path):
        """UpdateFolder.
        [Preview API] Updates an existing folder at given  existing path
        :param :class:`<Folder> <vsts_cli_build.models.Folder>` folder:
        :param str project: Project ID or project name
        :param str path:
        :rtype: :class:`<Folder> <vsts_cli_build.models.Folder>`
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str'),
            'path': self._serialize.url('path', path, 'str')
        }
        content = self._serialize.body(folder, 'Folder')
        response = self._send(http_method='POST',
                              location_id='a906531b-d2da-4f55-bda7-f3e676cc50d9',
                              version='4.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Folder', response)

    def get_build_log(self, project, build_id, log_id, start_line=None, end_line=None):
        """GetBuildLog.
        [Preview API] Gets a log
        :param str project: Project ID or project name
        :param int build_id:
        :param int log_id:
        :param long start_line:
        :param long end_line:
        :rtype: object
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str'),
            'buildId': self._serialize.url('build_id', build_id, 'int'),
            'logId': self._serialize.url('log_id', log_id, 'int')
        }
        query_parameters = {}
        if start_line is not None:
            query_parameters['startLine'] = self._serialize.query('start_line', start_line, 'long')
        if end_line is not None:
            query_parameters['endLine'] = self._serialize.query('end_line', end_line, 'long')
        response = self._send(http_method='GET',
                              location_id='35a80daf-7f30-45fc-86e8-6b813d9c90df',
                              version='4.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('object', response)

    def get_build_log_lines(self, project, build_id, log_id, start_line=None, end_line=None):
        """GetBuildLogLines.
        [Preview API] Gets a log
        :param str project: Project ID or project name
        :param int build_id:
        :param int log_id:
        :param long start_line:
        :param long end_line:
        :rtype: [str]
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str'),
            'buildId': self._serialize.url('build_id', build_id, 'int'),
            'logId': self._serialize.url('log_id', log_id, 'int')
        }
        query_parameters = {}
        if start_line is not None:
            query_parameters['startLine'] = self._serialize.query('start_line', start_line, 'long')
        if end_line is not None:
            query_parameters['endLine'] = self._serialize.query('end_line', end_line, 'long')
        response = self._send(http_method='GET',
                              location_id='35a80daf-7f30-45fc-86e8-6b813d9c90df',
                              version='4.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              returns_collection=True)
        return self._deserialize('[str]', response)

    def get_build_logs(self, project, build_id):
        """GetBuildLogs.
        [Preview API] Gets logs for a vsts_cli_build
        :param str project: Project ID or project name
        :param int build_id:
        :rtype: [BuildLog]
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str'),
            'buildId': self._serialize.url('build_id', build_id, 'int')
        }
        response = self._send(http_method='GET',
                              location_id='35a80daf-7f30-45fc-86e8-6b813d9c90df',
                              version='4.1-preview.2',
                              route_values=route_values,
                              returns_collection=True)
        return self._deserialize('[BuildLog]', response)

    def get_build_logs_zip(self, project, build_id):
        """GetBuildLogsZip.
        [Preview API] Gets logs for a vsts_cli_build
        :param str project: Project ID or project name
        :param int build_id:
        :rtype: object
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str'),
            'buildId': self._serialize.url('build_id', build_id, 'int')
        }
        response = self._send(http_method='GET',
                              location_id='35a80daf-7f30-45fc-86e8-6b813d9c90df',
                              version='4.1-preview.2',
                              route_values=route_values)
        return self._deserialize('object', response)

    def get_project_metrics(self, project, metric_aggregation_type=None, min_metrics_time=None):
        """GetProjectMetrics.
        [Preview API] Gets metrics of a project
        :param str project: Project ID or project name
        :param str metric_aggregation_type:
        :param datetime min_metrics_time:
        :rtype: [BuildMetric]
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str'),
            'metricAggregationType': self._serialize.url('metric_aggregation_type', metric_aggregation_type, 'str')
        }
        query_parameters = {}
        if min_metrics_time is not None:
            query_parameters['minMetricsTime'] = self._serialize.query('min_metrics_time', min_metrics_time, 'datetime')
        response = self._send(http_method='GET',
                              location_id='7433fae7-a6bc-41dc-a6e2-eef9005ce41a',
                              version='4.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              returns_collection=True)
        return self._deserialize('[BuildMetric]', response)

    def get_definition_metrics(self, project, definition_id, min_metrics_time=None):
        """GetDefinitionMetrics.
        [Preview API] Gets metrics of a definition
        :param str project: Project ID or project name
        :param int definition_id:
        :param datetime min_metrics_time:
        :rtype: [BuildMetric]
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str'),
            'definitionId': self._serialize.url('definition_id', definition_id, 'int')
        }
        query_parameters = {}
        if min_metrics_time is not None:
            query_parameters['minMetricsTime'] = self._serialize.query('min_metrics_time', min_metrics_time, 'datetime')
        response = self._send(http_method='GET',
                              location_id='d973b939-0ce0-4fec-91d8-da3940fa1827',
                              version='4.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              returns_collection=True)
        return self._deserialize('[BuildMetric]', response)

    def get_build_option_definitions(self, project=None):
        """GetBuildOptionDefinitions.
        [Preview API] Gets all vsts_cli_build option definitions
        :param str project: Project ID or project name
        :rtype: [BuildOptionDefinition]
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str')
        }
        response = self._send(http_method='GET',
                              location_id='591cb5a4-2d46-4f3a-a697-5cd42b6bd332',
                              version='4.1-preview.2',
                              route_values=route_values,
                              returns_collection=True)
        return self._deserialize('[BuildOptionDefinition]', response)

    def get_build_properties(self, project, build_id, filter=None):
        """GetBuildProperties.
        [Preview API] Gets properties for a vsts_cli_build.
        :param str project: Project ID or project name
        :param int build_id: The vsts_cli_build id.
        :param [str] filter: Filter to specific properties. Defaults to all properties.
        :rtype: :class:`<object> <vsts_cli_build.models.object>`
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str'),
            'buildId': self._serialize.url('build_id', build_id, 'int')
        }
        query_parameters = {}
        if filter is not None:
            filter = ",".join(filter)
            query_parameters['filter'] = self._serialize.query('filter', filter, 'str')
        response = self._send(http_method='GET',
                              location_id='0a6312e9-0627-49b7-8083-7d74a64849c9',
                              version='4.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('object', response)

    def update_build_properties(self, document, project, build_id):
        """UpdateBuildProperties.
        [Preview API] Updates properties for a vsts_cli_build.
        :param :class:`<[JsonPatchOperation]> <vsts_cli_build.models.[JsonPatchOperation]>` document:
        :param str project: Project ID or project name
        :param int build_id: The vsts_cli_build id.
        :rtype: :class:`<object> <vsts_cli_build.models.object>`
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str'),
            'buildId': self._serialize.url('build_id', build_id, 'int')
        }
        content = self._serialize.body(document, '[JsonPatchOperation]')
        response = self._send(http_method='PATCH',
                              location_id='0a6312e9-0627-49b7-8083-7d74a64849c9',
                              version='4.1-preview.1',
                              route_values=route_values,
                              content=content,
                              media_type='application/json-patch+json')
        return self._deserialize('object', response)

    def get_definition_properties(self, project, definition_id, filter=None):
        """GetDefinitionProperties.
        [Preview API] Gets properties for a definition.
        :param str project: Project ID or project name
        :param int definition_id: The definition id.
        :param [str] filter: Filter to specific properties. Defaults to all properties.
        :rtype: :class:`<object> <vsts_cli_build.models.object>`
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str'),
            'definitionId': self._serialize.url('definition_id', definition_id, 'int')
        }
        query_parameters = {}
        if filter is not None:
            filter = ",".join(filter)
            query_parameters['filter'] = self._serialize.query('filter', filter, 'str')
        response = self._send(http_method='GET',
                              location_id='d9826ad7-2a68-46a9-a6e9-677698777895',
                              version='4.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('object', response)

    def update_definition_properties(self, document, project, definition_id):
        """UpdateDefinitionProperties.
        [Preview API] Updates properties for a definition.
        :param :class:`<[JsonPatchOperation]> <vsts_cli_build.models.[JsonPatchOperation]>` document:
        :param str project: Project ID or project name
        :param int definition_id: The definition id.
        :rtype: :class:`<object> <vsts_cli_build.models.object>`
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str'),
            'definitionId': self._serialize.url('definition_id', definition_id, 'int')
        }
        content = self._serialize.body(document, '[JsonPatchOperation]')
        response = self._send(http_method='PATCH',
                              location_id='d9826ad7-2a68-46a9-a6e9-677698777895',
                              version='4.1-preview.1',
                              route_values=route_values,
                              content=content,
                              media_type='application/json-patch+json')
        return self._deserialize('object', response)

    def get_build_report(self, project, build_id, type=None):
        """GetBuildReport.
        [Preview API] Gets report for a vsts_cli_build
        :param str project: Project ID or project name
        :param int build_id:
        :param str type:
        :rtype: :class:`<BuildReportMetadata> <vsts_cli_build.models.BuildReportMetadata>`
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str'),
            'buildId': self._serialize.url('build_id', build_id, 'int')
        }
        query_parameters = {}
        if type is not None:
            query_parameters['type'] = self._serialize.query('type', type, 'str')
        response = self._send(http_method='GET',
                              location_id='45bcaa88-67e1-4042-a035-56d3b4a7d44c',
                              version='4.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('BuildReportMetadata', response)

    def get_build_report_html_content(self, project, build_id, type=None):
        """GetBuildReportHtmlContent.
        [Preview API] Gets report for a vsts_cli_build
        :param str project: Project ID or project name
        :param int build_id:
        :param str type:
        :rtype: object
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str'),
            'buildId': self._serialize.url('build_id', build_id, 'int')
        }
        query_parameters = {}
        if type is not None:
            query_parameters['type'] = self._serialize.query('type', type, 'str')
        response = self._send(http_method='GET',
                              location_id='45bcaa88-67e1-4042-a035-56d3b4a7d44c',
                              version='4.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('object', response)

    def get_resource_usage(self):
        """GetResourceUsage.
        [Preview API]
        :rtype: :class:`<BuildResourceUsage> <vsts_cli_build.models.BuildResourceUsage>`
        """
        response = self._send(http_method='GET',
                              location_id='3813d06c-9e36-4ea1-aac3-61a485d60e3d',
                              version='4.1-preview.2')
        return self._deserialize('BuildResourceUsage', response)

    def get_definition_revisions(self, project, definition_id):
        """GetDefinitionRevisions.
        [Preview API] Gets revisions of a definition
        :param str project: Project ID or project name
        :param int definition_id:
        :rtype: [BuildDefinitionRevision]
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str'),
            'definitionId': self._serialize.url('definition_id', definition_id, 'int')
        }
        response = self._send(http_method='GET',
                              location_id='7c116775-52e5-453e-8c5d-914d9762d8c4',
                              version='4.1-preview.2',
                              route_values=route_values,
                              returns_collection=True)
        return self._deserialize('[BuildDefinitionRevision]', response)

    def get_build_settings(self):
        """GetBuildSettings.
        [Preview API] Gets the vsts_cli_build settings
        :rtype: :class:`<BuildSettings> <vsts_cli_build.models.BuildSettings>`
        """
        response = self._send(http_method='GET',
                              location_id='aa8c1c9c-ef8b-474a-b8c4-785c7b191d0d',
                              version='4.1-preview.1')
        return self._deserialize('BuildSettings', response)

    def update_build_settings(self, settings):
        """UpdateBuildSettings.
        [Preview API] Updates the vsts_cli_build settings
        :param :class:`<BuildSettings> <vsts_cli_build.models.BuildSettings>` settings:
        :rtype: :class:`<BuildSettings> <vsts_cli_build.models.BuildSettings>`
        """
        content = self._serialize.body(settings, 'BuildSettings')
        response = self._send(http_method='PATCH',
                              location_id='aa8c1c9c-ef8b-474a-b8c4-785c7b191d0d',
                              version='4.1-preview.1',
                              content=content)
        return self._deserialize('BuildSettings', response)

    def add_build_tag(self, project, build_id, tag):
        """AddBuildTag.
        [Preview API] Adds a tag to a vsts_cli_build
        :param str project: Project ID or project name
        :param int build_id:
        :param str tag:
        :rtype: [str]
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str'),
            'buildId': self._serialize.url('build_id', build_id, 'int'),
            'tag': self._serialize.url('tag', tag, 'str')
        }
        response = self._send(http_method='PUT',
                              location_id='6e6114b2-8161-44c8-8f6c-c5505782427f',
                              version='4.1-preview.2',
                              route_values=route_values,
                              returns_collection=True)
        return self._deserialize('[str]', response)

    def add_build_tags(self, tags, project, build_id):
        """AddBuildTags.
        [Preview API] Adds tag to a vsts_cli_build
        :param [str] tags:
        :param str project: Project ID or project name
        :param int build_id:
        :rtype: [str]
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str'),
            'buildId': self._serialize.url('build_id', build_id, 'int')
        }
        content = self._serialize.body(tags, '[str]')
        response = self._send(http_method='POST',
                              location_id='6e6114b2-8161-44c8-8f6c-c5505782427f',
                              version='4.1-preview.2',
                              route_values=route_values,
                              content=content,
                              returns_collection=True)
        return self._deserialize('[str]', response)

    def delete_build_tag(self, project, build_id, tag):
        """DeleteBuildTag.
        [Preview API] Deletes a tag from a vsts_cli_build
        :param str project: Project ID or project name
        :param int build_id:
        :param str tag:
        :rtype: [str]
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str'),
            'buildId': self._serialize.url('build_id', build_id, 'int'),
            'tag': self._serialize.url('tag', tag, 'str')
        }
        response = self._send(http_method='DELETE',
                              location_id='6e6114b2-8161-44c8-8f6c-c5505782427f',
                              version='4.1-preview.2',
                              route_values=route_values,
                              returns_collection=True)
        return self._deserialize('[str]', response)

    def get_build_tags(self, project, build_id):
        """GetBuildTags.
        [Preview API] Gets the tags for a vsts_cli_build
        :param str project: Project ID or project name
        :param int build_id:
        :rtype: [str]
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str'),
            'buildId': self._serialize.url('build_id', build_id, 'int')
        }
        response = self._send(http_method='GET',
                              location_id='6e6114b2-8161-44c8-8f6c-c5505782427f',
                              version='4.1-preview.2',
                              route_values=route_values,
                              returns_collection=True)
        return self._deserialize('[str]', response)

    def add_definition_tag(self, project, definition_id, tag):
        """AddDefinitionTag.
        [Preview API] Adds a tag to a definition
        :param str project: Project ID or project name
        :param int definition_id:
        :param str tag:
        :rtype: [str]
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str'),
            'definitionId': self._serialize.url('definition_id', definition_id, 'int'),
            'tag': self._serialize.url('tag', tag, 'str')
        }
        response = self._send(http_method='PUT',
                              location_id='cb894432-134a-4d31-a839-83beceaace4b',
                              version='4.1-preview.2',
                              route_values=route_values,
                              returns_collection=True)
        return self._deserialize('[str]', response)

    def add_definition_tags(self, tags, project, definition_id):
        """AddDefinitionTags.
        [Preview API] Adds multiple tags to a definition
        :param [str] tags:
        :param str project: Project ID or project name
        :param int definition_id:
        :rtype: [str]
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str'),
            'definitionId': self._serialize.url('definition_id', definition_id, 'int')
        }
        content = self._serialize.body(tags, '[str]')
        response = self._send(http_method='POST',
                              location_id='cb894432-134a-4d31-a839-83beceaace4b',
                              version='4.1-preview.2',
                              route_values=route_values,
                              content=content,
                              returns_collection=True)
        return self._deserialize('[str]', response)

    def delete_definition_tag(self, project, definition_id, tag):
        """DeleteDefinitionTag.
        [Preview API] Deletes a tag from a definition
        :param str project: Project ID or project name
        :param int definition_id:
        :param str tag:
        :rtype: [str]
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str'),
            'definitionId': self._serialize.url('definition_id', definition_id, 'int'),
            'tag': self._serialize.url('tag', tag, 'str')
        }
        response = self._send(http_method='DELETE',
                              location_id='cb894432-134a-4d31-a839-83beceaace4b',
                              version='4.1-preview.2',
                              route_values=route_values,
                              returns_collection=True)
        return self._deserialize('[str]', response)

    def get_definition_tags(self, project, definition_id, revision=None):
        """GetDefinitionTags.
        [Preview API] Gets the tags for a definition
        :param str project: Project ID or project name
        :param int definition_id:
        :param int revision:
        :rtype: [str]
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str'),
            'definitionId': self._serialize.url('definition_id', definition_id, 'int')
        }
        query_parameters = {}
        if revision is not None:
            query_parameters['revision'] = self._serialize.query('revision', revision, 'int')
        response = self._send(http_method='GET',
                              location_id='cb894432-134a-4d31-a839-83beceaace4b',
                              version='4.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              returns_collection=True)
        return self._deserialize('[str]', response)

    def get_tags(self, project):
        """GetTags.
        [Preview API] Gets a list of tags in the project
        :param str project: Project ID or project name
        :rtype: [str]
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str')
        }
        response = self._send(http_method='GET',
                              location_id='d84ac5c6-edc7-43d5-adc9-1b34be5dea09',
                              version='4.1-preview.2',
                              route_values=route_values,
                              returns_collection=True)
        return self._deserialize('[str]', response)

    def delete_template(self, project, template_id):
        """DeleteTemplate.
        [Preview API] Deletes a definition template
        :param str project: Project ID or project name
        :param str template_id:
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str'),
            'templateId': self._serialize.url('template_id', template_id, 'str')
        }
        self._send(http_method='DELETE',
                   location_id='e884571e-7f92-4d6a-9274-3f5649900835',
                   version='4.1-preview.3',
                   route_values=route_values)

    def get_template(self, project, template_id):
        """GetTemplate.
        [Preview API] Gets definition template filtered by id
        :param str project: Project ID or project name
        :param str template_id: Id of the requested template.
        :rtype: :class:`<BuildDefinitionTemplate> <vsts_cli_build.models.BuildDefinitionTemplate>`
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str'),
            'templateId': self._serialize.url('template_id', template_id, 'str')
        }
        response = self._send(http_method='GET',
                              location_id='e884571e-7f92-4d6a-9274-3f5649900835',
                              version='4.1-preview.3',
                              route_values=route_values)
        return self._deserialize('BuildDefinitionTemplate', response)

    def get_templates(self, project):
        """GetTemplates.
        [Preview API] Gets definition templates
        :param str project: Project ID or project name
        :rtype: [BuildDefinitionTemplate]
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str')
        }
        response = self._send(http_method='GET',
                              location_id='e884571e-7f92-4d6a-9274-3f5649900835',
                              version='4.1-preview.3',
                              route_values=route_values,
                              returns_collection=True)
        return self._deserialize('[BuildDefinitionTemplate]', response)

    def save_template(self, template, project, template_id):
        """SaveTemplate.
        [Preview API] Saves a definition template
        :param :class:`<BuildDefinitionTemplate> <vsts_cli_build.models.BuildDefinitionTemplate>` template:
        :param str project: Project ID or project name
        :param str template_id:
        :rtype: :class:`<BuildDefinitionTemplate> <vsts_cli_build.models.BuildDefinitionTemplate>`
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str'),
            'templateId': self._serialize.url('template_id', template_id, 'str')
        }
        content = self._serialize.body(template, 'BuildDefinitionTemplate')
        response = self._send(http_method='PUT',
                              location_id='e884571e-7f92-4d6a-9274-3f5649900835',
                              version='4.1-preview.3',
                              route_values=route_values,
                              content=content)
        return self._deserialize('BuildDefinitionTemplate', response)

    def get_build_timeline(self, project, build_id, timeline_id=None, change_id=None, plan_id=None):
        """GetBuildTimeline.
        [Preview API] Gets details for a vsts_cli_build
        :param str project: Project ID or project name
        :param int build_id:
        :param str timeline_id:
        :param int change_id:
        :param str plan_id:
        :rtype: :class:`<Timeline> <vsts_cli_build.models.Timeline>`
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str'),
            'buildId': self._serialize.url('build_id', build_id, 'int'),
            'timelineId': self._serialize.url('timeline_id', timeline_id, 'str')
        }
        query_parameters = {}
        if change_id is not None:
            query_parameters['changeId'] = self._serialize.query('change_id', change_id, 'int')
        if plan_id is not None:
            query_parameters['planId'] = self._serialize.query('plan_id', plan_id, 'str')
        response = self._send(http_method='GET',
                              location_id='8baac422-4c6e-4de5-8532-db96d92acffa',
                              version='4.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('Timeline', response)

    def get_build_work_items_refs(self, project, build_id, top=None):
        """GetBuildWorkItemsRefs.
        [Preview API] Gets the work item ids associated with a vsts_cli_build
        :param str project: Project ID or project name
        :param int build_id:
        :param int top: The maximum number of workitems to return
        :rtype: [ResourceRef]
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str'),
            'buildId': self._serialize.url('build_id', build_id, 'int')
        }
        query_parameters = {}
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        response = self._send(http_method='GET',
                              location_id='5a21f5d2-5642-47e4-a0bd-1356e6731bee',
                              version='4.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              returns_collection=True)
        return self._deserialize('[ResourceRef]', response)

    def get_build_work_items_refs_from_commits(self, commit_ids, project, build_id, top=None):
        """GetBuildWorkItemsRefsFromCommits.
        [Preview API] Gets the work item ids associated with vsts_cli_build commits
        :param [str] commit_ids:
        :param str project: Project ID or project name
        :param int build_id:
        :param int top: The maximum number of workitems to return, also number of commits to consider if commitids are not sent
        :rtype: [ResourceRef]
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str'),
            'buildId': self._serialize.url('build_id', build_id, 'int')
        }
        query_parameters = {}
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        content = self._serialize.body(commit_ids, '[str]')
        response = self._send(http_method='POST',
                              location_id='5a21f5d2-5642-47e4-a0bd-1356e6731bee',
                              version='4.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content,
                              returns_collection=True)
        return self._deserialize('[ResourceRef]', response)

    def get_work_items_between_builds(self, project, from_build_id, to_build_id, top=None):
        """GetWorkItemsBetweenBuilds.
        [Preview API] Gets all the work item ids inbetween fromBuildId to toBuildId
        :param str project: Project ID or project name
        :param int from_build_id:
        :param int to_build_id:
        :param int top: The maximum number of workitems to return
        :rtype: [ResourceRef]
        """
        route_values = {
            'project': self._serialize.url('project', project, 'str')
        }
        query_parameters = {}
        if from_build_id is not None:
            query_parameters['fromBuildId'] = self._serialize.query('from_build_id', from_build_id, 'int')
        if to_build_id is not None:
            query_parameters['toBuildId'] = self._serialize.query('to_build_id', to_build_id, 'int')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        response = self._send(http_method='GET',
                              location_id='52ba8915-5518-42e3-a4bb-b0182d159e2d',
                              version='4.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              returns_collection=True)
        return self._deserialize('[ResourceRef]', response)

