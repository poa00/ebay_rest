# coding: utf-8

"""
     Seller Service Metrics API 

    The <i>Analytics API</i> provides data and information about a seller and their eBay business.  <br><br>The resources and methods in this API let sellers review information on their listing performance, metrics on their customer service performance, and details on their eBay seller performance rating.  <br><br>The three resources in the Analytics API provide the following data and information: <ul><li><b>Customer Service Metric</b> &ndash; Returns benchmark data and a metric rating pertaining to a seller's customer service performance as compared to other seller's in the same peer group.</li> <li><b>Traffic Report</b> &ndash; Returns data and information that shows how buyers are engaging with a seller's listings.</li> <li><b>Seller Standards Profile</b> &ndash; Returns information pertaining to a seller's profile rating.</li></ul> Sellers can use the data and information returned by the various Analytics API methods to determine where they can make improvements to increase sales and how they might improve their seller status as viewed by eBay buyers.  <br><br>For details on using this API, see <a href=\"/api-docs/sell/static/performance/analyzing-performance.html\" title=\"Selling Integration Guide\">Analyzing seller performance</a>.  # noqa: E501

    OpenAPI spec version: 1.3.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ...sell_analytics.api_client import ApiClient


class SellerStandardsProfileApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def find_seller_standards_profiles(self, **kwargs):  # noqa: E501
        """find_seller_standards_profiles  # noqa: E501

        This call retrieves all the standards profiles for the associated seller.  <br><br>A <i>standards profile </i> is a set of eBay seller metrics and the seller's associated compliance values (either <code>TOP_RATED</code>, <code>ABOVE_STANDARD</code>, or <code>BELOW_STANDARD</code>).  <br><br>A seller's multiple profiles are distinguished by two criteria, a \"program\" and a \"cycle.\" A profile's <i>program </i> is one of three regions where the seller may have done business, or <code>PROGRAM_GLOBAL</code> to indicate all marketplaces where the seller has done business. The <i>cycle</i> value specifies whether the standards compliance values were determined at the last official eBay evaluation or at the time of the request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.find_seller_standards_profiles(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: FindSellerStandardsProfilesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.find_seller_standards_profiles_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.find_seller_standards_profiles_with_http_info(**kwargs)  # noqa: E501
            return data

    def find_seller_standards_profiles_with_http_info(self, **kwargs):  # noqa: E501
        """find_seller_standards_profiles  # noqa: E501

        This call retrieves all the standards profiles for the associated seller.  <br><br>A <i>standards profile </i> is a set of eBay seller metrics and the seller's associated compliance values (either <code>TOP_RATED</code>, <code>ABOVE_STANDARD</code>, or <code>BELOW_STANDARD</code>).  <br><br>A seller's multiple profiles are distinguished by two criteria, a \"program\" and a \"cycle.\" A profile's <i>program </i> is one of three regions where the seller may have done business, or <code>PROGRAM_GLOBAL</code> to indicate all marketplaces where the seller has done business. The <i>cycle</i> value specifies whether the standards compliance values were determined at the last official eBay evaluation or at the time of the request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.find_seller_standards_profiles_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: FindSellerStandardsProfilesResponse
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
                    " to method find_seller_standards_profiles" % key
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
            '/seller_standards_profile', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FindSellerStandardsProfilesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_seller_standards_profile(self, cycle, program, **kwargs):  # noqa: E501
        """get_seller_standards_profile  # noqa: E501

        This call retrieves a single standards profile for the associated seller.  <br><br>A <i>standards profile </i> is a set of eBay seller metrics and the seller's associated compliance values (either <code>TOP_RATED</code>, <code>ABOVE_STANDARD</code>, or <code>BELOW_STANDARD</code>).  <br><br>A seller can have multiple profiles distinguished by two criteria, a \"program\" and a \"cycle.\" A profile's <i>program </i> is one of three regions where the seller may have done business, or <code>PROGRAM_GLOBAL</code> to indicate all marketplaces where the seller has done business. The <i>cycle</i> value specifies whether the standards compliance values were determined at the last official eBay evaluation (<code>CURRENT</code>) or at the time of the request (<code>PROJECTED</code>). Both cycle and a program values are required URI parameters for this method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_seller_standards_profile(cycle, program, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cycle: This path parameter is used to specify the cycle for which metrics and metadata will be retrieved.<br><br>See <a href=\"/api-docs/sell/analytics/types/ssp:CycleTypeEnum\" target=\"_blank\">CycleTypeEnum</a> for a list of supported values. (required)
        :param str program: This path parameter is used to specify the seller standards program for which metrics and metadata will be retrieved. <br><br>See <a href=\"/api-docs/sell/analytics/types/ssp:ProgramEnum\" target=\"_blank\">ProgramEnum</a> for a list of supported values. (required)
        :return: StandardsProfile
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_seller_standards_profile_with_http_info(cycle, program, **kwargs)  # noqa: E501
        else:
            (data) = self.get_seller_standards_profile_with_http_info(cycle, program, **kwargs)  # noqa: E501
            return data

    def get_seller_standards_profile_with_http_info(self, cycle, program, **kwargs):  # noqa: E501
        """get_seller_standards_profile  # noqa: E501

        This call retrieves a single standards profile for the associated seller.  <br><br>A <i>standards profile </i> is a set of eBay seller metrics and the seller's associated compliance values (either <code>TOP_RATED</code>, <code>ABOVE_STANDARD</code>, or <code>BELOW_STANDARD</code>).  <br><br>A seller can have multiple profiles distinguished by two criteria, a \"program\" and a \"cycle.\" A profile's <i>program </i> is one of three regions where the seller may have done business, or <code>PROGRAM_GLOBAL</code> to indicate all marketplaces where the seller has done business. The <i>cycle</i> value specifies whether the standards compliance values were determined at the last official eBay evaluation (<code>CURRENT</code>) or at the time of the request (<code>PROJECTED</code>). Both cycle and a program values are required URI parameters for this method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_seller_standards_profile_with_http_info(cycle, program, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cycle: This path parameter is used to specify the cycle for which metrics and metadata will be retrieved.<br><br>See <a href=\"/api-docs/sell/analytics/types/ssp:CycleTypeEnum\" target=\"_blank\">CycleTypeEnum</a> for a list of supported values. (required)
        :param str program: This path parameter is used to specify the seller standards program for which metrics and metadata will be retrieved. <br><br>See <a href=\"/api-docs/sell/analytics/types/ssp:ProgramEnum\" target=\"_blank\">ProgramEnum</a> for a list of supported values. (required)
        :return: StandardsProfile
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cycle', 'program']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_seller_standards_profile" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cycle' is set
        if ('cycle' not in params or
                params['cycle'] is None):
            raise ValueError("Missing the required parameter `cycle` when calling `get_seller_standards_profile`")  # noqa: E501
        # verify the required parameter 'program' is set
        if ('program' not in params or
                params['program'] is None):
            raise ValueError("Missing the required parameter `program` when calling `get_seller_standards_profile`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cycle' in params:
            path_params['cycle'] = params['cycle']  # noqa: E501
        if 'program' in params:
            path_params['program'] = params['program']  # noqa: E501

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
            '/seller_standards_profile/{program}/{cycle}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StandardsProfile',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
