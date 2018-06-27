# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...vss_client import VssClient
from . import models


class UserClient(VssClient):
    """User
    :param str base_url: Service URL
    :param Authentication creds: Authenticated credentials.
    """

    def __init__(self, base_url=None, creds=None):
        super(UserClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = None

    def delete_attribute(self, descriptor, attribute_name):
        """DeleteAttribute.
        [Preview API] Deletes an attribute for the given user.
        :param str descriptor: The identity of the user for the operation.
        :param str attribute_name: The name of the attribute to delete.
        """
        route_values = {}
        if descriptor is not None:
            route_values['descriptor'] = self._serialize.url('descriptor', descriptor, 'str')
        if attribute_name is not None:
            route_values['attributeName'] = self._serialize.url('attribute_name', attribute_name, 'str')
        self._send(http_method='DELETE',
                   location_id='ac77b682-1ef8-4277-afde-30af9b546004',
                   version='4.1-preview.2',
                   route_values=route_values)

    def get_attribute(self, descriptor, attribute_name):
        """GetAttribute.
        [Preview API] Retrieves an attribute for a given user.
        :param str descriptor: The identity of the user for the operation.
        :param str attribute_name: The name of the attribute to retrieve.
        :rtype: :class:`<UserAttribute> <user.v4_1.models.UserAttribute>`
        """
        route_values = {}
        if descriptor is not None:
            route_values['descriptor'] = self._serialize.url('descriptor', descriptor, 'str')
        if attribute_name is not None:
            route_values['attributeName'] = self._serialize.url('attribute_name', attribute_name, 'str')
        response = self._send(http_method='GET',
                              location_id='ac77b682-1ef8-4277-afde-30af9b546004',
                              version='4.1-preview.2',
                              route_values=route_values)
        return self._deserialize('UserAttribute', response)

    def query_attributes(self, descriptor, continuation_token=None, query_pattern=None, modified_after=None):
        """QueryAttributes.
        [Preview API] Retrieves attributes for a given user. May return subset of attributes providing continuation token to retrieve the next batch
        :param str descriptor: The identity of the user for the operation.
        :param str continuation_token: The token telling server to return the next chunk of attributes from where it stopped last time. This must either be null or be a value returned from the previous call to this API
        :param str query_pattern: The wildcardable pattern for the attribute names to be retrieved, e.g. queryPattern=visualstudio.14.*
        :param str modified_after: The optional date/time of the minimum modification date for attributes to be retrieved, e.g. modifiedafter=2017-04-12T15:00:00.000Z
        :rtype: :class:`<UserAttributes> <user.v4_1.models.UserAttributes>`
        """
        route_values = {}
        if descriptor is not None:
            route_values['descriptor'] = self._serialize.url('descriptor', descriptor, 'str')
        query_parameters = {}
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        if query_pattern is not None:
            query_parameters['queryPattern'] = self._serialize.query('query_pattern', query_pattern, 'str')
        if modified_after is not None:
            query_parameters['modifiedAfter'] = self._serialize.query('modified_after', modified_after, 'str')
        response = self._send(http_method='GET',
                              location_id='ac77b682-1ef8-4277-afde-30af9b546004',
                              version='4.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('UserAttributes', response)

    def set_attributes(self, attribute_parameters_list, descriptor):
        """SetAttributes.
        [Preview API] Updates multiple attributes for a given user.
        :param [SetUserAttributeParameters] attribute_parameters_list: The list of attribute data to update.  Existing values will be overwritten.
        :param str descriptor: The identity of the user for the operation.
        :rtype: [UserAttribute]
        """
        route_values = {}
        if descriptor is not None:
            route_values['descriptor'] = self._serialize.url('descriptor', descriptor, 'str')
        content = self._serialize.body(attribute_parameters_list, '[SetUserAttributeParameters]')
        response = self._send(http_method='PATCH',
                              location_id='ac77b682-1ef8-4277-afde-30af9b546004',
                              version='4.1-preview.2',
                              route_values=route_values,
                              content=content,
                              returns_collection=True)
        return self._deserialize('[UserAttribute]', response)

    def delete_avatar(self, descriptor):
        """DeleteAvatar.
        [Preview API] Deletes a user's avatar.
        :param str descriptor: The identity of the user for the operation.
        """
        route_values = {}
        if descriptor is not None:
            route_values['descriptor'] = self._serialize.url('descriptor', descriptor, 'str')
        self._send(http_method='DELETE',
                   location_id='1c34cdf0-dd20-4370-a316-56ba776d75ce',
                   version='4.1-preview.1',
                   route_values=route_values)

    def get_avatar(self, descriptor, size=None, format=None):
        """GetAvatar.
        [Preview API] Retrieves the user's avatar.
        :param str descriptor: The identity of the user for the operation.
        :param str size: The size to retrieve, e.g. small, medium (default), or large.
        :param str format: The format for the response. Can be null. Accepted values: "png", "json"
        :rtype: :class:`<Avatar> <user.v4_1.models.Avatar>`
        """
        route_values = {}
        if descriptor is not None:
            route_values['descriptor'] = self._serialize.url('descriptor', descriptor, 'str')
        query_parameters = {}
        if size is not None:
            query_parameters['size'] = self._serialize.query('size', size, 'str')
        if format is not None:
            query_parameters['format'] = self._serialize.query('format', format, 'str')
        response = self._send(http_method='GET',
                              location_id='1c34cdf0-dd20-4370-a316-56ba776d75ce',
                              version='4.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('Avatar', response)

    def set_avatar(self, avatar, descriptor):
        """SetAvatar.
        [Preview API] Creates or updates an avatar to be associated with a given user.
        :param :class:`<Avatar> <user.v4_1.models.Avatar>` avatar: The avatar to set. The Image property must contain the binary representation of the image, in either jpg or png format.
        :param str descriptor: The identity of the user for the operation.
        """
        route_values = {}
        if descriptor is not None:
            route_values['descriptor'] = self._serialize.url('descriptor', descriptor, 'str')
        content = self._serialize.body(avatar, 'Avatar')
        self._send(http_method='PUT',
                   location_id='1c34cdf0-dd20-4370-a316-56ba776d75ce',
                   version='4.1-preview.1',
                   route_values=route_values,
                   content=content)

    def create_avatar_preview(self, avatar, descriptor, size=None, display_name=None):
        """CreateAvatarPreview.
        [Preview API]
        :param :class:`<Avatar> <user.v4_1.models.Avatar>` avatar:
        :param str descriptor:
        :param str size:
        :param str display_name:
        :rtype: :class:`<Avatar> <user.v4_1.models.Avatar>`
        """
        route_values = {}
        if descriptor is not None:
            route_values['descriptor'] = self._serialize.url('descriptor', descriptor, 'str')
        query_parameters = {}
        if size is not None:
            query_parameters['size'] = self._serialize.query('size', size, 'str')
        if display_name is not None:
            query_parameters['displayName'] = self._serialize.query('display_name', display_name, 'str')
        content = self._serialize.body(avatar, 'Avatar')
        response = self._send(http_method='POST',
                              location_id='aad154d3-750f-47e6-9898-dc3a2e7a1708',
                              version='4.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('Avatar', response)

    def get_descriptor(self, descriptor):
        """GetDescriptor.
        [Preview API]
        :param str descriptor:
        :rtype: :class:`<str> <user.v4_1.models.str>`
        """
        route_values = {}
        if descriptor is not None:
            route_values['descriptor'] = self._serialize.url('descriptor', descriptor, 'str')
        response = self._send(http_method='GET',
                              location_id='e338ed36-f702-44d3-8d18-9cba811d013a',
                              version='4.1-preview.1',
                              route_values=route_values)
        return self._deserialize('str', response)

    def confirm_mail(self, confirmation_parameters, descriptor):
        """ConfirmMail.
        [Preview API] Confirms preferred email for a given user.
        :param :class:`<MailConfirmationParameters> <user.v4_1.models.MailConfirmationParameters>` confirmation_parameters:
        :param str descriptor: The descriptor identifying the user for the operation.
        """
        route_values = {}
        if descriptor is not None:
            route_values['descriptor'] = self._serialize.url('descriptor', descriptor, 'str')
        content = self._serialize.body(confirmation_parameters, 'MailConfirmationParameters')
        self._send(http_method='POST',
                   location_id='fc213dcd-3a4e-4951-a2e2-7e3fed15706d',
                   version='4.1-preview.1',
                   route_values=route_values,
                   content=content)

    def write_notifications(self, notifications):
        """WriteNotifications.
        [Preview API] Stores/forwards provided notifications Accepts batch of notifications and each of those may be targeting multiple users
        :param [SendUserNotificationParameters] notifications: Collection of notifications to be persisted.
        """
        content = self._serialize.body(notifications, '[SendUserNotificationParameters]')
        self._send(http_method='POST',
                   location_id='63e9e5c8-09a5-4de6-9aa1-01a96219073c',
                   version='4.1-preview.1',
                   content=content)

    def query_notifications(self, descriptor, top=None, continuation_token=None):
        """QueryNotifications.
        [Preview API] Queries notifications for a given user
        :param str descriptor: The identity of the user for the operation.
        :param int top: Maximum amount of items to retrieve.
        :param str continuation_token: Token representing the position to restart reading notifications from.
        :rtype: :class:`<UserNotifications> <user.v4_1.models.UserNotifications>`
        """
        route_values = {}
        if descriptor is not None:
            route_values['descriptor'] = self._serialize.url('descriptor', descriptor, 'str')
        query_parameters = {}
        if top is not None:
            query_parameters['top'] = self._serialize.query('top', top, 'int')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        response = self._send(http_method='GET',
                              location_id='58ff9476-0a49-4a70-81d6-1ef63d4f92e8',
                              version='4.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('UserNotifications', response)

    def get_storage_key(self, descriptor):
        """GetStorageKey.
        [Preview API]
        :param str descriptor:
        :rtype: str
        """
        route_values = {}
        if descriptor is not None:
            route_values['descriptor'] = self._serialize.url('descriptor', descriptor, 'str')
        response = self._send(http_method='GET',
                              location_id='c1d0bf9e-3220-44d9-b048-222ae15fc3e4',
                              version='4.1-preview.1',
                              route_values=route_values)
        return self._deserialize('str', response)

    def get_user_defaults(self):
        """GetUserDefaults.
        [Preview API] Retrieves the default data for the authenticated user.
        :rtype: :class:`<User> <user.v4_1.models.User>`
        """
        response = self._send(http_method='GET',
                              location_id='a9e65880-7489-4453-aa72-0f7896f0b434',
                              version='4.1-preview.1')
        return self._deserialize('User', response)

    def create_user(self, user_parameters, create_local=None):
        """CreateUser.
        [Preview API] Creates a new user.
        :param :class:`<CreateUserParameters> <user.v4_1.models.CreateUserParameters>` user_parameters: The parameters to be used for user creation.
        :param bool create_local:
        :rtype: :class:`<User> <user.v4_1.models.User>`
        """
        query_parameters = {}
        if create_local is not None:
            query_parameters['createLocal'] = self._serialize.query('create_local', create_local, 'bool')
        content = self._serialize.body(user_parameters, 'CreateUserParameters')
        response = self._send(http_method='POST',
                              location_id='61117502-a055-422c-9122-b56e6643ed02',
                              version='4.1-preview.2',
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('User', response)

    def get_user(self, descriptor, create_if_not_exists=None):
        """GetUser.
        [Preview API] Retrieves the data for a given user.
        :param str descriptor: The identity of the user for the operation.
        :param Boolean create_if_not_exists: Whether to auto-provision the authenticated user
        :rtype: :class:`<User> <user.v4_1.models.User>`
        """
        route_values = {}
        if descriptor is not None:
            route_values['descriptor'] = self._serialize.url('descriptor', descriptor, 'str')
        response = self._send(http_method='GET',
                              location_id='61117502-a055-422c-9122-b56e6643ed02',
                              version='4.1-preview.2',
                              route_values=route_values)
        return self._deserialize('User', response)

    def update_user(self, user_parameters, descriptor):
        """UpdateUser.
        [Preview API] Updates an existing user.
        :param :class:`<UpdateUserParameters> <user.v4_1.models.UpdateUserParameters>` user_parameters: The parameters to be used for user update.
        :param str descriptor: The identity of the user for the operation.
        :rtype: :class:`<User> <user.v4_1.models.User>`
        """
        route_values = {}
        if descriptor is not None:
            route_values['descriptor'] = self._serialize.url('descriptor', descriptor, 'str')
        content = self._serialize.body(user_parameters, 'UpdateUserParameters')
        response = self._send(http_method='PATCH',
                              location_id='61117502-a055-422c-9122-b56e6643ed02',
                              version='4.1-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('User', response)

