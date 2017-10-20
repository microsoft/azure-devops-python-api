# coding=utf-8
# --------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class GitForkRelationship(Model):
    """GitForkRelationship.

    :param _links:
    :type _links: :class:`ReferenceLinks <git.models.ReferenceLinks>`
    :param collection: Team Project Collection where this Fork resides
    :type collection: :class:`TeamProjectCollectionReference <git.models.TeamProjectCollectionReference>`
    :param project: Team Project where this Fork resides
    :type project: :class:`TeamProjectReference <git.models.TeamProjectReference>`
    :param relationship: Relationship of this fork to the current repository context
    :type relationship: object
    :param repository_id:
    :type repository_id: str
    :param repository_name:
    :type repository_name: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'collection': {'key': 'collection', 'type': 'TeamProjectCollectionReference'},
        'project': {'key': 'project', 'type': 'TeamProjectReference'},
        'relationship': {'key': 'relationship', 'type': 'object'},
        'repository_id': {'key': 'repositoryId', 'type': 'str'},
        'repository_name': {'key': 'repositoryName', 'type': 'str'}
    }

    def __init__(self, _links=None, collection=None, project=None, relationship=None, repository_id=None, repository_name=None):
        super(GitForkRelationship, self).__init__()
        self._links = _links
        self.collection = collection
        self.project = project
        self.relationship = relationship
        self.repository_id = repository_id
        self.repository_name = repository_name
