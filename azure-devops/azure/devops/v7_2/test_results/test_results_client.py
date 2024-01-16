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


class TestResultsClient(Client):
    """TestResults
    :param str base_url: Service URL
    :param Authentication creds: Authenticated credentials.
    """

    def __init__(self, base_url=None, creds=None):
        super(TestResultsClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = 'c83eaf52-edf3-4034-ae11-17d38f25404c'

    def create_test_iteration_result_attachment(self, attachment_request_model, project, run_id, test_case_result_id, iteration_id, action_path=None):
        """CreateTestIterationResultAttachment.
        [Preview API]
        :param :class:`<TestAttachmentRequestModel> <azure.devops.v7_2.test_results.models.TestAttachmentRequestModel>` attachment_request_model:
        :param str project: Project ID or project name
        :param int run_id:
        :param int test_case_result_id:
        :param int iteration_id:
        :param str action_path:
        :rtype: :class:`<TestAttachmentReference> <azure.devops.v7_2.test_results.models.TestAttachmentReference>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if test_case_result_id is not None:
            route_values['testCaseResultId'] = self._serialize.url('test_case_result_id', test_case_result_id, 'int')
        query_parameters = {}
        if iteration_id is not None:
            query_parameters['iterationId'] = self._serialize.query('iteration_id', iteration_id, 'int')
        if action_path is not None:
            query_parameters['actionPath'] = self._serialize.query('action_path', action_path, 'str')
        content = self._serialize.body(attachment_request_model, 'TestAttachmentRequestModel')
        response = self._send(http_method='POST',
                              location_id='2a632e97-e014-4275-978f-8e5c4906d4b3',
                              version='7.2-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('TestAttachmentReference', response)

    def create_test_result_attachment(self, attachment_request_model, project, run_id, test_case_result_id):
        """CreateTestResultAttachment.
        [Preview API]
        :param :class:`<TestAttachmentRequestModel> <azure.devops.v7_2.test_results.models.TestAttachmentRequestModel>` attachment_request_model:
        :param str project: Project ID or project name
        :param int run_id:
        :param int test_case_result_id:
        :rtype: :class:`<TestAttachmentReference> <azure.devops.v7_2.test_results.models.TestAttachmentReference>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if test_case_result_id is not None:
            route_values['testCaseResultId'] = self._serialize.url('test_case_result_id', test_case_result_id, 'int')
        content = self._serialize.body(attachment_request_model, 'TestAttachmentRequestModel')
        response = self._send(http_method='POST',
                              location_id='2a632e97-e014-4275-978f-8e5c4906d4b3',
                              version='7.2-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TestAttachmentReference', response)

    def create_test_sub_result_attachment(self, attachment_request_model, project, run_id, test_case_result_id, test_sub_result_id):
        """CreateTestSubResultAttachment.
        [Preview API]
        :param :class:`<TestAttachmentRequestModel> <azure.devops.v7_2.test_results.models.TestAttachmentRequestModel>` attachment_request_model:
        :param str project: Project ID or project name
        :param int run_id:
        :param int test_case_result_id:
        :param int test_sub_result_id:
        :rtype: :class:`<TestAttachmentReference> <azure.devops.v7_2.test_results.models.TestAttachmentReference>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if test_case_result_id is not None:
            route_values['testCaseResultId'] = self._serialize.url('test_case_result_id', test_case_result_id, 'int')
        query_parameters = {}
        if test_sub_result_id is not None:
            query_parameters['testSubResultId'] = self._serialize.query('test_sub_result_id', test_sub_result_id, 'int')
        content = self._serialize.body(attachment_request_model, 'TestAttachmentRequestModel')
        response = self._send(http_method='POST',
                              location_id='2a632e97-e014-4275-978f-8e5c4906d4b3',
                              version='7.2-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('TestAttachmentReference', response)

    def delete_test_result_attachment(self, project, run_id, test_case_result_id, attachment_id):
        """DeleteTestResultAttachment.
        [Preview API]
        :param str project: Project ID or project name
        :param int run_id:
        :param int test_case_result_id:
        :param int attachment_id:
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if test_case_result_id is not None:
            route_values['testCaseResultId'] = self._serialize.url('test_case_result_id', test_case_result_id, 'int')
        if attachment_id is not None:
            route_values['attachmentId'] = self._serialize.url('attachment_id', attachment_id, 'int')
        self._send(http_method='DELETE',
                   location_id='2a632e97-e014-4275-978f-8e5c4906d4b3',
                   version='7.2-preview.1',
                   route_values=route_values)

    def get_test_iteration_attachment_content(self, project, run_id, test_case_result_id, attachment_id, iteration_id, **kwargs):
        """GetTestIterationAttachmentContent.
        [Preview API] Returns a test iteration attachment
        :param str project: Project ID or project name
        :param int run_id:
        :param int test_case_result_id:
        :param int attachment_id:
        :param int iteration_id:
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if test_case_result_id is not None:
            route_values['testCaseResultId'] = self._serialize.url('test_case_result_id', test_case_result_id, 'int')
        if attachment_id is not None:
            route_values['attachmentId'] = self._serialize.url('attachment_id', attachment_id, 'int')
        query_parameters = {}
        if iteration_id is not None:
            query_parameters['iterationId'] = self._serialize.query('iteration_id', iteration_id, 'int')
        response = self._send(http_method='GET',
                              location_id='2a632e97-e014-4275-978f-8e5c4906d4b3',
                              version='7.2-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='application/octet-stream')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_test_iteration_attachment_zip(self, project, run_id, test_case_result_id, attachment_id, iteration_id, **kwargs):
        """GetTestIterationAttachmentZip.
        [Preview API] Returns a test iteration attachment
        :param str project: Project ID or project name
        :param int run_id:
        :param int test_case_result_id:
        :param int attachment_id:
        :param int iteration_id:
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if test_case_result_id is not None:
            route_values['testCaseResultId'] = self._serialize.url('test_case_result_id', test_case_result_id, 'int')
        if attachment_id is not None:
            route_values['attachmentId'] = self._serialize.url('attachment_id', attachment_id, 'int')
        query_parameters = {}
        if iteration_id is not None:
            query_parameters['iterationId'] = self._serialize.query('iteration_id', iteration_id, 'int')
        response = self._send(http_method='GET',
                              location_id='2a632e97-e014-4275-978f-8e5c4906d4b3',
                              version='7.2-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='application/zip')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_test_result_attachment_content(self, project, run_id, test_case_result_id, attachment_id, **kwargs):
        """GetTestResultAttachmentContent.
        [Preview API] Returns a test result attachment
        :param str project: Project ID or project name
        :param int run_id:
        :param int test_case_result_id:
        :param int attachment_id:
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if test_case_result_id is not None:
            route_values['testCaseResultId'] = self._serialize.url('test_case_result_id', test_case_result_id, 'int')
        if attachment_id is not None:
            route_values['attachmentId'] = self._serialize.url('attachment_id', attachment_id, 'int')
        response = self._send(http_method='GET',
                              location_id='2a632e97-e014-4275-978f-8e5c4906d4b3',
                              version='7.2-preview.1',
                              route_values=route_values,
                              accept_media_type='application/octet-stream')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_test_result_attachments(self, project, run_id, test_case_result_id):
        """GetTestResultAttachments.
        [Preview API]
        :param str project: Project ID or project name
        :param int run_id:
        :param int test_case_result_id:
        :rtype: [TestAttachment]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if test_case_result_id is not None:
            route_values['testCaseResultId'] = self._serialize.url('test_case_result_id', test_case_result_id, 'int')
        response = self._send(http_method='GET',
                              location_id='2a632e97-e014-4275-978f-8e5c4906d4b3',
                              version='7.2-preview.1',
                              route_values=route_values)
        return self._deserialize('[TestAttachment]', self._unwrap_collection(response))

    def get_test_result_attachment_zip(self, project, run_id, test_case_result_id, attachment_id, **kwargs):
        """GetTestResultAttachmentZip.
        [Preview API] Returns a test result attachment
        :param str project: Project ID or project name
        :param int run_id:
        :param int test_case_result_id:
        :param int attachment_id:
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if test_case_result_id is not None:
            route_values['testCaseResultId'] = self._serialize.url('test_case_result_id', test_case_result_id, 'int')
        if attachment_id is not None:
            route_values['attachmentId'] = self._serialize.url('attachment_id', attachment_id, 'int')
        response = self._send(http_method='GET',
                              location_id='2a632e97-e014-4275-978f-8e5c4906d4b3',
                              version='7.2-preview.1',
                              route_values=route_values,
                              accept_media_type='application/zip')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_test_sub_result_attachment_content(self, project, run_id, test_case_result_id, attachment_id, test_sub_result_id, **kwargs):
        """GetTestSubResultAttachmentContent.
        [Preview API] Returns a test sub result attachment
        :param str project: Project ID or project name
        :param int run_id:
        :param int test_case_result_id:
        :param int attachment_id:
        :param int test_sub_result_id:
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if test_case_result_id is not None:
            route_values['testCaseResultId'] = self._serialize.url('test_case_result_id', test_case_result_id, 'int')
        if attachment_id is not None:
            route_values['attachmentId'] = self._serialize.url('attachment_id', attachment_id, 'int')
        query_parameters = {}
        if test_sub_result_id is not None:
            query_parameters['testSubResultId'] = self._serialize.query('test_sub_result_id', test_sub_result_id, 'int')
        response = self._send(http_method='GET',
                              location_id='2a632e97-e014-4275-978f-8e5c4906d4b3',
                              version='7.2-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='application/octet-stream')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_test_sub_result_attachments(self, project, run_id, test_case_result_id, test_sub_result_id):
        """GetTestSubResultAttachments.
        [Preview API] Returns attachment references for test sub result.
        :param str project: Project ID or project name
        :param int run_id:
        :param int test_case_result_id:
        :param int test_sub_result_id:
        :rtype: [TestAttachment]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if test_case_result_id is not None:
            route_values['testCaseResultId'] = self._serialize.url('test_case_result_id', test_case_result_id, 'int')
        query_parameters = {}
        if test_sub_result_id is not None:
            query_parameters['testSubResultId'] = self._serialize.query('test_sub_result_id', test_sub_result_id, 'int')
        response = self._send(http_method='GET',
                              location_id='2a632e97-e014-4275-978f-8e5c4906d4b3',
                              version='7.2-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TestAttachment]', self._unwrap_collection(response))

    def get_test_sub_result_attachment_zip(self, project, run_id, test_case_result_id, attachment_id, test_sub_result_id, **kwargs):
        """GetTestSubResultAttachmentZip.
        [Preview API] Returns a test sub result attachment
        :param str project: Project ID or project name
        :param int run_id:
        :param int test_case_result_id:
        :param int attachment_id:
        :param int test_sub_result_id:
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if test_case_result_id is not None:
            route_values['testCaseResultId'] = self._serialize.url('test_case_result_id', test_case_result_id, 'int')
        if attachment_id is not None:
            route_values['attachmentId'] = self._serialize.url('attachment_id', attachment_id, 'int')
        query_parameters = {}
        if test_sub_result_id is not None:
            query_parameters['testSubResultId'] = self._serialize.query('test_sub_result_id', test_sub_result_id, 'int')
        response = self._send(http_method='GET',
                              location_id='2a632e97-e014-4275-978f-8e5c4906d4b3',
                              version='7.2-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='application/zip')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def create_test_run_attachment(self, attachment_request_model, project, run_id):
        """CreateTestRunAttachment.
        [Preview API]
        :param :class:`<TestAttachmentRequestModel> <azure.devops.v7_2.test_results.models.TestAttachmentRequestModel>` attachment_request_model:
        :param str project: Project ID or project name
        :param int run_id:
        :rtype: :class:`<TestAttachmentReference> <azure.devops.v7_2.test_results.models.TestAttachmentReference>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        content = self._serialize.body(attachment_request_model, 'TestAttachmentRequestModel')
        response = self._send(http_method='POST',
                              location_id='b5731898-8206-477a-a51d-3fdf116fc6bf',
                              version='7.2-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TestAttachmentReference', response)

    def delete_test_run_attachment(self, project, run_id, attachment_id):
        """DeleteTestRunAttachment.
        [Preview API]
        :param str project: Project ID or project name
        :param int run_id:
        :param int attachment_id:
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if attachment_id is not None:
            route_values['attachmentId'] = self._serialize.url('attachment_id', attachment_id, 'int')
        self._send(http_method='DELETE',
                   location_id='b5731898-8206-477a-a51d-3fdf116fc6bf',
                   version='7.2-preview.1',
                   route_values=route_values)

    def get_test_run_attachment_content(self, project, run_id, attachment_id, **kwargs):
        """GetTestRunAttachmentContent.
        [Preview API] Returns a test run attachment
        :param str project: Project ID or project name
        :param int run_id:
        :param int attachment_id:
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if attachment_id is not None:
            route_values['attachmentId'] = self._serialize.url('attachment_id', attachment_id, 'int')
        response = self._send(http_method='GET',
                              location_id='b5731898-8206-477a-a51d-3fdf116fc6bf',
                              version='7.2-preview.1',
                              route_values=route_values,
                              accept_media_type='application/octet-stream')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_test_run_attachments(self, project, run_id):
        """GetTestRunAttachments.
        [Preview API]
        :param str project: Project ID or project name
        :param int run_id:
        :rtype: [TestAttachment]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        response = self._send(http_method='GET',
                              location_id='b5731898-8206-477a-a51d-3fdf116fc6bf',
                              version='7.2-preview.1',
                              route_values=route_values)
        return self._deserialize('[TestAttachment]', self._unwrap_collection(response))

    def get_test_run_attachment_zip(self, project, run_id, attachment_id, **kwargs):
        """GetTestRunAttachmentZip.
        [Preview API] Returns a test run attachment
        :param str project: Project ID or project name
        :param int run_id:
        :param int attachment_id:
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if attachment_id is not None:
            route_values['attachmentId'] = self._serialize.url('attachment_id', attachment_id, 'int')
        response = self._send(http_method='GET',
                              location_id='b5731898-8206-477a-a51d-3fdf116fc6bf',
                              version='7.2-preview.1',
                              route_values=route_values,
                              accept_media_type='application/zip')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_bugs_linked_to_test_result(self, project, run_id, test_case_result_id):
        """GetBugsLinkedToTestResult.
        [Preview API]
        :param str project: Project ID or project name
        :param int run_id:
        :param int test_case_result_id:
        :rtype: [WorkItemReference]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if test_case_result_id is not None:
            route_values['testCaseResultId'] = self._serialize.url('test_case_result_id', test_case_result_id, 'int')
        response = self._send(http_method='GET',
                              location_id='d8dbf98f-eb34-4f8d-8365-47972af34f29',
                              version='7.2-preview.1',
                              route_values=route_values)
        return self._deserialize('[WorkItemReference]', self._unwrap_collection(response))

    def fetch_source_code_coverage_report(self, project, build_id):
        """FetchSourceCodeCoverageReport.
        [Preview API]
        :param str project: Project ID or project name
        :param int build_id:
        :rtype: [SourceViewBuildCoverage]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if build_id is not None:
            query_parameters['buildId'] = self._serialize.query('build_id', build_id, 'int')
        response = self._send(http_method='GET',
                              location_id='a459e10b-d703-4193-b3c1-60f2287918b3',
                              version='7.2-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[SourceViewBuildCoverage]', self._unwrap_collection(response))

    def get_build_code_coverage(self, project, build_id, flags):
        """GetBuildCodeCoverage.
        [Preview API]
        :param str project: Project ID or project name
        :param int build_id:
        :param int flags:
        :rtype: [BuildCoverage]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if build_id is not None:
            query_parameters['buildId'] = self._serialize.query('build_id', build_id, 'int')
        if flags is not None:
            query_parameters['flags'] = self._serialize.query('flags', flags, 'int')
        response = self._send(http_method='GET',
                              location_id='9b3e1ece-c6ab-4fbb-8167-8a32a0c92216',
                              version='7.2-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[BuildCoverage]', self._unwrap_collection(response))

    def get_code_coverage_summary(self, project, build_id, delta_build_id=None):
        """GetCodeCoverageSummary.
        [Preview API] http://(tfsserver):8080/tfs/DefaultCollection/_apis/test/CodeCoverage?buildId=10&deltaBuildId=9 Request: build id and delta build id (optional)
        :param str project: Project ID or project name
        :param int build_id:
        :param int delta_build_id:
        :rtype: :class:`<CodeCoverageSummary> <azure.devops.v7_2.test_results.models.CodeCoverageSummary>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if build_id is not None:
            query_parameters['buildId'] = self._serialize.query('build_id', build_id, 'int')
        if delta_build_id is not None:
            query_parameters['deltaBuildId'] = self._serialize.query('delta_build_id', delta_build_id, 'int')
        response = self._send(http_method='GET',
                              location_id='9b3e1ece-c6ab-4fbb-8167-8a32a0c92216',
                              version='7.2-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('CodeCoverageSummary', response)

    def update_code_coverage_summary(self, project, build_id, coverage_data=None):
        """UpdateCodeCoverageSummary.
        [Preview API] http://(tfsserver):8080/tfs/DefaultCollection/_apis/test/CodeCoverage?buildId=10 Request: Json of code coverage summary
        :param str project: Project ID or project name
        :param int build_id:
        :param :class:`<CodeCoverageData> <azure.devops.v7_2.test_results.models.CodeCoverageData>` coverage_data:
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if build_id is not None:
            query_parameters['buildId'] = self._serialize.query('build_id', build_id, 'int')
        content = self._serialize.body(coverage_data, 'CodeCoverageData')
        self._send(http_method='POST',
                   location_id='9b3e1ece-c6ab-4fbb-8167-8a32a0c92216',
                   version='7.2-preview.1',
                   route_values=route_values,
                   query_parameters=query_parameters,
                   content=content)

    def get_test_run_code_coverage(self, project, run_id, flags):
        """GetTestRunCodeCoverage.
        [Preview API]
        :param str project: Project ID or project name
        :param int run_id:
        :param int flags:
        :rtype: [TestRunCoverage]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        query_parameters = {}
        if flags is not None:
            query_parameters['flags'] = self._serialize.query('flags', flags, 'int')
        response = self._send(http_method='GET',
                              location_id='5641efbc-6f9b-401a-baeb-d3da22489e5e',
                              version='7.2-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TestRunCoverage]', self._unwrap_collection(response))

    def get_file_level_code_coverage(self, file_coverage_request, project, **kwargs):
        """GetFileLevelCodeCoverage.
        [Preview API] Get file coverage for the specified file
        :param :class:`<FileCoverageRequest> <azure.devops.v7_2.test_results.models.FileCoverageRequest>` file_coverage_request: File details with pull request iteration context
        :param str project: Project ID or project name
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(file_coverage_request, 'FileCoverageRequest')
        response = self._send(http_method='POST',
                              location_id='4a6d0c46-51ca-45aa-9163-249cee3289b7',
                              version='7.2-preview.1',
                              route_values=route_values,
                              content=content,
                              accept_media_type='text/plain')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def query_test_result_history(self, filter, project):
        """QueryTestResultHistory.
        [Preview API]
        :param :class:`<ResultsFilter> <azure.devops.v7_2.test_results.models.ResultsFilter>` filter:
        :param str project: Project ID or project name
        :rtype: :class:`<TestResultHistory> <azure.devops.v7_2.test_results.models.TestResultHistory>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(filter, 'ResultsFilter')
        response = self._send(http_method='POST',
                              location_id='bdf7a97b-0395-4da8-9d5d-f957619327d1',
                              version='7.2-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TestResultHistory', response)

    def get_test_run_message_logs(self, project, run_id):
        """GetTestRunMessageLogs.
        [Preview API] Get test run message logs
        :param str project: Project ID or project name
        :param int run_id: ID of the run to get.
        :rtype: [TestMessageLogDetails]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        response = self._send(http_method='GET',
                              location_id='e9ab0c6a-1984-418b-87c0-ee4202318ba3',
                              version='7.2-preview.1',
                              route_values=route_values)
        return self._deserialize('[TestMessageLogDetails]', self._unwrap_collection(response))

    def get_test_pipeline_metrics(self, project, pipeline_id, stage_name=None, phase_name=None, job_name=None, metric_names=None, group_by_node=None):
        """GetTestPipelineMetrics.
        [Preview API] Get summary of test results.
        :param str project: Project ID or project name
        :param int pipeline_id: Pipeline Id. This is same as build Id.
        :param str stage_name: Name of the stage. Maximum supported length for name is 256 character.
        :param str phase_name: Name of the phase. Maximum supported length for name is 256 character.
        :param str job_name: Matrixing in YAML generates copies of a job with different inputs in matrix. JobName is the name of those input. Maximum supported length for name is 256 character.
        :param [Metrics] metric_names:
        :param bool group_by_node: Group summary for each node of the pipleine heirarchy
        :rtype: :class:`<PipelineTestMetrics> <azure.devops.v7_2.test_results.models.PipelineTestMetrics>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if pipeline_id is not None:
            query_parameters['pipelineId'] = self._serialize.query('pipeline_id', pipeline_id, 'int')
        if stage_name is not None:
            query_parameters['stageName'] = self._serialize.query('stage_name', stage_name, 'str')
        if phase_name is not None:
            query_parameters['phaseName'] = self._serialize.query('phase_name', phase_name, 'str')
        if job_name is not None:
            query_parameters['jobName'] = self._serialize.query('job_name', job_name, 'str')
        if metric_names is not None:
            metric_names = ",".join(map(str, metric_names))
            query_parameters['metricNames'] = self._serialize.query('metric_names', metric_names, 'str')
        if group_by_node is not None:
            query_parameters['groupByNode'] = self._serialize.query('group_by_node', group_by_node, 'bool')
        response = self._send(http_method='GET',
                              location_id='65f35817-86a1-4131-b38b-3ec2d4744e53',
                              version='7.2-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('PipelineTestMetrics', response)

    def create_one_mRXTest_session(self, session, project):
        """CreateOneMRXTestSession.
        [Preview API] Creates OneMRX Session object in TCM data store
        :param :class:`<Session> <azure.devops.v7_2.test_results.models.Session>` session: Received session object.
        :param str project: Project ID or project name
        :rtype: long
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(session, 'Session')
        response = self._send(http_method='POST',
                              location_id='531e61ce-580d-4962-8591-0b2942b6bf78',
                              version='7.2-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('long', response)

    def get_one_mRXTest_session(self, project, build_id):
        """GetOneMRXTestSession.
        [Preview API] Retrieves OneMRX Session metadata object in TCM data store
        :param str project: Project ID or project name
        :param int build_id:
        :rtype: [Session]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if build_id is not None:
            query_parameters['buildId'] = self._serialize.query('build_id', build_id, 'int')
        response = self._send(http_method='GET',
                              location_id='531e61ce-580d-4962-8591-0b2942b6bf78',
                              version='7.2-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[Session]', self._unwrap_collection(response))

    def get_one_mRXTest_session_layout(self, project, session_id):
        """GetOneMRXTestSessionLayout.
        [Preview API] Retrieves OneMRX Session Layout object in TCM data store
        :param str project: Project ID or project name
        :param str session_id:
        :rtype: [object]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if session_id is not None:
            query_parameters['sessionId'] = self._serialize.query('session_id', session_id, 'str')
        response = self._send(http_method='GET',
                              location_id='531e61ce-580d-4962-8591-0b2942b6bf78',
                              version='7.2-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[object]', self._unwrap_collection(response))

    def get_test_result_details_for_build(self, project, build_id, publish_context=None, group_by=None, filter=None, orderby=None, should_include_results=None, query_run_summary_for_in_progress=None):
        """GetTestResultDetailsForBuild.
        [Preview API]
        :param str project: Project ID or project name
        :param int build_id:
        :param str publish_context:
        :param str group_by:
        :param str filter:
        :param str orderby:
        :param bool should_include_results:
        :param bool query_run_summary_for_in_progress:
        :rtype: :class:`<TestResultsDetails> <azure.devops.v7_2.test_results.models.TestResultsDetails>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if build_id is not None:
            query_parameters['buildId'] = self._serialize.query('build_id', build_id, 'int')
        if publish_context is not None:
            query_parameters['publishContext'] = self._serialize.query('publish_context', publish_context, 'str')
        if group_by is not None:
            query_parameters['groupBy'] = self._serialize.query('group_by', group_by, 'str')
        if filter is not None:
            query_parameters['$filter'] = self._serialize.query('filter', filter, 'str')
        if orderby is not None:
            query_parameters['$orderby'] = self._serialize.query('orderby', orderby, 'str')
        if should_include_results is not None:
            query_parameters['shouldIncludeResults'] = self._serialize.query('should_include_results', should_include_results, 'bool')
        if query_run_summary_for_in_progress is not None:
            query_parameters['queryRunSummaryForInProgress'] = self._serialize.query('query_run_summary_for_in_progress', query_run_summary_for_in_progress, 'bool')
        response = self._send(http_method='GET',
                              location_id='a518c749-4524-45b2-a7ef-1ac009b312cd',
                              version='7.2-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestResultsDetails', response)

    def get_test_result_details_for_release(self, project, release_id, release_env_id, publish_context=None, group_by=None, filter=None, orderby=None, should_include_results=None, query_run_summary_for_in_progress=None):
        """GetTestResultDetailsForRelease.
        [Preview API]
        :param str project: Project ID or project name
        :param int release_id:
        :param int release_env_id:
        :param str publish_context:
        :param str group_by:
        :param str filter:
        :param str orderby:
        :param bool should_include_results:
        :param bool query_run_summary_for_in_progress:
        :rtype: :class:`<TestResultsDetails> <azure.devops.v7_2.test_results.models.TestResultsDetails>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if release_id is not None:
            query_parameters['releaseId'] = self._serialize.query('release_id', release_id, 'int')
        if release_env_id is not None:
            query_parameters['releaseEnvId'] = self._serialize.query('release_env_id', release_env_id, 'int')
        if publish_context is not None:
            query_parameters['publishContext'] = self._serialize.query('publish_context', publish_context, 'str')
        if group_by is not None:
            query_parameters['groupBy'] = self._serialize.query('group_by', group_by, 'str')
        if filter is not None:
            query_parameters['$filter'] = self._serialize.query('filter', filter, 'str')
        if orderby is not None:
            query_parameters['$orderby'] = self._serialize.query('orderby', orderby, 'str')
        if should_include_results is not None:
            query_parameters['shouldIncludeResults'] = self._serialize.query('should_include_results', should_include_results, 'bool')
        if query_run_summary_for_in_progress is not None:
            query_parameters['queryRunSummaryForInProgress'] = self._serialize.query('query_run_summary_for_in_progress', query_run_summary_for_in_progress, 'bool')
        response = self._send(http_method='GET',
                              location_id='19a8183a-69fb-47d7-bfbf-1b6b0d921294',
                              version='7.2-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestResultsDetails', response)

    def publish_test_result_document(self, document, project, run_id):
        """PublishTestResultDocument.
        [Preview API]
        :param :class:`<TestResultDocument> <azure.devops.v7_2.test_results.models.TestResultDocument>` document:
        :param str project: Project ID or project name
        :param int run_id:
        :rtype: :class:`<TestResultDocument> <azure.devops.v7_2.test_results.models.TestResultDocument>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        content = self._serialize.body(document, 'TestResultDocument')
        response = self._send(http_method='POST',
                              location_id='74838649-b038-42f1-a0e7-6deb3973bf14',
                              version='7.2-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TestResultDocument', response)

    def get_result_groups_by_build(self, project, build_id, publish_context, fields=None, continuation_token=None):
        """GetResultGroupsByBuild.
        [Preview API]
        :param str project: Project ID or project name
        :param int build_id:
        :param str publish_context:
        :param [str] fields:
        :param str continuation_token:
        :rtype: :class:`<[FieldDetailsForTestResults]> <azure.devops.v7_2.test_results.models.[FieldDetailsForTestResults]>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if build_id is not None:
            query_parameters['buildId'] = self._serialize.query('build_id', build_id, 'int')
        if publish_context is not None:
            query_parameters['publishContext'] = self._serialize.query('publish_context', publish_context, 'str')
        if fields is not None:
            fields = ",".join(fields)
            query_parameters['fields'] = self._serialize.query('fields', fields, 'str')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        response = self._send(http_method='GET',
                              location_id='e49244d1-c49f-49ad-a717-3bbaefe6a201',
                              version='7.2-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[FieldDetailsForTestResults]', self._unwrap_collection(response))

    def get_result_groups_by_release(self, project, release_id, publish_context, release_env_id=None, fields=None, continuation_token=None):
        """GetResultGroupsByRelease.
        [Preview API]
        :param str project: Project ID or project name
        :param int release_id:
        :param str publish_context:
        :param int release_env_id:
        :param [str] fields:
        :param str continuation_token:
        :rtype: :class:`<[FieldDetailsForTestResults]> <azure.devops.v7_2.test_results.models.[FieldDetailsForTestResults]>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if release_id is not None:
            query_parameters['releaseId'] = self._serialize.query('release_id', release_id, 'int')
        if publish_context is not None:
            query_parameters['publishContext'] = self._serialize.query('publish_context', publish_context, 'str')
        if release_env_id is not None:
            query_parameters['releaseEnvId'] = self._serialize.query('release_env_id', release_env_id, 'int')
        if fields is not None:
            fields = ",".join(fields)
            query_parameters['fields'] = self._serialize.query('fields', fields, 'str')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        response = self._send(http_method='GET',
                              location_id='3c2b6bb0-0620-434a-a5c3-26aa0fcfda15',
                              version='7.2-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[FieldDetailsForTestResults]', self._unwrap_collection(response))

    def query_test_results_meta_data(self, test_case_reference_ids, project, details_to_include=None):
        """QueryTestResultsMetaData.
        [Preview API] Get list of test Result meta data details for corresponding testcasereferenceId
        :param [str] test_case_reference_ids: TestCaseReference Ids of the test Result to be queried, comma separated list of valid ids (limit no. of ids 200).
        :param str project: Project ID or project name
        :param str details_to_include: Details to include with test results metadata. Default is None. Other values are FlakyIdentifiers.
        :rtype: [TestResultMetaData]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if details_to_include is not None:
            query_parameters['detailsToInclude'] = self._serialize.query('details_to_include', details_to_include, 'str')
        content = self._serialize.body(test_case_reference_ids, '[str]')
        response = self._send(http_method='POST',
                              location_id='b72ff4c0-4341-4213-ba27-f517cf341c95',
                              version='7.2-preview.4',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('[TestResultMetaData]', self._unwrap_collection(response))

    def update_test_results_meta_data(self, test_result_meta_data_update_input, project, test_case_reference_id):
        """UpdateTestResultsMetaData.
        [Preview API] Update properties of test result meta data
        :param :class:`<TestResultMetaDataUpdateInput> <azure.devops.v7_2.test_results.models.TestResultMetaDataUpdateInput>` test_result_meta_data_update_input: TestResultMetaData update input TestResultMetaDataUpdateInput
        :param str project: Project ID or project name
        :param int test_case_reference_id: TestCaseReference Id of Test Result to be updated.
        :rtype: :class:`<TestResultMetaData> <azure.devops.v7_2.test_results.models.TestResultMetaData>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if test_case_reference_id is not None:
            route_values['testCaseReferenceId'] = self._serialize.url('test_case_reference_id', test_case_reference_id, 'int')
        content = self._serialize.body(test_result_meta_data_update_input, 'TestResultMetaDataUpdateInput')
        response = self._send(http_method='PATCH',
                              location_id='b72ff4c0-4341-4213-ba27-f517cf341c95',
                              version='7.2-preview.4',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TestResultMetaData', response)

    def get_test_results_by_query(self, query, project):
        """GetTestResultsByQuery.
        [Preview API]
        :param :class:`<TestResultsQuery> <azure.devops.v7_2.test_results.models.TestResultsQuery>` query:
        :param str project: Project ID or project name
        :rtype: :class:`<TestResultsQuery> <azure.devops.v7_2.test_results.models.TestResultsQuery>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(query, 'TestResultsQuery')
        response = self._send(http_method='POST',
                              location_id='14033a2c-af25-4af1-9e39-8ef6900482e3',
                              version='7.2-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TestResultsQuery', response)

    def get_test_results_by_query_wiql(self, query_model, project, include_result_details=None, include_iteration_details=None, skip=None, top=None):
        """GetTestResultsByQueryWiql.
        [Preview API]
        :param :class:`<QueryModel> <azure.devops.v7_2.test_results.models.QueryModel>` query_model:
        :param str project: Project ID or project name
        :param bool include_result_details:
        :param bool include_iteration_details:
        :param int skip:
        :param int top:
        :rtype: [TestCaseResult]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if include_result_details is not None:
            query_parameters['includeResultDetails'] = self._serialize.query('include_result_details', include_result_details, 'bool')
        if include_iteration_details is not None:
            query_parameters['includeIterationDetails'] = self._serialize.query('include_iteration_details', include_iteration_details, 'bool')
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        content = self._serialize.body(query_model, 'QueryModel')
        response = self._send(http_method='POST',
                              location_id='5ea78be3-2f5a-4110-8034-c27f24c62db1',
                              version='7.2-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('[TestCaseResult]', self._unwrap_collection(response))

    def add_test_results_to_test_run(self, results, project, run_id):
        """AddTestResultsToTestRun.
        [Preview API]
        :param [TestCaseResult] results:
        :param str project: Project ID or project name
        :param int run_id:
        :rtype: [TestCaseResult]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        content = self._serialize.body(results, '[TestCaseResult]')
        response = self._send(http_method='POST',
                              location_id='02afa165-e79a-4d70-8f0c-2af0f35b4e07',
                              version='7.2-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[TestCaseResult]', self._unwrap_collection(response))

    def get_test_result_by_id(self, project, run_id, test_result_id, details_to_include=None):
        """GetTestResultById.
        [Preview API]
        :param str project: Project ID or project name
        :param int run_id:
        :param int test_result_id:
        :param str details_to_include:
        :rtype: :class:`<TestCaseResult> <azure.devops.v7_2.test_results.models.TestCaseResult>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if test_result_id is not None:
            route_values['testResultId'] = self._serialize.url('test_result_id', test_result_id, 'int')
        query_parameters = {}
        if details_to_include is not None:
            query_parameters['detailsToInclude'] = self._serialize.query('details_to_include', details_to_include, 'str')
        response = self._send(http_method='GET',
                              location_id='02afa165-e79a-4d70-8f0c-2af0f35b4e07',
                              version='7.2-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestCaseResult', response)

    def get_test_results(self, project, run_id, details_to_include=None, skip=None, top=None, outcomes=None, new_tests_only=None):
        """GetTestResults.
        [Preview API]
        :param str project: Project ID or project name
        :param int run_id:
        :param str details_to_include:
        :param int skip:
        :param int top:
        :param [TestOutcome] outcomes:
        :param bool new_tests_only:
        :rtype: [TestCaseResult]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        query_parameters = {}
        if details_to_include is not None:
            query_parameters['detailsToInclude'] = self._serialize.query('details_to_include', details_to_include, 'str')
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if outcomes is not None:
            outcomes = ",".join(map(str, outcomes))
            query_parameters['outcomes'] = self._serialize.query('outcomes', outcomes, 'str')
        if new_tests_only is not None:
            query_parameters['$newTestsOnly'] = self._serialize.query('new_tests_only', new_tests_only, 'bool')
        response = self._send(http_method='GET',
                              location_id='02afa165-e79a-4d70-8f0c-2af0f35b4e07',
                              version='7.2-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TestCaseResult]', self._unwrap_collection(response))

    def update_test_results(self, results, project, run_id):
        """UpdateTestResults.
        [Preview API]
        :param [TestCaseResult] results:
        :param str project: Project ID or project name
        :param int run_id:
        :rtype: [TestCaseResult]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        content = self._serialize.body(results, '[TestCaseResult]')
        response = self._send(http_method='PATCH',
                              location_id='02afa165-e79a-4d70-8f0c-2af0f35b4e07',
                              version='7.2-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[TestCaseResult]', self._unwrap_collection(response))

    def get_test_results_by_build(self, project, build_id, publish_context=None, outcomes=None, top=None, continuation_token=None):
        """GetTestResultsByBuild.
        [Preview API]
        :param str project: Project ID or project name
        :param int build_id:
        :param str publish_context:
        :param [TestOutcome] outcomes:
        :param int top:
        :param str continuation_token:
        :rtype: :class:`<[ShallowTestCaseResult]> <azure.devops.v7_2.test_results.models.[ShallowTestCaseResult]>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if build_id is not None:
            query_parameters['buildId'] = self._serialize.query('build_id', build_id, 'int')
        if publish_context is not None:
            query_parameters['publishContext'] = self._serialize.query('publish_context', publish_context, 'str')
        if outcomes is not None:
            outcomes = ",".join(map(str, outcomes))
            query_parameters['outcomes'] = self._serialize.query('outcomes', outcomes, 'str')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        response = self._send(http_method='GET',
                              location_id='f48cc885-dbc4-4efc-ab19-ae8c19d1e02a',
                              version='7.2-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[ShallowTestCaseResult]', self._unwrap_collection(response))

    def get_test_results_by_pipeline(self, project, pipeline_id, stage_name=None, phase_name=None, job_name=None, outcomes=None, top=None, continuation_token=None):
        """GetTestResultsByPipeline.
        [Preview API] Get a list of results.
        :param str project: Project ID or project name
        :param int pipeline_id: Pipeline Id. This is same as build Id.
        :param str stage_name: Name of the stage. Maximum supported length for name is 256 character.
        :param str phase_name: Name of the phase. Maximum supported length for name is 256 character.
        :param str job_name: Matrixing in YAML generates copies of a job with different inputs in matrix. JobName is the name of those input. Maximum supported length for name is 256 character.
        :param [TestOutcome] outcomes: List of outcome of results
        :param int top: Maximum number of results to return
        :param String continuation_token: Header to pass the continuationToken
        :rtype: :class:`<[ShallowTestCaseResult]> <azure.devops.v7_2.test_results.models.[ShallowTestCaseResult]>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if pipeline_id is not None:
            query_parameters['pipelineId'] = self._serialize.query('pipeline_id', pipeline_id, 'int')
        if stage_name is not None:
            query_parameters['stageName'] = self._serialize.query('stage_name', stage_name, 'str')
        if phase_name is not None:
            query_parameters['phaseName'] = self._serialize.query('phase_name', phase_name, 'str')
        if job_name is not None:
            query_parameters['jobName'] = self._serialize.query('job_name', job_name, 'str')
        if outcomes is not None:
            outcomes = ",".join(map(str, outcomes))
            query_parameters['outcomes'] = self._serialize.query('outcomes', outcomes, 'str')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        additional_headers = {}
        if continuation_token is not None:
            additional_headers['x-ms-continuationtoken'] = continuation_token
        response = self._send(http_method='GET',
                              location_id='80169dc2-30c3-4c25-84b2-dd67d7ff1f52',
                              version='7.2-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              additional_headers=additional_headers)
        return self._deserialize('[ShallowTestCaseResult]', self._unwrap_collection(response))

    def get_test_results_by_release(self, project, release_id, release_envid=None, publish_context=None, outcomes=None, top=None, continuation_token=None):
        """GetTestResultsByRelease.
        [Preview API]
        :param str project: Project ID or project name
        :param int release_id:
        :param int release_envid:
        :param str publish_context:
        :param [TestOutcome] outcomes:
        :param int top:
        :param str continuation_token:
        :rtype: :class:`<[ShallowTestCaseResult]> <azure.devops.v7_2.test_results.models.[ShallowTestCaseResult]>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if release_id is not None:
            query_parameters['releaseId'] = self._serialize.query('release_id', release_id, 'int')
        if release_envid is not None:
            query_parameters['releaseEnvid'] = self._serialize.query('release_envid', release_envid, 'int')
        if publish_context is not None:
            query_parameters['publishContext'] = self._serialize.query('publish_context', publish_context, 'str')
        if outcomes is not None:
            outcomes = ",".join(map(str, outcomes))
            query_parameters['outcomes'] = self._serialize.query('outcomes', outcomes, 'str')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        response = self._send(http_method='GET',
                              location_id='3994b949-77e5-495d-8034-edf80d95b84e',
                              version='7.2-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[ShallowTestCaseResult]', self._unwrap_collection(response))

    def test_results_group_details(self, project, pipeline_id, stage_name=None, phase_name=None, job_name=None, should_include_failed_and_aborted_results=None, query_group_summary_for_in_progress=None):
        """TestResultsGroupDetails.
        [Preview API] Get all the available groups details and for these groups get failed and aborted results.
        :param str project: Project ID or project name
        :param int pipeline_id: Pipeline Id. This is same as build Id.
        :param str stage_name: Name of the stage. Maximum supported length for name is 256 character.
        :param str phase_name: Name of the phase. Maximum supported length for name is 256 character.
        :param str job_name: Matrixing in YAML generates copies of a job with different inputs in matrix. JobName is the name of those input. Maximum supported length for name is 256 character.
        :param bool should_include_failed_and_aborted_results: If true, it will return Ids of failed and aborted results for each test group
        :param bool query_group_summary_for_in_progress: If true, it will calculate summary for InProgress runs as well.
        :rtype: :class:`<TestResultsDetails> <azure.devops.v7_2.test_results.models.TestResultsDetails>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if pipeline_id is not None:
            query_parameters['pipelineId'] = self._serialize.query('pipeline_id', pipeline_id, 'int')
        if stage_name is not None:
            query_parameters['stageName'] = self._serialize.query('stage_name', stage_name, 'str')
        if phase_name is not None:
            query_parameters['phaseName'] = self._serialize.query('phase_name', phase_name, 'str')
        if job_name is not None:
            query_parameters['jobName'] = self._serialize.query('job_name', job_name, 'str')
        if should_include_failed_and_aborted_results is not None:
            query_parameters['shouldIncludeFailedAndAbortedResults'] = self._serialize.query('should_include_failed_and_aborted_results', should_include_failed_and_aborted_results, 'bool')
        if query_group_summary_for_in_progress is not None:
            query_parameters['queryGroupSummaryForInProgress'] = self._serialize.query('query_group_summary_for_in_progress', query_group_summary_for_in_progress, 'bool')
        response = self._send(http_method='GET',
                              location_id='f903b850-06af-4b50-a344-d7bbfb19e93b',
                              version='7.2-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestResultsDetails', response)

    def query_test_results_report_for_build(self, project, build_id, publish_context=None, include_failure_details=None, build_to_compare=None):
        """QueryTestResultsReportForBuild.
        [Preview API]
        :param str project: Project ID or project name
        :param int build_id:
        :param str publish_context:
        :param bool include_failure_details:
        :param :class:`<BuildReference> <azure.devops.v7_2.test_results.models.BuildReference>` build_to_compare:
        :rtype: :class:`<TestResultSummary> <azure.devops.v7_2.test_results.models.TestResultSummary>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if build_id is not None:
            query_parameters['buildId'] = self._serialize.query('build_id', build_id, 'int')
        if publish_context is not None:
            query_parameters['publishContext'] = self._serialize.query('publish_context', publish_context, 'str')
        if include_failure_details is not None:
            query_parameters['includeFailureDetails'] = self._serialize.query('include_failure_details', include_failure_details, 'bool')
        if build_to_compare is not None:
            if build_to_compare.id is not None:
                query_parameters['buildToCompare.id'] = build_to_compare.id
            if build_to_compare.definition_id is not None:
                query_parameters['buildToCompare.definitionId'] = build_to_compare.definition_id
            if build_to_compare.number is not None:
                query_parameters['buildToCompare.number'] = build_to_compare.number
            if build_to_compare.uri is not None:
                query_parameters['buildToCompare.uri'] = build_to_compare.uri
            if build_to_compare.build_system is not None:
                query_parameters['buildToCompare.buildSystem'] = build_to_compare.build_system
            if build_to_compare.branch_name is not None:
                query_parameters['buildToCompare.branchName'] = build_to_compare.branch_name
            if build_to_compare.repository_id is not None:
                query_parameters['buildToCompare.repositoryId'] = build_to_compare.repository_id
        response = self._send(http_method='GET',
                              location_id='e009fa95-95a5-4ad4-9681-590043ce2423',
                              version='7.2-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestResultSummary', response)

    def query_test_results_report_for_pipeline(self, project, pipeline_id, stage_name=None, phase_name=None, job_name=None, include_failure_details=None):
        """QueryTestResultsReportForPipeline.
        [Preview API] Get summary of test results.
        :param str project: Project ID or project name
        :param int pipeline_id: Pipeline Id. This is same as build Id.
        :param str stage_name: Name of the stage. Maximum supported length for name is 256 character.
        :param str phase_name: Name of the phase. Maximum supported length for name is 256 character.
        :param str job_name: Matrixing in YAML generates copies of a job with different inputs in matrix. JobName is the name of those input. Maximum supported length for name is 256 character.
        :param bool include_failure_details: If true returns failure insights
        :rtype: :class:`<TestResultSummary> <azure.devops.v7_2.test_results.models.TestResultSummary>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if pipeline_id is not None:
            query_parameters['pipelineId'] = self._serialize.query('pipeline_id', pipeline_id, 'int')
        if stage_name is not None:
            query_parameters['stageName'] = self._serialize.query('stage_name', stage_name, 'str')
        if phase_name is not None:
            query_parameters['phaseName'] = self._serialize.query('phase_name', phase_name, 'str')
        if job_name is not None:
            query_parameters['jobName'] = self._serialize.query('job_name', job_name, 'str')
        if include_failure_details is not None:
            query_parameters['includeFailureDetails'] = self._serialize.query('include_failure_details', include_failure_details, 'bool')
        response = self._send(http_method='GET',
                              location_id='71f746a1-7d68-40fe-b705-9d821a73dff2',
                              version='7.2-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestResultSummary', response)

    def query_test_results_report_for_release(self, project, release_id, release_env_id, publish_context=None, include_failure_details=None, release_to_compare=None):
        """QueryTestResultsReportForRelease.
        [Preview API]
        :param str project: Project ID or project name
        :param int release_id:
        :param int release_env_id:
        :param str publish_context:
        :param bool include_failure_details:
        :param :class:`<ReleaseReference> <azure.devops.v7_2.test_results.models.ReleaseReference>` release_to_compare:
        :rtype: :class:`<TestResultSummary> <azure.devops.v7_2.test_results.models.TestResultSummary>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if release_id is not None:
            query_parameters['releaseId'] = self._serialize.query('release_id', release_id, 'int')
        if release_env_id is not None:
            query_parameters['releaseEnvId'] = self._serialize.query('release_env_id', release_env_id, 'int')
        if publish_context is not None:
            query_parameters['publishContext'] = self._serialize.query('publish_context', publish_context, 'str')
        if include_failure_details is not None:
            query_parameters['includeFailureDetails'] = self._serialize.query('include_failure_details', include_failure_details, 'bool')
        if release_to_compare is not None:
            if release_to_compare.id is not None:
                query_parameters['releaseToCompare.id'] = release_to_compare.id
            if release_to_compare.name is not None:
                query_parameters['releaseToCompare.name'] = release_to_compare.name
            if release_to_compare.environment_id is not None:
                query_parameters['releaseToCompare.environmentId'] = release_to_compare.environment_id
            if release_to_compare.environment_name is not None:
                query_parameters['releaseToCompare.environmentName'] = release_to_compare.environment_name
            if release_to_compare.definition_id is not None:
                query_parameters['releaseToCompare.definitionId'] = release_to_compare.definition_id
            if release_to_compare.environment_definition_id is not None:
                query_parameters['releaseToCompare.environmentDefinitionId'] = release_to_compare.environment_definition_id
            if release_to_compare.environment_definition_name is not None:
                query_parameters['releaseToCompare.environmentDefinitionName'] = release_to_compare.environment_definition_name
            if release_to_compare.creation_date is not None:
                query_parameters['releaseToCompare.creationDate'] = release_to_compare.creation_date
            if release_to_compare.environment_creation_date is not None:
                query_parameters['releaseToCompare.environmentCreationDate'] = release_to_compare.environment_creation_date
            if release_to_compare.attempt is not None:
                query_parameters['releaseToCompare.attempt'] = release_to_compare.attempt
        response = self._send(http_method='GET',
                              location_id='f10f9577-2c04-45ab-8c99-b26567a7cd55',
                              version='7.2-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestResultSummary', response)

    def query_test_results_summary_for_releases(self, releases, project):
        """QueryTestResultsSummaryForReleases.
        [Preview API]
        :param [ReleaseReference] releases:
        :param str project: Project ID or project name
        :rtype: [TestResultSummary]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(releases, '[ReleaseReference]')
        response = self._send(http_method='POST',
                              location_id='f10f9577-2c04-45ab-8c99-b26567a7cd55',
                              version='7.2-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[TestResultSummary]', self._unwrap_collection(response))

    def query_test_summary_by_requirement(self, results_context, project, work_item_ids=None):
        """QueryTestSummaryByRequirement.
        [Preview API]
        :param :class:`<TestResultsContext> <azure.devops.v7_2.test_results.models.TestResultsContext>` results_context:
        :param str project: Project ID or project name
        :param [int] work_item_ids:
        :rtype: [TestSummaryForWorkItem]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if work_item_ids is not None:
            work_item_ids = ",".join(map(str, work_item_ids))
            query_parameters['workItemIds'] = self._serialize.query('work_item_ids', work_item_ids, 'str')
        content = self._serialize.body(results_context, 'TestResultsContext')
        response = self._send(http_method='POST',
                              location_id='3b7fd26f-c335-4e55-afc1-a588f5e2af3c',
                              version='7.2-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('[TestSummaryForWorkItem]', self._unwrap_collection(response))

    def query_result_trend_for_build(self, filter, project):
        """QueryResultTrendForBuild.
        [Preview API]
        :param :class:`<TestResultTrendFilter> <azure.devops.v7_2.test_results.models.TestResultTrendFilter>` filter:
        :param str project: Project ID or project name
        :rtype: [AggregatedDataForResultTrend]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(filter, 'TestResultTrendFilter')
        response = self._send(http_method='POST',
                              location_id='0886a7ae-315a-4dba-9122-bcce93301f3a',
                              version='7.2-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[AggregatedDataForResultTrend]', self._unwrap_collection(response))

    def query_result_trend_for_release(self, filter, project):
        """QueryResultTrendForRelease.
        [Preview API]
        :param :class:`<TestResultTrendFilter> <azure.devops.v7_2.test_results.models.TestResultTrendFilter>` filter:
        :param str project: Project ID or project name
        :rtype: [AggregatedDataForResultTrend]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(filter, 'TestResultTrendFilter')
        response = self._send(http_method='POST',
                              location_id='107f23c3-359a-460a-a70c-63ee739f9f9a',
                              version='7.2-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[AggregatedDataForResultTrend]', self._unwrap_collection(response))

    def create_test_run(self, test_run, project):
        """CreateTestRun.
        [Preview API]
        :param :class:`<RunCreateModel> <azure.devops.v7_2.test_results.models.RunCreateModel>` test_run:
        :param str project: Project ID or project name
        :rtype: :class:`<TestRun> <azure.devops.v7_2.test_results.models.TestRun>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(test_run, 'RunCreateModel')
        response = self._send(http_method='POST',
                              location_id='364538f9-8062-4ce0-b024-75a0fb463f0d',
                              version='7.2-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TestRun', response)

    def delete_test_run(self, project, run_id):
        """DeleteTestRun.
        [Preview API]
        :param str project: Project ID or project name
        :param int run_id:
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        self._send(http_method='DELETE',
                   location_id='364538f9-8062-4ce0-b024-75a0fb463f0d',
                   version='7.2-preview.1',
                   route_values=route_values)

    def get_test_run_by_id(self, project, run_id, include_details=None, include_tags=None):
        """GetTestRunById.
        [Preview API]
        :param str project: Project ID or project name
        :param int run_id:
        :param bool include_details:
        :param bool include_tags:
        :rtype: :class:`<TestRun> <azure.devops.v7_2.test_results.models.TestRun>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        query_parameters = {}
        if include_details is not None:
            query_parameters['includeDetails'] = self._serialize.query('include_details', include_details, 'bool')
        if include_tags is not None:
            query_parameters['includeTags'] = self._serialize.query('include_tags', include_tags, 'bool')
        response = self._send(http_method='GET',
                              location_id='364538f9-8062-4ce0-b024-75a0fb463f0d',
                              version='7.2-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestRun', response)

    def get_test_runs(self, project, build_uri=None, owner=None, tmi_run_id=None, plan_id=None, include_run_details=None, automated=None, skip=None, top=None):
        """GetTestRuns.
        [Preview API]
        :param str project: Project ID or project name
        :param str build_uri:
        :param str owner:
        :param str tmi_run_id:
        :param int plan_id:
        :param bool include_run_details:
        :param bool automated:
        :param int skip:
        :param int top:
        :rtype: [TestRun]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if build_uri is not None:
            query_parameters['buildUri'] = self._serialize.query('build_uri', build_uri, 'str')
        if owner is not None:
            query_parameters['owner'] = self._serialize.query('owner', owner, 'str')
        if tmi_run_id is not None:
            query_parameters['tmiRunId'] = self._serialize.query('tmi_run_id', tmi_run_id, 'str')
        if plan_id is not None:
            query_parameters['planId'] = self._serialize.query('plan_id', plan_id, 'int')
        if include_run_details is not None:
            query_parameters['includeRunDetails'] = self._serialize.query('include_run_details', include_run_details, 'bool')
        if automated is not None:
            query_parameters['automated'] = self._serialize.query('automated', automated, 'bool')
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        response = self._send(http_method='GET',
                              location_id='364538f9-8062-4ce0-b024-75a0fb463f0d',
                              version='7.2-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TestRun]', self._unwrap_collection(response))

    def query_test_runs(self, project, min_last_updated_date, max_last_updated_date, state=None, plan_ids=None, is_automated=None, publish_context=None, build_ids=None, build_def_ids=None, branch_name=None, release_ids=None, release_def_ids=None, release_env_ids=None, release_env_def_ids=None, run_title=None, top=None, continuation_token=None):
        """QueryTestRuns.
        [Preview API] Query Test Runs based on filters. Mandatory fields are minLastUpdatedDate and maxLastUpdatedDate.
        :param str project: Project ID or project name
        :param datetime min_last_updated_date: Minimum Last Modified Date of run to be queried (Mandatory).
        :param datetime max_last_updated_date: Maximum Last Modified Date of run to be queried (Mandatory, difference between min and max date can be atmost 7 days).
        :param str state: Current state of the Runs to be queried.
        :param [int] plan_ids: Plan Ids of the Runs to be queried, comma separated list of valid ids.
        :param bool is_automated: Automation type of the Runs to be queried.
        :param str publish_context: PublishContext of the Runs to be queried.
        :param [int] build_ids: Build Ids of the Runs to be queried, comma separated list of valid ids.
        :param [int] build_def_ids: Build Definition Ids of the Runs to be queried, comma separated list of valid ids.
        :param str branch_name: Source Branch name of the Runs to be queried.
        :param [int] release_ids: Release Ids of the Runs to be queried, comma separated list of valid ids.
        :param [int] release_def_ids: Release Definition Ids of the Runs to be queried, comma separated list of valid ids.
        :param [int] release_env_ids: Release Environment Ids of the Runs to be queried, comma separated list of valid ids.
        :param [int] release_env_def_ids: Release Environment Definition Ids of the Runs to be queried, comma separated list of valid ids.
        :param str run_title: Run Title of the Runs to be queried.
        :param int top: Number of runs to be queried. Limit is 100
        :param str continuation_token: continuationToken received from previous batch or null for first batch. It is not supposed to be created (or altered, if received from last batch) by user.
        :rtype: :class:`<[TestRun]> <azure.devops.v7_2.test_results.models.[TestRun]>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if min_last_updated_date is not None:
            query_parameters['minLastUpdatedDate'] = self._serialize.query('min_last_updated_date', min_last_updated_date, 'iso-8601')
        if max_last_updated_date is not None:
            query_parameters['maxLastUpdatedDate'] = self._serialize.query('max_last_updated_date', max_last_updated_date, 'iso-8601')
        if state is not None:
            query_parameters['state'] = self._serialize.query('state', state, 'str')
        if plan_ids is not None:
            plan_ids = ",".join(map(str, plan_ids))
            query_parameters['planIds'] = self._serialize.query('plan_ids', plan_ids, 'str')
        if is_automated is not None:
            query_parameters['isAutomated'] = self._serialize.query('is_automated', is_automated, 'bool')
        if publish_context is not None:
            query_parameters['publishContext'] = self._serialize.query('publish_context', publish_context, 'str')
        if build_ids is not None:
            build_ids = ",".join(map(str, build_ids))
            query_parameters['buildIds'] = self._serialize.query('build_ids', build_ids, 'str')
        if build_def_ids is not None:
            build_def_ids = ",".join(map(str, build_def_ids))
            query_parameters['buildDefIds'] = self._serialize.query('build_def_ids', build_def_ids, 'str')
        if branch_name is not None:
            query_parameters['branchName'] = self._serialize.query('branch_name', branch_name, 'str')
        if release_ids is not None:
            release_ids = ",".join(map(str, release_ids))
            query_parameters['releaseIds'] = self._serialize.query('release_ids', release_ids, 'str')
        if release_def_ids is not None:
            release_def_ids = ",".join(map(str, release_def_ids))
            query_parameters['releaseDefIds'] = self._serialize.query('release_def_ids', release_def_ids, 'str')
        if release_env_ids is not None:
            release_env_ids = ",".join(map(str, release_env_ids))
            query_parameters['releaseEnvIds'] = self._serialize.query('release_env_ids', release_env_ids, 'str')
        if release_env_def_ids is not None:
            release_env_def_ids = ",".join(map(str, release_env_def_ids))
            query_parameters['releaseEnvDefIds'] = self._serialize.query('release_env_def_ids', release_env_def_ids, 'str')
        if run_title is not None:
            query_parameters['runTitle'] = self._serialize.query('run_title', run_title, 'str')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        response = self._send(http_method='GET',
                              location_id='364538f9-8062-4ce0-b024-75a0fb463f0d',
                              version='7.2-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TestRun]', self._unwrap_collection(response))

    def update_test_run(self, run_update_model, project, run_id):
        """UpdateTestRun.
        [Preview API]
        :param :class:`<RunUpdateModel> <azure.devops.v7_2.test_results.models.RunUpdateModel>` run_update_model:
        :param str project: Project ID or project name
        :param int run_id:
        :rtype: :class:`<TestRun> <azure.devops.v7_2.test_results.models.TestRun>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        content = self._serialize.body(run_update_model, 'RunUpdateModel')
        response = self._send(http_method='PATCH',
                              location_id='364538f9-8062-4ce0-b024-75a0fb463f0d',
                              version='7.2-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TestRun', response)

    def get_test_run_summary_by_outcome(self, project, run_id):
        """GetTestRunSummaryByOutcome.
        [Preview API] Get test run summary, used when we want to get summary of a run by outcome. Test run should be in completed state.
        :param str project: Project ID or project name
        :param int run_id: ID of the run to get.
        :rtype: :class:`<TestRunStatistic> <azure.devops.v7_2.test_results.models.TestRunStatistic>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        response = self._send(http_method='GET',
                              location_id='5c6a250c-53b7-4851-990c-42a7a00c8b39',
                              version='7.2-preview.1',
                              route_values=route_values)
        return self._deserialize('TestRunStatistic', response)

    def get_test_results_settings(self, project, settings_type=None):
        """GetTestResultsSettings.
        [Preview API] Get TestResultsSettings data
        :param str project: Project ID or project name
        :param str settings_type:
        :rtype: :class:`<TestResultsSettings> <azure.devops.v7_2.test_results.models.TestResultsSettings>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if settings_type is not None:
            query_parameters['settingsType'] = self._serialize.query('settings_type', settings_type, 'str')
        response = self._send(http_method='GET',
                              location_id='7319952e-e5a9-4e19-a006-84f3be8b7c68',
                              version='7.2-preview.3',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestResultsSettings', response)

    def update_pipelines_test_settings(self, test_results_update_settings, project):
        """UpdatePipelinesTestSettings.
        [Preview API] Update project settings of test results
        :param :class:`<TestResultsUpdateSettings> <azure.devops.v7_2.test_results.models.TestResultsUpdateSettings>` test_results_update_settings:
        :param str project: Project ID or project name
        :rtype: :class:`<TestResultsSettings> <azure.devops.v7_2.test_results.models.TestResultsSettings>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(test_results_update_settings, 'TestResultsUpdateSettings')
        response = self._send(http_method='PATCH',
                              location_id='7319952e-e5a9-4e19-a006-84f3be8b7c68',
                              version='7.2-preview.3',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TestResultsSettings', response)

    def get_similar_test_results(self, project, run_id, test_result_id, test_sub_result_id, top=None, continuation_token=None):
        """GetSimilarTestResults.
        [Preview API] Gets the list of results whose failure matches with the provided one.
        :param str project: Project ID or project name
        :param int run_id: id of test run
        :param int test_result_id: id of test result inside a test run
        :param int test_sub_result_id: id of subresult inside a test result
        :param int top: Maximum number of results to return
        :param String continuation_token: Header to pass the continuationToken
        :rtype: [TestCaseResult]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if test_result_id is not None:
            route_values['testResultId'] = self._serialize.url('test_result_id', test_result_id, 'int')
        query_parameters = {}
        if test_sub_result_id is not None:
            query_parameters['testSubResultId'] = self._serialize.query('test_sub_result_id', test_sub_result_id, 'int')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        additional_headers = {}
        if continuation_token is not None:
            additional_headers['x-ms-continuationtoken'] = continuation_token
        response = self._send(http_method='GET',
                              location_id='67d0a074-b255-4902-a639-e3e6de7a3de6',
                              version='7.2-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              additional_headers=additional_headers)
        return self._deserialize('[TestCaseResult]', self._unwrap_collection(response))

    def get_test_run_statistics(self, project, run_id):
        """GetTestRunStatistics.
        [Preview API] Get test run statistics , used when we want to get summary of a run by outcome.
        :param str project: Project ID or project name
        :param int run_id: ID of the run to get.
        :rtype: :class:`<TestRunStatistic> <azure.devops.v7_2.test_results.models.TestRunStatistic>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        response = self._send(http_method='GET',
                              location_id='82b986e8-ca9e-4a89-b39e-f65c69bc104a',
                              version='7.2-preview.2',
                              route_values=route_values)
        return self._deserialize('TestRunStatistic', response)

    def get_coverage_status_badge(self, project, definition, branch_name=None, label=None):
        """GetCoverageStatusBadge.
        [Preview API] <p>Gets the coverage status for the last successful build of a definition, optionally scoped to a specific branch</p>
        :param str project: Project ID or project name
        :param str definition: The ID or name of the definition.
        :param str branch_name: The branch name.
        :param str label: The String to replace the default text on the left side of the badge.
        :rtype: str
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if definition is not None:
            route_values['definition'] = self._serialize.url('definition', definition, 'str')
        query_parameters = {}
        if branch_name is not None:
            query_parameters['branchName'] = self._serialize.query('branch_name', branch_name, 'str')
        if label is not None:
            query_parameters['label'] = self._serialize.query('label', label, 'str')
        response = self._send(http_method='GET',
                              location_id='73b7c9d8-defb-4b60-b3d6-2162d60d6b13',
                              version='7.2-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('str', response)

    def get_test_tags_for_build(self, project, build_id):
        """GetTestTagsForBuild.
        [Preview API] Get all the tags in a build.
        :param str project: Project ID or project name
        :param int build_id: Build ID
        :rtype: [TestTag]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if build_id is not None:
            query_parameters['buildId'] = self._serialize.query('build_id', build_id, 'int')
        response = self._send(http_method='GET',
                              location_id='52ee2057-4b54-41a6-a18c-ed4375a00f8d',
                              version='7.2-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TestTag]', self._unwrap_collection(response))

    def get_test_tags_for_release(self, project, release_id, release_env_id):
        """GetTestTagsForRelease.
        [Preview API] Get all the tags in a release.
        :param str project: Project ID or project name
        :param int release_id: Release ID
        :param int release_env_id: Release environment ID
        :rtype: [TestTag]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if release_id is not None:
            query_parameters['releaseId'] = self._serialize.query('release_id', release_id, 'int')
        if release_env_id is not None:
            query_parameters['releaseEnvId'] = self._serialize.query('release_env_id', release_env_id, 'int')
        response = self._send(http_method='GET',
                              location_id='52ee2057-4b54-41a6-a18c-ed4375a00f8d',
                              version='7.2-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TestTag]', self._unwrap_collection(response))

    def update_test_run_tags(self, test_tags_update_model, project, run_id):
        """UpdateTestRunTags.
        [Preview API] Update tags of a run, Tags can be Added and Deleted
        :param :class:`<TestTagsUpdateModel> <azure.devops.v7_2.test_results.models.TestTagsUpdateModel>` test_tags_update_model: TestTagsUpdateModel
        :param str project: Project ID or project name
        :param int run_id: RunId of the run
        :rtype: [TestTag]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        content = self._serialize.body(test_tags_update_model, 'TestTagsUpdateModel')
        response = self._send(http_method='PATCH',
                              location_id='a5e2f411-2b43-45f3-989c-05b71339f5b8',
                              version='7.2-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[TestTag]', self._unwrap_collection(response))

    def get_test_tag_summary_for_build(self, project, build_id):
        """GetTestTagSummaryForBuild.
        [Preview API] Get all the tags in a build.
        :param str project: Project ID or project name
        :param int build_id: Build ID
        :rtype: :class:`<TestTagSummary> <azure.devops.v7_2.test_results.models.TestTagSummary>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if build_id is not None:
            query_parameters['buildId'] = self._serialize.query('build_id', build_id, 'int')
        response = self._send(http_method='GET',
                              location_id='655a8f6b-fec7-4b46-b672-68b44141b498',
                              version='7.2-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestTagSummary', response)

    def get_test_tag_summary_for_release(self, project, release_id, release_env_id):
        """GetTestTagSummaryForRelease.
        [Preview API] Get all the tags in a release.
        :param str project: Project ID or project name
        :param int release_id: Release ID
        :param int release_env_id: Release environment ID
        :rtype: :class:`<TestTagSummary> <azure.devops.v7_2.test_results.models.TestTagSummary>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if release_id is not None:
            query_parameters['releaseId'] = self._serialize.query('release_id', release_id, 'int')
        if release_env_id is not None:
            query_parameters['releaseEnvId'] = self._serialize.query('release_env_id', release_env_id, 'int')
        response = self._send(http_method='GET',
                              location_id='655a8f6b-fec7-4b46-b672-68b44141b498',
                              version='7.2-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestTagSummary', response)

    def create_build_attachment_in_log_store(self, attachment_request_model, project, build_id):
        """CreateBuildAttachmentInLogStore.
        [Preview API] Creates an attachment in the LogStore for the specified buildId.
        :param :class:`<TestAttachmentRequestModel> <azure.devops.v7_2.test_results.models.TestAttachmentRequestModel>` attachment_request_model: Contains attachment info like stream, filename, comment, attachmentType
        :param str project: Project ID or project name
        :param int build_id: BuildId
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        content = self._serialize.body(attachment_request_model, 'TestAttachmentRequestModel')
        self._send(http_method='POST',
                   location_id='6f747e16-18c2-435a-b4fb-fa05d6845fee',
                   version='7.2-preview.1',
                   route_values=route_values,
                   content=content)

    def create_test_run_log_store_attachment(self, attachment_request_model, project, run_id):
        """CreateTestRunLogStoreAttachment.
        [Preview API] Creates an attachment in the LogStore for the specified runId.
        :param :class:`<TestAttachmentRequestModel> <azure.devops.v7_2.test_results.models.TestAttachmentRequestModel>` attachment_request_model: Contains attachment info like stream, filename, comment, attachmentType
        :param str project: Project ID or project name
        :param int run_id: Test RunId
        :rtype: :class:`<TestLogStoreAttachmentReference> <azure.devops.v7_2.test_results.models.TestLogStoreAttachmentReference>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        content = self._serialize.body(attachment_request_model, 'TestAttachmentRequestModel')
        response = self._send(http_method='POST',
                              location_id='1026d5de-4b0b-46ae-a31f-7c59b6af51ef',
                              version='7.2-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TestLogStoreAttachmentReference', response)

    def delete_test_run_log_store_attachment(self, project, run_id, filename):
        """DeleteTestRunLogStoreAttachment.
        [Preview API] Deletes the attachment with the specified filename for the specified runId from the LogStore.
        :param str project: Project ID or project name
        :param int run_id: Test RunId
        :param str filename: Attachment FileName
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        query_parameters = {}
        if filename is not None:
            query_parameters['filename'] = self._serialize.query('filename', filename, 'str')
        self._send(http_method='DELETE',
                   location_id='1026d5de-4b0b-46ae-a31f-7c59b6af51ef',
                   version='7.2-preview.1',
                   route_values=route_values,
                   query_parameters=query_parameters)

    def get_test_run_log_store_attachment_content(self, project, run_id, filename, **kwargs):
        """GetTestRunLogStoreAttachmentContent.
        [Preview API] Returns the attachment with the specified filename for the specified runId from the LogStore.
        :param str project: Project ID or project name
        :param int run_id: Test RunId
        :param str filename: Attachment FileName
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        query_parameters = {}
        if filename is not None:
            query_parameters['filename'] = self._serialize.query('filename', filename, 'str')
        response = self._send(http_method='GET',
                              location_id='1026d5de-4b0b-46ae-a31f-7c59b6af51ef',
                              version='7.2-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='application/octet-stream')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_test_run_log_store_attachments(self, project, run_id):
        """GetTestRunLogStoreAttachments.
        [Preview API] Returns a list of attachments for the specified runId from the LogStore.
        :param str project: Project ID or project name
        :param int run_id: Test RunId
        :rtype: [TestLogStoreAttachment]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        response = self._send(http_method='GET',
                              location_id='1026d5de-4b0b-46ae-a31f-7c59b6af51ef',
                              version='7.2-preview.1',
                              route_values=route_values)
        return self._deserialize('[TestLogStoreAttachment]', self._unwrap_collection(response))

    def get_test_run_log_store_attachment_zip(self, project, run_id, filename, **kwargs):
        """GetTestRunLogStoreAttachmentZip.
        [Preview API] Returns the attachment with the specified filename for the specified runId from the LogStore.
        :param str project: Project ID or project name
        :param int run_id: Test RunId
        :param str filename: Attachment FileName
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        query_parameters = {}
        if filename is not None:
            query_parameters['filename'] = self._serialize.query('filename', filename, 'str')
        response = self._send(http_method='GET',
                              location_id='1026d5de-4b0b-46ae-a31f-7c59b6af51ef',
                              version='7.2-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='application/zip')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def create_failure_type(self, test_result_failure_type, project):
        """CreateFailureType.
        [Preview API] Creates a new test failure type
        :param :class:`<TestResultFailureTypeRequestModel> <azure.devops.v7_2.test_results.models.TestResultFailureTypeRequestModel>` test_result_failure_type:
        :param str project: Project ID or project name
        :rtype: :class:`<TestResultFailureType> <azure.devops.v7_2.test_results.models.TestResultFailureType>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(test_result_failure_type, 'TestResultFailureTypeRequestModel')
        response = self._send(http_method='POST',
                              location_id='c4ac0486-830c-4a2a-9ef9-e8a1791a70fd',
                              version='7.2-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TestResultFailureType', response)

    def delete_failure_type(self, project, failure_type_id):
        """DeleteFailureType.
        [Preview API] Deletes a test failure type with specified failureTypeId
        :param str project: Project ID or project name
        :param int failure_type_id:
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if failure_type_id is not None:
            route_values['failureTypeId'] = self._serialize.url('failure_type_id', failure_type_id, 'int')
        self._send(http_method='DELETE',
                   location_id='c4ac0486-830c-4a2a-9ef9-e8a1791a70fd',
                   version='7.2-preview.1',
                   route_values=route_values)

    def get_failure_types(self, project):
        """GetFailureTypes.
        [Preview API] Returns the list of test failure types.
        :param str project: Project ID or project name
        :rtype: [TestResultFailureType]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        response = self._send(http_method='GET',
                              location_id='c4ac0486-830c-4a2a-9ef9-e8a1791a70fd',
                              version='7.2-preview.1',
                              route_values=route_values)
        return self._deserialize('[TestResultFailureType]', self._unwrap_collection(response))

    def query_test_history(self, filter, project):
        """QueryTestHistory.
        [Preview API] Get history of a test method using TestHistoryQuery
        :param :class:`<TestHistoryQuery> <azure.devops.v7_2.test_results.models.TestHistoryQuery>` filter: TestHistoryQuery to get history
        :param str project: Project ID or project name
        :rtype: :class:`<TestHistoryQuery> <azure.devops.v7_2.test_results.models.TestHistoryQuery>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(filter, 'TestHistoryQuery')
        response = self._send(http_method='POST',
                              location_id='2a41bd6a-8118-4403-b74e-5ba7492aed9d',
                              version='7.2-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TestHistoryQuery', response)

    def get_test_logs_for_build(self, project, build_id, type, directory_path=None, file_name_prefix=None, fetch_meta_data=None, top=None, continuation_token=None):
        """GetTestLogsForBuild.
        [Preview API] Get list of build attachments reference
        :param str project: Project ID or project name
        :param int build_id: Id of the build to get
        :param str type: type of the attachment to get
        :param str directory_path: directory path for which attachments are needed
        :param str file_name_prefix: file name prefix to filter the list of attachment
        :param bool fetch_meta_data: Default is false, set if metadata is needed
        :param int top: Number of test attachments reference to return
        :param String continuation_token: Header to pass the continuationToken
        :rtype: :class:`<[TestLog]> <azure.devops.v7_2.test_results.models.[TestLog]>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if build_id is not None:
            query_parameters['buildId'] = self._serialize.query('build_id', build_id, 'int')
        if type is not None:
            query_parameters['type'] = self._serialize.query('type', type, 'str')
        if directory_path is not None:
            query_parameters['directoryPath'] = self._serialize.query('directory_path', directory_path, 'str')
        if file_name_prefix is not None:
            query_parameters['fileNamePrefix'] = self._serialize.query('file_name_prefix', file_name_prefix, 'str')
        if fetch_meta_data is not None:
            query_parameters['fetchMetaData'] = self._serialize.query('fetch_meta_data', fetch_meta_data, 'bool')
        if top is not None:
            query_parameters['top'] = self._serialize.query('top', top, 'int')
        additional_headers = {}
        if continuation_token is not None:
            additional_headers['x-ms-continuationtoken'] = continuation_token
        response = self._send(http_method='GET',
                              location_id='dff8ce3a-e539-4817-a405-d968491a88f1',
                              version='7.2-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              additional_headers=additional_headers)
        return self._deserialize('[TestLog]', self._unwrap_collection(response))

    def get_test_result_logs(self, project, run_id, result_id, type, directory_path=None, file_name_prefix=None, fetch_meta_data=None, top=None, continuation_token=None):
        """GetTestResultLogs.
        [Preview API] Get list of test result attachments reference
        :param str project: Project ID or project name
        :param int run_id: Id of the test run that contains the result
        :param int result_id: Id of the test result
        :param str type: type of attachments to get
        :param str directory_path: directory path of attachments to get
        :param str file_name_prefix: file name prefix to filter the list of attachment
        :param bool fetch_meta_data: Default is false, set if metadata is needed
        :param int top: Numbe of attachments reference to return
        :param String continuation_token: Header to pass the continuationToken
        :rtype: :class:`<[TestLog]> <azure.devops.v7_2.test_results.models.[TestLog]>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if result_id is not None:
            route_values['resultId'] = self._serialize.url('result_id', result_id, 'int')
        query_parameters = {}
        if type is not None:
            query_parameters['type'] = self._serialize.query('type', type, 'str')
        if directory_path is not None:
            query_parameters['directoryPath'] = self._serialize.query('directory_path', directory_path, 'str')
        if file_name_prefix is not None:
            query_parameters['fileNamePrefix'] = self._serialize.query('file_name_prefix', file_name_prefix, 'str')
        if fetch_meta_data is not None:
            query_parameters['fetchMetaData'] = self._serialize.query('fetch_meta_data', fetch_meta_data, 'bool')
        if top is not None:
            query_parameters['top'] = self._serialize.query('top', top, 'int')
        additional_headers = {}
        if continuation_token is not None:
            additional_headers['x-ms-continuationtoken'] = continuation_token
        response = self._send(http_method='GET',
                              location_id='714caaac-ae1e-4869-8323-9bc0f5120dbf',
                              version='7.2-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              additional_headers=additional_headers)
        return self._deserialize('[TestLog]', self._unwrap_collection(response))

    def get_test_sub_result_logs(self, project, run_id, result_id, sub_result_id, type, directory_path=None, file_name_prefix=None, fetch_meta_data=None, top=None, continuation_token=None):
        """GetTestSubResultLogs.
        [Preview API] Get list of test subresult attachments reference
        :param str project: Project ID or project name
        :param int run_id: Id of the test run that contains the results
        :param int result_id: Id of the test result that contains subresult
        :param int sub_result_id: Id of the test subresult
        :param str type: type of the attachments to get
        :param str directory_path: directory path of the attachment to get
        :param str file_name_prefix: file name prefix to filter the list of attachments
        :param bool fetch_meta_data: Default is false, set if metadata is needed
        :param int top: Number of attachments reference to return
        :param String continuation_token: Header to pass the continuationToken
        :rtype: :class:`<[TestLog]> <azure.devops.v7_2.test_results.models.[TestLog]>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if result_id is not None:
            route_values['resultId'] = self._serialize.url('result_id', result_id, 'int')
        query_parameters = {}
        if sub_result_id is not None:
            query_parameters['subResultId'] = self._serialize.query('sub_result_id', sub_result_id, 'int')
        if type is not None:
            query_parameters['type'] = self._serialize.query('type', type, 'str')
        if directory_path is not None:
            query_parameters['directoryPath'] = self._serialize.query('directory_path', directory_path, 'str')
        if file_name_prefix is not None:
            query_parameters['fileNamePrefix'] = self._serialize.query('file_name_prefix', file_name_prefix, 'str')
        if fetch_meta_data is not None:
            query_parameters['fetchMetaData'] = self._serialize.query('fetch_meta_data', fetch_meta_data, 'bool')
        if top is not None:
            query_parameters['top'] = self._serialize.query('top', top, 'int')
        additional_headers = {}
        if continuation_token is not None:
            additional_headers['x-ms-continuationtoken'] = continuation_token
        response = self._send(http_method='GET',
                              location_id='714caaac-ae1e-4869-8323-9bc0f5120dbf',
                              version='7.2-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              additional_headers=additional_headers)
        return self._deserialize('[TestLog]', self._unwrap_collection(response))

    def get_test_run_logs(self, project, run_id, type, directory_path=None, file_name_prefix=None, fetch_meta_data=None, top=None, continuation_token=None):
        """GetTestRunLogs.
        [Preview API] Get list of test run attachments reference
        :param str project: Project ID or project name
        :param int run_id: Id of the test run
        :param str type: type of the attachments to get
        :param str directory_path: directory path for which attachments are needed
        :param str file_name_prefix: file name prefix to filter the list of attachment
        :param bool fetch_meta_data: Default is false, set if metadata is needed
        :param int top: Number of attachments reference to return
        :param String continuation_token: Header to pass the continuationToken
        :rtype: :class:`<[TestLog]> <azure.devops.v7_2.test_results.models.[TestLog]>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        query_parameters = {}
        if type is not None:
            query_parameters['type'] = self._serialize.query('type', type, 'str')
        if directory_path is not None:
            query_parameters['directoryPath'] = self._serialize.query('directory_path', directory_path, 'str')
        if file_name_prefix is not None:
            query_parameters['fileNamePrefix'] = self._serialize.query('file_name_prefix', file_name_prefix, 'str')
        if fetch_meta_data is not None:
            query_parameters['fetchMetaData'] = self._serialize.query('fetch_meta_data', fetch_meta_data, 'bool')
        if top is not None:
            query_parameters['top'] = self._serialize.query('top', top, 'int')
        additional_headers = {}
        if continuation_token is not None:
            additional_headers['x-ms-continuationtoken'] = continuation_token
        response = self._send(http_method='GET',
                              location_id='5b47b946-e875-4c9a-acdc-2a20996caebe',
                              version='7.2-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              additional_headers=additional_headers)
        return self._deserialize('[TestLog]', self._unwrap_collection(response))

    def get_test_log_store_endpoint_details_for_build_log(self, project, build, type, file_path):
        """GetTestLogStoreEndpointDetailsForBuildLog.
        [Preview API] Get SAS Uri of a build attachment
        :param str project: Project ID or project name
        :param int build: Id of the build to get
        :param str type: type of the file
        :param str file_path: filePath for which sas uri is needed
        :rtype: :class:`<TestLogStoreEndpointDetails> <azure.devops.v7_2.test_results.models.TestLogStoreEndpointDetails>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if build is not None:
            query_parameters['build'] = self._serialize.query('build', build, 'int')
        if type is not None:
            query_parameters['type'] = self._serialize.query('type', type, 'str')
        if file_path is not None:
            query_parameters['filePath'] = self._serialize.query('file_path', file_path, 'str')
        response = self._send(http_method='GET',
                              location_id='39b09be7-f0c9-4a83-a513-9ae31b45c56f',
                              version='7.2-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestLogStoreEndpointDetails', response)

    def test_log_store_endpoint_details_for_build(self, project, build_id, test_log_store_operation_type):
        """TestLogStoreEndpointDetailsForBuild.
        [Preview API] Create and Get sas uri of the build container
        :param str project: Project ID or project name
        :param int build_id: Id of the build to get
        :param str test_log_store_operation_type: Type of operation to perform using sas uri
        :rtype: :class:`<TestLogStoreEndpointDetails> <azure.devops.v7_2.test_results.models.TestLogStoreEndpointDetails>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if build_id is not None:
            query_parameters['buildId'] = self._serialize.query('build_id', build_id, 'int')
        if test_log_store_operation_type is not None:
            query_parameters['testLogStoreOperationType'] = self._serialize.query('test_log_store_operation_type', test_log_store_operation_type, 'str')
        response = self._send(http_method='POST',
                              location_id='39b09be7-f0c9-4a83-a513-9ae31b45c56f',
                              version='7.2-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestLogStoreEndpointDetails', response)

    def get_test_log_store_endpoint_details_for_result_log(self, project, run_id, result_id, type, file_path):
        """GetTestLogStoreEndpointDetailsForResultLog.
        [Preview API] Get SAS Uri of a test results attachment
        :param str project: Project ID or project name
        :param int run_id: Id of the test run that contains result
        :param int result_id: Id of the test result whose files need to be downloaded
        :param str type: type of the file
        :param str file_path: filePath for which sas uri is needed
        :rtype: :class:`<TestLogStoreEndpointDetails> <azure.devops.v7_2.test_results.models.TestLogStoreEndpointDetails>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if result_id is not None:
            route_values['resultId'] = self._serialize.url('result_id', result_id, 'int')
        query_parameters = {}
        if type is not None:
            query_parameters['type'] = self._serialize.query('type', type, 'str')
        if file_path is not None:
            query_parameters['filePath'] = self._serialize.query('file_path', file_path, 'str')
        response = self._send(http_method='GET',
                              location_id='da630b37-1236-45b5-945e-1d7bdb673850',
                              version='7.2-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestLogStoreEndpointDetails', response)

    def get_test_log_store_endpoint_details_for_sub_result_log(self, project, run_id, result_id, sub_result_id, type, file_path):
        """GetTestLogStoreEndpointDetailsForSubResultLog.
        [Preview API] Get SAS Uri of a test subresults attachment
        :param str project: Project ID or project name
        :param int run_id: Id of the test run that contains result
        :param int result_id: Id of the test result that contains subresult
        :param int sub_result_id: Id of the test subresult whose file sas uri is needed
        :param str type: type of the file
        :param str file_path: filePath for which sas uri is needed
        :rtype: :class:`<TestLogStoreEndpointDetails> <azure.devops.v7_2.test_results.models.TestLogStoreEndpointDetails>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if result_id is not None:
            route_values['resultId'] = self._serialize.url('result_id', result_id, 'int')
        query_parameters = {}
        if sub_result_id is not None:
            query_parameters['subResultId'] = self._serialize.query('sub_result_id', sub_result_id, 'int')
        if type is not None:
            query_parameters['type'] = self._serialize.query('type', type, 'str')
        if file_path is not None:
            query_parameters['filePath'] = self._serialize.query('file_path', file_path, 'str')
        response = self._send(http_method='GET',
                              location_id='da630b37-1236-45b5-945e-1d7bdb673850',
                              version='7.2-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestLogStoreEndpointDetails', response)

    def test_log_store_endpoint_details_for_result(self, project, run_id, result_id, sub_result_id, file_path, type):
        """TestLogStoreEndpointDetailsForResult.
        [Preview API] Create empty file for a result and Get Sas uri for the file
        :param str project: Project ID or project name
        :param int run_id: Id of the test run that contains the result
        :param int result_id: Id of the test results that contains sub result
        :param int sub_result_id: Id of the test sub result whose file sas uri is needed
        :param str file_path: file path inside the sub result for which sas uri is needed
        :param str type: Type of the file for download
        :rtype: :class:`<TestLogStoreEndpointDetails> <azure.devops.v7_2.test_results.models.TestLogStoreEndpointDetails>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if result_id is not None:
            route_values['resultId'] = self._serialize.url('result_id', result_id, 'int')
        query_parameters = {}
        if sub_result_id is not None:
            query_parameters['subResultId'] = self._serialize.query('sub_result_id', sub_result_id, 'int')
        if file_path is not None:
            query_parameters['filePath'] = self._serialize.query('file_path', file_path, 'str')
        if type is not None:
            query_parameters['type'] = self._serialize.query('type', type, 'str')
        response = self._send(http_method='POST',
                              location_id='da630b37-1236-45b5-945e-1d7bdb673850',
                              version='7.2-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestLogStoreEndpointDetails', response)

    def get_test_log_store_endpoint_details_for_run_log(self, project, run_id, type, file_path):
        """GetTestLogStoreEndpointDetailsForRunLog.
        [Preview API] Get SAS Uri of a test run attachment
        :param str project: Project ID or project name
        :param int run_id: Id of the test run whose file has to be downloaded
        :param str type: type of the file
        :param str file_path: filePath for which sas uri is needed
        :rtype: :class:`<TestLogStoreEndpointDetails> <azure.devops.v7_2.test_results.models.TestLogStoreEndpointDetails>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        query_parameters = {}
        if type is not None:
            query_parameters['type'] = self._serialize.query('type', type, 'str')
        if file_path is not None:
            query_parameters['filePath'] = self._serialize.query('file_path', file_path, 'str')
        response = self._send(http_method='GET',
                              location_id='67eb3f92-6c97-4fd9-8b63-6cbdc7e526ea',
                              version='7.2-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestLogStoreEndpointDetails', response)

    def test_log_store_endpoint_details_for_run(self, project, run_id, test_log_store_operation_type, file_path=None, type=None):
        """TestLogStoreEndpointDetailsForRun.
        [Preview API] Create empty file for a run and Get Sas uri for the file
        :param str project: Project ID or project name
        :param int run_id: Id of the run to get endpoint details
        :param str test_log_store_operation_type: Type of operation to perform using sas uri
        :param str file_path: file path to create an empty file
        :param str type: Default is GeneralAttachment, type of empty file to be created
        :rtype: :class:`<TestLogStoreEndpointDetails> <azure.devops.v7_2.test_results.models.TestLogStoreEndpointDetails>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        query_parameters = {}
        if test_log_store_operation_type is not None:
            query_parameters['testLogStoreOperationType'] = self._serialize.query('test_log_store_operation_type', test_log_store_operation_type, 'str')
        if file_path is not None:
            query_parameters['filePath'] = self._serialize.query('file_path', file_path, 'str')
        if type is not None:
            query_parameters['type'] = self._serialize.query('type', type, 'str')
        response = self._send(http_method='POST',
                              location_id='67eb3f92-6c97-4fd9-8b63-6cbdc7e526ea',
                              version='7.2-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestLogStoreEndpointDetails', response)

    def create_test_settings(self, test_settings, project):
        """CreateTestSettings.
        [Preview API]
        :param :class:`<TestSettings> <azure.devops.v7_2.test_results.models.TestSettings>` test_settings:
        :param str project: Project ID or project name
        :rtype: int
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(test_settings, 'TestSettings')
        response = self._send(http_method='POST',
                              location_id='930bad47-f826-4099-9597-f44d0a9c735c',
                              version='7.2-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('int', response)

    def delete_test_settings(self, project, test_settings_id):
        """DeleteTestSettings.
        [Preview API]
        :param str project: Project ID or project name
        :param int test_settings_id:
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if test_settings_id is not None:
            query_parameters['testSettingsId'] = self._serialize.query('test_settings_id', test_settings_id, 'int')
        self._send(http_method='DELETE',
                   location_id='930bad47-f826-4099-9597-f44d0a9c735c',
                   version='7.2-preview.1',
                   route_values=route_values,
                   query_parameters=query_parameters)

    def get_test_settings_by_id(self, project, test_settings_id):
        """GetTestSettingsById.
        [Preview API]
        :param str project: Project ID or project name
        :param int test_settings_id:
        :rtype: :class:`<TestSettings> <azure.devops.v7_2.test_results.models.TestSettings>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if test_settings_id is not None:
            query_parameters['testSettingsId'] = self._serialize.query('test_settings_id', test_settings_id, 'int')
        response = self._send(http_method='GET',
                              location_id='930bad47-f826-4099-9597-f44d0a9c735c',
                              version='7.2-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestSettings', response)

    def add_work_item_to_test_links(self, work_item_to_test_links, project):
        """AddWorkItemToTestLinks.
        [Preview API]
        :param :class:`<WorkItemToTestLinks> <azure.devops.v7_2.test_results.models.WorkItemToTestLinks>` work_item_to_test_links:
        :param str project: Project ID or project name
        :rtype: :class:`<WorkItemToTestLinks> <azure.devops.v7_2.test_results.models.WorkItemToTestLinks>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(work_item_to_test_links, 'WorkItemToTestLinks')
        response = self._send(http_method='POST',
                              location_id='4e3abe63-ca46-4fe0-98b2-363f7ec7aa5f',
                              version='7.2-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('WorkItemToTestLinks', response)

    def delete_test_method_to_work_item_link(self, project, test_name, work_item_id):
        """DeleteTestMethodToWorkItemLink.
        [Preview API]
        :param str project: Project ID or project name
        :param str test_name:
        :param int work_item_id:
        :rtype: bool
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if test_name is not None:
            query_parameters['testName'] = self._serialize.query('test_name', test_name, 'str')
        if work_item_id is not None:
            query_parameters['workItemId'] = self._serialize.query('work_item_id', work_item_id, 'int')
        response = self._send(http_method='DELETE',
                              location_id='cbd50bd7-f7ed-4e35-b127-4408ae6bfa2c',
                              version='7.2-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('bool', response)

    def query_test_method_linked_work_items(self, project, test_name):
        """QueryTestMethodLinkedWorkItems.
        [Preview API]
        :param str project: Project ID or project name
        :param str test_name:
        :rtype: :class:`<TestToWorkItemLinks> <azure.devops.v7_2.test_results.models.TestToWorkItemLinks>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if test_name is not None:
            query_parameters['testName'] = self._serialize.query('test_name', test_name, 'str')
        response = self._send(http_method='POST',
                              location_id='cbd50bd7-f7ed-4e35-b127-4408ae6bfa2c',
                              version='7.2-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestToWorkItemLinks', response)

    def get_test_result_work_items_by_id(self, project, run_id, test_case_result_id):
        """GetTestResultWorkItemsById.
        [Preview API]
        :param str project: Project ID or project name
        :param int run_id:
        :param int test_case_result_id:
        :rtype: [WorkItemReference]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if test_case_result_id is not None:
            route_values['testCaseResultId'] = self._serialize.url('test_case_result_id', test_case_result_id, 'int')
        response = self._send(http_method='GET',
                              location_id='3d032fd6-e7a0-468b-b105-75d206f99aad',
                              version='7.2-preview.2',
                              route_values=route_values)
        return self._deserialize('[WorkItemReference]', self._unwrap_collection(response))

    def query_test_result_work_items(self, project, work_item_category, automated_test_name=None, test_case_id=None, max_complete_date=None, days=None, work_item_count=None):
        """QueryTestResultWorkItems.
        [Preview API] Query Test Result WorkItems based on filter
        :param str project: Project ID or project name
        :param str work_item_category: can take values Microsoft.BugCategory or all(for getting all workitems)
        :param str automated_test_name:
        :param int test_case_id:
        :param datetime max_complete_date:
        :param int days:
        :param int work_item_count:
        :rtype: [WorkItemReference]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if work_item_category is not None:
            query_parameters['workItemCategory'] = self._serialize.query('work_item_category', work_item_category, 'str')
        if automated_test_name is not None:
            query_parameters['automatedTestName'] = self._serialize.query('automated_test_name', automated_test_name, 'str')
        if test_case_id is not None:
            query_parameters['testCaseId'] = self._serialize.query('test_case_id', test_case_id, 'int')
        if max_complete_date is not None:
            query_parameters['maxCompleteDate'] = self._serialize.query('max_complete_date', max_complete_date, 'iso-8601')
        if days is not None:
            query_parameters['days'] = self._serialize.query('days', days, 'int')
        if work_item_count is not None:
            query_parameters['$workItemCount'] = self._serialize.query('work_item_count', work_item_count, 'int')
        response = self._send(http_method='GET',
                              location_id='f7401a26-331b-44fe-a470-f7ed35138e4a',
                              version='7.2-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[WorkItemReference]', self._unwrap_collection(response))

