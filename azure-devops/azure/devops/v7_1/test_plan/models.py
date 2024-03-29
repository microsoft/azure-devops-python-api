﻿# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class BuildDefinitionReference(Model):
    """
    The build definition reference resource

    :param id: ID of the build definition
    :type id: int
    :param name: Name of the build definition
    :type name: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, id=None, name=None):
        super(BuildDefinitionReference, self).__init__()
        self.id = id
        self.name = name


class CloneOperationCommonResponse(Model):
    """
    Common Response for clone operation

    :param clone_statistics: Various statistics related to the clone operation
    :type clone_statistics: :class:`CloneStatistics <azure.devops.v7_1.test_plan.models.CloneStatistics>`
    :param completion_date: Completion data of the operation
    :type completion_date: datetime
    :param creation_date: Creation data of the operation
    :type creation_date: datetime
    :param links: Reference links
    :type links: :class:`ReferenceLinks <azure.devops.v7_1.test_plan.models.ReferenceLinks>`
    :param message: Message related to the job
    :type message: str
    :param op_id: Clone operation Id
    :type op_id: int
    :param state: Clone operation state
    :type state: object
    """

    _attribute_map = {
        'clone_statistics': {'key': 'cloneStatistics', 'type': 'CloneStatistics'},
        'completion_date': {'key': 'completionDate', 'type': 'iso-8601'},
        'creation_date': {'key': 'creationDate', 'type': 'iso-8601'},
        'links': {'key': 'links', 'type': 'ReferenceLinks'},
        'message': {'key': 'message', 'type': 'str'},
        'op_id': {'key': 'opId', 'type': 'int'},
        'state': {'key': 'state', 'type': 'object'}
    }

    def __init__(self, clone_statistics=None, completion_date=None, creation_date=None, links=None, message=None, op_id=None, state=None):
        super(CloneOperationCommonResponse, self).__init__()
        self.clone_statistics = clone_statistics
        self.completion_date = completion_date
        self.creation_date = creation_date
        self.links = links
        self.message = message
        self.op_id = op_id
        self.state = state


class CloneOptions(Model):
    """
    Clone options for cloning the test suite.

    :param clone_requirements: If set to true requirements will be cloned
    :type clone_requirements: bool
    :param copy_all_suites: copy all suites from a source plan
    :type copy_all_suites: bool
    :param copy_ancestor_hierarchy: copy ancestor hierarchy
    :type copy_ancestor_hierarchy: bool
    :param destination_work_item_type: Name of the workitem type of the clone
    :type destination_work_item_type: str
    :param override_parameters: Key value pairs where the key value is overridden by the value.
    :type override_parameters: dict
    :param related_link_comment: Comment on the link that will link the new clone  test case to the original Set null for no comment
    :type related_link_comment: str
    """

    _attribute_map = {
        'clone_requirements': {'key': 'cloneRequirements', 'type': 'bool'},
        'copy_all_suites': {'key': 'copyAllSuites', 'type': 'bool'},
        'copy_ancestor_hierarchy': {'key': 'copyAncestorHierarchy', 'type': 'bool'},
        'destination_work_item_type': {'key': 'destinationWorkItemType', 'type': 'str'},
        'override_parameters': {'key': 'overrideParameters', 'type': '{str}'},
        'related_link_comment': {'key': 'relatedLinkComment', 'type': 'str'}
    }

    def __init__(self, clone_requirements=None, copy_all_suites=None, copy_ancestor_hierarchy=None, destination_work_item_type=None, override_parameters=None, related_link_comment=None):
        super(CloneOptions, self).__init__()
        self.clone_requirements = clone_requirements
        self.copy_all_suites = copy_all_suites
        self.copy_ancestor_hierarchy = copy_ancestor_hierarchy
        self.destination_work_item_type = destination_work_item_type
        self.override_parameters = override_parameters
        self.related_link_comment = related_link_comment


class CloneStatistics(Model):
    """
    Clone Statistics Details.

    :param cloned_requirements_count: Number of requirements cloned so far.
    :type cloned_requirements_count: int
    :param cloned_shared_steps_count: Number of shared steps cloned so far.
    :type cloned_shared_steps_count: int
    :param cloned_test_cases_count: Number of test cases cloned so far
    :type cloned_test_cases_count: int
    :param total_requirements_count: Total number of requirements to be cloned
    :type total_requirements_count: int
    :param total_test_cases_count: Total number of test cases to be cloned
    :type total_test_cases_count: int
    """

    _attribute_map = {
        'cloned_requirements_count': {'key': 'clonedRequirementsCount', 'type': 'int'},
        'cloned_shared_steps_count': {'key': 'clonedSharedStepsCount', 'type': 'int'},
        'cloned_test_cases_count': {'key': 'clonedTestCasesCount', 'type': 'int'},
        'total_requirements_count': {'key': 'totalRequirementsCount', 'type': 'int'},
        'total_test_cases_count': {'key': 'totalTestCasesCount', 'type': 'int'}
    }

    def __init__(self, cloned_requirements_count=None, cloned_shared_steps_count=None, cloned_test_cases_count=None, total_requirements_count=None, total_test_cases_count=None):
        super(CloneStatistics, self).__init__()
        self.cloned_requirements_count = cloned_requirements_count
        self.cloned_shared_steps_count = cloned_shared_steps_count
        self.cloned_test_cases_count = cloned_test_cases_count
        self.total_requirements_count = total_requirements_count
        self.total_test_cases_count = total_test_cases_count


class CloneTestCaseOperationInformation(Model):
    """
    :param clone_operation_response: Various information related to the clone
    :type clone_operation_response: :class:`CloneOperationCommonResponse <azure.devops.v7_1.test_plan.models.CloneOperationCommonResponse>`
    :param clone_options: Test Plan Clone create parameters
    :type clone_options: :class:`CloneTestCaseOptions <azure.devops.v7_1.test_plan.models.CloneTestCaseOptions>`
    :param destination_test_suite: Information of destination Test Suite
    :type destination_test_suite: :class:`TestSuiteReferenceWithProject <azure.devops.v7_1.test_plan.models.TestSuiteReferenceWithProject>`
    :param source_test_suite: Information of source Test Suite
    :type source_test_suite: :class:`SourceTestSuiteResponse <azure.devops.v7_1.test_plan.models.SourceTestSuiteResponse>`
    """

    _attribute_map = {
        'clone_operation_response': {'key': 'cloneOperationResponse', 'type': 'CloneOperationCommonResponse'},
        'clone_options': {'key': 'cloneOptions', 'type': 'CloneTestCaseOptions'},
        'destination_test_suite': {'key': 'destinationTestSuite', 'type': 'TestSuiteReferenceWithProject'},
        'source_test_suite': {'key': 'sourceTestSuite', 'type': 'SourceTestSuiteResponse'}
    }

    def __init__(self, clone_operation_response=None, clone_options=None, destination_test_suite=None, source_test_suite=None):
        super(CloneTestCaseOperationInformation, self).__init__()
        self.clone_operation_response = clone_operation_response
        self.clone_options = clone_options
        self.destination_test_suite = destination_test_suite
        self.source_test_suite = source_test_suite


class CloneTestCaseOptions(Model):
    """
    :param include_attachments: If set to true, include the attachments
    :type include_attachments: bool
    :param include_links: If set to true, include the links
    :type include_links: bool
    :param related_link_comment: Comment on the link that will link the new clone  test case to the original Set null for no comment
    :type related_link_comment: str
    """

    _attribute_map = {
        'include_attachments': {'key': 'includeAttachments', 'type': 'bool'},
        'include_links': {'key': 'includeLinks', 'type': 'bool'},
        'related_link_comment': {'key': 'relatedLinkComment', 'type': 'str'}
    }

    def __init__(self, include_attachments=None, include_links=None, related_link_comment=None):
        super(CloneTestCaseOptions, self).__init__()
        self.include_attachments = include_attachments
        self.include_links = include_links
        self.related_link_comment = related_link_comment


class CloneTestCaseParams(Model):
    """
    Parameters for Test Suite clone operation

    :param clone_options: Test Case Clone create parameters
    :type clone_options: :class:`CloneTestCaseOptions <azure.devops.v7_1.test_plan.models.CloneTestCaseOptions>`
    :param destination_test_plan: Information about destination Test Plan
    :type destination_test_plan: :class:`TestPlanReference <azure.devops.v7_1.test_plan.models.TestPlanReference>`
    :param destination_test_suite: Information about destination Test Suite
    :type destination_test_suite: :class:`DestinationTestSuiteInfo <azure.devops.v7_1.test_plan.models.DestinationTestSuiteInfo>`
    :param source_test_plan: Information about source Test Plan
    :type source_test_plan: :class:`TestPlanReference <azure.devops.v7_1.test_plan.models.TestPlanReference>`
    :param source_test_suite: Information about source Test Suite
    :type source_test_suite: :class:`SourceTestSuiteInfo <azure.devops.v7_1.test_plan.models.SourceTestSuiteInfo>`
    :param test_case_ids: Test Case IDs
    :type test_case_ids: list of int
    """

    _attribute_map = {
        'clone_options': {'key': 'cloneOptions', 'type': 'CloneTestCaseOptions'},
        'destination_test_plan': {'key': 'destinationTestPlan', 'type': 'TestPlanReference'},
        'destination_test_suite': {'key': 'destinationTestSuite', 'type': 'DestinationTestSuiteInfo'},
        'source_test_plan': {'key': 'sourceTestPlan', 'type': 'TestPlanReference'},
        'source_test_suite': {'key': 'sourceTestSuite', 'type': 'SourceTestSuiteInfo'},
        'test_case_ids': {'key': 'testCaseIds', 'type': '[int]'}
    }

    def __init__(self, clone_options=None, destination_test_plan=None, destination_test_suite=None, source_test_plan=None, source_test_suite=None, test_case_ids=None):
        super(CloneTestCaseParams, self).__init__()
        self.clone_options = clone_options
        self.destination_test_plan = destination_test_plan
        self.destination_test_suite = destination_test_suite
        self.source_test_plan = source_test_plan
        self.source_test_suite = source_test_suite
        self.test_case_ids = test_case_ids


class CloneTestPlanOperationInformation(Model):
    """
    Response for Test Plan clone operation

    :param clone_operation_response: Various information related to the clone
    :type clone_operation_response: :class:`CloneOperationCommonResponse <azure.devops.v7_1.test_plan.models.CloneOperationCommonResponse>`
    :param clone_options: Test Plan Clone create parameters
    :type clone_options: :class:`CloneOptions <azure.devops.v7_1.test_plan.models.CloneOptions>`
    :param destination_test_plan: Information of destination Test Plan
    :type destination_test_plan: :class:`TestPlan <azure.devops.v7_1.test_plan.models.TestPlan>`
    :param source_test_plan: Information of source Test Plan
    :type source_test_plan: :class:`SourceTestplanResponse <azure.devops.v7_1.test_plan.models.SourceTestplanResponse>`
    """

    _attribute_map = {
        'clone_operation_response': {'key': 'cloneOperationResponse', 'type': 'CloneOperationCommonResponse'},
        'clone_options': {'key': 'cloneOptions', 'type': 'CloneOptions'},
        'destination_test_plan': {'key': 'destinationTestPlan', 'type': 'TestPlan'},
        'source_test_plan': {'key': 'sourceTestPlan', 'type': 'SourceTestplanResponse'}
    }

    def __init__(self, clone_operation_response=None, clone_options=None, destination_test_plan=None, source_test_plan=None):
        super(CloneTestPlanOperationInformation, self).__init__()
        self.clone_operation_response = clone_operation_response
        self.clone_options = clone_options
        self.destination_test_plan = destination_test_plan
        self.source_test_plan = source_test_plan


class CloneTestPlanParams(Model):
    """
    Parameters for Test Plan clone operation

    :param clone_options: Test Plan Clone create parameters
    :type clone_options: :class:`CloneOptions <azure.devops.v7_1.test_plan.models.CloneOptions>`
    :param destination_test_plan: Information about destination Test Plan
    :type destination_test_plan: :class:`DestinationTestPlanCloneParams <azure.devops.v7_1.test_plan.models.DestinationTestPlanCloneParams>`
    :param source_test_plan: Information about source Test Plan
    :type source_test_plan: :class:`SourceTestPlanInfo <azure.devops.v7_1.test_plan.models.SourceTestPlanInfo>`
    """

    _attribute_map = {
        'clone_options': {'key': 'cloneOptions', 'type': 'CloneOptions'},
        'destination_test_plan': {'key': 'destinationTestPlan', 'type': 'DestinationTestPlanCloneParams'},
        'source_test_plan': {'key': 'sourceTestPlan', 'type': 'SourceTestPlanInfo'}
    }

    def __init__(self, clone_options=None, destination_test_plan=None, source_test_plan=None):
        super(CloneTestPlanParams, self).__init__()
        self.clone_options = clone_options
        self.destination_test_plan = destination_test_plan
        self.source_test_plan = source_test_plan


class CloneTestSuiteOperationInformation(Model):
    """
    Response for Test Suite clone operation

    :param cloned_test_suite: Information of newly cloned Test Suite
    :type cloned_test_suite: :class:`TestSuiteReferenceWithProject <azure.devops.v7_1.test_plan.models.TestSuiteReferenceWithProject>`
    :param clone_operation_response: Various information related to the clone
    :type clone_operation_response: :class:`CloneOperationCommonResponse <azure.devops.v7_1.test_plan.models.CloneOperationCommonResponse>`
    :param clone_options: Test Plan Clone create parameters
    :type clone_options: :class:`CloneOptions <azure.devops.v7_1.test_plan.models.CloneOptions>`
    :param destination_test_suite: Information of destination Test Suite
    :type destination_test_suite: :class:`TestSuiteReferenceWithProject <azure.devops.v7_1.test_plan.models.TestSuiteReferenceWithProject>`
    :param source_test_suite: Information of source Test Suite
    :type source_test_suite: :class:`TestSuiteReferenceWithProject <azure.devops.v7_1.test_plan.models.TestSuiteReferenceWithProject>`
    """

    _attribute_map = {
        'cloned_test_suite': {'key': 'clonedTestSuite', 'type': 'TestSuiteReferenceWithProject'},
        'clone_operation_response': {'key': 'cloneOperationResponse', 'type': 'CloneOperationCommonResponse'},
        'clone_options': {'key': 'cloneOptions', 'type': 'CloneOptions'},
        'destination_test_suite': {'key': 'destinationTestSuite', 'type': 'TestSuiteReferenceWithProject'},
        'source_test_suite': {'key': 'sourceTestSuite', 'type': 'TestSuiteReferenceWithProject'}
    }

    def __init__(self, cloned_test_suite=None, clone_operation_response=None, clone_options=None, destination_test_suite=None, source_test_suite=None):
        super(CloneTestSuiteOperationInformation, self).__init__()
        self.cloned_test_suite = cloned_test_suite
        self.clone_operation_response = clone_operation_response
        self.clone_options = clone_options
        self.destination_test_suite = destination_test_suite
        self.source_test_suite = source_test_suite


class CloneTestSuiteParams(Model):
    """
    Parameters for Test Suite clone operation

    :param clone_options: Test Plan Clone create parameters
    :type clone_options: :class:`CloneOptions <azure.devops.v7_1.test_plan.models.CloneOptions>`
    :param destination_test_suite: Information about destination Test Suite
    :type destination_test_suite: :class:`DestinationTestSuiteInfo <azure.devops.v7_1.test_plan.models.DestinationTestSuiteInfo>`
    :param source_test_suite: Information about source Test Suite
    :type source_test_suite: :class:`SourceTestSuiteInfo <azure.devops.v7_1.test_plan.models.SourceTestSuiteInfo>`
    """

    _attribute_map = {
        'clone_options': {'key': 'cloneOptions', 'type': 'CloneOptions'},
        'destination_test_suite': {'key': 'destinationTestSuite', 'type': 'DestinationTestSuiteInfo'},
        'source_test_suite': {'key': 'sourceTestSuite', 'type': 'SourceTestSuiteInfo'}
    }

    def __init__(self, clone_options=None, destination_test_suite=None, source_test_suite=None):
        super(CloneTestSuiteParams, self).__init__()
        self.clone_options = clone_options
        self.destination_test_suite = destination_test_suite
        self.source_test_suite = source_test_suite


class Configuration(Model):
    """
    Configuration of the Test Point

    :param configuration_id: Id of the Configuration Assigned to the Test Point
    :type configuration_id: int
    """

    _attribute_map = {
        'configuration_id': {'key': 'configurationId', 'type': 'int'}
    }

    def __init__(self, configuration_id=None):
        super(Configuration, self).__init__()
        self.configuration_id = configuration_id


class DestinationTestSuiteInfo(Model):
    """
    Destination Test Suite information for Test Suite clone operation

    :param id: Destination Suite Id
    :type id: int
    :param project: Destination Project Name
    :type project: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'project': {'key': 'project', 'type': 'str'}
    }

    def __init__(self, id=None, project=None):
        super(DestinationTestSuiteInfo, self).__init__()
        self.id = id
        self.project = project


