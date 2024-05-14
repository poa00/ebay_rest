# coding: utf-8

"""
    Marketing API

    <p>The <i>Marketing API </i> offers two platforms that sellers can use to promote and advertise their products:</p> <ul><li><b>Promoted Listings</b> is an eBay ad service that lets sellers set up <i>ad campaigns </i> for the products they want to promote. eBay displays the ads in search results and in other marketing modules as <b>SPONSORED</b> listings. If an item in a Promoted Listings campaign sells, the seller is assessed a Promoted Listings fee, which is a seller-specified percentage applied to the sales price. For complete details, refer to the <a href=\"/api-docs/sell/static/marketing/pl-landing.html\">Promoted Listings playbook</a>.</li><li><b>Promotions Manager</b> gives sellers a way to offer discounts on specific items as a way to attract buyers to their inventory. Sellers can set up discounts (such as \"20% off\" and other types of offers) on specific items or on an entire customer order. To further attract buyers, eBay prominently displays promotion <i>teasers</i> throughout buyer flows. For complete details, see <a href=\"/api-docs/sell/static/marketing/promotions-manager.html\">Promotions Manager</a>.</li></ul>  <p><b>Marketing reports</b>, on both the Promoted Listings and Promotions Manager platforms, give sellers information that shows the effectiveness of their marketing strategies. The data gives sellers the ability to review and fine tune their marketing efforts.</p><p><b>Store Email Campaign</b> allows sellers to create and send email campaigns to customers who have signed up to receive their newsletter. For more information on email campaigns, see <a href=\"/api-docs/sell/static/marketing/store-email-campaigns.html#email-campain-types\" target=\"_blank\">Store Email Campaigns</a>.<p class=\"tablenote\"><b>Important!</b> Sellers must have an active eBay Store subscription, and they must accept the <b>Terms and Conditions</b> before they can make requests to these APIs in the Production environment. There are also site-specific listings requirements and restrictions associated with these marketing tools, as listed in the \"requirements and restrictions\" sections for <a href=\"/api-docs/sell/marketing/static/overview.html#PL-requirements\">Promoted Listings</a> and <a href=\"/api-docs/sell/marketing/static/overview.html#PM-requirements\">Promotions Manager</a>.</p> <p>The table below lists all the Marketing API calls grouped by resource.</p>  # noqa: E501

    OpenAPI spec version: v1.21.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ...sell_marketing.api_client import ApiClient


class AdReportTaskApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_report_task(self, body, content_type, **kwargs):  # noqa: E501
        """create_report_task  # noqa: E501

        This method creates a <i>report task</i>, which generates a Promoted Listings report based on the values specified in the call.<br /><br />The report is generated based on the criteria you specify, including the report type, the report's dimensions and metrics, the report's start and end dates, the listings to include in the report, and more. <i>Metrics </i>are the quantitative measurements in the report while <i>dimensions</i> specify the attributes of the data included in the reports.<br /><br />When creating a report task, you can specify the items you want included in the report. The items you specify, using either <b>listingId</b> or <b>inventoryReference</b> values, must be in a Promoted Listings campaign for them to be included in the report.<br /><br />For details on the required and optional fields for each report type, see <a href=\"/api-docs/sell/static/marketing/pl-reports.html\">Promoted Listings reporting</a>.<br /><br />This call returns the URL to the report task in the <b>Location</b> response header, and the URL includes the report-task ID.<br /><br />Reports often take time to generate and it's common for this call to return an HTTP status of <code>202</code>, which indicates the report is being generated. Call <a href=\"/api-docs/sell/marketing/resources/ad_report_task/methods/getReportTasks\">getReportTasks</a> (or <a href=\"/api-docs/sell/marketing/resources/ad_report_task/methods/getReportTask\">getReportTask</a> with the report-task ID) to determine the status of a Promoted Listings report. When a report is complete, eBay sets its status to <b>SUCCESS</b> and you can download it using the URL returned in the <b>reportHref</b> field of the <b>getReportTask</b> call. Report files are tab-separated value gzip files with a file extension of <code>.tsv.gz</code>.<br/><br/><span class=\"tablenote\"><b>Note:</b> The reporting of some data related to sales and ad-fees may require a 72-hour (<b>maximum</b>) adjustment period which is often referred to as the <i>Reconciliation Period</i>. Such adjustment periods should, on average, be minimal. However, at any given time, the <b>payments</b> tab may be used to view those amounts that have actually been charged.</span><br /><span class=\"tablenote\"><span style=\"color:#004680\"><strong>Note:</strong></span> This call fails if you don't submit all the required fields for the specified report type. Fields not supported by the specified report type are ignored. Call <a href=\"/api-docs/sell/marketing/resources/ad_report_metadata/methods/getReportMetadata\">getReportMetadata</a> to retrieve a list of the fields you need to configure for each Promoted Listings report type.</span><br/><div class=\"msgbox_important\"><p class=\"msgbox_importantInDiv\" data-mc-autonum=\"&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;\"><span class=\"autonumber\"><span><b><span style=\"color: #dd1e31;\" class=\"mcFormatColor\">Important!</span></b></span></span>For <b>ad_report</b> and <b>ad_report_task</b> methods, the API call limit is subject to a per user quota. These API calls can <b>only</b> be executed a maximum of 200 times per hour for each seller/user. If the number of calls per hour exceeds this limit, any new calls will be blocked for the next hour.</p></div><br><div class=\"msgbox_important\"><p class=\"msgbox_importantInDiv\" data-mc-autonum=\"&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;\"><span class=\"autonumber\"><span><b><span style=\"color: #dd1e31;\" class=\"mcFormatColor\">Important!</span></b></span></span> The data threshold for a single report is currently 500,000 records; if this threshold is exceeded, the report will fail.</p></div>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_report_task(body, content_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateReportTask body: The container for the fields that define the report task. (required)
        :param str content_type: This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br> For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_report_task_with_http_info(body, content_type, **kwargs)  # noqa: E501
        else:
            (data) = self.create_report_task_with_http_info(body, content_type, **kwargs)  # noqa: E501
            return data

    def create_report_task_with_http_info(self, body, content_type, **kwargs):  # noqa: E501
        """create_report_task  # noqa: E501

        This method creates a <i>report task</i>, which generates a Promoted Listings report based on the values specified in the call.<br /><br />The report is generated based on the criteria you specify, including the report type, the report's dimensions and metrics, the report's start and end dates, the listings to include in the report, and more. <i>Metrics </i>are the quantitative measurements in the report while <i>dimensions</i> specify the attributes of the data included in the reports.<br /><br />When creating a report task, you can specify the items you want included in the report. The items you specify, using either <b>listingId</b> or <b>inventoryReference</b> values, must be in a Promoted Listings campaign for them to be included in the report.<br /><br />For details on the required and optional fields for each report type, see <a href=\"/api-docs/sell/static/marketing/pl-reports.html\">Promoted Listings reporting</a>.<br /><br />This call returns the URL to the report task in the <b>Location</b> response header, and the URL includes the report-task ID.<br /><br />Reports often take time to generate and it's common for this call to return an HTTP status of <code>202</code>, which indicates the report is being generated. Call <a href=\"/api-docs/sell/marketing/resources/ad_report_task/methods/getReportTasks\">getReportTasks</a> (or <a href=\"/api-docs/sell/marketing/resources/ad_report_task/methods/getReportTask\">getReportTask</a> with the report-task ID) to determine the status of a Promoted Listings report. When a report is complete, eBay sets its status to <b>SUCCESS</b> and you can download it using the URL returned in the <b>reportHref</b> field of the <b>getReportTask</b> call. Report files are tab-separated value gzip files with a file extension of <code>.tsv.gz</code>.<br/><br/><span class=\"tablenote\"><b>Note:</b> The reporting of some data related to sales and ad-fees may require a 72-hour (<b>maximum</b>) adjustment period which is often referred to as the <i>Reconciliation Period</i>. Such adjustment periods should, on average, be minimal. However, at any given time, the <b>payments</b> tab may be used to view those amounts that have actually been charged.</span><br /><span class=\"tablenote\"><span style=\"color:#004680\"><strong>Note:</strong></span> This call fails if you don't submit all the required fields for the specified report type. Fields not supported by the specified report type are ignored. Call <a href=\"/api-docs/sell/marketing/resources/ad_report_metadata/methods/getReportMetadata\">getReportMetadata</a> to retrieve a list of the fields you need to configure for each Promoted Listings report type.</span><br/><div class=\"msgbox_important\"><p class=\"msgbox_importantInDiv\" data-mc-autonum=\"&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;\"><span class=\"autonumber\"><span><b><span style=\"color: #dd1e31;\" class=\"mcFormatColor\">Important!</span></b></span></span>For <b>ad_report</b> and <b>ad_report_task</b> methods, the API call limit is subject to a per user quota. These API calls can <b>only</b> be executed a maximum of 200 times per hour for each seller/user. If the number of calls per hour exceeds this limit, any new calls will be blocked for the next hour.</p></div><br><div class=\"msgbox_important\"><p class=\"msgbox_importantInDiv\" data-mc-autonum=\"&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;\"><span class=\"autonumber\"><span><b><span style=\"color: #dd1e31;\" class=\"mcFormatColor\">Important!</span></b></span></span> The data threshold for a single report is currently 500,000 records; if this threshold is exceeded, the report will fail.</p></div>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_report_task_with_http_info(body, content_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateReportTask body: The container for the fields that define the report task. (required)
        :param str content_type: This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br> For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>. (required)
        :return: None
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
                    " to method create_report_task" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_report_task`")  # noqa: E501
        # verify the required parameter 'content_type' is set
        if ('content_type' not in params or
                params['content_type'] is None):
            raise ValueError("Missing the required parameter `content_type` when calling `create_report_task`")  # noqa: E501

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
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_auth']  # noqa: E501

        return self.api_client.call_api(
            '/ad_report_task', 'POST',
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

    def delete_report_task(self, report_task_id, **kwargs):  # noqa: E501
        """delete_report_task  # noqa: E501

        This call deletes the report task specified by the <b>report_task_id</b> path parameter. This method also deletes any reports generated by the report task.  <p>Report task IDs are generated by eBay when you call <a href=\"/api-docs/sell/marketing/resources/ad_report_task/methods/createReportTask\">createReportTask</a>. Get a complete list of a seller's report-task IDs by calling <a href=\"/api-docs/sell/marketing/resources/ad_report_task/methods/getReportTasks\">getReportTasks</a>.</p><br/><div class=\"msgbox_important\"><p class=\"msgbox_importantInDiv\" data-mc-autonum=\"&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;\"><span class=\"autonumber\"><span><b><span style=\"color: #dd1e31;\" class=\"mcFormatColor\">Important!</span></b></span></span>For <b>ad_report</b> and <b>ad_report_task</b> methods, the API call limit is subject to a per user quota. These API calls can <b>only</b> be executed a maximum of 200 times per hour for each seller/user. If the number of calls per hour exceeds this limit, any new calls will be blocked for the next hour.</p></div>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_report_task(report_task_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str report_task_id: This path parameter specifies the unique identifier of the report task being deleted.<br><br> Use the <a href=\"/api-docs/sell/marketing/resources/ad_report_task/methods/getReportTasks\" target=\"_blank\">getReportTasks</a> method to retrieve report task Ids. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_report_task_with_http_info(report_task_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_report_task_with_http_info(report_task_id, **kwargs)  # noqa: E501
            return data

    def delete_report_task_with_http_info(self, report_task_id, **kwargs):  # noqa: E501
        """delete_report_task  # noqa: E501

        This call deletes the report task specified by the <b>report_task_id</b> path parameter. This method also deletes any reports generated by the report task.  <p>Report task IDs are generated by eBay when you call <a href=\"/api-docs/sell/marketing/resources/ad_report_task/methods/createReportTask\">createReportTask</a>. Get a complete list of a seller's report-task IDs by calling <a href=\"/api-docs/sell/marketing/resources/ad_report_task/methods/getReportTasks\">getReportTasks</a>.</p><br/><div class=\"msgbox_important\"><p class=\"msgbox_importantInDiv\" data-mc-autonum=\"&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;\"><span class=\"autonumber\"><span><b><span style=\"color: #dd1e31;\" class=\"mcFormatColor\">Important!</span></b></span></span>For <b>ad_report</b> and <b>ad_report_task</b> methods, the API call limit is subject to a per user quota. These API calls can <b>only</b> be executed a maximum of 200 times per hour for each seller/user. If the number of calls per hour exceeds this limit, any new calls will be blocked for the next hour.</p></div>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_report_task_with_http_info(report_task_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str report_task_id: This path parameter specifies the unique identifier of the report task being deleted.<br><br> Use the <a href=\"/api-docs/sell/marketing/resources/ad_report_task/methods/getReportTasks\" target=\"_blank\">getReportTasks</a> method to retrieve report task Ids. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['report_task_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_report_task" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'report_task_id' is set
        if ('report_task_id' not in params or
                params['report_task_id'] is None):
            raise ValueError("Missing the required parameter `report_task_id` when calling `delete_report_task`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'report_task_id' in params:
            path_params['report_task_id'] = params['report_task_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['api_auth']  # noqa: E501

        return self.api_client.call_api(
            '/ad_report_task/{report_task_id}', 'DELETE',
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

    def get_report_task(self, report_task_id, **kwargs):  # noqa: E501
        """get_report_task  # noqa: E501

        This call returns the details of a specific Promoted Listings report task, as specified by the <b>report_task_id</b> path parameter. <p>The report task includes the report criteria (such as the report dimensions, metrics, and included listing) and the report-generation rules (such as starting and ending dates for the specified report task).</p>  <p>Report-task IDs are generated by eBay when you call <a href=\"/api-docs/sell/marketing/resources/ad_report_task/methods/createReportTask\">createReportTask</a>. Get a complete list of a seller's report-task IDs by calling <a href=\"/api-docs/sell/marketing/resources/ad_report_task/methods/getReportTasks\">getReportTasks</a>.</p><br/><div class=\"msgbox_important\"><p class=\"msgbox_importantInDiv\" data-mc-autonum=\"&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;\"><span class=\"autonumber\"><span><b><span style=\"color: #dd1e31;\" class=\"mcFormatColor\">Important!</span></b></span></span>For <b>ad_report</b> and <b>ad_report_task</b> methods, the API call limit is subject to a per user quota. These API calls can <b>only</b> be executed a maximum of 200 times per hour for each seller/user. If the number of calls per hour exceeds this limit, any new calls will be blocked for the next hour.</p></div>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_report_task(report_task_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str report_task_id: This path parameter specifies the unique identifier of the report task being retrieved.<br><br> Use the <a href=\"/api-docs/sell/marketing/resources/ad_report_task/methods/getReportTasks\" target=\"_blank\">getReportTasks</a> method to retrieve report task Ids. (required)
        :return: ReportTask
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_report_task_with_http_info(report_task_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_report_task_with_http_info(report_task_id, **kwargs)  # noqa: E501
            return data

    def get_report_task_with_http_info(self, report_task_id, **kwargs):  # noqa: E501
        """get_report_task  # noqa: E501

        This call returns the details of a specific Promoted Listings report task, as specified by the <b>report_task_id</b> path parameter. <p>The report task includes the report criteria (such as the report dimensions, metrics, and included listing) and the report-generation rules (such as starting and ending dates for the specified report task).</p>  <p>Report-task IDs are generated by eBay when you call <a href=\"/api-docs/sell/marketing/resources/ad_report_task/methods/createReportTask\">createReportTask</a>. Get a complete list of a seller's report-task IDs by calling <a href=\"/api-docs/sell/marketing/resources/ad_report_task/methods/getReportTasks\">getReportTasks</a>.</p><br/><div class=\"msgbox_important\"><p class=\"msgbox_importantInDiv\" data-mc-autonum=\"&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;\"><span class=\"autonumber\"><span><b><span style=\"color: #dd1e31;\" class=\"mcFormatColor\">Important!</span></b></span></span>For <b>ad_report</b> and <b>ad_report_task</b> methods, the API call limit is subject to a per user quota. These API calls can <b>only</b> be executed a maximum of 200 times per hour for each seller/user. If the number of calls per hour exceeds this limit, any new calls will be blocked for the next hour.</p></div>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_report_task_with_http_info(report_task_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str report_task_id: This path parameter specifies the unique identifier of the report task being retrieved.<br><br> Use the <a href=\"/api-docs/sell/marketing/resources/ad_report_task/methods/getReportTasks\" target=\"_blank\">getReportTasks</a> method to retrieve report task Ids. (required)
        :return: ReportTask
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['report_task_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_report_task" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'report_task_id' is set
        if ('report_task_id' not in params or
                params['report_task_id'] is None):
            raise ValueError("Missing the required parameter `report_task_id` when calling `get_report_task`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'report_task_id' in params:
            path_params['report_task_id'] = params['report_task_id']  # noqa: E501

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
            '/ad_report_task/{report_task_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReportTask',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_report_tasks(self, **kwargs):  # noqa: E501
        """get_report_tasks  # noqa: E501

        This method returns information on all the existing report tasks related to a seller. <p>Use the <b>report_task_statuses</b> query parameter to control which reports to return. You can paginate the result set by specifying a <b>limit</b>, which dictates how many report tasks to return on each page of the response. Use the <b>offset</b> parameter to specify how many reports to skip in the result set before returning the first result.</p><br/><div class=\"msgbox_important\"><p class=\"msgbox_importantInDiv\" data-mc-autonum=\"&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;\"><span class=\"autonumber\"><span><b><span style=\"color: #dd1e31;\" class=\"mcFormatColor\">Important!</span></b></span></span>For <b>ad_report</b> and <b>ad_report_task</b> methods, the API call limit is subject to a per user quota. These API calls can <b>only</b> be executed a maximum of 200 times per hour for each seller/user. If the number of calls per hour exceeds this limit, any new calls will be blocked for the next hour.</p></div>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_report_tasks(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str limit: Specifies the maximum number of report tasks to return on a page in the paginated response.<br><br><b>Default:</b> 10<br><b>Maximum:</b> 500
        :param str offset: Specifies the number of report tasks to skip in the result set before returning the first report in the paginated response.  <p>Combine <b>offset</b> with the <b>limit</b> query parameter to control the reports returned in the response. For example, if you supply an <b>offset</b> of <code>0</code> and a <b>limit</b> of <code>10</code>, the response contains the first 10 reports from the complete list of report tasks retrieved by the call. If <b>offset</b> is <code>10</code> and <b>limit</b> is <code>10</code>, the first page of the response contains reports 11-20 from the complete result set.</p> <b>Default:</b> 0
        :param str report_task_statuses: This query parameter filters the returned report tasks by their status. Supply a comma-separated list of the report statuses you want returned. The results are filtered to include only the report statuses you specify.<br /><br /><span class=\"tablenote\"><span style=\"color:#004680\"><strong>Note:</strong></span> The results might not include some report tasks if other search conditions exclude them.</span><br />See <a href=\"/api-docs/sell/marketing/types/plr:TaskStatusEnum\" target=\"_blank\">TaskStatusEnum</a> for supported values.
        :return: ReportTaskPagedCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_report_tasks_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_report_tasks_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_report_tasks_with_http_info(self, **kwargs):  # noqa: E501
        """get_report_tasks  # noqa: E501

        This method returns information on all the existing report tasks related to a seller. <p>Use the <b>report_task_statuses</b> query parameter to control which reports to return. You can paginate the result set by specifying a <b>limit</b>, which dictates how many report tasks to return on each page of the response. Use the <b>offset</b> parameter to specify how many reports to skip in the result set before returning the first result.</p><br/><div class=\"msgbox_important\"><p class=\"msgbox_importantInDiv\" data-mc-autonum=\"&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;\"><span class=\"autonumber\"><span><b><span style=\"color: #dd1e31;\" class=\"mcFormatColor\">Important!</span></b></span></span>For <b>ad_report</b> and <b>ad_report_task</b> methods, the API call limit is subject to a per user quota. These API calls can <b>only</b> be executed a maximum of 200 times per hour for each seller/user. If the number of calls per hour exceeds this limit, any new calls will be blocked for the next hour.</p></div>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_report_tasks_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str limit: Specifies the maximum number of report tasks to return on a page in the paginated response.<br><br><b>Default:</b> 10<br><b>Maximum:</b> 500
        :param str offset: Specifies the number of report tasks to skip in the result set before returning the first report in the paginated response.  <p>Combine <b>offset</b> with the <b>limit</b> query parameter to control the reports returned in the response. For example, if you supply an <b>offset</b> of <code>0</code> and a <b>limit</b> of <code>10</code>, the response contains the first 10 reports from the complete list of report tasks retrieved by the call. If <b>offset</b> is <code>10</code> and <b>limit</b> is <code>10</code>, the first page of the response contains reports 11-20 from the complete result set.</p> <b>Default:</b> 0
        :param str report_task_statuses: This query parameter filters the returned report tasks by their status. Supply a comma-separated list of the report statuses you want returned. The results are filtered to include only the report statuses you specify.<br /><br /><span class=\"tablenote\"><span style=\"color:#004680\"><strong>Note:</strong></span> The results might not include some report tasks if other search conditions exclude them.</span><br />See <a href=\"/api-docs/sell/marketing/types/plr:TaskStatusEnum\" target=\"_blank\">TaskStatusEnum</a> for supported values.
        :return: ReportTaskPagedCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'offset', 'report_task_statuses']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_report_tasks" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'report_task_statuses' in params:
            query_params.append(('report_task_statuses', params['report_task_statuses']))  # noqa: E501

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
            '/ad_report_task', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReportTaskPagedCollection',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
