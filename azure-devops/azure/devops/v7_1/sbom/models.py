# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class Configuration(Model):
    """
    This holds the configuration for the ManifestTool. The values in this file are populated from the command line, config file and default.

    :param additional_component_detector_args: Additional set of command-line arguments for Component Detector.
    :type additional_component_detector_args: :class:`ConfigurationSetting <azure.devops.v7_1.sbom.models.ConfigurationSetting>`
    :param build_component_path: The folder containing the build components and packages.
    :type build_component_path: :class:`ConfigurationSetting <azure.devops.v7_1.sbom.models.ConfigurationSetting>`
    :param build_drop_path: The root folder of the drop directory to validate or generate.
    :type build_drop_path: :class:`ConfigurationSetting <azure.devops.v7_1.sbom.models.ConfigurationSetting>`
    :param build_list_file: Full file name of a list file that contains all files to be validated.
    :type build_list_file: :class:`ConfigurationSetting <azure.devops.v7_1.sbom.models.ConfigurationSetting>`
    :param catalog_file_path: The path of the signed catalog file used to validate the manifest.json.
    :type catalog_file_path: :class:`ConfigurationSetting <azure.devops.v7_1.sbom.models.ConfigurationSetting>`
    :param config_file_path: The json file that contains the configuration for the DropValidator.
    :type config_file_path: :class:`ConfigurationSetting <azure.devops.v7_1.sbom.models.ConfigurationSetting>`
    :param docker_images_to_scan: Comma separated list of docker image names or hashes to be scanned for packages, ex: ubuntu:16.04, 56bab49eef2ef07505f6a1b0d5bd3a601dfc3c76ad4460f24c91d6fa298369ab.
    :type docker_images_to_scan: :class:`ConfigurationSetting <azure.devops.v7_1.sbom.models.ConfigurationSetting>`
    :param external_document_reference_list_file: Full file path to a file that contains list of external SBOMs to be included as External document reference.
    :type external_document_reference_list_file: :class:`ConfigurationSetting <azure.devops.v7_1.sbom.models.ConfigurationSetting>`
    :param hash_algorithm: The Hash algorithm to use while verifying the hash value of a file.
    :type hash_algorithm: :class:`ConfigurationSetting <azure.devops.v7_1.sbom.models.ConfigurationSetting>`
    :param ignore_missing: If set, will not fail validation on the files presented in Manifest but missing on the disk.
    :type ignore_missing: :class:`ConfigurationSetting <azure.devops.v7_1.sbom.models.ConfigurationSetting>`
    :param manifest_dir_path: The root folder where the generated manifest (and other files like bsi.json) files will be placed. By default we will generate this folder in the same level as the build drop with the name '_manifest'
    :type manifest_dir_path: :class:`ConfigurationSetting <azure.devops.v7_1.sbom.models.ConfigurationSetting>`
    :param manifest_info: A list of name and version of the manifest that we are generating.
    :type manifest_info: :class:`ConfigurationSetting <azure.devops.v7_1.sbom.models.ConfigurationSetting>`
    :param manifest_tool_action: The action currently being performed by the manifest tool.
    :type manifest_tool_action: object
    :param package_name: The name of the package this SBOM represents.
    :type package_name: :class:`ConfigurationSetting <azure.devops.v7_1.sbom.models.ConfigurationSetting>`
    :param package_version: The version of the package this SBOM represents.
    :type package_version: :class:`ConfigurationSetting <azure.devops.v7_1.sbom.models.ConfigurationSetting>`
    :param parallelism: The number of parallel threads to use for the workflows.
    :type parallelism: :class:`ConfigurationSetting <azure.devops.v7_1.sbom.models.ConfigurationSetting>`
    :param root_path_filter: If you're downloading only a part of the drop using the '-r' or 'root' parameter in the drop client, specify the same string value here in order to skip validating paths that are not downloaded.
    :type root_path_filter: :class:`ConfigurationSetting <azure.devops.v7_1.sbom.models.ConfigurationSetting>`
    :param telemetry_file_path: If specified, we will store the generated telemetry for the execution of the SBOM tool at this path.
    :type telemetry_file_path: :class:`ConfigurationSetting <azure.devops.v7_1.sbom.models.ConfigurationSetting>`
    :param validate_signature: If set, will validate the manifest using the signed catalog file.
    :type validate_signature: :class:`ConfigurationSetting <azure.devops.v7_1.sbom.models.ConfigurationSetting>`
    """

    _attribute_map = {
        'additional_component_detector_args': {'key': 'additionalComponentDetectorArgs', 'type': 'ConfigurationSetting'},
        'build_component_path': {'key': 'buildComponentPath', 'type': 'ConfigurationSetting'},
        'build_drop_path': {'key': 'buildDropPath', 'type': 'ConfigurationSetting'},
        'build_list_file': {'key': 'buildListFile', 'type': 'ConfigurationSetting'},
        'catalog_file_path': {'key': 'catalogFilePath', 'type': 'ConfigurationSetting'},
        'config_file_path': {'key': 'configFilePath', 'type': 'ConfigurationSetting'},
        'docker_images_to_scan': {'key': 'dockerImagesToScan', 'type': 'ConfigurationSetting'},
        'external_document_reference_list_file': {'key': 'externalDocumentReferenceListFile', 'type': 'ConfigurationSetting'},
        'hash_algorithm': {'key': 'hashAlgorithm', 'type': 'ConfigurationSetting'},
        'ignore_missing': {'key': 'ignoreMissing', 'type': 'ConfigurationSetting'},
        'manifest_dir_path': {'key': 'manifestDirPath', 'type': 'ConfigurationSetting'},
        'manifest_info': {'key': 'manifestInfo', 'type': 'ConfigurationSetting'},
        'manifest_tool_action': {'key': 'manifestToolAction', 'type': 'object'},
        'package_name': {'key': 'packageName', 'type': 'ConfigurationSetting'},
        'package_version': {'key': 'packageVersion', 'type': 'ConfigurationSetting'},
        'parallelism': {'key': 'parallelism', 'type': 'ConfigurationSetting'},
        'root_path_filter': {'key': 'rootPathFilter', 'type': 'ConfigurationSetting'},
        'telemetry_file_path': {'key': 'telemetryFilePath', 'type': 'ConfigurationSetting'},
        'validate_signature': {'key': 'validateSignature', 'type': 'ConfigurationSetting'}
    }

    def __init__(self, additional_component_detector_args=None, build_component_path=None, build_drop_path=None, build_list_file=None, catalog_file_path=None, config_file_path=None, docker_images_to_scan=None, external_document_reference_list_file=None, hash_algorithm=None, ignore_missing=None, manifest_dir_path=None, manifest_info=None, manifest_tool_action=None, package_name=None, package_version=None, parallelism=None, root_path_filter=None, telemetry_file_path=None, validate_signature=None):
        super(Configuration, self).__init__()
        self.additional_component_detector_args = additional_component_detector_args
        self.build_component_path = build_component_path
        self.build_drop_path = build_drop_path
        self.build_list_file = build_list_file
        self.catalog_file_path = catalog_file_path
        self.config_file_path = config_file_path
        self.docker_images_to_scan = docker_images_to_scan
        self.external_document_reference_list_file = external_document_reference_list_file
        self.hash_algorithm = hash_algorithm
        self.ignore_missing = ignore_missing
        self.manifest_dir_path = manifest_dir_path
        self.manifest_info = manifest_info
        self.manifest_tool_action = manifest_tool_action
        self.package_name = package_name
        self.package_version = package_version
        self.parallelism = parallelism
        self.root_path_filter = root_path_filter
        self.telemetry_file_path = telemetry_file_path
        self.validate_signature = validate_signature