class GraphSubjectBase(Model):
    """
    :param _links: This field contains zero or more interesting links about the graph subject. These links may be invoked to obtain additional relationships or more detailed information about this graph subject.
    :type _links: :class:`ReferenceLinks <azure.devops.v7_1.microsoft._visual_studio._services._web_api.models.ReferenceLinks>`
    :param descriptor: The descriptor is the primary way to reference the graph subject while the system is running. This field will uniquely identify the same graph subject across both Accounts and Organizations.
    :type descriptor: str
    :param display_name: This is the non-unique display name of the graph subject. To change this field, you must alter its value in the source provider.
    :type display_name: str
    :param url: This url is the full route to the source resource of this graph subject.
    :type url: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'descriptor': {'key': 'descriptor', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, descriptor=None, display_name=None, url=None):
        super(GraphSubjectBase, self).__init__()
        self._links = _links
        self.descriptor = descriptor
        self.display_name = display_name
        self.url = url


class IdentityRef(GraphSubjectBase):
    """
    :param _links: This field contains zero or more interesting links about the graph subject. These links may be invoked to obtain additional relationships or more detailed information about this graph subject.
    :type _links: :class:`ReferenceLinks <azure.devops.v7_1.microsoft._visual_studio._services._web_api.models.ReferenceLinks>`
    :param descriptor: The descriptor is the primary way to reference the graph subject while the system is running. This field will uniquely identify the same graph subject across both Accounts and Organizations.
    :type descriptor: str
    :param display_name: This is the non-unique display name of the graph subject. To change this field, you must alter its value in the source provider.
    :type display_name: str
    :param url: This url is the full route to the source resource of this graph subject.
    :type url: str
    :param directory_alias: Deprecated - Can be retrieved by querying the Graph user referenced in the "self" entry of the IdentityRef "_links" dictionary
    :type directory_alias: str
    :param id:
    :type id: str
    :param image_url: Deprecated - Available in the "avatar" entry of the IdentityRef "_links" dictionary
    :type image_url: str
    :param inactive: Deprecated - Can be retrieved by querying the Graph membership state referenced in the "membershipState" entry of the GraphUser "_links" dictionary
    :type inactive: bool
    :param is_aad_identity: Deprecated - Can be inferred from the subject type of the descriptor (Descriptor.IsAadUserType/Descriptor.IsAadGroupType)
    :type is_aad_identity: bool
    :param is_container: Deprecated - Can be inferred from the subject type of the descriptor (Descriptor.IsGroupType)
    :type is_container: bool
    :param is_deleted_in_origin:
    :type is_deleted_in_origin: bool
    :param profile_url: Deprecated - not in use in most preexisting implementations of ToIdentityRef
    :type profile_url: str
    :param unique_name: Deprecated - use Domain+PrincipalName instead
    :type unique_name: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'descriptor': {'key': 'descriptor', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'directory_alias': {'key': 'directoryAlias', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'image_url': {'key': 'imageUrl', 'type': 'str'},
        'inactive': {'key': 'inactive', 'type': 'bool'},
        'is_aad_identity': {'key': 'isAadIdentity', 'type': 'bool'},
        'is_container': {'key': 'isContainer', 'type': 'bool'},
        'is_deleted_in_origin': {'key': 'isDeletedInOrigin', 'type': 'bool'},
        'profile_url': {'key': 'profileUrl', 'type': 'str'},
        'unique_name': {'key': 'uniqueName', 'type': 'str'}
    }

    def __init__(self, _links=None, descriptor=None, display_name=None, url=None, directory_alias=None, id=None, image_url=None, inactive=None, is_aad_identity=None, is_container=None, is_deleted_in_origin=None, profile_url=None, unique_name=None):
        super(IdentityRef, self).__init__(_links=_links, descriptor=descriptor, display_name=display_name, url=url)
        self.directory_alias = directory_alias
        self.id = id
        self.image_url = image_url
        self.inactive = inactive
        self.is_aad_identity = is_aad_identity
        self.is_container = is_container
        self.is_deleted_in_origin = is_deleted_in_origin
        self.profile_url = profile_url
        self.unique_name = unique_name


class LastResultDetails(Model):
    """
    Last result details of test point.

    :param date_completed: Completed date of last result.
    :type date_completed: datetime
    :param duration: Duration of the last result in milliseconds.
    :type duration: long
    :param run_by: The user who executed the last result.
    :type run_by: :class:`IdentityRef <azure.devops.v7_1.microsoft._team_foundation._test_management._web_api.models.IdentityRef>`
    """

    _attribute_map = {
        'date_completed': {'key': 'dateCompleted', 'type': 'iso-8601'},
        'duration': {'key': 'duration', 'type': 'long'},
        'run_by': {'key': 'runBy', 'type': 'IdentityRef'}
    }

    def __init__(self, date_completed=None, duration=None, run_by=None):
        super(LastResultDetails, self).__init__()
        self.date_completed = date_completed
        self.duration = duration
        self.run_by = run_by


class LibraryWorkItemsData(Model):
    """
    This data model is used in Work item-based tabs of Test Plans Library.

    :param column_options: Specifies the column option field names
    :type column_options: list of str
    :param continuation_token: Continuation token to fetch next set of elements. Present only when HasMoreElements is true.
    :type continuation_token: str
    :param exceeded_work_item_query_limit: Boolean indicating if the WIQL query has exceeded the limit of items returned.
    :type exceeded_work_item_query_limit: bool
    :param has_more_elements: Boolean indicating if there are more elements present than what are being sent.
    :type has_more_elements: bool
    :param return_code: Specifies if there was an error while execution of data provider.
    :type return_code: object
    :param work_item_ids: List of work items returned when OrderByField is sent something other than Id.
    :type work_item_ids: list of int
    :param work_items: List of work items to be returned.
    :type work_items: list of :class:`WorkItemDetails <azure.devops.v7_1.test_plan.models.WorkItemDetails>`
    """

    _attribute_map = {
        'column_options': {'key': 'columnOptions', 'type': '[str]'},
        'continuation_token': {'key': 'continuationToken', 'type': 'str'},
        'exceeded_work_item_query_limit': {'key': 'exceededWorkItemQueryLimit', 'type': 'bool'},
        'has_more_elements': {'key': 'hasMoreElements', 'type': 'bool'},
        'return_code': {'key': 'returnCode', 'type': 'object'},
        'work_item_ids': {'key': 'workItemIds', 'type': '[int]'},
        'work_items': {'key': 'workItems', 'type': '[WorkItemDetails]'}
    }

    def __init__(self, column_options=None, continuation_token=None, exceeded_work_item_query_limit=None, has_more_elements=None, return_code=None, work_item_ids=None, work_items=None):
        super(LibraryWorkItemsData, self).__init__()
        self.column_options = column_options
        self.continuation_token = continuation_token
        self.exceeded_work_item_query_limit = exceeded_work_item_query_limit
        self.has_more_elements = has_more_elements
        self.return_code = return_code
        self.work_item_ids = work_item_ids
        self.work_items = work_items


class LibraryWorkItemsDataProviderRequest(Model):
    """
    This is the request data contract for LibraryTestCaseDataProvider.

    :param column_options: Specifies the list of column options to show in test cases table.
    :type column_options: list of str
    :param continuation_token: The continuation token required for paging of work items. This is required when getting subsequent sets of work items when OrderByField is Id.
    :type continuation_token: str
    :param filter_values: List of filter values to be supplied. Currently supported filters are Title, State, AssignedTo, Priority, AreaPath.
    :type filter_values: list of :class:`TestPlansLibraryWorkItemFilter <azure.devops.v7_1.test_plan.models.TestPlansLibraryWorkItemFilter>`
    :param is_ascending: Whether the data is to be sorted in ascending or descending order. When not supplied, defaults to descending.
    :type is_ascending: bool
    :param library_query_type: The type of query to run.
    :type library_query_type: object
    :param order_by_field: Work item field on which to order the results. When not supplied, defaults to work item IDs.
    :type order_by_field: str
    :param work_item_ids: List of work items to query for field details. This is required when getting subsequent sets of work item fields when OrderByField is other than Id.
    :type work_item_ids: list of int
    """

    _attribute_map = {
        'column_options': {'key': 'columnOptions', 'type': '[str]'},
        'continuation_token': {'key': 'continuationToken', 'type': 'str'},
        'filter_values': {'key': 'filterValues', 'type': '[TestPlansLibraryWorkItemFilter]'},
        'is_ascending': {'key': 'isAscending', 'type': 'bool'},
        'library_query_type': {'key': 'libraryQueryType', 'type': 'object'},
        'order_by_field': {'key': 'orderByField', 'type': 'str'},
        'work_item_ids': {'key': 'workItemIds', 'type': '[int]'}
    }

    def __init__(self, column_options=None, continuation_token=None, filter_values=None, is_ascending=None, library_query_type=None, order_by_field=None, work_item_ids=None):
        super(LibraryWorkItemsDataProviderRequest, self).__init__()
        self.column_options = column_options
        self.continuation_token = continuation_token
        self.filter_values = filter_values
        self.is_ascending = is_ascending
        self.library_query_type = library_query_type
        self.order_by_field = order_by_field
        self.work_item_ids = work_item_ids


class NameValuePair(Model):
    """
    Name value pair

    :param name: Name
    :type name: str
    :param value: Value
    :type value: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, name=None, value=None):
        super(NameValuePair, self).__init__()
        self.name = name
        self.value = value


class PointAssignment(Configuration):
    """
    Assignments for the Test Point

    :param configuration_id: Id of the Configuration Assigned to the Test Point
    :type configuration_id: int
    :param configuration_name: Name of the Configuration Assigned to the Test Point
    :type configuration_name: str
    :param id: Id of the Test Point
    :type id: int
    :param tester: Tester Assigned to the Test Point
    :type tester: :class:`IdentityRef <azure.devops.v7_1.test_plan.models.IdentityRef>`
    """

    _attribute_map = {
        'configuration_id': {'key': 'configurationId', 'type': 'int'},
        'configuration_name': {'key': 'configurationName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'tester': {'key': 'tester', 'type': 'IdentityRef'}
    }

    def __init__(self, configuration_id=None, configuration_name=None, id=None, tester=None):
        super(PointAssignment, self).__init__(configuration_id=configuration_id)
        self.configuration_name = configuration_name
        self.id = id
        self.tester = tester


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


class ReleaseEnvironmentDefinitionReference(Model):
    """
    Reference to release environment resource.

    :param definition_id: ID of the release definition that contains the release environment definition.
    :type definition_id: int
    :param environment_definition_id: ID of the release environment definition.
    :type environment_definition_id: int
    """

    _attribute_map = {
        'definition_id': {'key': 'definitionId', 'type': 'int'},
        'environment_definition_id': {'key': 'environmentDefinitionId', 'type': 'int'}
    }

    def __init__(self, definition_id=None, environment_definition_id=None):
        super(ReleaseEnvironmentDefinitionReference, self).__init__()
        self.definition_id = definition_id
        self.environment_definition_id = environment_definition_id


class Results(Model):
    """
    Results class for Test Point

    :param outcome: Outcome of the Test Point
    :type outcome: object
    """

    _attribute_map = {
        'outcome': {'key': 'outcome', 'type': 'object'}
    }

    def __init__(self, outcome=None):
        super(Results, self).__init__()
        self.outcome = outcome


class SourceTestPlanInfo(Model):
    """
    Source Test Plan information for Test Plan clone operation

    :param id: ID of the source Test Plan
    :type id: int
    :param suite_ids: Id of suites to be cloned inside source Test Plan
    :type suite_ids: list of int
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'suite_ids': {'key': 'suiteIds', 'type': '[int]'}
    }

    def __init__(self, id=None, suite_ids=None):
        super(SourceTestPlanInfo, self).__init__()
        self.id = id
        self.suite_ids = suite_ids


