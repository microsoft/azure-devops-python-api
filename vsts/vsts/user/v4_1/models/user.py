# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class User(Model):
    """User.

    :param bio: A short blurb of "about me"-style text.
    :type bio: str
    :param blog: A link to an external blog.
    :type blog: str
    :param company: The company at which the user is employed.
    :type company: str
    :param country: The user's country of residence or association.
    :type country: str
    :param date_created: The date the user was created in the system
    :type date_created: datetime
    :param descriptor: The user's unique identifier, and the primary means by which the user is referenced.
    :type descriptor: :class:`str <user.v4_1.models.str>`
    :param display_name: The user's name, as displayed throughout the product.
    :type display_name: str
    :param last_modified: The date/time at which the user data was last modified.
    :type last_modified: datetime
    :param links: A set of readonly links for obtaining more info about the user.
    :type links: :class:`ReferenceLinks <user.v4_1.models.ReferenceLinks>`
    :param mail: The user's preferred email address.
    :type mail: str
    :param revision: The attribute's revision, for change tracking.
    :type revision: int
    :param unconfirmed_mail: The user's preferred email address which has not yet been confirmed.
    :type unconfirmed_mail: str
    :param user_name: The unique name of the user.
    :type user_name: str
    """

    _attribute_map = {
        'bio': {'key': 'bio', 'type': 'str'},
        'blog': {'key': 'blog', 'type': 'str'},
        'company': {'key': 'company', 'type': 'str'},
        'country': {'key': 'country', 'type': 'str'},
        'date_created': {'key': 'dateCreated', 'type': 'iso-8601'},
        'descriptor': {'key': 'descriptor', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'last_modified': {'key': 'lastModified', 'type': 'iso-8601'},
        'links': {'key': 'links', 'type': 'ReferenceLinks'},
        'mail': {'key': 'mail', 'type': 'str'},
        'revision': {'key': 'revision', 'type': 'int'},
        'unconfirmed_mail': {'key': 'unconfirmedMail', 'type': 'str'},
        'user_name': {'key': 'userName', 'type': 'str'}
    }

    def __init__(self, bio=None, blog=None, company=None, country=None, date_created=None, descriptor=None, display_name=None, last_modified=None, links=None, mail=None, revision=None, unconfirmed_mail=None, user_name=None):
        super(User, self).__init__()
        self.bio = bio
        self.blog = blog
        self.company = company
        self.country = country
        self.date_created = date_created
        self.descriptor = descriptor
        self.display_name = display_name
        self.last_modified = last_modified
        self.links = links
        self.mail = mail
        self.revision = revision
        self.unconfirmed_mail = unconfirmed_mail
        self.user_name = user_name
