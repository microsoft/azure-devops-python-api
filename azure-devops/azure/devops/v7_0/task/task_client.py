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


class TaskClient(Client):
    """Task
    :param str base_url: Service URL
    :param Authentication creds: Authenticated credentials.
    """

    def __init__(self, base_url=None, creds=None):
        super(TaskClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = None

    def get_plan_attachments(self, scope_identifier, hub_name, plan_id, type):
        """GetPlanAttachments.
        :param str scope_identifier: The project GUID to scope the request
        :param str hub_name: The name of the server hub: "build" for the Build server or "rm" for the Release Management server
        :param str plan_id:
        :param str type:
        :rtype: [TaskAttachment]
        """
        route_values = {}
        if scope_identifier is not None:
            route_values['scopeIdentifier'] = self._serialize.url('scope_identifier', scope_identifier, 'str')
        if hub_name is not None:
            route_values['hubName'] = self._serialize.url('hub_name', hub_name, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'str')
        if type is not None:
            route_values['type'] = self._serialize.url('type', type, 'str')
        response = self._send(http_method='GET',
                              location_id='eb55e5d6-2f30-4295-b5ed-38da50b1fc52',
                              version='7.0',
                              route_values=route_values)
        return self._deserialize('[TaskAttachment]', self._unwrap_collection(response))

    def create_attachment(self, upload_stream, scope_identifier, hub_name, plan_id, timeline_id, record_id, type, name, **kwargs):
        """CreateAttachment.
        :param object upload_stream: Stream to upload
        :param str scope_identifier: The project GUID to scope the request
        :param str hub_name: The name of the server hub: "build" for the Build server or "rm" for the Release Management server
        :param str plan_id:
        :param str timeline_id:
        :param str record_id:
        :param str type:
        :param str name:
        :rtype: :class:`<TaskAttachment> <azure.devops.v7_0.task.models.TaskAttachment>`
        """
        route_values = {}
        if scope_identifier is not None:
            route_values['scopeIdentifier'] = self._serialize.url('scope_identifier', scope_identifier, 'str')
        if hub_name is not None:
            route_values['hubName'] = self._serialize.url('hub_name', hub_name, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'str')
        if timeline_id is not None:
            route_values['timelineId'] = self._serialize.url('timeline_id', timeline_id, 'str')
        if record_id is not None:
            route_values['recordId'] = self._serialize.url('record_id', record_id, 'str')
        if type is not None:
            route_values['type'] = self._serialize.url('type', type, 'str')
        if name is not None:
            route_values['name'] = self._serialize.url('name', name, 'str')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        content = self._client.stream_upload(upload_stream, callback=callback)
        response = self._send(http_method='PUT',
                              location_id='7898f959-9cdf-4096-b29e-7f293031629e',
                              version='7.0',
                              route_values=route_values,
                              content=content,
                              media_type='application/octet-stream')
        return self._deserialize('TaskAttachment', response)

    def create_attachment_from_artifact(self, scope_identifier, hub_name, plan_id, timeline_id, record_id, type, name, artifact_hash, length):
        """CreateAttachmentFromArtifact.
        :param str scope_identifier: The project GUID to scope the request
        :param str hub_name: The name of the server hub: "build" for the Build server or "rm" for the Release Management server
        :param str plan_id:
        :param str timeline_id:
        :param str record_id:
        :param str type:
        :param str name:
        :param str artifact_hash:
        :param long length:
        :rtype: :class:`<TaskAttachment> <azure.devops.v7_0.task.models.TaskAttachment>`
        """
        route_values = {}
        if scope_identifier is not None:
            route_values['scopeIdentifier'] = self._serialize.url('scope_identifier', scope_identifier, 'str')
        if hub_name is not None:
            route_values['hubName'] = self._serialize.url('hub_name', hub_name, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'str')
        if timeline_id is not None:
            route_values['timelineId'] = self._serialize.url('timeline_id', timeline_id, 'str')
        if record_id is not None:
            route_values['recordId'] = self._serialize.url('record_id', record_id, 'str')
        if type is not None:
            route_values['type'] = self._serialize.url('type', type, 'str')
        if name is not None:
            route_values['name'] = self._serialize.url('name', name, 'str')
        query_parameters = {}
        if artifact_hash is not None:
            query_parameters['artifactHash'] = self._serialize.query('artifact_hash', artifact_hash, 'str')
        if length is not None:
            query_parameters['length'] = self._serialize.query('length', length, 'long')
        response = self._send(http_method='PUT',
                              location_id='7898f959-9cdf-4096-b29e-7f293031629e',
                              version='7.0',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TaskAttachment', response)

    def get_attachment(self, scope_identifier, hub_name, plan_id, timeline_id, record_id, type, name):
        """GetAttachment.
        :param str scope_identifier: The project GUID to scope the request
        :param str hub_name: The name of the server hub: "build" for the Build server or "rm" for the Release Management server
        :param str plan_id:
        :param str timeline_id:
        :param str record_id:
        :param str type:
        :param str name:
        :rtype: :class:`<TaskAttachment> <azure.devops.v7_0.task.models.TaskAttachment>`
        """
        route_values = {}
        if scope_identifier is not None:
            route_values['scopeIdentifier'] = self._serialize.url('scope_identifier', scope_identifier, 'str')
        if hub_name is not None:
            route_values['hubName'] = self._serialize.url('hub_name', hub_name, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'str')
        if timeline_id is not None:
            route_values['timelineId'] = self._serialize.url('timeline_id', timeline_id, 'str')
        if record_id is not None:
            route_values['recordId'] = self._serialize.url('record_id', record_id, 'str')
        if type is not None:
            route_values['type'] = self._serialize.url('type', type, 'str')
        if name is not None:
            route_values['name'] = self._serialize.url('name', name, 'str')
        response = self._send(http_method='GET',
                              location_id='7898f959-9cdf-4096-b29e-7f293031629e',
                              version='7.0',
                              route_values=route_values)
        return self._deserialize('TaskAttachment', response)

    def get_attachment_content(self, scope_identifier, hub_name, plan_id, timeline_id, record_id, type, name, **kwargs):
        """GetAttachmentContent.
        :param str scope_identifier: The project GUID to scope the request
        :param str hub_name: The name of the server hub: "build" for the Build server or "rm" for the Release Management server
        :param str plan_id:
        :param str timeline_id:
        :param str record_id:
        :param str type:
        :param str name:
        :rtype: object
        """
        route_values = {}
        if scope_identifier is not None:
            route_values['scopeIdentifier'] = self._serialize.url('scope_identifier', scope_identifier, 'str')
        if hub_name is not None:
            route_values['hubName'] = self._serialize.url('hub_name', hub_name, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'str')
        if timeline_id is not None:
            route_values['timelineId'] = self._serialize.url('timeline_id', timeline_id, 'str')
        if record_id is not None:
            route_values['recordId'] = self._serialize.url('record_id', record_id, 'str')
        if type is not None:
            route_values['type'] = self._serialize.url('type', type, 'str')
        if name is not None:
            route_values['name'] = self._serialize.url('name', name, 'str')
        response = self._send(http_method='GET',
                              location_id='7898f959-9cdf-4096-b29e-7f293031629e',
                              version='7.0',
                              route_values=route_values,
                              accept_media_type='application/octet-stream')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_attachments(self, scope_identifier, hub_name, plan_id, timeline_id, record_id, type):
        """GetAttachments.
        :param str scope_identifier: The project GUID to scope the request
        :param str hub_name: The name of the server hub: "build" for the Build server or "rm" for the Release Management server
        :param str plan_id:
        :param str timeline_id:
        :param str record_id:
        :param str type:
        :rtype: [TaskAttachment]
        """
        route_values = {}
        if scope_identifier is not None:
            route_values['scopeIdentifier'] = self._serialize.url('scope_identifier', scope_identifier, 'str')
        if hub_name is not None:
            route_values['hubName'] = self._serialize.url('hub_name', hub_name, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'str')
        if timeline_id is not None:
            route_values['timelineId'] = self._serialize.url('timeline_id', timeline_id, 'str')
        if record_id is not None:
            route_values['recordId'] = self._serialize.url('record_id', record_id, 'str')
        if type is not None:
            route_values['type'] = self._serialize.url('type', type, 'str')
        response = self._send(http_method='GET',
                              location_id='7898f959-9cdf-4096-b29e-7f293031629e',
                              version='7.0',
                              route_values=route_values)
        return self._deserialize('[TaskAttachment]', self._unwrap_collection(response))

    def append_log_content(self, upload_stream, scope_identifier, hub_name, plan_id, log_id, **kwargs):
        """AppendLogContent.
        :param object upload_stream: Stream to upload
        :param str scope_identifier: The project GUID to scope the request
        :param str hub_name: The name of the server hub: "build" for the Build server or "rm" for the Release Management server
        :param str plan_id:
        :param int log_id:
        :rtype: :class:`<TaskLog> <azure.devops.v7_0.task.models.TaskLog>`
        """
        route_values = {}
        if scope_identifier is not None:
            route_values['scopeIdentifier'] = self._serialize.url('scope_identifier', scope_identifier, 'str')
        if hub_name is not None:
            route_values['hubName'] = self._serialize.url('hub_name', hub_name, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'str')
        if log_id is not None:
            route_values['logId'] = self._serialize.url('log_id', log_id, 'int')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        content = self._client.stream_upload(upload_stream, callback=callback)
        response = self._send(http_method='POST',
                              location_id='46f5667d-263a-4684-91b1-dff7fdcf64e2',
                              version='7.0',
                              route_values=route_values,
                              content=content,
                              media_type='application/octet-stream')
        return self._deserialize('TaskLog', response)

    def associate_log(self, scope_identifier, hub_name, plan_id, log_id, serialized_blob_id, line_count):
        """AssociateLog.
        :param str scope_identifier: The project GUID to scope the request
        :param str hub_name: The name of the server hub: "build" for the Build server or "rm" for the Release Management server
        :param str plan_id:
        :param int log_id:
        :param str serialized_blob_id:
        :param int line_count:
        :rtype: :class:`<TaskLog> <azure.devops.v7_0.task.models.TaskLog>`
        """
        route_values = {}
        if scope_identifier is not None:
            route_values['scopeIdentifier'] = self._serialize.url('scope_identifier', scope_identifier, 'str')
        if hub_name is not None:
            route_values['hubName'] = self._serialize.url('hub_name', hub_name, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'str')
        if log_id is not None:
            route_values['logId'] = self._serialize.url('log_id', log_id, 'int')
        query_parameters = {}
        if serialized_blob_id is not None:
            query_parameters['serializedBlobId'] = self._serialize.query('serialized_blob_id', serialized_blob_id, 'str')
        if line_count is not None:
            query_parameters['lineCount'] = self._serialize.query('line_count', line_count, 'int')
        response = self._send(http_method='POST',
                              location_id='46f5667d-263a-4684-91b1-dff7fdcf64e2',
                              version='7.0',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TaskLog', response)

    def create_log(self, log, scope_identifier, hub_name, plan_id):
        """CreateLog.
        :param :class:`<TaskLog> <azure.devops.v7_0.task.models.TaskLog>` log:
        :param str scope_identifier: The project GUID to scope the request
        :param str hub_name: The name of the server hub: "build" for the Build server or "rm" for the Release Management server
        :param str plan_id:
        :rtype: :class:`<TaskLog> <azure.devops.v7_0.task.models.TaskLog>`
        """
        route_values = {}
        if scope_identifier is not None:
            route_values['scopeIdentifier'] = self._serialize.url('scope_identifier', scope_identifier, 'str')
        if hub_name is not None:
            route_values['hubName'] = self._serialize.url('hub_name', hub_name, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'str')
        content = self._serialize.body(log, 'TaskLog')
        response = self._send(http_method='POST',
                              location_id='46f5667d-263a-4684-91b1-dff7fdcf64e2',
                              version='7.0',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TaskLog', response)

    def get_log(self, scope_identifier, hub_name, plan_id, log_id, start_line=None, end_line=None):
        """GetLog.
        :param str scope_identifier: The project GUID to scope the request
        :param str hub_name: The name of the server hub: "build" for the Build server or "rm" for the Release Management server
        :param str plan_id:
        :param int log_id:
        :param long start_line:
        :param long end_line:
        :rtype: [str]
        """
        route_values = {}
        if scope_identifier is not None:
            route_values['scopeIdentifier'] = self._serialize.url('scope_identifier', scope_identifier, 'str')
        if hub_name is not None:
            route_values['hubName'] = self._serialize.url('hub_name', hub_name, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'str')
        if log_id is not None:
            route_values['logId'] = self._serialize.url('log_id', log_id, 'int')
        query_parameters = {}
        if start_line is not None:
            query_parameters['startLine'] = self._serialize.query('start_line', start_line, 'long')
        if end_line is not None:
            query_parameters['endLine'] = self._serialize.query('end_line', end_line, 'long')
        response = self._send(http_method='GET',
                              location_id='46f5667d-263a-4684-91b1-dff7fdcf64e2',
                              version='7.0',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[str]', self._unwrap_collection(response))

    def get_logs(self, scope_identifier, hub_name, plan_id):
        """GetLogs.
        :param str scope_identifier: The project GUID to scope the request
        :param str hub_name: The name of the server hub: "build" for the Build server or "rm" for the Release Management server
        :param str plan_id:
        :rtype: [TaskLog]
        """
        route_values = {}
        if scope_identifier is not None:
            route_values['scopeIdentifier'] = self._serialize.url('scope_identifier', scope_identifier, 'str')
        if hub_name is not None:
            route_values['hubName'] = self._serialize.url('hub_name', hub_name, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'str')
        response = self._send(http_method='GET',
                              location_id='46f5667d-263a-4684-91b1-dff7fdcf64e2',
                              version='7.0',
                              route_values=route_values)
        return self._deserialize('[TaskLog]', self._unwrap_collection(response))

    def get_records(self, scope_identifier, hub_name, plan_id, timeline_id, change_id=None):
        """GetRecords.
        :param str scope_identifier: The project GUID to scope the request
        :param str hub_name: The name of the server hub: "build" for the Build server or "rm" for the Release Management server
        :param str plan_id:
        :param str timeline_id:
        :param int change_id:
        :rtype: [TimelineRecord]
        """
        route_values = {}
        if scope_identifier is not None:
            route_values['scopeIdentifier'] = self._serialize.url('scope_identifier', scope_identifier, 'str')
        if hub_name is not None:
            route_values['hubName'] = self._serialize.url('hub_name', hub_name, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'str')
        if timeline_id is not None:
            route_values['timelineId'] = self._serialize.url('timeline_id', timeline_id, 'str')
        query_parameters = {}
        if change_id is not None:
            query_parameters['changeId'] = self._serialize.query('change_id', change_id, 'int')
        response = self._send(http_method='GET',
                              location_id='8893bc5b-35b2-4be7-83cb-99e683551db4',
                              version='7.0',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TimelineRecord]', self._unwrap_collection(response))

    def update_records(self, records, scope_identifier, hub_name, plan_id, timeline_id):
        """UpdateRecords.
        :param :class:`<VssJsonCollectionWrapper> <azure.devops.v7_0.task.models.VssJsonCollectionWrapper>` records:
        :param str scope_identifier: The project GUID to scope the request
        :param str hub_name: The name of the server hub: "build" for the Build server or "rm" for the Release Management server
        :param str plan_id:
        :param str timeline_id:
        :rtype: [TimelineRecord]
        """
        route_values = {}
        if scope_identifier is not None:
            route_values['scopeIdentifier'] = self._serialize.url('scope_identifier', scope_identifier, 'str')
        if hub_name is not None:
            route_values['hubName'] = self._serialize.url('hub_name', hub_name, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'str')
        if timeline_id is not None:
            route_values['timelineId'] = self._serialize.url('timeline_id', timeline_id, 'str')
        content = self._serialize.body(records, 'VssJsonCollectionWrapper')
        response = self._send(http_method='PATCH',
                              location_id='8893bc5b-35b2-4be7-83cb-99e683551db4',
                              version='7.0',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[TimelineRecord]', self._unwrap_collection(response))

    def create_timeline(self, timeline, scope_identifier, hub_name, plan_id):
        """CreateTimeline.
        :param :class:`<Timeline> <azure.devops.v7_0.task.models.Timeline>` timeline:
        :param str scope_identifier: The project GUID to scope the request
        :param str hub_name: The name of the server hub: "build" for the Build server or "rm" for the Release Management server
        :param str plan_id:
        :rtype: :class:`<Timeline> <azure.devops.v7_0.task.models.Timeline>`
        """
        route_values = {}
        if scope_identifier is not None:
            route_values['scopeIdentifier'] = self._serialize.url('scope_identifier', scope_identifier, 'str')
        if hub_name is not None:
            route_values['hubName'] = self._serialize.url('hub_name', hub_name, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'str')
        content = self._serialize.body(timeline, 'Timeline')
        response = self._send(http_method='POST',
                              location_id='83597576-cc2c-453c-bea6-2882ae6a1653',
                              version='7.0',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Timeline', response)

    def delete_timeline(self, scope_identifier, hub_name, plan_id, timeline_id):
        """DeleteTimeline.
        :param str scope_identifier: The project GUID to scope the request
        :param str hub_name: The name of the server hub: "build" for the Build server or "rm" for the Release Management server
        :param str plan_id:
        :param str timeline_id:
        """
        route_values = {}
        if scope_identifier is not None:
            route_values['scopeIdentifier'] = self._serialize.url('scope_identifier', scope_identifier, 'str')
        if hub_name is not None:
            route_values['hubName'] = self._serialize.url('hub_name', hub_name, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'str')
        if timeline_id is not None:
            route_values['timelineId'] = self._serialize.url('timeline_id', timeline_id, 'str')
        self._send(http_method='DELETE',
                   location_id='83597576-cc2c-453c-bea6-2882ae6a1653',
                   version='7.0',
                   route_values=route_values)

    def get_timeline(self, scope_identifier, hub_name, plan_id, timeline_id, change_id=None, include_records=None):
        """GetTimeline.
        :param str scope_identifier: The project GUID to scope the request
        :param str hub_name: The name of the server hub: "build" for the Build server or "rm" for the Release Management server
        :param str plan_id:
        :param str timeline_id:
        :param int change_id:
        :param bool include_records:
        :rtype: :class:`<Timeline> <azure.devops.v7_0.task.models.Timeline>`
        """
        route_values = {}
        if scope_identifier is not None:
            route_values['scopeIdentifier'] = self._serialize.url('scope_identifier', scope_identifier, 'str')
        if hub_name is not None:
            route_values['hubName'] = self._serialize.url('hub_name', hub_name, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'str')
        if timeline_id is not None:
            route_values['timelineId'] = self._serialize.url('timeline_id', timeline_id, 'str')
        query_parameters = {}
        if change_id is not None:
            query_parameters['changeId'] = self._serialize.query('change_id', change_id, 'int')
        if include_records is not None:
            query_parameters['includeRecords'] = self._serialize.query('include_records', include_records, 'bool')
        response = self._send(http_method='GET',
                              location_id='83597576-cc2c-453c-bea6-2882ae6a1653',
                              version='7.0',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('Timeline', response)

    def get_timelines(self, scope_identifier, hub_name, plan_id):
        """GetTimelines.
        :param str scope_identifier: The project GUID to scope the request
        :param str hub_name: The name of the server hub: "build" for the Build server or "rm" for the Release Management server
        :param str plan_id:
        :rtype: [Timeline]
        """
        route_values = {}
        if scope_identifier is not None:
            route_values['scopeIdentifier'] = self._serialize.url('scope_identifier', scope_identifier, 'str')
        if hub_name is not None:
            route_values['hubName'] = self._serialize.url('hub_name', hub_name, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'str')
        response = self._send(http_method='GET',
                              location_id='83597576-cc2c-453c-bea6-2882ae6a1653',
                              version='7.0',
                              route_values=route_values)
        return self._deserialize('[Timeline]', self._unwrap_collection(response))

