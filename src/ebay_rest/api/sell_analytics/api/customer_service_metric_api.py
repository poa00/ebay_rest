# coding: utf-8

"""
     Seller Service Metrics API 

    The <i>Analytics API</i> provides data and information about a seller and their eBay business.  <br><br>The resources and methods in this API let sellers review information on their listing performance, metrics on their customer service performance, and details on their eBay seller performance rating.  <br><br>The three resources in the Analytics API provide the following data and information: <ul><li><b>Customer Service Metric</b> &ndash; Returns benchmark data and a metric rating pertaining to a seller's customer service performance as compared to other seller's in the same peer group.</li> <li><b>Traffic Report</b> &ndash; Returns data and information that shows how buyers are engaging with a seller's listings.</li> <li><b>Seller Standards Profile</b> &ndash; Returns information pertaining to a seller's profile rating.</li></ul> Sellers can use the data and information returned by the various Analytics API methods to determine where they can make improvements to increase sales and how they might improve their seller status as viewed by eBay buyers.  <br><br>For details on using this API, see <a href=\"/api-docs/sell/static/performance/analyzing-performance.html\" title=\"Selling Integration Guide\">Analyzing seller performance</a>.  # noqa: E501

    OpenAPI spec version: 1.3.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ...sell_analytics.api_client import ApiClient


class CustomerServiceMetricApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_customer_service_metric(self, customer_service_metric_type, evaluation_marketplace_id, evaluation_type, **kwargs):  # noqa: E501
        """get_customer_service_metric  # noqa: E501

        Use this method to retrieve a seller's performance and rating for the customer service metric.  <br><br>Control the response from the <b>getCustomerServiceMetric</b> method using the following path and query parameters: <ul><li><b>customer_service_metric_type</b> controls the type of customer service transactions evaluated for the metric rating.</li> <li><b>evaluation_type</b> controls the period you want to review.</li> <li><b>evaluation_marketplace_id</b> specifies the target marketplace for the evaluation.</li></ul> Currently, metric data is returned for only peer benchmarking. For details on the workings of peer benchmarking, see <a href=\"https://www.ebay.com/help/policies/selling-policies/seller-performance-policy/service-metrics-policy?id=4769\" title=\"eBay Help pages\" target=\"_blank\">Service metrics policy</a>.  <br><br>For details on using and understanding the response from this method, see <a href=\"/api-docs/sell/static/performance/customer-service-metric.html\" title=\"Selling Integration Guide\">Interpreting customer service metric ratings</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_customer_service_metric(customer_service_metric_type, evaluation_marketplace_id, evaluation_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str customer_service_metric_type: Use this path parameter to specify the type of customer service metrics and benchmark data you want returned for the seller. Supported types are:<br> <ul><li><code>ITEM_NOT_AS_DESCRIBED</code></li><li><code>ITEM_NOT_RECEIVED</code></li></ul> (required)
        :param str evaluation_marketplace_id: Use this query parameter to specify the Marketplace ID to evaluate for the customer service metrics and benchmark data.  <br><br>For the list of supported marketplaces, see <a href=\"/api-docs/sell/analytics/static/overview.html#requirements\" title=\"Analytics API Overview\" target=\"_blank\">Analytics API requirements and restrictions</a>. For implementation help, refer to eBay API documentation at https://developer.ebay.com/api-docs/sell/analytics/types/bas:MarketplaceIdEnum (required)
        :param str evaluation_type: Use this path parameter to specify the evaluation period to use for the performance metrics. See <a href=\"/api-docs/sell/analytics/types/api:EvaluationTypeEnum\" target=\"_blank\"> EvaluationTypeEnum</a> for more information on the supported values. (required)
        :return: GetCustomerServiceMetricResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_customer_service_metric_with_http_info(customer_service_metric_type, evaluation_marketplace_id, evaluation_type, **kwargs)  # noqa: E501
        else:
            (data) = self.get_customer_service_metric_with_http_info(customer_service_metric_type, evaluation_marketplace_id, evaluation_type, **kwargs)  # noqa: E501
            return data

    def get_customer_service_metric_with_http_info(self, customer_service_metric_type, evaluation_marketplace_id, evaluation_type, **kwargs):  # noqa: E501
        """get_customer_service_metric  # noqa: E501

        Use this method to retrieve a seller's performance and rating for the customer service metric.  <br><br>Control the response from the <b>getCustomerServiceMetric</b> method using the following path and query parameters: <ul><li><b>customer_service_metric_type</b> controls the type of customer service transactions evaluated for the metric rating.</li> <li><b>evaluation_type</b> controls the period you want to review.</li> <li><b>evaluation_marketplace_id</b> specifies the target marketplace for the evaluation.</li></ul> Currently, metric data is returned for only peer benchmarking. For details on the workings of peer benchmarking, see <a href=\"https://www.ebay.com/help/policies/selling-policies/seller-performance-policy/service-metrics-policy?id=4769\" title=\"eBay Help pages\" target=\"_blank\">Service metrics policy</a>.  <br><br>For details on using and understanding the response from this method, see <a href=\"/api-docs/sell/static/performance/customer-service-metric.html\" title=\"Selling Integration Guide\">Interpreting customer service metric ratings</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_customer_service_metric_with_http_info(customer_service_metric_type, evaluation_marketplace_id, evaluation_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str customer_service_metric_type: Use this path parameter to specify the type of customer service metrics and benchmark data you want returned for the seller. Supported types are:<br> <ul><li><code>ITEM_NOT_AS_DESCRIBED</code></li><li><code>ITEM_NOT_RECEIVED</code></li></ul> (required)
        :param str evaluation_marketplace_id: Use this query parameter to specify the Marketplace ID to evaluate for the customer service metrics and benchmark data.  <br><br>For the list of supported marketplaces, see <a href=\"/api-docs/sell/analytics/static/overview.html#requirements\" title=\"Analytics API Overview\" target=\"_blank\">Analytics API requirements and restrictions</a>. For implementation help, refer to eBay API documentation at https://developer.ebay.com/api-docs/sell/analytics/types/bas:MarketplaceIdEnum (required)
        :param str evaluation_type: Use this path parameter to specify the evaluation period to use for the performance metrics. See <a href=\"/api-docs/sell/analytics/types/api:EvaluationTypeEnum\" target=\"_blank\"> EvaluationTypeEnum</a> for more information on the supported values. (required)
        :return: GetCustomerServiceMetricResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['customer_service_metric_type', 'evaluation_marketplace_id', 'evaluation_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_customer_service_metric" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'customer_service_metric_type' is set
        if ('customer_service_metric_type' not in params or
                params['customer_service_metric_type'] is None):
            raise ValueError("Missing the required parameter `customer_service_metric_type` when calling `get_customer_service_metric`")  # noqa: E501
        # verify the required parameter 'evaluation_marketplace_id' is set
        if ('evaluation_marketplace_id' not in params or
                params['evaluation_marketplace_id'] is None):
            raise ValueError("Missing the required parameter `evaluation_marketplace_id` when calling `get_customer_service_metric`")  # noqa: E501
        # verify the required parameter 'evaluation_type' is set
        if ('evaluation_type' not in params or
                params['evaluation_type'] is None):
            raise ValueError("Missing the required parameter `evaluation_type` when calling `get_customer_service_metric`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'customer_service_metric_type' in params:
            path_params['customer_service_metric_type'] = params['customer_service_metric_type']  # noqa: E501
        if 'evaluation_type' in params:
            path_params['evaluation_type'] = params['evaluation_type']  # noqa: E501

        query_params = []
        if 'evaluation_marketplace_id' in params:
            query_params.append(('evaluation_marketplace_id', params['evaluation_marketplace_id']))  # noqa: E501

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
            '/customer_service_metric/{customer_service_metric_type}/{evaluation_type}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetCustomerServiceMetricResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
