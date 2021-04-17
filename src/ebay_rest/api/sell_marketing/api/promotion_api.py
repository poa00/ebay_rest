# coding: utf-8

"""
    Marketing API

    <p>The <i>Marketing API </i> offers two platforms that sellers can use to promote and advertise their products:</p> <ul><li><b>Promoted Listings</b> is an eBay ad service that lets sellers set up <i>ad campaigns </i> for the products they want to promote. eBay displays the ads in search results and in other marketing modules as <b>SPONSORED</b> listings. If an item in a Promoted Listings campaign sells, the seller is assessed a Promoted Listings fee, which is a seller-specified percentage applied to the sales price. For complete details, see <a href=\"/api-docs/sell/static/marketing/promoted-listings.html\">Promoted Listings</a>.</li>  <li><b>Promotions Manager</b> gives sellers a way to offer discounts on specific items as a way to attract buyers to their inventory. Sellers can set up discounts (such as \"20% off\" and other types of offers) on specific items or on an entire customer order. To further attract buyers, eBay prominently displays promotion <i>teasers</i> throughout buyer flows. For complete details, see <a href=\"/api-docs/sell/static/marketing/promotions-manager.html\">Promotions Manager</a>.</li></ul>  <p><b>Marketing reports</b>, on both the Promoted Listings and Promotions Manager platforms, give sellers information that shows the effectiveness of their marketing strategies. The data gives sellers the ability to review and fine tune their marketing efforts.</p> <p class=\"tablenote\"><b>Important!</b> Sellers must have an active eBay Store subscription, and they must accept the <b>Terms and Conditions</b> before they can make requests to these APIs in the Production environment. There are also site-specific listings requirements and restrictions associated with these marketing tools, as listed in the \"requirements and restrictions\" sections for <a href=\"/api-docs/sell/marketing/static/overview.html#PL-requirements\">Promoted Listings</a> and <a href=\"/api-docs/sell/marketing/static/overview.html#PM-requirements\">Promotions Manager</a>.</p> <p>The table below lists all the Marketing API calls grouped by resource.</p>  # noqa: E501

    OpenAPI spec version: v1.8.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from sell_marketing.api_client import ApiClient


class PromotionApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_listing_set(self, promotion_id, **kwargs):  # noqa: E501
        """get_listing_set  # noqa: E501

        This method returns the set of listings associated with the promotion_id specified in the path parameter. Call getPromotions to retrieve the IDs of a seller's promotions. The listing details are returned in a paginated set and you can control and results returned using the following query parameters: limit, offset, q, sort, and status. Maximum associated listings returned: 200 Default number of listings returned: 200  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_listing_set(promotion_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str promotion_id: This path parameter takes a concatenation of the ID of the promotion you want to get plus the marketplace ID on which the promotion is hosted. Concatenate the two values by separating them with an &quot;at sign&quot; (@). The ID of the promotion (promotionId) is a unique eBay-assigned value that's generated when the promotion is created. The Marketplace ID is the ENUM value of eBay marketplace where the promotion is hosted. Example: 115001954505@EBAY_US (required)
        :param str limit: Specifies the maximum number of promotions returned on a page from the result set. Default: 200 Maximum: 200
        :param str offset: Specifies the number of promotions to skip in the result set before returning the first promotion in the paginated response. Combine offset with the limit query parameter to control the items returned in the response. For example, if you supply an offset of 0 and a limit of 10, the first page of the response contains the first 10 items from the complete list of items retrieved by the call. If offset is 10 and limit is 20, the first page of the response contains items 11-30 from the complete result set. Default: 0
        :param str q: Reserved for future use.
        :param str sort: Specifies the order in which to sort the associated listings in the response. If you precede the supplied value with a dash, the response is sorted in reverse order. Example: &nbsp;&nbsp;&nbsp;sort=PRICE - Sorts the associated listings by their current price in ascending order &nbsp;&nbsp;&nbsp;sort=-TITLE - Sorts the associated listings by their title in descending alphabetical order (Z-Az-a) Valid values: AVAILABLE PRICE TITLE For implementation help, refer to eBay API documentation at https://developer.ebay.com/api-docs/sell/marketing/types/csb:SortField
        :param str status: This query parameter applies only to markdown promotions. It filters the response based on the indicated status of the promotion. Currently, the only supported value for this parameter is MARKED_DOWN, which indicates active markdown promotions. For implementation help, refer to eBay API documentation at https://developer.ebay.com/api-docs/sell/marketing/types/sme:ItemMarkdownStatusEnum
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_listing_set_with_http_info(promotion_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_listing_set_with_http_info(promotion_id, **kwargs)  # noqa: E501
            return data

    def get_listing_set_with_http_info(self, promotion_id, **kwargs):  # noqa: E501
        """get_listing_set  # noqa: E501

        This method returns the set of listings associated with the promotion_id specified in the path parameter. Call getPromotions to retrieve the IDs of a seller's promotions. The listing details are returned in a paginated set and you can control and results returned using the following query parameters: limit, offset, q, sort, and status. Maximum associated listings returned: 200 Default number of listings returned: 200  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_listing_set_with_http_info(promotion_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str promotion_id: This path parameter takes a concatenation of the ID of the promotion you want to get plus the marketplace ID on which the promotion is hosted. Concatenate the two values by separating them with an &quot;at sign&quot; (@). The ID of the promotion (promotionId) is a unique eBay-assigned value that's generated when the promotion is created. The Marketplace ID is the ENUM value of eBay marketplace where the promotion is hosted. Example: 115001954505@EBAY_US (required)
        :param str limit: Specifies the maximum number of promotions returned on a page from the result set. Default: 200 Maximum: 200
        :param str offset: Specifies the number of promotions to skip in the result set before returning the first promotion in the paginated response. Combine offset with the limit query parameter to control the items returned in the response. For example, if you supply an offset of 0 and a limit of 10, the first page of the response contains the first 10 items from the complete list of items retrieved by the call. If offset is 10 and limit is 20, the first page of the response contains items 11-30 from the complete result set. Default: 0
        :param str q: Reserved for future use.
        :param str sort: Specifies the order in which to sort the associated listings in the response. If you precede the supplied value with a dash, the response is sorted in reverse order. Example: &nbsp;&nbsp;&nbsp;sort=PRICE - Sorts the associated listings by their current price in ascending order &nbsp;&nbsp;&nbsp;sort=-TITLE - Sorts the associated listings by their title in descending alphabetical order (Z-Az-a) Valid values: AVAILABLE PRICE TITLE For implementation help, refer to eBay API documentation at https://developer.ebay.com/api-docs/sell/marketing/types/csb:SortField
        :param str status: This query parameter applies only to markdown promotions. It filters the response based on the indicated status of the promotion. Currently, the only supported value for this parameter is MARKED_DOWN, which indicates active markdown promotions. For implementation help, refer to eBay API documentation at https://developer.ebay.com/api-docs/sell/marketing/types/sme:ItemMarkdownStatusEnum
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['promotion_id', 'limit', 'offset', 'q', 'sort', 'status']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_listing_set" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'promotion_id' is set
        if ('promotion_id' not in params or
                params['promotion_id'] is None):
            raise ValueError("Missing the required parameter `promotion_id` when calling `get_listing_set`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'promotion_id' in params:
            path_params['promotion_id'] = params['promotion_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'q' in params:
            query_params.append(('q', params['q']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'status' in params:
            query_params.append(('status', params['status']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['api_auth']  # noqa: E501

        return self.api_client.call_api(
            '/promotion/{promotion_id}/get_listing_set', 'GET',
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

    def get_promotions(self, marketplace_id, **kwargs):  # noqa: E501
        """get_promotions  # noqa: E501

        This method returns a list of a seller's undeleted promotions. The call returns up to 200 currently-available promotions on the specified marketplace. While the response body does not include the promotion's discountRules or inventoryCriterion containers, it does include the promotionHref (which you can use to retrieve the complete details of the promotion). Use query parameters to sort and filter the results by the number of promotions to return, the promotion state or type, and the eBay marketplace. You can also supply keywords to limit the response to the promotions that contain that keywords in the title of the promotion. Maximum returned: 200  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_promotions(marketplace_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str marketplace_id: The eBay marketplace ID of the site where the promotion is hosted. Valid values: EBAY_AU = Australia EBAY_DE = Germany EBAY_ES = Spain EBAY_FR = France EBAY_GB = Great Britain EBAY_IT = Italy EBAY_US = United States (required)
        :param str limit: Specifies the maximum number of promotions returned on a page from the result set. Default: 200 Maximum: 200
        :param str offset: Specifies the number of promotions to skip in the result set before returning the first promotion in the paginated response. Combine offset with the limit query parameter to control the items returned in the response. For example, if you supply an offset of 0 and a limit of 10, the first page of the response contains the first 10 items from the complete list of items retrieved by the call. If offset is 10 and limit is 20, the first page of the response contains items 11-30 from the complete result set. Default: 0
        :param str promotion_status: Specifies the promotion state by which you want to filter the results. The response contains only those promotions that match the state you specify. Valid values: DRAFT SCHEDULED RUNNING PAUSED ENDEDMaximum number of input values: 1
        :param str promotion_type: Filters the returned promotions based on their campaign promotion type. Specify one of the following values to indicate the promotion type you want returned: MARKDOWN_SALE &ndash; A markdown promotion set with createItemPriceMarkdownPromotion. ORDER_DISCOUNT &ndash; A threshold promotion set with createItemPromotion. VOLUME_DISCOUNT &ndash; A volume pricing promotion set with createItemPromotion.
        :param str q: A string consisting of one or more keywords. eBay filters the response by returning only the promotions that contain the supplied keywords in the promotion title. Example: &quot;iPhone&quot; or &quot;Harry Potter.&quot; Commas that separate keywords are ignored. For example, a keyword string of &quot;iPhone, iPad&quot; equals &quot;iPhone iPad&quot;, and each results in a response that contains promotions with both &quot;iPhone&quot; and &quot;iPad&quot; in the title.
        :param str sort: Specifies the order for how to sort the response. If you precede the supplied value with a dash, the response is sorted in reverse order. Example: &nbsp;&nbsp;&nbsp;sort=END_DATE &nbsp; Sorts the promotions in the response by their end dates in ascending order &nbsp;&nbsp;&nbsp;sort=-PROMOTION_NAME &nbsp; Sorts the promotions by their promotion name in descending alphabetical order (Z-Az-a) Valid values: START_DATE END_DATE PROMOTION_NAME For implementation help, refer to eBay API documentation at https://developer.ebay.com/api-docs/sell/marketing/types/csb:SortField
        :return: PromotionsPagedCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_promotions_with_http_info(marketplace_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_promotions_with_http_info(marketplace_id, **kwargs)  # noqa: E501
            return data

    def get_promotions_with_http_info(self, marketplace_id, **kwargs):  # noqa: E501
        """get_promotions  # noqa: E501

        This method returns a list of a seller's undeleted promotions. The call returns up to 200 currently-available promotions on the specified marketplace. While the response body does not include the promotion's discountRules or inventoryCriterion containers, it does include the promotionHref (which you can use to retrieve the complete details of the promotion). Use query parameters to sort and filter the results by the number of promotions to return, the promotion state or type, and the eBay marketplace. You can also supply keywords to limit the response to the promotions that contain that keywords in the title of the promotion. Maximum returned: 200  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_promotions_with_http_info(marketplace_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str marketplace_id: The eBay marketplace ID of the site where the promotion is hosted. Valid values: EBAY_AU = Australia EBAY_DE = Germany EBAY_ES = Spain EBAY_FR = France EBAY_GB = Great Britain EBAY_IT = Italy EBAY_US = United States (required)
        :param str limit: Specifies the maximum number of promotions returned on a page from the result set. Default: 200 Maximum: 200
        :param str offset: Specifies the number of promotions to skip in the result set before returning the first promotion in the paginated response. Combine offset with the limit query parameter to control the items returned in the response. For example, if you supply an offset of 0 and a limit of 10, the first page of the response contains the first 10 items from the complete list of items retrieved by the call. If offset is 10 and limit is 20, the first page of the response contains items 11-30 from the complete result set. Default: 0
        :param str promotion_status: Specifies the promotion state by which you want to filter the results. The response contains only those promotions that match the state you specify. Valid values: DRAFT SCHEDULED RUNNING PAUSED ENDEDMaximum number of input values: 1
        :param str promotion_type: Filters the returned promotions based on their campaign promotion type. Specify one of the following values to indicate the promotion type you want returned: MARKDOWN_SALE &ndash; A markdown promotion set with createItemPriceMarkdownPromotion. ORDER_DISCOUNT &ndash; A threshold promotion set with createItemPromotion. VOLUME_DISCOUNT &ndash; A volume pricing promotion set with createItemPromotion.
        :param str q: A string consisting of one or more keywords. eBay filters the response by returning only the promotions that contain the supplied keywords in the promotion title. Example: &quot;iPhone&quot; or &quot;Harry Potter.&quot; Commas that separate keywords are ignored. For example, a keyword string of &quot;iPhone, iPad&quot; equals &quot;iPhone iPad&quot;, and each results in a response that contains promotions with both &quot;iPhone&quot; and &quot;iPad&quot; in the title.
        :param str sort: Specifies the order for how to sort the response. If you precede the supplied value with a dash, the response is sorted in reverse order. Example: &nbsp;&nbsp;&nbsp;sort=END_DATE &nbsp; Sorts the promotions in the response by their end dates in ascending order &nbsp;&nbsp;&nbsp;sort=-PROMOTION_NAME &nbsp; Sorts the promotions by their promotion name in descending alphabetical order (Z-Az-a) Valid values: START_DATE END_DATE PROMOTION_NAME For implementation help, refer to eBay API documentation at https://developer.ebay.com/api-docs/sell/marketing/types/csb:SortField
        :return: PromotionsPagedCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['marketplace_id', 'limit', 'offset', 'promotion_status', 'promotion_type', 'q', 'sort']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_promotions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'marketplace_id' is set
        if ('marketplace_id' not in params or
                params['marketplace_id'] is None):
            raise ValueError("Missing the required parameter `marketplace_id` when calling `get_promotions`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'marketplace_id' in params:
            query_params.append(('marketplace_id', params['marketplace_id']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'promotion_status' in params:
            query_params.append(('promotion_status', params['promotion_status']))  # noqa: E501
        if 'promotion_type' in params:
            query_params.append(('promotion_type', params['promotion_type']))  # noqa: E501
        if 'q' in params:
            query_params.append(('q', params['q']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501

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
            '/promotion', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PromotionsPagedCollection',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def pause_promotion(self, promotion_id, **kwargs):  # noqa: E501
        """pause_promotion  # noqa: E501

        This method pauses a currently-active (RUNNING) threshold promotion and changes the state of the promotion from RUNNING to PAUSED. Pausing a promotion makes the promotion temporarily unavailable to buyers and any currently-incomplete transactions will not receive the promotional offer until the promotion is resumed. Also, promotion teasers are not displayed when a promotion is paused. Pass the ID of the promotion you want to pause using the promotion_id path parameter. Call getPromotions to retrieve the IDs of the seller's promotions. Note: You can only pause threshold promotions (you cannot pause markdown promotions).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pause_promotion(promotion_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str promotion_id: This path parameter takes a concatenation of the ID of the promotion you want to pause plus the marketplace ID on which the promotion is hosted. Concatenate the two values by separating them with an &quot;at sign&quot; (@). The ID of the promotion (promotionId) is a unique eBay-assigned value that's generated when the promotion is created. The Marketplace ID is the ENUM value of eBay marketplace where the promotion is hosted. Example: 115001954505@EBAY_US (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pause_promotion_with_http_info(promotion_id, **kwargs)  # noqa: E501
        else:
            (data) = self.pause_promotion_with_http_info(promotion_id, **kwargs)  # noqa: E501
            return data

    def pause_promotion_with_http_info(self, promotion_id, **kwargs):  # noqa: E501
        """pause_promotion  # noqa: E501

        This method pauses a currently-active (RUNNING) threshold promotion and changes the state of the promotion from RUNNING to PAUSED. Pausing a promotion makes the promotion temporarily unavailable to buyers and any currently-incomplete transactions will not receive the promotional offer until the promotion is resumed. Also, promotion teasers are not displayed when a promotion is paused. Pass the ID of the promotion you want to pause using the promotion_id path parameter. Call getPromotions to retrieve the IDs of the seller's promotions. Note: You can only pause threshold promotions (you cannot pause markdown promotions).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pause_promotion_with_http_info(promotion_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str promotion_id: This path parameter takes a concatenation of the ID of the promotion you want to pause plus the marketplace ID on which the promotion is hosted. Concatenate the two values by separating them with an &quot;at sign&quot; (@). The ID of the promotion (promotionId) is a unique eBay-assigned value that's generated when the promotion is created. The Marketplace ID is the ENUM value of eBay marketplace where the promotion is hosted. Example: 115001954505@EBAY_US (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['promotion_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pause_promotion" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'promotion_id' is set
        if ('promotion_id' not in params or
                params['promotion_id'] is None):
            raise ValueError("Missing the required parameter `promotion_id` when calling `pause_promotion`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'promotion_id' in params:
            path_params['promotion_id'] = params['promotion_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['api_auth']  # noqa: E501

        return self.api_client.call_api(
            '/promotion/{promotion_id}/pause', 'POST',
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

    def resume_promotion(self, promotion_id, **kwargs):  # noqa: E501
        """resume_promotion  # noqa: E501

        This method restarts a threshold promotion that was previously paused and changes the state of the promotion from PAUSED to RUNNING. Only promotions that have been previously paused can be resumed. Resuming a promotion reinstates the promotional teasers and any transactions that were in motion before the promotion was paused will again be eligible for the promotion. Pass the ID of the promotion you want to resume using the promotion_id path parameter. Call getPromotions to retrieve the IDs of the seller's promotions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.resume_promotion(promotion_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str promotion_id: This path parameter takes a concatenation of the ID of the promotion you want to resume plus the marketplace ID on which the promotion is hosted. Concatenate the two values by separating them with an &quot;at sign&quot; (@). The ID of the promotion (promotionId) is a unique eBay-assigned value that's generated when the promotion is created. The Marketplace ID is the ENUM value of eBay marketplace where the promotion is hosted. Example: 115001954505@EBAY_US (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.resume_promotion_with_http_info(promotion_id, **kwargs)  # noqa: E501
        else:
            (data) = self.resume_promotion_with_http_info(promotion_id, **kwargs)  # noqa: E501
            return data

    def resume_promotion_with_http_info(self, promotion_id, **kwargs):  # noqa: E501
        """resume_promotion  # noqa: E501

        This method restarts a threshold promotion that was previously paused and changes the state of the promotion from PAUSED to RUNNING. Only promotions that have been previously paused can be resumed. Resuming a promotion reinstates the promotional teasers and any transactions that were in motion before the promotion was paused will again be eligible for the promotion. Pass the ID of the promotion you want to resume using the promotion_id path parameter. Call getPromotions to retrieve the IDs of the seller's promotions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.resume_promotion_with_http_info(promotion_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str promotion_id: This path parameter takes a concatenation of the ID of the promotion you want to resume plus the marketplace ID on which the promotion is hosted. Concatenate the two values by separating them with an &quot;at sign&quot; (@). The ID of the promotion (promotionId) is a unique eBay-assigned value that's generated when the promotion is created. The Marketplace ID is the ENUM value of eBay marketplace where the promotion is hosted. Example: 115001954505@EBAY_US (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['promotion_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resume_promotion" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'promotion_id' is set
        if ('promotion_id' not in params or
                params['promotion_id'] is None):
            raise ValueError("Missing the required parameter `promotion_id` when calling `resume_promotion`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'promotion_id' in params:
            path_params['promotion_id'] = params['promotion_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['api_auth']  # noqa: E501

        return self.api_client.call_api(
            '/promotion/{promotion_id}/resume', 'POST',
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