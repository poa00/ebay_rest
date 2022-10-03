# coding: utf-8

"""
    Fulfillment API

    Use the Fulfillment API to complete the process of packaging, addressing, handling, and shipping each order on behalf of the seller, in accordance with the payment method and timing specified at checkout.  # noqa: E501

    OpenAPI spec version: v1.19.15
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class TaxAddress(object):
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
        'city': 'str',
        'country_code': 'str',
        'postal_code': 'str',
        'state_or_province': 'str'
    }

    attribute_map = {
        'city': 'city',
        'country_code': 'countryCode',
        'postal_code': 'postalCode',
        'state_or_province': 'stateOrProvince'
    }

    def __init__(self, city=None, country_code=None, postal_code=None, state_or_province=None):  # noqa: E501
        """TaxAddress - a model defined in Swagger"""  # noqa: E501
        self._city = None
        self._country_code = None
        self._postal_code = None
        self._state_or_province = None
        self.discriminator = None
        if city is not None:
            self.city = city
        if country_code is not None:
            self.country_code = country_code
        if postal_code is not None:
            self.postal_code = postal_code
        if state_or_province is not None:
            self.state_or_province = state_or_province

    @property
    def city(self):
        """Gets the city of this TaxAddress.  # noqa: E501

        The city name that can be used by sellers for tax purpose.  # noqa: E501

        :return: The city of this TaxAddress.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this TaxAddress.

        The city name that can be used by sellers for tax purpose.  # noqa: E501

        :param city: The city of this TaxAddress.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def country_code(self):
        """Gets the country_code of this TaxAddress.  # noqa: E501

        The country code that can be used by sellers for tax purpose, represented as a two-letter ISO 3166-1 alpha-2 country code. For example, <strong>US</strong> represents the United States, and <strong>DE</strong> represents Germany. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/ba:CountryCodeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The country_code of this TaxAddress.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this TaxAddress.

        The country code that can be used by sellers for tax purpose, represented as a two-letter ISO 3166-1 alpha-2 country code. For example, <strong>US</strong> represents the United States, and <strong>DE</strong> represents Germany. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/ba:CountryCodeEnum'>eBay API documentation</a>  # noqa: E501

        :param country_code: The country_code of this TaxAddress.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def postal_code(self):
        """Gets the postal_code of this TaxAddress.  # noqa: E501

        The postal code that can be used by sellers for tax purpose. Usually referred to as Zip codes in the US.  # noqa: E501

        :return: The postal_code of this TaxAddress.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this TaxAddress.

        The postal code that can be used by sellers for tax purpose. Usually referred to as Zip codes in the US.  # noqa: E501

        :param postal_code: The postal_code of this TaxAddress.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def state_or_province(self):
        """Gets the state_or_province of this TaxAddress.  # noqa: E501

        The state name that can be used by sellers for tax purpose.  # noqa: E501

        :return: The state_or_province of this TaxAddress.  # noqa: E501
        :rtype: str
        """
        return self._state_or_province

    @state_or_province.setter
    def state_or_province(self, state_or_province):
        """Sets the state_or_province of this TaxAddress.

        The state name that can be used by sellers for tax purpose.  # noqa: E501

        :param state_or_province: The state_or_province of this TaxAddress.  # noqa: E501
        :type: str
        """

        self._state_or_province = state_or_province

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
        if issubclass(TaxAddress, dict):
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
        if not isinstance(other, TaxAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
