# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class RetentionPolicy(Model):
    """RetentionPolicy.

    :param artifacts:
    :type artifacts: list of str
    :param artifact_types_to_delete:
    :type artifact_types_to_delete: list of str
    :param branches:
    :type branches: list of str
    :param days_to_keep: The number of days to keep builds.
    :type days_to_keep: int
    :param delete_build_record: Indicates whether the build record itself should be deleted.
    :type delete_build_record: bool
    :param delete_test_results: Indicates whether to delete test results associated with the build.
    :type delete_test_results: bool
    :param minimum_to_keep: The minimum number of builds to keep.
    :type minimum_to_keep: int
    """

    _attribute_map = {
        'artifacts': {'key': 'artifacts', 'type': '[str]'},
        'artifact_types_to_delete': {'key': 'artifactTypesToDelete', 'type': '[str]'},
        'branches': {'key': 'branches', 'type': '[str]'},
        'days_to_keep': {'key': 'daysToKeep', 'type': 'int'},
        'delete_build_record': {'key': 'deleteBuildRecord', 'type': 'bool'},
        'delete_test_results': {'key': 'deleteTestResults', 'type': 'bool'},
        'minimum_to_keep': {'key': 'minimumToKeep', 'type': 'int'}
    }

    def __init__(self, artifacts=None, artifact_types_to_delete=None, branches=None, days_to_keep=None, delete_build_record=None, delete_test_results=None, minimum_to_keep=None):
        super(RetentionPolicy, self).__init__()
        self.artifacts = artifacts
        self.artifact_types_to_delete = artifact_types_to_delete
        self.branches = branches
        self.days_to_keep = days_to_keep
        self.delete_build_record = delete_build_record
        self.delete_test_results = delete_test_results
        self.minimum_to_keep = minimum_to_keep
