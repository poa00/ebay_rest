# coding: utf-8

"""
    eBay Finances API

    This API is used to retrieve seller payouts and monetary transaction details related to those payouts.  # noqa: E501

    OpenAPI spec version: v1.16.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ...sell_finances.api_client import ApiClient


class SellerFundsSummaryApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_seller_funds_summary(self, x_ebay_c_marketplace_id, **kwargs):  # noqa: E501
        """get_seller_funds_summary  # noqa: E501

        <div class=\"msgbox_important\"><p class=\"msgbox_importantInDiv\" data-mc-autonum=\"&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;\"><span class=\"autonumber\"><span><b><span style=\"color: #dd1e31;\" class=\"mcFormatColor\">Important!</span></b></span></span> Due to EU &amp; UK Payments regulatory requirements, an additional security verification via Digital Signatures is required for certain API calls that are made on behalf of EU/UK sellers, including all <b>Finances API</b> methods. Please refer to <a href=\"/develop/guides/digital-signatures-for-apis \" target=\"_blank\">Digital Signatures for APIs</a> to learn more on the impacted APIs and the process to create signatures to be included in the HTTP payload.</p></div><br>This method retrieves all pending funds that have not yet been distibuted through a seller payout.<br><br>There are no input parameters for this method. The response payload includes available funds, funds being processed, funds on hold, and also an aggregate count of all three of these categories.<br><br>If there are no funds that are pending, on hold, or being processed for the seller's account, no response payload is returned, and an http status code of <code>204 - No Content</code> is returned instead.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_seller_funds_summary(x_ebay_c_marketplace_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_ebay_c_marketplace_id: This header identifies the seller's eBay marketplace. It is required for all marketplaces outside of the US.<br><br><span class=\"tablenote\"><b>Note:</b> If a marketplace ID value is not provided, the default value of <code>EBAY_US</code> is used.</span> <br> See <a href=\"/api-docs/static/rest-request-components.html#marketpl \" target=\"_blank \">HTTP request headers</a> for the marketplace ID values. (required)
        :return: SellerFundsSummaryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_seller_funds_summary_with_http_info(x_ebay_c_marketplace_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_seller_funds_summary_with_http_info(x_ebay_c_marketplace_id, **kwargs)  # noqa: E501
            return data

    def get_seller_funds_summary_with_http_info(self, x_ebay_c_marketplace_id, **kwargs):  # noqa: E501
        """get_seller_funds_summary  # noqa: E501

        <div class=\"msgbox_important\"><p class=\"msgbox_importantInDiv\" data-mc-autonum=\"&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;\"><span class=\"autonumber\"><span><b><span style=\"color: #dd1e31;\" class=\"mcFormatColor\">Important!</span></b></span></span> Due to EU &amp; UK Payments regulatory requirements, an additional security verification via Digital Signatures is required for certain API calls that are made on behalf of EU/UK sellers, including all <b>Finances API</b> methods. Please refer to <a href=\"/develop/guides/digital-signatures-for-apis \" target=\"_blank\">Digital Signatures for APIs</a> to learn more on the impacted APIs and the process to create signatures to be included in the HTTP payload.</p></div><br>This method retrieves all pending funds that have not yet been distibuted through a seller payout.<br><br>There are no input parameters for this method. The response payload includes available funds, funds being processed, funds on hold, and also an aggregate count of all three of these categories.<br><br>If there are no funds that are pending, on hold, or being processed for the seller's account, no response payload is returned, and an http status code of <code>204 - No Content</code> is returned instead.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_seller_funds_summary_with_http_info(x_ebay_c_marketplace_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_ebay_c_marketplace_id: This header identifies the seller's eBay marketplace. It is required for all marketplaces outside of the US.<br><br><span class=\"tablenote\"><b>Note:</b> If a marketplace ID value is not provided, the default value of <code>EBAY_US</code> is used.</span> <br> See <a href=\"/api-docs/static/rest-request-components.html#marketpl \" target=\"_blank \">HTTP request headers</a> for the marketplace ID values. (required)
        :return: SellerFundsSummaryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_ebay_c_marketplace_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_seller_funds_summary" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_ebay_c_marketplace_id' is set
        if ('x_ebay_c_marketplace_id' not in params or
                params['x_ebay_c_marketplace_id'] is None):
            raise ValueError("Missing the required parameter `x_ebay_c_marketplace_id` when calling `get_seller_funds_summary`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_ebay_c_marketplace_id' in params:
            header_params['X-EBAY-C-MARKETPLACE-ID'] = params['x_ebay_c_marketplace_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_auth']  # noqa: E501

        return self.api_client.call_api(
            '/seller_funds_summary', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SellerFundsSummaryResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
