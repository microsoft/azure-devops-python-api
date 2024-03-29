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


class GalleryClient(Client):
    """Gallery
    :param str base_url: Service URL
    :param Authentication creds: Authenticated credentials.
    """

    def __init__(self, base_url=None, creds=None):
        super(GalleryClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = '69d21c00-f135-441b-b5ce-3626378e0819'

    def share_extension_by_id(self, extension_id, account_name):
        """ShareExtensionById.
        [Preview API]
        :param str extension_id:
        :param str account_name:
        """
        route_values = {}
        if extension_id is not None:
            route_values['extensionId'] = self._serialize.url('extension_id', extension_id, 'str')
        if account_name is not None:
            route_values['accountName'] = self._serialize.url('account_name', account_name, 'str')
        self._send(http_method='POST',
                   location_id='1f19631b-a0b4-4a03-89c2-d79785d24360',
                   version='7.1-preview.1',
                   route_values=route_values)

    def unshare_extension_by_id(self, extension_id, account_name):
        """UnshareExtensionById.
        [Preview API]
        :param str extension_id:
        :param str account_name:
        """
        route_values = {}
        if extension_id is not None:
            route_values['extensionId'] = self._serialize.url('extension_id', extension_id, 'str')
        if account_name is not None:
            route_values['accountName'] = self._serialize.url('account_name', account_name, 'str')
        self._send(http_method='DELETE',
                   location_id='1f19631b-a0b4-4a03-89c2-d79785d24360',
                   version='7.1-preview.1',
                   route_values=route_values)

    def share_extension(self, publisher_name, extension_name, account_name):
        """ShareExtension.
        [Preview API]
        :param str publisher_name:
        :param str extension_name:
        :param str account_name:
        """
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        if account_name is not None:
            route_values['accountName'] = self._serialize.url('account_name', account_name, 'str')
        self._send(http_method='POST',
                   location_id='a1e66d8f-f5de-4d16-8309-91a4e015ee46',
                   version='7.1-preview.1',
                   route_values=route_values)

    def unshare_extension(self, publisher_name, extension_name, account_name):
        """UnshareExtension.
        [Preview API]
        :param str publisher_name:
        :param str extension_name:
        :param str account_name:
        """
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        if account_name is not None:
            route_values['accountName'] = self._serialize.url('account_name', account_name, 'str')
        self._send(http_method='DELETE',
                   location_id='a1e66d8f-f5de-4d16-8309-91a4e015ee46',
                   version='7.1-preview.1',
                   route_values=route_values)

    def get_acquisition_options(self, item_id, installation_target, test_commerce=None, is_free_or_trial_install=None):
        """GetAcquisitionOptions.
        [Preview API]
        :param str item_id:
        :param str installation_target:
        :param bool test_commerce:
        :param bool is_free_or_trial_install:
        :rtype: :class:`<AcquisitionOptions> <azure.devops.v7_1.gallery.models.AcquisitionOptions>`
        """
        route_values = {}
        if item_id is not None:
            route_values['itemId'] = self._serialize.url('item_id', item_id, 'str')
        query_parameters = {}
        if installation_target is not None:
            query_parameters['installationTarget'] = self._serialize.query('installation_target', installation_target, 'str')
        if test_commerce is not None:
            query_parameters['testCommerce'] = self._serialize.query('test_commerce', test_commerce, 'bool')
        if is_free_or_trial_install is not None:
            query_parameters['isFreeOrTrialInstall'] = self._serialize.query('is_free_or_trial_install', is_free_or_trial_install, 'bool')
        response = self._send(http_method='GET',
                              location_id='9d0a0105-075e-4760-aa15-8bcf54d1bd7d',
                              version='7.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('AcquisitionOptions', response)

    def request_acquisition(self, acquisition_request):
        """RequestAcquisition.
        [Preview API]
        :param :class:`<ExtensionAcquisitionRequest> <azure.devops.v7_1.gallery.models.ExtensionAcquisitionRequest>` acquisition_request:
        :rtype: :class:`<ExtensionAcquisitionRequest> <azure.devops.v7_1.gallery.models.ExtensionAcquisitionRequest>`
        """
        content = self._serialize.body(acquisition_request, 'ExtensionAcquisitionRequest')
        response = self._send(http_method='POST',
                              location_id='3adb1f2d-e328-446e-be73-9f6d98071c45',
                              version='7.1-preview.1',
                              content=content)
        return self._deserialize('ExtensionAcquisitionRequest', response)

    def get_asset_by_name(self, publisher_name, extension_name, version, asset_type, account_token=None, accept_default=None, account_token_header=None, **kwargs):
        """GetAssetByName.
        [Preview API]
        :param str publisher_name:
        :param str extension_name:
        :param str version:
        :param str asset_type:
        :param str account_token:
        :param bool accept_default:
        :param String account_token_header: Header to pass the account token
        :rtype: object
        """
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        if version is not None:
            route_values['version'] = self._serialize.url('version', version, 'str')
        if asset_type is not None:
            route_values['assetType'] = self._serialize.url('asset_type', asset_type, 'str')
        query_parameters = {}
        if account_token is not None:
            query_parameters['accountToken'] = self._serialize.query('account_token', account_token, 'str')
        if accept_default is not None:
            query_parameters['acceptDefault'] = self._serialize.query('accept_default', accept_default, 'bool')
        additional_headers = {}
        if account_token_header is not None:
            additional_headers['X-Market-AccountToken'] = account_token_header
        response = self._send(http_method='GET',
                              location_id='7529171f-a002-4180-93ba-685f358a0482',
                              version='7.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              additional_headers=additional_headers,
                              accept_media_type='application/octet-stream')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_asset(self, extension_id, version, asset_type, account_token=None, accept_default=None, account_token_header=None, **kwargs):
        """GetAsset.
        [Preview API]
        :param str extension_id:
        :param str version:
        :param str asset_type:
        :param str account_token:
        :param bool accept_default:
        :param String account_token_header: Header to pass the account token
        :rtype: object
        """
        route_values = {}
        if extension_id is not None:
            route_values['extensionId'] = self._serialize.url('extension_id', extension_id, 'str')
        if version is not None:
            route_values['version'] = self._serialize.url('version', version, 'str')
        if asset_type is not None:
            route_values['assetType'] = self._serialize.url('asset_type', asset_type, 'str')
        query_parameters = {}
        if account_token is not None:
            query_parameters['accountToken'] = self._serialize.query('account_token', account_token, 'str')
        if accept_default is not None:
            query_parameters['acceptDefault'] = self._serialize.query('accept_default', accept_default, 'bool')
        additional_headers = {}
        if account_token_header is not None:
            additional_headers['X-Market-AccountToken'] = account_token_header
        response = self._send(http_method='GET',
                              location_id='5d545f3d-ef47-488b-8be3-f5ee1517856c',
                              version='7.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              additional_headers=additional_headers,
                              accept_media_type='application/octet-stream')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_asset_authenticated(self, publisher_name, extension_name, version, asset_type, account_token=None, account_token_header=None, **kwargs):
        """GetAssetAuthenticated.
        [Preview API]
        :param str publisher_name:
        :param str extension_name:
        :param str version:
        :param str asset_type:
        :param str account_token:
        :param String account_token_header: Header to pass the account token
        :rtype: object
        """
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        if version is not None:
            route_values['version'] = self._serialize.url('version', version, 'str')
        if asset_type is not None:
            route_values['assetType'] = self._serialize.url('asset_type', asset_type, 'str')
        query_parameters = {}
        if account_token is not None:
            query_parameters['accountToken'] = self._serialize.query('account_token', account_token, 'str')
        additional_headers = {}
        if account_token_header is not None:
            additional_headers['X-Market-AccountToken'] = account_token_header
        response = self._send(http_method='GET',
                              location_id='506aff36-2622-4f70-8063-77cce6366d20',
                              version='7.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              additional_headers=additional_headers,
                              accept_media_type='application/octet-stream')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def associate_azure_publisher(self, publisher_name, azure_publisher_id):
        """AssociateAzurePublisher.
        [Preview API]
        :param str publisher_name:
        :param str azure_publisher_id:
        :rtype: :class:`<AzurePublisher> <azure.devops.v7_1.gallery.models.AzurePublisher>`
        """
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        query_parameters = {}
        if azure_publisher_id is not None:
            query_parameters['azurePublisherId'] = self._serialize.query('azure_publisher_id', azure_publisher_id, 'str')
        response = self._send(http_method='PUT',
                              location_id='efd202a6-9d87-4ebc-9229-d2b8ae2fdb6d',
                              version='7.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('AzurePublisher', response)

    def query_associated_azure_publisher(self, publisher_name):
        """QueryAssociatedAzurePublisher.
        [Preview API]
        :param str publisher_name:
        :rtype: :class:`<AzurePublisher> <azure.devops.v7_1.gallery.models.AzurePublisher>`
        """
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        response = self._send(http_method='GET',
                              location_id='efd202a6-9d87-4ebc-9229-d2b8ae2fdb6d',
                              version='7.1-preview.1',
                              route_values=route_values)
        return self._deserialize('AzurePublisher', response)

    def get_categories(self, languages=None):
        """GetCategories.
        [Preview API]
        :param str languages:
        :rtype: [str]
        """
        query_parameters = {}
        if languages is not None:
            query_parameters['languages'] = self._serialize.query('languages', languages, 'str')
        response = self._send(http_method='GET',
                              location_id='e0a5a71e-3ac3-43a0-ae7d-0bb5c3046a2a',
                              version='7.1-preview.1',
                              query_parameters=query_parameters)
        return self._deserialize('[str]', self._unwrap_collection(response))

    def get_category_details(self, category_name, languages=None, product=None):
        """GetCategoryDetails.
        [Preview API]
        :param str category_name:
        :param str languages:
        :param str product:
        :rtype: :class:`<CategoriesResult> <azure.devops.v7_1.gallery.models.CategoriesResult>`
        """
        route_values = {}
        if category_name is not None:
            route_values['categoryName'] = self._serialize.url('category_name', category_name, 'str')
        query_parameters = {}
        if languages is not None:
            query_parameters['languages'] = self._serialize.query('languages', languages, 'str')
        if product is not None:
            query_parameters['product'] = self._serialize.query('product', product, 'str')
        response = self._send(http_method='GET',
                              location_id='75d3c04d-84d2-4973-acd2-22627587dabc',
                              version='7.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('CategoriesResult', response)

    def get_category_tree(self, product, category_id, lcid=None, source=None, product_version=None, skus=None, sub_skus=None, product_architecture=None):
        """GetCategoryTree.
        [Preview API]
        :param str product:
        :param str category_id:
        :param int lcid:
        :param str source:
        :param str product_version:
        :param str skus:
        :param str sub_skus:
        :param str product_architecture:
        :rtype: :class:`<ProductCategory> <azure.devops.v7_1.gallery.models.ProductCategory>`
        """
        route_values = {}
        if product is not None:
            route_values['product'] = self._serialize.url('product', product, 'str')
        if category_id is not None:
            route_values['categoryId'] = self._serialize.url('category_id', category_id, 'str')
        query_parameters = {}
        if lcid is not None:
            query_parameters['lcid'] = self._serialize.query('lcid', lcid, 'int')
        if source is not None:
            query_parameters['source'] = self._serialize.query('source', source, 'str')
        if product_version is not None:
            query_parameters['productVersion'] = self._serialize.query('product_version', product_version, 'str')
        if skus is not None:
            query_parameters['skus'] = self._serialize.query('skus', skus, 'str')
        if sub_skus is not None:
            query_parameters['subSkus'] = self._serialize.query('sub_skus', sub_skus, 'str')
        if product_architecture is not None:
            query_parameters['productArchitecture'] = self._serialize.query('product_architecture', product_architecture, 'str')
        response = self._send(http_method='GET',
                              location_id='1102bb42-82b0-4955-8d8a-435d6b4cedd3',
                              version='7.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('ProductCategory', response)

    def get_root_categories(self, product, lcid=None, source=None, product_version=None, skus=None, sub_skus=None):
        """GetRootCategories.
        [Preview API]
        :param str product:
        :param int lcid:
        :param str source:
        :param str product_version:
        :param str skus:
        :param str sub_skus:
        :rtype: :class:`<ProductCategoriesResult> <azure.devops.v7_1.gallery.models.ProductCategoriesResult>`
        """
        route_values = {}
        if product is not None:
            route_values['product'] = self._serialize.url('product', product, 'str')
        query_parameters = {}
        if lcid is not None:
            query_parameters['lcid'] = self._serialize.query('lcid', lcid, 'int')
        if source is not None:
            query_parameters['source'] = self._serialize.query('source', source, 'str')
        if product_version is not None:
            query_parameters['productVersion'] = self._serialize.query('product_version', product_version, 'str')
        if skus is not None:
            query_parameters['skus'] = self._serialize.query('skus', skus, 'str')
        if sub_skus is not None:
            query_parameters['subSkus'] = self._serialize.query('sub_skus', sub_skus, 'str')
        response = self._send(http_method='GET',
                              location_id='31fba831-35b2-46f6-a641-d05de5a877d8',
                              version='7.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('ProductCategoriesResult', response)

    def get_certificate(self, publisher_name, extension_name, version=None, **kwargs):
        """GetCertificate.
        [Preview API]
        :param str publisher_name:
        :param str extension_name:
        :param str version:
        :rtype: object
        """
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        if version is not None:
            route_values['version'] = self._serialize.url('version', version, 'str')
        response = self._send(http_method='GET',
                              location_id='e905ad6a-3f1f-4d08-9f6d-7d357ff8b7d0',
                              version='7.1-preview.1',
                              route_values=route_values,
                              accept_media_type='application/octet-stream')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_content_verification_log(self, publisher_name, extension_name, **kwargs):
        """GetContentVerificationLog.
        [Preview API]
        :param str publisher_name:
        :param str extension_name:
        :rtype: object
        """
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        response = self._send(http_method='GET',
                              location_id='c0f1c7c4-3557-4ffb-b774-1e48c4865e99',
                              version='7.1-preview.1',
                              route_values=route_values,
                              accept_media_type='application/octet-stream')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def create_support_request(self, customer_support_request):
        """CreateSupportRequest.
        [Preview API]
        :param :class:`<CustomerSupportRequest> <azure.devops.v7_1.gallery.models.CustomerSupportRequest>` customer_support_request:
        """
        content = self._serialize.body(customer_support_request, 'CustomerSupportRequest')
        self._send(http_method='POST',
                   location_id='8eded385-026a-4c15-b810-b8eb402771f1',
                   version='7.1-preview.1',
                   content=content)

    def create_draft_for_edit_extension(self, publisher_name, extension_name):
        """CreateDraftForEditExtension.
        [Preview API]
        :param str publisher_name:
        :param str extension_name:
        :rtype: :class:`<ExtensionDraft> <azure.devops.v7_1.gallery.models.ExtensionDraft>`
        """
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        response = self._send(http_method='POST',
                              location_id='02b33873-4e61-496e-83a2-59d1df46b7d8',
                              version='7.1-preview.1',
                              route_values=route_values)
        return self._deserialize('ExtensionDraft', response)

    def perform_edit_extension_draft_operation(self, draft_patch, publisher_name, extension_name, draft_id):
        """PerformEditExtensionDraftOperation.
        [Preview API]
        :param :class:`<ExtensionDraftPatch> <azure.devops.v7_1.gallery.models.ExtensionDraftPatch>` draft_patch:
        :param str publisher_name:
        :param str extension_name:
        :param str draft_id:
        :rtype: :class:`<ExtensionDraft> <azure.devops.v7_1.gallery.models.ExtensionDraft>`
        """
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        if draft_id is not None:
            route_values['draftId'] = self._serialize.url('draft_id', draft_id, 'str')
        content = self._serialize.body(draft_patch, 'ExtensionDraftPatch')
        response = self._send(http_method='PATCH',
                              location_id='02b33873-4e61-496e-83a2-59d1df46b7d8',
                              version='7.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('ExtensionDraft', response)

    def update_payload_in_draft_for_edit_extension(self, upload_stream, publisher_name, extension_name, draft_id, file_name=None, **kwargs):
        """UpdatePayloadInDraftForEditExtension.
        [Preview API]
        :param object upload_stream: Stream to upload
        :param str publisher_name:
        :param str extension_name:
        :param str draft_id:
        :param String file_name: Header to pass the filename of the uploaded data
        :rtype: :class:`<ExtensionDraft> <azure.devops.v7_1.gallery.models.ExtensionDraft>`
        """
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        if draft_id is not None:
            route_values['draftId'] = self._serialize.url('draft_id', draft_id, 'str')
        additional_headers = {}
        if file_name is not None:
            additional_headers['X-Market-UploadFileName'] = file_name
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        content = self._client.stream_upload(upload_stream, callback=callback)
        response = self._send(http_method='PUT',
                              location_id='02b33873-4e61-496e-83a2-59d1df46b7d8',
                              version='7.1-preview.1',
                              route_values=route_values,
                              additional_headers=additional_headers,
                              content=content,
                              media_type='application/octet-stream')
        return self._deserialize('ExtensionDraft', response)

    def add_asset_for_edit_extension_draft(self, upload_stream, publisher_name, extension_name, draft_id, asset_type, **kwargs):
        """AddAssetForEditExtensionDraft.
        [Preview API]
        :param object upload_stream: Stream to upload
        :param str publisher_name:
        :param str extension_name:
        :param str draft_id:
        :param str asset_type:
        :rtype: :class:`<ExtensionDraftAsset> <azure.devops.v7_1.gallery.models.ExtensionDraftAsset>`
        """
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        if draft_id is not None:
            route_values['draftId'] = self._serialize.url('draft_id', draft_id, 'str')
        if asset_type is not None:
            route_values['assetType'] = self._serialize.url('asset_type', asset_type, 'str')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        content = self._client.stream_upload(upload_stream, callback=callback)
        response = self._send(http_method='PUT',
                              location_id='f1db9c47-6619-4998-a7e5-d7f9f41a4617',
                              version='7.1-preview.1',
                              route_values=route_values,
                              content=content,
                              media_type='application/octet-stream')
        return self._deserialize('ExtensionDraftAsset', response)

    def create_draft_for_new_extension(self, upload_stream, publisher_name, product, file_name=None, **kwargs):
        """CreateDraftForNewExtension.
        [Preview API]
        :param object upload_stream: Stream to upload
        :param str publisher_name:
        :param String product: Header to pass the product type of the payload file
        :param String file_name: Header to pass the filename of the uploaded data
        :rtype: :class:`<ExtensionDraft> <azure.devops.v7_1.gallery.models.ExtensionDraft>`
        """
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        additional_headers = {}
        if product is not None:
            additional_headers['X-Market-UploadFileProduct'] = product
        if file_name is not None:
            additional_headers['X-Market-UploadFileName'] = file_name
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        content = self._client.stream_upload(upload_stream, callback=callback)
        response = self._send(http_method='POST',
                              location_id='b3ab127d-ebb9-4d22-b611-4e09593c8d79',
                              version='7.1-preview.1',
                              route_values=route_values,
                              additional_headers=additional_headers,
                              content=content,
                              media_type='application/octet-stream')
        return self._deserialize('ExtensionDraft', response)

    def perform_new_extension_draft_operation(self, draft_patch, publisher_name, draft_id):
        """PerformNewExtensionDraftOperation.
        [Preview API]
        :param :class:`<ExtensionDraftPatch> <azure.devops.v7_1.gallery.models.ExtensionDraftPatch>` draft_patch:
        :param str publisher_name:
        :param str draft_id:
        :rtype: :class:`<ExtensionDraft> <azure.devops.v7_1.gallery.models.ExtensionDraft>`
        """
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if draft_id is not None:
            route_values['draftId'] = self._serialize.url('draft_id', draft_id, 'str')
        content = self._serialize.body(draft_patch, 'ExtensionDraftPatch')
        response = self._send(http_method='PATCH',
                              location_id='b3ab127d-ebb9-4d22-b611-4e09593c8d79',
                              version='7.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('ExtensionDraft', response)

    def update_payload_in_draft_for_new_extension(self, upload_stream, publisher_name, draft_id, file_name=None, **kwargs):
        """UpdatePayloadInDraftForNewExtension.
        [Preview API]
        :param object upload_stream: Stream to upload
        :param str publisher_name:
        :param str draft_id:
        :param String file_name: Header to pass the filename of the uploaded data
        :rtype: :class:`<ExtensionDraft> <azure.devops.v7_1.gallery.models.ExtensionDraft>`
        """
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if draft_id is not None:
            route_values['draftId'] = self._serialize.url('draft_id', draft_id, 'str')
        additional_headers = {}
        if file_name is not None:
            additional_headers['X-Market-UploadFileName'] = file_name
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        content = self._client.stream_upload(upload_stream, callback=callback)
        response = self._send(http_method='PUT',
                              location_id='b3ab127d-ebb9-4d22-b611-4e09593c8d79',
                              version='7.1-preview.1',
                              route_values=route_values,
                              additional_headers=additional_headers,
                              content=content,
                              media_type='application/octet-stream')
        return self._deserialize('ExtensionDraft', response)

    def add_asset_for_new_extension_draft(self, upload_stream, publisher_name, draft_id, asset_type, **kwargs):
        """AddAssetForNewExtensionDraft.
        [Preview API]
        :param object upload_stream: Stream to upload
        :param str publisher_name:
        :param str draft_id:
        :param str asset_type:
        :rtype: :class:`<ExtensionDraftAsset> <azure.devops.v7_1.gallery.models.ExtensionDraftAsset>`
        """
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if draft_id is not None:
            route_values['draftId'] = self._serialize.url('draft_id', draft_id, 'str')
        if asset_type is not None:
            route_values['assetType'] = self._serialize.url('asset_type', asset_type, 'str')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        content = self._client.stream_upload(upload_stream, callback=callback)
        response = self._send(http_method='PUT',
                              location_id='88c0b1c8-b4f1-498a-9b2a-8446ef9f32e7',
                              version='7.1-preview.1',
                              route_values=route_values,
                              content=content,
                              media_type='application/octet-stream')
        return self._deserialize('ExtensionDraftAsset', response)

    def get_asset_from_edit_extension_draft(self, publisher_name, draft_id, asset_type, extension_name, **kwargs):
        """GetAssetFromEditExtensionDraft.
        [Preview API]
        :param str publisher_name:
        :param str draft_id:
        :param str asset_type:
        :param str extension_name:
        :rtype: object
        """
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if draft_id is not None:
            route_values['draftId'] = self._serialize.url('draft_id', draft_id, 'str')
        if asset_type is not None:
            route_values['assetType'] = self._serialize.url('asset_type', asset_type, 'str')
        query_parameters = {}
        if extension_name is not None:
            query_parameters['extensionName'] = self._serialize.query('extension_name', extension_name, 'str')
        response = self._send(http_method='GET',
                              location_id='88c0b1c8-b4f1-498a-9b2a-8446ef9f32e7',
                              version='7.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='application/octet-stream')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_asset_from_new_extension_draft(self, publisher_name, draft_id, asset_type, **kwargs):
        """GetAssetFromNewExtensionDraft.
        [Preview API]
        :param str publisher_name:
        :param str draft_id:
        :param str asset_type:
        :rtype: object
        """
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if draft_id is not None:
            route_values['draftId'] = self._serialize.url('draft_id', draft_id, 'str')
        if asset_type is not None:
            route_values['assetType'] = self._serialize.url('asset_type', asset_type, 'str')
        response = self._send(http_method='GET',
                              location_id='88c0b1c8-b4f1-498a-9b2a-8446ef9f32e7',
                              version='7.1-preview.1',
                              route_values=route_values,
                              accept_media_type='application/octet-stream')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_extension_events(self, publisher_name, extension_name, count=None, after_date=None, include=None, include_property=None):
        """GetExtensionEvents.
        [Preview API] Get install/uninstall events of an extension. If both count and afterDate parameters are specified, count takes precedence.
        :param str publisher_name: Name of the publisher
        :param str extension_name: Name of the extension
        :param int count: Count of events to fetch, applies to each event type.
        :param datetime after_date: Fetch events that occurred on or after this date
        :param str include: Filter options. Supported values: install, uninstall, review, acquisition, sales. Default is to fetch all types of events
        :param str include_property: Event properties to include. Currently only 'lastContactDetails' is supported for uninstall events
        :rtype: :class:`<ExtensionEvents> <azure.devops.v7_1.gallery.models.ExtensionEvents>`
        """
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        query_parameters = {}
        if count is not None:
            query_parameters['count'] = self._serialize.query('count', count, 'int')
        if after_date is not None:
            query_parameters['afterDate'] = self._serialize.query('after_date', after_date, 'iso-8601')
        if include is not None:
            query_parameters['include'] = self._serialize.query('include', include, 'str')
        if include_property is not None:
            query_parameters['includeProperty'] = self._serialize.query('include_property', include_property, 'str')
        response = self._send(http_method='GET',
                              location_id='3d13c499-2168-4d06-bef4-14aba185dcd5',
                              version='7.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('ExtensionEvents', response)

    def publish_extension_events(self, extension_events):
        """PublishExtensionEvents.
        [Preview API] API endpoint to publish extension install/uninstall events. This is meant to be invoked by EMS only for sending us data related to install/uninstall of an extension.
        :param [ExtensionEvents] extension_events:
        """
        content = self._serialize.body(extension_events, '[ExtensionEvents]')
        self._send(http_method='POST',
                   location_id='0bf2bd3a-70e0-4d5d-8bf7-bd4a9c2ab6e7',
                   version='7.1-preview.1',
                   content=content)

    def query_extensions(self, extension_query, account_token=None, account_token_header=None):
        """QueryExtensions.
        [Preview API]
        :param :class:`<ExtensionQuery> <azure.devops.v7_1.gallery.models.ExtensionQuery>` extension_query:
        :param str account_token:
        :param String account_token_header: Header to pass the account token
        :rtype: :class:`<ExtensionQueryResult> <azure.devops.v7_1.gallery.models.ExtensionQueryResult>`
        """
        query_parameters = {}
        if account_token is not None:
            query_parameters['accountToken'] = self._serialize.query('account_token', account_token, 'str')
        additional_headers = {}
        if account_token_header is not None:
            additional_headers['X-Market-AccountToken'] = account_token_header
        content = self._serialize.body(extension_query, 'ExtensionQuery')
        response = self._send(http_method='POST',
                              location_id='eb9d5ee1-6d43-456b-b80e-8a96fbc014b6',
                              version='7.1-preview.1',
                              query_parameters=query_parameters,
                              additional_headers=additional_headers,
                              content=content)
        return self._deserialize('ExtensionQueryResult', response)

    def create_extension(self, upload_stream, extension_type=None, re_captcha_token=None, **kwargs):
        """CreateExtension.
        [Preview API]
        :param object upload_stream: Stream to upload
        :param str extension_type:
        :param str re_captcha_token:
        :rtype: :class:`<PublishedExtension> <azure.devops.v7_1.gallery.models.PublishedExtension>`
        """
        query_parameters = {}
        if extension_type is not None:
            query_parameters['extensionType'] = self._serialize.query('extension_type', extension_type, 'str')
        if re_captcha_token is not None:
            query_parameters['reCaptchaToken'] = self._serialize.query('re_captcha_token', re_captcha_token, 'str')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        content = self._client.stream_upload(upload_stream, callback=callback)
        response = self._send(http_method='POST',
                              location_id='a41192c8-9525-4b58-bc86-179fa549d80d',
                              version='7.1-preview.2',
                              query_parameters=query_parameters,
                              content=content,
                              media_type='application/octet-stream')
        return self._deserialize('PublishedExtension', response)

    def delete_extension_by_id(self, extension_id, version=None):
        """DeleteExtensionById.
        [Preview API]
        :param str extension_id:
        :param str version:
        """
        route_values = {}
        if extension_id is not None:
            route_values['extensionId'] = self._serialize.url('extension_id', extension_id, 'str')
        query_parameters = {}
        if version is not None:
            query_parameters['version'] = self._serialize.query('version', version, 'str')
        self._send(http_method='DELETE',
                   location_id='a41192c8-9525-4b58-bc86-179fa549d80d',
                   version='7.1-preview.2',
                   route_values=route_values,
                   query_parameters=query_parameters)

    def get_extension_by_id(self, extension_id, version=None, flags=None):
        """GetExtensionById.
        [Preview API]
        :param str extension_id:
        :param str version:
        :param str flags:
        :rtype: :class:`<PublishedExtension> <azure.devops.v7_1.gallery.models.PublishedExtension>`
        """
        route_values = {}
        if extension_id is not None:
            route_values['extensionId'] = self._serialize.url('extension_id', extension_id, 'str')
        query_parameters = {}
        if version is not None:
            query_parameters['version'] = self._serialize.query('version', version, 'str')
        if flags is not None:
            query_parameters['flags'] = self._serialize.query('flags', flags, 'str')
        response = self._send(http_method='GET',
                              location_id='a41192c8-9525-4b58-bc86-179fa549d80d',
                              version='7.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('PublishedExtension', response)

    def update_extension_by_id(self, extension_id, re_captcha_token=None):
        """UpdateExtensionById.
        [Preview API]
        :param str extension_id:
        :param str re_captcha_token:
        :rtype: :class:`<PublishedExtension> <azure.devops.v7_1.gallery.models.PublishedExtension>`
        """
        route_values = {}
        if extension_id is not None:
            route_values['extensionId'] = self._serialize.url('extension_id', extension_id, 'str')
        query_parameters = {}
        if re_captcha_token is not None:
            query_parameters['reCaptchaToken'] = self._serialize.query('re_captcha_token', re_captcha_token, 'str')
        response = self._send(http_method='PUT',
                              location_id='a41192c8-9525-4b58-bc86-179fa549d80d',
                              version='7.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('PublishedExtension', response)

    def create_extension_with_publisher(self, upload_stream, publisher_name, extension_type=None, re_captcha_token=None, **kwargs):
        """CreateExtensionWithPublisher.
        [Preview API]
        :param object upload_stream: Stream to upload
        :param str publisher_name:
        :param str extension_type:
        :param str re_captcha_token:
        :rtype: :class:`<PublishedExtension> <azure.devops.v7_1.gallery.models.PublishedExtension>`
        """
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        query_parameters = {}
        if extension_type is not None:
            query_parameters['extensionType'] = self._serialize.query('extension_type', extension_type, 'str')
        if re_captcha_token is not None:
            query_parameters['reCaptchaToken'] = self._serialize.query('re_captcha_token', re_captcha_token, 'str')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        content = self._client.stream_upload(upload_stream, callback=callback)
        response = self._send(http_method='POST',
                              location_id='e11ea35a-16fe-4b80-ab11-c4cab88a0966',
                              version='7.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content,
                              media_type='application/octet-stream')
        return self._deserialize('PublishedExtension', response)

    def delete_extension(self, publisher_name, extension_name, version=None):
        """DeleteExtension.
        [Preview API]
        :param str publisher_name:
        :param str extension_name:
        :param str version:
        """
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        query_parameters = {}
        if version is not None:
            query_parameters['version'] = self._serialize.query('version', version, 'str')
        self._send(http_method='DELETE',
                   location_id='e11ea35a-16fe-4b80-ab11-c4cab88a0966',
                   version='7.1-preview.2',
                   route_values=route_values,
                   query_parameters=query_parameters)

    def get_extension(self, publisher_name, extension_name, version=None, flags=None, account_token=None, account_token_header=None):
        """GetExtension.
        [Preview API]
        :param str publisher_name:
        :param str extension_name:
        :param str version:
        :param str flags:
        :param str account_token:
        :param String account_token_header: Header to pass the account token
        :rtype: :class:`<PublishedExtension> <azure.devops.v7_1.gallery.models.PublishedExtension>`
        """
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        query_parameters = {}
        if version is not None:
            query_parameters['version'] = self._serialize.query('version', version, 'str')
        if flags is not None:
            query_parameters['flags'] = self._serialize.query('flags', flags, 'str')
        if account_token is not None:
            query_parameters['accountToken'] = self._serialize.query('account_token', account_token, 'str')
        additional_headers = {}
        if account_token_header is not None:
            additional_headers['X-Market-AccountToken'] = account_token_header
        response = self._send(http_method='GET',
                              location_id='e11ea35a-16fe-4b80-ab11-c4cab88a0966',
                              version='7.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              additional_headers=additional_headers)
        return self._deserialize('PublishedExtension', response)

    def update_extension(self, upload_stream, publisher_name, extension_name, extension_type=None, re_captcha_token=None, bypass_scope_check=None, **kwargs):
        """UpdateExtension.
        [Preview API] REST endpoint to update an extension.
        :param object upload_stream: Stream to upload
        :param str publisher_name: Name of the publisher
        :param str extension_name: Name of the extension
        :param str extension_type:
        :param str re_captcha_token:
        :param bool bypass_scope_check: This parameter decides if the scope change check needs to be invoked or not
        :rtype: :class:`<PublishedExtension> <azure.devops.v7_1.gallery.models.PublishedExtension>`
        """
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        query_parameters = {}
        if extension_type is not None:
            query_parameters['extensionType'] = self._serialize.query('extension_type', extension_type, 'str')
        if re_captcha_token is not None:
            query_parameters['reCaptchaToken'] = self._serialize.query('re_captcha_token', re_captcha_token, 'str')
        if bypass_scope_check is not None:
            query_parameters['bypassScopeCheck'] = self._serialize.query('bypass_scope_check', bypass_scope_check, 'bool')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        content = self._client.stream_upload(upload_stream, callback=callback)
        response = self._send(http_method='PUT',
                              location_id='e11ea35a-16fe-4b80-ab11-c4cab88a0966',
                              version='7.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content,
                              media_type='application/octet-stream')
        return self._deserialize('PublishedExtension', response)

    def update_extension_properties(self, publisher_name, extension_name, flags):
        """UpdateExtensionProperties.
        [Preview API]
        :param str publisher_name:
        :param str extension_name:
        :param str flags:
        :rtype: :class:`<PublishedExtension> <azure.devops.v7_1.gallery.models.PublishedExtension>`
        """
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        query_parameters = {}
        if flags is not None:
            query_parameters['flags'] = self._serialize.query('flags', flags, 'str')
        response = self._send(http_method='PATCH',
                              location_id='e11ea35a-16fe-4b80-ab11-c4cab88a0966',
                              version='7.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('PublishedExtension', response)

    def share_extension_with_host(self, publisher_name, extension_name, host_type, host_name):
        """ShareExtensionWithHost.
        [Preview API]
        :param str publisher_name:
        :param str extension_name:
        :param str host_type:
        :param str host_name:
        """
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        if host_type is not None:
            route_values['hostType'] = self._serialize.url('host_type', host_type, 'str')
        if host_name is not None:
            route_values['hostName'] = self._serialize.url('host_name', host_name, 'str')
        self._send(http_method='POST',
                   location_id='328a3af8-d124-46e9-9483-01690cd415b9',
                   version='7.1-preview.1',
                   route_values=route_values)

    def unshare_extension_with_host(self, publisher_name, extension_name, host_type, host_name):
        """UnshareExtensionWithHost.
        [Preview API]
        :param str publisher_name:
        :param str extension_name:
        :param str host_type:
        :param str host_name:
        """
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        if host_type is not None:
            route_values['hostType'] = self._serialize.url('host_type', host_type, 'str')
        if host_name is not None:
            route_values['hostName'] = self._serialize.url('host_name', host_name, 'str')
        self._send(http_method='DELETE',
                   location_id='328a3af8-d124-46e9-9483-01690cd415b9',
                   version='7.1-preview.1',
                   route_values=route_values)

    def extension_validator(self, azure_rest_api_request_model):
        """ExtensionValidator.
        [Preview API]
        :param :class:`<AzureRestApiRequestModel> <azure.devops.v7_1.gallery.models.AzureRestApiRequestModel>` azure_rest_api_request_model:
        """
        content = self._serialize.body(azure_rest_api_request_model, 'AzureRestApiRequestModel')
        self._send(http_method='POST',
                   location_id='05e8a5e1-8c59-4c2c-8856-0ff087d1a844',
                   version='7.1-preview.1',
                   content=content)

    def send_notifications(self, notification_data):
        """SendNotifications.
        [Preview API] Send Notification
        :param :class:`<NotificationsData> <azure.devops.v7_1.gallery.models.NotificationsData>` notification_data: Denoting the data needed to send notification
        """
        content = self._serialize.body(notification_data, 'NotificationsData')
        self._send(http_method='POST',
                   location_id='eab39817-413c-4602-a49f-07ad00844980',
                   version='7.1-preview.1',
                   content=content)

    def get_package(self, publisher_name, extension_name, version, account_token=None, accept_default=None, account_token_header=None, **kwargs):
        """GetPackage.
        [Preview API] This endpoint gets hit when you download a VSTS extension from the Web UI
        :param str publisher_name:
        :param str extension_name:
        :param str version:
        :param str account_token:
        :param bool accept_default:
        :param String account_token_header: Header to pass the account token
        :rtype: object
        """
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        if version is not None:
            route_values['version'] = self._serialize.url('version', version, 'str')
        query_parameters = {}
        if account_token is not None:
            query_parameters['accountToken'] = self._serialize.query('account_token', account_token, 'str')
        if accept_default is not None:
            query_parameters['acceptDefault'] = self._serialize.query('accept_default', accept_default, 'bool')
        additional_headers = {}
        if account_token_header is not None:
            additional_headers['X-Market-AccountToken'] = account_token_header
        response = self._send(http_method='GET',
                              location_id='7cb576f8-1cae-4c4b-b7b1-e4af5759e965',
                              version='7.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              additional_headers=additional_headers,
                              accept_media_type='application/octet-stream')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_asset_with_token(self, publisher_name, extension_name, version, asset_type, asset_token=None, account_token=None, accept_default=None, account_token_header=None, **kwargs):
        """GetAssetWithToken.
        [Preview API]
        :param str publisher_name:
        :param str extension_name:
        :param str version:
        :param str asset_type:
        :param str asset_token:
        :param str account_token:
        :param bool accept_default:
        :param String account_token_header: Header to pass the account token
        :rtype: object
        """
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        if version is not None:
            route_values['version'] = self._serialize.url('version', version, 'str')
        if asset_type is not None:
            route_values['assetType'] = self._serialize.url('asset_type', asset_type, 'str')
        if asset_token is not None:
            route_values['assetToken'] = self._serialize.url('asset_token', asset_token, 'str')
        query_parameters = {}
        if account_token is not None:
            query_parameters['accountToken'] = self._serialize.query('account_token', account_token, 'str')
        if accept_default is not None:
            query_parameters['acceptDefault'] = self._serialize.query('accept_default', accept_default, 'bool')
        additional_headers = {}
        if account_token_header is not None:
            additional_headers['X-Market-AccountToken'] = account_token_header
        response = self._send(http_method='GET',
                              location_id='364415a1-0077-4a41-a7a0-06edd4497492',
                              version='7.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              additional_headers=additional_headers,
                              accept_media_type='application/octet-stream')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def delete_publisher_asset(self, publisher_name, asset_type=None):
        """DeletePublisherAsset.
        [Preview API] Delete publisher asset like logo
        :param str publisher_name: Internal name of the publisher
        :param str asset_type: Type of asset. Default value is 'logo'.
        """
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        query_parameters = {}
        if asset_type is not None:
            query_parameters['assetType'] = self._serialize.query('asset_type', asset_type, 'str')
        self._send(http_method='DELETE',
                   location_id='21143299-34f9-4c62-8ca8-53da691192f9',
                   version='7.1-preview.1',
                   route_values=route_values,
                   query_parameters=query_parameters)

    def get_publisher_asset(self, publisher_name, asset_type=None, **kwargs):
        """GetPublisherAsset.
        [Preview API] Get publisher asset like logo as a stream
        :param str publisher_name: Internal name of the publisher
        :param str asset_type: Type of asset. Default value is 'logo'.
        :rtype: object
        """
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        query_parameters = {}
        if asset_type is not None:
            query_parameters['assetType'] = self._serialize.query('asset_type', asset_type, 'str')
        response = self._send(http_method='GET',
                              location_id='21143299-34f9-4c62-8ca8-53da691192f9',
                              version='7.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='application/octet-stream')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def update_publisher_asset(self, upload_stream, publisher_name, asset_type=None, file_name=None, **kwargs):
        """UpdatePublisherAsset.
        [Preview API] Update publisher asset like logo. It accepts asset file as an octet stream and file name is passed in header values.
        :param object upload_stream: Stream to upload
        :param str publisher_name: Internal name of the publisher
        :param str asset_type: Type of asset. Default value is 'logo'.
        :param String file_name: Header to pass the filename of the uploaded data
        :rtype: {str}
        """
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        query_parameters = {}
        if asset_type is not None:
            query_parameters['assetType'] = self._serialize.query('asset_type', asset_type, 'str')
        additional_headers = {}
        if file_name is not None:
            additional_headers['X-Market-UploadFileName'] = file_name
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        content = self._client.stream_upload(upload_stream, callback=callback)
        response = self._send(http_method='PUT',
                              location_id='21143299-34f9-4c62-8ca8-53da691192f9',
                              version='7.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              additional_headers=additional_headers,
                              content=content,
                              media_type='application/octet-stream')
        return self._deserialize('{str}', self._unwrap_collection(response))

    def fetch_domain_token(self, publisher_name):
        """FetchDomainToken.
        [Preview API]
        :param str publisher_name:
        :rtype: str
        """
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        response = self._send(http_method='GET',
                              location_id='67a609ef-fa74-4b52-8664-78d76f7b3634',
                              version='7.1-preview.1',
                              route_values=route_values)
        return self._deserialize('str', response)

    def verify_domain_token(self, publisher_name):
        """VerifyDomainToken.
        [Preview API]
        :param str publisher_name:
        """
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        self._send(http_method='PUT',
                   location_id='67a609ef-fa74-4b52-8664-78d76f7b3634',
                   version='7.1-preview.1',
                   route_values=route_values)

    def query_publishers(self, publisher_query):
        """QueryPublishers.
        [Preview API]
        :param :class:`<PublisherQuery> <azure.devops.v7_1.gallery.models.PublisherQuery>` publisher_query:
        :rtype: :class:`<PublisherQueryResult> <azure.devops.v7_1.gallery.models.PublisherQueryResult>`
        """
        content = self._serialize.body(publisher_query, 'PublisherQuery')
        response = self._send(http_method='POST',
                              location_id='2ad6ee0a-b53f-4034-9d1d-d009fda1212e',
                              version='7.1-preview.1',
                              content=content)
        return self._deserialize('PublisherQueryResult', response)

    def create_publisher(self, publisher):
        """CreatePublisher.
        [Preview API]
        :param :class:`<Publisher> <azure.devops.v7_1.gallery.models.Publisher>` publisher:
        :rtype: :class:`<Publisher> <azure.devops.v7_1.gallery.models.Publisher>`
        """
        content = self._serialize.body(publisher, 'Publisher')
        response = self._send(http_method='POST',
                              location_id='4ddec66a-e4f6-4f5d-999e-9e77710d7ff4',
                              version='7.1-preview.1',
                              content=content)
        return self._deserialize('Publisher', response)

    def delete_publisher(self, publisher_name):
        """DeletePublisher.
        [Preview API]
        :param str publisher_name:
        """
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        self._send(http_method='DELETE',
                   location_id='4ddec66a-e4f6-4f5d-999e-9e77710d7ff4',
                   version='7.1-preview.1',
                   route_values=route_values)

    def get_publisher(self, publisher_name, flags=None):
        """GetPublisher.
        [Preview API]
        :param str publisher_name:
        :param int flags:
        :rtype: :class:`<Publisher> <azure.devops.v7_1.gallery.models.Publisher>`
        """
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        query_parameters = {}
        if flags is not None:
            query_parameters['flags'] = self._serialize.query('flags', flags, 'int')
        response = self._send(http_method='GET',
                              location_id='4ddec66a-e4f6-4f5d-999e-9e77710d7ff4',
                              version='7.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('Publisher', response)

    def update_publisher(self, publisher, publisher_name):
        """UpdatePublisher.
        [Preview API]
        :param :class:`<Publisher> <azure.devops.v7_1.gallery.models.Publisher>` publisher:
        :param str publisher_name:
        :rtype: :class:`<Publisher> <azure.devops.v7_1.gallery.models.Publisher>`
        """
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        content = self._serialize.body(publisher, 'Publisher')
        response = self._send(http_method='PUT',
                              location_id='4ddec66a-e4f6-4f5d-999e-9e77710d7ff4',
                              version='7.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Publisher', response)

    def update_publisher_members(self, role_assignments, publisher_name, limit_to_caller_identity_domain=None):
        """UpdatePublisherMembers.
        [Preview API] Endpoint to add/modify publisher membership. Currently Supports only addition/modification of 1 user at a time Works only for adding members of same tenant.
        :param [PublisherUserRoleAssignmentRef] role_assignments: List of user identifiers(email address) and role to be added. Currently only one entry is supported.
        :param str publisher_name: The name/id of publisher to which users have to be added
        :param bool limit_to_caller_identity_domain: Should cross tenant addtions be allowed or not.
        :rtype: [PublisherRoleAssignment]
        """
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        query_parameters = {}
        if limit_to_caller_identity_domain is not None:
            query_parameters['limitToCallerIdentityDomain'] = self._serialize.query('limit_to_caller_identity_domain', limit_to_caller_identity_domain, 'bool')
        content = self._serialize.body(role_assignments, '[PublisherUserRoleAssignmentRef]')
        response = self._send(http_method='POST',
                              location_id='4ddec66a-e4f6-4f5d-999e-9e77710d7ff4',
                              version='7.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('[PublisherRoleAssignment]', self._unwrap_collection(response))

    def get_publisher_without_token(self, publisher_name):
        """GetPublisherWithoutToken.
        [Preview API]
        :param str publisher_name:
        :rtype: :class:`<Publisher> <azure.devops.v7_1.gallery.models.Publisher>`
        """
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        response = self._send(http_method='GET',
                              location_id='215a2ed8-458a-4850-ad5a-45f1dabc3461',
                              version='7.1-preview.1',
                              route_values=route_values)
        return self._deserialize('Publisher', response)

    def get_questions(self, publisher_name, extension_name, count=None, page=None, after_date=None):
        """GetQuestions.
        [Preview API] Returns a list of questions with their responses associated with an extension.
        :param str publisher_name: Name of the publisher who published the extension.
        :param str extension_name: Name of the extension.
        :param int count: Number of questions to retrieve (defaults to 10).
        :param int page: Page number from which set of questions are to be retrieved.
        :param datetime after_date: If provided, results questions are returned which were posted after this date
        :rtype: :class:`<QuestionsResult> <azure.devops.v7_1.gallery.models.QuestionsResult>`
        """
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        query_parameters = {}
        if count is not None:
            query_parameters['count'] = self._serialize.query('count', count, 'int')
        if page is not None:
            query_parameters['page'] = self._serialize.query('page', page, 'int')
        if after_date is not None:
            query_parameters['afterDate'] = self._serialize.query('after_date', after_date, 'iso-8601')
        response = self._send(http_method='GET',
                              location_id='c010d03d-812c-4ade-ae07-c1862475eda5',
                              version='7.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('QuestionsResult', response)

    def report_question(self, concern, pub_name, ext_name, question_id):
        """ReportQuestion.
        [Preview API] Flags a concern with an existing question for an extension.
        :param :class:`<Concern> <azure.devops.v7_1.gallery.models.Concern>` concern: User reported concern with a question for the extension.
        :param str pub_name: Name of the publisher who published the extension.
        :param str ext_name: Name of the extension.
        :param long question_id: Identifier of the question to be updated for the extension.
        :rtype: :class:`<Concern> <azure.devops.v7_1.gallery.models.Concern>`
        """
        route_values = {}
        if pub_name is not None:
            route_values['pubName'] = self._serialize.url('pub_name', pub_name, 'str')
        if ext_name is not None:
            route_values['extName'] = self._serialize.url('ext_name', ext_name, 'str')
        if question_id is not None:
            route_values['questionId'] = self._serialize.url('question_id', question_id, 'long')
        content = self._serialize.body(concern, 'Concern')
        response = self._send(http_method='POST',
                              location_id='784910cd-254a-494d-898b-0728549b2f10',
                              version='7.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Concern', response)

    def create_question(self, question, publisher_name, extension_name):
        """CreateQuestion.
        [Preview API] Creates a new question for an extension.
        :param :class:`<Question> <azure.devops.v7_1.gallery.models.Question>` question: Question to be created for the extension.
        :param str publisher_name: Name of the publisher who published the extension.
        :param str extension_name: Name of the extension.
        :rtype: :class:`<Question> <azure.devops.v7_1.gallery.models.Question>`
        """
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        content = self._serialize.body(question, 'Question')
        response = self._send(http_method='POST',
                              location_id='6d1d9741-eca8-4701-a3a5-235afc82dfa4',
                              version='7.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Question', response)

    def delete_question(self, publisher_name, extension_name, question_id):
        """DeleteQuestion.
        [Preview API] Deletes an existing question and all its associated responses for an extension. (soft delete)
        :param str publisher_name: Name of the publisher who published the extension.
        :param str extension_name: Name of the extension.
        :param long question_id: Identifier of the question to be deleted for the extension.
        """
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        if question_id is not None:
            route_values['questionId'] = self._serialize.url('question_id', question_id, 'long')
        self._send(http_method='DELETE',
                   location_id='6d1d9741-eca8-4701-a3a5-235afc82dfa4',
                   version='7.1-preview.1',
                   route_values=route_values)

    def update_question(self, question, publisher_name, extension_name, question_id):
        """UpdateQuestion.
        [Preview API] Updates an existing question for an extension.
        :param :class:`<Question> <azure.devops.v7_1.gallery.models.Question>` question: Updated question to be set for the extension.
        :param str publisher_name: Name of the publisher who published the extension.
        :param str extension_name: Name of the extension.
        :param long question_id: Identifier of the question to be updated for the extension.
        :rtype: :class:`<Question> <azure.devops.v7_1.gallery.models.Question>`
        """
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        if question_id is not None:
            route_values['questionId'] = self._serialize.url('question_id', question_id, 'long')
        content = self._serialize.body(question, 'Question')
        response = self._send(http_method='PATCH',
                              location_id='6d1d9741-eca8-4701-a3a5-235afc82dfa4',
                              version='7.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Question', response)

    def create_response(self, response, publisher_name, extension_name, question_id):
        """CreateResponse.
        [Preview API] Creates a new response for a given question for an extension.
        :param :class:`<Response> <azure.devops.v7_1.gallery.models.Response>` response: Response to be created for the extension.
        :param str publisher_name: Name of the publisher who published the extension.
        :param str extension_name: Name of the extension.
        :param long question_id: Identifier of the question for which response is to be created for the extension.
        :rtype: :class:`<Response> <azure.devops.v7_1.gallery.models.Response>`
        """
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        if question_id is not None:
            route_values['questionId'] = self._serialize.url('question_id', question_id, 'long')
        content = self._serialize.body(response, 'Response')
        response = self._send(http_method='POST',
                              location_id='7f8ae5e0-46b0-438f-b2e8-13e8513517bd',
                              version='7.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Response', response)

    def delete_response(self, publisher_name, extension_name, question_id, response_id):
        """DeleteResponse.
        [Preview API] Deletes a response for an extension. (soft delete)
        :param str publisher_name: Name of the publisher who published the extension.
        :param str extension_name: Name of the extension.
        :param long question_id: Identifies the question whose response is to be deleted.
        :param long response_id: Identifies the response to be deleted.
        """
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        if question_id is not None:
            route_values['questionId'] = self._serialize.url('question_id', question_id, 'long')
        if response_id is not None:
            route_values['responseId'] = self._serialize.url('response_id', response_id, 'long')
        self._send(http_method='DELETE',
                   location_id='7f8ae5e0-46b0-438f-b2e8-13e8513517bd',
                   version='7.1-preview.1',
                   route_values=route_values)

    def update_response(self, response, publisher_name, extension_name, question_id, response_id):
        """UpdateResponse.
        [Preview API] Updates an existing response for a given question for an extension.
        :param :class:`<Response> <azure.devops.v7_1.gallery.models.Response>` response: Updated response to be set for the extension.
        :param str publisher_name: Name of the publisher who published the extension.
        :param str extension_name: Name of the extension.
        :param long question_id: Identifier of the question for which response is to be updated for the extension.
        :param long response_id: Identifier of the response which has to be updated.
        :rtype: :class:`<Response> <azure.devops.v7_1.gallery.models.Response>`
        """
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        if question_id is not None:
            route_values['questionId'] = self._serialize.url('question_id', question_id, 'long')
        if response_id is not None:
            route_values['responseId'] = self._serialize.url('response_id', response_id, 'long')
        content = self._serialize.body(response, 'Response')
        response = self._send(http_method='PATCH',
                              location_id='7f8ae5e0-46b0-438f-b2e8-13e8513517bd',
                              version='7.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Response', response)

    def get_extension_reports(self, publisher_name, extension_name, days=None, count=None, after_date=None):
        """GetExtensionReports.
        [Preview API] Returns extension reports
        :param str publisher_name: Name of the publisher who published the extension
        :param str extension_name: Name of the extension
        :param int days: Last n days report. If afterDate and days are specified, days will take priority
        :param int count: Number of events to be returned
        :param datetime after_date: Use if you want to fetch events newer than the specified date
        :rtype: object
        """
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        query_parameters = {}
        if days is not None:
            query_parameters['days'] = self._serialize.query('days', days, 'int')
        if count is not None:
            query_parameters['count'] = self._serialize.query('count', count, 'int')
        if after_date is not None:
            query_parameters['afterDate'] = self._serialize.query('after_date', after_date, 'iso-8601')
        response = self._send(http_method='GET',
                              location_id='79e0c74f-157f-437e-845f-74fbb4121d4c',
                              version='7.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('object', response)

    def get_reviews(self, publisher_name, extension_name, count=None, filter_options=None, before_date=None, after_date=None):
        """GetReviews.
        [Preview API] Returns a list of reviews associated with an extension
        :param str publisher_name: Name of the publisher who published the extension
        :param str extension_name: Name of the extension
        :param int count: Number of reviews to retrieve (defaults to 5)
        :param str filter_options: FilterOptions to filter out empty reviews etcetera, defaults to none
        :param datetime before_date: Use if you want to fetch reviews older than the specified date, defaults to null
        :param datetime after_date: Use if you want to fetch reviews newer than the specified date, defaults to null
        :rtype: :class:`<ReviewsResult> <azure.devops.v7_1.gallery.models.ReviewsResult>`
        """
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        query_parameters = {}
        if count is not None:
            query_parameters['count'] = self._serialize.query('count', count, 'int')
        if filter_options is not None:
            query_parameters['filterOptions'] = self._serialize.query('filter_options', filter_options, 'str')
        if before_date is not None:
            query_parameters['beforeDate'] = self._serialize.query('before_date', before_date, 'iso-8601')
        if after_date is not None:
            query_parameters['afterDate'] = self._serialize.query('after_date', after_date, 'iso-8601')
        response = self._send(http_method='GET',
                              location_id='5b3f819f-f247-42ad-8c00-dd9ab9ab246d',
                              version='7.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('ReviewsResult', response)

    def get_reviews_summary(self, pub_name, ext_name, before_date=None, after_date=None):
        """GetReviewsSummary.
        [Preview API] Returns a summary of the reviews
        :param str pub_name: Name of the publisher who published the extension
        :param str ext_name: Name of the extension
        :param datetime before_date: Use if you want to fetch summary of reviews older than the specified date, defaults to null
        :param datetime after_date: Use if you want to fetch summary of reviews newer than the specified date, defaults to null
        :rtype: :class:`<ReviewSummary> <azure.devops.v7_1.gallery.models.ReviewSummary>`
        """
        route_values = {}
        if pub_name is not None:
            route_values['pubName'] = self._serialize.url('pub_name', pub_name, 'str')
        if ext_name is not None:
            route_values['extName'] = self._serialize.url('ext_name', ext_name, 'str')
        query_parameters = {}
        if before_date is not None:
            query_parameters['beforeDate'] = self._serialize.query('before_date', before_date, 'iso-8601')
        if after_date is not None:
            query_parameters['afterDate'] = self._serialize.query('after_date', after_date, 'iso-8601')
        response = self._send(http_method='GET',
                              location_id='b7b44e21-209e-48f0-ae78-04727fc37d77',
                              version='7.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('ReviewSummary', response)

    def create_review(self, review, pub_name, ext_name):
        """CreateReview.
        [Preview API] Creates a new review for an extension
        :param :class:`<Review> <azure.devops.v7_1.gallery.models.Review>` review: Review to be created for the extension
        :param str pub_name: Name of the publisher who published the extension
        :param str ext_name: Name of the extension
        :rtype: :class:`<Review> <azure.devops.v7_1.gallery.models.Review>`
        """
        route_values = {}
        if pub_name is not None:
            route_values['pubName'] = self._serialize.url('pub_name', pub_name, 'str')
        if ext_name is not None:
            route_values['extName'] = self._serialize.url('ext_name', ext_name, 'str')
        content = self._serialize.body(review, 'Review')
        response = self._send(http_method='POST',
                              location_id='e6e85b9d-aa70-40e6-aa28-d0fbf40b91a3',
                              version='7.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Review', response)

    def delete_review(self, pub_name, ext_name, review_id):
        """DeleteReview.
        [Preview API] Deletes a review
        :param str pub_name: Name of the publisher who published the extension
        :param str ext_name: Name of the extension
        :param long review_id: Id of the review which needs to be updated
        """
        route_values = {}
        if pub_name is not None:
            route_values['pubName'] = self._serialize.url('pub_name', pub_name, 'str')
        if ext_name is not None:
            route_values['extName'] = self._serialize.url('ext_name', ext_name, 'str')
        if review_id is not None:
            route_values['reviewId'] = self._serialize.url('review_id', review_id, 'long')
        self._send(http_method='DELETE',
                   location_id='e6e85b9d-aa70-40e6-aa28-d0fbf40b91a3',
                   version='7.1-preview.1',
                   route_values=route_values)

    def update_review(self, review_patch, pub_name, ext_name, review_id):
        """UpdateReview.
        [Preview API] Updates or Flags a review
        :param :class:`<ReviewPatch> <azure.devops.v7_1.gallery.models.ReviewPatch>` review_patch: ReviewPatch object which contains the changes to be applied to the review
        :param str pub_name: Name of the publisher who published the extension
        :param str ext_name: Name of the extension
        :param long review_id: Id of the review which needs to be updated
        :rtype: :class:`<ReviewPatch> <azure.devops.v7_1.gallery.models.ReviewPatch>`
        """
        route_values = {}
        if pub_name is not None:
            route_values['pubName'] = self._serialize.url('pub_name', pub_name, 'str')
        if ext_name is not None:
            route_values['extName'] = self._serialize.url('ext_name', ext_name, 'str')
        if review_id is not None:
            route_values['reviewId'] = self._serialize.url('review_id', review_id, 'long')
        content = self._serialize.body(review_patch, 'ReviewPatch')
        response = self._send(http_method='PATCH',
                              location_id='e6e85b9d-aa70-40e6-aa28-d0fbf40b91a3',
                              version='7.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('ReviewPatch', response)

    def create_category(self, category):
        """CreateCategory.
        [Preview API]
        :param :class:`<ExtensionCategory> <azure.devops.v7_1.gallery.models.ExtensionCategory>` category:
        :rtype: :class:`<ExtensionCategory> <azure.devops.v7_1.gallery.models.ExtensionCategory>`
        """
        content = self._serialize.body(category, 'ExtensionCategory')
        response = self._send(http_method='POST',
                              location_id='476531a3-7024-4516-a76a-ed64d3008ad6',
                              version='7.1-preview.1',
                              content=content)
        return self._deserialize('ExtensionCategory', response)

    def get_gallery_user_settings(self, user_scope, key=None):
        """GetGalleryUserSettings.
        [Preview API] Get all setting entries for the given user/all-users scope
        :param str user_scope: User-Scope at which to get the value. Should be "me" for the current user or "host" for all users.
        :param str key: Optional key under which to filter all the entries
        :rtype: {object}
        """
        route_values = {}
        if user_scope is not None:
            route_values['userScope'] = self._serialize.url('user_scope', user_scope, 'str')
        if key is not None:
            route_values['key'] = self._serialize.url('key', key, 'str')
        response = self._send(http_method='GET',
                              location_id='9b75ece3-7960-401c-848b-148ac01ca350',
                              version='7.1-preview.1',
                              route_values=route_values)
        return self._deserialize('{object}', self._unwrap_collection(response))

    def set_gallery_user_settings(self, entries, user_scope):
        """SetGalleryUserSettings.
        [Preview API] Set all setting entries for the given user/all-users scope
        :param {object} entries: A key-value pair of all settings that need to be set
        :param str user_scope: User-Scope at which to get the value. Should be "me" for the current user or "host" for all users.
        """
        route_values = {}
        if user_scope is not None:
            route_values['userScope'] = self._serialize.url('user_scope', user_scope, 'str')
        content = self._serialize.body(entries, '{object}')
        self._send(http_method='PATCH',
                   location_id='9b75ece3-7960-401c-848b-148ac01ca350',
                   version='7.1-preview.1',
                   route_values=route_values,
                   content=content)

    def generate_key(self, key_type, expire_current_seconds=None):
        """GenerateKey.
        [Preview API]
        :param str key_type:
        :param int expire_current_seconds:
        """
        route_values = {}
        if key_type is not None:
            route_values['keyType'] = self._serialize.url('key_type', key_type, 'str')
        query_parameters = {}
        if expire_current_seconds is not None:
            query_parameters['expireCurrentSeconds'] = self._serialize.query('expire_current_seconds', expire_current_seconds, 'int')
        self._send(http_method='POST',
                   location_id='92ed5cf4-c38b-465a-9059-2f2fb7c624b5',
                   version='7.1-preview.1',
                   route_values=route_values,
                   query_parameters=query_parameters)

    def get_signing_key(self, key_type):
        """GetSigningKey.
        [Preview API]
        :param str key_type:
        :rtype: str
        """
        route_values = {}
        if key_type is not None:
            route_values['keyType'] = self._serialize.url('key_type', key_type, 'str')
        response = self._send(http_method='GET',
                              location_id='92ed5cf4-c38b-465a-9059-2f2fb7c624b5',
                              version='7.1-preview.1',
                              route_values=route_values)
        return self._deserialize('str', response)

    def update_extension_statistics(self, extension_statistics_update, publisher_name, extension_name):
        """UpdateExtensionStatistics.
        [Preview API]
        :param :class:`<ExtensionStatisticUpdate> <azure.devops.v7_1.gallery.models.ExtensionStatisticUpdate>` extension_statistics_update:
        :param str publisher_name:
        :param str extension_name:
        """
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        content = self._serialize.body(extension_statistics_update, 'ExtensionStatisticUpdate')
        self._send(http_method='PATCH',
                   location_id='a0ea3204-11e9-422d-a9ca-45851cc41400',
                   version='7.1-preview.1',
                   route_values=route_values,
                   content=content)

    def get_extension_daily_stats(self, publisher_name, extension_name, days=None, aggregate=None, after_date=None):
        """GetExtensionDailyStats.
        [Preview API]
        :param str publisher_name:
        :param str extension_name:
        :param int days:
        :param str aggregate:
        :param datetime after_date:
        :rtype: :class:`<ExtensionDailyStats> <azure.devops.v7_1.gallery.models.ExtensionDailyStats>`
        """
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        query_parameters = {}
        if days is not None:
            query_parameters['days'] = self._serialize.query('days', days, 'int')
        if aggregate is not None:
            query_parameters['aggregate'] = self._serialize.query('aggregate', aggregate, 'str')
        if after_date is not None:
            query_parameters['afterDate'] = self._serialize.query('after_date', after_date, 'iso-8601')
        response = self._send(http_method='GET',
                              location_id='ae06047e-51c5-4fb4-ab65-7be488544416',
                              version='7.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('ExtensionDailyStats', response)

    def get_extension_daily_stats_anonymous(self, publisher_name, extension_name, version):
        """GetExtensionDailyStatsAnonymous.
        [Preview API] This route/location id only supports HTTP POST anonymously, so that the page view daily stat can be incremented from Marketplace client. Trying to call GET on this route should result in an exception. Without this explicit implementation, calling GET on this public route invokes the above GET implementation GetExtensionDailyStats.
        :param str publisher_name: Name of the publisher
        :param str extension_name: Name of the extension
        :param str version: Version of the extension
        :rtype: :class:`<ExtensionDailyStats> <azure.devops.v7_1.gallery.models.ExtensionDailyStats>`
        """
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        if version is not None:
            route_values['version'] = self._serialize.url('version', version, 'str')
        response = self._send(http_method='GET',
                              location_id='4fa7adb6-ca65-4075-a232-5f28323288ea',
                              version='7.1-preview.1',
                              route_values=route_values)
        return self._deserialize('ExtensionDailyStats', response)

    def increment_extension_daily_stat(self, publisher_name, extension_name, version, stat_type, target_platform=None):
        """IncrementExtensionDailyStat.
        [Preview API] Increments a daily statistic associated with the extension
        :param str publisher_name: Name of the publisher
        :param str extension_name: Name of the extension
        :param str version: Version of the extension
        :param str stat_type: Type of stat to increment
        :param str target_platform:
        """
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        if version is not None:
            route_values['version'] = self._serialize.url('version', version, 'str')
        query_parameters = {}
        if stat_type is not None:
            query_parameters['statType'] = self._serialize.query('stat_type', stat_type, 'str')
        if target_platform is not None:
            query_parameters['targetPlatform'] = self._serialize.query('target_platform', target_platform, 'str')
        self._send(http_method='POST',
                   location_id='4fa7adb6-ca65-4075-a232-5f28323288ea',
                   version='7.1-preview.1',
                   route_values=route_values,
                   query_parameters=query_parameters)

    def get_verification_log(self, publisher_name, extension_name, version, target_platform=None, **kwargs):
        """GetVerificationLog.
        [Preview API]
        :param str publisher_name:
        :param str extension_name:
        :param str version:
        :param str target_platform:
        :rtype: object
        """
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        if version is not None:
            route_values['version'] = self._serialize.url('version', version, 'str')
        query_parameters = {}
        if target_platform is not None:
            query_parameters['targetPlatform'] = self._serialize.query('target_platform', target_platform, 'str')
        response = self._send(http_method='GET',
                              location_id='c5523abe-b843-437f-875b-5833064efe4d',
                              version='7.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='application/octet-stream')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def update_vSCode_web_extension_statistics(self, item_name, version, stat_type):
        """UpdateVSCodeWebExtensionStatistics.
        [Preview API]
        :param str item_name:
        :param str version:
        :param VSCodeWebExtensionStatisicsType stat_type:
        """
        route_values = {}
        if item_name is not None:
            route_values['itemName'] = self._serialize.url('item_name', item_name, 'str')
        if version is not None:
            route_values['version'] = self._serialize.url('version', version, 'str')
        if stat_type is not None:
            route_values['statType'] = self._serialize.url('stat_type', stat_type, 'VSCodeWebExtensionStatisicsType')
        self._send(http_method='POST',
                   location_id='205c91a8-7841-4fd3-ae4f-5a745d5a8df5',
                   version='7.1-preview.1',
                   route_values=route_values)

