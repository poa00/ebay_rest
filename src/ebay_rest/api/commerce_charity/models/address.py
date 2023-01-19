# coding: utf-8

"""
    Charity API

    The Charity API allows third-party developers to search for and access details on supported charitable organizations.  # noqa: E501

    OpenAPI spec version: v1.2.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Address(object):
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
        'state_or_province': 'str',
        'postal_code': 'str',
        'country': 'str'
    }

    attribute_map = {
        'city': 'city',
        'state_or_province': 'stateOrProvince',
        'postal_code': 'postalCode',
        'country': 'country'
    }

    def __init__(self, city=None, state_or_province=None, postal_code=None, country=None):  # noqa: E501
        """Address - a model defined in Swagger"""  # noqa: E501
        self._city = None
        self._state_or_province = None
        self._postal_code = None
        self._country = None
        self.discriminator = None
        if city is not None:
            self.city = city
        if state_or_province is not None:
            self.state_or_province = state_or_province
        if postal_code is not None:
            self.postal_code = postal_code
        if country is not None:
            self.country = country

    @property
    def city(self):
        """Gets the city of this Address.  # noqa: E501

        The city of the charitable organization.  # noqa: E501

        :return: The city of this Address.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Address.

        The city of the charitable organization.  # noqa: E501

        :param city: The city of this Address.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def state_or_province(self):
        """Gets the state_or_province of this Address.  # noqa: E501

        The state or province of the charitable organization.  # noqa: E501

        :return: The state_or_province of this Address.  # noqa: E501
        :rtype: str
        """
        return self._state_or_province

    @state_or_province.setter
    def state_or_province(self, state_or_province):
        """Sets the state_or_province of this Address.

        The state or province of the charitable organization.  # noqa: E501

        :param state_or_province: The state_or_province of this Address.  # noqa: E501
        :type: str
        """

        self._state_or_province = state_or_province

    @property
    def postal_code(self):
        """Gets the postal_code of this Address.  # noqa: E501

        The postal code of the charitable organization.  # noqa: E501

        :return: The postal_code of this Address.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this Address.

        The postal code of the charitable organization.  # noqa: E501

        :param postal_code: The postal_code of this Address.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def country(self):
        """Gets the country of this Address.  # noqa: E501

        The two-letter <a href=\"https://www.iso.org/iso-3166-country-codes.html \">ISO 3166</a> standard of the country of the address. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/commerce/charity/types/bas:CountryCodeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The country of this Address.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Address.

        The two-letter <a href=\"https://www.iso.org/iso-3166-country-codes.html \">ISO 3166</a> standard of the country of the address. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/commerce/charity/types/bas:CountryCodeEnum'>eBay API documentation</a>  # noqa: E501

        :param country: The country of this Address.  # noqa: E501
        :type: str
        """

        self._country = country

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
        if issubclass(Address, dict):
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
        if not isinstance(other, Address):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
