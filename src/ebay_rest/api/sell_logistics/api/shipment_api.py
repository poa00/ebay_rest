# coding: utf-8

"""
    Logistics API

    <span class=\"tablenote\"><b>Note:</b> This is a <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited \" target=\"_blank\"> <img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"  alt=\"Limited Release\" />(Limited Release)</a> API available only to select developers approved by business units.</span><br /><br />The <b>Logistics API</b> resources offer the following capabilities: <ul><li><b>shipping_quote</b> &ndash; Consolidates into a list a set of live shipping rates, or quotes, from which you can select a rate to ship a package.</li> <li><b>shipment</b> &ndash; Creates a \"shipment\" for the selected shipping rate.</li></ul> Call <b>createShippingQuote</b> to get a list of live shipping rates. The rates returned are all valid for a specific time window and all quoted prices are at eBay-negotiated rates. <br><br>Select one of the live rates and using its associated <b>rateId</b>, create a \"shipment\" for the package by calling <b>createFromShippingQuote</b>. Creating a shipment completes an agreement, and the cost of the base service and any added shipping options are summed into the returned <b>totalShippingCost</b> value. This action also generates a shipping label that you can use to ship the package.  The total cost of the shipment is incurred when the package is shipped using the supplied shipping label.  <p class=\"tablenote\"><b>Important!</b> Sellers must set up a payment method via their eBay account before they can use the methods in this API to create a shipment and the associated shipping label.</p>  # noqa: E501

    OpenAPI spec version: v1_beta.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ...sell_logistics.api_client import ApiClient


class ShipmentApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def cancel_shipment(self, shipment_id, **kwargs):  # noqa: E501
        """cancel_shipment  # noqa: E501

        This method cancels the shipment associated with the specified shipment ID and the associated shipping label is deleted. When you cancel a shipment, the <b>totalShippingCost</b> of the canceled shipment is refunded to the account established by the user's billing agreement.  <br><br>Note that you cannot cancel a shipment if you have used the associated shipping label.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_shipment(shipment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str shipment_id: This path parameter specifies the unique eBay-assigned ID of the shipment to be canceled.<br><br>The <b>shipmentId</b> value is generated and returned by the <a href=\"/api-docs/sell/logistics/resources/shipment/methods/createFromShippingQuote\" target=\"_blank\">createFromShippingQuote</a> method. (required)
        :return: Shipment
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.cancel_shipment_with_http_info(shipment_id, **kwargs)  # noqa: E501
        else:
            (data) = self.cancel_shipment_with_http_info(shipment_id, **kwargs)  # noqa: E501
            return data

    def cancel_shipment_with_http_info(self, shipment_id, **kwargs):  # noqa: E501
        """cancel_shipment  # noqa: E501

        This method cancels the shipment associated with the specified shipment ID and the associated shipping label is deleted. When you cancel a shipment, the <b>totalShippingCost</b> of the canceled shipment is refunded to the account established by the user's billing agreement.  <br><br>Note that you cannot cancel a shipment if you have used the associated shipping label.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_shipment_with_http_info(shipment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str shipment_id: This path parameter specifies the unique eBay-assigned ID of the shipment to be canceled.<br><br>The <b>shipmentId</b> value is generated and returned by the <a href=\"/api-docs/sell/logistics/resources/shipment/methods/createFromShippingQuote\" target=\"_blank\">createFromShippingQuote</a> method. (required)
        :return: Shipment
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['shipment_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cancel_shipment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'shipment_id' is set
        if ('shipment_id' not in params or
                params['shipment_id'] is None):
            raise ValueError("Missing the required parameter `shipment_id` when calling `cancel_shipment`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'shipment_id' in params:
            path_params['shipmentId'] = params['shipment_id']  # noqa: E501

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
            '/shipment/{shipmentId}/cancel', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Shipment',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_from_shipping_quote(self, body, content_type, **kwargs):  # noqa: E501
        """create_from_shipping_quote  # noqa: E501

        This method creates a shipment based on the <b>shippingQuoteId</b> and <b>rateId</b> values supplied in the request. The rate identified by the <b>rateId</b> value specifies the carrier and service for the package shipment, and the rate ID must be contained in the shipping quote identified by the <b>shippingQuoteId</b> value. Call <b>createShippingQuote</b> to retrieve a set of live shipping rates.<br/><br/>When you create a shipment, eBay generates a shipping label that you can download and use to ship your package.<br/><br/>In a <b>createFromShippingQuote</b> request, sellers can include a list of shipping options they want to add to the base service quoted in the selected rate. The list of available shipping options is specific to each quoted rate and if available, the options are listed in the rate container of the shipping quote.<br/><br/>In addition to a configurable return-to location and other details about the shipment, the response to this method includes:<ul><li>The shipping carrier and service to be used for the package shipment</li><li>A list of selected shipping options, if any</li><li>The shipment tracking number</li><li>The total shipping cost (the sum cost of the base shipping service and any added options)</li></ul>When you create a shipment, your billing agreement account is charged the sum of the <b>baseShippingCost</b> and the total cost of any additional shipping options you might have selected. Use the URL returned in <b>labelDownloadURL</b> field, or call <b>downloadLabelFile</b> with the <b>shipmentId</b> value from the response, to download a shipping label for your package.<br/><br/><div class=\"msgbox_important\"><p class=\"msgbox_importantInDiv\" data-mc-autonum=\"&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;\"><span class=\"autonumber\"><span><b><span style=\"color: #dd1e31;\" class=\"mcFormatColor\">Important!</span></b></span></span> Sellers must set up their payment method before they can use this method to create a shipment and the associated shipping label.</p></div><h3 id=\"ba\">Set up a billing agreement</h3>Prior to using this method to create a shipment, sellers must first set up their billing agreement. Failure to do so will return <code>Error 90030 Payment could not be completed.</code><br/><br/>The preferred method for sellers to set up their billing agreement is to go to <a href=\"https://gslblui.ebay.com/gslblui/payments \" target=\"_blank\">Set up billing agreement</a> and follow the on-screen directions.<br/><br/>Alternatively, sellers can do the following:<ul><li>Go to https://www.ebay.com/ship/single/{order_id}, where {order_id} is that of the order for which the label is being printed.</li><li>When prompted, select <b>PayPal</b>.</li><li>Verify that <b>Save PayPal for future purchases</b> is selected.</li><li>Click <b>Set up Payments</b> which will open PayPal in a pop-up window.</li><li>Log in using <i>PayPal credentials</i>, and then follow the on-screen prompts to set up the billing agreement.</li><li>Once the agreement has been set up, sellers can leave this page as there is no need to actually print a label.</li></ul>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_from_shipping_quote(body, content_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateShipmentFromQuoteRequest body: The create shipment from quote request. (required)
        :param str content_type: This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br> For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>. (required)
        :return: Shipment
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_from_shipping_quote_with_http_info(body, content_type, **kwargs)  # noqa: E501
        else:
            (data) = self.create_from_shipping_quote_with_http_info(body, content_type, **kwargs)  # noqa: E501
            return data

    def create_from_shipping_quote_with_http_info(self, body, content_type, **kwargs):  # noqa: E501
        """create_from_shipping_quote  # noqa: E501

        This method creates a shipment based on the <b>shippingQuoteId</b> and <b>rateId</b> values supplied in the request. The rate identified by the <b>rateId</b> value specifies the carrier and service for the package shipment, and the rate ID must be contained in the shipping quote identified by the <b>shippingQuoteId</b> value. Call <b>createShippingQuote</b> to retrieve a set of live shipping rates.<br/><br/>When you create a shipment, eBay generates a shipping label that you can download and use to ship your package.<br/><br/>In a <b>createFromShippingQuote</b> request, sellers can include a list of shipping options they want to add to the base service quoted in the selected rate. The list of available shipping options is specific to each quoted rate and if available, the options are listed in the rate container of the shipping quote.<br/><br/>In addition to a configurable return-to location and other details about the shipment, the response to this method includes:<ul><li>The shipping carrier and service to be used for the package shipment</li><li>A list of selected shipping options, if any</li><li>The shipment tracking number</li><li>The total shipping cost (the sum cost of the base shipping service and any added options)</li></ul>When you create a shipment, your billing agreement account is charged the sum of the <b>baseShippingCost</b> and the total cost of any additional shipping options you might have selected. Use the URL returned in <b>labelDownloadURL</b> field, or call <b>downloadLabelFile</b> with the <b>shipmentId</b> value from the response, to download a shipping label for your package.<br/><br/><div class=\"msgbox_important\"><p class=\"msgbox_importantInDiv\" data-mc-autonum=\"&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;\"><span class=\"autonumber\"><span><b><span style=\"color: #dd1e31;\" class=\"mcFormatColor\">Important!</span></b></span></span> Sellers must set up their payment method before they can use this method to create a shipment and the associated shipping label.</p></div><h3 id=\"ba\">Set up a billing agreement</h3>Prior to using this method to create a shipment, sellers must first set up their billing agreement. Failure to do so will return <code>Error 90030 Payment could not be completed.</code><br/><br/>The preferred method for sellers to set up their billing agreement is to go to <a href=\"https://gslblui.ebay.com/gslblui/payments \" target=\"_blank\">Set up billing agreement</a> and follow the on-screen directions.<br/><br/>Alternatively, sellers can do the following:<ul><li>Go to https://www.ebay.com/ship/single/{order_id}, where {order_id} is that of the order for which the label is being printed.</li><li>When prompted, select <b>PayPal</b>.</li><li>Verify that <b>Save PayPal for future purchases</b> is selected.</li><li>Click <b>Set up Payments</b> which will open PayPal in a pop-up window.</li><li>Log in using <i>PayPal credentials</i>, and then follow the on-screen prompts to set up the billing agreement.</li><li>Once the agreement has been set up, sellers can leave this page as there is no need to actually print a label.</li></ul>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_from_shipping_quote_with_http_info(body, content_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateShipmentFromQuoteRequest body: The create shipment from quote request. (required)
        :param str content_type: This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br> For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>. (required)
        :return: Shipment
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
                    " to method create_from_shipping_quote" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_from_shipping_quote`")  # noqa: E501
        # verify the required parameter 'content_type' is set
        if ('content_type' not in params or
                params['content_type'] is None):
            raise ValueError("Missing the required parameter `content_type` when calling `create_from_shipping_quote`")  # noqa: E501

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
            '/shipment/create_from_shipping_quote', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Shipment',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def download_label_file(self, shipment_id, accept, **kwargs):  # noqa: E501
        """download_label_file  # noqa: E501

        This method returns the shipping label file that was generated for the <b>shipmentId</b> value specified in the request. Call <b>createFromShippingQuote</b> to generate a shipment ID.  <br><br>Use the <code>Accept</code> HTTP header to specify the format of the returned file. The default file format is a PDF file. <!-- Are other options available? -->  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_label_file(shipment_id, accept, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str shipment_id: This path parameter specifies the unique eBay-assigned identifier of the shipment associated with the shipping label you want to download.<br><br> The <b>shipmentId</b> value is generated and returned by the <a href=\"/api-docs/sell/logistics/resources/shipment/methods/createFromShippingQuote\" target=\"_blank\">createFromShippingQuote</a> method. (required)
        :param str accept: This header specifies the format of the returned file. For this method, the value of the header should be <code>Accept: application/pdf</code>.  (required)
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.download_label_file_with_http_info(shipment_id, accept, **kwargs)  # noqa: E501
        else:
            (data) = self.download_label_file_with_http_info(shipment_id, accept, **kwargs)  # noqa: E501
            return data

    def download_label_file_with_http_info(self, shipment_id, accept, **kwargs):  # noqa: E501
        """download_label_file  # noqa: E501

        This method returns the shipping label file that was generated for the <b>shipmentId</b> value specified in the request. Call <b>createFromShippingQuote</b> to generate a shipment ID.  <br><br>Use the <code>Accept</code> HTTP header to specify the format of the returned file. The default file format is a PDF file. <!-- Are other options available? -->  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_label_file_with_http_info(shipment_id, accept, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str shipment_id: This path parameter specifies the unique eBay-assigned identifier of the shipment associated with the shipping label you want to download.<br><br> The <b>shipmentId</b> value is generated and returned by the <a href=\"/api-docs/sell/logistics/resources/shipment/methods/createFromShippingQuote\" target=\"_blank\">createFromShippingQuote</a> method. (required)
        :param str accept: This header specifies the format of the returned file. For this method, the value of the header should be <code>Accept: application/pdf</code>.  (required)
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['shipment_id', 'accept']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method download_label_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'shipment_id' is set
        if ('shipment_id' not in params or
                params['shipment_id'] is None):
            raise ValueError("Missing the required parameter `shipment_id` when calling `download_label_file`")  # noqa: E501
        # verify the required parameter 'accept' is set
        if ('accept' not in params or
                params['accept'] is None):
            raise ValueError("Missing the required parameter `accept` when calling `download_label_file`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'shipment_id' in params:
            path_params['shipmentId'] = params['shipment_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'accept' in params:
            header_params['Accept'] = params['accept']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/pdf'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_auth']  # noqa: E501

        return self.api_client.call_api(
            '/shipment/{shipmentId}/download_label_file', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[str]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_shipment(self, shipment_id, **kwargs):  # noqa: E501
        """get_shipment  # noqa: E501

        This method retrieves the shipment details for the specified shipment ID. Call <b>createFromShippingQuote</b> to generate a shipment ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_shipment(shipment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str shipment_id: This path parameter specifies the unique eBay-assigned identifier of the shipment you want to retrieve.<br><br>The <b>shipmentId</b> value is generated and returned by the <a href=\"/api-docs/sell/logistics/resources/shipment/methods/createFromShippingQuote\" target=\"_blank\">createFromShippingQuote</a> method. (required)
        :return: Shipment
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_shipment_with_http_info(shipment_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_shipment_with_http_info(shipment_id, **kwargs)  # noqa: E501
            return data

    def get_shipment_with_http_info(self, shipment_id, **kwargs):  # noqa: E501
        """get_shipment  # noqa: E501

        This method retrieves the shipment details for the specified shipment ID. Call <b>createFromShippingQuote</b> to generate a shipment ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_shipment_with_http_info(shipment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str shipment_id: This path parameter specifies the unique eBay-assigned identifier of the shipment you want to retrieve.<br><br>The <b>shipmentId</b> value is generated and returned by the <a href=\"/api-docs/sell/logistics/resources/shipment/methods/createFromShippingQuote\" target=\"_blank\">createFromShippingQuote</a> method. (required)
        :return: Shipment
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['shipment_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_shipment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'shipment_id' is set
        if ('shipment_id' not in params or
                params['shipment_id'] is None):
            raise ValueError("Missing the required parameter `shipment_id` when calling `get_shipment`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'shipment_id' in params:
            path_params['shipmentId'] = params['shipment_id']  # noqa: E501

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
            '/shipment/{shipmentId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Shipment',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
