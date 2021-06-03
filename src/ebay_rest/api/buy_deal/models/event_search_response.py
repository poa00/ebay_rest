# coding: utf-8

"""
    Deal API

    <span class=\"tablenote\"><b>Note:</b> This is a <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited\" target=\"_blank\"> <img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"  alt=\"Limited Release\" />(Limited Release)</a> API available only to select developers approved by business units.</span><br /><br />This API allows third-party developers to search for and retrieve details about eBay deals and events, as well as the items associated with those deals and events.  # noqa: E501

    OpenAPI spec version: v1.3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class EventSearchResponse(object):
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
        'events': 'list[Event]',
        'href': 'str',
        'limit': 'int',
        'next': 'str',
        'offset': 'int',
        'prev': 'str',
        'total': 'int'
    }

    attribute_map = {
        'events': 'events',
        'href': 'href',
        'limit': 'limit',
        'next': 'next',
        'offset': 'offset',
        'prev': 'prev',
        'total': 'total'
    }

    def __init__(self, events=None, href=None, limit=None, next=None, offset=None, prev=None, total=None):  # noqa: E501
        """EventSearchResponse - a model defined in Swagger"""  # noqa: E501
        self._events = None
        self._href = None
        self._limit = None
        self._next = None
        self._offset = None
        self._prev = None
        self._total = None
        self.discriminator = None
        if events is not None:
            self.events = events
        if href is not None:
            self.href = href
        if limit is not None:
            self.limit = limit
        if next is not None:
            self.next = next
        if offset is not None:
            self.offset = offset
        if prev is not None:
            self.prev = prev
        if total is not None:
            self.total = total

    @property
    def events(self):
        """Gets the events of this EventSearchResponse.  # noqa: E501

        A list of results that match the search criteria.  # noqa: E501

        :return: The events of this EventSearchResponse.  # noqa: E501
        :rtype: list[Event]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this EventSearchResponse.

        A list of results that match the search criteria.  # noqa: E501

        :param events: The events of this EventSearchResponse.  # noqa: E501
        :type: list[Event]
        """

        self._events = events

    @property
    def href(self):
        """Gets the href of this EventSearchResponse.  # noqa: E501

        The relative path to the current set of results.  # noqa: E501

        :return: The href of this EventSearchResponse.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this EventSearchResponse.

        The relative path to the current set of results.  # noqa: E501

        :param href: The href of this EventSearchResponse.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def limit(self):
        """Gets the limit of this EventSearchResponse.  # noqa: E501

        The maximum number of items, from the current result set, returned on a single page. Default: 20  # noqa: E501

        :return: The limit of this EventSearchResponse.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this EventSearchResponse.

        The maximum number of items, from the current result set, returned on a single page. Default: 20  # noqa: E501

        :param limit: The limit of this EventSearchResponse.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def next(self):
        """Gets the next of this EventSearchResponse.  # noqa: E501

        The relative path to the next set of results.  # noqa: E501

        :return: The next of this EventSearchResponse.  # noqa: E501
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this EventSearchResponse.

        The relative path to the next set of results.  # noqa: E501

        :param next: The next of this EventSearchResponse.  # noqa: E501
        :type: str
        """

        self._next = next

    @property
    def offset(self):
        """Gets the offset of this EventSearchResponse.  # noqa: E501

        The number of items that will be skipped in the result set. This is used with the limit field to control the pagination of the output. For example, if the offset is set to 0 and the limit is set to 10, the method will retrieve items 1 through 10 from the list of items returned. If the offset is set to 10 and the limit is set to 10, the method will retrieve items 11 through 20 from the list of items returned. Default: 0  # noqa: E501

        :return: The offset of this EventSearchResponse.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this EventSearchResponse.

        The number of items that will be skipped in the result set. This is used with the limit field to control the pagination of the output. For example, if the offset is set to 0 and the limit is set to 10, the method will retrieve items 1 through 10 from the list of items returned. If the offset is set to 10 and the limit is set to 10, the method will retrieve items 11 through 20 from the list of items returned. Default: 0  # noqa: E501

        :param offset: The offset of this EventSearchResponse.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def prev(self):
        """Gets the prev of this EventSearchResponse.  # noqa: E501

        The relative path to the previous set of results.  # noqa: E501

        :return: The prev of this EventSearchResponse.  # noqa: E501
        :rtype: str
        """
        return self._prev

    @prev.setter
    def prev(self, prev):
        """Sets the prev of this EventSearchResponse.

        The relative path to the previous set of results.  # noqa: E501

        :param prev: The prev of this EventSearchResponse.  # noqa: E501
        :type: str
        """

        self._prev = prev

    @property
    def total(self):
        """Gets the total of this EventSearchResponse.  # noqa: E501

        The total number of matches for the specified search criteria.  # noqa: E501

        :return: The total of this EventSearchResponse.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this EventSearchResponse.

        The total number of matches for the specified search criteria.  # noqa: E501

        :param total: The total of this EventSearchResponse.  # noqa: E501
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
        if issubclass(EventSearchResponse, dict):
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
        if not isinstance(other, EventSearchResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
