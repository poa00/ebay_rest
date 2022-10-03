# coding: utf-8

"""
    Account API

    The <b>Account API</b> gives sellers the ability to configure their eBay seller accounts, including the seller's policies (eBay business policies and seller-defined custom policies), opt in and out of eBay seller programs, configure sales tax tables, and get account information.  <br/><br/>For details on the availability of the methods in this API, see <a href=\"/api-docs/sell/account/overview.html#requirements\">Account API requirements and restrictions</a>.  # noqa: E501

    OpenAPI spec version: v1.9.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ...sell_account.api_client import ApiClient


class SalesTaxApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_or_replace_sales_tax(self, body, country_code, jurisdiction_id, **kwargs):  # noqa: E501
        """create_or_replace_sales_tax  # noqa: E501

        This method creates or updates a sales tax table entry for a jurisdiction. Specify the tax table entry you want to configure using the two path parameters: <b>countryCode</b> and <b>jurisdictionId</b>.  <br/><br/>A tax table entry for a jurisdiction is comprised of two fields: one for the jurisdiction's sales-tax rate and another that's a boolean value indicating whether or not shipping and handling are taxed in the jurisdiction.  <br/><br/>You can set up <i>tax tables</i> for countries that support different <i>tax jurisdictions</i>. Currently, only Canada, India, and the US support separate tax jurisdictions. If you sell into any of these countries, you can set up tax tables for any of the country's jurisdictions. Retrieve valid jurisdiction IDs using <b>getSalesTaxJurisdictions</b> in the Metadata API.  <br/><br/>For details on using this call, see <a href=\"/api-docs/sell/static/seller-accounts/tax-tables.html\">Establishing sales-tax tables</a>. <br/><br/><span class=\"tablenote\"><b>Important!</b> In the US, eBay now 'collects and remits' sales tax for every US state except for Missouri (and a few US territories), so sellers can no longer configure sales tax rates for any states except Missouri. With eBay 'collect and remit', eBay calculates the sales tax, collects the sales tax from the buyer, and remits the sales tax to the tax authorities at the buyer's location.</span>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_or_replace_sales_tax(body, country_code, jurisdiction_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SalesTaxBase body: A container that describes the how the sales tax is calculated. (required)
        :param str country_code: This path parameter specifies the two-letter <a href=\"https://www.iso.org/iso-3166-country-codes.html\" title=\"https://www.iso.org\" target=\"_blank\">ISO 3166</a> code for the country for which you want to create a sales tax table entry. (required)
        :param str jurisdiction_id: This path parameter specifies the ID of the tax jurisdiction for the table entry you want to create. Retrieve valid jurisdiction IDs using <b>getSalesTaxJurisdictions</b> in the Metadata API. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_or_replace_sales_tax_with_http_info(body, country_code, jurisdiction_id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_or_replace_sales_tax_with_http_info(body, country_code, jurisdiction_id, **kwargs)  # noqa: E501
            return data

    def create_or_replace_sales_tax_with_http_info(self, body, country_code, jurisdiction_id, **kwargs):  # noqa: E501
        """create_or_replace_sales_tax  # noqa: E501

        This method creates or updates a sales tax table entry for a jurisdiction. Specify the tax table entry you want to configure using the two path parameters: <b>countryCode</b> and <b>jurisdictionId</b>.  <br/><br/>A tax table entry for a jurisdiction is comprised of two fields: one for the jurisdiction's sales-tax rate and another that's a boolean value indicating whether or not shipping and handling are taxed in the jurisdiction.  <br/><br/>You can set up <i>tax tables</i> for countries that support different <i>tax jurisdictions</i>. Currently, only Canada, India, and the US support separate tax jurisdictions. If you sell into any of these countries, you can set up tax tables for any of the country's jurisdictions. Retrieve valid jurisdiction IDs using <b>getSalesTaxJurisdictions</b> in the Metadata API.  <br/><br/>For details on using this call, see <a href=\"/api-docs/sell/static/seller-accounts/tax-tables.html\">Establishing sales-tax tables</a>. <br/><br/><span class=\"tablenote\"><b>Important!</b> In the US, eBay now 'collects and remits' sales tax for every US state except for Missouri (and a few US territories), so sellers can no longer configure sales tax rates for any states except Missouri. With eBay 'collect and remit', eBay calculates the sales tax, collects the sales tax from the buyer, and remits the sales tax to the tax authorities at the buyer's location.</span>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_or_replace_sales_tax_with_http_info(body, country_code, jurisdiction_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SalesTaxBase body: A container that describes the how the sales tax is calculated. (required)
        :param str country_code: This path parameter specifies the two-letter <a href=\"https://www.iso.org/iso-3166-country-codes.html\" title=\"https://www.iso.org\" target=\"_blank\">ISO 3166</a> code for the country for which you want to create a sales tax table entry. (required)
        :param str jurisdiction_id: This path parameter specifies the ID of the tax jurisdiction for the table entry you want to create. Retrieve valid jurisdiction IDs using <b>getSalesTaxJurisdictions</b> in the Metadata API. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'country_code', 'jurisdiction_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_or_replace_sales_tax" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_or_replace_sales_tax`")  # noqa: E501
        # verify the required parameter 'country_code' is set
        if ('country_code' not in params or
                params['country_code'] is None):
            raise ValueError("Missing the required parameter `country_code` when calling `create_or_replace_sales_tax`")  # noqa: E501
        # verify the required parameter 'jurisdiction_id' is set
        if ('jurisdiction_id' not in params or
                params['jurisdiction_id'] is None):
            raise ValueError("Missing the required parameter `jurisdiction_id` when calling `create_or_replace_sales_tax`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'country_code' in params:
            path_params['countryCode'] = params['country_code']  # noqa: E501
        if 'jurisdiction_id' in params:
            path_params['jurisdictionId'] = params['jurisdiction_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_auth']  # noqa: E501

        return self.api_client.call_api(
            '/sales_tax/{countryCode}/{jurisdictionId}', 'PUT',
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

    def delete_sales_tax(self, country_code, jurisdiction_id, **kwargs):  # noqa: E501
        """delete_sales_tax  # noqa: E501

        This call deletes a sales tax table entry for a jurisdiction. Specify the jurisdiction to delete using the <b>countryCode</b> and <b>jurisdictionId</b> path parameters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_sales_tax(country_code, jurisdiction_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str country_code: This path parameter specifies the two-letter <a href=\"https://www.iso.org/iso-3166-country-codes.html\" title=\"https://www.iso.org\" target=\"_blank\">ISO 3166</a> code for the country whose sales tax table entry you want to delete. (required)
        :param str jurisdiction_id: This path parameter specifies the ID of the sales tax jurisdiction whose table entry you want to delete. Retrieve valid jurisdiction IDs using <b>getSalesTaxJurisdictions</b> in the Metadata API. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_sales_tax_with_http_info(country_code, jurisdiction_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_sales_tax_with_http_info(country_code, jurisdiction_id, **kwargs)  # noqa: E501
            return data

    def delete_sales_tax_with_http_info(self, country_code, jurisdiction_id, **kwargs):  # noqa: E501
        """delete_sales_tax  # noqa: E501

        This call deletes a sales tax table entry for a jurisdiction. Specify the jurisdiction to delete using the <b>countryCode</b> and <b>jurisdictionId</b> path parameters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_sales_tax_with_http_info(country_code, jurisdiction_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str country_code: This path parameter specifies the two-letter <a href=\"https://www.iso.org/iso-3166-country-codes.html\" title=\"https://www.iso.org\" target=\"_blank\">ISO 3166</a> code for the country whose sales tax table entry you want to delete. (required)
        :param str jurisdiction_id: This path parameter specifies the ID of the sales tax jurisdiction whose table entry you want to delete. Retrieve valid jurisdiction IDs using <b>getSalesTaxJurisdictions</b> in the Metadata API. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['country_code', 'jurisdiction_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_sales_tax" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'country_code' is set
        if ('country_code' not in params or
                params['country_code'] is None):
            raise ValueError("Missing the required parameter `country_code` when calling `delete_sales_tax`")  # noqa: E501
        # verify the required parameter 'jurisdiction_id' is set
        if ('jurisdiction_id' not in params or
                params['jurisdiction_id'] is None):
            raise ValueError("Missing the required parameter `jurisdiction_id` when calling `delete_sales_tax`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'country_code' in params:
            path_params['countryCode'] = params['country_code']  # noqa: E501
        if 'jurisdiction_id' in params:
            path_params['jurisdictionId'] = params['jurisdiction_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['api_auth']  # noqa: E501

        return self.api_client.call_api(
            '/sales_tax/{countryCode}/{jurisdictionId}', 'DELETE',
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

    def get_sales_tax(self, country_code, jurisdiction_id, **kwargs):  # noqa: E501
        """get_sales_tax  # noqa: E501

        This call gets the current sales tax table entry for a specific tax jurisdiction. Specify the jurisdiction to retrieve using the <b>countryCode</b> and <b>jurisdictionId</b> path parameters. All four response fields will be returned if a sales tax entry exists for the tax jurisdiction. Otherwise, the response will be returned as empty.<br/><br/><span class=\"tablenote\"><b>Important!</b> In most US states and territories, eBay now 'collects and remits' sales tax, so sellers can no longer configure sales tax rates for these states/territories.</span>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sales_tax(country_code, jurisdiction_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str country_code: This path parameter specifies the two-letter <a href=\"https://www.iso.org/iso-3166-country-codes.html\" title=\"https://www.iso.org\" target=\"_blank\">ISO 3166</a> code for the country whose sales tax table you want to retrieve. (required)
        :param str jurisdiction_id: This path parameter specifies the ID of the sales tax jurisdiction for the tax table entry you want to retrieve. Retrieve valid jurisdiction IDs using <b>getSalesTaxJurisdictions</b> in the Metadata API. (required)
        :return: SalesTax
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_sales_tax_with_http_info(country_code, jurisdiction_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_sales_tax_with_http_info(country_code, jurisdiction_id, **kwargs)  # noqa: E501
            return data

    def get_sales_tax_with_http_info(self, country_code, jurisdiction_id, **kwargs):  # noqa: E501
        """get_sales_tax  # noqa: E501

        This call gets the current sales tax table entry for a specific tax jurisdiction. Specify the jurisdiction to retrieve using the <b>countryCode</b> and <b>jurisdictionId</b> path parameters. All four response fields will be returned if a sales tax entry exists for the tax jurisdiction. Otherwise, the response will be returned as empty.<br/><br/><span class=\"tablenote\"><b>Important!</b> In most US states and territories, eBay now 'collects and remits' sales tax, so sellers can no longer configure sales tax rates for these states/territories.</span>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sales_tax_with_http_info(country_code, jurisdiction_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str country_code: This path parameter specifies the two-letter <a href=\"https://www.iso.org/iso-3166-country-codes.html\" title=\"https://www.iso.org\" target=\"_blank\">ISO 3166</a> code for the country whose sales tax table you want to retrieve. (required)
        :param str jurisdiction_id: This path parameter specifies the ID of the sales tax jurisdiction for the tax table entry you want to retrieve. Retrieve valid jurisdiction IDs using <b>getSalesTaxJurisdictions</b> in the Metadata API. (required)
        :return: SalesTax
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['country_code', 'jurisdiction_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sales_tax" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'country_code' is set
        if ('country_code' not in params or
                params['country_code'] is None):
            raise ValueError("Missing the required parameter `country_code` when calling `get_sales_tax`")  # noqa: E501
        # verify the required parameter 'jurisdiction_id' is set
        if ('jurisdiction_id' not in params or
                params['jurisdiction_id'] is None):
            raise ValueError("Missing the required parameter `jurisdiction_id` when calling `get_sales_tax`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'country_code' in params:
            path_params['countryCode'] = params['country_code']  # noqa: E501
        if 'jurisdiction_id' in params:
            path_params['jurisdictionId'] = params['jurisdiction_id']  # noqa: E501

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
            '/sales_tax/{countryCode}/{jurisdictionId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SalesTax',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_sales_taxes(self, country_code, **kwargs):  # noqa: E501
        """get_sales_taxes  # noqa: E501

        Use this call to retrieve all sales tax table entries that the seller has defined for a specific country. All four response fields will be returned for each tax jurisdiction that matches the search criteria. <br/><br/><span class=\"tablenote\"><b>Important!</b> In most US states and territories, eBay now 'collects and remits' sales tax, so sellers can no longer configure sales tax rates for these states/territories.</span>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sales_taxes(country_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str country_code: This path parameter specifies the two-letter <a href=\"https://www.iso.org/iso-3166-country-codes.html\" title=\"https://www.iso.org\" target=\"_blank\">ISO 3166</a> code for the country whose tax table you want to retrieve. For implementation help, refer to eBay API documentation at https://developer.ebay.com/api-docs/sell/account/types/ba:CountryCodeEnum (required)
        :return: SalesTaxes
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_sales_taxes_with_http_info(country_code, **kwargs)  # noqa: E501
        else:
            (data) = self.get_sales_taxes_with_http_info(country_code, **kwargs)  # noqa: E501
            return data

    def get_sales_taxes_with_http_info(self, country_code, **kwargs):  # noqa: E501
        """get_sales_taxes  # noqa: E501

        Use this call to retrieve all sales tax table entries that the seller has defined for a specific country. All four response fields will be returned for each tax jurisdiction that matches the search criteria. <br/><br/><span class=\"tablenote\"><b>Important!</b> In most US states and territories, eBay now 'collects and remits' sales tax, so sellers can no longer configure sales tax rates for these states/territories.</span>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sales_taxes_with_http_info(country_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str country_code: This path parameter specifies the two-letter <a href=\"https://www.iso.org/iso-3166-country-codes.html\" title=\"https://www.iso.org\" target=\"_blank\">ISO 3166</a> code for the country whose tax table you want to retrieve. For implementation help, refer to eBay API documentation at https://developer.ebay.com/api-docs/sell/account/types/ba:CountryCodeEnum (required)
        :return: SalesTaxes
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['country_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sales_taxes" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'country_code' is set
        if ('country_code' not in params or
                params['country_code'] is None):
            raise ValueError("Missing the required parameter `country_code` when calling `get_sales_taxes`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'country_code' in params:
            query_params.append(('country_code', params['country_code']))  # noqa: E501

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
            '/sales_tax', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SalesTaxes',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
