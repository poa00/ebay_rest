# coding: utf-8

"""
    Account API

    The <b>Account API</b> gives sellers the ability to configure their eBay seller accounts, including the seller's policies (seller-defined custom policies and eBay business policies), opt in and out of eBay seller programs, configure sales tax tables, and get account information.  <br><br>For details on the availability of the methods in this API, see <a href=\"/api-docs/sell/account/overview.html#requirements\">Account API requirements and restrictions</a>.  # noqa: E501

    OpenAPI spec version: v1.7.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CustomPolicyResponse(object):
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
        'custom_policies': 'list[CompactCustomPolicyResponse]',
        'href': 'str',
        'limit': 'int',
        'next': 'str',
        'offset': 'int',
        'prev': 'str',
        'total': 'int'
    }

    attribute_map = {
        'custom_policies': 'customPolicies',
        'href': 'href',
        'limit': 'limit',
        'next': 'next',
        'offset': 'offset',
        'prev': 'prev',
        'total': 'total'
    }

    def __init__(self, custom_policies=None, href=None, limit=None, next=None, offset=None, prev=None, total=None):  # noqa: E501
        """CustomPolicyResponse - a model defined in Swagger"""  # noqa: E501
        self._custom_policies = None
        self._href = None
        self._limit = None
        self._next = None
        self._offset = None
        self._prev = None
        self._total = None
        self.discriminator = None
        if custom_policies is not None:
            self.custom_policies = custom_policies
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
    def custom_policies(self):
        """Gets the custom_policies of this CustomPolicyResponse.  # noqa: E501

        This array contains the custom policies that match the input criteria.  # noqa: E501

        :return: The custom_policies of this CustomPolicyResponse.  # noqa: E501
        :rtype: list[CompactCustomPolicyResponse]
        """
        return self._custom_policies

    @custom_policies.setter
    def custom_policies(self, custom_policies):
        """Sets the custom_policies of this CustomPolicyResponse.

        This array contains the custom policies that match the input criteria.  # noqa: E501

        :param custom_policies: The custom_policies of this CustomPolicyResponse.  # noqa: E501
        :type: list[CompactCustomPolicyResponse]
        """

        self._custom_policies = custom_policies

    @property
    def href(self):
        """Gets the href of this CustomPolicyResponse.  # noqa: E501

        <i>This field is for future use.</i>  # noqa: E501

        :return: The href of this CustomPolicyResponse.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this CustomPolicyResponse.

        <i>This field is for future use.</i>  # noqa: E501

        :param href: The href of this CustomPolicyResponse.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def limit(self):
        """Gets the limit of this CustomPolicyResponse.  # noqa: E501

        <i>This field is for future use.</i>  # noqa: E501

        :return: The limit of this CustomPolicyResponse.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this CustomPolicyResponse.

        <i>This field is for future use.</i>  # noqa: E501

        :param limit: The limit of this CustomPolicyResponse.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def next(self):
        """Gets the next of this CustomPolicyResponse.  # noqa: E501

        <i>This field is for future use.</i>  # noqa: E501

        :return: The next of this CustomPolicyResponse.  # noqa: E501
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this CustomPolicyResponse.

        <i>This field is for future use.</i>  # noqa: E501

        :param next: The next of this CustomPolicyResponse.  # noqa: E501
        :type: str
        """

        self._next = next

    @property
    def offset(self):
        """Gets the offset of this CustomPolicyResponse.  # noqa: E501

        <i>This field is for future use.</i>  # noqa: E501

        :return: The offset of this CustomPolicyResponse.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this CustomPolicyResponse.

        <i>This field is for future use.</i>  # noqa: E501

        :param offset: The offset of this CustomPolicyResponse.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def prev(self):
        """Gets the prev of this CustomPolicyResponse.  # noqa: E501

        <i>This field is for future use.</i>  # noqa: E501

        :return: The prev of this CustomPolicyResponse.  # noqa: E501
        :rtype: str
        """
        return self._prev

    @prev.setter
    def prev(self, prev):
        """Sets the prev of this CustomPolicyResponse.

        <i>This field is for future use.</i>  # noqa: E501

        :param prev: The prev of this CustomPolicyResponse.  # noqa: E501
        :type: str
        """

        self._prev = prev

    @property
    def total(self):
        """Gets the total of this CustomPolicyResponse.  # noqa: E501

        <i>This field is for future use.</i>  # noqa: E501

        :return: The total of this CustomPolicyResponse.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this CustomPolicyResponse.

        <i>This field is for future use.</i>  # noqa: E501

        :param total: The total of this CustomPolicyResponse.  # noqa: E501
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
        if issubclass(CustomPolicyResponse, dict):
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
        if not isinstance(other, CustomPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
