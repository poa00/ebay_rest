# coding: utf-8

"""
    Notification API

    The eBay Notification API enables management of the entire end-to-end eBay notification experience by allowing users to:<ul><li>Browse for supported notification topics and retrieve topic details</li><li>Create, configure, and manage notification destination endpoints</li><li>Configure, manage, and test notification subscriptions</li><li>Process eBay notifications and verify the integrity of the message payload</li></ul>  # noqa: E501

    OpenAPI spec version: v1.5.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ...commerce_notification.api_client import ApiClient


class TopicApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_topic(self, topic_id, **kwargs):  # noqa: E501
        """get_topic  # noqa: E501

        This method allows applications to retrieve details for the specified topic. This information includes supported schema versions, formats, and other metadata for the topic.<br><br>Applications can subscribe to any of the topics for a supported schema version and format, limited by the authorization scopes required to subscribe to the topic.<br><br>A topic specifies the type of information to be received and the data types associated with an event. An event occurs in the eBay system, such as when a user requests deletion or revokes access for an application. An event is an instance of an event type (topic).<br><br>Specify the topic to retrieve using the <b>topic_id</b> URI parameter.<br><br><span class=\"tablenote\"><b>Note:</b> Use the <a href=\"/api-docs/commerce/notification/resources/topic/methods/getTopics\">getTopics</a> method to find a topic if you do not know the topic ID.</span>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_topic(topic_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str topic_id: The unique identifier of the notification topic for which the details are retrieved. Use <b>getTopics</b> to retrieve the topic ID. (required)
        :return: Topic
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_topic_with_http_info(topic_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_topic_with_http_info(topic_id, **kwargs)  # noqa: E501
            return data

    def get_topic_with_http_info(self, topic_id, **kwargs):  # noqa: E501
        """get_topic  # noqa: E501

        This method allows applications to retrieve details for the specified topic. This information includes supported schema versions, formats, and other metadata for the topic.<br><br>Applications can subscribe to any of the topics for a supported schema version and format, limited by the authorization scopes required to subscribe to the topic.<br><br>A topic specifies the type of information to be received and the data types associated with an event. An event occurs in the eBay system, such as when a user requests deletion or revokes access for an application. An event is an instance of an event type (topic).<br><br>Specify the topic to retrieve using the <b>topic_id</b> URI parameter.<br><br><span class=\"tablenote\"><b>Note:</b> Use the <a href=\"/api-docs/commerce/notification/resources/topic/methods/getTopics\">getTopics</a> method to find a topic if you do not know the topic ID.</span>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_topic_with_http_info(topic_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str topic_id: The unique identifier of the notification topic for which the details are retrieved. Use <b>getTopics</b> to retrieve the topic ID. (required)
        :return: Topic
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['topic_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_topic" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'topic_id' is set
        if ('topic_id' not in params or
                params['topic_id'] is None):
            raise ValueError("Missing the required parameter `topic_id` when calling `get_topic`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'topic_id' in params:
            path_params['topic_id'] = params['topic_id']  # noqa: E501

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
            '/topic/{topic_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Topic',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_topics(self, **kwargs):  # noqa: E501
        """get_topics  # noqa: E501

        This method returns a paginated collection of all supported topics, along with the details for the topics. This information includes supported schema versions, formats, and other metadata for the topics.<br><br>Applications can subscribe to any of the topics for a supported schema version and format, limited by the authorization scopes required to subscribe to the topic.<br><br>A topic specifies the type of information to be received and the data types associated with an event. An event occurs in the eBay system, such as when a user requests deletion or revokes access for an application. An event is an instance of an event type (topic).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_topics(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str continuation_token: This string value can be used to return the next page in the result set. The string to use here is returned in the <b>next</b> field of the current page of results.
        :param str limit: The maximum number of notification topics to return per page from the result set.<br><br><b>Min:</b> 10<br><br><b>Max:</b> 100<br><br><b>Default:</b> 20
        :return: TopicSearchResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_topics_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_topics_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_topics_with_http_info(self, **kwargs):  # noqa: E501
        """get_topics  # noqa: E501

        This method returns a paginated collection of all supported topics, along with the details for the topics. This information includes supported schema versions, formats, and other metadata for the topics.<br><br>Applications can subscribe to any of the topics for a supported schema version and format, limited by the authorization scopes required to subscribe to the topic.<br><br>A topic specifies the type of information to be received and the data types associated with an event. An event occurs in the eBay system, such as when a user requests deletion or revokes access for an application. An event is an instance of an event type (topic).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_topics_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str continuation_token: This string value can be used to return the next page in the result set. The string to use here is returned in the <b>next</b> field of the current page of results.
        :param str limit: The maximum number of notification topics to return per page from the result set.<br><br><b>Min:</b> 10<br><br><b>Max:</b> 100<br><br><b>Default:</b> 20
        :return: TopicSearchResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['continuation_token', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_topics" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'continuation_token' in params:
            query_params.append(('continuation_token', params['continuation_token']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/topic', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TopicSearchResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
