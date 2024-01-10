# coding: utf-8

"""
    Account API

    The <b>Account API</b> gives sellers the ability to configure their eBay seller accounts, including the seller's policies (eBay business policies and seller-defined custom policies), opt in and out of eBay seller programs, configure sales tax tables, and get account information.  <br><br>For details on the availability of the methods in this API, see <a href=\"/api-docs/sell/account/overview.html#requirements\">Account API requirements and restrictions</a>.  # noqa: E501

    OpenAPI spec version: v1.9.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ...sell_account.api_client import ApiClient


class FulfillmentPolicyApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_fulfillment_policy(self, body, content_type, **kwargs):  # noqa: E501
        """create_fulfillment_policy  # noqa: E501

        This method creates a new fulfillment policy where the policy encapsulates seller's terms for fulfilling item purchases. Fulfillment policies include the shipment options that the seller offers to buyers.  <br><br>Each policy targets a specific eBay marketplace and a category group type, and you can create multiple policies for each combination. <br><br>A successful request returns the <b>getFulfillmentPolicy</b> URI to the new policy in the <b>Location</b> response header and the ID for the new policy is returned in the response payload.  <p class=\"tablenote\"><b>Tip:</b> For details on creating and using the business policies supported by the Account API, see <a href=\"/api-docs/sell/static/seller-accounts/business-policies.html\">eBay business policies</a>.</p>  <p><b>Using the eBay standard envelope service (eSE)</b></p><p>The eBay standard envelope service (eSE) is a domestic envelope service with tracking through eBay. This service applies to specific sub-categories of <b>Trading Cards</b>, and to coins & paper money, postcards, stamps, patches, and similar <a href=\"https://www.ebay.com/sellercenter/shipping/choosing-a-carrier-and-service/ebay-standard-envelope#eligible-categories\" target=\"_blank \">eligible categories</a>, and is only available on the US marketplace. To use this service, send envelopes using the USPS mail and set the <b>shippingServiceCode</b> field to <code>US_eBayStandardEnvelope</code>. See <a href=\"/api-docs/sell/static/seller-accounts/using-the-ebay-standard-envelope-service.html\" target=\"_blank\">Using eBay standard envelope (eSE) service</a> for details. See <a href=\"https://pages.ebay.com/seller-center/shipping/ebay-standard-envelope.html#lower-cost-way\" target=\"_blank \">eBay standard envelope</a> for additional details, restrictions, and an <a href=\"https://ir.ebaystatic.com/pictures/sc/Shipping/ebay_standard_envelope_template.pdf\" target=\"_blank \">envelope size template</a>.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_fulfillment_policy(body, content_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FulfillmentPolicyRequest body: Request to create a seller account fulfillment policy. (required)
        :param str content_type: This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br> For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>. (required)
        :return: SetFulfillmentPolicyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_fulfillment_policy_with_http_info(body, content_type, **kwargs)  # noqa: E501
        else:
            (data) = self.create_fulfillment_policy_with_http_info(body, content_type, **kwargs)  # noqa: E501
            return data

    def create_fulfillment_policy_with_http_info(self, body, content_type, **kwargs):  # noqa: E501
        """create_fulfillment_policy  # noqa: E501

        This method creates a new fulfillment policy where the policy encapsulates seller's terms for fulfilling item purchases. Fulfillment policies include the shipment options that the seller offers to buyers.  <br><br>Each policy targets a specific eBay marketplace and a category group type, and you can create multiple policies for each combination. <br><br>A successful request returns the <b>getFulfillmentPolicy</b> URI to the new policy in the <b>Location</b> response header and the ID for the new policy is returned in the response payload.  <p class=\"tablenote\"><b>Tip:</b> For details on creating and using the business policies supported by the Account API, see <a href=\"/api-docs/sell/static/seller-accounts/business-policies.html\">eBay business policies</a>.</p>  <p><b>Using the eBay standard envelope service (eSE)</b></p><p>The eBay standard envelope service (eSE) is a domestic envelope service with tracking through eBay. This service applies to specific sub-categories of <b>Trading Cards</b>, and to coins & paper money, postcards, stamps, patches, and similar <a href=\"https://www.ebay.com/sellercenter/shipping/choosing-a-carrier-and-service/ebay-standard-envelope#eligible-categories\" target=\"_blank \">eligible categories</a>, and is only available on the US marketplace. To use this service, send envelopes using the USPS mail and set the <b>shippingServiceCode</b> field to <code>US_eBayStandardEnvelope</code>. See <a href=\"/api-docs/sell/static/seller-accounts/using-the-ebay-standard-envelope-service.html\" target=\"_blank\">Using eBay standard envelope (eSE) service</a> for details. See <a href=\"https://pages.ebay.com/seller-center/shipping/ebay-standard-envelope.html#lower-cost-way\" target=\"_blank \">eBay standard envelope</a> for additional details, restrictions, and an <a href=\"https://ir.ebaystatic.com/pictures/sc/Shipping/ebay_standard_envelope_template.pdf\" target=\"_blank \">envelope size template</a>.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_fulfillment_policy_with_http_info(body, content_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FulfillmentPolicyRequest body: Request to create a seller account fulfillment policy. (required)
        :param str content_type: This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br> For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>. (required)
        :return: SetFulfillmentPolicyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'content_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_fulfillment_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_fulfillment_policy`")  # noqa: E501
        # verify the required parameter 'content_type' is set
        if ('content_type' not in params or
                params['content_type'] is None):
            raise ValueError("Missing the required parameter `content_type` when calling `create_fulfillment_policy`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'content_type' in params:
            header_params['Content-Type'] = params['content_type']  # noqa: E501

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
            '/fulfillment_policy/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SetFulfillmentPolicyResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_fulfillment_policy(self, fulfillment_policy_id, **kwargs):  # noqa: E501
        """delete_fulfillment_policy  # noqa: E501

        This method deletes a fulfillment policy. Supply the ID of the policy you want to delete in the <b>fulfillmentPolicyId</b> path parameter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_fulfillment_policy(fulfillment_policy_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str fulfillment_policy_id: This path parameter specifies the ID of the fulfillment policy to delete.<br><br> This ID can be retrieved for a fulfillment policy by using the <a href=\"/api-docs/sell/account/resources/fulfillment_policy/methods/getFulfillmentPolicies\" target=\"_blank \">getFulfillmentPolicies</a> method. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_fulfillment_policy_with_http_info(fulfillment_policy_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_fulfillment_policy_with_http_info(fulfillment_policy_id, **kwargs)  # noqa: E501
            return data

    def delete_fulfillment_policy_with_http_info(self, fulfillment_policy_id, **kwargs):  # noqa: E501
        """delete_fulfillment_policy  # noqa: E501

        This method deletes a fulfillment policy. Supply the ID of the policy you want to delete in the <b>fulfillmentPolicyId</b> path parameter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_fulfillment_policy_with_http_info(fulfillment_policy_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str fulfillment_policy_id: This path parameter specifies the ID of the fulfillment policy to delete.<br><br> This ID can be retrieved for a fulfillment policy by using the <a href=\"/api-docs/sell/account/resources/fulfillment_policy/methods/getFulfillmentPolicies\" target=\"_blank \">getFulfillmentPolicies</a> method. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fulfillment_policy_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_fulfillment_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'fulfillment_policy_id' is set
        if ('fulfillment_policy_id' not in params or
                params['fulfillment_policy_id'] is None):
            raise ValueError("Missing the required parameter `fulfillment_policy_id` when calling `delete_fulfillment_policy`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'fulfillment_policy_id' in params:
            path_params['fulfillmentPolicyId'] = params['fulfillment_policy_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['api_auth']  # noqa: E501

        return self.api_client.call_api(
            '/fulfillment_policy/{fulfillmentPolicyId}', 'DELETE',
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

    def get_fulfillment_policies(self, marketplace_id, **kwargs):  # noqa: E501
        """get_fulfillment_policies  # noqa: E501

        This method retrieves all the fulfillment policies configured for the marketplace you specify using the <code>marketplace_id</code> query parameter.  <br><br><b>Marketplaces and locales</b>  <br><br>Get the correct policies for a marketplace that supports multiple locales using the <code>Content-Language</code> request header. For example, get the policies for the French locale of the Canadian marketplace by specifying <code>fr-CA</code> for the <code>Content-Language</code> header. Likewise, target the Dutch locale of the Belgium marketplace by setting <code>Content-Language: nl-BE</code>. For details on header values, see <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank\">HTTP request headers</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_fulfillment_policies(marketplace_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str marketplace_id: This query parameter specifies the eBay marketplace of the policies you want to retrieve. For implementation help, refer to eBay API documentation at https://developer.ebay.com/api-docs/sell/account/types/ba:MarketplaceIdEnum (required)
        :return: FulfillmentPolicyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_fulfillment_policies_with_http_info(marketplace_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_fulfillment_policies_with_http_info(marketplace_id, **kwargs)  # noqa: E501
            return data

    def get_fulfillment_policies_with_http_info(self, marketplace_id, **kwargs):  # noqa: E501
        """get_fulfillment_policies  # noqa: E501

        This method retrieves all the fulfillment policies configured for the marketplace you specify using the <code>marketplace_id</code> query parameter.  <br><br><b>Marketplaces and locales</b>  <br><br>Get the correct policies for a marketplace that supports multiple locales using the <code>Content-Language</code> request header. For example, get the policies for the French locale of the Canadian marketplace by specifying <code>fr-CA</code> for the <code>Content-Language</code> header. Likewise, target the Dutch locale of the Belgium marketplace by setting <code>Content-Language: nl-BE</code>. For details on header values, see <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank\">HTTP request headers</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_fulfillment_policies_with_http_info(marketplace_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str marketplace_id: This query parameter specifies the eBay marketplace of the policies you want to retrieve. For implementation help, refer to eBay API documentation at https://developer.ebay.com/api-docs/sell/account/types/ba:MarketplaceIdEnum (required)
        :return: FulfillmentPolicyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['marketplace_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_fulfillment_policies" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'marketplace_id' is set
        if ('marketplace_id' not in params or
                params['marketplace_id'] is None):
            raise ValueError("Missing the required parameter `marketplace_id` when calling `get_fulfillment_policies`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'marketplace_id' in params:
            query_params.append(('marketplace_id', params['marketplace_id']))  # noqa: E501

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
            '/fulfillment_policy', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FulfillmentPolicyResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_fulfillment_policy(self, fulfillment_policy_id, **kwargs):  # noqa: E501
        """get_fulfillment_policy  # noqa: E501

        This method retrieves the complete details of a fulfillment policy. Supply the ID of the policy you want to retrieve using the <b>fulfillmentPolicyId</b> path parameter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_fulfillment_policy(fulfillment_policy_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str fulfillment_policy_id: This path parameter specifies the ID of the fulfillment policy you want to retrieve.<br><br> This ID can be retrieved for a fulfillment policy by using the <a href=\"/api-docs/sell/account/resources/fulfillment_policy/methods/getFulfillmentPolicies\" target=\"_blank \">getFulfillmentPolicies</a> method. (required)
        :return: FulfillmentPolicy
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_fulfillment_policy_with_http_info(fulfillment_policy_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_fulfillment_policy_with_http_info(fulfillment_policy_id, **kwargs)  # noqa: E501
            return data

    def get_fulfillment_policy_with_http_info(self, fulfillment_policy_id, **kwargs):  # noqa: E501
        """get_fulfillment_policy  # noqa: E501

        This method retrieves the complete details of a fulfillment policy. Supply the ID of the policy you want to retrieve using the <b>fulfillmentPolicyId</b> path parameter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_fulfillment_policy_with_http_info(fulfillment_policy_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str fulfillment_policy_id: This path parameter specifies the ID of the fulfillment policy you want to retrieve.<br><br> This ID can be retrieved for a fulfillment policy by using the <a href=\"/api-docs/sell/account/resources/fulfillment_policy/methods/getFulfillmentPolicies\" target=\"_blank \">getFulfillmentPolicies</a> method. (required)
        :return: FulfillmentPolicy
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fulfillment_policy_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_fulfillment_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'fulfillment_policy_id' is set
        if ('fulfillment_policy_id' not in params or
                params['fulfillment_policy_id'] is None):
            raise ValueError("Missing the required parameter `fulfillment_policy_id` when calling `get_fulfillment_policy`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'fulfillment_policy_id' in params:
            path_params['fulfillmentPolicyId'] = params['fulfillment_policy_id']  # noqa: E501

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
            '/fulfillment_policy/{fulfillmentPolicyId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FulfillmentPolicy',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_fulfillment_policy_by_name(self, marketplace_id, name, **kwargs):  # noqa: E501
        """get_fulfillment_policy_by_name  # noqa: E501

        This method retrieves the details for a specific fulfillment policy. In the request, supply both the policy <code>name</code> and its associated <code>marketplace_id</code> as query parameters.   <br><br><b>Marketplaces and locales</b>  <br><br>Get the correct policy for a marketplace that supports multiple locales using the <code>Content-Language</code> request header. For example, get a policy for the French locale of the Canadian marketplace by specifying <code>fr-CA</code> for the <code>Content-Language</code> header. Likewise, target the Dutch locale of the Belgium marketplace by setting <code>Content-Language: nl-BE</code>. For details on header values, see <a href=\"/api-docs/static/rest-request-components.html#HTTP\">HTTP request headers</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_fulfillment_policy_by_name(marketplace_id, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str marketplace_id: This query parameter specifies the eBay marketplace of the policy you want to retrieve. For implementation help, refer to eBay API documentation at https://developer.ebay.com/api-docs/sell/account/types/ba:MarketplaceIdEnum (required)
        :param str name: This query parameter specifies the seller-defined name of the fulfillment policy you want to retrieve.<br><br>This value can be retrieved for a fulfillment policy by using the <a href=\"/api-docs/sell/account/resources/fulfillment_policy/methods/getFulfillmentPolicies\" target=\"_blank \">getFulfillmentPolicies</a> method. (required)
        :return: FulfillmentPolicy
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_fulfillment_policy_by_name_with_http_info(marketplace_id, name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_fulfillment_policy_by_name_with_http_info(marketplace_id, name, **kwargs)  # noqa: E501
            return data

    def get_fulfillment_policy_by_name_with_http_info(self, marketplace_id, name, **kwargs):  # noqa: E501
        """get_fulfillment_policy_by_name  # noqa: E501

        This method retrieves the details for a specific fulfillment policy. In the request, supply both the policy <code>name</code> and its associated <code>marketplace_id</code> as query parameters.   <br><br><b>Marketplaces and locales</b>  <br><br>Get the correct policy for a marketplace that supports multiple locales using the <code>Content-Language</code> request header. For example, get a policy for the French locale of the Canadian marketplace by specifying <code>fr-CA</code> for the <code>Content-Language</code> header. Likewise, target the Dutch locale of the Belgium marketplace by setting <code>Content-Language: nl-BE</code>. For details on header values, see <a href=\"/api-docs/static/rest-request-components.html#HTTP\">HTTP request headers</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_fulfillment_policy_by_name_with_http_info(marketplace_id, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str marketplace_id: This query parameter specifies the eBay marketplace of the policy you want to retrieve. For implementation help, refer to eBay API documentation at https://developer.ebay.com/api-docs/sell/account/types/ba:MarketplaceIdEnum (required)
        :param str name: This query parameter specifies the seller-defined name of the fulfillment policy you want to retrieve.<br><br>This value can be retrieved for a fulfillment policy by using the <a href=\"/api-docs/sell/account/resources/fulfillment_policy/methods/getFulfillmentPolicies\" target=\"_blank \">getFulfillmentPolicies</a> method. (required)
        :return: FulfillmentPolicy
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['marketplace_id', 'name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_fulfillment_policy_by_name" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'marketplace_id' is set
        if ('marketplace_id' not in params or
                params['marketplace_id'] is None):
            raise ValueError("Missing the required parameter `marketplace_id` when calling `get_fulfillment_policy_by_name`")  # noqa: E501
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_fulfillment_policy_by_name`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'marketplace_id' in params:
            query_params.append(('marketplace_id', params['marketplace_id']))  # noqa: E501
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501

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
            '/fulfillment_policy/get_by_policy_name', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FulfillmentPolicy',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_fulfillment_policy(self, body, content_type, fulfillment_policy_id, **kwargs):  # noqa: E501
        """update_fulfillment_policy  # noqa: E501

        This method updates an existing fulfillment policy. Specify the policy you want to update using the <b>fulfillment_policy_id</b> path parameter. Supply a complete policy payload with the updates you want to make; this call overwrites the existing policy with the new details specified in the payload.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_fulfillment_policy(body, content_type, fulfillment_policy_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FulfillmentPolicyRequest body: Fulfillment policy request (required)
        :param str content_type: This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br> For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>. (required)
        :param str fulfillment_policy_id: This path parameter specifies the ID of the fulfillment policy you want to update.<br><br>This ID can be retrieved for a specific fulfillment policy by using the <a href=\"/api-docs/sell/account/resources/fulfillment_policy/methods/getFulfillmentPolicies\" target=\"_blank \">getFulfillmentPolicies</a> method. (required)
        :return: SetFulfillmentPolicyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_fulfillment_policy_with_http_info(body, content_type, fulfillment_policy_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_fulfillment_policy_with_http_info(body, content_type, fulfillment_policy_id, **kwargs)  # noqa: E501
            return data

    def update_fulfillment_policy_with_http_info(self, body, content_type, fulfillment_policy_id, **kwargs):  # noqa: E501
        """update_fulfillment_policy  # noqa: E501

        This method updates an existing fulfillment policy. Specify the policy you want to update using the <b>fulfillment_policy_id</b> path parameter. Supply a complete policy payload with the updates you want to make; this call overwrites the existing policy with the new details specified in the payload.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_fulfillment_policy_with_http_info(body, content_type, fulfillment_policy_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FulfillmentPolicyRequest body: Fulfillment policy request (required)
        :param str content_type: This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br> For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>. (required)
        :param str fulfillment_policy_id: This path parameter specifies the ID of the fulfillment policy you want to update.<br><br>This ID can be retrieved for a specific fulfillment policy by using the <a href=\"/api-docs/sell/account/resources/fulfillment_policy/methods/getFulfillmentPolicies\" target=\"_blank \">getFulfillmentPolicies</a> method. (required)
        :return: SetFulfillmentPolicyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'content_type', 'fulfillment_policy_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_fulfillment_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_fulfillment_policy`")  # noqa: E501
        # verify the required parameter 'content_type' is set
        if ('content_type' not in params or
                params['content_type'] is None):
            raise ValueError("Missing the required parameter `content_type` when calling `update_fulfillment_policy`")  # noqa: E501
        # verify the required parameter 'fulfillment_policy_id' is set
        if ('fulfillment_policy_id' not in params or
                params['fulfillment_policy_id'] is None):
            raise ValueError("Missing the required parameter `fulfillment_policy_id` when calling `update_fulfillment_policy`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'fulfillment_policy_id' in params:
            path_params['fulfillmentPolicyId'] = params['fulfillment_policy_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'content_type' in params:
            header_params['Content-Type'] = params['content_type']  # noqa: E501

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
            '/fulfillment_policy/{fulfillmentPolicyId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SetFulfillmentPolicyResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
