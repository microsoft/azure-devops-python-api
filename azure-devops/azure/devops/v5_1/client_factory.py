# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------


class ClientFactoryV5_1(object):
    """ClientFactoryV5_1.
    """

    def __init__(self, connection):
        self._connection = connection

    def get_build_client(self):
        """get_build_client.
        Gets the 5.1 version of the BuildClient
        :rtype: :class:`<BuildClient> <azure.devops.v5_1.build.build_client.BuildClient>`
        """
        return self._connection.get_client('azure.devops.v5_1.build.build_client.BuildClient')

    def get_client_trace_client(self):
        """get_client_trace_client.
        Gets the 5.1 version of the ClientTraceClient
        :rtype: :class:`<ClientTraceClient> <azure.devops.v5_1.client_trace.client_trace_client.ClientTraceClient>`
        """
        return self._connection.get_client('azure.devops.v5_1.client_trace.client_trace_client.ClientTraceClient')

    def get_cloud_load_test_client(self):
        """get_cloud_load_test_client.
        Gets the 5.1 version of the CloudLoadTestClient
        :rtype: :class:`<CloudLoadTestClient> <azure.devops.v5_1.cloud_load_test.cloud_load_test_client.CloudLoadTestClient>`
        """
        return self._connection.get_client('azure.devops.v5_1.cloud_load_test.cloud_load_test_client.CloudLoadTestClient')

    def get_feature_availability_client(self):
        """get_feature_availability_client.
        Gets the 5.1 version of the FeatureAvailabilityClient
        :rtype: :class:`<FeatureAvailabilityClient> <azure.devops.v5_1.feature_availability.feature_availability_client.FeatureAvailabilityClient>`
        """
        return self._connection.get_client('azure.devops.v5_1.feature_availability.feature_availability_client.FeatureAvailabilityClient')

    def get_file_container_client(self):
        """get_file_container_client.
        Gets the 5.1 version of the FileContainerClient
        :rtype: :class:`<FileContainerClient> <azure.devops.v5_1.file_container.file_container_client.FileContainerClient>`
        """
        return self._connection.get_client('azure.devops.v5_1.file_container.file_container_client.FileContainerClient')

    def get_git_client(self):
        """get_git_client.
        Gets the 5.1 version of the GitClient
        :rtype: :class:`<GitClient> <azure.devops.v5_1.git.git_client.GitClient>`
        """
        return self._connection.get_client('azure.devops.v5_1.git.git_client.GitClient')

    def get_graph_client(self):
        """get_graph_client.
        Gets the 5.1 version of the GraphClient
        :rtype: :class:`<GraphClient> <azure.devops.v5_1.graph.graph_client.GraphClient>`
        """
        return self._connection.get_client('azure.devops.v5_1.graph.graph_client.GraphClient')

    def get_identity_client(self):
        """get_identity_client.
        Gets the 5.1 version of the IdentityClient
        :rtype: :class:`<IdentityClient> <azure.devops.v5_1.identity.identity_client.IdentityClient>`
        """
        return self._connection.get_client('azure.devops.v5_1.identity.identity_client.IdentityClient')

    def get_location_client(self):
        """get_location_client.
        Gets the 5.1 version of the LocationClient
        :rtype: :class:`<LocationClient> <azure.devops.v5_1.location.location_client.LocationClient>`
        """
        return self._connection.get_client('azure.devops.v5_1.location.location_client.LocationClient')

    def get_notification_client(self):
        """get_notification_client.
        Gets the 5.1 version of the NotificationClient
        :rtype: :class:`<NotificationClient> <azure.devops.v5_1.notification.notification_client.NotificationClient>`
        """
        return self._connection.get_client('azure.devops.v5_1.notification.notification_client.NotificationClient')

    def get_npm_client(self):
        """get_npm_client.
        Gets the 5.1 version of the NpmClient
        :rtype: :class:`<NpmClient> <azure.devops.v5_1.npm.npm_client.NpmClient>`
        """
        return self._connection.get_client('azure.devops.v5_1.npm.npm_client.NpmClient')

    def get_nuGet_client(self):
        """get_nuGet_client.
        Gets the 5.1 version of the NuGetClient
        :rtype: :class:`<NuGetClient> <azure.devops.v5_1.nuGet.nuGet_client.NuGetClient>`
        """
        return self._connection.get_client('azure.devops.v5_1.nuGet.nuGet_client.NuGetClient')

    def get_operations_client(self):
        """get_operations_client.
        Gets the 5.1 version of the OperationsClient
        :rtype: :class:`<OperationsClient> <azure.devops.v5_1.operations.operations_client.OperationsClient>`
        """
        return self._connection.get_client('azure.devops.v5_1.operations.operations_client.OperationsClient')

    def get_policy_client(self):
        """get_policy_client.
        Gets the 5.1 version of the PolicyClient
        :rtype: :class:`<PolicyClient> <azure.devops.v5_1.policy.policy_client.PolicyClient>`
        """
        return self._connection.get_client('azure.devops.v5_1.policy.policy_client.PolicyClient')

    def get_profile_client(self):
        """get_profile_client.
        Gets the 5.1 version of the ProfileClient
        :rtype: :class:`<ProfileClient> <azure.devops.v5_1.profile.profile_client.ProfileClient>`
        """
        return self._connection.get_client('azure.devops.v5_1.profile.profile_client.ProfileClient')

    def get_project_analysis_client(self):
        """get_project_analysis_client.
        Gets the 5.1 version of the ProjectAnalysisClient
        :rtype: :class:`<ProjectAnalysisClient> <azure.devops.v5_1.project_analysis.project_analysis_client.ProjectAnalysisClient>`
        """
        return self._connection.get_client('azure.devops.v5_1.project_analysis.project_analysis_client.ProjectAnalysisClient')

    def get_provenance_client(self):
        """get_provenance_client.
        Gets the 5.1 version of the ProvenanceClient
        :rtype: :class:`<ProvenanceClient> <azure.devops.v5_1.provenance.provenance_client.ProvenanceClient>`
        """
        return self._connection.get_client('azure.devops.v5_1.provenance.provenance_client.ProvenanceClient')

    def get_py_pi_api_client(self):
        """get_py_pi_api_client.
        Gets the 5.1 version of the PyPiApiClient
        :rtype: :class:`<PyPiApiClient> <azure.devops.v5_1.py_pi_api.py_pi_api_client.PyPiApiClient>`
        """
        return self._connection.get_client('azure.devops.v5_1.py_pi_api.py_pi_api_client.PyPiApiClient')

    def get_release_client(self):
        """get_release_client.
        Gets the 5.1 version of the ReleaseClient
        :rtype: :class:`<ReleaseClient> <azure.devops.v5_1.release.release_client.ReleaseClient>`
        """
        return self._connection.get_client('azure.devops.v5_1.release.release_client.ReleaseClient')

    def get_security_client(self):
        """get_security_client.
        Gets the 5.1 version of the SecurityClient
        :rtype: :class:`<SecurityClient> <azure.devops.v5_1.security.security_client.SecurityClient>`
        """
        return self._connection.get_client('azure.devops.v5_1.security.security_client.SecurityClient')

    def get_service_endpoint_client(self):
        """get_service_endpoint_client.
        Gets the 5.1 version of the ServiceEndpointClient
        :rtype: :class:`<ServiceEndpointClient> <azure.devops.v5_1.service_endpoint.service_endpoint_client.ServiceEndpointClient>`
        """
        return self._connection.get_client('azure.devops.v5_1.service_endpoint.service_endpoint_client.ServiceEndpointClient')

    def get_service_hooks_client(self):
        """get_service_hooks_client.
        Gets the 5.1 version of the ServiceHooksClient
        :rtype: :class:`<ServiceHooksClient> <azure.devops.v5_1.service_hooks.service_hooks_client.ServiceHooksClient>`
        """
        return self._connection.get_client('azure.devops.v5_1.service_hooks.service_hooks_client.ServiceHooksClient')

    def get_settings_client(self):
        """get_settings_client.
        Gets the 5.1 version of the SettingsClient
        :rtype: :class:`<SettingsClient> <azure.devops.v5_1.settings.settings_client.SettingsClient>`
        """
        return self._connection.get_client('azure.devops.v5_1.settings.settings_client.SettingsClient')

    def get_symbol_client(self):
        """get_symbol_client.
        Gets the 5.1 version of the SymbolClient
        :rtype: :class:`<SymbolClient> <azure.devops.v5_1.symbol.symbol_client.SymbolClient>`
        """
        return self._connection.get_client('azure.devops.v5_1.symbol.symbol_client.SymbolClient')

    def get_task_client(self):
        """get_task_client.
        Gets the 5.1 version of the TaskClient
        :rtype: :class:`<TaskClient> <azure.devops.v5_1.task.task_client.TaskClient>`
        """
        return self._connection.get_client('azure.devops.v5_1.task.task_client.TaskClient')

    def get_task_agent_client(self):
        """get_task_agent_client.
        Gets the 5.1 version of the TaskAgentClient
        :rtype: :class:`<TaskAgentClient> <azure.devops.v5_1.task_agent.task_agent_client.TaskAgentClient>`
        """
        return self._connection.get_client('azure.devops.v5_1.task_agent.task_agent_client.TaskAgentClient')

    def get_test_client(self):
        """get_test_client.
        Gets the 5.1 version of the TestClient
        :rtype: :class:`<TestClient> <azure.devops.v5_1.test.test_client.TestClient>`
        """
        return self._connection.get_client('azure.devops.v5_1.test.test_client.TestClient')

    def get_tfvc_client(self):
        """get_tfvc_client.
        Gets the 5.1 version of the TfvcClient
        :rtype: :class:`<TfvcClient> <azure.devops.v5_1.tfvc.tfvc_client.TfvcClient>`
        """
        return self._connection.get_client('azure.devops.v5_1.tfvc.tfvc_client.TfvcClient')

    def get_uPack_api_client(self):
        """get_uPack_api_client.
        Gets the 5.1 version of the UPackApiClient
        :rtype: :class:`<UPackApiClient> <azure.devops.v5_1.uPack_api.uPack_api_client.UPackApiClient>`
        """
        return self._connection.get_client('azure.devops.v5_1.uPack_api.uPack_api_client.UPackApiClient')

    def get_uPack_packaging_client(self):
        """get_uPack_packaging_client.
        Gets the 5.1 version of the UPackPackagingClient
        :rtype: :class:`<UPackPackagingClient> <azure.devops.v5_1.uPack_packaging.uPack_packaging_client.UPackPackagingClient>`
        """
        return self._connection.get_client('azure.devops.v5_1.uPack_packaging.uPack_packaging_client.UPackPackagingClient')

    def get_wiki_client(self):
        """get_wiki_client.
        Gets the 5.1 version of the WikiClient
        :rtype: :class:`<WikiClient> <azure.devops.v5_1.wiki.wiki_client.WikiClient>`
        """
        return self._connection.get_client('azure.devops.v5_1.wiki.wiki_client.WikiClient')

    def get_work_client(self):
        """get_work_client.
        Gets the 5.1 version of the WorkClient
        :rtype: :class:`<WorkClient> <azure.devops.v5_1.work.work_client.WorkClient>`
        """
        return self._connection.get_client('azure.devops.v5_1.work.work_client.WorkClient')

    def get_work_item_tracking_client(self):
        """get_work_item_tracking_client.
        Gets the 5.1 version of the WorkItemTrackingClient
        :rtype: :class:`<WorkItemTrackingClient> <azure.devops.v5_1.work_item_tracking.work_item_tracking_client.WorkItemTrackingClient>`
        """
        return self._connection.get_client('azure.devops.v5_1.work_item_tracking.work_item_tracking_client.WorkItemTrackingClient')

    def get_work_item_tracking_client(self):
        """get_work_item_tracking_client.
        Gets the 5.1 version of the WorkItemTrackingClient
        :rtype: :class:`<WorkItemTrackingClient> <azure.devops.v5_1.work_item_tracking.work_item_tracking_client.WorkItemTrackingClient>`
        """
        return self._connection.get_client('azure.devops.v5_1.work_item_tracking.work_item_tracking_client.WorkItemTrackingClient')

    def get_work_item_tracking_comments_client(self):
        """get_work_item_tracking_comments_client.
        Gets the 5.1 version of the WorkItemTrackingCommentsClient
        :rtype: :class:`<WorkItemTrackingCommentsClient> <azure.devops.v5_1.work_item_tracking_comments.work_item_tracking_comments_client.WorkItemTrackingCommentsClient>`
        """
        return self._connection.get_client('azure.devops.v5_1.work_item_tracking_comments.work_item_tracking_comments_client.WorkItemTrackingCommentsClient')

    def get_work_item_tracking_process_template_client(self):
        """get_work_item_tracking_process_template_client.
        Gets the 5.1 version of the WorkItemTrackingProcessTemplateClient
        :rtype: :class:`<WorkItemTrackingProcessTemplateClient> <azure.devops.v5_1.work_item_tracking_process_template.work_item_tracking_process_template_client.WorkItemTrackingProcessTemplateClient>`
        """
        return self._connection.get_client('azure.devops.v5_1.work_item_tracking_process_template.work_item_tracking_process_template_client.WorkItemTrackingProcessTemplateClient')

