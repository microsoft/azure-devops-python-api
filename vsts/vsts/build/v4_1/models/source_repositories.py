# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class SourceRepositories(Model):
    """SourceRepositories.

    :param continuation_token: A token used to continue this paged request; 'null' if the request is complete
    :type continuation_token: str
    :param page_length: The number of repositories requested for each page
    :type page_length: int
    :param repositories: A list of repositories
    :type repositories: list of :class:`SourceRepository <build.v4_1.models.SourceRepository>`
    :param total_page_count: The total number of pages, or '-1' if unknown
    :type total_page_count: int
    """

    _attribute_map = {
        'continuation_token': {'key': 'continuationToken', 'type': 'str'},
        'page_length': {'key': 'pageLength', 'type': 'int'},
        'repositories': {'key': 'repositories', 'type': '[SourceRepository]'},
        'total_page_count': {'key': 'totalPageCount', 'type': 'int'}
    }

    def __init__(self, continuation_token=None, page_length=None, repositories=None, total_page_count=None):
        super(SourceRepositories, self).__init__()
        self.continuation_token = continuation_token
        self.page_length = page_length
        self.repositories = repositories
        self.total_page_count = total_page_count
