# coding=utf-8
# --------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class WebApiProjectCollectionRef(Model):
    """WebApiProjectCollectionRef.

    :param collection_url: Collection Tfs Url (Host Url)
    :type collection_url: str
    :param id: Collection Guid
    :type id: str
    :param name: Collection Name
    :type name: str
    :param url: Collection REST Url
    :type url: str
    """

    _attribute_map = {
        'collection_url': {'key': 'collectionUrl', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, collection_url=None, id=None, name=None, url=None):
        super(WebApiProjectCollectionRef, self).__init__()
        self.collection_url = collection_url
        self.id = id
        self.name = name
        self.url = url
