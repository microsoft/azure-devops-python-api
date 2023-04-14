# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class Artifact(Model):
    """
    Artifacts are collections of files produced by a pipeline. Use artifacts to share files between stages in a pipeline or between different pipelines.

    :param name: The name of the artifact.
    :type name: str
    :param signed_content: Signed url for downloading this artifact
    :type signed_content: :class:`SignedUrl <azure.devops.v7_1.pipelines.models.SignedUrl>`
    :param url: Self-referential url
    :type url: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'signed_content': {'key': 'signedContent', 'type': 'SignedUrl'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, name=None, signed_content=None, url=None):
        super(Artifact, self).__init__()
        self.name = name
        self.signed_content = signed_content
        self.url = url


class BuildResourceParameters(Model):
    """
    :param version:
    :type version: str
    """

    _attribute_map = {
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, version=None):
        super(BuildResourceParameters, self).__init__()
        self.version = version


class Container(Model):
    """
    :param environment:
    :type environment: dict
    :param image:
    :type image: str
    :param map_docker_socket:
    :type map_docker_socket: bool
    :param options:
    :type options: str
    :param ports:
    :type ports: list of str
    :param volumes:
    :type volumes: list of str
    """

    _attribute_map = {
        'environment': {'key': 'environment', 'type': '{str}'},
        'image': {'key': 'image', 'type': 'str'},
        'map_docker_socket': {'key': 'mapDockerSocket', 'type': 'bool'},
        'options': {'key': 'options', 'type': 'str'},
        'ports': {'key': 'ports', 'type': '[str]'},
        'volumes': {'key': 'volumes', 'type': '[str]'}
    }

    def __init__(self, environment=None, image=None, map_docker_socket=None, options=None, ports=None, volumes=None):
        super(Container, self).__init__()
        self.environment = environment
        self.image = image
        self.map_docker_socket = map_docker_socket
        self.options = options
        self.ports = ports
        self.volumes = volumes


class ContainerResource(Model):
    """
    :param container:
    :type container: :class:`Container <azure.devops.v7_1.pipelines.models.Container>`
    """

    _attribute_map = {
        'container': {'key': 'container', 'type': 'Container'}
    }

    def __init__(self, container=None):
        super(ContainerResource, self).__init__()
        self.container = container


class ContainerResourceParameters(Model):
    """
    :param version:
    :type version: str
    """

    _attribute_map = {
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, version=None):
        super(ContainerResourceParameters, self).__init__()
        self.version = version


class CreatePipelineConfigurationParameters(Model):
    """
    Configuration parameters of the pipeline.

    :param type: Type of configuration.
    :type type: object
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, type=None):
        super(CreatePipelineConfigurationParameters, self).__init__()
        self.type = type


