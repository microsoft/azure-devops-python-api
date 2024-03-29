﻿# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from . import models


class DashboardClient(Client):
    """Dashboard
    :param str base_url: Service URL
    :param Authentication creds: Authenticated credentials.
    """

    def __init__(self, base_url=None, creds=None):
        super(DashboardClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = '31c84e0a-3ece-48fd-a29d-100849af99ba'

    def create_dashboard(self, dashboard, team_context):
        """CreateDashboard.
        [Preview API] Create the supplied dashboard.
        :param :class:`<Dashboard> <azure.devops.v7_0.dashboard.models.Dashboard>` dashboard: The initial state of the dashboard
        :param :class:`<TeamContext> <azure.devops.v7_0.dashboard.models.TeamContext>` team_context: The team context for the operation
        :rtype: :class:`<Dashboard> <azure.devops.v7_0.dashboard.models.Dashboard>`
        """
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        content = self._serialize.body(dashboard, 'Dashboard')
        response = self._send(http_method='POST',
                              location_id='454b3e51-2e6e-48d4-ad81-978154089351',
                              version='7.0-preview.3',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Dashboard', response)

    def delete_dashboard(self, team_context, dashboard_id):
        """DeleteDashboard.
        [Preview API] Delete a dashboard given its ID. This also deletes the widgets associated with this dashboard.
        :param :class:`<TeamContext> <azure.devops.v7_0.dashboard.models.TeamContext>` team_context: The team context for the operation
        :param str dashboard_id: ID of the dashboard to delete.
        """
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        if dashboard_id is not None:
            route_values['dashboardId'] = self._serialize.url('dashboard_id', dashboard_id, 'str')
        self._send(http_method='DELETE',
                   location_id='454b3e51-2e6e-48d4-ad81-978154089351',
                   version='7.0-preview.3',
                   route_values=route_values)

    def get_dashboard(self, team_context, dashboard_id):
        """GetDashboard.
        [Preview API] Get a dashboard by its ID.
        :param :class:`<TeamContext> <azure.devops.v7_0.dashboard.models.TeamContext>` team_context: The team context for the operation
        :param str dashboard_id:
        :rtype: :class:`<Dashboard> <azure.devops.v7_0.dashboard.models.Dashboard>`
        """
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        if dashboard_id is not None:
            route_values['dashboardId'] = self._serialize.url('dashboard_id', dashboard_id, 'str')
        response = self._send(http_method='GET',
                              location_id='454b3e51-2e6e-48d4-ad81-978154089351',
                              version='7.0-preview.3',
                              route_values=route_values)
        return self._deserialize('Dashboard', response)

    def get_dashboards_by_project(self, team_context):
        """GetDashboardsByProject.
        [Preview API] Get a list of dashboards under a project.
        :param :class:`<TeamContext> <azure.devops.v7_0.dashboard.models.TeamContext>` team_context: The team context for the operation
        :rtype: [Dashboard]
        """
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        response = self._send(http_method='GET',
                              location_id='454b3e51-2e6e-48d4-ad81-978154089351',
                              version='7.0-preview.3',
                              route_values=route_values)
        return self._deserialize('[Dashboard]', self._unwrap_collection(response))

    def replace_dashboard(self, dashboard, team_context, dashboard_id):
        """ReplaceDashboard.
        [Preview API] Replace configuration for the specified dashboard. Replaces Widget list on Dashboard, only if property is supplied.
        :param :class:`<Dashboard> <azure.devops.v7_0.dashboard.models.Dashboard>` dashboard: The Configuration of the dashboard to replace.
        :param :class:`<TeamContext> <azure.devops.v7_0.dashboard.models.TeamContext>` team_context: The team context for the operation
        :param str dashboard_id: ID of the dashboard to replace.
        :rtype: :class:`<Dashboard> <azure.devops.v7_0.dashboard.models.Dashboard>`
        """
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        if dashboard_id is not None:
            route_values['dashboardId'] = self._serialize.url('dashboard_id', dashboard_id, 'str')
        content = self._serialize.body(dashboard, 'Dashboard')
        response = self._send(http_method='PUT',
                              location_id='454b3e51-2e6e-48d4-ad81-978154089351',
                              version='7.0-preview.3',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Dashboard', response)

    def replace_dashboards(self, group, team_context):
        """ReplaceDashboards.
        [Preview API] Update the name and position of dashboards in the supplied group, and remove omitted dashboards. Does not modify dashboard content.
        :param :class:`<DashboardGroup> <azure.devops.v7_0.dashboard.models.DashboardGroup>` group:
        :param :class:`<TeamContext> <azure.devops.v7_0.dashboard.models.TeamContext>` team_context: The team context for the operation
        :rtype: :class:`<DashboardGroup> <azure.devops.v7_0.dashboard.models.DashboardGroup>`
        """
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        content = self._serialize.body(group, 'DashboardGroup')
        response = self._send(http_method='PUT',
                              location_id='454b3e51-2e6e-48d4-ad81-978154089351',
                              version='7.0-preview.3',
                              route_values=route_values,
                              content=content)
        return self._deserialize('DashboardGroup', response)

    def create_widget(self, widget, team_context, dashboard_id):
        """CreateWidget.
        [Preview API] Create a widget on the specified dashboard.
        :param :class:`<Widget> <azure.devops.v7_0.dashboard.models.Widget>` widget: State of the widget to add
        :param :class:`<TeamContext> <azure.devops.v7_0.dashboard.models.TeamContext>` team_context: The team context for the operation
        :param str dashboard_id: ID of dashboard the widget will be added to.
        :rtype: :class:`<Widget> <azure.devops.v7_0.dashboard.models.Widget>`
        """
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        if dashboard_id is not None:
            route_values['dashboardId'] = self._serialize.url('dashboard_id', dashboard_id, 'str')
        content = self._serialize.body(widget, 'Widget')
        response = self._send(http_method='POST',
                              location_id='bdcff53a-8355-4172-a00a-40497ea23afc',
                              version='7.0-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Widget', response)

    def delete_widget(self, team_context, dashboard_id, widget_id):
        """DeleteWidget.
        [Preview API] Delete the specified widget.
        :param :class:`<TeamContext> <azure.devops.v7_0.dashboard.models.TeamContext>` team_context: The team context for the operation
        :param str dashboard_id: ID of the dashboard containing the widget.
        :param str widget_id: ID of the widget to update.
        :rtype: :class:`<Dashboard> <azure.devops.v7_0.dashboard.models.Dashboard>`
        """
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        if dashboard_id is not None:
            route_values['dashboardId'] = self._serialize.url('dashboard_id', dashboard_id, 'str')
        if widget_id is not None:
            route_values['widgetId'] = self._serialize.url('widget_id', widget_id, 'str')
        response = self._send(http_method='DELETE',
                              location_id='bdcff53a-8355-4172-a00a-40497ea23afc',
                              version='7.0-preview.2',
                              route_values=route_values)
        return self._deserialize('Dashboard', response)

    def get_widget(self, team_context, dashboard_id, widget_id):
        """GetWidget.
        [Preview API] Get the current state of the specified widget.
        :param :class:`<TeamContext> <azure.devops.v7_0.dashboard.models.TeamContext>` team_context: The team context for the operation
        :param str dashboard_id: ID of the dashboard containing the widget.
        :param str widget_id: ID of the widget to read.
        :rtype: :class:`<Widget> <azure.devops.v7_0.dashboard.models.Widget>`
        """
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        if dashboard_id is not None:
            route_values['dashboardId'] = self._serialize.url('dashboard_id', dashboard_id, 'str')
        if widget_id is not None:
            route_values['widgetId'] = self._serialize.url('widget_id', widget_id, 'str')
        response = self._send(http_method='GET',
                              location_id='bdcff53a-8355-4172-a00a-40497ea23afc',
                              version='7.0-preview.2',
                              route_values=route_values)
        return self._deserialize('Widget', response)

    def get_widgets(self, team_context, dashboard_id, eTag=None):
        """GetWidgets.
        [Preview API] Get widgets contained on the specified dashboard.
        :param :class:`<TeamContext> <azure.devops.v7_0.dashboard.models.TeamContext>` team_context: The team context for the operation
        :param str dashboard_id: ID of the dashboard to read.
        :param String eTag: Dashboard Widgets Version
        :rtype: :class:`<WidgetsVersionedList> <azure.devops.v7_0.dashboard.models.WidgetsVersionedList>`
        """
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        if dashboard_id is not None:
            route_values['dashboardId'] = self._serialize.url('dashboard_id', dashboard_id, 'str')
        additional_headers = {}
        if eTag is not None:
            additional_headers['ETag'] = eTag
        response = self._send(http_method='GET',
                              location_id='bdcff53a-8355-4172-a00a-40497ea23afc',
                              version='7.0-preview.2',
                              route_values=route_values,
                              additional_headers=additional_headers)
        response_object = models.WidgetsVersionedList()
        response_object.widgets = self._deserialize('[Widget]', self._unwrap_collection(response))
        response_object.eTag = response.headers.get('ETag')
        return response_object

    def replace_widget(self, widget, team_context, dashboard_id, widget_id):
        """ReplaceWidget.
        [Preview API] Override the  state of the specified widget.
        :param :class:`<Widget> <azure.devops.v7_0.dashboard.models.Widget>` widget: State to be written for the widget.
        :param :class:`<TeamContext> <azure.devops.v7_0.dashboard.models.TeamContext>` team_context: The team context for the operation
        :param str dashboard_id: ID of the dashboard containing the widget.
        :param str widget_id: ID of the widget to update.
        :rtype: :class:`<Widget> <azure.devops.v7_0.dashboard.models.Widget>`
        """
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        if dashboard_id is not None:
            route_values['dashboardId'] = self._serialize.url('dashboard_id', dashboard_id, 'str')
        if widget_id is not None:
            route_values['widgetId'] = self._serialize.url('widget_id', widget_id, 'str')
        content = self._serialize.body(widget, 'Widget')
        response = self._send(http_method='PUT',
                              location_id='bdcff53a-8355-4172-a00a-40497ea23afc',
                              version='7.0-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Widget', response)

    def replace_widgets(self, widgets, team_context, dashboard_id, eTag=None):
        """ReplaceWidgets.
        [Preview API] Replace the widgets on specified dashboard with the supplied widgets.
        :param [Widget] widgets: Revised state of widgets to store for the dashboard.
        :param :class:`<TeamContext> <azure.devops.v7_0.dashboard.models.TeamContext>` team_context: The team context for the operation
        :param str dashboard_id: ID of the Dashboard to modify.
        :param String eTag: Dashboard Widgets Version
        :rtype: :class:`<WidgetsVersionedList> <azure.devops.v7_0.dashboard.models.WidgetsVersionedList>`
        """
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        if dashboard_id is not None:
            route_values['dashboardId'] = self._serialize.url('dashboard_id', dashboard_id, 'str')
        additional_headers = {}
        if eTag is not None:
            additional_headers['ETag'] = eTag
        content = self._serialize.body(widgets, '[Widget]')
        response = self._send(http_method='PUT',
                              location_id='bdcff53a-8355-4172-a00a-40497ea23afc',
                              version='7.0-preview.2',
                              route_values=route_values,
                              additional_headers=additional_headers,
                              content=content)
        response_object = models.WidgetsVersionedList()
        response_object.widgets = self._deserialize('[Widget]', self._unwrap_collection(response))
        response_object.eTag = response.headers.get('ETag')
        return response_object

    def update_widget(self, widget, team_context, dashboard_id, widget_id):
        """UpdateWidget.
        [Preview API] Perform a partial update of the specified widget.
        :param :class:`<Widget> <azure.devops.v7_0.dashboard.models.Widget>` widget: Description of the widget changes to apply. All non-null fields will be replaced.
        :param :class:`<TeamContext> <azure.devops.v7_0.dashboard.models.TeamContext>` team_context: The team context for the operation
        :param str dashboard_id: ID of the dashboard containing the widget.
        :param str widget_id: ID of the widget to update.
        :rtype: :class:`<Widget> <azure.devops.v7_0.dashboard.models.Widget>`
        """
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        if dashboard_id is not None:
            route_values['dashboardId'] = self._serialize.url('dashboard_id', dashboard_id, 'str')
        if widget_id is not None:
            route_values['widgetId'] = self._serialize.url('widget_id', widget_id, 'str')
        content = self._serialize.body(widget, 'Widget')
        response = self._send(http_method='PATCH',
                              location_id='bdcff53a-8355-4172-a00a-40497ea23afc',
                              version='7.0-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Widget', response)

    def update_widgets(self, widgets, team_context, dashboard_id, eTag=None):
        """UpdateWidgets.
        [Preview API] Update the supplied widgets on the dashboard using supplied state. State of existing Widgets not passed in the widget list is preserved.
        :param [Widget] widgets: The set of widget states to update on the dashboard.
        :param :class:`<TeamContext> <azure.devops.v7_0.dashboard.models.TeamContext>` team_context: The team context for the operation
        :param str dashboard_id: ID of the Dashboard to modify.
        :param String eTag: Dashboard Widgets Version
        :rtype: :class:`<WidgetsVersionedList> <azure.devops.v7_0.dashboard.models.WidgetsVersionedList>`
        """
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        if dashboard_id is not None:
            route_values['dashboardId'] = self._serialize.url('dashboard_id', dashboard_id, 'str')
        additional_headers = {}
        if eTag is not None:
            additional_headers['ETag'] = eTag
        content = self._serialize.body(widgets, '[Widget]')
        response = self._send(http_method='PATCH',
                              location_id='bdcff53a-8355-4172-a00a-40497ea23afc',
                              version='7.0-preview.2',
                              route_values=route_values,
                              additional_headers=additional_headers,
                              content=content)
        response_object = models.WidgetsVersionedList()
        response_object.widgets = self._deserialize('[Widget]', self._unwrap_collection(response))
        response_object.eTag = response.headers.get('ETag')
        return response_object

    def get_widget_metadata(self, contribution_id, project=None):
        """GetWidgetMetadata.
        [Preview API] Get the widget metadata satisfying the specified contribution ID.
        :param str contribution_id: The ID of Contribution for the Widget
        :param str project: Project ID or project name
        :rtype: :class:`<WidgetMetadataResponse> <azure.devops.v7_0.dashboard.models.WidgetMetadataResponse>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if contribution_id is not None:
            route_values['contributionId'] = self._serialize.url('contribution_id', contribution_id, 'str')
        response = self._send(http_method='GET',
                              location_id='6b3628d3-e96f-4fc7-b176-50240b03b515',
                              version='7.0-preview.1',
                              route_values=route_values)
        return self._deserialize('WidgetMetadataResponse', response)

    def get_widget_types(self, scope, project=None):
        """GetWidgetTypes.
        [Preview API] Get all available widget metadata in alphabetical order, including widgets marked with isVisibleFromCatalog == false.
        :param str scope:
        :param str project: Project ID or project name
        :rtype: :class:`<WidgetTypesResponse> <azure.devops.v7_0.dashboard.models.WidgetTypesResponse>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if scope is not None:
            query_parameters['$scope'] = self._serialize.query('scope', scope, 'str')
        response = self._send(http_method='GET',
                              location_id='6b3628d3-e96f-4fc7-b176-50240b03b515',
                              version='7.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('WidgetTypesResponse', response)

