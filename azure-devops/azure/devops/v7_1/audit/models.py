﻿# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class AuditActionInfo(Model):
    """
    :param action_id: The action id for the event, i.e Git.CreateRepo, Project.RenameProject
    :type action_id: str
    :param area: Area of Azure DevOps the action occurred
    :type area: str
    :param category: Type of action executed
    :type category: object
    """

    _attribute_map = {
        'action_id': {'key': 'actionId', 'type': 'str'},
        'area': {'key': 'area', 'type': 'str'},
        'category': {'key': 'category', 'type': 'object'}
    }

    def __init__(self, action_id=None, area=None, category=None):
        super(AuditActionInfo, self).__init__()
        self.action_id = action_id
        self.area = area
        self.category = category


class AuditLogEntry(Model):
    """
    :param action_id: The action if for the event, i.e Git.CreateRepo, Project.RenameProject
    :type action_id: str
    :param activity_id: ActivityId
    :type activity_id: str
    :param actor_client_id: The Actor's Client Id (if actor is a service principal)
    :type actor_client_id: str
    :param actor_cUID: The Actor's CUID
    :type actor_cUID: str
    :param actor_uPN: The Actor's UPN
    :type actor_uPN: str
    :param actor_user_id: The Actor's User Id (if actor is a user)
    :type actor_user_id: str
    :param authentication_mechanism: Type of authentication used by the author
    :type authentication_mechanism: str
    :param correlation_id: This allows us to group things together, like one user action that caused a cascade of event entries (project creation).
    :type correlation_id: str
    :param data: External data such as CUIDs, item names, etc.
    :type data: dict
    :param id: EventId, should be unique
    :type id: str
    :param ip_address: IP Address where the event was originated
    :type ip_address: str
    :param project_id: When specified, the id of the project this event is associated to
    :type project_id: str
    :param scope_id: The organization Id (Organization is the only scope currently supported)
    :type scope_id: str
    :param scope_type: The type of the scope (Organization is only scope currently supported)
    :type scope_type: object
    :param timestamp: The time when the event occurred in UTC
    :type timestamp: datetime
    :param user_agent: The user agent from the request
    :type user_agent: str
    """

    _attribute_map = {
        'action_id': {'key': 'actionId', 'type': 'str'},
        'activity_id': {'key': 'activityId', 'type': 'str'},
        'actor_client_id': {'key': 'actorClientId', 'type': 'str'},
        'actor_cUID': {'key': 'actorCUID', 'type': 'str'},
        'actor_uPN': {'key': 'actorUPN', 'type': 'str'},
        'actor_user_id': {'key': 'actorUserId', 'type': 'str'},
        'authentication_mechanism': {'key': 'authenticationMechanism', 'type': 'str'},
        'correlation_id': {'key': 'correlationId', 'type': 'str'},
        'data': {'key': 'data', 'type': '{object}'},
        'id': {'key': 'id', 'type': 'str'},
        'ip_address': {'key': 'ipAddress', 'type': 'str'},
        'project_id': {'key': 'projectId', 'type': 'str'},
        'scope_id': {'key': 'scopeId', 'type': 'str'},
        'scope_type': {'key': 'scopeType', 'type': 'object'},
        'timestamp': {'key': 'timestamp', 'type': 'iso-8601'},
        'user_agent': {'key': 'userAgent', 'type': 'str'}
    }

    def __init__(self, action_id=None, activity_id=None, actor_client_id=None, actor_cUID=None, actor_uPN=None, actor_user_id=None, authentication_mechanism=None, correlation_id=None, data=None, id=None, ip_address=None, project_id=None, scope_id=None, scope_type=None, timestamp=None, user_agent=None):
        super(AuditLogEntry, self).__init__()
        self.action_id = action_id
        self.activity_id = activity_id
        self.actor_client_id = actor_client_id
        self.actor_cUID = actor_cUID
        self.actor_uPN = actor_uPN
        self.actor_user_id = actor_user_id
        self.authentication_mechanism = authentication_mechanism
        self.correlation_id = correlation_id
        self.data = data
        self.id = id
        self.ip_address = ip_address
        self.project_id = project_id
        self.scope_id = scope_id
        self.scope_type = scope_type
        self.timestamp = timestamp
        self.user_agent = user_agent


