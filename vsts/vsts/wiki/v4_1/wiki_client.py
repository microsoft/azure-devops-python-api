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


class WikiClient(VssClient):
    """Wiki
    :param str base_url: Service URL
    :param Authentication creds: Authenticated credentials.
    """

    def __init__(self, base_url=None, creds=None):
        super(WikiClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = 'bf7d82a0-8aa5-4613-94ef-6172a5ea01f3'

    def get_page_text(self, project, wiki_identifier, path=None, recursion_level=None, version_descriptor=None, include_content=None):
        """GetPageText.
        Gets metadata or content of the wiki page for the provided path. Content negotiation is done based on the `Accept` header sent in the request.
        :param str project: Project ID or project name
        :param str wiki_identifier: Wiki Id or name.
        :param str path: Wiki page path.
        :param str recursion_level: Recursion level for subpages retrieval. Defaults to `None` (Optional).
        :param :class:`<GitVersionDescriptor> <wiki.v4_1.models.GitVersionDescriptor>` version_descriptor: GitVersionDescriptor for the page. Defaults to the default branch (Optional).
        :param bool include_content: True to include the content of the page in the response for Json content type. Defaults to false (Optional)
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if wiki_identifier is not None:
            route_values['wikiIdentifier'] = self._serialize.url('wiki_identifier', wiki_identifier, 'str')
        query_parameters = {}
        if path is not None:
            query_parameters['path'] = self._serialize.query('path', path, 'str')
        if recursion_level is not None:
            query_parameters['recursionLevel'] = self._serialize.query('recursion_level', recursion_level, 'str')
        if version_descriptor is not None:
            if version_descriptor.version_type is not None:
                query_parameters['versionDescriptor.VersionType'] = version_descriptor.version_type
            if version_descriptor.version is not None:
                query_parameters['versionDescriptor.Version'] = version_descriptor.version
            if version_descriptor.version_options is not None:
                query_parameters['versionDescriptor.VersionOptions'] = version_descriptor.version_options
        if include_content is not None:
            query_parameters['includeContent'] = self._serialize.query('include_content', include_content, 'bool')
        response = self._send(http_method='GET',
                              location_id='25d3fbc7-fe3d-46cb-b5a5-0b6f79caf27b',
                              version='4.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('object', response)

    def get_page_zip(self, project, wiki_identifier, path=None, recursion_level=None, version_descriptor=None, include_content=None):
        """GetPageZip.
        Gets metadata or content of the wiki page for the provided path. Content negotiation is done based on the `Accept` header sent in the request.
        :param str project: Project ID or project name
        :param str wiki_identifier: Wiki Id or name.
        :param str path: Wiki page path.
        :param str recursion_level: Recursion level for subpages retrieval. Defaults to `None` (Optional).
        :param :class:`<GitVersionDescriptor> <wiki.v4_1.models.GitVersionDescriptor>` version_descriptor: GitVersionDescriptor for the page. Defaults to the default branch (Optional).
        :param bool include_content: True to include the content of the page in the response for Json content type. Defaults to false (Optional)
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if wiki_identifier is not None:
            route_values['wikiIdentifier'] = self._serialize.url('wiki_identifier', wiki_identifier, 'str')
        query_parameters = {}
        if path is not None:
            query_parameters['path'] = self._serialize.query('path', path, 'str')
        if recursion_level is not None:
            query_parameters['recursionLevel'] = self._serialize.query('recursion_level', recursion_level, 'str')
        if version_descriptor is not None:
            if version_descriptor.version_type is not None:
                query_parameters['versionDescriptor.VersionType'] = version_descriptor.version_type
            if version_descriptor.version is not None:
                query_parameters['versionDescriptor.Version'] = version_descriptor.version
            if version_descriptor.version_options is not None:
                query_parameters['versionDescriptor.VersionOptions'] = version_descriptor.version_options
        if include_content is not None:
            query_parameters['includeContent'] = self._serialize.query('include_content', include_content, 'bool')
        response = self._send(http_method='GET',
                              location_id='25d3fbc7-fe3d-46cb-b5a5-0b6f79caf27b',
                              version='4.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('object', response)

    def create_wiki(self, wiki_create_params, project=None):
        """CreateWiki.
        Creates the wiki resource.
        :param :class:`<WikiCreateParametersV2> <wiki.v4_1.models.WikiCreateParametersV2>` wiki_create_params: Parameters for the wiki creation.
        :param str project: Project ID or project name
        :rtype: :class:`<WikiV2> <wiki.v4_1.models.WikiV2>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(wiki_create_params, 'WikiCreateParametersV2')
        response = self._send(http_method='POST',
                              location_id='288d122c-dbd4-451d-aa5f-7dbbba070728',
                              version='4.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('WikiV2', response)

    def delete_wiki(self, wiki_identifier, project=None):
        """DeleteWiki.
        Deletes the wiki corresponding to the wiki name or Id provided.
        :param str wiki_identifier: Wiki name or Id.
        :param str project: Project ID or project name
        :rtype: :class:`<WikiV2> <wiki.v4_1.models.WikiV2>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if wiki_identifier is not None:
            route_values['wikiIdentifier'] = self._serialize.url('wiki_identifier', wiki_identifier, 'str')
        response = self._send(http_method='DELETE',
                              location_id='288d122c-dbd4-451d-aa5f-7dbbba070728',
                              version='4.1',
                              route_values=route_values)
        return self._deserialize('WikiV2', response)

    def get_all_wikis(self, project=None):
        """GetAllWikis.
        Gets all wikis in a project or collection.
        :param str project: Project ID or project name
        :rtype: [WikiV2]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        response = self._send(http_method='GET',
                              location_id='288d122c-dbd4-451d-aa5f-7dbbba070728',
                              version='4.1',
                              route_values=route_values,
                              returns_collection=True)
        return self._deserialize('[WikiV2]', response)

    def get_wiki(self, wiki_identifier, project=None):
        """GetWiki.
        Gets the wiki corresponding to the wiki name or Id provided.
        :param str wiki_identifier: Wiki name or id.
        :param str project: Project ID or project name
        :rtype: :class:`<WikiV2> <wiki.v4_1.models.WikiV2>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if wiki_identifier is not None:
            route_values['wikiIdentifier'] = self._serialize.url('wiki_identifier', wiki_identifier, 'str')
        response = self._send(http_method='GET',
                              location_id='288d122c-dbd4-451d-aa5f-7dbbba070728',
                              version='4.1',
                              route_values=route_values)
        return self._deserialize('WikiV2', response)

    def update_wiki(self, update_parameters, wiki_identifier, project=None):
        """UpdateWiki.
        Updates the wiki corresponding to the wiki Id or name provided using the update parameters.
        :param :class:`<WikiUpdateParameters> <wiki.v4_1.models.WikiUpdateParameters>` update_parameters: Update parameters.
        :param str wiki_identifier: Wiki name or Id.
        :param str project: Project ID or project name
        :rtype: :class:`<WikiV2> <wiki.v4_1.models.WikiV2>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if wiki_identifier is not None:
            route_values['wikiIdentifier'] = self._serialize.url('wiki_identifier', wiki_identifier, 'str')
        content = self._serialize.body(update_parameters, 'WikiUpdateParameters')
        response = self._send(http_method='PATCH',
                              location_id='288d122c-dbd4-451d-aa5f-7dbbba070728',
                              version='4.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('WikiV2', response)

