﻿# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from ...v7_0.security import models


class SecurityClient(Client):
    """Security
    :param str base_url: Service URL
    :param Authentication creds: Authenticated credentials.
    """

    def __init__(self, base_url=None, creds=None):
        super(SecurityClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = None

    def remove_access_control_entries(self, security_namespace_id, token=None, descriptors=None):
        """RemoveAccessControlEntries.
        Remove the specified ACEs from the ACL belonging to the specified token.
        :param str security_namespace_id: Security namespace identifier.
        :param str token: The token whose ACL should be modified.
        :param str descriptors: String containing a list of identity descriptors separated by ',' whose entries should be removed.
        :rtype: bool
        """
        route_values = {}
        if security_namespace_id is not None:
            route_values['securityNamespaceId'] = self._serialize.url('security_namespace_id', security_namespace_id, 'str')
        query_parameters = {}
        if token is not None:
            query_parameters['token'] = self._serialize.query('token', token, 'str')
        if descriptors is not None:
            query_parameters['descriptors'] = self._serialize.query('descriptors', descriptors, 'str')
        response = self._send(http_method='DELETE',
                              location_id='ac08c8ff-4323-4b08-af90-bcd018d380ce',
                              version='7.0',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('bool', response)

    def set_access_control_entries(self, container, security_namespace_id):
        """SetAccessControlEntries.
        Add or update ACEs in the ACL for the provided token. The request body contains the target token, a list of [ACEs](https://docs.microsoft.com/en-us/rest/api/azure/devops/security/access%20control%20entries/set%20access%20control%20entries?#accesscontrolentry) and a optional merge parameter. In the case of a collision (by identity descriptor) with an existing ACE in the ACL, the "merge" parameter determines the behavior. If set, the existing ACE has its allow and deny merged with the incoming ACE's allow and deny. If unset, the existing ACE is displaced.
        :param :class:`<object> <azure.devops.v7_0.security.models.object>` container:
        :param str security_namespace_id: Security namespace identifier.
        :rtype: [AccessControlEntry]
        """
        route_values = {}
        if security_namespace_id is not None:
            route_values['securityNamespaceId'] = self._serialize.url('security_namespace_id', security_namespace_id, 'str')
        content = self._serialize.body(container, 'object')
        response = self._send(http_method='POST',
                              location_id='ac08c8ff-4323-4b08-af90-bcd018d380ce',
                              version='7.0',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[AccessControlEntry]', self._unwrap_collection(response))

    def query_access_control_lists(self, security_namespace_id, token=None, descriptors=None, include_extended_info=None, recurse=None):
        """QueryAccessControlLists.
        Return a list of access control lists for the specified security namespace and token. All ACLs in the security namespace will be retrieved if no optional parameters are provided.
        :param str security_namespace_id: Security namespace identifier.
        :param str token: Security token
        :param str descriptors: An optional filter string containing a list of identity descriptors separated by ',' whose ACEs should be retrieved. If this is left null, entire ACLs will be returned.
        :param bool include_extended_info: If true, populate the extended information properties for the access control entries contained in the returned lists.
        :param bool recurse: If true and this is a hierarchical namespace, return child ACLs of the specified token.
        :rtype: [AccessControlList]
        """
        route_values = {}
        if security_namespace_id is not None:
            route_values['securityNamespaceId'] = self._serialize.url('security_namespace_id', security_namespace_id, 'str')
        query_parameters = {}
        if token is not None:
            query_parameters['token'] = self._serialize.query('token', token, 'str')
        if descriptors is not None:
            query_parameters['descriptors'] = self._serialize.query('descriptors', descriptors, 'str')
        if include_extended_info is not None:
            query_parameters['includeExtendedInfo'] = self._serialize.query('include_extended_info', include_extended_info, 'bool')
        if recurse is not None:
            query_parameters['recurse'] = self._serialize.query('recurse', recurse, 'bool')
        response = self._send(http_method='GET',
                              location_id='18a2ad18-7571-46ae-bec7-0c7da1495885',
                              version='7.0',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[AccessControlList]', self._unwrap_collection(response))

    def remove_access_control_lists(self, security_namespace_id, tokens=None, recurse=None):
        """RemoveAccessControlLists.
        Remove access control lists under the specfied security namespace.
        :param str security_namespace_id: Security namespace identifier.
        :param str tokens: One or more comma-separated security tokens
        :param bool recurse: If true and this is a hierarchical namespace, also remove child ACLs of the specified tokens.
        :rtype: bool
        """
        route_values = {}
        if security_namespace_id is not None:
            route_values['securityNamespaceId'] = self._serialize.url('security_namespace_id', security_namespace_id, 'str')
        query_parameters = {}
        if tokens is not None:
            query_parameters['tokens'] = self._serialize.query('tokens', tokens, 'str')
        if recurse is not None:
            query_parameters['recurse'] = self._serialize.query('recurse', recurse, 'bool')
        response = self._send(http_method='DELETE',
                              location_id='18a2ad18-7571-46ae-bec7-0c7da1495885',
                              version='7.0',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('bool', response)

    def set_access_control_lists(self, access_control_lists, security_namespace_id):
        """SetAccessControlLists.
        Create or update one or more access control lists. All data that currently exists for the ACLs supplied will be overwritten.
        :param :class:`<VssJsonCollectionWrapper> <azure.devops.v7_0.security.models.VssJsonCollectionWrapper>` access_control_lists: A list of ACLs to create or update.
        :param str security_namespace_id: Security namespace identifier.
        """
        route_values = {}
        if security_namespace_id is not None:
            route_values['securityNamespaceId'] = self._serialize.url('security_namespace_id', security_namespace_id, 'str')
        content = self._serialize.body(access_control_lists, 'VssJsonCollectionWrapper')
        self._send(http_method='POST',
                   location_id='18a2ad18-7571-46ae-bec7-0c7da1495885',
                   version='7.0',
                   route_values=route_values,
                   content=content)

    def has_permissions_batch(self, eval_batch):
        """HasPermissionsBatch.
        Evaluates multiple permissions for the calling user.  Note: This method does not aggregate the results, nor does it short-circuit if one of the permissions evaluates to false.
        :param :class:`<PermissionEvaluationBatch> <azure.devops.v7_0.security.models.PermissionEvaluationBatch>` eval_batch: The set of evaluation requests.
        :rtype: :class:`<PermissionEvaluationBatch> <azure.devops.v7_0.security.models.PermissionEvaluationBatch>`
        """
        content = self._serialize.body(eval_batch, 'PermissionEvaluationBatch')
        response = self._send(http_method='POST',
                              location_id='cf1faa59-1b63-4448-bf04-13d981a46f5d',
                              version='7.0',
                              content=content)
        return self._deserialize('PermissionEvaluationBatch', response)

    def has_permissions(self, security_namespace_id, permissions=None, tokens=None, always_allow_administrators=None, delimiter=None):
        """HasPermissions.
        Evaluates whether the caller has the specified permissions on the specified set of security tokens.
        :param str security_namespace_id: Security namespace identifier.
        :param int permissions: Permissions to evaluate.
        :param str tokens: One or more security tokens to evaluate.
        :param bool always_allow_administrators: If true and if the caller is an administrator, always return true.
        :param str delimiter: Optional security token separator. Defaults to ",".
        :rtype: [bool]
        """
        route_values = {}
        if security_namespace_id is not None:
            route_values['securityNamespaceId'] = self._serialize.url('security_namespace_id', security_namespace_id, 'str')
        if permissions is not None:
            route_values['permissions'] = self._serialize.url('permissions', permissions, 'int')
        query_parameters = {}
        if tokens is not None:
            query_parameters['tokens'] = self._serialize.query('tokens', tokens, 'str')
        if always_allow_administrators is not None:
            query_parameters['alwaysAllowAdministrators'] = self._serialize.query('always_allow_administrators', always_allow_administrators, 'bool')
        if delimiter is not None:
            query_parameters['delimiter'] = self._serialize.query('delimiter', delimiter, 'str')
        response = self._send(http_method='GET',
                              location_id='dd3b8bd6-c7fc-4cbd-929a-933d9c011c9d',
                              version='7.0',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[bool]', self._unwrap_collection(response))

    def remove_permission(self, security_namespace_id, descriptor, permissions=None, token=None):
        """RemovePermission.
        Removes the specified permissions on a security token for a user or group.
        :param str security_namespace_id: Security namespace identifier.
        :param str descriptor: Identity descriptor of the user to remove permissions for.
        :param int permissions: Permissions to remove.
        :param str token: Security token to remove permissions for.
        :rtype: :class:`<AccessControlEntry> <azure.devops.v7_0.security.models.AccessControlEntry>`
        """
        route_values = {}
        if security_namespace_id is not None:
            route_values['securityNamespaceId'] = self._serialize.url('security_namespace_id', security_namespace_id, 'str')
        if permissions is not None:
            route_values['permissions'] = self._serialize.url('permissions', permissions, 'int')
        query_parameters = {}
        if descriptor is not None:
            query_parameters['descriptor'] = self._serialize.query('descriptor', descriptor, 'str')
        if token is not None:
            query_parameters['token'] = self._serialize.query('token', token, 'str')
        response = self._send(http_method='DELETE',
                              location_id='dd3b8bd6-c7fc-4cbd-929a-933d9c011c9d',
                              version='7.0',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('AccessControlEntry', response)

    def query_security_namespaces(self, security_namespace_id=None, local_only=None):
        """QuerySecurityNamespaces.
        List all security namespaces or just the specified namespace.
        :param str security_namespace_id: Security namespace identifier.
        :param bool local_only: If true, retrieve only local security namespaces.
        :rtype: [SecurityNamespaceDescription]
        """
        route_values = {}
        if security_namespace_id is not None:
            route_values['securityNamespaceId'] = self._serialize.url('security_namespace_id', security_namespace_id, 'str')
        query_parameters = {}
        if local_only is not None:
            query_parameters['localOnly'] = self._serialize.query('local_only', local_only, 'bool')
        response = self._send(http_method='GET',
                              location_id='ce7b9f95-fde9-4be8-a86d-83b366f0b87a',
                              version='7.0',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[SecurityNamespaceDescription]', self._unwrap_collection(response))

