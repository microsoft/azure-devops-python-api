# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------
from .accounts.accounts_client import AccountsClient
from .audit.audit_client import AuditClient
from .build.build_client import BuildClient
from .cix.cix_client import CixClient
from .client_trace.client_trace_client import ClientTraceClient
from .contributions.contributions_client import ContributionsClient
from .core.core_client import CoreClient
from .customer_intelligence.customer_intelligence_client import CustomerIntelligenceClient
from .dashboard.dashboard_client import DashboardClient
from .elastic.elastic_client import ElasticClient
from .extension_management.extension_management_client import ExtensionManagementClient
from .feature_availability.feature_availability_client import FeatureAvailabilityClient
from .feature_management.feature_management_client import FeatureManagementClient
from .feed.feed_client import FeedClient
from .file_container.file_container_client import FileContainerClient
from .gallery.gallery_client import GalleryClient
from .git.git_client import GitClient
from .graph.graph_client import GraphClient
from .identity.identity_client import IdentityClient
from .location.location_client import LocationClient
from .maven.maven_client import MavenClient
from .member_entitlement_management.member_entitlement_management_client import MemberEntitlementManagementClient
from .notification.notification_client import NotificationClient
from .npm.npm_client import NpmClient
from .nuget.nuget_client import NuGetClient
from .operations.operations_client import OperationsClient
from .pipeline_permissions.pipeline_permissions_client import PipelinePermissionsClient
from .pipelines.pipelines_client import PipelinesClient
from .pipelines_checks.pipelines_checks_client import PipelinesChecksClient
from .policy.policy_client import PolicyClient
from .profile.profile_client import ProfileClient
from .profile_regions.profile_regions_client import ProfileRegionsClient
from .project_analysis.project_analysis_client import ProjectAnalysisClient
from .provenance.provenance_client import ProvenanceClient
from .py_pi_api.py_pi_api_client import PyPiApiClient
from .release.release_client import ReleaseClient
from .sbom.sbom_client import SBOMClient
from .search.search_client import SearchClient
from .security.security_client import SecurityClient
from .service_endpoint.service_endpoint_client import ServiceEndpointClient
from .service_hooks.service_hooks_client import ServiceHooksClient
from .settings.settings_client import SettingsClient
from .symbol.symbol_client import SymbolClient
from .task.task_client import TaskClient
from .task_agent.task_agent_client import TaskAgentClient
from .test.test_client import TestClient
from .test_plan.test_plan_client import TestPlanClient
from .test_results.test_results_client import TestResultsClient
from .tfvc.tfvc_client import TfvcClient
from .token_admin.token_admin_client import TokenAdminClient
from .upack_api.upack_api_client import UPackApiClient
from .upack_packaging.upack_packaging_client import UPackPackagingClient
from .wiki.wiki_client import WikiClient
from .work.work_client import WorkClient
from .work_item_tracking.work_item_tracking_client import WorkItemTrackingClient
from .work_item_tracking_process.work_item_tracking_process_client import WorkItemTrackingProcessClient
from .work_item_tracking_process_template.work_item_tracking_process_template_client import WorkItemTrackingProcessTemplateClient


