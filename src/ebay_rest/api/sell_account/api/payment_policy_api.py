# coding: utf-8

"""
    Account API

    The <b>Account API</b> gives sellers the ability to configure their eBay seller accounts, including the seller's policies (the Fulfillment Policy, Payment Policy, and Return Policy), opt in and out of eBay seller programs, configure sales tax tables, and get account information.  <br><br>For details on the availability of the methods in this API, see <a href=\"/api-docs/sell/account/overview.html#requirements\">Account API requirements and restrictions</a>.  # noqa: E501

    OpenAPI spec version: v1.6.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ...sell_account.api_client import ApiClient


class PaymentPolicyApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_payment_policy(self, body, **kwargs):  # noqa: E501
        """create_payment_policy  # noqa: E501

        This method creates a new payment policy where the policy encapsulates seller's terms for purchase payments.  <br><br>Each policy targets a <b>marketplaceId</b> and <code>categoryTypes.</code><b>name</b> combination and you can create multiple policies for each combination. Be aware that some marketplaces require a specific payment policy for vehicle listings.  <br><br>A successful request returns the URI to the new policy in the <b>Location</b> response header and the ID for the new policy is returned in the response payload.  <p class=\"tablenote\"><b>Tip:</b> For details on creating and using the business policies supported by the Account API, see <a href=\"/api-docs/sell/static/seller-accounts/business-policies.html\">eBay business policies</a>.</p>  <p><b>Marketplaces and locales</b></p>  <p>Policy instructions can be localized by providing a locale in the <code>Accept-Language</code> HTTP request header. For example, the following setting displays field values from the request body in German: <code>Accept-Language: de-DE</code>.</p>  <p>Target the specific locale of a marketplace that supports multiple locales using the <code>Content-Language</code> request header. For example, target the French locale of the Canadian marketplace by specifying the <code>fr-CA</code> locale for <code>Content-Language</code>. Likewise, target the Dutch locale of the Belgium marketplace by setting <code>Content-Language: nl-BE</code>.</p> <p class=\"tablenote\"><b>Tip:</b> For details on headers, see <a href=\"/api-docs/static/rest-request-components.html#HTTP\">HTTP request headers</a>.</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_payment_policy(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PaymentPolicyRequest body: Payment policy request (required)
        :return: SetPaymentPolicyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_payment_policy_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_payment_policy_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_payment_policy_with_http_info(self, body, **kwargs):  # noqa: E501
        """create_payment_policy  # noqa: E501

        This method creates a new payment policy where the policy encapsulates seller's terms for purchase payments.  <br><br>Each policy targets a <b>marketplaceId</b> and <code>categoryTypes.</code><b>name</b> combination and you can create multiple policies for each combination. Be aware that some marketplaces require a specific payment policy for vehicle listings.  <br><br>A successful request returns the URI to the new policy in the <b>Location</b> response header and the ID for the new policy is returned in the response payload.  <p class=\"tablenote\"><b>Tip:</b> For details on creating and using the business policies supported by the Account API, see <a href=\"/api-docs/sell/static/seller-accounts/business-policies.html\">eBay business policies</a>.</p>  <p><b>Marketplaces and locales</b></p>  <p>Policy instructions can be localized by providing a locale in the <code>Accept-Language</code> HTTP request header. For example, the following setting displays field values from the request body in German: <code>Accept-Language: de-DE</code>.</p>  <p>Target the specific locale of a marketplace that supports multiple locales using the <code>Content-Language</code> request header. For example, target the French locale of the Canadian marketplace by specifying the <code>fr-CA</code> locale for <code>Content-Language</code>. Likewise, target the Dutch locale of the Belgium marketplace by setting <code>Content-Language: nl-BE</code>.</p> <p class=\"tablenote\"><b>Tip:</b> For details on headers, see <a href=\"/api-docs/static/rest-request-components.html#HTTP\">HTTP request headers</a>.</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_payment_policy_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PaymentPolicyRequest body: Payment policy request (required)
        :return: SetPaymentPolicyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_payment_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_payment_policy`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

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
            '/payment_policy', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SetPaymentPolicyResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_payment_policy(self, payment_policy_id, **kwargs):  # noqa: E501
        """delete_payment_policy  # noqa: E501

        This method deletes a payment policy. Supply the ID of the policy you want to delete in the <b>paymentPolicyId</b> path parameter. Note that you cannot delete the default payment policy.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_payment_policy(payment_policy_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str payment_policy_id: This path parameter specifies the ID of the payment policy you want to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_payment_policy_with_http_info(payment_policy_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_payment_policy_with_http_info(payment_policy_id, **kwargs)  # noqa: E501
            return data

    def delete_payment_policy_with_http_info(self, payment_policy_id, **kwargs):  # noqa: E501
        """delete_payment_policy  # noqa: E501

        This method deletes a payment policy. Supply the ID of the policy you want to delete in the <b>paymentPolicyId</b> path parameter. Note that you cannot delete the default payment policy.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_payment_policy_with_http_info(payment_policy_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str payment_policy_id: This path parameter specifies the ID of the payment policy you want to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['payment_policy_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_payment_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'payment_policy_id' is set
        if ('payment_policy_id' not in params or
                params['payment_policy_id'] is None):
            raise ValueError("Missing the required parameter `payment_policy_id` when calling `delete_payment_policy`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'payment_policy_id' in params:
            path_params['payment_policy_id'] = params['payment_policy_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['api_auth']  # noqa: E501

        return self.api_client.call_api(
            '/payment_policy/{payment_policy_id}', 'DELETE',
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

    def get_payment_policies(self, marketplace_id, **kwargs):  # noqa: E501
        """get_payment_policies  # noqa: E501

        This method retrieves all the payment policies configured for the marketplace you specify using the <code>marketplace_id</code> query parameter.  <br><br><b>Marketplaces and locales</b>  <br><br>Get the correct policies for a marketplace that supports multiple locales using the <code>Content-Language</code> request header. For example, get the policies for the French locale of the Canadian marketplace by specifying <code>fr-CA</code> for the <code>Content-Language</code> header. Likewise, target the Dutch locale of the Belgium marketplace by setting <code>Content-Language: nl-BE</code>. For details on header values, see <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank\">HTTP request headers</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_payment_policies(marketplace_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str marketplace_id: This query parameter specifies the eBay marketplace of the policies you want to retrieve. For implementation help, refer to eBay API documentation at https://developer.ebay.com/api-docs/sell/account/types/ba:MarketplaceIdEnum (required)
        :return: PaymentPolicyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_payment_policies_with_http_info(marketplace_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_payment_policies_with_http_info(marketplace_id, **kwargs)  # noqa: E501
            return data

    def get_payment_policies_with_http_info(self, marketplace_id, **kwargs):  # noqa: E501
        """get_payment_policies  # noqa: E501

        This method retrieves all the payment policies configured for the marketplace you specify using the <code>marketplace_id</code> query parameter.  <br><br><b>Marketplaces and locales</b>  <br><br>Get the correct policies for a marketplace that supports multiple locales using the <code>Content-Language</code> request header. For example, get the policies for the French locale of the Canadian marketplace by specifying <code>fr-CA</code> for the <code>Content-Language</code> header. Likewise, target the Dutch locale of the Belgium marketplace by setting <code>Content-Language: nl-BE</code>. For details on header values, see <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank\">HTTP request headers</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_payment_policies_with_http_info(marketplace_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str marketplace_id: This query parameter specifies the eBay marketplace of the policies you want to retrieve. For implementation help, refer to eBay API documentation at https://developer.ebay.com/api-docs/sell/account/types/ba:MarketplaceIdEnum (required)
        :return: PaymentPolicyResponse
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
                    " to method get_payment_policies" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'marketplace_id' is set
        if ('marketplace_id' not in params or
                params['marketplace_id'] is None):
            raise ValueError("Missing the required parameter `marketplace_id` when calling `get_payment_policies`")  # noqa: E501

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
            '/payment_policy', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaymentPolicyResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_payment_policy(self, payment_policy_id, **kwargs):  # noqa: E501
        """get_payment_policy  # noqa: E501

        This method retrieves the complete details of a payment policy. Supply the ID of the policy you want to retrieve using the <b>paymentPolicyId</b> path parameter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_payment_policy(payment_policy_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str payment_policy_id: This path parameter specifies the ID of the payment policy you want to retrieve. (required)
        :return: PaymentPolicy
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_payment_policy_with_http_info(payment_policy_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_payment_policy_with_http_info(payment_policy_id, **kwargs)  # noqa: E501
            return data

    def get_payment_policy_with_http_info(self, payment_policy_id, **kwargs):  # noqa: E501
        """get_payment_policy  # noqa: E501

        This method retrieves the complete details of a payment policy. Supply the ID of the policy you want to retrieve using the <b>paymentPolicyId</b> path parameter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_payment_policy_with_http_info(payment_policy_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str payment_policy_id: This path parameter specifies the ID of the payment policy you want to retrieve. (required)
        :return: PaymentPolicy
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['payment_policy_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_payment_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'payment_policy_id' is set
        if ('payment_policy_id' not in params or
                params['payment_policy_id'] is None):
            raise ValueError("Missing the required parameter `payment_policy_id` when calling `get_payment_policy`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'payment_policy_id' in params:
            path_params['payment_policy_id'] = params['payment_policy_id']  # noqa: E501

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
            '/payment_policy/{payment_policy_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaymentPolicy',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_payment_policy_by_name(self, marketplace_id, name, **kwargs):  # noqa: E501
        """get_payment_policy_by_name  # noqa: E501

        This method retrieves the complete details of a single payment policy. Supply both the policy <code>name</code> and its associated <code>marketplace_id</code> in the request query parameters.   <br><br><b>Marketplaces and locales</b>  <br><br>Get the correct policy for a marketplace that supports multiple locales using the <code>Content-Language</code> request header. For example, get a policy for the French locale of the Canadian marketplace by specifying <code>fr-CA</code> for the <code>Content-Language</code> header. Likewise, target the Dutch locale of the Belgium marketplace by setting <code>Content-Language: nl-BE</code>. For details on header values, see <a href=\"/api-docs/static/rest-request-components.html#HTTP\">HTTP request headers</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_payment_policy_by_name(marketplace_id, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str marketplace_id: This query parameter specifies the eBay marketplace of the policy you want to retrieve. For implementation help, refer to eBay API documentation at https://developer.ebay.com/api-docs/sell/account/types/ba:MarketplaceIdEnum (required)
        :param str name: This query parameter specifies the user-defined name of the payment policy you want to retrieve. (required)
        :return: PaymentPolicy
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_payment_policy_by_name_with_http_info(marketplace_id, name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_payment_policy_by_name_with_http_info(marketplace_id, name, **kwargs)  # noqa: E501
            return data

    def get_payment_policy_by_name_with_http_info(self, marketplace_id, name, **kwargs):  # noqa: E501
        """get_payment_policy_by_name  # noqa: E501

        This method retrieves the complete details of a single payment policy. Supply both the policy <code>name</code> and its associated <code>marketplace_id</code> in the request query parameters.   <br><br><b>Marketplaces and locales</b>  <br><br>Get the correct policy for a marketplace that supports multiple locales using the <code>Content-Language</code> request header. For example, get a policy for the French locale of the Canadian marketplace by specifying <code>fr-CA</code> for the <code>Content-Language</code> header. Likewise, target the Dutch locale of the Belgium marketplace by setting <code>Content-Language: nl-BE</code>. For details on header values, see <a href=\"/api-docs/static/rest-request-components.html#HTTP\">HTTP request headers</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_payment_policy_by_name_with_http_info(marketplace_id, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str marketplace_id: This query parameter specifies the eBay marketplace of the policy you want to retrieve. For implementation help, refer to eBay API documentation at https://developer.ebay.com/api-docs/sell/account/types/ba:MarketplaceIdEnum (required)
        :param str name: This query parameter specifies the user-defined name of the payment policy you want to retrieve. (required)
        :return: PaymentPolicy
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
                    " to method get_payment_policy_by_name" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'marketplace_id' is set
        if ('marketplace_id' not in params or
                params['marketplace_id'] is None):
            raise ValueError("Missing the required parameter `marketplace_id` when calling `get_payment_policy_by_name`")  # noqa: E501
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_payment_policy_by_name`")  # noqa: E501

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
            '/payment_policy/get_by_policy_name', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaymentPolicy',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_payment_policy(self, body, payment_policy_id, **kwargs):  # noqa: E501
        """update_payment_policy  # noqa: E501

        This method updates an existing payment policy. Specify the policy you want to update using the <b>payment_policy_id</b> path parameter. Supply a complete policy payload with the updates you want to make; this call overwrites the existing policy with the new details specified in the payload.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_payment_policy(body, payment_policy_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PaymentPolicyRequest body: Payment policy request (required)
        :param str payment_policy_id: This path parameter specifies the ID of the payment policy you want to update. (required)
        :return: SetPaymentPolicyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_payment_policy_with_http_info(body, payment_policy_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_payment_policy_with_http_info(body, payment_policy_id, **kwargs)  # noqa: E501
            return data

    def update_payment_policy_with_http_info(self, body, payment_policy_id, **kwargs):  # noqa: E501
        """update_payment_policy  # noqa: E501

        This method updates an existing payment policy. Specify the policy you want to update using the <b>payment_policy_id</b> path parameter. Supply a complete policy payload with the updates you want to make; this call overwrites the existing policy with the new details specified in the payload.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_payment_policy_with_http_info(body, payment_policy_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PaymentPolicyRequest body: Payment policy request (required)
        :param str payment_policy_id: This path parameter specifies the ID of the payment policy you want to update. (required)
        :return: SetPaymentPolicyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'payment_policy_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_payment_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_payment_policy`")  # noqa: E501
        # verify the required parameter 'payment_policy_id' is set
        if ('payment_policy_id' not in params or
                params['payment_policy_id'] is None):
            raise ValueError("Missing the required parameter `payment_policy_id` when calling `update_payment_policy`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'payment_policy_id' in params:
            path_params['payment_policy_id'] = params['payment_policy_id']  # noqa: E501

        query_params = []

        header_params = {}

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
            '/payment_policy/{payment_policy_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SetPaymentPolicyResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
