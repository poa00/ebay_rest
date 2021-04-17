# coding: utf-8

"""
    Inventory API

    The Inventory API is used to create and manage inventory, and then to publish and manage this inventory on an eBay marketplace. There are also methods in this API that will convert eligible, active eBay listings into the Inventory API model.  # noqa: E501

    OpenAPI spec version: 1.12.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from sell_inventory.api_client import ApiClient


class InventoryItemGroupApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_or_replace_inventory_item_group(self, body, content_language, inventory_item_group_key, **kwargs):  # noqa: E501
        """create_or_replace_inventory_item_group  # noqa: E501

        This call creates a new inventory item group or updates an existing inventory item group. It is up to sellers whether they want to create a complete inventory item group record right from the start, or sellers can provide only some information with the initial createOrReplaceInventoryItemGroup call, and then make one or more additional createOrReplaceInventoryItemGroup calls to complete the inventory item group record. Upon first creating an inventory item group record, the only required elements are the inventoryItemGroupKey identifier in the call URI, and the members of the inventory item group specified through the variantSKUs array in the request payload. In the case of updating/replacing an existing inventory item group, this call does a complete replacement of the existing inventory item group record, so all fields (including the member SKUs) that make up the inventory item group are required, regardless of whether their values changed. So, when replacing/updating an inventory item group record, it is advised that the seller run a getInventoryItemGroup call for that inventory item group to see all of its current values/settings/members before attempting to update the record. And if changes are made to an inventory item group that is part of a live, multiple-variation eBay listing, these changes automatically update the eBay listing. For example, if a SKU value is removed from the inventory item group, the corresponding product variation will be removed from the eBay listing as well. In addition to the required inventory item group identifier and member SKUs, other key information that is set with this call include: Title and description of the inventory item group. The string values provided in these fields will actually become the listing title and listing description of the listing once the first SKU of the inventory item group is published successfully Common aspects that inventory items in the qroup share Product aspects that vary within each product variation Links to images demonstrating the variations of the product, and these images should correspond to the product aspect that is set with the variesBy.aspectsImageVariesBy field In addition to the authorization header, which is required for all eBay REST API calls, the createOrReplaceInventoryItemGroup call also requires the Content-Language header, that sets the natural language that will be used in the field values of the request payload. For US English, the code value passed in this header should be en-US. To view other supported Content-Language values, and to read more about all supported HTTP headers for eBay REST API calls, see the HTTP request headers topic in the Using eBay RESTful APIs document.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_or_replace_inventory_item_group(body, content_language, inventory_item_group_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param InventoryItemGroup body: Details of the inventory Item Group (required)
        :param str content_language: This request header sets the natural language that will be provided in the field values of the request payload. (required)
        :param str inventory_item_group_key: Unique identifier of the inventory item group. This identifier is supplied by the seller. The inventoryItemGroupKey value for the inventory item group to create/update is passed in at the end of the call URI. This value cannot be changed once it is set. (required)
        :return: BaseResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_or_replace_inventory_item_group_with_http_info(body, content_language, inventory_item_group_key, **kwargs)  # noqa: E501
        else:
            (data) = self.create_or_replace_inventory_item_group_with_http_info(body, content_language, inventory_item_group_key, **kwargs)  # noqa: E501
            return data

    def create_or_replace_inventory_item_group_with_http_info(self, body, content_language, inventory_item_group_key, **kwargs):  # noqa: E501
        """create_or_replace_inventory_item_group  # noqa: E501

        This call creates a new inventory item group or updates an existing inventory item group. It is up to sellers whether they want to create a complete inventory item group record right from the start, or sellers can provide only some information with the initial createOrReplaceInventoryItemGroup call, and then make one or more additional createOrReplaceInventoryItemGroup calls to complete the inventory item group record. Upon first creating an inventory item group record, the only required elements are the inventoryItemGroupKey identifier in the call URI, and the members of the inventory item group specified through the variantSKUs array in the request payload. In the case of updating/replacing an existing inventory item group, this call does a complete replacement of the existing inventory item group record, so all fields (including the member SKUs) that make up the inventory item group are required, regardless of whether their values changed. So, when replacing/updating an inventory item group record, it is advised that the seller run a getInventoryItemGroup call for that inventory item group to see all of its current values/settings/members before attempting to update the record. And if changes are made to an inventory item group that is part of a live, multiple-variation eBay listing, these changes automatically update the eBay listing. For example, if a SKU value is removed from the inventory item group, the corresponding product variation will be removed from the eBay listing as well. In addition to the required inventory item group identifier and member SKUs, other key information that is set with this call include: Title and description of the inventory item group. The string values provided in these fields will actually become the listing title and listing description of the listing once the first SKU of the inventory item group is published successfully Common aspects that inventory items in the qroup share Product aspects that vary within each product variation Links to images demonstrating the variations of the product, and these images should correspond to the product aspect that is set with the variesBy.aspectsImageVariesBy field In addition to the authorization header, which is required for all eBay REST API calls, the createOrReplaceInventoryItemGroup call also requires the Content-Language header, that sets the natural language that will be used in the field values of the request payload. For US English, the code value passed in this header should be en-US. To view other supported Content-Language values, and to read more about all supported HTTP headers for eBay REST API calls, see the HTTP request headers topic in the Using eBay RESTful APIs document.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_or_replace_inventory_item_group_with_http_info(body, content_language, inventory_item_group_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param InventoryItemGroup body: Details of the inventory Item Group (required)
        :param str content_language: This request header sets the natural language that will be provided in the field values of the request payload. (required)
        :param str inventory_item_group_key: Unique identifier of the inventory item group. This identifier is supplied by the seller. The inventoryItemGroupKey value for the inventory item group to create/update is passed in at the end of the call URI. This value cannot be changed once it is set. (required)
        :return: BaseResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'content_language', 'inventory_item_group_key']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_or_replace_inventory_item_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_or_replace_inventory_item_group`")  # noqa: E501
        # verify the required parameter 'content_language' is set
        if ('content_language' not in params or
                params['content_language'] is None):
            raise ValueError("Missing the required parameter `content_language` when calling `create_or_replace_inventory_item_group`")  # noqa: E501
        # verify the required parameter 'inventory_item_group_key' is set
        if ('inventory_item_group_key' not in params or
                params['inventory_item_group_key'] is None):
            raise ValueError("Missing the required parameter `inventory_item_group_key` when calling `create_or_replace_inventory_item_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'inventory_item_group_key' in params:
            path_params['inventoryItemGroupKey'] = params['inventory_item_group_key']  # noqa: E501

        query_params = []

        header_params = {}
        if 'content_language' in params:
            header_params['Content-Language'] = params['content_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_auth']  # noqa: E501

        return self.api_client.call_api(
            '/inventory_item_group/{inventoryItemGroupKey}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BaseResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_inventory_item_group(self, inventory_item_group_key, **kwargs):  # noqa: E501
        """delete_inventory_item_group  # noqa: E501

        This call deletes the inventory item group for a given inventoryItemGroupKey value.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_inventory_item_group(inventory_item_group_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str inventory_item_group_key: The unique identifier of an inventory item group. This value is assigned by the seller when an inventory item group is created. The inventoryItemGroupKey value for the inventory item group to delete is passed in at the end of the call URI. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_inventory_item_group_with_http_info(inventory_item_group_key, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_inventory_item_group_with_http_info(inventory_item_group_key, **kwargs)  # noqa: E501
            return data

    def delete_inventory_item_group_with_http_info(self, inventory_item_group_key, **kwargs):  # noqa: E501
        """delete_inventory_item_group  # noqa: E501

        This call deletes the inventory item group for a given inventoryItemGroupKey value.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_inventory_item_group_with_http_info(inventory_item_group_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str inventory_item_group_key: The unique identifier of an inventory item group. This value is assigned by the seller when an inventory item group is created. The inventoryItemGroupKey value for the inventory item group to delete is passed in at the end of the call URI. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['inventory_item_group_key']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_inventory_item_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'inventory_item_group_key' is set
        if ('inventory_item_group_key' not in params or
                params['inventory_item_group_key'] is None):
            raise ValueError("Missing the required parameter `inventory_item_group_key` when calling `delete_inventory_item_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'inventory_item_group_key' in params:
            path_params['inventoryItemGroupKey'] = params['inventory_item_group_key']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['api_auth']  # noqa: E501

        return self.api_client.call_api(
            '/inventory_item_group/{inventoryItemGroupKey}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_inventory_item_group(self, inventory_item_group_key, **kwargs):  # noqa: E501
        """get_inventory_item_group  # noqa: E501

        This call retrieves the inventory item group for a given inventoryItemGroupKey value. The inventoryItemGroupKey value is passed in at the end of the call URI.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_inventory_item_group(inventory_item_group_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str inventory_item_group_key: The unique identifier of an inventory item group. This value is assigned by the seller when an inventory item group is created. The inventoryItemGroupKey value for the inventory item group to retrieve is passed in at the end of the call URI. (required)
        :return: InventoryItemGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_inventory_item_group_with_http_info(inventory_item_group_key, **kwargs)  # noqa: E501
        else:
            (data) = self.get_inventory_item_group_with_http_info(inventory_item_group_key, **kwargs)  # noqa: E501
            return data

    def get_inventory_item_group_with_http_info(self, inventory_item_group_key, **kwargs):  # noqa: E501
        """get_inventory_item_group  # noqa: E501

        This call retrieves the inventory item group for a given inventoryItemGroupKey value. The inventoryItemGroupKey value is passed in at the end of the call URI.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_inventory_item_group_with_http_info(inventory_item_group_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str inventory_item_group_key: The unique identifier of an inventory item group. This value is assigned by the seller when an inventory item group is created. The inventoryItemGroupKey value for the inventory item group to retrieve is passed in at the end of the call URI. (required)
        :return: InventoryItemGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['inventory_item_group_key']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_inventory_item_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'inventory_item_group_key' is set
        if ('inventory_item_group_key' not in params or
                params['inventory_item_group_key'] is None):
            raise ValueError("Missing the required parameter `inventory_item_group_key` when calling `get_inventory_item_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'inventory_item_group_key' in params:
            path_params['inventoryItemGroupKey'] = params['inventory_item_group_key']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_auth']  # noqa: E501

        return self.api_client.call_api(
            '/inventory_item_group/{inventoryItemGroupKey}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InventoryItemGroup',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