class ConfigurationSetting(Model):
    """
    Encapsulates a configuration setting to provide metadata about the setting source and type.

    :param source: The source where this setting came from.
    :type source: str
    :param value: The actual value of the setting.
    :type value: object
    """

    _attribute_map = {
        'source': {'key': 'source', 'type': 'str'},
        'value': {'key': 'value', 'type': 'object'}
    }

    def __init__(self, source=None, value=None):
        super(ConfigurationSetting, self).__init__()
        self.source = source
        self.value = value


class FileHash(Model):
    """
    Used to provide the filename and hash of the SBOM file to be added to the catalog file.

    :param file_name: The filename of the SBOM.
    :type file_name: str
    :param hash: The string hash of the SBOM file.
    :type hash: str
    :param hash_algorithm_name: The HashAlgorithmName used to generate the hash of the file.
    :type hash_algorithm_name: HashAlgorithmName
    """

    _attribute_map = {
        'file_name': {'key': 'fileName', 'type': 'str'},
        'hash': {'key': 'hash', 'type': 'str'},
        'hash_algorithm_name': {'key': 'hashAlgorithmName', 'type': 'HashAlgorithmName'}
    }

    def __init__(self, file_name=None, hash=None, hash_algorithm_name=None):
        super(FileHash, self).__init__()
        self.file_name = file_name
        self.hash = hash
        self.hash_algorithm_name = hash_algorithm_name