class SourceTestSuiteInfo(Model):
    """
    Source Test Suite information for Test Suite clone operation

    :param id: Id of the Source Test Suite
    :type id: int
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'}
    }

    def __init__(self, id=None):
        super(SourceTestSuiteInfo, self).__init__()
        self.id = id


class SuiteEntryUpdateParams(Model):
    """
    A suite entry defines properties for a test suite.

    :param id: Id of the suite entry in the test suite: either a test case id or child suite id.
    :type id: int
    :param sequence_number: Sequence number for the suite entry object in the test suite.
    :type sequence_number: int
    :param suite_entry_type: Defines whether the entry is of type test case or suite.
    :type suite_entry_type: object
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'sequence_number': {'key': 'sequenceNumber', 'type': 'int'},
        'suite_entry_type': {'key': 'suiteEntryType', 'type': 'object'}
    }

    def __init__(self, id=None, sequence_number=None, suite_entry_type=None):
        super(SuiteEntryUpdateParams, self).__init__()
        self.id = id
        self.sequence_number = sequence_number
        self.suite_entry_type = suite_entry_type


class SuiteTestCaseCreateUpdateParameters(Model):
    """
    Create and Update Suite Test Case Parameters

    :param point_assignments: Configurations Ids
    :type point_assignments: list of :class:`Configuration <azure.devops.v7_1.test_plan.models.Configuration>`
    :param work_item: Id of Test Case to be updated or created
    :type work_item: :class:`WorkItem <azure.devops.v7_1.test_plan.models.WorkItem>`
    """

    _attribute_map = {
        'point_assignments': {'key': 'pointAssignments', 'type': '[Configuration]'},
        'work_item': {'key': 'workItem', 'type': 'WorkItem'}
    }

    def __init__(self, point_assignments=None, work_item=None):
        super(SuiteTestCaseCreateUpdateParameters, self).__init__()
        self.point_assignments = point_assignments
        self.work_item = work_item


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


class TestCase(Model):
    """
    Test Case Class

    :param links: Reference links
    :type links: :class:`ReferenceLinks <azure.devops.v7_1.test_plan.models.ReferenceLinks>`
    :param order: Order of the TestCase in the Suite
    :type order: int
    :param point_assignments: List of Points associated with the Test Case
    :type point_assignments: list of :class:`PointAssignment <azure.devops.v7_1.test_plan.models.PointAssignment>`
    :param project: Project under which the Test Case is
    :type project: :class:`TeamProjectReference <azure.devops.v7_1.test_plan.models.TeamProjectReference>`
    :param test_plan: Test Plan under which the Test Case is
    :type test_plan: :class:`TestPlanReference <azure.devops.v7_1.test_plan.models.TestPlanReference>`
    :param test_suite: Test Suite under which the Test Case is
    :type test_suite: :class:`TestSuiteReference <azure.devops.v7_1.test_plan.models.TestSuiteReference>`
    :param work_item: Work Item details of the TestCase
    :type work_item: :class:`WorkItemDetails <azure.devops.v7_1.test_plan.models.WorkItemDetails>`
    """

    _attribute_map = {
        'links': {'key': 'links', 'type': 'ReferenceLinks'},
        'order': {'key': 'order', 'type': 'int'},
        'point_assignments': {'key': 'pointAssignments', 'type': '[PointAssignment]'},
        'project': {'key': 'project', 'type': 'TeamProjectReference'},
        'test_plan': {'key': 'testPlan', 'type': 'TestPlanReference'},
        'test_suite': {'key': 'testSuite', 'type': 'TestSuiteReference'},
        'work_item': {'key': 'workItem', 'type': 'WorkItemDetails'}
    }

    def __init__(self, links=None, order=None, point_assignments=None, project=None, test_plan=None, test_suite=None, work_item=None):
        super(TestCase, self).__init__()
        self.links = links
        self.order = order
        self.point_assignments = point_assignments
        self.project = project
        self.test_plan = test_plan
        self.test_suite = test_suite
        self.work_item = work_item


class TestCaseAssociatedResult(Model):
    """
    :param completed_date:
    :type completed_date: datetime
    :param configuration:
    :type configuration: :class:`TestConfigurationReference <azure.devops.v7_1.test_plan.models.TestConfigurationReference>`
    :param outcome:
    :type outcome: object
    :param plan:
    :type plan: :class:`TestPlanReference <azure.devops.v7_1.test_plan.models.TestPlanReference>`
    :param point_id:
    :type point_id: int
    :param result_id:
    :type result_id: int
    :param run_by:
    :type run_by: :class:`IdentityRef <azure.devops.v7_1.test_plan.models.IdentityRef>`
    :param run_id:
    :type run_id: int
    :param suite:
    :type suite: :class:`TestSuiteReference <azure.devops.v7_1.test_plan.models.TestSuiteReference>`
    :param tester:
    :type tester: :class:`IdentityRef <azure.devops.v7_1.test_plan.models.IdentityRef>`
    """

    _attribute_map = {
        'completed_date': {'key': 'completedDate', 'type': 'iso-8601'},
        'configuration': {'key': 'configuration', 'type': 'TestConfigurationReference'},
        'outcome': {'key': 'outcome', 'type': 'object'},
        'plan': {'key': 'plan', 'type': 'TestPlanReference'},
        'point_id': {'key': 'pointId', 'type': 'int'},
        'result_id': {'key': 'resultId', 'type': 'int'},
        'run_by': {'key': 'runBy', 'type': 'IdentityRef'},
        'run_id': {'key': 'runId', 'type': 'int'},
        'suite': {'key': 'suite', 'type': 'TestSuiteReference'},
        'tester': {'key': 'tester', 'type': 'IdentityRef'}
    }

    def __init__(self, completed_date=None, configuration=None, outcome=None, plan=None, point_id=None, result_id=None, run_by=None, run_id=None, suite=None, tester=None):
        super(TestCaseAssociatedResult, self).__init__()
        self.completed_date = completed_date
        self.configuration = configuration
        self.outcome = outcome
        self.plan = plan
        self.point_id = point_id
        self.result_id = result_id
        self.run_by = run_by
        self.run_id = run_id
        self.suite = suite
        self.tester = tester


