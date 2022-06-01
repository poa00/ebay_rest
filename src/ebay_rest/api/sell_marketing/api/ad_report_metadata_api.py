# coding: utf-8

"""
    Marketing API

    <p>The <i>Marketing API </i> offers two platforms that sellers can use to promote and advertise their products:</p> <ul><li><b>Promoted Listings</b> is an eBay ad service that lets sellers set up <i>ad campaigns </i> for the products they want to promote. eBay displays the ads in search results and in other marketing modules as <b>SPONSORED</b> listings. If an item in a Promoted Listings campaign sells, the seller is assessed a Promoted Listings fee, which is a seller-specified percentage applied to the sales price. For complete details, see <a href=\"/api-docs/sell/static/marketing/promoted-listings.html\">Promoted Listings</a>.</li>  <li><b>Promotions Manager</b> gives sellers a way to offer discounts on specific items as a way to attract buyers to their inventory. Sellers can set up discounts (such as \"20% off\" and other types of offers) on specific items or on an entire customer order. To further attract buyers, eBay prominently displays promotion <i>teasers</i> throughout buyer flows. For complete details, see <a href=\"/api-docs/sell/static/marketing/promotions-manager.html\">Promotions Manager</a>.</li></ul>  <p><b>Marketing reports</b>, on both the Promoted Listings and Promotions Manager platforms, give sellers information that shows the effectiveness of their marketing strategies. The data gives sellers the ability to review and fine tune their marketing efforts.</p> <p class=\"tablenote\"><b>Important!</b> Sellers must have an active eBay Store subscription, and they must accept the <b>Terms and Conditions</b> before they can make requests to these APIs in the Production environment. There are also site-specific listings requirements and restrictions associated with these marketing tools, as listed in the \"requirements and restrictions\" sections for <a href=\"/api-docs/sell/marketing/static/overview.html#PL-requirements\">Promoted Listings</a> and <a href=\"/api-docs/sell/marketing/static/overview.html#PM-requirements\">Promotions Manager</a>.</p> <p>The table below lists all the Marketing API calls grouped by resource.</p>  # noqa: E501

    OpenAPI spec version: v1.10.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ...sell_marketing.api_client import ApiClient


class AdReportMetadataApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_report_metadata(self, **kwargs):  # noqa: E501
        """get_report_metadata  # noqa: E501

        This call retrieves information that details the fields used in each of the Promoted Listings reports. Use the returned information to configure the different types of Promoted Listings reports.  <p> The request for this method does not use a payload or any URI parameters.</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_report_metadata(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ReportMetadatas
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_report_metadata_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_report_metadata_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_report_metadata_with_http_info(self, **kwargs):  # noqa: E501
        """get_report_metadata  # noqa: E501

        This call retrieves information that details the fields used in each of the Promoted Listings reports. Use the returned information to configure the different types of Promoted Listings reports.  <p> The request for this method does not use a payload or any URI parameters.</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_report_metadata_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ReportMetadatas
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_report_metadata" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/ad_report_metadata', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReportMetadatas',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_report_metadata_for_report_type(self, report_type, **kwargs):  # noqa: E501
        """get_report_metadata_for_report_type  # noqa: E501

        This call retrieves metadata that details the fields used by a specific Promoted Listings report type. Use the <b>report_type</b> path parameter to indicate metadata to retrieve.  <p>This method does not use a request payload.</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_report_metadata_for_report_type(report_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str report_type: The name of the report type whose metadata you want to get.  <br><br>For details about each report type, see <a href=\"/api-docs/sell/marketing/types/plr:ReportTypeEnum\">ReportTypeEnum</a>. <br><br><b>Valid values:</b> <br>&nbsp;&nbsp;&nbsp;<code>ACCOUNT_PERFORMANCE_REPORT</code> <br>&nbsp;&nbsp;&nbsp;<code>CAMPAIGN_PERFORMANCE_REPORT</code> <br>&nbsp;&nbsp;&nbsp;<code>CAMPAIGN_PERFORMANCE_SUMMARY_REPORT</code> <br>&nbsp;&nbsp;&nbsp;<code>LISTING_PERFORMANCE_REPORT</code> <br>&nbsp;&nbsp;&nbsp;<code>INVENTORY_PERFORMANCE_REPORT</code> (required)
        :return: ReportMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_report_metadata_for_report_type_with_http_info(report_type, **kwargs)  # noqa: E501
        else:
            (data) = self.get_report_metadata_for_report_type_with_http_info(report_type, **kwargs)  # noqa: E501
            return data

    def get_report_metadata_for_report_type_with_http_info(self, report_type, **kwargs):  # noqa: E501
        """get_report_metadata_for_report_type  # noqa: E501

        This call retrieves metadata that details the fields used by a specific Promoted Listings report type. Use the <b>report_type</b> path parameter to indicate metadata to retrieve.  <p>This method does not use a request payload.</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_report_metadata_for_report_type_with_http_info(report_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str report_type: The name of the report type whose metadata you want to get.  <br><br>For details about each report type, see <a href=\"/api-docs/sell/marketing/types/plr:ReportTypeEnum\">ReportTypeEnum</a>. <br><br><b>Valid values:</b> <br>&nbsp;&nbsp;&nbsp;<code>ACCOUNT_PERFORMANCE_REPORT</code> <br>&nbsp;&nbsp;&nbsp;<code>CAMPAIGN_PERFORMANCE_REPORT</code> <br>&nbsp;&nbsp;&nbsp;<code>CAMPAIGN_PERFORMANCE_SUMMARY_REPORT</code> <br>&nbsp;&nbsp;&nbsp;<code>LISTING_PERFORMANCE_REPORT</code> <br>&nbsp;&nbsp;&nbsp;<code>INVENTORY_PERFORMANCE_REPORT</code> (required)
        :return: ReportMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['report_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_report_metadata_for_report_type" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'report_type' is set
        if ('report_type' not in params or
                params['report_type'] is None):
            raise ValueError("Missing the required parameter `report_type` when calling `get_report_metadata_for_report_type`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'report_type' in params:
            path_params['report_type'] = params['report_type']  # noqa: E501

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
            '/ad_report_metadata/{report_type}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReportMetadata',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
