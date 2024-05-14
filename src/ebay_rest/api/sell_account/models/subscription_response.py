# coding: utf-8

"""
    Account API

    The <b>Account API</b> gives sellers the ability to configure their eBay seller accounts, including the seller's policies (eBay business policies and seller-defined custom policies), opt in and out of eBay seller programs, configure sales tax tables, and get account information.  <br><br>For details on the availability of the methods in this API, see <a href=\"/api-docs/sell/account/overview.html#requirements\">Account API requirements and restrictions</a>.  # noqa: E501

    OpenAPI spec version: v1.9.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SubscriptionResponse(object):
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
        'subscriptions': 'list[Subscription]',
        'total': 'int'
    }

    attribute_map = {
        'href': 'href',
        'limit': 'limit',
        'next': 'next',
        'subscriptions': 'subscriptions',
        'total': 'total'
    }

    def __init__(self, href=None, limit=None, next=None, subscriptions=None, total=None):  # noqa: E501
        """SubscriptionResponse - a model defined in Swagger"""  # noqa: E501
        self._href = None
        self._limit = None
        self._next = None
        self._subscriptions = None
        self._total = None
        self.discriminator = None
        if href is not None:
            self.href = href
        if limit is not None:
            self.limit = limit
        if next is not None:
            self.next = next
        if subscriptions is not None:
            self.subscriptions = subscriptions
        if total is not None:
            self.total = total

    @property
    def href(self):
        """Gets the href of this SubscriptionResponse.  # noqa: E501

        This field is for future use.  # noqa: E501

        :return: The href of this SubscriptionResponse.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this SubscriptionResponse.

        This field is for future use.  # noqa: E501

        :param href: The href of this SubscriptionResponse.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def limit(self):
        """Gets the limit of this SubscriptionResponse.  # noqa: E501

        This field is for future use.  # noqa: E501

        :return: The limit of this SubscriptionResponse.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this SubscriptionResponse.

        This field is for future use.  # noqa: E501

        :param limit: The limit of this SubscriptionResponse.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def next(self):
        """Gets the next of this SubscriptionResponse.  # noqa: E501

        This field is for future use.  # noqa: E501

        :return: The next of this SubscriptionResponse.  # noqa: E501
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this SubscriptionResponse.

        This field is for future use.  # noqa: E501

        :param next: The next of this SubscriptionResponse.  # noqa: E501
        :type: str
        """

        self._next = next

    @property
    def subscriptions(self):
        """Gets the subscriptions of this SubscriptionResponse.  # noqa: E501

        An array of subscriptions associated with the seller account.  # noqa: E501

        :return: The subscriptions of this SubscriptionResponse.  # noqa: E501
        :rtype: list[Subscription]
        """
        return self._subscriptions

    @subscriptions.setter
    def subscriptions(self, subscriptions):
        """Sets the subscriptions of this SubscriptionResponse.

        An array of subscriptions associated with the seller account.  # noqa: E501

        :param subscriptions: The subscriptions of this SubscriptionResponse.  # noqa: E501
        :type: list[Subscription]
        """

        self._subscriptions = subscriptions

    @property
    def total(self):
        """Gets the total of this SubscriptionResponse.  # noqa: E501

        The total number of subscriptions displayed on the current page of results.  # noqa: E501

        :return: The total of this SubscriptionResponse.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this SubscriptionResponse.

        The total number of subscriptions displayed on the current page of results.  # noqa: E501

        :param total: The total of this SubscriptionResponse.  # noqa: E501
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
        if issubclass(SubscriptionResponse, dict):
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
        if not isinstance(other, SubscriptionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
