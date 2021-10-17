# coding: utf-8

"""
    Notification API

    The eBay Notification API enables management of the entire end-to-end eBay notification experience by allowing users to:<ul><li>Browse for supported notification topics and retrieve topic details</li><li>Create, configure, and manage notification destination endpionts</li><li>Configure, manage, and test notification subscriptions</li><li>Process eBay notifications and verify the integrity of the message payload</li></ul>  # noqa: E501

    OpenAPI spec version: v1.2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class TopicSearchResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'href': 'str',
        'limit': 'int',
        'next': 'str',
        'topics': 'list[Topic]',
        'total': 'int'
    }

    attribute_map = {
        'href': 'href',
        'limit': 'limit',
        'next': 'next',
        'topics': 'topics',
        'total': 'total'
    }

    def __init__(self, href=None, limit=None, next=None, topics=None, total=None):  # noqa: E501
        """TopicSearchResponse - a model defined in Swagger"""  # noqa: E501
        self._href = None
        self._limit = None
        self._next = None
        self._topics = None
        self._total = None
        self.discriminator = None
        if href is not None:
            self.href = href
        if limit is not None:
            self.limit = limit
        if next is not None:
            self.next = next
        if topics is not None:
            self.topics = topics
        if total is not None:
            self.total = total

    @property
    def href(self):
        """Gets the href of this TopicSearchResponse.  # noqa: E501

        The path to the call URI that produced the current page of results.  # noqa: E501

        :return: The href of this TopicSearchResponse.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this TopicSearchResponse.

        The path to the call URI that produced the current page of results.  # noqa: E501

        :param href: The href of this TopicSearchResponse.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def limit(self):
        """Gets the limit of this TopicSearchResponse.  # noqa: E501

        The value of the limit parameter submitted in the request, which is the maximum number of items to return per page, from the result set. A result set is the complete set of results returned by the method.<br /><br /><span class=\"tablenote\"><b>Note:</b> Though this parameter is not required to be submitted in the request, the parameter defaults to <code>20</code> if omitted.</span>  # noqa: E501

        :return: The limit of this TopicSearchResponse.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this TopicSearchResponse.

        The value of the limit parameter submitted in the request, which is the maximum number of items to return per page, from the result set. A result set is the complete set of results returned by the method.<br /><br /><span class=\"tablenote\"><b>Note:</b> Though this parameter is not required to be submitted in the request, the parameter defaults to <code>20</code> if omitted.</span>  # noqa: E501

        :param limit: The limit of this TopicSearchResponse.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def next(self):
        """Gets the next of this TopicSearchResponse.  # noqa: E501

        The URL to access the next set of results. This field includes a <strong>continuation_token</strong>. No <b>prev</b> field is returned, but this value is persistent during the session so that you can use it to return to the next page.<br><br>This field is not returned if fewer records than specified by the <strong>limit</strong> field are returned.  # noqa: E501

        :return: The next of this TopicSearchResponse.  # noqa: E501
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this TopicSearchResponse.

        The URL to access the next set of results. This field includes a <strong>continuation_token</strong>. No <b>prev</b> field is returned, but this value is persistent during the session so that you can use it to return to the next page.<br><br>This field is not returned if fewer records than specified by the <strong>limit</strong> field are returned.  # noqa: E501

        :param next: The next of this TopicSearchResponse.  # noqa: E501
        :type: str
        """

        self._next = next

    @property
    def topics(self):
        """Gets the topics of this TopicSearchResponse.  # noqa: E501

        An array of topics that match the specified criteria.  # noqa: E501

        :return: The topics of this TopicSearchResponse.  # noqa: E501
        :rtype: list[Topic]
        """
        return self._topics

    @topics.setter
    def topics(self, topics):
        """Sets the topics of this TopicSearchResponse.

        An array of topics that match the specified criteria.  # noqa: E501

        :param topics: The topics of this TopicSearchResponse.  # noqa: E501
        :type: list[Topic]
        """

        self._topics = topics

    @property
    def total(self):
        """Gets the total of this TopicSearchResponse.  # noqa: E501

        The total number of matches for the search criteria.  # noqa: E501

        :return: The total of this TopicSearchResponse.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this TopicSearchResponse.

        The total number of matches for the search criteria.  # noqa: E501

        :param total: The total of this TopicSearchResponse.  # noqa: E501
        :type: int
        """

        self._total = total

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(TopicSearchResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TopicSearchResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
