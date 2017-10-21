# coding=utf-8
# --------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .web_api_project_collection_ref import WebApiProjectCollectionRef


class WebApiProjectCollection(WebApiProjectCollectionRef):
    """WebApiProjectCollection.

    :param collection_url: Collection Tfs Url (Host Url)
    :type collection_url: str
    :param id: Collection Guid
    :type id: str
    :param name: Collection Name
    :type name: str
    :param url: Collection REST Url
    :type url: str
    :param description: Project collection description
    :type description: str
    :param state: Project collection state
    :type state: str
    """

    _attribute_map = {
        'collection_url': {'key': 'collectionUrl', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'}
    }

    def __init__(self, collection_url=None, id=None, name=None, url=None, description=None, state=None):
        super(WebApiProjectCollection, self).__init__(collection_url=collection_url, id=id, name=name, url=url)
        self.description = description
        self.state = state
