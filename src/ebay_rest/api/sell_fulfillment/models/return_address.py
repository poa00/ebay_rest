# coding: utf-8

"""
    Fulfillment API

    Use the Fulfillment API to complete the process of packaging, addressing, handling, and shipping each order on behalf of the seller, in accordance with the payment method and timing specified at checkout.  # noqa: E501

    OpenAPI spec version: v1.20.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ReturnAddress(object):
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
        'country': 'str',
        'county': 'str',
        'full_name': 'str',
        'postal_code': 'str',
        'primary_phone': 'Phone',
        'state_or_province': 'str'
    }

    attribute_map = {
        'address_line1': 'addressLine1',
        'address_line2': 'addressLine2',
        'city': 'city',
        'country': 'country',
        'county': 'county',
        'full_name': 'fullName',
        'postal_code': 'postalCode',
        'primary_phone': 'primaryPhone',
        'state_or_province': 'stateOrProvince'
    }

    def __init__(self, address_line1=None, address_line2=None, city=None, country=None, county=None, full_name=None, postal_code=None, primary_phone=None, state_or_province=None):  # noqa: E501
        """ReturnAddress - a model defined in Swagger"""  # noqa: E501
        self._address_line1 = None
        self._address_line2 = None
        self._city = None
        self._country = None
        self._county = None
        self._full_name = None
        self._postal_code = None
        self._primary_phone = None
        self._state_or_province = None
        self.discriminator = None
        if address_line1 is not None:
            self.address_line1 = address_line1
        if address_line2 is not None:
            self.address_line2 = address_line2
        if city is not None:
            self.city = city
        if country is not None:
            self.country = country
        if county is not None:
            self.county = county
        if full_name is not None:
            self.full_name = full_name
        if postal_code is not None:
            self.postal_code = postal_code
        if primary_phone is not None:
            self.primary_phone = primary_phone
        if state_or_province is not None:
            self.state_or_province = state_or_province

    @property
    def address_line1(self):
        """Gets the address_line1 of this ReturnAddress.  # noqa: E501

        The first line of the street address.  # noqa: E501

        :return: The address_line1 of this ReturnAddress.  # noqa: E501
        :rtype: str
        """
        return self._address_line1

    @address_line1.setter
    def address_line1(self, address_line1):
        """Sets the address_line1 of this ReturnAddress.

        The first line of the street address.  # noqa: E501

        :param address_line1: The address_line1 of this ReturnAddress.  # noqa: E501
        :type: str
        """

        self._address_line1 = address_line1

    @property
    def address_line2(self):
        """Gets the address_line2 of this ReturnAddress.  # noqa: E501

        The second line of the street address. This line is not always necessarily, but is often used for apartment number or suite number, or other relevant information that can not fit on the first line.  # noqa: E501

        :return: The address_line2 of this ReturnAddress.  # noqa: E501
        :rtype: str
        """
        return self._address_line2

    @address_line2.setter
    def address_line2(self, address_line2):
        """Sets the address_line2 of this ReturnAddress.

        The second line of the street address. This line is not always necessarily, but is often used for apartment number or suite number, or other relevant information that can not fit on the first line.  # noqa: E501

        :param address_line2: The address_line2 of this ReturnAddress.  # noqa: E501
        :type: str
        """

        self._address_line2 = address_line2

    @property
    def city(self):
        """Gets the city of this ReturnAddress.  # noqa: E501

        The city of the return address.  # noqa: E501

        :return: The city of this ReturnAddress.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this ReturnAddress.

        The city of the return address.  # noqa: E501

        :param city: The city of this ReturnAddress.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def country(self):
        """Gets the country of this ReturnAddress.  # noqa: E501

        The country's two-digit, ISO 3166-1 country code. See the enumeration type for a country's value. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/ba:CountryCodeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The country of this ReturnAddress.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this ReturnAddress.

        The country's two-digit, ISO 3166-1 country code. See the enumeration type for a country's value. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/ba:CountryCodeEnum'>eBay API documentation</a>  # noqa: E501

        :param country: The country of this ReturnAddress.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def county(self):
        """Gets the county of this ReturnAddress.  # noqa: E501

        The county of the return address. Counties are not applicable to all countries.  # noqa: E501

        :return: The county of this ReturnAddress.  # noqa: E501
        :rtype: str
        """
        return self._county

    @county.setter
    def county(self, county):
        """Sets the county of this ReturnAddress.

        The county of the return address. Counties are not applicable to all countries.  # noqa: E501

        :param county: The county of this ReturnAddress.  # noqa: E501
        :type: str
        """

        self._county = county

    @property
    def full_name(self):
        """Gets the full_name of this ReturnAddress.  # noqa: E501

        The full name of return address owner.  # noqa: E501

        :return: The full_name of this ReturnAddress.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this ReturnAddress.

        The full name of return address owner.  # noqa: E501

        :param full_name: The full_name of this ReturnAddress.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def postal_code(self):
        """Gets the postal_code of this ReturnAddress.  # noqa: E501

        The postal code of the return address.  # noqa: E501

        :return: The postal_code of this ReturnAddress.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this ReturnAddress.

        The postal code of the return address.  # noqa: E501

        :param postal_code: The postal_code of this ReturnAddress.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def primary_phone(self):
        """Gets the primary_phone of this ReturnAddress.  # noqa: E501


        :return: The primary_phone of this ReturnAddress.  # noqa: E501
        :rtype: Phone
        """
        return self._primary_phone

    @primary_phone.setter
    def primary_phone(self, primary_phone):
        """Sets the primary_phone of this ReturnAddress.


        :param primary_phone: The primary_phone of this ReturnAddress.  # noqa: E501
        :type: Phone
        """

        self._primary_phone = primary_phone

    @property
    def state_or_province(self):
        """Gets the state_or_province of this ReturnAddress.  # noqa: E501

        The state or province of the return address.  # noqa: E501

        :return: The state_or_province of this ReturnAddress.  # noqa: E501
        :rtype: str
        """
        return self._state_or_province

    @state_or_province.setter
    def state_or_province(self, state_or_province):
        """Sets the state_or_province of this ReturnAddress.

        The state or province of the return address.  # noqa: E501

        :param state_or_province: The state_or_province of this ReturnAddress.  # noqa: E501
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
        if issubclass(ReturnAddress, dict):
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
        if not isinstance(other, ReturnAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
