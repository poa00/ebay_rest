# coding: utf-8

"""
    Fulfillment API

    Use the Fulfillment API to complete the process of packaging, addressing, handling, and shipping each order on behalf of the seller, in accordance with the payment method and timing specified at checkout.  # noqa: E501

    OpenAPI spec version: v1.19.18
    
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
        'address_line1': 'str',
        'address_line2': 'str',
        'city': 'str',
        'country_code': 'str',
        'county': 'str',
        'postal_code': 'str',
        'state_or_province': 'str'
    }

    attribute_map = {
        'address_line1': 'addressLine1',
        'address_line2': 'addressLine2',
        'city': 'city',
        'country_code': 'countryCode',
        'county': 'county',
        'postal_code': 'postalCode',
        'state_or_province': 'stateOrProvince'
    }

    def __init__(self, address_line1=None, address_line2=None, city=None, country_code=None, county=None, postal_code=None, state_or_province=None):  # noqa: E501
        """Address - a model defined in Swagger"""  # noqa: E501
        self._address_line1 = None
        self._address_line2 = None
        self._city = None
        self._country_code = None
        self._county = None
        self._postal_code = None
        self._state_or_province = None
        self.discriminator = None
        if address_line1 is not None:
            self.address_line1 = address_line1
        if address_line2 is not None:
            self.address_line2 = address_line2
        if city is not None:
            self.city = city
        if country_code is not None:
            self.country_code = country_code
        if county is not None:
            self.county = county
        if postal_code is not None:
            self.postal_code = postal_code
        if state_or_province is not None:
            self.state_or_province = state_or_province

    @property
    def address_line1(self):
        """Gets the address_line1 of this Address.  # noqa: E501

        The first line of the street address.  # noqa: E501

        :return: The address_line1 of this Address.  # noqa: E501
        :rtype: str
        """
        return self._address_line1

    @address_line1.setter
    def address_line1(self, address_line1):
        """Sets the address_line1 of this Address.

        The first line of the street address.  # noqa: E501

        :param address_line1: The address_line1 of this Address.  # noqa: E501
        :type: str
        """

        self._address_line1 = address_line1

    @property
    def address_line2(self):
        """Gets the address_line2 of this Address.  # noqa: E501

        The second line of the street address. This field can be used for additional address information, such as a suite or apartment number. This field will be returned if defined for the shipping address.  # noqa: E501

        :return: The address_line2 of this Address.  # noqa: E501
        :rtype: str
        """
        return self._address_line2

    @address_line2.setter
    def address_line2(self, address_line2):
        """Sets the address_line2 of this Address.

        The second line of the street address. This field can be used for additional address information, such as a suite or apartment number. This field will be returned if defined for the shipping address.  # noqa: E501

        :param address_line2: The address_line2 of this Address.  # noqa: E501
        :type: str
        """

        self._address_line2 = address_line2

    @property
    def city(self):
        """Gets the city of this Address.  # noqa: E501

        The city of the shipping destination.  # noqa: E501

        :return: The city of this Address.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Address.

        The city of the shipping destination.  # noqa: E501

        :param city: The city of this Address.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def country_code(self):
        """Gets the country_code of this Address.  # noqa: E501

        The country of the shipping destination, represented as a two-letter ISO 3166-1 alpha-2 country code. For example, <code>US</code> represents the United States, and <code>DE</code> represents Germany. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/ba:CountryCodeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The country_code of this Address.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this Address.

        The country of the shipping destination, represented as a two-letter ISO 3166-1 alpha-2 country code. For example, <code>US</code> represents the United States, and <code>DE</code> represents Germany. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/ba:CountryCodeEnum'>eBay API documentation</a>  # noqa: E501

        :param country_code: The country_code of this Address.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def county(self):
        """Gets the county of this Address.  # noqa: E501

        The county of the shipping destination. Counties typically, but not always, contain multiple cities or towns. This field is returned if known/available.  # noqa: E501

        :return: The county of this Address.  # noqa: E501
        :rtype: str
        """
        return self._county

    @county.setter
    def county(self, county):
        """Sets the county of this Address.

        The county of the shipping destination. Counties typically, but not always, contain multiple cities or towns. This field is returned if known/available.  # noqa: E501

        :param county: The county of this Address.  # noqa: E501
        :type: str
        """

        self._county = county

    @property
    def postal_code(self):
        """Gets the postal_code of this Address.  # noqa: E501

        The postal code of the shipping destination. Usually referred to as Zip codes in the US. Most countries have postal codes, but not all. The postal code will be returned if applicable.  # noqa: E501

        :return: The postal_code of this Address.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this Address.

        The postal code of the shipping destination. Usually referred to as Zip codes in the US. Most countries have postal codes, but not all. The postal code will be returned if applicable.  # noqa: E501

        :param postal_code: The postal_code of this Address.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def state_or_province(self):
        """Gets the state_or_province of this Address.  # noqa: E501

        The state or province of the shipping destination. Most countries have states or provinces, but not all. The state or province will be returned if applicable.  # noqa: E501

        :return: The state_or_province of this Address.  # noqa: E501
        :rtype: str
        """
        return self._state_or_province

    @state_or_province.setter
    def state_or_province(self, state_or_province):
        """Sets the state_or_province of this Address.

        The state or province of the shipping destination. Most countries have states or provinces, but not all. The state or province will be returned if applicable.  # noqa: E501

        :param state_or_province: The state_or_province of this Address.  # noqa: E501
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
