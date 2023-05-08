# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from typing import Optional, Dict, Any, List
from msrest.serialization import Model


class CopyDashboardOptions(Model):
    """
    Copy options of a Dashboard.

    :param copy_dashboard_scope: Dashboard Scope. Can be either Project or Project_Team
    :type copy_dashboard_scope: object
    :param copy_queries_flag: When this flag is set to true,option to select the folder to copy Queries of copy dashboard will appear.
    :type copy_queries_flag: bool
    :param description: Description of the dashboard
    :type description: str
    :param name: Name of the dashboard
    :type name: str
    :param project_id: ID of the project. Provided by service at creation time.
    :type project_id: str
    :param query_folder_path: Path to which the queries should be copied of copy dashboard
    :type query_folder_path: str
    :param refresh_interval: Refresh interval of dashboard
    :type refresh_interval: int
    :param team_id: ID of the team. Provided by service at creation time
    :type team_id: str
    """

    _attribute_map = {
        'copy_dashboard_scope': {'key': 'copyDashboardScope', 'type': 'object'},
        'copy_queries_flag': {'key': 'copyQueriesFlag', 'type': 'bool'},
        'description': {'key': 'description', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'project_id': {'key': 'projectId', 'type': 'str'},
        'query_folder_path': {'key': 'queryFolderPath', 'type': 'str'},
        'refresh_interval': {'key': 'refreshInterval', 'type': 'int'},
        'team_id': {'key': 'teamId', 'type': 'str'}
    }

    def __init__(self, copy_dashboard_scope=None, copy_queries_flag: Optional[bool] = None,
                 description: Optional[str] = None, name: Optional[str] = None, project_id: Optional[str] = None,
                 query_folder_path: Optional[str] = None, refresh_interval: Optional[int] = None,
                 team_id: Optional[str] = None) -> None:
        super(CopyDashboardOptions, self).__init__()
        self.copy_dashboard_scope = copy_dashboard_scope
        self.copy_queries_flag = copy_queries_flag
        self.description = description
        self.name = name
        self.project_id = project_id
        self.query_folder_path = query_folder_path
        self.refresh_interval = refresh_interval
        self.team_id = team_id


class ReferenceLinks(Model):
    """
    The class to represent a collection of REST reference links.

    :param links: The readonly view of the links.  Because Reference links are readonly, we only want to expose them as read only.
    :type links: dict
    """

    _attribute_map = {
        'links': {'key': 'links', 'type': '{object}'}
    }

    def __init__(self, links: Optional[Dict[Any, Any]] = None) -> None:
        super(ReferenceLinks, self).__init__()
        self.links = links


class WidgetSize(Model):
    """
    :param column_span: The Width of the widget, expressed in dashboard grid columns.
    :type column_span: int
    :param row_span: The height of the widget, expressed in dashboard grid rows.
    :type row_span: int
    """

    _attribute_map = {
        'column_span': {'key': 'columnSpan', 'type': 'int'},
        'row_span': {'key': 'rowSpan', 'type': 'int'}
    }

    def __init__(self, column_span: Optional[int] = None, row_span: Optional[int] = None) -> None:
        super(WidgetSize, self).__init__()
        self.column_span = column_span
        self.row_span = row_span


class LightboxOptions(Model):
    """
    Lightbox configuration

    :param height: Height of desired lightbox, in pixels
    :type height: int
    :param resizable: True to allow lightbox resizing, false to disallow lightbox resizing, defaults to false.
    :type resizable: bool
    :param width: Width of desired lightbox, in pixels
    :type width: int
    """

    _attribute_map = {
        'height': {'key': 'height', 'type': 'int'},
        'resizable': {'key': 'resizable', 'type': 'bool'},
        'width': {'key': 'width', 'type': 'int'}
    }

    def __init__(self, height: Optional[int] = None, resizable: Optional[bool] = None,
                 width: Optional[int] = None) -> None:
        super(LightboxOptions, self).__init__()
        self.height = height
        self.resizable = resizable
        self.width = width


class WidgetPosition(Model):
    """
    :param column:
    :type column: int
    :param row:
    :type row: int
    """

    _attribute_map = {
        'column': {'key': 'column', 'type': 'int'},
        'row': {'key': 'row', 'type': 'int'}
    }

    def __init__(self, column: Optional[int] = None, row: Optional[int] = None) -> None:
        super(WidgetPosition, self).__init__()
        self.column = column
        self.row = row


class SemanticVersion(Model):
    """
    versioning for an artifact as described at: http://semver.org/, of the form major.minor.patch.

    :param major: Major version when you make incompatible API changes
    :type major: int
    :param minor: Minor version when you add functionality in a backwards-compatible manner
    :type minor: int
    :param patch: Patch version when you make backwards-compatible bug fixes
    :type patch: int
    """

    _attribute_map = {
        'major': {'key': 'major', 'type': 'int'},
        'minor': {'key': 'minor', 'type': 'int'},
        'patch': {'key': 'patch', 'type': 'int'}
    }

    def __init__(self, major: Optional[int] = None, minor: Optional[int] = None, patch: Optional[int] = None) -> None:
        super(SemanticVersion, self).__init__()
        self.major = major
        self.minor = minor
        self.patch = patch


class Widget(Model):
    """
    Widget data

    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v7_0.dashboard.models.ReferenceLinks>`
    :param allowed_sizes: Refers to the allowed sizes for the widget. This gets populated when user wants to configure the widget
    :type allowed_sizes: list of :class:`WidgetSize <azure.devops.v7_0.dashboard.models.WidgetSize>`
    :param are_settings_blocked_for_user: Read-Only Property from Dashboard Service. Indicates if settings are blocked for the current user.
    :type are_settings_blocked_for_user: bool
    :param artifact_id: Refers to unique identifier of a feature artifact. Used for pinning+unpinning a specific artifact.
    :type artifact_id: str
    :param configuration_contribution_id:
    :type configuration_contribution_id: str
    :param configuration_contribution_relative_id:
    :type configuration_contribution_relative_id: str
    :param content_uri:
    :type content_uri: str
    :param contribution_id: The id of the underlying contribution defining the supplied Widget Configuration.
    :type contribution_id: str
    :param dashboard: Optional partial dashboard content, to support exchanging dashboard-level version ETag for widget-level APIs
    :type dashboard: :class:`Dashboard <azure.devops.v7_0.dashboard.models.Dashboard>`
    :param eTag:
    :type eTag: str
    :param id:
    :type id: str
    :param is_enabled:
    :type is_enabled: bool
    :param is_name_configurable:
    :type is_name_configurable: bool
    :param lightbox_options:
    :type lightbox_options: :class:`LightboxOptions <azure.devops.v7_0.dashboard.models.LightboxOptions>`
    :param loading_image_url:
    :type loading_image_url: str
    :param name:
    :type name: str
    :param position:
    :type position: :class:`WidgetPosition <azure.devops.v7_0.dashboard.models.WidgetPosition>`
    :param settings:
    :type settings: str
    :param settings_version:
    :type settings_version: :class:`SemanticVersion <azure.devops.v7_0.dashboard.models.SemanticVersion>`
    :param size:
    :type size: :class:`WidgetSize <azure.devops.v7_0.dashboard.models.WidgetSize>`
    :param type_id:
    :type type_id: str
    :param url:
    :type url: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'allowed_sizes': {'key': 'allowedSizes', 'type': '[WidgetSize]'},
        'are_settings_blocked_for_user': {'key': 'areSettingsBlockedForUser', 'type': 'bool'},
        'artifact_id': {'key': 'artifactId', 'type': 'str'},
        'configuration_contribution_id': {'key': 'configurationContributionId', 'type': 'str'},
        'configuration_contribution_relative_id': {'key': 'configurationContributionRelativeId', 'type': 'str'},
        'content_uri': {'key': 'contentUri', 'type': 'str'},
        'contribution_id': {'key': 'contributionId', 'type': 'str'},
        'dashboard': {'key': 'dashboard', 'type': 'Dashboard'},
        'eTag': {'key': 'eTag', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'is_enabled': {'key': 'isEnabled', 'type': 'bool'},
        'is_name_configurable': {'key': 'isNameConfigurable', 'type': 'bool'},
        'lightbox_options': {'key': 'lightboxOptions', 'type': 'LightboxOptions'},
        'loading_image_url': {'key': 'loadingImageUrl', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'position': {'key': 'position', 'type': 'WidgetPosition'},
        'settings': {'key': 'settings', 'type': 'str'},
        'settings_version': {'key': 'settingsVersion', 'type': 'SemanticVersion'},
        'size': {'key': 'size', 'type': 'WidgetSize'},
        'type_id': {'key': 'typeId', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links: Optional[ReferenceLinks] = None, allowed_sizes: Optional[List[WidgetSize]] = None,
                 are_settings_blocked_for_user: Optional[bool] = None, artifact_id: Optional[str] = None,
                 configuration_contribution_id: Optional[str] = None,
                 configuration_contribution_relative_id: Optional[str] = None, content_uri: Optional[str] = None,
                 contribution_id: Optional[str] = None, dashboard=None, eTag: Optional[str] = None,
                 id: Optional[str] = None, is_enabled: Optional[bool] = None,
                 is_name_configurable: Optional[bool] = None, lightbox_options: Optional[LightboxOptions] = None,
                 loading_image_url: Optional[str] = None, name: Optional[str] = None,
                 position: Optional[WidgetPosition] = None, settings: Optional[str] = None,
                 settings_version: Optional[SemanticVersion] = None, size: Optional[WidgetSize] = None,
                 type_id: Optional[str] = None, url: Optional[str] = None) -> None:
        super(Widget, self).__init__()
        self._links = _links
        self.allowed_sizes = allowed_sizes
        self.are_settings_blocked_for_user = are_settings_blocked_for_user
        self.artifact_id = artifact_id
        self.configuration_contribution_id = configuration_contribution_id
        self.configuration_contribution_relative_id = configuration_contribution_relative_id
        self.content_uri = content_uri
        self.contribution_id = contribution_id
        self.dashboard = dashboard
        self.eTag = eTag
        self.id = id
        self.is_enabled = is_enabled
        self.is_name_configurable = is_name_configurable
        self.lightbox_options = lightbox_options
        self.loading_image_url = loading_image_url
        self.name = name
        self.position = position
        self.settings = settings
        self.settings_version = settings_version
        self.size = size
        self.type_id = type_id
        self.url = url


class Dashboard(Model):
    """
    Model of a Dashboard.

    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v7_0.dashboard.models.ReferenceLinks>`
    :param dashboard_scope: Entity to which the dashboard is scoped.
    :type dashboard_scope: object
    :param description: Description of the dashboard.
    :type description: str
    :param eTag: Server defined version tracking value, used for edit collision detection.
    :type eTag: str
    :param group_id: ID of the group for a dashboard. For team-scoped dashboards, this is the unique identifier for the team associated with the dashboard. For project-scoped dashboards this property is empty.
    :type group_id: str
    :param id: ID of the Dashboard. Provided by service at creation time.
    :type id: str
    :param name: Name of the Dashboard.
    :type name: str
    :param owner_id: ID of the owner for a dashboard. For team-scoped dashboards, this is the unique identifier for the team associated with the dashboard. For project-scoped dashboards, this is the unique identifier for the user identity associated with the dashboard.
    :type owner_id: str
    :param position: Position of the dashboard, within a dashboard group. If unset at creation time, position is decided by the service.
    :type position: int
    :param refresh_interval: Interval for client to automatically refresh the dashboard. Expressed in minutes.
    :type refresh_interval: int
    :param url:
    :type url: str
    :param widgets: The set of Widgets on the dashboard.
    :type widgets: list of :class:`Widget <azure.devops.v7_0.dashboard.models.Widget>`
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'dashboard_scope': {'key': 'dashboardScope', 'type': 'object'},
        'description': {'key': 'description', 'type': 'str'},
        'eTag': {'key': 'eTag', 'type': 'str'},
        'group_id': {'key': 'groupId', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'owner_id': {'key': 'ownerId', 'type': 'str'},
        'position': {'key': 'position', 'type': 'int'},
        'refresh_interval': {'key': 'refreshInterval', 'type': 'int'},
        'url': {'key': 'url', 'type': 'str'},
        'widgets': {'key': 'widgets', 'type': '[Widget]'}
    }

    def __init__(self, _links: Optional[ReferenceLinks] = None, dashboard_scope=None, description: Optional[str] = None,
                 eTag: Optional[str] = None, group_id: Optional[str] = None, id: Optional[str] = None,
                 name: Optional[str] = None, owner_id: Optional[str] = None, position: Optional[int] = None,
                 refresh_interval: Optional[int] = None, url: Optional[str] = None,
                 widgets: Optional[List[Widget]] = None) -> None:
        super(Dashboard, self).__init__()
        self._links = _links
        self.dashboard_scope = dashboard_scope
        self.description = description
        self.eTag = eTag
        self.group_id = group_id
        self.id = id
        self.name = name
        self.owner_id = owner_id
        self.position = position
        self.refresh_interval = refresh_interval
        self.url = url
        self.widgets = widgets


class CopyDashboardResponse(Model):
    """
    :param copied_dashboard: Copied Dashboard
    :type copied_dashboard: :class:`Dashboard <azure.devops.v7_0.dashboard.models.Dashboard>`
    :param copy_dashboard_options: Copy Dashboard options
    :type copy_dashboard_options: :class:`CopyDashboardOptions <azure.devops.v7_0.dashboard.models.CopyDashboardOptions>`
    """

    _attribute_map = {
        'copied_dashboard': {'key': 'copiedDashboard', 'type': 'Dashboard'},
        'copy_dashboard_options': {'key': 'copyDashboardOptions', 'type': 'CopyDashboardOptions'}
    }

    def __init__(self, copied_dashboard: Optional[Dashboard] = None,
                 copy_dashboard_options: Optional[CopyDashboardOptions] = None) -> None:
        super(CopyDashboardResponse, self).__init__()
        self.copied_dashboard = copied_dashboard
        self.copy_dashboard_options = copy_dashboard_options


class DashboardGroupEntry(Dashboard):
    """
    Dashboard group entry, wrapping around Dashboard (needed?)

    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v7_0.dashboard.models.ReferenceLinks>`
    :param dashboard_scope: Entity to which the dashboard is scoped.
    :type dashboard_scope: object
    :param description: Description of the dashboard.
    :type description: str
    :param eTag: Server defined version tracking value, used for edit collision detection.
    :type eTag: str
    :param group_id: ID of the group for a dashboard. For team-scoped dashboards, this is the unique identifier for the team associated with the dashboard. For project-scoped dashboards this property is empty.
    :type group_id: str
    :param id: ID of the Dashboard. Provided by service at creation time.
    :type id: str
    :param name: Name of the Dashboard.
    :type name: str
    :param owner_id: ID of the owner for a dashboard. For team-scoped dashboards, this is the unique identifier for the team associated with the dashboard. For project-scoped dashboards, this is the unique identifier for the user identity associated with the dashboard.
    :type owner_id: str
    :param position: Position of the dashboard, within a dashboard group. If unset at creation time, position is decided by the service.
    :type position: int
    :param refresh_interval: Interval for client to automatically refresh the dashboard. Expressed in minutes.
    :type refresh_interval: int
    :param url:
    :type url: str
    :param widgets: The set of Widgets on the dashboard.
    :type widgets: list of :class:`Widget <azure.devops.v7_0.dashboard.models.Widget>`
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'dashboard_scope': {'key': 'dashboardScope', 'type': 'object'},
        'description': {'key': 'description', 'type': 'str'},
        'eTag': {'key': 'eTag', 'type': 'str'},
        'group_id': {'key': 'groupId', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'owner_id': {'key': 'ownerId', 'type': 'str'},
        'position': {'key': 'position', 'type': 'int'},
        'refresh_interval': {'key': 'refreshInterval', 'type': 'int'},
        'url': {'key': 'url', 'type': 'str'},
        'widgets': {'key': 'widgets', 'type': '[Widget]'},
    }

    def __init__(self, _links: Optional[ReferenceLinks] = None, dashboard_scope: Optional[Dict[Any, Any]] = None,
                 description: Optional[str] = None, eTag: Optional[str] = None, group_id: Optional[str] = None,
                 id: Optional[str] = None, name: Optional[str] = None, owner_id: Optional[str] = None,
                 position: Optional[int] = None, refresh_interval: Optional[int] = None, url: Optional[str] = None,
                 widgets: Optional[List[Widget]] = None) -> None:
        super(DashboardGroupEntry, self).__init__(_links=_links, dashboard_scope=dashboard_scope,
                                                  description=description, eTag=eTag, group_id=group_id, id=id,
                                                  name=name, owner_id=owner_id, position=position,
                                                  refresh_interval=refresh_interval, url=url, widgets=widgets)


class DashboardGroup(Model):
    """
    Describes a list of dashboards associated to an owner. Currently, teams own dashboard groups.

    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v7_0.dashboard.models.ReferenceLinks>`
    :param dashboard_entries: A list of Dashboards held by the Dashboard Group
    :type dashboard_entries: list of :class:`DashboardGroupEntry <azure.devops.v7_0.dashboard.models.DashboardGroupEntry>`
    :param permission: Deprecated: The old permission model describing the level of permissions for the current team. Pre-M125.
    :type permission: object
    :param team_dashboard_permission: A permissions bit mask describing the security permissions of the current team for dashboards. When this permission is the value None, use GroupMemberPermission. Permissions are evaluated based on the presence of a value other than None, else the GroupMemberPermission will be saved.
    :type team_dashboard_permission: object
    :param url:
    :type url: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'dashboard_entries': {'key': 'dashboardEntries', 'type': '[DashboardGroupEntry]'},
        'permission': {'key': 'permission', 'type': 'object'},
        'team_dashboard_permission': {'key': 'teamDashboardPermission', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links: Optional[ReferenceLinks] = None,
                 dashboard_entries: Optional[List[DashboardGroupEntry]] = None,
                 permission: Optional[Dict[Any, Any]] = None,
                 team_dashboard_permission: Optional[Dict[Any, Any]] = None,
                 url: Optional[str] = None) -> None:
        super(DashboardGroup, self).__init__()
        self._links = _links
        self.dashboard_entries = dashboard_entries
        self.permission = permission
        self.team_dashboard_permission = team_dashboard_permission
        self.url = url


class DashboardGroupEntryResponse(DashboardGroupEntry):
    """
    Response from RestAPI when saving and editing DashboardGroupEntry

    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v7_0.dashboard.models.ReferenceLinks>`
    :param dashboard_scope: Entity to which the dashboard is scoped.
    :type dashboard_scope: object
    :param description: Description of the dashboard.
    :type description: str
    :param eTag: Server defined version tracking value, used for edit collision detection.
    :type eTag: str
    :param group_id: ID of the group for a dashboard. For team-scoped dashboards, this is the unique identifier for the team associated with the dashboard. For project-scoped dashboards this property is empty.
    :type group_id: str
    :param id: ID of the Dashboard. Provided by service at creation time.
    :type id: str
    :param name: Name of the Dashboard.
    :type name: str
    :param owner_id: ID of the owner for a dashboard. For team-scoped dashboards, this is the unique identifier for the team associated with the dashboard. For project-scoped dashboards, this is the unique identifier for the user identity associated with the dashboard.
    :type owner_id: str
    :param position: Position of the dashboard, within a dashboard group. If unset at creation time, position is decided by the service.
    :type position: int
    :param refresh_interval: Interval for client to automatically refresh the dashboard. Expressed in minutes.
    :type refresh_interval: int
    :param url:
    :type url: str
    :param widgets: The set of Widgets on the dashboard.
    :type widgets: list of :class:`Widget <azure.devops.v7_0.dashboard.models.Widget>`
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'dashboard_scope': {'key': 'dashboardScope', 'type': 'object'},
        'description': {'key': 'description', 'type': 'str'},
        'eTag': {'key': 'eTag', 'type': 'str'},
        'group_id': {'key': 'groupId', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'owner_id': {'key': 'ownerId', 'type': 'str'},
        'position': {'key': 'position', 'type': 'int'},
        'refresh_interval': {'key': 'refreshInterval', 'type': 'int'},
        'url': {'key': 'url', 'type': 'str'},
        'widgets': {'key': 'widgets', 'type': '[Widget]'},
    }

    def __init__(self, _links: Optional[ReferenceLinks] = None, dashboard_scope: Optional[Dict[Any, Any]] = None,
                 description: Optional[str] = None, eTag: Optional[str] = None, group_id: Optional[str] = None,
                 id: Optional[str] = None, name: Optional[str] = None, owner_id: Optional[str] = None,
                 position: Optional[int] = None, refresh_interval: Optional[int] = None, url: Optional[str] = None,
                 widgets: Optional[List[Widget]] = None) -> None:
        super(DashboardGroupEntryResponse, self).__init__(_links=_links, dashboard_scope=dashboard_scope,
                                                          description=description, eTag=eTag, group_id=group_id, id=id,
                                                          name=name, owner_id=owner_id, position=position,
                                                          refresh_interval=refresh_interval, url=url, widgets=widgets)


class DashboardResponse(DashboardGroupEntry):
    """
    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v7_0.dashboard.models.ReferenceLinks>`
    :param dashboard_scope: Entity to which the dashboard is scoped.
    :type dashboard_scope: object
    :param description: Description of the dashboard.
    :type description: str
    :param eTag: Server defined version tracking value, used for edit collision detection.
    :type eTag: str
    :param group_id: ID of the group for a dashboard. For team-scoped dashboards, this is the unique identifier for the team associated with the dashboard. For project-scoped dashboards this property is empty.
    :type group_id: str
    :param id: ID of the Dashboard. Provided by service at creation time.
    :type id: str
    :param name: Name of the Dashboard.
    :type name: str
    :param owner_id: ID of the owner for a dashboard. For team-scoped dashboards, this is the unique identifier for the team associated with the dashboard. For project-scoped dashboards, this is the unique identifier for the user identity associated with the dashboard.
    :type owner_id: str
    :param position: Position of the dashboard, within a dashboard group. If unset at creation time, position is decided by the service.
    :type position: int
    :param refresh_interval: Interval for client to automatically refresh the dashboard. Expressed in minutes.
    :type refresh_interval: int
    :param url:
    :type url: str
    :param widgets: The set of Widgets on the dashboard.
    :type widgets: list of :class:`Widget <azure.devops.v7_0.dashboard.models.Widget>`
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'dashboard_scope': {'key': 'dashboardScope', 'type': 'object'},
        'description': {'key': 'description', 'type': 'str'},
        'eTag': {'key': 'eTag', 'type': 'str'},
        'group_id': {'key': 'groupId', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'owner_id': {'key': 'ownerId', 'type': 'str'},
        'position': {'key': 'position', 'type': 'int'},
        'refresh_interval': {'key': 'refreshInterval', 'type': 'int'},
        'url': {'key': 'url', 'type': 'str'},
        'widgets': {'key': 'widgets', 'type': '[Widget]'},
    }

    def __init__(self, _links: Optional[ReferenceLinks] = None, dashboard_scope: Optional[Dict[Any, Any]] = None,
                 description: Optional[str] = None, eTag: Optional[str] = None, group_id: Optional[str] = None,
                 id: Optional[str] = None, name: Optional[str] = None, owner_id: Optional[str] = None,
                 position: Optional[int] = None, refresh_interval: Optional[int] = None, url: Optional[str] = None,
                 widgets: Optional[List[Widget]] = None) -> None:
        super(DashboardResponse, self).__init__(_links=_links, dashboard_scope=dashboard_scope, description=description,
                                                eTag=eTag, group_id=group_id, id=id, name=name, owner_id=owner_id,
                                                position=position, refresh_interval=refresh_interval, url=url,
                                                widgets=widgets)


class TeamContext(Model):
    """
    The Team Context for an operation.

    :param project: The team project Id or name.  Ignored if ProjectId is set.
    :type project: str
    :param project_id: The Team Project ID.  Required if Project is not set.
    :type project_id: str
    :param team: The Team Id or name.  Ignored if TeamId is set.
    :type team: str
    :param team_id: The Team Id
    :type team_id: str
    """

    _attribute_map = {
        'project': {'key': 'project', 'type': 'str'},
        'project_id': {'key': 'projectId', 'type': 'str'},
        'team': {'key': 'team', 'type': 'str'},
        'team_id': {'key': 'teamId', 'type': 'str'}
    }

    def __init__(self, project: Optional[str] = None, project_id: Optional[str] = None, team: Optional[str] = None,
                 team_id: Optional[str] = None) -> None:
        super(TeamContext, self).__init__()
        self.project = project
        self.project_id = project_id
        self.team = team
        self.team_id = team_id


class WidgetMetadata(Model):
    """
    Contribution based information describing Dashboard Widgets.

    :param allowed_sizes: Sizes supported by the Widget.
    :type allowed_sizes: list of :class:`WidgetSize <azure.devops.v7_0.dashboard.models.WidgetSize>`
    :param analytics_service_required: Opt-in boolean that indicates if the widget requires the Analytics Service to function. Widgets requiring the analytics service are hidden from the catalog if the Analytics Service is not available.
    :type analytics_service_required: bool
    :param catalog_icon_url: Resource for an icon in the widget catalog.
    :type catalog_icon_url: str
    :param catalog_info_url: Opt-in URL string pointing at widget information. Defaults to extension marketplace URL if omitted
    :type catalog_info_url: str
    :param configuration_contribution_id: The id of the underlying contribution defining the supplied Widget custom configuration UI. Null if custom configuration UI is not available.
    :type configuration_contribution_id: str
    :param configuration_contribution_relative_id: The relative id of the underlying contribution defining the supplied Widget custom configuration UI. Null if custom configuration UI is not available.
    :type configuration_contribution_relative_id: str
    :param configuration_required: Indicates if the widget requires configuration before being added to dashboard.
    :type configuration_required: bool
    :param content_uri: Uri for the widget content to be loaded from .
    :type content_uri: str
    :param contribution_id: The id of the underlying contribution defining the supplied Widget.
    :type contribution_id: str
    :param default_settings: Optional default settings to be copied into widget settings.
    :type default_settings: str
    :param description: Summary information describing the widget.
    :type description: str
    :param is_enabled: Widgets can be disabled by the app store.  We'll need to gracefully handle for: - persistence (Allow) - Requests (Tag as disabled, and provide context)
    :type is_enabled: bool
    :param is_name_configurable: Opt-out boolean that indicates if the widget supports widget name/title configuration. Widgets ignoring the name should set it to false in the manifest.
    :type is_name_configurable: bool
    :param is_visible_from_catalog: Opt-out boolean indicating if the widget is hidden from the catalog. Commonly, this is used to allow developers to disable creation of a deprecated widget. A widget must have a functional default state, or have a configuration experience, in order to be visible from the catalog.
    :type is_visible_from_catalog: bool
    :param keywords: Keywords associated with this widget, non-filterable and invisible
    :type keywords: list of str
    :param lightbox_options: Opt-in properties for customizing widget presentation in a "lightbox" dialog.
    :type lightbox_options: :class:`LightboxOptions <azure.devops.v7_0.dashboard.models.LightboxOptions>`
    :param loading_image_url: Resource for a loading placeholder image on dashboard
    :type loading_image_url: str
    :param name: User facing name of the widget type. Each widget must use a unique value here.
    :type name: str
    :param publisher_name: Publisher Name of this kind of widget.
    :type publisher_name: str
    :param supported_scopes: Data contract required for the widget to function and to work in its container.
    :type supported_scopes: list of WidgetScope
    :param tags: Tags associated with this widget, visible on each widget and filterable.
    :type tags: list of str
    :param targets: Contribution target IDs
    :type targets: list of str
    :param type_id: Deprecated: locally unique developer-facing id of this kind of widget. ContributionId provides a globally unique identifier for widget types.
    :type type_id: str
    """

    _attribute_map = {
        'allowed_sizes': {'key': 'allowedSizes', 'type': '[WidgetSize]'},
        'analytics_service_required': {'key': 'analyticsServiceRequired', 'type': 'bool'},
        'catalog_icon_url': {'key': 'catalogIconUrl', 'type': 'str'},
        'catalog_info_url': {'key': 'catalogInfoUrl', 'type': 'str'},
        'configuration_contribution_id': {'key': 'configurationContributionId', 'type': 'str'},
        'configuration_contribution_relative_id': {'key': 'configurationContributionRelativeId', 'type': 'str'},
        'configuration_required': {'key': 'configurationRequired', 'type': 'bool'},
        'content_uri': {'key': 'contentUri', 'type': 'str'},
        'contribution_id': {'key': 'contributionId', 'type': 'str'},
        'default_settings': {'key': 'defaultSettings', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'is_enabled': {'key': 'isEnabled', 'type': 'bool'},
        'is_name_configurable': {'key': 'isNameConfigurable', 'type': 'bool'},
        'is_visible_from_catalog': {'key': 'isVisibleFromCatalog', 'type': 'bool'},
        'keywords': {'key': 'keywords', 'type': '[str]'},
        'lightbox_options': {'key': 'lightboxOptions', 'type': 'LightboxOptions'},
        'loading_image_url': {'key': 'loadingImageUrl', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'publisher_name': {'key': 'publisherName', 'type': 'str'},
        'supported_scopes': {'key': 'supportedScopes', 'type': '[object]'},
        'tags': {'key': 'tags', 'type': '[str]'},
        'targets': {'key': 'targets', 'type': '[str]'},
        'type_id': {'key': 'typeId', 'type': 'str'}
    }

    def __init__(self, allowed_sizes: Optional[List[WidgetSize]] = None,
                 analytics_service_required: Optional[bool] = None,
                 catalog_icon_url: Optional[str] = None, catalog_info_url: Optional[str] = None,
                 configuration_contribution_id: Optional[str] = None,
                 configuration_contribution_relative_id: Optional[str] = None,
                 configuration_required: Optional[bool] = None, content_uri: Optional[str] = None,
                 contribution_id: Optional[str] = None, default_settings: Optional[str] = None,
                 description: Optional[str] = None, is_enabled: Optional[bool] = None,
                 is_name_configurable: Optional[bool] = None, is_visible_from_catalog: Optional[bool] = None,
                 keywords: Optional[List[str]] = None, lightbox_options: Optional[LightboxOptions] = None,
                 loading_image_url: Optional[str] = None, name: Optional[str] = None,
                 publisher_name: Optional[str] = None, supported_scopes: Optional[List[Dict[Any, Any]]] = None,
                 tags: Optional[List[str]] = None, targets: Optional[List[str]] = None,
                 type_id: Optional[str] = None) -> None:
        super(WidgetMetadata, self).__init__()
        self.allowed_sizes = allowed_sizes
        self.analytics_service_required = analytics_service_required
        self.catalog_icon_url = catalog_icon_url
        self.catalog_info_url = catalog_info_url
        self.configuration_contribution_id = configuration_contribution_id
        self.configuration_contribution_relative_id = configuration_contribution_relative_id
        self.configuration_required = configuration_required
        self.content_uri = content_uri
        self.contribution_id = contribution_id
        self.default_settings = default_settings
        self.description = description
        self.is_enabled = is_enabled
        self.is_name_configurable = is_name_configurable
        self.is_visible_from_catalog = is_visible_from_catalog
        self.keywords = keywords
        self.lightbox_options = lightbox_options
        self.loading_image_url = loading_image_url
        self.name = name
        self.publisher_name = publisher_name
        self.supported_scopes = supported_scopes
        self.tags = tags
        self.targets = targets
        self.type_id = type_id


class WidgetMetadataResponse(Model):
    """
    :param uri:
    :type uri: str
    :param widget_metadata:
    :type widget_metadata: :class:`WidgetMetadata <azure.devops.v7_0.dashboard.models.WidgetMetadata>`
    """

    _attribute_map = {
        'uri': {'key': 'uri', 'type': 'str'},
        'widget_metadata': {'key': 'widgetMetadata', 'type': 'WidgetMetadata'}
    }

    def __init__(self, uri: Optional[str] = None, widget_metadata: Optional[WidgetMetadata] = None) -> None:
        super(WidgetMetadataResponse, self).__init__()
        self.uri = uri
        self.widget_metadata = widget_metadata


class WidgetResponse(Widget):
    """
    Response from RestAPI when saving and editing Widget

    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v7_0.dashboard.models.ReferenceLinks>`
    :param allowed_sizes: Refers to the allowed sizes for the widget. This gets populated when user wants to configure the widget
    :type allowed_sizes: list of :class:`WidgetSize <azure.devops.v7_0.dashboard.models.WidgetSize>`
    :param are_settings_blocked_for_user: Read-Only Property from Dashboard Service. Indicates if settings are blocked for the current user.
    :type are_settings_blocked_for_user: bool
    :param artifact_id: Refers to unique identifier of a feature artifact. Used for pinning+unpinning a specific artifact.
    :type artifact_id: str
    :param configuration_contribution_id:
    :type configuration_contribution_id: str
    :param configuration_contribution_relative_id:
    :type configuration_contribution_relative_id: str
    :param content_uri:
    :type content_uri: str
    :param contribution_id: The id of the underlying contribution defining the supplied Widget Configuration.
    :type contribution_id: str
    :param dashboard: Optional partial dashboard content, to support exchanging dashboard-level version ETag for widget-level APIs
    :type dashboard: :class:`Dashboard <azure.devops.v7_0.dashboard.models.Dashboard>`
    :param eTag:
    :type eTag: str
    :param id:
    :type id: str
    :param is_enabled:
    :type is_enabled: bool
    :param is_name_configurable:
    :type is_name_configurable: bool
    :param lightbox_options:
    :type lightbox_options: :class:`LightboxOptions <azure.devops.v7_0.dashboard.models.LightboxOptions>`
    :param loading_image_url:
    :type loading_image_url: str
    :param name:
    :type name: str
    :param position:
    :type position: :class:`WidgetPosition <azure.devops.v7_0.dashboard.models.WidgetPosition>`
    :param settings:
    :type settings: str
    :param settings_version:
    :type settings_version: :class:`SemanticVersion <azure.devops.v7_0.dashboard.models.SemanticVersion>`
    :param size:
    :type size: :class:`WidgetSize <azure.devops.v7_0.dashboard.models.WidgetSize>`
    :param type_id:
    :type type_id: str
    :param url:
    :type url: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'allowed_sizes': {'key': 'allowedSizes', 'type': '[WidgetSize]'},
        'are_settings_blocked_for_user': {'key': 'areSettingsBlockedForUser', 'type': 'bool'},
        'artifact_id': {'key': 'artifactId', 'type': 'str'},
        'configuration_contribution_id': {'key': 'configurationContributionId', 'type': 'str'},
        'configuration_contribution_relative_id': {'key': 'configurationContributionRelativeId', 'type': 'str'},
        'content_uri': {'key': 'contentUri', 'type': 'str'},
        'contribution_id': {'key': 'contributionId', 'type': 'str'},
        'dashboard': {'key': 'dashboard', 'type': 'Dashboard'},
        'eTag': {'key': 'eTag', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'is_enabled': {'key': 'isEnabled', 'type': 'bool'},
        'is_name_configurable': {'key': 'isNameConfigurable', 'type': 'bool'},
        'lightbox_options': {'key': 'lightboxOptions', 'type': 'LightboxOptions'},
        'loading_image_url': {'key': 'loadingImageUrl', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'position': {'key': 'position', 'type': 'WidgetPosition'},
        'settings': {'key': 'settings', 'type': 'str'},
        'settings_version': {'key': 'settingsVersion', 'type': 'SemanticVersion'},
        'size': {'key': 'size', 'type': 'WidgetSize'},
        'type_id': {'key': 'typeId', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
    }

    def __init__(self, _links: Optional[ReferenceLinks] = None, allowed_sizes: Optional[List[WidgetSize]] = None,
                 are_settings_blocked_for_user: Optional[bool] = None, artifact_id: Optional[str] = None,
                 configuration_contribution_id: Optional[str] = None,
                 configuration_contribution_relative_id: Optional[str] = None, content_uri: Optional[str] = None,
                 contribution_id: Optional[str] = None, dashboard: Optional[Dashboard] = None,
                 eTag: Optional[str] = None, id: Optional[str] = None, is_enabled: Optional[bool] = None,
                 is_name_configurable: Optional[bool] = None, lightbox_options: Optional[LightboxOptions] = None,
                 loading_image_url: Optional[str] = None, name: Optional[str] = None,
                 position: Optional[WidgetPosition] = None, settings: Optional[str] = None,
                 settings_version: Optional[SemanticVersion] = None, size: Optional[WidgetSize] = None,
                 type_id: Optional[str] = None, url: Optional[str] = None) -> None:
        super(WidgetResponse, self).__init__(
            _links=_links, allowed_sizes=allowed_sizes,
            are_settings_blocked_for_user=are_settings_blocked_for_user,
            artifact_id=artifact_id,
            configuration_contribution_id=configuration_contribution_id,
            configuration_contribution_relative_id=configuration_contribution_relative_id,
            content_uri=content_uri, contribution_id=contribution_id,
            dashboard=dashboard, eTag=eTag, id=id, is_enabled=is_enabled,
            is_name_configurable=is_name_configurable,
            lightbox_options=lightbox_options, loading_image_url=loading_image_url,
            name=name, position=position, settings=settings,
            settings_version=settings_version, size=size, type_id=type_id, url=url)


class WidgetsVersionedList(Model):
    """
    Wrapper class to support HTTP header generation using CreateResponse, ClientHeaderParameter and ClientResponseType in WidgetV2Controller

    :param eTag:
    :type eTag: list of str
    :param widgets:
    :type widgets: list of :class:`Widget <azure.devops.v7_0.dashboard.models.Widget>`
    """

    _attribute_map = {
        'eTag': {'key': 'eTag', 'type': '[str]'},
        'widgets': {'key': 'widgets', 'type': '[Widget]'}
    }

    def __init__(self, eTag: Optional[List[str]] = None, widgets: Optional[List[Widget]] = None) -> None:
        super(WidgetsVersionedList, self).__init__()
        self.eTag = eTag
        self.widgets = widgets


class WidgetTypesResponse(Model):
    """
    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v7_0.dashboard.models.ReferenceLinks>`
    :param uri:
    :type uri: str
    :param widget_types:
    :type widget_types: list of :class:`WidgetMetadata <azure.devops.v7_0.dashboard.models.WidgetMetadata>`
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'uri': {'key': 'uri', 'type': 'str'},
        'widget_types': {'key': 'widgetTypes', 'type': '[WidgetMetadata]'}
    }

    def __init__(self, _links: Optional[ReferenceLinks] = None, uri: Optional[str] = None,
                 widget_types: Optional[List[WidgetMetadata]] = None) -> None:
        super(WidgetTypesResponse, self).__init__()
        self._links = _links
        self.uri = uri
        self.widget_types = widget_types


__all__ = [
    'CopyDashboardOptions',
    'CopyDashboardResponse',
    'Dashboard',
    'DashboardGroup',
    'DashboardGroupEntry',
    'DashboardGroupEntryResponse',
    'DashboardResponse',
    'LightboxOptions',
    'ReferenceLinks',
    'SemanticVersion',
    'TeamContext',
    'Widget',
    'WidgetMetadata',
    'WidgetMetadataResponse',
    'WidgetPosition',
    'WidgetResponse',
    'WidgetSize',
    'WidgetsVersionedList',
    'WidgetTypesResponse',
]