class TestCaseReference(Model):
    """
    Test Case Reference

    :param assigned_to: Identity to whom the test case is assigned
    :type assigned_to: :class:`IdentityRef <azure.devops.v7_1.test_plan.models.IdentityRef>`
    :param id: Test Case Id
    :type id: int
    :param name: Test Case Name
    :type name: str
    :param state: State of the test case work item
    :type state: str
    """

    _attribute_map = {
        'assigned_to': {'key': 'assignedTo', 'type': 'IdentityRef'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'}
    }

    def __init__(self, assigned_to=None, id=None, name=None, state=None):
        super(TestCaseReference, self).__init__()
        self.assigned_to = assigned_to
        self.id = id
        self.name = name
        self.state = state


class TestCaseResultsData(Model):
    """
    This data model is used in TestCaseResultsDataProvider and populates the data required for initial page load

    :param context_point: Point information from where the execution history was viewed. Used to set initial filters.
    :type context_point: :class:`TestPointDetailedReference <azure.devops.v7_1.test_plan.models.TestPointDetailedReference>`
    :param results: Use to store the results displayed in the table
    :type results: list of :class:`TestCaseAssociatedResult <azure.devops.v7_1.test_plan.models.TestCaseAssociatedResult>`
    :param test_case_name: Test Case Name to be displayed in the table header
    :type test_case_name: str
    """

    _attribute_map = {
        'context_point': {'key': 'contextPoint', 'type': 'TestPointDetailedReference'},
        'results': {'key': 'results', 'type': '[TestCaseAssociatedResult]'},
        'test_case_name': {'key': 'testCaseName', 'type': 'str'}
    }

    def __init__(self, context_point=None, results=None, test_case_name=None):
        super(TestCaseResultsData, self).__init__()
        self.context_point = context_point
        self.results = results
        self.test_case_name = test_case_name


class TestConfigurationCreateUpdateParameters(Model):
    """
    Test Configuration Create or Update Parameters

    :param description: Description of the configuration
    :type description: str
    :param is_default: Is the configuration a default for the test plans
    :type is_default: bool
    :param name: Name of the configuration
    :type name: str
    :param state: State of the configuration
    :type state: object
    :param values: Dictionary of Test Variable, Selected Value
    :type values: list of :class:`NameValuePair <azure.devops.v7_1.test_plan.models.NameValuePair>`
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'is_default': {'key': 'isDefault', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'state': {'key': 'state', 'type': 'object'},
        'values': {'key': 'values', 'type': '[NameValuePair]'}
    }

    def __init__(self, description=None, is_default=None, name=None, state=None, values=None):
        super(TestConfigurationCreateUpdateParameters, self).__init__()
        self.description = description
        self.is_default = is_default
        self.name = name
        self.state = state
        self.values = values


class TestConfigurationReference(Model):
    """
    Test Configuration Reference

    :param id: Id of the configuration
    :type id: int
    :param name: Name of the configuration
    :type name: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, id=None, name=None):
        super(TestConfigurationReference, self).__init__()
        self.id = id
        self.name = name


class TestEntityCount(Model):
    """
    Test Entity Count Used to store test cases count (define tab) and test point count (execute tab) Used to store test cases count (define tab) and test point count (execute tab)

    :param count: Test Entity Count
    :type count: int
    :param test_plan_id: Test Plan under which the Test Entities are
    :type test_plan_id: int
    :param test_suite_id: Test Suite under which the Test Entities are
    :type test_suite_id: int
    :param total_count: Total test entities in the suite without the applied filters
    :type total_count: int
    """

    _attribute_map = {
        'count': {'key': 'count', 'type': 'int'},
        'test_plan_id': {'key': 'testPlanId', 'type': 'int'},
        'test_suite_id': {'key': 'testSuiteId', 'type': 'int'},
        'total_count': {'key': 'totalCount', 'type': 'int'}
    }

    def __init__(self, count=None, test_plan_id=None, test_suite_id=None, total_count=None):
        super(TestEntityCount, self).__init__()
        self.count = count
        self.test_plan_id = test_plan_id
        self.test_suite_id = test_suite_id
        self.total_count = total_count


class TestEnvironment(Model):
    """
    Test environment Detail.

    :param environment_id: Test Environment Id.
    :type environment_id: str
    :param environment_name: Test Environment Name.
    :type environment_name: str
    """

    _attribute_map = {
        'environment_id': {'key': 'environmentId', 'type': 'str'},
        'environment_name': {'key': 'environmentName', 'type': 'str'}
    }

    def __init__(self, environment_id=None, environment_name=None):
        super(TestEnvironment, self).__init__()
        self.environment_id = environment_id
        self.environment_name = environment_name


class TestOutcomeSettings(Model):
    """
    Test outcome settings

    :param sync_outcome_across_suites: Value to configure how test outcomes for the same tests across suites are shown
    :type sync_outcome_across_suites: bool
    """

    _attribute_map = {
        'sync_outcome_across_suites': {'key': 'syncOutcomeAcrossSuites', 'type': 'bool'}
    }

    def __init__(self, sync_outcome_across_suites=None):
        super(TestOutcomeSettings, self).__init__()
        self.sync_outcome_across_suites = sync_outcome_across_suites


class TestPlanCreateParams(Model):
    """
    The test plan create parameters.

    :param area_path: Area of the test plan.
    :type area_path: str
    :param automated_test_environment:
    :type automated_test_environment: :class:`TestEnvironment <azure.devops.v7_1.test_plan.models.TestEnvironment>`
    :param automated_test_settings:
    :type automated_test_settings: :class:`TestSettings <azure.devops.v7_1.test_plan.models.TestSettings>`
    :param build_definition: The Build Definition that generates a build associated with this test plan.
    :type build_definition: :class:`BuildDefinitionReference <azure.devops.v7_1.test_plan.models.BuildDefinitionReference>`
    :param build_id: Build to be tested.
    :type build_id: int
    :param description: Description of the test plan.
    :type description: str
    :param end_date: End date for the test plan.
    :type end_date: datetime
    :param iteration: Iteration path of the test plan.
    :type iteration: str
    :param manual_test_environment:
    :type manual_test_environment: :class:`TestEnvironment <azure.devops.v7_1.test_plan.models.TestEnvironment>`
    :param manual_test_settings:
    :type manual_test_settings: :class:`TestSettings <azure.devops.v7_1.test_plan.models.TestSettings>`
    :param name: Name of the test plan.
    :type name: str
    :param owner: Owner of the test plan.
    :type owner: :class:`IdentityRef <azure.devops.v7_1.test_plan.models.IdentityRef>`
    :param release_environment_definition: Release Environment to be used to deploy the build and run automated tests from this test plan.
    :type release_environment_definition: :class:`ReleaseEnvironmentDefinitionReference <azure.devops.v7_1.test_plan.models.ReleaseEnvironmentDefinitionReference>`
    :param start_date: Start date for the test plan.
    :type start_date: datetime
    :param state: State of the test plan.
    :type state: str
    :param test_outcome_settings: Value to configure how same tests across test suites under a test plan need to behave
    :type test_outcome_settings: :class:`TestOutcomeSettings <azure.devops.v7_1.test_plan.models.TestOutcomeSettings>`
    """

    _attribute_map = {
        'area_path': {'key': 'areaPath', 'type': 'str'},
        'automated_test_environment': {'key': 'automatedTestEnvironment', 'type': 'TestEnvironment'},
        'automated_test_settings': {'key': 'automatedTestSettings', 'type': 'TestSettings'},
        'build_definition': {'key': 'buildDefinition', 'type': 'BuildDefinitionReference'},
        'build_id': {'key': 'buildId', 'type': 'int'},
        'description': {'key': 'description', 'type': 'str'},
        'end_date': {'key': 'endDate', 'type': 'iso-8601'},
        'iteration': {'key': 'iteration', 'type': 'str'},
        'manual_test_environment': {'key': 'manualTestEnvironment', 'type': 'TestEnvironment'},
        'manual_test_settings': {'key': 'manualTestSettings', 'type': 'TestSettings'},
        'name': {'key': 'name', 'type': 'str'},
        'owner': {'key': 'owner', 'type': 'IdentityRef'},
        'release_environment_definition': {'key': 'releaseEnvironmentDefinition', 'type': 'ReleaseEnvironmentDefinitionReference'},
        'start_date': {'key': 'startDate', 'type': 'iso-8601'},
        'state': {'key': 'state', 'type': 'str'},
        'test_outcome_settings': {'key': 'testOutcomeSettings', 'type': 'TestOutcomeSettings'}
    }

    def __init__(self, area_path=None, automated_test_environment=None, automated_test_settings=None, build_definition=None, build_id=None, description=None, end_date=None, iteration=None, manual_test_environment=None, manual_test_settings=None, name=None, owner=None, release_environment_definition=None, start_date=None, state=None, test_outcome_settings=None):
        super(TestPlanCreateParams, self).__init__()
        self.area_path = area_path
        self.automated_test_environment = automated_test_environment
        self.automated_test_settings = automated_test_settings
        self.build_definition = build_definition
        self.build_id = build_id
        self.description = description
        self.end_date = end_date
        self.iteration = iteration
        self.manual_test_environment = manual_test_environment
        self.manual_test_settings = manual_test_settings
        self.name = name
        self.owner = owner
        self.release_environment_definition = release_environment_definition
        self.start_date = start_date
        self.state = state
        self.test_outcome_settings = test_outcome_settings