class CreatePipelineParameters(Model):
    """
    Parameters to create a pipeline.

    :param configuration: Configuration parameters of the pipeline.
    :type configuration: :class:`CreatePipelineConfigurationParameters <azure.devops.v7_1.pipelines.models.CreatePipelineConfigurationParameters>`
    :param folder: Folder of the pipeline.
    :type folder: str
    :param name: Name of the pipeline.
    :type name: str
    """

    _attribute_map = {
        'configuration': {'key': 'configuration', 'type': 'CreatePipelineConfigurationParameters'},
        'folder': {'key': 'folder', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, configuration=None, folder=None, name=None):
        super(CreatePipelineParameters, self).__init__()
        self.configuration = configuration
        self.folder = folder
        self.name = name


class Log(Model):
    """
    Log for a pipeline.

    :param created_on: The date and time the log was created.
    :type created_on: datetime
    :param id: The ID of the log.
    :type id: int
    :param last_changed_on: The date and time the log was last changed.
    :type last_changed_on: datetime
    :param line_count: The number of lines in the log.
    :type line_count: long
    :param signed_content:
    :type signed_content: :class:`SignedUrl <azure.devops.v7_1.pipelines.models.SignedUrl>`
    :param url:
    :type url: str
    """

    _attribute_map = {
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'int'},
        'last_changed_on': {'key': 'lastChangedOn', 'type': 'iso-8601'},
        'line_count': {'key': 'lineCount', 'type': 'long'},
        'signed_content': {'key': 'signedContent', 'type': 'SignedUrl'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, created_on=None, id=None, last_changed_on=None, line_count=None, signed_content=None, url=None):
        super(Log, self).__init__()
        self.created_on = created_on
        self.id = id
        self.last_changed_on = last_changed_on
        self.line_count = line_count
        self.signed_content = signed_content
        self.url = url


class LogCollection(Model):
    """
    A collection of logs.

    :param logs: The list of logs.
    :type logs: list of :class:`Log <azure.devops.v7_1.pipelines.models.Log>`
    :param signed_content:
    :type signed_content: :class:`SignedUrl <azure.devops.v7_1.pipelines.models.SignedUrl>`
    :param url: URL of the log.
    :type url: str
    """

    _attribute_map = {
        'logs': {'key': 'logs', 'type': '[Log]'},
        'signed_content': {'key': 'signedContent', 'type': 'SignedUrl'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, logs=None, signed_content=None, url=None):
        super(LogCollection, self).__init__()
        self.logs = logs
        self.signed_content = signed_content
        self.url = url


class PackageResourceParameters(Model):
    """
    :param version:
    :type version: str
    """

    _attribute_map = {
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, version=None):
        super(PackageResourceParameters, self).__init__()
        self.version = version


class PipelineBase(Model):
    """
    :param folder: Pipeline folder
    :type folder: str
    :param id: Pipeline ID
    :type id: int
    :param name: Pipeline name
    :type name: str
    :param revision: Revision number
    :type revision: int
    """

    _attribute_map = {
        'folder': {'key': 'folder', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'revision': {'key': 'revision', 'type': 'int'}
    }

    def __init__(self, folder=None, id=None, name=None, revision=None):
        super(PipelineBase, self).__init__()
        self.folder = folder
        self.id = id
        self.name = name
        self.revision = revision


class PipelineConfiguration(Model):
    """
    :param type:
    :type type: object
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, type=None):
        super(PipelineConfiguration, self).__init__()
        self.type = type


class PipelineReference(PipelineBase):
    """
    A reference to a Pipeline.

    :param folder: Pipeline folder
    :type folder: str
    :param id: Pipeline ID
    :type id: int
    :param name: Pipeline name
    :type name: str
    :param revision: Revision number
    :type revision: int
    :param url:
    :type url: str
    """

    _attribute_map = {
        'folder': {'key': 'folder', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'revision': {'key': 'revision', 'type': 'int'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, folder=None, id=None, name=None, revision=None, url=None):
        super(PipelineReference, self).__init__(folder=folder, id=id, name=name, revision=revision)
        self.url = url


class PipelineResource(Model):
    """
    :param pipeline:
    :type pipeline: :class:`PipelineReference <azure.devops.v7_1.pipelines.models.PipelineReference>`
    :param version:
    :type version: str
    """

    _attribute_map = {
        'pipeline': {'key': 'pipeline', 'type': 'PipelineReference'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, pipeline=None, version=None):
        super(PipelineResource, self).__init__()
        self.pipeline = pipeline
        self.version = version


class PipelineResourceParameters(Model):
    """
    :param version:
    :type version: str
    """

    _attribute_map = {
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, version=None):
        super(PipelineResourceParameters, self).__init__()
        self.version = version


class PreviewRun(Model):
    """
    :param final_yaml:
    :type final_yaml: str
    """

    _attribute_map = {
        'final_yaml': {'key': 'finalYaml', 'type': 'str'}
    }

    def __init__(self, final_yaml=None):
        super(PreviewRun, self).__init__()
        self.final_yaml = final_yaml


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


class Repository(Model):
    """
    :param type:
    :type type: object
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, type=None):
        super(Repository, self).__init__()
        self.type = type


class RepositoryResource(Model):
    """
    :param ref_name:
    :type ref_name: str
    :param repository:
    :type repository: :class:`Repository <azure.devops.v7_1.pipelines.models.Repository>`
    :param version:
    :type version: str
    """

    _attribute_map = {
        'ref_name': {'key': 'refName', 'type': 'str'},
        'repository': {'key': 'repository', 'type': 'Repository'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, ref_name=None, repository=None, version=None):
        super(RepositoryResource, self).__init__()
        self.ref_name = ref_name
        self.repository = repository
        self.version = version


class RepositoryResourceParameters(Model):
    """
    :param ref_name:
    :type ref_name: str
    :param token: This is the security token to use when connecting to the repository.
    :type token: str
    :param token_type: Optional. This is the type of the token given. If not provided, a type of "Bearer" is assumed. Note: Use "Basic" for a PAT token.
    :type token_type: str
    :param version:
    :type version: str
    """

    _attribute_map = {
        'ref_name': {'key': 'refName', 'type': 'str'},
        'token': {'key': 'token', 'type': 'str'},
        'token_type': {'key': 'tokenType', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, ref_name=None, token=None, token_type=None, version=None):
        super(RepositoryResourceParameters, self).__init__()
        self.ref_name = ref_name
        self.token = token
        self.token_type = token_type
        self.version = version


class RunPipelineParameters(Model):
    """
    Settings which influence pipeline runs.

    :param preview_run: If true, don't actually create a new run. Instead, return the final YAML document after parsing templates.
    :type preview_run: bool
    :param resources: The resources the run requires.
    :type resources: :class:`RunResourcesParameters <azure.devops.v7_1.pipelines.models.RunResourcesParameters>`
    :param stages_to_skip:
    :type stages_to_skip: list of str
    :param template_parameters:
    :type template_parameters: dict
    :param variables:
    :type variables: dict
    :param yaml_override: If you use the preview run option, you may optionally supply different YAML. This allows you to preview the final YAML document without committing a changed file.
    :type yaml_override: str
    """

    _attribute_map = {
        'preview_run': {'key': 'previewRun', 'type': 'bool'},
        'resources': {'key': 'resources', 'type': 'RunResourcesParameters'},
        'stages_to_skip': {'key': 'stagesToSkip', 'type': '[str]'},
        'template_parameters': {'key': 'templateParameters', 'type': '{str}'},
        'variables': {'key': 'variables', 'type': '{Variable}'},
        'yaml_override': {'key': 'yamlOverride', 'type': 'str'}
    }

    def __init__(self, preview_run=None, resources=None, stages_to_skip=None, template_parameters=None, variables=None, yaml_override=None):
        super(RunPipelineParameters, self).__init__()
        self.preview_run = preview_run
        self.resources = resources
        self.stages_to_skip = stages_to_skip
        self.template_parameters = template_parameters
        self.variables = variables
        self.yaml_override = yaml_override


class RunReference(Model):
    """
    :param id:
    :type id: int
    :param name:
    :type name: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, id=None, name=None):
        super(RunReference, self).__init__()
        self.id = id
        self.name = name


class RunResources(Model):
    """
    :param containers:
    :type containers: dict
    :param pipelines:
    :type pipelines: dict
    :param repositories:
    :type repositories: dict
    """

    _attribute_map = {
        'containers': {'key': 'containers', 'type': '{ContainerResource}'},
        'pipelines': {'key': 'pipelines', 'type': '{PipelineResource}'},
        'repositories': {'key': 'repositories', 'type': '{RepositoryResource}'}
    }

    def __init__(self, containers=None, pipelines=None, repositories=None):
        super(RunResources, self).__init__()
        self.containers = containers
        self.pipelines = pipelines
        self.repositories = repositories


class RunResourcesParameters(Model):
    """
    :param builds:
    :type builds: dict
    :param containers:
    :type containers: dict
    :param packages:
    :type packages: dict
    :param pipelines:
    :type pipelines: dict
    :param repositories:
    :type repositories: dict
    """

    _attribute_map = {
        'builds': {'key': 'builds', 'type': '{BuildResourceParameters}'},
        'containers': {'key': 'containers', 'type': '{ContainerResourceParameters}'},
        'packages': {'key': 'packages', 'type': '{PackageResourceParameters}'},
        'pipelines': {'key': 'pipelines', 'type': '{PipelineResourceParameters}'},
        'repositories': {'key': 'repositories', 'type': '{RepositoryResourceParameters}'}
    }

    def __init__(self, builds=None, containers=None, packages=None, pipelines=None, repositories=None):
        super(RunResourcesParameters, self).__init__()
        self.builds = builds
        self.containers = containers
        self.packages = packages
        self.pipelines = pipelines
        self.repositories = repositories


class SignalRConnection(Model):
    """
    :param signed_content:
    :type signed_content: :class:`SignedUrl <azure.devops.v7_1.pipelines.models.SignedUrl>`
    """

    _attribute_map = {
        'signed_content': {'key': 'signedContent', 'type': 'SignedUrl'}
    }

    def __init__(self, signed_content=None):
        super(SignalRConnection, self).__init__()
        self.signed_content = signed_content


class SignedUrl(Model):
    """
    A signed url allowing limited-time anonymous access to private resources.

    :param signature_expires: Timestamp when access expires.
    :type signature_expires: datetime
    :param url: The URL to allow access to.
    :type url: str
    """

    _attribute_map = {
        'signature_expires': {'key': 'signatureExpires', 'type': 'iso-8601'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, signature_expires=None, url=None):
        super(SignedUrl, self).__init__()
        self.signature_expires = signature_expires
        self.url = url


class Variable(Model):
    """
    :param is_secret:
    :type is_secret: bool
    :param value:
    :type value: str
    """

    _attribute_map = {
        'is_secret': {'key': 'isSecret', 'type': 'bool'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, is_secret=None, value=None):
        super(Variable, self).__init__()
        self.is_secret = is_secret
        self.value = value


class Pipeline(PipelineBase):
    """
    Definition of a pipeline.

    :param folder: Pipeline folder
    :type folder: str
    :param id: Pipeline ID
    :type id: int
    :param name: Pipeline name
    :type name: str
    :param revision: Revision number
    :type revision: int
    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v7_1.pipelines.models.ReferenceLinks>`
    :param configuration:
    :type configuration: :class:`PipelineConfiguration <azure.devops.v7_1.pipelines.models.PipelineConfiguration>`
    :param url: URL of the pipeline
    :type url: str
    """

    _attribute_map = {
        'folder': {'key': 'folder', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'revision': {'key': 'revision', 'type': 'int'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'configuration': {'key': 'configuration', 'type': 'PipelineConfiguration'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, folder=None, id=None, name=None, revision=None, _links=None, configuration=None, url=None):
        super(Pipeline, self).__init__(folder=folder, id=id, name=name, revision=revision)
        self._links = _links
        self.configuration = configuration
        self.url = url


class Run(RunReference):
    """
    :param id:
    :type id: int
    :param name:
    :type name: str
    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v7_1.pipelines.models.ReferenceLinks>`
    :param created_date:
    :type created_date: datetime
    :param final_yaml:
    :type final_yaml: str
    :param finished_date:
    :type finished_date: datetime
    :param pipeline:
    :type pipeline: :class:`PipelineReference <azure.devops.v7_1.pipelines.models.PipelineReference>`
    :param resources:
    :type resources: :class:`RunResources <azure.devops.v7_1.pipelines.models.RunResources>`
    :param result:
    :type result: object
    :param state:
    :type state: object
    :param template_parameters:
    :type template_parameters: dict
    :param url:
    :type url: str
    :param variables:
    :type variables: dict
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'final_yaml': {'key': 'finalYaml', 'type': 'str'},
        'finished_date': {'key': 'finishedDate', 'type': 'iso-8601'},
        'pipeline': {'key': 'pipeline', 'type': 'PipelineReference'},
        'resources': {'key': 'resources', 'type': 'RunResources'},
        'result': {'key': 'result', 'type': 'object'},
        'state': {'key': 'state', 'type': 'object'},
        'template_parameters': {'key': 'templateParameters', 'type': '{object}'},
        'url': {'key': 'url', 'type': 'str'},
        'variables': {'key': 'variables', 'type': '{Variable}'}
    }

    def __init__(self, id=None, name=None, _links=None, created_date=None, final_yaml=None, finished_date=None, pipeline=None, resources=None, result=None, state=None, template_parameters=None, url=None, variables=None):
        super(Run, self).__init__(id=id, name=name)
        self._links = _links
        self.created_date = created_date
        self.final_yaml = final_yaml
        self.finished_date = finished_date
        self.pipeline = pipeline
        self.resources = resources
        self.result = result
        self.state = state
        self.template_parameters = template_parameters
        self.url = url
        self.variables = variables


__all__ = [
    'Artifact',
    'BuildResourceParameters',
    'Container',
    'ContainerResource',
    'ContainerResourceParameters',
    'CreatePipelineConfigurationParameters',
    'CreatePipelineParameters',
    'Log',
    'LogCollection',
    'PackageResourceParameters',
    'PipelineBase',
    'PipelineConfiguration',
    'PipelineReference',
    'PipelineResource',
    'PipelineResourceParameters',
    'PreviewRun',
    'ReferenceLinks',
    'Repository',
    'RepositoryResource',
    'RepositoryResourceParameters',
    'RunPipelineParameters',
    'RunReference',
    'RunResources',
    'RunResourcesParameters',
    'SignalRConnection',
    'SignedUrl',
    'Variable',
    'Pipeline',
    'Run',
]
