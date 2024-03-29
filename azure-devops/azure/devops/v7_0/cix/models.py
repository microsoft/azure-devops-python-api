﻿# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class ConfigurationFile(Model):
    """
    :param content: The content of the file.
    :type content: str
    :param is_base64_encoded: Indicates if the content is base64 encoded.
    :type is_base64_encoded: bool
    :param path: The full path of the file, relative to the root of the repository.
    :type path: str
    """

    _attribute_map = {
        'content': {'key': 'content', 'type': 'str'},
        'is_base64_encoded': {'key': 'isBase64Encoded', 'type': 'bool'},
        'path': {'key': 'path', 'type': 'str'}
    }

    def __init__(self, content=None, is_base64_encoded=None, path=None):
        super(ConfigurationFile, self).__init__()
        self.content = content
        self.is_base64_encoded = is_base64_encoded
        self.path = path


class CreatedResources(Model):
    """
    :param resources:
    :type resources: dict
    """

    _attribute_map = {
        'resources': {'key': 'resources', 'type': '{object}'}
    }

    def __init__(self, resources=None):
        super(CreatedResources, self).__init__()
        self.resources = resources


class CreatePipelineConnectionInputs(Model):
    """
    This class is used to create a pipeline connection within the team project provided. If the team project does not exist, it will be created.

    :param project: The team project settings for an existing team project or for a new team project.
    :type project: :class:`TeamProject <azure.devops.v7_0.pipelines.models.TeamProject>`
    :param provider_data: This dictionary contains information that is specific to the provider. This data is opaque to the rest of the Pipelines infrastructure and does NOT contribute to the resources Token. The format of the string and its contents depend on the implementation of the provider.
    :type provider_data: dict
    :param provider_id: The external source provider id for which the connection is being made.
    :type provider_id: str
    :param redirect_url: If provided, this will be the URL returned with the PipelineConnection. This will override any other redirect URL that would have been generated for the connection.
    :type redirect_url: str
    :param request_source: Where the request to create the pipeline originated (such as 'GitHub Marketplace' or 'Azure DevOps')
    :type request_source: str
    """

    _attribute_map = {
        'project': {'key': 'project', 'type': 'TeamProject'},
        'provider_data': {'key': 'providerData', 'type': '{str}'},
        'provider_id': {'key': 'providerId', 'type': 'str'},
        'redirect_url': {'key': 'redirectUrl', 'type': 'str'},
        'request_source': {'key': 'requestSource', 'type': 'str'}
    }

    def __init__(self, project=None, provider_data=None, provider_id=None, redirect_url=None, request_source=None):
        super(CreatePipelineConnectionInputs, self).__init__()
        self.project = project
        self.provider_data = provider_data
        self.provider_id = provider_id
        self.redirect_url = redirect_url
        self.request_source = request_source