class TestPlanReference(Model):
    """
    The test plan reference resource.

    :param id: ID of the test plan.
    :type id: int
    :param name: Name of the test plan.
    :type name: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, id=None, name=None):
        super(TestPlanReference, self).__init__()
        self.id = id
        self.name = name


class TestPlansHubRefreshData(Model):
    """
    This data model is used in TestPlansHubRefreshDataProvider and populates the data required for initial page load

    :param define_column_option_fields:
    :type define_column_option_fields: list of str
    :param define_tab_custom_column_field_map:
    :type define_tab_custom_column_field_map: dict
    :param error_message:
    :type error_message: str
    :param execute_column_option_fields:
    :type execute_column_option_fields: list of str
    :param execute_tab_custom_column_field_map:
    :type execute_tab_custom_column_field_map: dict
    :param is_advanced_extension_enabled:
    :type is_advanced_extension_enabled: bool
    :param selected_pivot_id:
    :type selected_pivot_id: str
    :param selected_suite_id:
    :type selected_suite_id: int
    :param test_case_page_size:
    :type test_case_page_size: int
    :param test_cases:
    :type test_cases: list of :class:`TestCase <azure.devops.v7_1.test_plan.models.TestCase>`
    :param test_cases_continuation_token:
    :type test_cases_continuation_token: str
    :param test_plan:
    :type test_plan: :class:`TestPlanDetailedReference <azure.devops.v7_1.test_plan.models.TestPlanDetailedReference>`
    :param test_point_page_size:
    :type test_point_page_size: int
    :param test_points:
    :type test_points: list of :class:`TestPoint <azure.devops.v7_1.test_plan.models.TestPoint>`
    :param test_points_continuation_token:
    :type test_points_continuation_token: str
    :param test_suites:
    :type test_suites: list of :class:`TestSuite <azure.devops.v7_1.test_plan.models.TestSuite>`
    :param test_suites_continuation_token:
    :type test_suites_continuation_token: str
    """

    _attribute_map = {
        'define_column_option_fields': {'key': 'defineColumnOptionFields', 'type': '[str]'},
        'define_tab_custom_column_field_map': {'key': 'defineTabCustomColumnFieldMap', 'type': '{str}'},
        'error_message': {'key': 'errorMessage', 'type': 'str'},
        'execute_column_option_fields': {'key': 'executeColumnOptionFields', 'type': '[str]'},
        'execute_tab_custom_column_field_map': {'key': 'executeTabCustomColumnFieldMap', 'type': '{str}'},
        'is_advanced_extension_enabled': {'key': 'isAdvancedExtensionEnabled', 'type': 'bool'},
        'selected_pivot_id': {'key': 'selectedPivotId', 'type': 'str'},
        'selected_suite_id': {'key': 'selectedSuiteId', 'type': 'int'},
        'test_case_page_size': {'key': 'testCasePageSize', 'type': 'int'},
        'test_cases': {'key': 'testCases', 'type': '[TestCase]'},
        'test_cases_continuation_token': {'key': 'testCasesContinuationToken', 'type': 'str'},
        'test_plan': {'key': 'testPlan', 'type': 'TestPlanDetailedReference'},
        'test_point_page_size': {'key': 'testPointPageSize', 'type': 'int'},
        'test_points': {'key': 'testPoints', 'type': '[TestPoint]'},
        'test_points_continuation_token': {'key': 'testPointsContinuationToken', 'type': 'str'},
        'test_suites': {'key': 'testSuites', 'type': '[TestSuite]'},
        'test_suites_continuation_token': {'key': 'testSuitesContinuationToken', 'type': 'str'}
    }

    def __init__(self, define_column_option_fields=None, define_tab_custom_column_field_map=None, error_message=None, execute_column_option_fields=None, execute_tab_custom_column_field_map=None, is_advanced_extension_enabled=None, selected_pivot_id=None, selected_suite_id=None, test_case_page_size=None, test_cases=None, test_cases_continuation_token=None, test_plan=None, test_point_page_size=None, test_points=None, test_points_continuation_token=None, test_suites=None, test_suites_continuation_token=None):
        super(TestPlansHubRefreshData, self).__init__()
        self.define_column_option_fields = define_column_option_fields
        self.define_tab_custom_column_field_map = define_tab_custom_column_field_map
        self.error_message = error_message
        self.execute_column_option_fields = execute_column_option_fields
        self.execute_tab_custom_column_field_map = execute_tab_custom_column_field_map
        self.is_advanced_extension_enabled = is_advanced_extension_enabled
        self.selected_pivot_id = selected_pivot_id
        self.selected_suite_id = selected_suite_id
        self.test_case_page_size = test_case_page_size
        self.test_cases = test_cases
        self.test_cases_continuation_token = test_cases_continuation_token
        self.test_plan = test_plan
        self.test_point_page_size = test_point_page_size
        self.test_points = test_points
        self.test_points_continuation_token = test_points_continuation_token
        self.test_suites = test_suites
        self.test_suites_continuation_token = test_suites_continuation_token


class TestPlansLibraryWorkItemFilter(Model):
    """
    Container to hold information about a filter being applied in Test Plans Library.

    :param field_name: Work item field name on which the items are to be filtered.
    :type field_name: str
    :param field_values: Work item field values corresponding to the field name.
    :type field_values: list of str
    :param filter_mode: Mode of the filter.
    :type filter_mode: object
    """

    _attribute_map = {
        'field_name': {'key': 'fieldName', 'type': 'str'},
        'field_values': {'key': 'fieldValues', 'type': '[str]'},
        'filter_mode': {'key': 'filterMode', 'type': 'object'}
    }

    def __init__(self, field_name=None, field_values=None, filter_mode=None):
        super(TestPlansLibraryWorkItemFilter, self).__init__()
        self.field_name = field_name
        self.field_values = field_values
        self.filter_mode = filter_mode


class TestPlanUpdateParams(TestPlanCreateParams):
    """
    The test plan update parameters.

    :param area_path: Area of the test plan.
    :type area_path: str
    :param automated_test_environment:
    :type automated_test_environment: :class:`TestEnvironment <azure.devops.v7_1.test_plan.models.TestEnvironment>`
    :param automated_test_settings:
    :type automated_test_settings: :class:`TestSettings <azure.devops.v7_1.test_plan.models.TestSettings>`
    :param build_definition: The Build Definition that generates a build associated with this test plan.
    :type build_definition: :class:`BuildDefinitionReference <azure.devops.v7_1.test_plan.models.BuildDefinitionReference>`
    :param build_id: Build to be tested.
    :type build_id: int
    :param description: Description of the test plan.
    :type description: str
    :param end_date: End date for the test plan.
    :type end_date: datetime
    :param iteration: Iteration path of the test plan.
    :type iteration: str
    :param manual_test_environment:
    :type manual_test_environment: :class:`TestEnvironment <azure.devops.v7_1.test_plan.models.TestEnvironment>`
    :param manual_test_settings:
    :type manual_test_settings: :class:`TestSettings <azure.devops.v7_1.test_plan.models.TestSettings>`
    :param name: Name of the test plan.
    :type name: str
    :param owner: Owner of the test plan.
    :type owner: :class:`IdentityRef <azure.devops.v7_1.test_plan.models.IdentityRef>`
    :param release_environment_definition: Release Environment to be used to deploy the build and run automated tests from this test plan.
    :type release_environment_definition: :class:`ReleaseEnvironmentDefinitionReference <azure.devops.v7_1.test_plan.models.ReleaseEnvironmentDefinitionReference>`
    :param start_date: Start date for the test plan.
    :type start_date: datetime
    :param state: State of the test plan.
    :type state: str
    :param test_outcome_settings: Value to configure how same tests across test suites under a test plan need to behave
    :type test_outcome_settings: :class:`TestOutcomeSettings <azure.devops.v7_1.test_plan.models.TestOutcomeSettings>`
    :param revision: Revision of the test plan.
    :type revision: int
    """

    _attribute_map = {
        'area_path': {'key': 'areaPath', 'type': 'str'},
        'automated_test_environment': {'key': 'automatedTestEnvironment', 'type': 'TestEnvironment'},
        'automated_test_settings': {'key': 'automatedTestSettings', 'type': 'TestSettings'},
        'build_definition': {'key': 'buildDefinition', 'type': 'BuildDefinitionReference'},
        'build_id': {'key': 'buildId', 'type': 'int'},
        'description': {'key': 'description', 'type': 'str'},
        'end_date': {'key': 'endDate', 'type': 'iso-8601'},
        'iteration': {'key': 'iteration', 'type': 'str'},
        'manual_test_environment': {'key': 'manualTestEnvironment', 'type': 'TestEnvironment'},
        'manual_test_settings': {'key': 'manualTestSettings', 'type': 'TestSettings'},
        'name': {'key': 'name', 'type': 'str'},
        'owner': {'key': 'owner', 'type': 'IdentityRef'},
        'release_environment_definition': {'key': 'releaseEnvironmentDefinition', 'type': 'ReleaseEnvironmentDefinitionReference'},
        'start_date': {'key': 'startDate', 'type': 'iso-8601'},
        'state': {'key': 'state', 'type': 'str'},
        'test_outcome_settings': {'key': 'testOutcomeSettings', 'type': 'TestOutcomeSettings'},
        'revision': {'key': 'revision', 'type': 'int'}
    }

    def __init__(self, area_path=None, automated_test_environment=None, automated_test_settings=None, build_definition=None, build_id=None, description=None, end_date=None, iteration=None, manual_test_environment=None, manual_test_settings=None, name=None, owner=None, release_environment_definition=None, start_date=None, state=None, test_outcome_settings=None, revision=None):
        super(TestPlanUpdateParams, self).__init__(area_path=area_path, automated_test_environment=automated_test_environment, automated_test_settings=automated_test_settings, build_definition=build_definition, build_id=build_id, description=description, end_date=end_date, iteration=iteration, manual_test_environment=manual_test_environment, manual_test_settings=manual_test_settings, name=name, owner=owner, release_environment_definition=release_environment_definition, start_date=start_date, state=state, test_outcome_settings=test_outcome_settings)
        self.revision = revision


class TestPoint(Model):
    """
    Test Point Class

    :param comment: Comment associated to the Test Point
    :type comment: str
    :param configuration: Configuration associated with the Test Point
    :type configuration: :class:`TestConfigurationReference <azure.devops.v7_1.test_plan.models.TestConfigurationReference>`
    :param id: Id of the Test Point
    :type id: int
    :param is_active: Variable to decide whether the test case is Active or not
    :type is_active: bool
    :param is_automated: Is the Test Point for Automated Test Case or Manual
    :type is_automated: bool
    :param last_reset_to_active: Last Reset to Active Time Stamp for the Test Point
    :type last_reset_to_active: datetime
    :param last_updated_by: Last Updated details for the Test Point
    :type last_updated_by: :class:`IdentityRef <azure.devops.v7_1.test_plan.models.IdentityRef>`
    :param last_updated_date: Last Update Time Stamp for the Test Point
    :type last_updated_date: datetime
    :param links: Reference links
    :type links: :class:`ReferenceLinks <azure.devops.v7_1.test_plan.models.ReferenceLinks>`
    :param project: Project under which the Test Point is
    :type project: :class:`TeamProjectReference <azure.devops.v7_1.test_plan.models.TeamProjectReference>`
    :param results: Results associated to the Test Point
    :type results: :class:`TestPointResults <azure.devops.v7_1.test_plan.models.TestPointResults>`
    :param test_case_reference: Test Case Reference
    :type test_case_reference: :class:`TestCaseReference <azure.devops.v7_1.test_plan.models.TestCaseReference>`
    :param tester: Tester associated with the Test Point
    :type tester: :class:`IdentityRef <azure.devops.v7_1.test_plan.models.IdentityRef>`
    :param test_plan: Test Plan under which the Test Point is
    :type test_plan: :class:`TestPlanReference <azure.devops.v7_1.test_plan.models.TestPlanReference>`
    :param test_suite: Test Suite under which the Test Point is
    :type test_suite: :class:`TestSuiteReference <azure.devops.v7_1.test_plan.models.TestSuiteReference>`
    """

    _attribute_map = {
        'comment': {'key': 'comment', 'type': 'str'},
        'configuration': {'key': 'configuration', 'type': 'TestConfigurationReference'},
        'id': {'key': 'id', 'type': 'int'},
        'is_active': {'key': 'isActive', 'type': 'bool'},
        'is_automated': {'key': 'isAutomated', 'type': 'bool'},
        'last_reset_to_active': {'key': 'lastResetToActive', 'type': 'iso-8601'},
        'last_updated_by': {'key': 'lastUpdatedBy', 'type': 'IdentityRef'},
        'last_updated_date': {'key': 'lastUpdatedDate', 'type': 'iso-8601'},
        'links': {'key': 'links', 'type': 'ReferenceLinks'},
        'project': {'key': 'project', 'type': 'TeamProjectReference'},
        'results': {'key': 'results', 'type': 'TestPointResults'},
        'test_case_reference': {'key': 'testCaseReference', 'type': 'TestCaseReference'},
        'tester': {'key': 'tester', 'type': 'IdentityRef'},
        'test_plan': {'key': 'testPlan', 'type': 'TestPlanReference'},
        'test_suite': {'key': 'testSuite', 'type': 'TestSuiteReference'}
    }

    def __init__(self, comment=None, configuration=None, id=None, is_active=None, is_automated=None, last_reset_to_active=None, last_updated_by=None, last_updated_date=None, links=None, project=None, results=None, test_case_reference=None, tester=None, test_plan=None, test_suite=None):
        super(TestPoint, self).__init__()
        self.comment = comment
        self.configuration = configuration
        self.id = id
        self.is_active = is_active
        self.is_automated = is_automated
        self.last_reset_to_active = last_reset_to_active
        self.last_updated_by = last_updated_by
        self.last_updated_date = last_updated_date
        self.links = links
        self.project = project
        self.results = results
        self.test_case_reference = test_case_reference
        self.tester = tester
        self.test_plan = test_plan
        self.test_suite = test_suite


class TestPointDetailedReference(Model):
    """
    :param configuration:
    :type configuration: :class:`TestConfigurationReference <azure.devops.v7_1.test_plan.models.TestConfigurationReference>`
    :param plan:
    :type plan: :class:`TestPlanReference <azure.devops.v7_1.test_plan.models.TestPlanReference>`
    :param point_id:
    :type point_id: int
    :param suite:
    :type suite: :class:`TestSuiteReference <azure.devops.v7_1.test_plan.models.TestSuiteReference>`
    :param tester:
    :type tester: :class:`IdentityRef <azure.devops.v7_1.test_plan.models.IdentityRef>`
    """

    _attribute_map = {
        'configuration': {'key': 'configuration', 'type': 'TestConfigurationReference'},
        'plan': {'key': 'plan', 'type': 'TestPlanReference'},
        'point_id': {'key': 'pointId', 'type': 'int'},
        'suite': {'key': 'suite', 'type': 'TestSuiteReference'},
        'tester': {'key': 'tester', 'type': 'IdentityRef'}
    }

    def __init__(self, configuration=None, plan=None, point_id=None, suite=None, tester=None):
        super(TestPointDetailedReference, self).__init__()
        self.configuration = configuration
        self.plan = plan
        self.point_id = point_id
        self.suite = suite
        self.tester = tester


class TestPointResults(Model):
    """
    Test Point Results

    :param failure_type: Failure Type for the Test Point
    :type failure_type: object
    :param last_resolution_state: Last Resolution State Id for the Test Point
    :type last_resolution_state: object
    :param last_result_details: Last Result Details for the Test Point
    :type last_result_details: :class:`LastResultDetails <azure.devops.v7_1.test_plan.models.LastResultDetails>`
    :param last_result_id: Last Result Id
    :type last_result_id: int
    :param last_result_state: Last Result State of the Test Point
    :type last_result_state: object
    :param last_run_build_number: Last RUn Build Number for the Test Point
    :type last_run_build_number: str
    :param last_test_run_id: Last Test Run Id for the Test Point
    :type last_test_run_id: int
    :param outcome: Outcome of the Test Point
    :type outcome: object
    :param state: State of the Test Point
    :type state: object
    """

    _attribute_map = {
        'failure_type': {'key': 'failureType', 'type': 'object'},
        'last_resolution_state': {'key': 'lastResolutionState', 'type': 'object'},
        'last_result_details': {'key': 'lastResultDetails', 'type': 'LastResultDetails'},
        'last_result_id': {'key': 'lastResultId', 'type': 'int'},
        'last_result_state': {'key': 'lastResultState', 'type': 'object'},
        'last_run_build_number': {'key': 'lastRunBuildNumber', 'type': 'str'},
        'last_test_run_id': {'key': 'lastTestRunId', 'type': 'int'},
        'outcome': {'key': 'outcome', 'type': 'object'},
        'state': {'key': 'state', 'type': 'object'}
    }

    def __init__(self, failure_type=None, last_resolution_state=None, last_result_details=None, last_result_id=None, last_result_state=None, last_run_build_number=None, last_test_run_id=None, outcome=None, state=None):
        super(TestPointResults, self).__init__()
        self.failure_type = failure_type
        self.last_resolution_state = last_resolution_state
        self.last_result_details = last_result_details
        self.last_result_id = last_result_id
        self.last_result_state = last_result_state
        self.last_run_build_number = last_run_build_number
        self.last_test_run_id = last_test_run_id
        self.outcome = outcome
        self.state = state


class TestPointUpdateParams(Model):
    """
    Test Point Update Parameters

    :param id: Id of Test Point to be updated
    :type id: int
    :param is_active: Reset the Test Point to Active
    :type is_active: bool
    :param results: Results of the test point
    :type results: :class:`Results <azure.devops.v7_1.test_plan.models.Results>`
    :param tester: Tester of the Test Point
    :type tester: :class:`IdentityRef <azure.devops.v7_1.test_plan.models.IdentityRef>`
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'is_active': {'key': 'isActive', 'type': 'bool'},
        'results': {'key': 'results', 'type': 'Results'},
        'tester': {'key': 'tester', 'type': 'IdentityRef'}
    }

    def __init__(self, id=None, is_active=None, results=None, tester=None):
        super(TestPointUpdateParams, self).__init__()
        self.id = id
        self.is_active = is_active
        self.results = results
        self.tester = tester