class AuditLogQueryResult(Model):
    """
    The object returned when the audit log is queried. It contains the log and the information needed to query more audit entries.

    :param continuation_token: The continuation token to pass to get the next set of results
    :type continuation_token: str
    :param decorated_audit_log_entries: The list of audit log entries
    :type decorated_audit_log_entries: list of :class:`DecoratedAuditLogEntry <azure.devops.v7_1.audit.models.DecoratedAuditLogEntry>`
    :param has_more: True when there are more matching results to be fetched, false otherwise.
    :type has_more: bool
    """

    _attribute_map = {
        'continuation_token': {'key': 'continuationToken', 'type': 'str'},
        'decorated_audit_log_entries': {'key': 'decoratedAuditLogEntries', 'type': '[DecoratedAuditLogEntry]'},
        'has_more': {'key': 'hasMore', 'type': 'bool'}
    }

    def __init__(self, continuation_token=None, decorated_audit_log_entries=None, has_more=None):
        super(AuditLogQueryResult, self).__init__()
        self.continuation_token = continuation_token
        self.decorated_audit_log_entries = decorated_audit_log_entries
        self.has_more = has_more


class AuditStream(Model):
    """
    This class represents an audit stream

    :param consumer_inputs: Inputs used to communicate with external service. Inputs could be url, a connection string, a token, etc.
    :type consumer_inputs: dict
    :param consumer_type: Type of the consumer, i.e. splunk, azureEventHub, etc.
    :type consumer_type: str
    :param created_time: The time when the stream was created
    :type created_time: datetime
    :param display_name: Used to identify individual streams
    :type display_name: str
    :param id: Unique stream identifier
    :type id: int
    :param status: Status of the stream, Enabled, Disabled
    :type status: object
    :param status_reason: Reason for the current stream status, i.e. Disabled by the system, Invalid credentials, etc.
    :type status_reason: str
    :param updated_time: The time when the stream was last updated
    :type updated_time: datetime
    """

    _attribute_map = {
        'consumer_inputs': {'key': 'consumerInputs', 'type': '{str}'},
        'consumer_type': {'key': 'consumerType', 'type': 'str'},
        'created_time': {'key': 'createdTime', 'type': 'iso-8601'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'status': {'key': 'status', 'type': 'object'},
        'status_reason': {'key': 'statusReason', 'type': 'str'},
        'updated_time': {'key': 'updatedTime', 'type': 'iso-8601'}
    }

    def __init__(self, consumer_inputs=None, consumer_type=None, created_time=None, display_name=None, id=None, status=None, status_reason=None, updated_time=None):
        super(AuditStream, self).__init__()
        self.consumer_inputs = consumer_inputs
        self.consumer_type = consumer_type
        self.created_time = created_time
        self.display_name = display_name
        self.id = id
        self.status = status
        self.status_reason = status_reason
        self.updated_time = updated_time


class DecoratedAuditLogEntry(Model):
    """
    :param action_id: The action id for the event, i.e Git.CreateRepo, Project.RenameProject
    :type action_id: str
    :param activity_id: ActivityId
    :type activity_id: str
    :param actor_client_id: The Actor's Client Id (if actor is a service principal)
    :type actor_client_id: str
    :param actor_cUID: The Actor's CUID
    :type actor_cUID: str
    :param actor_display_name: DisplayName of the user who initiated the action
    :type actor_display_name: str
    :param actor_image_url: URL of Actor's Profile image
    :type actor_image_url: str
    :param actor_uPN: The Actor's UPN
    :type actor_uPN: str
    :param actor_user_id: The Actor's User Id (if actor is a user)
    :type actor_user_id: str
    :param area: Area of Azure DevOps the action occurred
    :type area: str
    :param authentication_mechanism: Type of authentication used by the actor
    :type authentication_mechanism: str
    :param category: Type of action executed
    :type category: object
    :param category_display_name: DisplayName of the category
    :type category_display_name: str
    :param correlation_id: This allows related audit entries to be grouped together. Generally this occurs when a single action causes a cascade of audit entries. For example, project creation.
    :type correlation_id: str
    :param data: External data such as CUIDs, item names, etc.
    :type data: dict
    :param details: Decorated details
    :type details: str
    :param id: EventId - Needs to be unique per service
    :type id: str
    :param ip_address: IP Address where the event was originated
    :type ip_address: str
    :param project_id: When specified, the id of the project this event is associated to
    :type project_id: str
    :param project_name: When specified, the name of the project this event is associated to
    :type project_name: str
    :param scope_display_name: DisplayName of the scope
    :type scope_display_name: str
    :param scope_id: The organization Id (Organization is the only scope currently supported)
    :type scope_id: str
    :param scope_type: The type of the scope (Organization is only scope currently supported)
    :type scope_type: object
    :param timestamp: The time when the event occurred in UTC
    :type timestamp: datetime
    :param user_agent: The user agent from the request
    :type user_agent: str
    """

    _attribute_map = {
        'action_id': {'key': 'actionId', 'type': 'str'},
        'activity_id': {'key': 'activityId', 'type': 'str'},
        'actor_client_id': {'key': 'actorClientId', 'type': 'str'},
        'actor_cUID': {'key': 'actorCUID', 'type': 'str'},
        'actor_display_name': {'key': 'actorDisplayName', 'type': 'str'},
        'actor_image_url': {'key': 'actorImageUrl', 'type': 'str'},
        'actor_uPN': {'key': 'actorUPN', 'type': 'str'},
        'actor_user_id': {'key': 'actorUserId', 'type': 'str'},
        'area': {'key': 'area', 'type': 'str'},
        'authentication_mechanism': {'key': 'authenticationMechanism', 'type': 'str'},
        'category': {'key': 'category', 'type': 'object'},
        'category_display_name': {'key': 'categoryDisplayName', 'type': 'str'},
        'correlation_id': {'key': 'correlationId', 'type': 'str'},
        'data': {'key': 'data', 'type': '{object}'},
        'details': {'key': 'details', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'ip_address': {'key': 'ipAddress', 'type': 'str'},
        'project_id': {'key': 'projectId', 'type': 'str'},
        'project_name': {'key': 'projectName', 'type': 'str'},
        'scope_display_name': {'key': 'scopeDisplayName', 'type': 'str'},
        'scope_id': {'key': 'scopeId', 'type': 'str'},
        'scope_type': {'key': 'scopeType', 'type': 'object'},
        'timestamp': {'key': 'timestamp', 'type': 'iso-8601'},
        'user_agent': {'key': 'userAgent', 'type': 'str'}
    }

    def __init__(self, action_id=None, activity_id=None, actor_client_id=None, actor_cUID=None, actor_display_name=None, actor_image_url=None, actor_uPN=None, actor_user_id=None, area=None, authentication_mechanism=None, category=None, category_display_name=None, correlation_id=None, data=None, details=None, id=None, ip_address=None, project_id=None, project_name=None, scope_display_name=None, scope_id=None, scope_type=None, timestamp=None, user_agent=None):
        super(DecoratedAuditLogEntry, self).__init__()
        self.action_id = action_id
        self.activity_id = activity_id
        self.actor_client_id = actor_client_id
        self.actor_cUID = actor_cUID
        self.actor_display_name = actor_display_name
        self.actor_image_url = actor_image_url
        self.actor_uPN = actor_uPN
        self.actor_user_id = actor_user_id
        self.area = area
        self.authentication_mechanism = authentication_mechanism
        self.category = category
        self.category_display_name = category_display_name
        self.correlation_id = correlation_id
        self.data = data
        self.details = details
        self.id = id
        self.ip_address = ip_address
        self.project_id = project_id
        self.project_name = project_name
        self.scope_display_name = scope_display_name
        self.scope_id = scope_id
        self.scope_type = scope_type
        self.timestamp = timestamp
        self.user_agent = user_agent


__all__ = [
    'AuditActionInfo',
    'AuditLogEntry',
    'AuditLogQueryResult',
    'AuditStream',
    'DecoratedAuditLogEntry',
]
