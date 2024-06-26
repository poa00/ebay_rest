# coding: utf-8

"""
    Item Feed Service

    <span class=\"tablenote\"><b>Note:</b> This is a <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited \" target=\"_blank\"> <img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"  alt=\"Limited Release\" />(Limited Release)</a> API available only to select developers approved by business units. For information on how to obtain access to this API in production, see the <a href=\"api-docs/buy/static/buy-requirements.html\" target=\"_blank\">Buy APIs Requirements</a>.</span><br><br>The Feed API provides the ability to download TSV_GZIP feed files containing eBay items and an hourly snapshot file of the items that have changed within an hour for a specific category, date and marketplace. <p>In addition to the API, there is an open source <a href=\"https://github.com/eBay/FeedSDK \" target=\"_blank\">Feed SDK</a> written in Java that downloads, combines files into a single file when needed, and unzips the entire feed file. It also lets you specify field filters to curate the items in the file.</p>  # noqa: E501

    OpenAPI spec version: v1_beta.35.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ...buy_feed.api_client import ApiClient


class ItemSnapshotApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_item_snapshot_feed(self, accept, x_ebay_c_marketplace_id, range, category_id, snapshot_date, **kwargs):  # noqa: E501
        """get_item_snapshot_feed  # noqa: E501

        The <b> Hourly Snapshot</b> feed file is generated each hour every day for most categories. This method lets you download an <b> Hourly Snapshot</b> TSV_GZIP (tab-separated value gzip) feed file containing the details of all the items that have changed <i> within</i> the specified day and hour for a specific category. This means to generate the 8AM file of items that have changed from 8AM and 8:59AM, the service starts at 9AM. You can retrieve the 8AM snapshot file at 10AM.<br><br>Snapshot feeds now include new listings. You can check <a href=\"/api-docs/buy/feed/resources/item_snapshot/methods/getItemSnapshotFeed#response.items.itemCreationDate\">itemCreationDate</a> to identify listings that were newly created within the specified hour.<br><br><span class=\"tablenote\"><b>Note: </b> Filters are applied to the feed files. For details, see <a href=\"/api-docs/buy/static/api-feed.html#feed-filters\">Feed File Filters</a>. When curating the items returned, be sure to code as if these filters are not applied as they can be changed or removed in the future.</span><br><br>You can use the response from this method to update the item details of items stored in your database. By looking at the value of <a href=\"/api-docs/buy/feed/resources/item_snapshot/methods/getItemSnapshotFeed#response.items.itemSnapshotDate\">itemSnapshotDate</a> for a given item, you will be able to tell which information is the latest.<br><span class=\"tablenote\"><span style=\"color:#FF0000\"> <b> Important:</b> </span> When the value of the <b>availability</b> column is <code>UNAVAILABLE</code>, only the <b>itemId</b> and <b> availability</b> columns are populated. </span><br><span class=\"tablenote\"><b>Note:</b>The downloaded file will be gzipped automatically, so there is no reason to supply <b>Accept-Encoding:gzip</b> as a header. If this header is supplied, the downloaded file will be compressed twice, and this has no extra benefit.</span><h3><b>Downloading feed files </b></h3>Hourly snapshot feed files are binary gzip files. If the file is larger than 100 MB, the download must be streamed in chunks. You specify the size of the chunks in bytes using the <a href=\"#range-header\">Range</a> request header. The <a href=\"#content-range\">Content-range</a> response header indicates where in the full resource this partial chunk of data belongs and the total number of bytes in the file. For more information about using these headers, see <a href=\"/api-docs/buy/static/api-feed_beta.html#retrv-gzip\">Retrieving a gzip feed file</a>.<br><br><span class=\"tablenote\">  <b> Note:</b> A successful call will always return a TSV.GZIP file; however, unsuccessful calls generate errors that are returned in JSON format. For documentation purposes, the successful call response is shown below as JSON fields so that the value returned in each column can be explained. The order of the response fields shows the order of the columns in the feed file.</span><h3><b>Restrictions </b></h3>For a list of supported sites and other restrictions, see <a href=\"/api-docs/buy/feed/overview.html#API\">API Restrictions</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_item_snapshot_feed(accept, x_ebay_c_marketplace_id, range, category_id, snapshot_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str accept: The formats that the client accepts for the response.<br><br>A successful call will always return a TSV.GZIP file; however, unsuccessful calls generate error codes that are returned in JSON format.<br><br><b>Default:</b> <code>application/json,text/tab-separated-values</code> (required)
        :param str x_ebay_c_marketplace_id: The ID of the eBay marketplace where the item is hosted. This value is case sensitive.<br><br>For example: <br>&nbsp;&nbsp;<code>X-EBAY-C-MARKETPLACE-ID = EBAY_US</code>  <br><br> For a list of supported sites see, <a href=\"/api-docs/buy/feed/overview.html#API\">API Restrictions</a>. (required)
        :param str range: <a name=\"range-header\"></a>This header specifies the range in bytes of the chunks of the gzip file being returned. <br><br><b> Format:</b> <code>bytes=<em>startpos</em>-<em>endpos</em></code><br><br>  For example, the following retrieves the first 10 MBs of the feed file. <br><br>&nbsp;&nbsp;<code>Range bytes=0-10485760</code> <br><br>For more information about using this header, see <a href=\"/api-docs/buy/static/api-feed_beta.html#retrv-gzip\">Retrieving a gzip feed file</a>. <br><br><b>Maximum:</b> 100 MB (10MB in the Sandbox) (required)
        :param str category_id: This query parameter specifies the eBay top-level category ID  of the items to be returned in the feed file.<br> <br>The list of eBay category IDs changes over time and category IDs are not the same across all the eBay marketplaces. To get a list of the top-level categories for a marketplace, you can use the Taxonomy API <a href=\"/api-docs/commerce/taxonomy/resources/category_tree/methods/getCategoryTree\">getCategoryTree</a> method. This method retrieves the complete category tree for the marketplace. The top-level categories are identified by the <b>categoryTreeNodeLevel</b> field.<br><br><b>For example:</b><br>&nbsp;&nbsp;<code>\"categoryTreeNodeLevel\": 1</code> <br><br>For details see <a href=\"/api-docs/buy/buy-categories.html\">Get Categories for Buy APIs</a>.</li>  </ul> <br><br>   <b>Restriction:</b> Must be a top-level category other than Real Estate. Items listed under Real Estate L1 categories are excluded from all feeds in all marketplaces. (required)
        :param str snapshot_date: This query parameter specifies the date and hour of the snapshot feed file you want to retrieve.<br><br>Each file contains the items that changed within the hour in the specified category. So, the 9AM file contains the items that changed between 9AM and 9:59AM on the day specified.  It takes 2 hours to generate a snapshot file, which means to get the file for 9AM the earliest you could submit the call is at 11AM.<br><br>There are 7 days of <b> Hourly Snapshot</b> feed files available.<p><span class=\"tablenote\"><b>Note: </b> The Feed API uses GMT, so you must convert your local time to GMT. For example, if you lived in California and wanted the September 15th 7pm file, you would submit the following call: <br> <br><code>item_snapshot?category_id=625&snapshot_date=2017-09-16T02:00:00.000Z</code> </span></p>  <b>Format: </b>UTC <code>yyyy-MM-ddThh:00:00.000Z</code><br><br><span class=\"tablenote\"><b>Note:</b> Files are generated on the hour, so minutes and seconds are <em> always</em> zeros.</span> (required)
        :return: ItemSnapshotResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_item_snapshot_feed_with_http_info(accept, x_ebay_c_marketplace_id, range, category_id, snapshot_date, **kwargs)  # noqa: E501
        else:
            (data) = self.get_item_snapshot_feed_with_http_info(accept, x_ebay_c_marketplace_id, range, category_id, snapshot_date, **kwargs)  # noqa: E501
            return data

    def get_item_snapshot_feed_with_http_info(self, accept, x_ebay_c_marketplace_id, range, category_id, snapshot_date, **kwargs):  # noqa: E501
        """get_item_snapshot_feed  # noqa: E501

        The <b> Hourly Snapshot</b> feed file is generated each hour every day for most categories. This method lets you download an <b> Hourly Snapshot</b> TSV_GZIP (tab-separated value gzip) feed file containing the details of all the items that have changed <i> within</i> the specified day and hour for a specific category. This means to generate the 8AM file of items that have changed from 8AM and 8:59AM, the service starts at 9AM. You can retrieve the 8AM snapshot file at 10AM.<br><br>Snapshot feeds now include new listings. You can check <a href=\"/api-docs/buy/feed/resources/item_snapshot/methods/getItemSnapshotFeed#response.items.itemCreationDate\">itemCreationDate</a> to identify listings that were newly created within the specified hour.<br><br><span class=\"tablenote\"><b>Note: </b> Filters are applied to the feed files. For details, see <a href=\"/api-docs/buy/static/api-feed.html#feed-filters\">Feed File Filters</a>. When curating the items returned, be sure to code as if these filters are not applied as they can be changed or removed in the future.</span><br><br>You can use the response from this method to update the item details of items stored in your database. By looking at the value of <a href=\"/api-docs/buy/feed/resources/item_snapshot/methods/getItemSnapshotFeed#response.items.itemSnapshotDate\">itemSnapshotDate</a> for a given item, you will be able to tell which information is the latest.<br><span class=\"tablenote\"><span style=\"color:#FF0000\"> <b> Important:</b> </span> When the value of the <b>availability</b> column is <code>UNAVAILABLE</code>, only the <b>itemId</b> and <b> availability</b> columns are populated. </span><br><span class=\"tablenote\"><b>Note:</b>The downloaded file will be gzipped automatically, so there is no reason to supply <b>Accept-Encoding:gzip</b> as a header. If this header is supplied, the downloaded file will be compressed twice, and this has no extra benefit.</span><h3><b>Downloading feed files </b></h3>Hourly snapshot feed files are binary gzip files. If the file is larger than 100 MB, the download must be streamed in chunks. You specify the size of the chunks in bytes using the <a href=\"#range-header\">Range</a> request header. The <a href=\"#content-range\">Content-range</a> response header indicates where in the full resource this partial chunk of data belongs and the total number of bytes in the file. For more information about using these headers, see <a href=\"/api-docs/buy/static/api-feed_beta.html#retrv-gzip\">Retrieving a gzip feed file</a>.<br><br><span class=\"tablenote\">  <b> Note:</b> A successful call will always return a TSV.GZIP file; however, unsuccessful calls generate errors that are returned in JSON format. For documentation purposes, the successful call response is shown below as JSON fields so that the value returned in each column can be explained. The order of the response fields shows the order of the columns in the feed file.</span><h3><b>Restrictions </b></h3>For a list of supported sites and other restrictions, see <a href=\"/api-docs/buy/feed/overview.html#API\">API Restrictions</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_item_snapshot_feed_with_http_info(accept, x_ebay_c_marketplace_id, range, category_id, snapshot_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str accept: The formats that the client accepts for the response.<br><br>A successful call will always return a TSV.GZIP file; however, unsuccessful calls generate error codes that are returned in JSON format.<br><br><b>Default:</b> <code>application/json,text/tab-separated-values</code> (required)
        :param str x_ebay_c_marketplace_id: The ID of the eBay marketplace where the item is hosted. This value is case sensitive.<br><br>For example: <br>&nbsp;&nbsp;<code>X-EBAY-C-MARKETPLACE-ID = EBAY_US</code>  <br><br> For a list of supported sites see, <a href=\"/api-docs/buy/feed/overview.html#API\">API Restrictions</a>. (required)
        :param str range: <a name=\"range-header\"></a>This header specifies the range in bytes of the chunks of the gzip file being returned. <br><br><b> Format:</b> <code>bytes=<em>startpos</em>-<em>endpos</em></code><br><br>  For example, the following retrieves the first 10 MBs of the feed file. <br><br>&nbsp;&nbsp;<code>Range bytes=0-10485760</code> <br><br>For more information about using this header, see <a href=\"/api-docs/buy/static/api-feed_beta.html#retrv-gzip\">Retrieving a gzip feed file</a>. <br><br><b>Maximum:</b> 100 MB (10MB in the Sandbox) (required)
        :param str category_id: This query parameter specifies the eBay top-level category ID  of the items to be returned in the feed file.<br> <br>The list of eBay category IDs changes over time and category IDs are not the same across all the eBay marketplaces. To get a list of the top-level categories for a marketplace, you can use the Taxonomy API <a href=\"/api-docs/commerce/taxonomy/resources/category_tree/methods/getCategoryTree\">getCategoryTree</a> method. This method retrieves the complete category tree for the marketplace. The top-level categories are identified by the <b>categoryTreeNodeLevel</b> field.<br><br><b>For example:</b><br>&nbsp;&nbsp;<code>\"categoryTreeNodeLevel\": 1</code> <br><br>For details see <a href=\"/api-docs/buy/buy-categories.html\">Get Categories for Buy APIs</a>.</li>  </ul> <br><br>   <b>Restriction:</b> Must be a top-level category other than Real Estate. Items listed under Real Estate L1 categories are excluded from all feeds in all marketplaces. (required)
        :param str snapshot_date: This query parameter specifies the date and hour of the snapshot feed file you want to retrieve.<br><br>Each file contains the items that changed within the hour in the specified category. So, the 9AM file contains the items that changed between 9AM and 9:59AM on the day specified.  It takes 2 hours to generate a snapshot file, which means to get the file for 9AM the earliest you could submit the call is at 11AM.<br><br>There are 7 days of <b> Hourly Snapshot</b> feed files available.<p><span class=\"tablenote\"><b>Note: </b> The Feed API uses GMT, so you must convert your local time to GMT. For example, if you lived in California and wanted the September 15th 7pm file, you would submit the following call: <br> <br><code>item_snapshot?category_id=625&snapshot_date=2017-09-16T02:00:00.000Z</code> </span></p>  <b>Format: </b>UTC <code>yyyy-MM-ddThh:00:00.000Z</code><br><br><span class=\"tablenote\"><b>Note:</b> Files are generated on the hour, so minutes and seconds are <em> always</em> zeros.</span> (required)
        :return: ItemSnapshotResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['accept', 'x_ebay_c_marketplace_id', 'range', 'category_id', 'snapshot_date']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_item_snapshot_feed" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'accept' is set
        if ('accept' not in params or
                params['accept'] is None):
            raise ValueError("Missing the required parameter `accept` when calling `get_item_snapshot_feed`")  # noqa: E501
        # verify the required parameter 'x_ebay_c_marketplace_id' is set
        if ('x_ebay_c_marketplace_id' not in params or
                params['x_ebay_c_marketplace_id'] is None):
            raise ValueError("Missing the required parameter `x_ebay_c_marketplace_id` when calling `get_item_snapshot_feed`")  # noqa: E501
        # verify the required parameter 'range' is set
        if ('range' not in params or
                params['range'] is None):
            raise ValueError("Missing the required parameter `range` when calling `get_item_snapshot_feed`")  # noqa: E501
        # verify the required parameter 'category_id' is set
        if ('category_id' not in params or
                params['category_id'] is None):
            raise ValueError("Missing the required parameter `category_id` when calling `get_item_snapshot_feed`")  # noqa: E501
        # verify the required parameter 'snapshot_date' is set
        if ('snapshot_date' not in params or
                params['snapshot_date'] is None):
            raise ValueError("Missing the required parameter `snapshot_date` when calling `get_item_snapshot_feed`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'category_id' in params:
            query_params.append(('category_id', params['category_id']))  # noqa: E501
        if 'snapshot_date' in params:
            query_params.append(('snapshot_date', params['snapshot_date']))  # noqa: E501

        header_params = {}
        if 'accept' in params:
            header_params['Accept'] = params['accept']  # noqa: E501
        if 'x_ebay_c_marketplace_id' in params:
            header_params['X-EBAY-C-MARKETPLACE-ID'] = params['x_ebay_c_marketplace_id']  # noqa: E501
        if 'range' in params:
            header_params['Range'] = params['range']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/tab-separated-values'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_auth']  # noqa: E501

        return self.api_client.call_api(
            '/item_snapshot', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ItemSnapshotResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
