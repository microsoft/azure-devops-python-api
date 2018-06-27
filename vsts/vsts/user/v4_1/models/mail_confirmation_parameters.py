# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class MailConfirmationParameters(Model):
    """MailConfirmationParameters.

    :param challenge_code: The unique code that proves ownership of the email address.
    :type challenge_code: str
    :param mail_address: The email address to be confirmed.
    :type mail_address: str
    """

    _attribute_map = {
        'challenge_code': {'key': 'challengeCode', 'type': 'str'},
        'mail_address': {'key': 'mailAddress', 'type': 'str'}
    }

    def __init__(self, challenge_code=None, mail_address=None):
        super(MailConfirmationParameters, self).__init__()
        self.challenge_code = challenge_code
        self.mail_address = mail_address
