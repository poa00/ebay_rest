# coding: utf-8

"""
    Buy Marketing API

    The Marketing API retrieves eBay products based on a metric, such as Best Selling, as well as products that were also bought and also viewed.  # noqa: E501

    OpenAPI spec version: v1_beta.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from buy_marketing.api_client import ApiClient


class MerchandisedProductApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_also_bought_by_product(self, **kwargs):  # noqa: E501
        """get_also_bought_by_product  # noqa: E501

        This method returns products that were also bought when shoppers bought the product specified in the request. Showing 'also bought' products inspires up-selling and cross-selling. You specify the product by one of the following: epid - eBay Product ID gtin - Global Trade Item Number (UPC, ISBN, EAN) brand - (brand name, such as Nike) plus mpn (Manufacturer's Part Number) Restrictions For a list of supported sites and other restrictions, see API Restrictions. Note: A maximum of 12 products are returned. The method will return up to 12 products, but it can be less than 12. If the number of products found is less than 12, the method will return all of the products matching the criteria.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_also_bought_by_product(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str brand: The brand of the product. Restriction: This must be used along with mpn. Required: You must specify one epid, or one gtin, or one brand plus mpn pair.
        :param str epid: The eBay product identifier of a product. Required: You must specify one epid, or one gtin, or one brand plus mpn pair.
        :param str gtin: The unique Global Trade Item Number of the item as defined by https://www.gtin.info. This can be a UPC (Universal Product Code), EAN (European Article Number), or an ISBN (International Standard Book Number value. Required: You must specify one epid, or one gtin, or one brand plus mpn pair.
        :param str mpn: The manufacturer part number of the product. Restriction: This must be used along with brand. Required: You must specify one epid, or one gtin, or one brand plus mpn pair.
        :return: BestSellingProductResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_also_bought_by_product_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_also_bought_by_product_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_also_bought_by_product_with_http_info(self, **kwargs):  # noqa: E501
        """get_also_bought_by_product  # noqa: E501

        This method returns products that were also bought when shoppers bought the product specified in the request. Showing 'also bought' products inspires up-selling and cross-selling. You specify the product by one of the following: epid - eBay Product ID gtin - Global Trade Item Number (UPC, ISBN, EAN) brand - (brand name, such as Nike) plus mpn (Manufacturer's Part Number) Restrictions For a list of supported sites and other restrictions, see API Restrictions. Note: A maximum of 12 products are returned. The method will return up to 12 products, but it can be less than 12. If the number of products found is less than 12, the method will return all of the products matching the criteria.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_also_bought_by_product_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str brand: The brand of the product. Restriction: This must be used along with mpn. Required: You must specify one epid, or one gtin, or one brand plus mpn pair.
        :param str epid: The eBay product identifier of a product. Required: You must specify one epid, or one gtin, or one brand plus mpn pair.
        :param str gtin: The unique Global Trade Item Number of the item as defined by https://www.gtin.info. This can be a UPC (Universal Product Code), EAN (European Article Number), or an ISBN (International Standard Book Number value. Required: You must specify one epid, or one gtin, or one brand plus mpn pair.
        :param str mpn: The manufacturer part number of the product. Restriction: This must be used along with brand. Required: You must specify one epid, or one gtin, or one brand plus mpn pair.
        :return: BestSellingProductResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['brand', 'epid', 'gtin', 'mpn']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_also_bought_by_product" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'brand' in params:
            query_params.append(('brand', params['brand']))  # noqa: E501
        if 'epid' in params:
            query_params.append(('epid', params['epid']))  # noqa: E501
        if 'gtin' in params:
            query_params.append(('gtin', params['gtin']))  # noqa: E501
        if 'mpn' in params:
            query_params.append(('mpn', params['mpn']))  # noqa: E501

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
            '/merchandised_product/get_also_bought_products', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BestSellingProductResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_also_viewed_by_product(self, **kwargs):  # noqa: E501
        """get_also_viewed_by_product  # noqa: E501

        This method returns products that were also viewed when shoppers viewed the product specified in the request. Showing 'also viewed' products encourages up-selling and cross-selling. You specify the product by one of the following: epid - eBay Product ID gtin - Global Trade Item Number (UPC, ISBN, EAN) brand (brand name, such as Nike) plus mpn (Manufacturer's Part Number) Restrictions For a list of supported sites and other restrictions, see API Restrictions. Note: A maximum of 12 products are returned. The method will return up to 12 products, but it can be less than 12. If the number of products found is less than 12, the method will return all of the products matching the criteria.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_also_viewed_by_product(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str brand: The brand of the product. Restriction: This must be used along with mpn. Required: You must specify one epid, or one gtin, or one brand plus mpn pair.
        :param str epid: The eBay product identifier of a product. Required: You must specify one epid, or one gtin, or one brand plus mpn pair.
        :param str gtin: The unique Global Trade Item Number of the item as defined by https://www.gtin.info. This can be a UPC (Universal Product Code), EAN (European Article Number), or an ISBN (International Standard Book Number value. Required: You must specify one epid, or one gtin, or one brand plus mpn pair.
        :param str mpn: The manufacturer part number of the product. Restriction: This must be used along with brand.
        :return: BestSellingProductResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_also_viewed_by_product_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_also_viewed_by_product_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_also_viewed_by_product_with_http_info(self, **kwargs):  # noqa: E501
        """get_also_viewed_by_product  # noqa: E501

        This method returns products that were also viewed when shoppers viewed the product specified in the request. Showing 'also viewed' products encourages up-selling and cross-selling. You specify the product by one of the following: epid - eBay Product ID gtin - Global Trade Item Number (UPC, ISBN, EAN) brand (brand name, such as Nike) plus mpn (Manufacturer's Part Number) Restrictions For a list of supported sites and other restrictions, see API Restrictions. Note: A maximum of 12 products are returned. The method will return up to 12 products, but it can be less than 12. If the number of products found is less than 12, the method will return all of the products matching the criteria.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_also_viewed_by_product_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str brand: The brand of the product. Restriction: This must be used along with mpn. Required: You must specify one epid, or one gtin, or one brand plus mpn pair.
        :param str epid: The eBay product identifier of a product. Required: You must specify one epid, or one gtin, or one brand plus mpn pair.
        :param str gtin: The unique Global Trade Item Number of the item as defined by https://www.gtin.info. This can be a UPC (Universal Product Code), EAN (European Article Number), or an ISBN (International Standard Book Number value. Required: You must specify one epid, or one gtin, or one brand plus mpn pair.
        :param str mpn: The manufacturer part number of the product. Restriction: This must be used along with brand.
        :return: BestSellingProductResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['brand', 'epid', 'gtin', 'mpn']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_also_viewed_by_product" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'brand' in params:
            query_params.append(('brand', params['brand']))  # noqa: E501
        if 'epid' in params:
            query_params.append(('epid', params['epid']))  # noqa: E501
        if 'gtin' in params:
            query_params.append(('gtin', params['gtin']))  # noqa: E501
        if 'mpn' in params:
            query_params.append(('mpn', params['mpn']))  # noqa: E501

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
            '/merchandised_product/get_also_viewed_products', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BestSellingProductResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_merchandised_products(self, category_id, metric_name, **kwargs):  # noqa: E501
        """get_merchandised_products  # noqa: E501

        This method returns an array of products based on the category and metric specified. This includes details of the product, such as the eBay product ID (EPID), title, and user reviews and ratings for the product. You can use the epid returned by this method in the Browse API search method to retrieve items for this product. Restrictions To test getMerchandisedProducts in Sandbox, you must use category ID 9355 and the response will be mock data. For a list of supported sites and other restrictions, see API Restrictions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_merchandised_products(category_id, metric_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str category_id: This query parameter limits the products returned to a specific eBay category. The list of eBay category IDs is not published and category IDs are not all the same across all the eBay maketplace. You can use the following techniques to find a category by site: Use the Category Changes page. Use the Taxonomy API. For details see Get Categories for Buy APIs. Use the Browse API and submit the following method to get the dominantCategoryId for an item. /buy/browse/v1/item_summary/search?q=keyword&amp;fieldgroups=ASPECT_REFINEMENTS Maximum: 1 Required: 1 (required)
        :param str metric_name: This value filters the result set by the specified metric. Only products in this metric are returned. Currently, the only metric supported is BEST_SELLING. Default: BEST_SELLING Maximum: 1 Required: 1 (required)
        :param str aspect_filter: The aspect name/value pairs used to further refine product results. For example: &nbsp;&nbsp;&nbsp;/buy/marketing/v1_beta/merchandised_product?category_id=31388&amp;metric_name=BEST_SELLING&amp;aspect_filter=Brand:Canon You can use the Browse API search method with the fieldgroups=ASPECT_REFINEMENTS field to return the aspects of a product. For implementation help, refer to eBay API documentation at https://developer.ebay.com/api-docs/buy/marketing/types/gct:MarketingAspectFilter
        :param str limit: This value specifies the maximum number of products to return in a result set. Note: Maximum value means the method will return up to that many products per set, but it can be less than this value. If the number of products found is less than this value, the method will return all of the products matching the criteria. Default: 8 Maximum: 100
        :return: BestSellingProductResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_merchandised_products_with_http_info(category_id, metric_name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_merchandised_products_with_http_info(category_id, metric_name, **kwargs)  # noqa: E501
            return data

    def get_merchandised_products_with_http_info(self, category_id, metric_name, **kwargs):  # noqa: E501
        """get_merchandised_products  # noqa: E501

        This method returns an array of products based on the category and metric specified. This includes details of the product, such as the eBay product ID (EPID), title, and user reviews and ratings for the product. You can use the epid returned by this method in the Browse API search method to retrieve items for this product. Restrictions To test getMerchandisedProducts in Sandbox, you must use category ID 9355 and the response will be mock data. For a list of supported sites and other restrictions, see API Restrictions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_merchandised_products_with_http_info(category_id, metric_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str category_id: This query parameter limits the products returned to a specific eBay category. The list of eBay category IDs is not published and category IDs are not all the same across all the eBay maketplace. You can use the following techniques to find a category by site: Use the Category Changes page. Use the Taxonomy API. For details see Get Categories for Buy APIs. Use the Browse API and submit the following method to get the dominantCategoryId for an item. /buy/browse/v1/item_summary/search?q=keyword&amp;fieldgroups=ASPECT_REFINEMENTS Maximum: 1 Required: 1 (required)
        :param str metric_name: This value filters the result set by the specified metric. Only products in this metric are returned. Currently, the only metric supported is BEST_SELLING. Default: BEST_SELLING Maximum: 1 Required: 1 (required)
        :param str aspect_filter: The aspect name/value pairs used to further refine product results. For example: &nbsp;&nbsp;&nbsp;/buy/marketing/v1_beta/merchandised_product?category_id=31388&amp;metric_name=BEST_SELLING&amp;aspect_filter=Brand:Canon You can use the Browse API search method with the fieldgroups=ASPECT_REFINEMENTS field to return the aspects of a product. For implementation help, refer to eBay API documentation at https://developer.ebay.com/api-docs/buy/marketing/types/gct:MarketingAspectFilter
        :param str limit: This value specifies the maximum number of products to return in a result set. Note: Maximum value means the method will return up to that many products per set, but it can be less than this value. If the number of products found is less than this value, the method will return all of the products matching the criteria. Default: 8 Maximum: 100
        :return: BestSellingProductResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['category_id', 'metric_name', 'aspect_filter', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_merchandised_products" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'category_id' is set
        if ('category_id' not in params or
                params['category_id'] is None):
            raise ValueError("Missing the required parameter `category_id` when calling `get_merchandised_products`")  # noqa: E501
        # verify the required parameter 'metric_name' is set
        if ('metric_name' not in params or
                params['metric_name'] is None):
            raise ValueError("Missing the required parameter `metric_name` when calling `get_merchandised_products`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'aspect_filter' in params:
            query_params.append(('aspect_filter', params['aspect_filter']))  # noqa: E501
        if 'category_id' in params:
            query_params.append(('category_id', params['category_id']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'metric_name' in params:
            query_params.append(('metric_name', params['metric_name']))  # noqa: E501

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
            '/merchandised_product', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BestSellingProductResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