class ClientFactoryV7_1(object):
    """ClientFactoryV7_1.
    A factory class to get the 7.1 preview clients.
    """

    def __init__(self, connection) -> None:
        self._connection = connection

    def get_accounts_client(self) -> AccountsClient:
        """get_accounts_client.
        Gets the 7.1 version of the AccountsClient
        :rtype: :class:`<AccountsClient> <azure.devops.v7_1.accounts.accounts_client.AccountsClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.accounts.accounts_client.AccountsClient')

    def get_audit_client(self) -> AuditClient:
        """get_audit_client.
        Gets the 7.1 version of the AuditClient
        :rtype: :class:`<AuditClient> <azure.devops.v7_1.audit.audit_client.AuditClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.audit.audit_client.AuditClient')

    def get_build_client(self) -> BuildClient:
        """get_build_client.
        Gets the 7.1 version of the BuildClient
        :rtype: :class:`<BuildClient> <azure.devops.v7_1.build.build_client.BuildClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.build.build_client.BuildClient')

    def get_cix_client(self) -> CixClient:
        """get_cix_client.
        Gets the 7.1 version of the CixClient
        :rtype: :class:`<CixClient> <azure.devops.v7_1.cix.cix_client.CixClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.cix.cix_client.CixClient')

    def get_client_trace_client(self) -> ClientTraceClient:
        """get_client_trace_client.
        Gets the 7.1 version of the ClientTraceClient
        :rtype: :class:`<ClientTraceClient> <azure.devops.v7_1.client_trace.client_trace_client.ClientTraceClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.client_trace.client_trace_client.ClientTraceClient')

    def get_contributions_client(self) -> ContributionsClient:
        """get_contributions_client.
        Gets the 7.1 version of the ContributionsClient
        :rtype: :class:`<ContributionsClient> <azure.devops.v7_1.contributions.contributions_client.ContributionsClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.contributions.contributions_client.ContributionsClient')

    def get_core_client(self) -> CoreClient:
        """get_core_client.
        Gets the 7.1 version of the CoreClient
        :rtype: :class:`<CoreClient> <azure.devops.v7_1.core.core_client.CoreClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.core.core_client.CoreClient')

    def get_customer_intelligence_client(self) -> CustomerIntelligenceClient:
        """get_customer_intelligence_client.
        Gets the 7.1 version of the CustomerIntelligenceClient
        :rtype: :class:`<CustomerIntelligenceClient> <azure.devops.v7_1.customer_intelligence.customer_intelligence_client.CustomerIntelligenceClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.customer_intelligence.customer_intelligence_client.CustomerIntelligenceClient')

    def get_dashboard_client(self) -> DashboardClient:
        """get_dashboard_client.
        Gets the 7.1 version of the DashboardClient
        :rtype: :class:`<DashboardClient> <azure.devops.v7_1.dashboard.dashboard_client.DashboardClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.dashboard.dashboard_client.DashboardClient')

    def get_elastic_client(self) -> ElasticClient:
        """get_elastic_client.
        Gets the 7.1 version of the ElasticClient
        :rtype: :class:`<ElasticClient> <azure.devops.v7_1.elastic.elastic_client.ElasticClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.elastic.elastic_client.ElasticClient')

    def get_extension_management_client(self) -> ExtensionManagementClient:
        """get_extension_management_client.
        Gets the 7.1 version of the ExtensionManagementClient
        :rtype: :class:`<ExtensionManagementClient> <azure.devops.v7_1.extension_management.extension_management_client.ExtensionManagementClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.extension_management.extension_management_client.ExtensionManagementClient')

    def get_feature_availability_client(self) -> FeatureAvailabilityClient:
        """get_feature_availability_client.
        Gets the 7.1 version of the FeatureAvailabilityClient
        :rtype: :class:`<FeatureAvailabilityClient> <azure.devops.v7_1.feature_availability.feature_availability_client.FeatureAvailabilityClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.feature_availability.feature_availability_client.FeatureAvailabilityClient')

    def get_feature_management_client(self) -> FeatureManagementClient:
        """get_feature_management_client.
        Gets the 7.1 version of the FeatureManagementClient
        :rtype: :class:`<FeatureManagementClient> <azure.devops.v7_1.feature_management.feature_management_client.FeatureManagementClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.feature_management.feature_management_client.FeatureManagementClient')

    def get_feed_client(self) -> FeedClient:
        """get_feed_client.
        Gets the 7.1 version of the FeedClient
        :rtype: :class:`<FeedClient> <azure.devops.v7_1.feed.feed_client.FeedClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.feed.feed_client.FeedClient')

    def get_file_container_client(self) -> FileContainerClient:
        """get_file_container_client.
        Gets the 7.1 version of the FileContainerClient
        :rtype: :class:`<FileContainerClient> <azure.devops.v7_1.file_container.file_container_client.FileContainerClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.file_container.file_container_client.FileContainerClient')

    def get_gallery_client(self) -> GalleryClient:
        """get_gallery_client.
        Gets the 7.1 version of the GalleryClient
        :rtype: :class:`<GalleryClient> <azure.devops.v7_1.gallery.gallery_client.GalleryClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.gallery.gallery_client.GalleryClient')

    def get_git_client(self) -> GitClient:
        """get_git_client.
        Gets the 7.1 version of the GitClient
        :rtype: :class:`<GitClient> <azure.devops.v7_1.git.git_client.GitClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.git.git_client.GitClient')

    def get_graph_client(self) -> GraphClient:
        """get_graph_client.
        Gets the 7.1 version of the GraphClient
        :rtype: :class:`<GraphClient> <azure.devops.v7_1.graph.graph_client.GraphClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.graph.graph_client.GraphClient')

    def get_identity_client(self) -> IdentityClient:
        """get_identity_client.
        Gets the 7.1 version of the IdentityClient
        :rtype: :class:`<IdentityClient> <azure.devops.v7_1.identity.identity_client.IdentityClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.identity.identity_client.IdentityClient')

    def get_location_client(self) -> LocationClient:
        """get_location_client.
        Gets the 7.1 version of the LocationClient
        :rtype: :class:`<LocationClient> <azure.devops.v7_1.location.location_client.LocationClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.location.location_client.LocationClient')

    def get_maven_client(self) -> MavenClient:
        """get_maven_client.
        Gets the 7.1 version of the MavenClient
        :rtype: :class:`<MavenClient> <azure.devops.v7_1.maven.maven_client.MavenClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.maven.maven_client.MavenClient')

    def get_member_entitlement_management_client(self) -> MemberEntitlementManagementClient:
        """get_member_entitlement_management_client.
        Gets the 7.1 version of the MemberEntitlementManagementClient
        :rtype: :class:`<MemberEntitlementManagementClient> <azure.devops.v7_1.member_entitlement_management.member_entitlement_management_client.MemberEntitlementManagementClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.member_entitlement_management.member_entitlement_management_client.MemberEntitlementManagementClient')

    def get_notification_client(self) -> NotificationClient:
        """get_notification_client.
        Gets the 7.1 version of the NotificationClient
        :rtype: :class:`<NotificationClient> <azure.devops.v7_1.notification.notification_client.NotificationClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.notification.notification_client.NotificationClient')

    def get_npm_client(self) -> NpmClient:
        """get_npm_client.
        Gets the 7.1 version of the NpmClient
        :rtype: :class:`<NpmClient> <azure.devops.v7_1.npm.npm_client.NpmClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.npm.npm_client.NpmClient')

    def get_nuget_client(self) -> NuGetClient:
        """get_nuget_client.
        Gets the 7.1 version of the NuGetClient
        :rtype: :class:`<NuGetClient> <azure.devops.v7_1.nuget.nuget_client.NuGetClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.nuget.nuget_client.NuGetClient')

    def get_operations_client(self) -> OperationsClient:
        """get_operations_client.
        Gets the 7.1 version of the OperationsClient
        :rtype: :class:`<OperationsClient> <azure.devops.v7_1.operations.operations_client.OperationsClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.operations.operations_client.OperationsClient')

    def get_pipeline_permissions_client(self) -> PipelinePermissionsClient:
        """get_pipeline_permissions_client.
        Gets the 7.1 version of the PipelinePermissionsClient
        :rtype: :class:`<PipelinePermissionsClient> <azure.devops.v7_1.pipeline_permissions.pipeline_permissions_client.PipelinePermissionsClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.pipeline_permissions.pipeline_permissions_client.PipelinePermissionsClient')

    def get_pipelines_client(self) -> PipelinesClient:
        """get_pipelines_client.
        Gets the 7.1 version of the PipelinesClient
        :rtype: :class:`<PipelinesClient> <azure.devops.v7_1.pipelines.pipelines_client.PipelinesClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.pipelines.pipelines_client.PipelinesClient')

    def get_pipelines_checks_client(self) -> PipelinesChecksClient:
        """get_pipelines_checks_client.
        Gets the 7.1 version of the PipelinesChecksClient
        :rtype: :class:`<PipelinesChecksClient> <azure.devops.v7_1.pipelines_checks.pipelines_checks_client.PipelinesChecksClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.pipelines_checks.pipelines_checks_client.PipelinesChecksClient')

    def get_policy_client(self) -> PolicyClient:
        """get_policy_client.
        Gets the 7.1 version of the PolicyClient
        :rtype: :class:`<PolicyClient> <azure.devops.v7_1.policy.policy_client.PolicyClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.policy.policy_client.PolicyClient')

    def get_profile_client(self) -> ProfileClient:
        """get_profile_client.
        Gets the 7.1 version of the ProfileClient
        :rtype: :class:`<ProfileClient> <azure.devops.v7_1.profile.profile_client.ProfileClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.profile.profile_client.ProfileClient')

    def get_profile_regions_client(self) -> ProfileRegionsClient:
        """get_profile_regions_client.
        Gets the 7.1 version of the ProfileRegionsClient
        :rtype: :class:`<ProfileRegionsClient> <azure.devops.v7_1.profile_regions.profile_regions_client.ProfileRegionsClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.profile_regions.profile_regions_client.ProfileRegionsClient')

    def get_project_analysis_client(self) -> ProjectAnalysisClient:
        """get_project_analysis_client.
        Gets the 7.1 version of the ProjectAnalysisClient
        :rtype: :class:`<ProjectAnalysisClient> <azure.devops.v7_1.project_analysis.project_analysis_client.ProjectAnalysisClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.project_analysis.project_analysis_client.ProjectAnalysisClient')

    def get_provenance_client(self) -> ProvenanceClient:
        """get_provenance_client.
        Gets the 7.1 version of the ProvenanceClient
        :rtype: :class:`<ProvenanceClient> <azure.devops.v7_1.provenance.provenance_client.ProvenanceClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.provenance.provenance_client.ProvenanceClient')

    def get_py_pi_api_client(self) -> PyPiApiClient:
        """get_py_pi_api_client.
        Gets the 7.1 version of the PyPiApiClient
        :rtype: :class:`<PyPiApiClient> <azure.devops.v7_1.py_pi_api.py_pi_api_client.PyPiApiClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.py_pi_api.py_pi_api_client.PyPiApiClient')

    def get_release_client(self) -> ReleaseClient:
        """get_release_client.
        Gets the 7.1 version of the ReleaseClient
        :rtype: :class:`<ReleaseClient> <azure.devops.v7_1.release.release_client.ReleaseClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.release.release_client.ReleaseClient')

    def get_sbom_client(self) -> SBOMClient:
        """get_sbom_client.
        Gets the 7.1 version of the SBOMClient
        :rtype: :class:`<SBOMClient> <azure.devops.v7_1.sbom.sbom_client.SBOMClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.sbom.sbom_client.SBOMClient')

    def get_search_client(self) -> SearchClient:
        """get_search_client.
        Gets the 7.1 version of the SearchClient
        :rtype: :class:`<SearchClient> <azure.devops.v7_1.search.search_client.SearchClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.search.search_client.SearchClient')

    def get_security_client(self) -> SecurityClient:
        """get_security_client.
        Gets the 7.1 version of the SecurityClient
        :rtype: :class:`<SecurityClient> <azure.devops.v7_1.security.security_client.SecurityClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.security.security_client.SecurityClient')

    def get_service_endpoint_client(self) -> ServiceEndpointClient:
        """get_service_endpoint_client.
        Gets the 7.1 version of the ServiceEndpointClient
        :rtype: :class:`<ServiceEndpointClient> <azure.devops.v7_1.service_endpoint.service_endpoint_client.ServiceEndpointClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.service_endpoint.service_endpoint_client.ServiceEndpointClient')

    def get_service_hooks_client(self) -> ServiceHooksClient:
        """get_service_hooks_client.
        Gets the 7.1 version of the ServiceHooksClient
        :rtype: :class:`<ServiceHooksClient> <azure.devops.v7_1.service_hooks.service_hooks_client.ServiceHooksClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.service_hooks.service_hooks_client.ServiceHooksClient')

    def get_settings_client(self) -> SettingsClient:
        """get_settings_client.
        Gets the 7.1 version of the SettingsClient
        :rtype: :class:`<SettingsClient> <azure.devops.v7_1.settings.settings_client.SettingsClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.settings.settings_client.SettingsClient')

    def get_symbol_client(self) -> SymbolClient:
        """get_symbol_client.
        Gets the 7.1 version of the SymbolClient
        :rtype: :class:`<SymbolClient> <azure.devops.v7_1.symbol.symbol_client.SymbolClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.symbol.symbol_client.SymbolClient')

    def get_task_client(self) -> TaskClient:
        """get_task_client.
        Gets the 7.1 version of the TaskClient
        :rtype: :class:`<TaskClient> <azure.devops.v7_1.task.task_client.TaskClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.task.task_client.TaskClient')

    def get_task_agent_client(self) -> TaskAgentClient:
        """get_task_agent_client.
        Gets the 7.1 version of the TaskAgentClient
        :rtype: :class:`<TaskAgentClient> <azure.devops.v7_1.task_agent.task_agent_client.TaskAgentClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.task_agent.task_agent_client.TaskAgentClient')

    def get_test_client(self) -> TestClient:
        """get_test_client.
        Gets the 7.1 version of the TestClient
        :rtype: :class:`<TestClient> <azure.devops.v7_1.test.test_client.TestClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.test.test_client.TestClient')

    def get_test_plan_client(self) -> TestPlanClient:
        """get_test_plan_client.
        Gets the 7.1 version of the TestPlanClient
        :rtype: :class:`<TestPlanClient> <azure.devops.v7_1.test_plan.test_plan_client.TestPlanClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.test_plan.test_plan_client.TestPlanClient')

    def get_test_results_client(self) -> TestResultsClient:
        """get_test_results_client.
        Gets the 7.1 version of the TestResultsClient
        :rtype: :class:`<TestResultsClient> <azure.devops.v7_1.test_results.test_results_client.TestResultsClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.test_results.test_results_client.TestResultsClient')

    def get_tfvc_client(self) -> TfvcClient:
        """get_tfvc_client.
        Gets the 7.1 version of the TfvcClient
        :rtype: :class:`<TfvcClient> <azure.devops.v7_1.tfvc.tfvc_client.TfvcClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.tfvc.tfvc_client.TfvcClient')

    def get_token_admin_client(self) -> TokenAdminClient:
        """get_token_admin_client.
        Gets the 7.1 version of the TokenAdminClient
        :rtype: :class:`<TokenAdminClient> <azure.devops.v7_1.token_admin.token_admin_client.TokenAdminClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.token_admin.token_admin_client.TokenAdminClient')

    def get_upack_api_client(self) -> UPackApiClient:
        """get_upack_api_client.
        Gets the 7.1 version of the UPackApiClient
        :rtype: :class:`<UPackApiClient> <azure.devops.v7_1.upack_api.upack_api_client.UPackApiClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.upack_api.upack_api_client.UPackApiClient')

    def get_upack_packaging_client(self) -> UPackPackagingClient:
        """get_upack_packaging_client.
        Gets the 7.1 version of the UPackPackagingClient
        :rtype: :class:`<UPackPackagingClient> <azure.devops.v7_1.upack_packaging.upack_packaging_client.UPackPackagingClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.upack_packaging.upack_packaging_client.UPackPackagingClient')

    def get_wiki_client(self) -> WikiClient:
        """get_wiki_client.
        Gets the 7.1 version of the WikiClient
        :rtype: :class:`<WikiClient> <azure.devops.v7_1.wiki.wiki_client.WikiClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.wiki.wiki_client.WikiClient')

    def get_work_client(self) -> WorkClient:
        """get_work_client.
        Gets the 7.1 version of the WorkClient
        :rtype: :class:`<WorkClient> <azure.devops.v7_1.work.work_client.WorkClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.work.work_client.WorkClient')

    def get_work_item_tracking_client(self) -> WorkItemTrackingClient:
        """get_work_item_tracking_client.
        Gets the 7.1 version of the WorkItemTrackingClient
        :rtype: :class:`<WorkItemTrackingClient> <azure.devops.v7_1.work_item_tracking.work_item_tracking_client.WorkItemTrackingClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.work_item_tracking.work_item_tracking_client.WorkItemTrackingClient')

    def get_work_item_tracking_process_client(self) -> WorkItemTrackingProcessClient:
        """get_work_item_tracking_process_client.
        Gets the 7.1 version of the WorkItemTrackingProcessClient
        :rtype: :class:`<WorkItemTrackingProcessClient> <azure.devops.v7_1.work_item_tracking_process.work_item_tracking_process_client.WorkItemTrackingProcessClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.work_item_tracking_process.work_item_tracking_process_client.WorkItemTrackingProcessClient')

    def get_work_item_tracking_process_template_client(self) -> WorkItemTrackingProcessTemplateClient:
        """get_work_item_tracking_process_template_client.
        Gets the 7.1 version of the WorkItemTrackingProcessTemplateClient
        :rtype: :class:`<WorkItemTrackingProcessTemplateClient> <azure.devops.v7_1.work_item_tracking_process_template.work_item_tracking_process_template_client.WorkItemTrackingProcessTemplateClient>`
        """
        return self._connection.get_client('azure.devops.v7_1.work_item_tracking_process_template.work_item_tracking_process_template_client.WorkItemTrackingProcessTemplateClient')
