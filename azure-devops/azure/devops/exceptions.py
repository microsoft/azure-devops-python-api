# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from msrest.exceptions import (
    ClientException,
    ClientRequestError,
    AuthenticationError,
)


class AzureDevOpsClientError(ClientException):
    pass


class AzureDevOpsAuthenticationError(AuthenticationError):
    """AzureDevOpsAuthenticationError.
    Extends the AuthenticationError to include support for claims challenges.
    """

    def __init__(self, message, claims_challenge=None, inner_exception=None):
        """
        :param message: The error message.
        :param claims_challenge: Optional claims challenge string from the WWW-Authenticate header.
        :param inner_exception: Optional inner exception.
        """
        super(AzureDevOpsAuthenticationError, self).__init__(message, inner_exception)
        self.claims_challenge = claims_challenge
        
    def get_claims_challenge(self):
        """Get the claims challenge value if one exists.
        
        :return: The claims challenge string or None.
        """
        return self.claims_challenge


class AzureDevOpsClientRequestError(ClientRequestError):
    pass


class AzureDevOpsServiceError(AzureDevOpsClientRequestError):
    """AzureDevOpsServiceError.
    """

    def __init__(self, wrapped_exception):
        self.inner_exception = None
        if wrapped_exception.inner_exception is not None:
            self.inner_exception = AzureDevOpsServiceError(wrapped_exception.inner_exception)
        super(AzureDevOpsServiceError, self).__init__(message=wrapped_exception.message,
                                                      inner_exception=self.inner_exception)
        self.message = wrapped_exception.message
        self.exception_id = wrapped_exception.exception_id
        self.type_name = wrapped_exception.type_name
        self.type_key = wrapped_exception.type_key
        self.error_code = wrapped_exception.error_code
        self.event_id = wrapped_exception.event_id
        self.custom_properties = wrapped_exception.custom_properties
