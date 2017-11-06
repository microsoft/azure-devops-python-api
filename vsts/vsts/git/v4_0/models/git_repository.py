# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class GitRepository(Model):
    """GitRepository.

    :param _links:
    :type _links: :class:`ReferenceLinks <git.v4_0.models.ReferenceLinks>`
    :param created_by_forking: True if the repository was created as a fork
    :type created_by_forking: bool
    :param default_branch:
    :type default_branch: str
    :param fork_options: If set, options for creating this repo as a fork of another one. If unset, this repo is unrelated to any existing forks.
    :type fork_options: :class:`GitForkSyncRequestParameters <git.v4_0.models.GitForkSyncRequestParameters>`
    :param fork_parent: Only set when querying repositories. If set, the "parent" fork of this repository.
    :type fork_parent: :class:`GlobalGitRepositoryKey <git.v4_0.models.GlobalGitRepositoryKey>`
    :param id:
    :type id: str
    :param is_fork: True if the repository was created as a fork
    :type is_fork: bool
    :param name:
    :type name: str
    :param parent_repository:
    :type parent_repository: :class:`GitRepositoryRef <git.v4_0.models.GitRepositoryRef>`
    :param project:
    :type project: :class:`TeamProjectReference <git.v4_0.models.TeamProjectReference>`
    :param remote_url:
    :type remote_url: str
    :param url:
    :type url: str
    :param valid_remote_urls:
    :type valid_remote_urls: list of str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'created_by_forking': {'key': 'createdByForking', 'type': 'bool'},
        'default_branch': {'key': 'defaultBranch', 'type': 'str'},
        'fork_options': {'key': 'forkOptions', 'type': 'GitForkSyncRequestParameters'},
        'fork_parent': {'key': 'forkParent', 'type': 'GlobalGitRepositoryKey'},
        'id': {'key': 'id', 'type': 'str'},
        'is_fork': {'key': 'isFork', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'parent_repository': {'key': 'parentRepository', 'type': 'GitRepositoryRef'},
        'project': {'key': 'project', 'type': 'TeamProjectReference'},
        'remote_url': {'key': 'remoteUrl', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'valid_remote_urls': {'key': 'validRemoteUrls', 'type': '[str]'}
    }

    def __init__(self, _links=None, created_by_forking=None, default_branch=None, fork_options=None, fork_parent=None, id=None, is_fork=None, name=None, parent_repository=None, project=None, remote_url=None, url=None, valid_remote_urls=None):
        super(GitRepository, self).__init__()
        self._links = _links
        self.created_by_forking = created_by_forking
        self.default_branch = default_branch
        self.fork_options = fork_options
        self.fork_parent = fork_parent
        self.id = id
        self.is_fork = is_fork
        self.name = name
        self.parent_repository = parent_repository
        self.project = project
        self.remote_url = remote_url
        self.url = url
        self.valid_remote_urls = valid_remote_urls