class TestSettings(Model):
    """
    Represents the test settings of the run. Used to create test settings and fetch test settings

    :param area_path: Area path required to create test settings
    :type area_path: str
    :param description: Description of the test settings. Used in create test settings.
    :type description: str
    :param is_public: Indicates if the tests settings is public or private.Used in create test settings.
    :type is_public: bool
    :param machine_roles: Xml string of machine roles. Used in create test settings.
    :type machine_roles: str
    :param test_settings_content: Test settings content.
    :type test_settings_content: str
    :param test_settings_id: Test settings id.
    :type test_settings_id: int
    :param test_settings_name: Test settings name.
    :type test_settings_name: str
    """

    _attribute_map = {
        'area_path': {'key': 'areaPath', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'is_public': {'key': 'isPublic', 'type': 'bool'},
        'machine_roles': {'key': 'machineRoles', 'type': 'str'},
        'test_settings_content': {'key': 'testSettingsContent', 'type': 'str'},
        'test_settings_id': {'key': 'testSettingsId', 'type': 'int'},
        'test_settings_name': {'key': 'testSettingsName', 'type': 'str'}
    }

    def __init__(self, area_path=None, description=None, is_public=None, machine_roles=None, test_settings_content=None, test_settings_id=None, test_settings_name=None):
        super(TestSettings, self).__init__()
        self.area_path = area_path
        self.description = description
        self.is_public = is_public
        self.machine_roles = machine_roles
        self.test_settings_content = test_settings_content
        self.test_settings_id = test_settings_id
        self.test_settings_name = test_settings_name


class TestSuiteCreateUpdateCommonParams(Model):
    """
    Test Suite Create/Update Common Parameters

    :param default_configurations: Test suite default configurations.
    :type default_configurations: list of :class:`TestConfigurationReference <azure.devops.v7_1.test_plan.models.TestConfigurationReference>`
    :param default_testers: Test suite default testers.
    :type default_testers: list of :class:`IdentityRef <azure.devops.v7_1.test_plan.models.IdentityRef>`
    :param inherit_default_configurations: Default configuration was inherited or not.
    :type inherit_default_configurations: bool
    :param name: Name of test suite.
    :type name: str
    :param parent_suite: Test suite parent shallow reference.
    :type parent_suite: :class:`TestSuiteReference <azure.devops.v7_1.test_plan.models.TestSuiteReference>`
    :param query_string: Test suite query string, for dynamic suites.
    :type query_string: str
    """

    _attribute_map = {
        'default_configurations': {'key': 'defaultConfigurations', 'type': '[TestConfigurationReference]'},
        'default_testers': {'key': 'defaultTesters', 'type': '[IdentityRef]'},
        'inherit_default_configurations': {'key': 'inheritDefaultConfigurations', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'parent_suite': {'key': 'parentSuite', 'type': 'TestSuiteReference'},
        'query_string': {'key': 'queryString', 'type': 'str'}
    }

    def __init__(self, default_configurations=None, default_testers=None, inherit_default_configurations=None, name=None, parent_suite=None, query_string=None):
        super(TestSuiteCreateUpdateCommonParams, self).__init__()
        self.default_configurations = default_configurations
        self.default_testers = default_testers
        self.inherit_default_configurations = inherit_default_configurations
        self.name = name
        self.parent_suite = parent_suite
        self.query_string = query_string


class TestSuiteReference(Model):
    """
    The test suite reference resource.

    :param id: ID of the test suite.
    :type id: int
    :param name: Name of the test suite.
    :type name: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, id=None, name=None):
        super(TestSuiteReference, self).__init__()
        self.id = id
        self.name = name


class TestSuiteReferenceWithProject(TestSuiteReference):
    """
    Test Suite Reference with Project

    :param id: ID of the test suite.
    :type id: int
    :param name: Name of the test suite.
    :type name: str
    :param project: Reference of destination Project
    :type project: :class:`TeamProjectReference <azure.devops.v7_1.test_plan.models.TeamProjectReference>`
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'project': {'key': 'project', 'type': 'TeamProjectReference'}
    }

    def __init__(self, id=None, name=None, project=None):
        super(TestSuiteReferenceWithProject, self).__init__(id=id, name=name)
        self.project = project


class TestSuiteUpdateParams(TestSuiteCreateUpdateCommonParams):
    """
    Test Suite Update Parameters

    :param default_configurations: Test suite default configurations.
    :type default_configurations: list of :class:`TestConfigurationReference <azure.devops.v7_1.test_plan.models.TestConfigurationReference>`
    :param default_testers: Test suite default testers.
    :type default_testers: list of :class:`IdentityRef <azure.devops.v7_1.test_plan.models.IdentityRef>`
    :param inherit_default_configurations: Default configuration was inherited or not.
    :type inherit_default_configurations: bool
    :param name: Name of test suite.
    :type name: str
    :param parent_suite: Test suite parent shallow reference.
    :type parent_suite: :class:`TestSuiteReference <azure.devops.v7_1.test_plan.models.TestSuiteReference>`
    :param query_string: Test suite query string, for dynamic suites.
    :type query_string: str
    :param revision: Test suite revision.
    :type revision: int
    """

    _attribute_map = {
        'default_configurations': {'key': 'defaultConfigurations', 'type': '[TestConfigurationReference]'},
        'default_testers': {'key': 'defaultTesters', 'type': '[IdentityRef]'},
        'inherit_default_configurations': {'key': 'inheritDefaultConfigurations', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'parent_suite': {'key': 'parentSuite', 'type': 'TestSuiteReference'},
        'query_string': {'key': 'queryString', 'type': 'str'},
        'revision': {'key': 'revision', 'type': 'int'}
    }

    def __init__(self, default_configurations=None, default_testers=None, inherit_default_configurations=None, name=None, parent_suite=None, query_string=None, revision=None):
        super(TestSuiteUpdateParams, self).__init__(default_configurations=default_configurations, default_testers=default_testers, inherit_default_configurations=inherit_default_configurations, name=name, parent_suite=parent_suite, query_string=query_string)
        self.revision = revision


class TestVariableCreateUpdateParameters(Model):
    """
    Test Variable Create or Update Parameters

    :param description: Description of the test variable
    :type description: str
    :param name: Name of the test variable
    :type name: str
    :param values: List of allowed values
    :type values: list of str
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'values': {'key': 'values', 'type': '[str]'}
    }

    def __init__(self, description=None, name=None, values=None):
        super(TestVariableCreateUpdateParameters, self).__init__()
        self.description = description
        self.name = name
        self.values = values


class WorkItem(Model):
    """
    Work Item

    :param id: Id of the Work Item
    :type id: int
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'}
    }

    def __init__(self, id=None):
        super(WorkItem, self).__init__()
        self.id = id


class WorkItemDetails(Model):
    """
    Work Item Class

    :param id: Work Item Id
    :type id: int
    :param name: Work Item Name
    :type name: str
    :param work_item_fields: Work Item Fields
    :type work_item_fields: list of object
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'work_item_fields': {'key': 'workItemFields', 'type': '[object]'}
    }

    def __init__(self, id=None, name=None, work_item_fields=None):
        super(WorkItemDetails, self).__init__()
        self.id = id
        self.name = name
        self.work_item_fields = work_item_fields


class DestinationTestPlanCloneParams(TestPlanCreateParams):
    """
    Destination Test Plan create parameters

    :param area_path: Area of the test plan.
    :type area_path: str
    :param automated_test_environment:
    :type automated_test_environment: :class:`TestEnvironment <azure.devops.v7_1.test_plan.models.TestEnvironment>`
    :param automated_test_settings:
    :type automated_test_settings: :class:`TestSettings <azure.devops.v7_1.test_plan.models.TestSettings>`
    :param build_definition: The Build Definition that generates a build associated with this test plan.
    :type build_definition: :class:`BuildDefinitionReference <azure.devops.v7_1.test_plan.models.BuildDefinitionReference>`
    :param build_id: Build to be tested.
    :type build_id: int
    :param description: Description of the test plan.
    :type description: str
    :param end_date: End date for the test plan.
    :type end_date: datetime
    :param iteration: Iteration path of the test plan.
    :type iteration: str
    :param manual_test_environment:
    :type manual_test_environment: :class:`TestEnvironment <azure.devops.v7_1.test_plan.models.TestEnvironment>`
    :param manual_test_settings:
    :type manual_test_settings: :class:`TestSettings <azure.devops.v7_1.test_plan.models.TestSettings>`
    :param name: Name of the test plan.
    :type name: str
    :param owner: Owner of the test plan.
    :type owner: :class:`IdentityRef <azure.devops.v7_1.test_plan.models.IdentityRef>`
    :param release_environment_definition: Release Environment to be used to deploy the build and run automated tests from this test plan.
    :type release_environment_definition: :class:`ReleaseEnvironmentDefinitionReference <azure.devops.v7_1.test_plan.models.ReleaseEnvironmentDefinitionReference>`
    :param start_date: Start date for the test plan.
    :type start_date: datetime
    :param state: State of the test plan.
    :type state: str
    :param test_outcome_settings: Value to configure how same tests across test suites under a test plan need to behave
    :type test_outcome_settings: :class:`TestOutcomeSettings <azure.devops.v7_1.test_plan.models.TestOutcomeSettings>`
    :param project: Destination Project Name
    :type project: str
    """

    _attribute_map = {
        'area_path': {'key': 'areaPath', 'type': 'str'},
        'automated_test_environment': {'key': 'automatedTestEnvironment', 'type': 'TestEnvironment'},
        'automated_test_settings': {'key': 'automatedTestSettings', 'type': 'TestSettings'},
        'build_definition': {'key': 'buildDefinition', 'type': 'BuildDefinitionReference'},
        'build_id': {'key': 'buildId', 'type': 'int'},
        'description': {'key': 'description', 'type': 'str'},
        'end_date': {'key': 'endDate', 'type': 'iso-8601'},
        'iteration': {'key': 'iteration', 'type': 'str'},
        'manual_test_environment': {'key': 'manualTestEnvironment', 'type': 'TestEnvironment'},
        'manual_test_settings': {'key': 'manualTestSettings', 'type': 'TestSettings'},
        'name': {'key': 'name', 'type': 'str'},
        'owner': {'key': 'owner', 'type': 'IdentityRef'},
        'release_environment_definition': {'key': 'releaseEnvironmentDefinition', 'type': 'ReleaseEnvironmentDefinitionReference'},
        'start_date': {'key': 'startDate', 'type': 'iso-8601'},
        'state': {'key': 'state', 'type': 'str'},
        'test_outcome_settings': {'key': 'testOutcomeSettings', 'type': 'TestOutcomeSettings'},
        'project': {'key': 'project', 'type': 'str'}
    }

    def __init__(self, area_path=None, automated_test_environment=None, automated_test_settings=None, build_definition=None, build_id=None, description=None, end_date=None, iteration=None, manual_test_environment=None, manual_test_settings=None, name=None, owner=None, release_environment_definition=None, start_date=None, state=None, test_outcome_settings=None, project=None):
        super(DestinationTestPlanCloneParams, self).__init__(area_path=area_path, automated_test_environment=automated_test_environment, automated_test_settings=automated_test_settings, build_definition=build_definition, build_id=build_id, description=description, end_date=end_date, iteration=iteration, manual_test_environment=manual_test_environment, manual_test_settings=manual_test_settings, name=name, owner=owner, release_environment_definition=release_environment_definition, start_date=start_date, state=state, test_outcome_settings=test_outcome_settings)
        self.project = project


class SourceTestplanResponse(TestPlanReference):
    """
    Source Test Plan Response for Test Plan clone operation

    :param id: ID of the test plan.
    :type id: int
    :param name: Name of the test plan.
    :type name: str
    :param project: project reference
    :type project: :class:`TeamProjectReference <azure.devops.v7_1.test_plan.models.TeamProjectReference>`
    :param suite_ids: Id of suites to be cloned inside source Test Plan
    :type suite_ids: list of int
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'project': {'key': 'project', 'type': 'TeamProjectReference'},
        'suite_ids': {'key': 'suiteIds', 'type': '[int]'}
    }

    def __init__(self, id=None, name=None, project=None, suite_ids=None):
        super(SourceTestplanResponse, self).__init__(id=id, name=name)
        self.project = project
        self.suite_ids = suite_ids


