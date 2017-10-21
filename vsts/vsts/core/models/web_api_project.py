# coding=utf-8
# --------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .team_project_reference import TeamProjectReference


class WebApiProject(TeamProjectReference):
    """WebApiProject.

    :param abbreviation: Project abbreviation.
    :type abbreviation: str
    :param description: The project's description (if any).
    :type description: str
    :param id: Project identifier.
    :type id: str
    :param name: Project name.
    :type name: str
    :param revision: Project revision.
    :type revision: long
    :param state: Project state.
    :type state: object
    :param url: Url to the full version of the object.
    :type url: str
    :param visibility: Project visibility.
    :type visibility: object
    :param capabilities: Set of capabilities this project has
    :type capabilities: dict
    :param collection: Reference to collection which contains this project
    :type collection: :class:`WebApiProjectCollectionRef <core.models.WebApiProjectCollectionRef>`
    :param default_team: Default team for this project
    :type default_team: :class:`WebApiTeamRef <core.models.WebApiTeamRef>`
    """

    _attribute_map = {
        'abbreviation': {'key': 'abbreviation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'revision': {'key': 'revision', 'type': 'long'},
        'state': {'key': 'state', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'},
        'visibility': {'key': 'visibility', 'type': 'object'},
        'capabilities': {'key': 'capabilities', 'type': '{{str}}'},
        'collection': {'key': 'collection', 'type': 'WebApiProjectCollectionRef'},
        'default_team': {'key': 'defaultTeam', 'type': 'WebApiTeamRef'}
    }

    def __init__(self, abbreviation=None, description=None, id=None, name=None, revision=None, state=None, url=None, visibility=None, capabilities=None, collection=None, default_team=None):
        super(WebApiProject, self).__init__(abbreviation=abbreviation, description=description, id=id, name=name, revision=revision, state=state, url=url, visibility=visibility)
        self.capabilities = capabilities
        self.collection = collection
        self.default_team = default_team
