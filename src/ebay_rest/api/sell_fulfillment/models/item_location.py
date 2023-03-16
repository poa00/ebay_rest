# coding: utf-8

"""
    Fulfillment API

    Use the Fulfillment API to complete the process of packaging, addressing, handling, and shipping each order on behalf of the seller, in accordance with the payment method and timing specified at checkout.  # noqa: E501

    OpenAPI spec version: v1.19.19
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ItemLocation(object):
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
        'country_code': 'str',
        'location': 'str',
        'postal_code': 'str'
    }

    attribute_map = {
        'country_code': 'countryCode',
        'location': 'location',
        'postal_code': 'postalCode'
    }

    def __init__(self, country_code=None, location=None, postal_code=None):  # noqa: E501
        """ItemLocation - a model defined in Swagger"""  # noqa: E501
        self._country_code = None
        self._location = None
        self._postal_code = None
        self.discriminator = None
        if country_code is not None:
            self.country_code = country_code
        if location is not None:
            self.location = location
        if postal_code is not None:
            self.postal_code = postal_code

    @property
    def country_code(self):
        """Gets the country_code of this ItemLocation.  # noqa: E501

        The two-letter <a href=\"https://www.iso.org/iso-3166-country-codes.html \" title=\"https://www.iso.org \" target=\"_blank\">ISO 3166</a> code representing the country of the address. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/ba:CountryCodeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The country_code of this ItemLocation.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this ItemLocation.

        The two-letter <a href=\"https://www.iso.org/iso-3166-country-codes.html \" title=\"https://www.iso.org \" target=\"_blank\">ISO 3166</a> code representing the country of the address. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/ba:CountryCodeEnum'>eBay API documentation</a>  # noqa: E501

        :param country_code: The country_code of this ItemLocation.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def location(self):
        """Gets the location of this ItemLocation.  # noqa: E501

        Indicates the geographical location of the item (along with the value in the <strong>countryCode</strong> field). This field provides city, province, state, or similar information.  # noqa: E501

        :return: The location of this ItemLocation.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this ItemLocation.

        Indicates the geographical location of the item (along with the value in the <strong>countryCode</strong> field). This field provides city, province, state, or similar information.  # noqa: E501

        :param location: The location of this ItemLocation.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def postal_code(self):
        """Gets the postal_code of this ItemLocation.  # noqa: E501

        The postal code of the address.  # noqa: E501

        :return: The postal_code of this ItemLocation.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this ItemLocation.

        The postal code of the address.  # noqa: E501

        :param postal_code: The postal_code of this ItemLocation.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

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
        if issubclass(ItemLocation, dict):
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
        if not isinstance(other, ItemLocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
