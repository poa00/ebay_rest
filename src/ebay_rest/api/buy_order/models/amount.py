# coding: utf-8

"""
    Order API

    <span class=\"tablenote\"><b>Note:</b> This version of the Order API (v2) currently only supports the guest payment flow for eBay managed payments. To view the v1_beta version of the Order API, which includes both member and guest checkout payment flows, refer to the <a href=\"/api-docs/buy/order_v1/resources/methods\">Order_v1 API</a> documentation.</span><br /><br /><span class=\"tablenote\"><b>Note:</b> This is a <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#Limited\" target=\"_blank\"><img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\"  alt=\"Limited Release\" title=\"Limited Release\" />(Limited Release)</a> API available only to select developers approved by business units.</span><br /><br />The Order API provides interfaces that let shoppers pay for items. It also returns payment and shipping status of the order.  # noqa: E501

    OpenAPI spec version: v2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Amount(object):
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
        'currency': 'str',
        'value': 'str'
    }

    attribute_map = {
        'currency': 'currency',
        'value': 'value'
    }

    def __init__(self, currency=None, value=None):  # noqa: E501
        """Amount - a model defined in Swagger"""  # noqa: E501
        self._currency = None
        self._value = None
        self.discriminator = None
        if currency is not None:
            self.currency = currency
        if value is not None:
            self.value = value

    @property
    def currency(self):
        """Gets the currency of this Amount.  # noqa: E501

        The currency used in the monetary transaction. Generally, this is the currency used by the country of the eBay site offering the item. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/buy/order/types/bas:CurrencyCodeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The currency of this Amount.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Amount.

        The currency used in the monetary transaction. Generally, this is the currency used by the country of the eBay site offering the item. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/buy/order/types/bas:CurrencyCodeEnum'>eBay API documentation</a>  # noqa: E501

        :param currency: The currency of this Amount.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def value(self):
        """Gets the value of this Amount.  # noqa: E501

        The amount of the currency specified in the currency field. The value of the currency defaults to the standard currency used by the country of the eBay site offering the item.  # noqa: E501

        :return: The value of this Amount.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Amount.

        The amount of the currency specified in the currency field. The value of the currency defaults to the standard currency used by the country of the eBay site offering the item.  # noqa: E501

        :param value: The value of this Amount.  # noqa: E501
        :type: str
        """

        self._value = value

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
        if issubclass(Amount, dict):
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
        if not isinstance(other, Amount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