class DetectedBuildFramework(Model):
    """
    :param build_targets: List of build targets discovered for the framework to act upon.
    :type build_targets: list of :class:`DetectedBuildTarget <azure.devops.v7_0.pipelines.models.DetectedBuildTarget>`
    :param id: The unique identifier of the build framework.
    :type id: str
    :param settings: Additional detected settings for the build framework.
    :type settings: dict
    :param version: The version of the framework if it can be determined from the sources.
    :type version: str
    """

    _attribute_map = {
        'build_targets': {'key': 'buildTargets', 'type': '[DetectedBuildTarget]'},
        'id': {'key': 'id', 'type': 'str'},
        'settings': {'key': 'settings', 'type': '{str}'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, build_targets=None, id=None, settings=None, version=None):
        super(DetectedBuildFramework, self).__init__()
        self.build_targets = build_targets
        self.id = id
        self.settings = settings
        self.version = version


class DetectedBuildTarget(Model):
    """
    :param path:
    :type path: str
    :param settings:
    :type settings: dict
    :param type:
    :type type: str
    """

    _attribute_map = {
        'path': {'key': 'path', 'type': 'str'},
        'settings': {'key': 'settings', 'type': '{str}'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, path=None, settings=None, type=None):
        super(DetectedBuildTarget, self).__init__()
        self.path = path
        self.settings = settings
        self.type = type


class OperationReference(Model):
    """
    Reference for an async operation.

    :param id: Unique identifier for the operation.
    :type id: str
    :param plugin_id: Unique identifier for the plugin.
    :type plugin_id: str
    :param status: The current status of the operation.
    :type status: object
    :param url: URL to get the full operation object.
    :type url: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'plugin_id': {'key': 'pluginId', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, plugin_id=None, status=None, url=None):
        super(OperationReference, self).__init__()
        self.id = id
        self.plugin_id = plugin_id
        self.status = status
        self.url = url


class OperationResultReference(Model):
    """
    :param result_url: URL to the operation result.
    :type result_url: str
    """

    _attribute_map = {
        'result_url': {'key': 'resultUrl', 'type': 'str'}
    }

    def __init__(self, result_url=None):
        super(OperationResultReference, self).__init__()
        self.result_url = result_url


class PipelineConnection(Model):
    """
    :param account_id: The account id that contains the team project for the connection.
    :type account_id: str
    :param definition_id: The definition id that was created for the connection.
    :type definition_id: int
    :param redirect_url: This is the URL that the user should be taken to in order to continue setup.
    :type redirect_url: str
    :param service_endpoint_id: The service endpoint that was created for the connection.
    :type service_endpoint_id: str
    :param team_project_id: The team project that contains the definition for the connection.
    :type team_project_id: str
    """

    _attribute_map = {
        'account_id': {'key': 'accountId', 'type': 'str'},
        'definition_id': {'key': 'definitionId', 'type': 'int'},
        'redirect_url': {'key': 'redirectUrl', 'type': 'str'},
        'service_endpoint_id': {'key': 'serviceEndpointId', 'type': 'str'},
        'team_project_id': {'key': 'teamProjectId', 'type': 'str'}
    }

    def __init__(self, account_id=None, definition_id=None, redirect_url=None, service_endpoint_id=None, team_project_id=None):
        super(PipelineConnection, self).__init__()
        self.account_id = account_id
        self.definition_id = definition_id
        self.redirect_url = redirect_url
        self.service_endpoint_id = service_endpoint_id
        self.team_project_id = team_project_id


class ReferenceLinks(Model):
    """
    The class to represent a collection of REST reference links.

    :param links: The readonly view of the links.  Because Reference links are readonly, we only want to expose them as read only.
    :type links: dict
    """

    _attribute_map = {
        'links': {'key': 'links', 'type': '{object}'}
    }

    def __init__(self, links=None):
        super(ReferenceLinks, self).__init__()
        self.links = links


class ResourceCreationParameter(Model):
    """
    :param resource_to_create:
    :type resource_to_create: :class:`object <azure.devops.v7_0.pipelines.models.object>`
    :param type:
    :type type: str
    """

    _attribute_map = {
        'resource_to_create': {'key': 'resourceToCreate', 'type': 'object'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, resource_to_create=None, type=None):
        super(ResourceCreationParameter, self).__init__()
        self.resource_to_create = resource_to_create
        self.type = type


class TeamProjectReference(Model):
    """
    Represents a shallow reference to a TeamProject.

    :param abbreviation: Project abbreviation.
    :type abbreviation: str
    :param default_team_image_url: Url to default team identity image.
    :type default_team_image_url: str
    :param description: The project's description (if any).
    :type description: str
    :param id: Project identifier.
    :type id: str
    :param last_update_time: Project last update time.
    :type last_update_time: datetime
    :param name: Project name.
    :type name: str
    :param revision: Project revision.
    :type revision: long
    :param state: Project state.
    :type state: object
    :param url: Url to the full version of the object.
    :type url: str
    :param visibility: Project visibility.
    :type visibility: object
    """

    _attribute_map = {
        'abbreviation': {'key': 'abbreviation', 'type': 'str'},
        'default_team_image_url': {'key': 'defaultTeamImageUrl', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'last_update_time': {'key': 'lastUpdateTime', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'revision': {'key': 'revision', 'type': 'long'},
        'state': {'key': 'state', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'},
        'visibility': {'key': 'visibility', 'type': 'object'}
    }

    def __init__(self, abbreviation=None, default_team_image_url=None, description=None, id=None, last_update_time=None, name=None, revision=None, state=None, url=None, visibility=None):
        super(TeamProjectReference, self).__init__()
        self.abbreviation = abbreviation
        self.default_team_image_url = default_team_image_url
        self.description = description
        self.id = id
        self.last_update_time = last_update_time
        self.name = name
        self.revision = revision
        self.state = state
        self.url = url
        self.visibility = visibility


class WebApiTeamRef(Model):
    """
    :param id: Team (Identity) Guid. A Team Foundation ID.
    :type id: str
    :param name: Team name
    :type name: str
    :param url: Team REST API Url
    :type url: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, name=None, url=None):
        super(WebApiTeamRef, self).__init__()
        self.id = id
        self.name = name
        self.url = url


class Operation(OperationReference):
    """
    Contains information about the progress or result of an async operation.

    :param id: Unique identifier for the operation.
    :type id: str
    :param plugin_id: Unique identifier for the plugin.
    :type plugin_id: str
    :param status: The current status of the operation.
    :type status: object
    :param url: URL to get the full operation object.
    :type url: str
    :param _links: Links to other related objects.
    :type _links: :class:`ReferenceLinks <azure.devops.v7_0.microsoft._visual_studio._services._web_api.models.ReferenceLinks>`
    :param detailed_message: Detailed messaged about the status of an operation.
    :type detailed_message: str
    :param result_message: Result message for an operation.
    :type result_message: str
    :param result_url: URL to the operation result.
    :type result_url: :class:`OperationResultReference <azure.devops.v7_0.microsoft._visual_studio._services._web_api.models.OperationResultReference>`
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'plugin_id': {'key': 'pluginId', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'detailed_message': {'key': 'detailedMessage', 'type': 'str'},
        'result_message': {'key': 'resultMessage', 'type': 'str'},
        'result_url': {'key': 'resultUrl', 'type': 'OperationResultReference'}
    }

    def __init__(self, id=None, plugin_id=None, status=None, url=None, _links=None, detailed_message=None, result_message=None, result_url=None):
        super(Operation, self).__init__(id=id, plugin_id=plugin_id, status=status, url=url)
        self._links = _links
        self.detailed_message = detailed_message
        self.result_message = result_message
        self.result_url = result_url


class TeamProject(TeamProjectReference):
    """
    Represents a Team Project object.

    :param abbreviation: Project abbreviation.
    :type abbreviation: str
    :param default_team_image_url: Url to default team identity image.
    :type default_team_image_url: str
    :param description: The project's description (if any).
    :type description: str
    :param id: Project identifier.
    :type id: str
    :param last_update_time: Project last update time.
    :type last_update_time: datetime
    :param name: Project name.
    :type name: str
    :param revision: Project revision.
    :type revision: long
    :param state: Project state.
    :type state: object
    :param url: Url to the full version of the object.
    :type url: str
    :param visibility: Project visibility.
    :type visibility: object
    :param _links: The links to other objects related to this object.
    :type _links: :class:`ReferenceLinks <azure.devops.v7_0.microsoft._team_foundation._core._web_api.models.ReferenceLinks>`
    :param capabilities: Set of capabilities this project has (such as process template & version control).
    :type capabilities: dict
    :param default_team: The shallow ref to the default team.
    :type default_team: :class:`WebApiTeamRef <azure.devops.v7_0.microsoft._team_foundation._core._web_api.models.WebApiTeamRef>`
    """

    _attribute_map = {
        'abbreviation': {'key': 'abbreviation', 'type': 'str'},
        'default_team_image_url': {'key': 'defaultTeamImageUrl', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'last_update_time': {'key': 'lastUpdateTime', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'revision': {'key': 'revision', 'type': 'long'},
        'state': {'key': 'state', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'},
        'visibility': {'key': 'visibility', 'type': 'object'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'capabilities': {'key': 'capabilities', 'type': '{{str}}'},
        'default_team': {'key': 'defaultTeam', 'type': 'WebApiTeamRef'}
    }

    def __init__(self, abbreviation=None, default_team_image_url=None, description=None, id=None, last_update_time=None, name=None, revision=None, state=None, url=None, visibility=None, _links=None, capabilities=None, default_team=None):
        super(TeamProject, self).__init__(abbreviation=abbreviation, default_team_image_url=default_team_image_url, description=description, id=id, last_update_time=last_update_time, name=name, revision=revision, state=state, url=url, visibility=visibility)
        self._links = _links
        self.capabilities = capabilities
        self.default_team = default_team


__all__ = [
    'ConfigurationFile',
    'CreatedResources',
    'CreatePipelineConnectionInputs',
    'DetectedBuildFramework',
    'DetectedBuildTarget',
    'OperationReference',
    'OperationResultReference',
    'PipelineConnection',
    'ReferenceLinks',
    'ResourceCreationParameter',
    'TeamProjectReference',
    'WebApiTeamRef',
    'Operation',
    'TeamProject',
]