class ManifestInfo(Model):
    """
    Defines a manifest name and version.

    :param name: The name of the manifest.
    :type name: str
    :param version: The version of the manifest.
    :type version: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, name=None, version=None):
        super(ManifestInfo, self).__init__()
        self.name = name
        self.version = version


class SBOMFile(Model):
    """
    Represents a SBOM file object and contains additional properties related to the file.

    :param file_size_in_bytes: The size of the SBOM file in bytes.
    :type file_size_in_bytes: long
    :param sbom_file_path: The path where the final generated SBOM is placed.
    :type sbom_file_path: str
    :param sbom_format_name: The name and version of the format of the generated SBOM.
    :type sbom_format_name: :class:`ManifestInfo <azure.devops.v7_1.sbom.models.ManifestInfo>`
    """

    _attribute_map = {
        'file_size_in_bytes': {'key': 'fileSizeInBytes', 'type': 'long'},
        'sbom_file_path': {'key': 'sbomFilePath', 'type': 'str'},
        'sbom_format_name': {'key': 'sbomFormatName', 'type': 'ManifestInfo'}
    }

    def __init__(self, file_size_in_bytes=None, sbom_file_path=None, sbom_format_name=None):
        super(SBOMFile, self).__init__()
        self.file_size_in_bytes = file_size_in_bytes
        self.sbom_file_path = sbom_file_path
        self.sbom_format_name = sbom_format_name


class SBOMTelemetry(Model):
    """
    The telemetry that is logged to a file/console for the given SBOM execution.

    :param bsi_data: All available bsi data from the task build execution which includes build and system environment variables like repository and build information.
    :type bsi_data: dict
    :param bsi_source: The source of the bsi data.
    :type bsi_source: str
    :param e2_eTask_result: The end to end results of the extension task.
    :type e2_eTask_result: str
    :param parameters: A list of ConfigurationSetting`1 representing each input parameter used in the validation.
    :type parameters: :class:`Configuration <azure.devops.v7_1.sbom.models.Configuration>`
    :param result: The result of the execution
    :type result: str
    :param sbom_formats_used: A list of the SBOM formats and related file properties that was used in the generation/validation of the SBOM.
    :type sbom_formats_used: list of :class:`SBOMFile <azure.devops.v7_1.sbom.models.SBOMFile>`
    :param switches: Any internal switches and their value that were used during the execution. A switch can be something that was provided through a configuraiton or an environment variable.
    :type switches: dict
    :param task_error_message: Error messages that came from the extension task.
    :type task_error_message: str
    :param telemetry_id: The unique id for this telemetry
    :type telemetry_id: str
    :param tool_execution_result: The result of the tool as a numeric value.
    :type tool_execution_result: int
    """

    _attribute_map = {
        'bsi_data': {'key': 'bsiData', 'type': '{str}'},
        'bsi_source': {'key': 'bsiSource', 'type': 'str'},
        'e2_eTask_result': {'key': 'e2ETaskResult', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': 'Configuration'},
        'result': {'key': 'result', 'type': 'str'},
        'sbom_formats_used': {'key': 'sbomFormatsUsed', 'type': '[SBOMFile]'},
        'switches': {'key': 'switches', 'type': '{object}'},
        'task_error_message': {'key': 'taskErrorMessage', 'type': 'str'},
        'telemetry_id': {'key': 'telemetryId', 'type': 'str'},
        'tool_execution_result': {'key': 'toolExecutionResult', 'type': 'int'}
    }

    def __init__(self, bsi_data=None, bsi_source=None, e2_eTask_result=None, parameters=None, result=None, sbom_formats_used=None, switches=None, task_error_message=None, telemetry_id=None, tool_execution_result=None):
        super(SBOMTelemetry, self).__init__()
        self.bsi_data = bsi_data
        self.bsi_source = bsi_source
        self.e2_eTask_result = e2_eTask_result
        self.parameters = parameters
        self.result = result
        self.sbom_formats_used = sbom_formats_used
        self.switches = switches
        self.task_error_message = task_error_message
        self.telemetry_id = telemetry_id
        self.tool_execution_result = tool_execution_result


class SignResponseBase(Model):
    """
    The base reponse object for all responses from the signing api.

    :param customer_correlation_id: The customer correlation id that is sent to ESRP for correlating the current request to ESRP.
    :type customer_correlation_id: str
    :param error_info: If this is an error response, it will have more information about the error.
    :type error_info: str
    :param result: The result of the response.
    :type result: object
    """

    _attribute_map = {
        'customer_correlation_id': {'key': 'customerCorrelationId', 'type': 'str'},
        'error_info': {'key': 'errorInfo', 'type': 'str'},
        'result': {'key': 'result', 'type': 'object'}
    }

    def __init__(self, customer_correlation_id=None, error_info=None, result=None):
        super(SignResponseBase, self).__init__()
        self.customer_correlation_id = customer_correlation_id
        self.error_info = error_info
        self.result = result


class SignStatusResponse(SignResponseBase):
    """
    The response returned by the sign status api.

    :param customer_correlation_id: The customer correlation id that is sent to ESRP for correlating the current request to ESRP.
    :type customer_correlation_id: str
    :param error_info: If this is an error response, it will have more information about the error.
    :type error_info: str
    :param result: The result of the response.
    :type result: object
    :param download_url: The pre-signed download url used to download the signed catalog file.
    :type download_url: str
    """

    _attribute_map = {
        'customer_correlation_id': {'key': 'customerCorrelationId', 'type': 'str'},
        'error_info': {'key': 'errorInfo', 'type': 'str'},
        'result': {'key': 'result', 'type': 'object'},
        'download_url': {'key': 'downloadUrl', 'type': 'str'}
    }

    def __init__(self, customer_correlation_id=None, error_info=None, result=None, download_url=None):
        super(SignStatusResponse, self).__init__(customer_correlation_id=customer_correlation_id, error_info=error_info, result=result)
        self.download_url = download_url


__all__ = [
    'Configuration',
    'ConfigurationSetting',
    'FileHash',
    'ManifestInfo',
    'SBOMFile',
    'SBOMTelemetry',
    'SignResponseBase',
    'SignStatusResponse',
]