class SourceTestSuiteResponse(TestSuiteReference):
    """
    Source Test Suite Response for Test Case clone operation

    :param id: ID of the test suite.
    :type id: int
    :param name: Name of the test suite.
    :type name: str
    :param project: project reference
    :type project: :class:`TeamProjectReference <azure.devops.v7_1.test_plan.models.TeamProjectReference>`
    :param test_case_ids: Id of suites to be cloned inside source Test Plan
    :type test_case_ids: list of int
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'project': {'key': 'project', 'type': 'TeamProjectReference'},
        'test_case_ids': {'key': 'testCaseIds', 'type': '[int]'}
    }

    def __init__(self, id=None, name=None, project=None, test_case_ids=None):
        super(SourceTestSuiteResponse, self).__init__(id=id, name=name)
        self.project = project
        self.test_case_ids = test_case_ids


class SuiteEntry(SuiteEntryUpdateParams):
    """
    A suite entry defines properties for a test suite.

    :param id: Id of the suite entry in the test suite: either a test case id or child suite id.
    :type id: int
    :param sequence_number: Sequence number for the suite entry object in the test suite.
    :type sequence_number: int
    :param suite_entry_type: Defines whether the entry is of type test case or suite.
    :type suite_entry_type: object
    :param suite_id: Id for the test suite.
    :type suite_id: int
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'sequence_number': {'key': 'sequenceNumber', 'type': 'int'},
        'suite_entry_type': {'key': 'suiteEntryType', 'type': 'object'},
        'suite_id': {'key': 'suiteId', 'type': 'int'}
    }

    def __init__(self, id=None, sequence_number=None, suite_entry_type=None, suite_id=None):
        super(SuiteEntry, self).__init__(id=id, sequence_number=sequence_number, suite_entry_type=suite_entry_type)
        self.suite_id = suite_id


class TestConfiguration(TestConfigurationCreateUpdateParameters):
    """
    Test configuration

    :param description: Description of the configuration
    :type description: str
    :param is_default: Is the configuration a default for the test plans
    :type is_default: bool
    :param name: Name of the configuration
    :type name: str
    :param state: State of the configuration
    :type state: object
    :param values: Dictionary of Test Variable, Selected Value
    :type values: list of :class:`NameValuePair <azure.devops.v7_1.test_plan.models.NameValuePair>`
    :param id: Id of the configuration
    :type id: int
    :param project: Id of the test configuration variable
    :type project: :class:`TeamProjectReference <azure.devops.v7_1.test_plan.models.TeamProjectReference>`
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'is_default': {'key': 'isDefault', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'state': {'key': 'state', 'type': 'object'},
        'values': {'key': 'values', 'type': '[NameValuePair]'},
        'id': {'key': 'id', 'type': 'int'},
        'project': {'key': 'project', 'type': 'TeamProjectReference'}
    }

    def __init__(self, description=None, is_default=None, name=None, state=None, values=None, id=None, project=None):
        super(TestConfiguration, self).__init__(description=description, is_default=is_default, name=name, state=state, values=values)
        self.id = id
        self.project = project


class TestPlan(TestPlanUpdateParams):
    """
    The test plan resource.

    :param area_path: Area of the test plan.
    :type area_path: str
    :param automated_test_environment:
    :type automated_test_environment: :class:`TestEnvironment <azure.devops.v7_1.test_plan.models.TestEnvironment>`
    :param automated_test_settings:
    :type automated_test_settings: :class:`TestSettings <azure.devops.v7_1.test_plan.models.TestSettings>`
    :param build_definition: The Build Definition that generates a build associated with this test plan.
    :type build_definition: :class:`BuildDefinitionReference <azure.devops.v7_1.test_plan.models.BuildDefinitionReference>`
    :param build_id: Build to be tested.
    :type build_id: int
    :param description: Description of the test plan.
    :type description: str
    :param end_date: End date for the test plan.
    :type end_date: datetime
    :param iteration: Iteration path of the test plan.
    :type iteration: str
    :param manual_test_environment:
    :type manual_test_environment: :class:`TestEnvironment <azure.devops.v7_1.test_plan.models.TestEnvironment>`
    :param manual_test_settings:
    :type manual_test_settings: :class:`TestSettings <azure.devops.v7_1.test_plan.models.TestSettings>`
    :param name: Name of the test plan.
    :type name: str
    :param owner: Owner of the test plan.
    :type owner: :class:`IdentityRef <azure.devops.v7_1.test_plan.models.IdentityRef>`
    :param release_environment_definition: Release Environment to be used to deploy the build and run automated tests from this test plan.
    :type release_environment_definition: :class:`ReleaseEnvironmentDefinitionReference <azure.devops.v7_1.test_plan.models.ReleaseEnvironmentDefinitionReference>`
    :param start_date: Start date for the test plan.
    :type start_date: datetime
    :param state: State of the test plan.
    :type state: str
    :param test_outcome_settings: Value to configure how same tests across test suites under a test plan need to behave
    :type test_outcome_settings: :class:`TestOutcomeSettings <azure.devops.v7_1.test_plan.models.TestOutcomeSettings>`
    :param revision: Revision of the test plan.
    :type revision: int
    :param _links: Relevant links
    :type _links: :class:`ReferenceLinks <azure.devops.v7_1.test_plan.models.ReferenceLinks>`
    :param id: ID of the test plan.
    :type id: int
    :param previous_build_id: Previous build Id associated with the test plan
    :type previous_build_id: int
    :param project: Project which contains the test plan.
    :type project: :class:`TeamProjectReference <azure.devops.v7_1.test_plan.models.TeamProjectReference>`
    :param root_suite: Root test suite of the test plan.
    :type root_suite: :class:`TestSuiteReference <azure.devops.v7_1.test_plan.models.TestSuiteReference>`
    :param updated_by: Identity Reference for the last update of the test plan
    :type updated_by: :class:`IdentityRef <azure.devops.v7_1.test_plan.models.IdentityRef>`
    :param updated_date: Updated date of the test plan
    :type updated_date: datetime
    """

    _attribute_map = {
        'area_path': {'key': 'areaPath', 'type': 'str'},
        'automated_test_environment': {'key': 'automatedTestEnvironment', 'type': 'TestEnvironment'},
        'automated_test_settings': {'key': 'automatedTestSettings', 'type': 'TestSettings'},
        'build_definition': {'key': 'buildDefinition', 'type': 'BuildDefinitionReference'},
        'build_id': {'key': 'buildId', 'type': 'int'},
        'description': {'key': 'description', 'type': 'str'},
        'end_date': {'key': 'endDate', 'type': 'iso-8601'},
        'iteration': {'key': 'iteration', 'type': 'str'},
        'manual_test_environment': {'key': 'manualTestEnvironment', 'type': 'TestEnvironment'},
        'manual_test_settings': {'key': 'manualTestSettings', 'type': 'TestSettings'},
        'name': {'key': 'name', 'type': 'str'},
        'owner': {'key': 'owner', 'type': 'IdentityRef'},
        'release_environment_definition': {'key': 'releaseEnvironmentDefinition', 'type': 'ReleaseEnvironmentDefinitionReference'},
        'start_date': {'key': 'startDate', 'type': 'iso-8601'},
        'state': {'key': 'state', 'type': 'str'},
        'test_outcome_settings': {'key': 'testOutcomeSettings', 'type': 'TestOutcomeSettings'},
        'revision': {'key': 'revision', 'type': 'int'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'id': {'key': 'id', 'type': 'int'},
        'previous_build_id': {'key': 'previousBuildId', 'type': 'int'},
        'project': {'key': 'project', 'type': 'TeamProjectReference'},
        'root_suite': {'key': 'rootSuite', 'type': 'TestSuiteReference'},
        'updated_by': {'key': 'updatedBy', 'type': 'IdentityRef'},
        'updated_date': {'key': 'updatedDate', 'type': 'iso-8601'}
    }

    def __init__(self, area_path=None, automated_test_environment=None, automated_test_settings=None, build_definition=None, build_id=None, description=None, end_date=None, iteration=None, manual_test_environment=None, manual_test_settings=None, name=None, owner=None, release_environment_definition=None, start_date=None, state=None, test_outcome_settings=None, revision=None, _links=None, id=None, previous_build_id=None, project=None, root_suite=None, updated_by=None, updated_date=None):
        super(TestPlan, self).__init__(area_path=area_path, automated_test_environment=automated_test_environment, automated_test_settings=automated_test_settings, build_definition=build_definition, build_id=build_id, description=description, end_date=end_date, iteration=iteration, manual_test_environment=manual_test_environment, manual_test_settings=manual_test_settings, name=name, owner=owner, release_environment_definition=release_environment_definition, start_date=start_date, state=state, test_outcome_settings=test_outcome_settings, revision=revision)
        self._links = _links
        self.id = id
        self.previous_build_id = previous_build_id
        self.project = project
        self.root_suite = root_suite
        self.updated_by = updated_by
        self.updated_date = updated_date


class TestPlanDetailedReference(TestPlanReference):
    """
    The test plan detailed reference resource. Contains additional workitem realted information

    :param id: ID of the test plan.
    :type id: int
    :param name: Name of the test plan.
    :type name: str
    :param area_path: Area of the test plan.
    :type area_path: str
    :param end_date: End date for the test plan.
    :type end_date: datetime
    :param iteration: Iteration path of the test plan.
    :type iteration: str
    :param root_suite_id: Root Suite Id
    :type root_suite_id: int
    :param start_date: Start date for the test plan.
    :type start_date: datetime
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'area_path': {'key': 'areaPath', 'type': 'str'},
        'end_date': {'key': 'endDate', 'type': 'iso-8601'},
        'iteration': {'key': 'iteration', 'type': 'str'},
        'root_suite_id': {'key': 'rootSuiteId', 'type': 'int'},
        'start_date': {'key': 'startDate', 'type': 'iso-8601'}
    }

    def __init__(self, id=None, name=None, area_path=None, end_date=None, iteration=None, root_suite_id=None, start_date=None):
        super(TestPlanDetailedReference, self).__init__(id=id, name=name)
        self.area_path = area_path
        self.end_date = end_date
        self.iteration = iteration
        self.root_suite_id = root_suite_id
        self.start_date = start_date


