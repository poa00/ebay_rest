# coding: utf-8

"""
    Browse API

    The Browse API has the following resources:<ul><li><b>item_summary:</b><br>Allows shoppers to search for specific items by keyword, GTIN, category, charity, product, image <a href=\"/api-docs/static/versioning.html#experimental\" target=\"_blank\"><img src=\"/cms/img/docs/experimental-icon.svg\" class=\"legend-icon experimental-icon\" alt=\"Experimental Method\" title=\"Experimental Method\" />(Experimental Method)</a>, or item aspects and refine the results by using filters, such as aspects, compatibility, and fields values, or UI parameters.</li><li><b>item:</b><br>Allows shoppers to retrieve the details of a specific item or all items in an item group, which is an item with variations such as color and size and check if a product is compatible with the specified item, such as if a specific car is compatible with a specific part.<br><br>This resource also provides a bridge between the eBay legacy APIs, such as the <a href=\"/api-docs/user-guides/static/finding-user-guide-landing.html\" target=\"_blank\">Finding</b>, and the RESTful APIs, which use different formats for the item IDs.</li></ul>The <b>item_summary</b>, <b>search_by_image</b>, and <b>item</b> resource calls require an <a href=\"/api-docs/static/oauth-client-credentials-grant.html\" target=\"_blank\">Application access token</a>.  # noqa: E501

    OpenAPI spec version: v1.19.7
    
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

        The list of valid currencies. Each <a href=\"https://www.iso.org/iso-4217-currency-codes.html \" target=\"_blank\">ISO 4217</a> currency code includes the currency name followed by the numeric value.<br><br>For example, the Canadian Dollar code (CAD) would take the following form: <code>Canadian Dollar, 124</code>. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/buy/browse/types/ba:CurrencyCodeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The currency of this Amount.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Amount.

        The list of valid currencies. Each <a href=\"https://www.iso.org/iso-4217-currency-codes.html \" target=\"_blank\">ISO 4217</a> currency code includes the currency name followed by the numeric value.<br><br>For example, the Canadian Dollar code (CAD) would take the following form: <code>Canadian Dollar, 124</code>. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/buy/browse/types/ba:CurrencyCodeEnum'>eBay API documentation</a>  # noqa: E501

        :param currency: The currency of this Amount.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def value(self):
        """Gets the value of this Amount.  # noqa: E501

        The value of the discounted amount.  # noqa: E501

        :return: The value of this Amount.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Amount.

        The value of the discounted amount.  # noqa: E501

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