class TestSuiteCreateParams(TestSuiteCreateUpdateCommonParams):
    """
    Test suite Create Parameters

    :param default_configurations: Test suite default configurations.
    :type default_configurations: list of :class:`TestConfigurationReference <azure.devops.v7_1.test_plan.models.TestConfigurationReference>`
    :param default_testers: Test suite default testers.
    :type default_testers: list of :class:`IdentityRef <azure.devops.v7_1.test_plan.models.IdentityRef>`
    :param inherit_default_configurations: Default configuration was inherited or not.
    :type inherit_default_configurations: bool
    :param name: Name of test suite.
    :type name: str
    :param parent_suite: Test suite parent shallow reference.
    :type parent_suite: :class:`TestSuiteReference <azure.devops.v7_1.test_plan.models.TestSuiteReference>`
    :param query_string: Test suite query string, for dynamic suites.
    :type query_string: str
    :param requirement_id: Test suite requirement id.
    :type requirement_id: int
    :param suite_type: Test suite type.
    :type suite_type: object
    """

    _attribute_map = {
        'default_configurations': {'key': 'defaultConfigurations', 'type': '[TestConfigurationReference]'},
        'default_testers': {'key': 'defaultTesters', 'type': '[IdentityRef]'},
        'inherit_default_configurations': {'key': 'inheritDefaultConfigurations', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'parent_suite': {'key': 'parentSuite', 'type': 'TestSuiteReference'},
        'query_string': {'key': 'queryString', 'type': 'str'},
        'requirement_id': {'key': 'requirementId', 'type': 'int'},
        'suite_type': {'key': 'suiteType', 'type': 'object'}
    }

    def __init__(self, default_configurations=None, default_testers=None, inherit_default_configurations=None, name=None, parent_suite=None, query_string=None, requirement_id=None, suite_type=None):
        super(TestSuiteCreateParams, self).__init__(default_configurations=default_configurations, default_testers=default_testers, inherit_default_configurations=inherit_default_configurations, name=name, parent_suite=parent_suite, query_string=query_string)
        self.requirement_id = requirement_id
        self.suite_type = suite_type


class TestVariable(TestVariableCreateUpdateParameters):
    """
    Test Variable

    :param description: Description of the test variable
    :type description: str
    :param name: Name of the test variable
    :type name: str
    :param values: List of allowed values
    :type values: list of str
    :param id: Id of the test variable
    :type id: int
    :param project: Id of the test variable
    :type project: :class:`TeamProjectReference <azure.devops.v7_1.test_plan.models.TeamProjectReference>`
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'values': {'key': 'values', 'type': '[str]'},
        'id': {'key': 'id', 'type': 'int'},
        'project': {'key': 'project', 'type': 'TeamProjectReference'}
    }

    def __init__(self, description=None, name=None, values=None, id=None, project=None):
        super(TestVariable, self).__init__(description=description, name=name, values=values)
        self.id = id
        self.project = project


class TestSuite(TestSuiteCreateParams):
    """
    Test suite

    :param default_configurations: Test suite default configurations.
    :type default_configurations: list of :class:`TestConfigurationReference <azure.devops.v7_1.test_plan.models.TestConfigurationReference>`
    :param default_testers: Test suite default testers.
    :type default_testers: list of :class:`IdentityRef <azure.devops.v7_1.test_plan.models.IdentityRef>`
    :param inherit_default_configurations: Default configuration was inherited or not.
    :type inherit_default_configurations: bool
    :param name: Name of test suite.
    :type name: str
    :param parent_suite: Test suite parent shallow reference.
    :type parent_suite: :class:`TestSuiteReference <azure.devops.v7_1.test_plan.models.TestSuiteReference>`
    :param query_string: Test suite query string, for dynamic suites.
    :type query_string: str
    :param requirement_id: Test suite requirement id.
    :type requirement_id: int
    :param suite_type: Test suite type.
    :type suite_type: object
    :param _links: Links: self, testPoints, testCases, parent
    :type _links: :class:`ReferenceLinks <azure.devops.v7_1.test_plan.models.ReferenceLinks>`
    :param has_children: Boolean value dictating if Child test suites are present
    :type has_children: bool
    :param children: Child test suites of current test suite.
    :type children: list of :class:`TestSuite <azure.devops.v7_1.test_plan.models.TestSuite>`
    :param id: Id of test suite.
    :type id: int
    :param last_error: Last error for test suite.
    :type last_error: str
    :param last_populated_date: Last populated date.
    :type last_populated_date: datetime
    :param last_updated_by: IdentityRef of user who has updated test suite recently.
    :type last_updated_by: :class:`IdentityRef <azure.devops.v7_1.test_plan.models.IdentityRef>`
    :param last_updated_date: Last update date.
    :type last_updated_date: datetime
    :param plan: Test plan to which the test suite belongs.
    :type plan: :class:`TestPlanReference <azure.devops.v7_1.test_plan.models.TestPlanReference>`
    :param project: Test suite project shallow reference.
    :type project: :class:`TeamProjectReference <azure.devops.v7_1.test_plan.models.TeamProjectReference>`
    :param revision: Test suite revision.
    :type revision: int
    """

    _attribute_map = {
        'default_configurations': {'key': 'defaultConfigurations', 'type': '[TestConfigurationReference]'},
        'default_testers': {'key': 'defaultTesters', 'type': '[IdentityRef]'},
        'inherit_default_configurations': {'key': 'inheritDefaultConfigurations', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'parent_suite': {'key': 'parentSuite', 'type': 'TestSuiteReference'},
        'query_string': {'key': 'queryString', 'type': 'str'},
        'requirement_id': {'key': 'requirementId', 'type': 'int'},
        'suite_type': {'key': 'suiteType', 'type': 'object'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'has_children': {'key': 'hasChildren', 'type': 'bool'},
        'children': {'key': 'children', 'type': '[TestSuite]'},
        'id': {'key': 'id', 'type': 'int'},
        'last_error': {'key': 'lastError', 'type': 'str'},
        'last_populated_date': {'key': 'lastPopulatedDate', 'type': 'iso-8601'},
        'last_updated_by': {'key': 'lastUpdatedBy', 'type': 'IdentityRef'},
        'last_updated_date': {'key': 'lastUpdatedDate', 'type': 'iso-8601'},
        'plan': {'key': 'plan', 'type': 'TestPlanReference'},
        'project': {'key': 'project', 'type': 'TeamProjectReference'},
        'revision': {'key': 'revision', 'type': 'int'}
    }

    def __init__(self, default_configurations=None, default_testers=None, inherit_default_configurations=None, name=None, parent_suite=None, query_string=None, requirement_id=None, suite_type=None, _links=None, has_children=None, children=None, id=None, last_error=None, last_populated_date=None, last_updated_by=None, last_updated_date=None, plan=None, project=None, revision=None):
        super(TestSuite, self).__init__(default_configurations=default_configurations, default_testers=default_testers, inherit_default_configurations=inherit_default_configurations, name=name, parent_suite=parent_suite, query_string=query_string, requirement_id=requirement_id, suite_type=suite_type)
        self._links = _links
        self.has_children = has_children
        self.children = children
        self.id = id
        self.last_error = last_error
        self.last_populated_date = last_populated_date
        self.last_updated_by = last_updated_by
        self.last_updated_date = last_updated_date
        self.plan = plan
        self.project = project
        self.revision = revision


__all__ = [
    'BuildDefinitionReference',
    'CloneOperationCommonResponse',
    'CloneOptions',
    'CloneStatistics',
    'CloneTestCaseOperationInformation',
    'CloneTestCaseOptions',
    'CloneTestCaseParams',
    'CloneTestPlanOperationInformation',
    'CloneTestPlanParams',
    'CloneTestSuiteOperationInformation',
    'CloneTestSuiteParams',
    'Configuration',
    'DestinationTestSuiteInfo',
    'GraphSubjectBase',
    'IdentityRef',
    'LastResultDetails',
    'LibraryWorkItemsData',
    'LibraryWorkItemsDataProviderRequest',
    'NameValuePair',
    'PointAssignment',
    'ReferenceLinks',
    'ReleaseEnvironmentDefinitionReference',
    'Results',
    'SourceTestPlanInfo',
    'SourceTestSuiteInfo',
    'SuiteEntryUpdateParams',
    'SuiteTestCaseCreateUpdateParameters',
    'TeamProjectReference',
    'TestCase',
    'TestCaseAssociatedResult',
    'TestCaseReference',
    'TestCaseResultsData',
    'TestConfigurationCreateUpdateParameters',
    'TestConfigurationReference',
    'TestEntityCount',
    'TestEnvironment',
    'TestOutcomeSettings',
    'TestPlanCreateParams',
    'TestPlanReference',
    'TestPlansHubRefreshData',
    'TestPlansLibraryWorkItemFilter',
    'TestPlanUpdateParams',
    'TestPoint',
    'TestPointDetailedReference',
    'TestPointResults',
    'TestPointUpdateParams',
    'TestSettings',
    'TestSuiteCreateUpdateCommonParams',
    'TestSuiteReference',
    'TestSuiteReferenceWithProject',
    'TestSuiteUpdateParams',
    'TestVariableCreateUpdateParameters',
    'WorkItem',
    'WorkItemDetails',
    'DestinationTestPlanCloneParams',
    'SourceTestplanResponse',
    'SourceTestSuiteResponse',
    'SuiteEntry',
    'TestConfiguration',
    'TestPlan',
    'TestPlanDetailedReference',
    'TestSuiteCreateParams',
    'TestVariable',
    'TestSuite',
]
