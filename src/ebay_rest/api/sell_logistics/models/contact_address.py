# coding: utf-8

"""
    Logistics API

    <span class=\"tablenote\"><b>Note:</b> This is a <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited \" target=\"_blank\"> <img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"  alt=\"Limited Release\" />(Limited Release)</a> API available only to select developers approved by business units.</span><br /><br />The <b>Logistics API</b> resources offer the following capabilities: <ul><li><b>shipping_quote</b> &ndash; Consolidates into a list a set of live shipping rates, or quotes, from which you can select a rate to ship a package.</li> <li><b>shipment</b> &ndash; Creates a \"shipment\" for the selected shipping rate.</li></ul> Call <b>createShippingQuote</b> to get a list of live shipping rates. The rates returned are all valid for a specific time window and all quoted prices are at eBay-negotiated rates. <br><br>Select one of the live rates and using its associated <b>rateId</b>, create a \"shipment\" for the package by calling <b>createFromShippingQuote</b>. Creating a shipment completes an agreement, and the cost of the base service and any added shipping options are summed into the returned <b>totalShippingCost</b> value. This action also generates a shipping label that you can use to ship the package.  The total cost of the shipment is incurred when the package is shipped using the supplied shipping label.  <p class=\"tablenote\"><b>Important!</b> Sellers must set up a payment method via their eBay account before they can use the methods in this API to create a shipment and the associated shipping label.</p>  # noqa: E501

    OpenAPI spec version: v1_beta.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ContactAddress(object):
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
        """ContactAddress - a model defined in Swagger"""  # noqa: E501
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
        """Gets the address_line1 of this ContactAddress.  # noqa: E501

        The first line of the street address.  # noqa: E501

        :return: The address_line1 of this ContactAddress.  # noqa: E501
        :rtype: str
        """
        return self._address_line1

    @address_line1.setter
    def address_line1(self, address_line1):
        """Sets the address_line1 of this ContactAddress.

        The first line of the street address.  # noqa: E501

        :param address_line1: The address_line1 of this ContactAddress.  # noqa: E501
        :type: str
        """

        self._address_line1 = address_line1

    @property
    def address_line2(self):
        """Gets the address_line2 of this ContactAddress.  # noqa: E501

        The second line of the street address. Use this field for additional address information, such as a suite or apartment number.  # noqa: E501

        :return: The address_line2 of this ContactAddress.  # noqa: E501
        :rtype: str
        """
        return self._address_line2

    @address_line2.setter
    def address_line2(self, address_line2):
        """Sets the address_line2 of this ContactAddress.

        The second line of the street address. Use this field for additional address information, such as a suite or apartment number.  # noqa: E501

        :param address_line2: The address_line2 of this ContactAddress.  # noqa: E501
        :type: str
        """

        self._address_line2 = address_line2

    @property
    def city(self):
        """Gets the city of this ContactAddress.  # noqa: E501

        The city in which the address is located.  # noqa: E501

        :return: The city of this ContactAddress.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this ContactAddress.

        The city in which the address is located.  # noqa: E501

        :param city: The city of this ContactAddress.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def country_code(self):
        """Gets the country_code of this ContactAddress.  # noqa: E501

        The country of the address, represented as two-letter <a href=\"https://www.iso.org/iso-3166-country-codes.html \" title=\"https://www.iso.org \" target=\"_blank\">ISO 3166</a> country code. For example, <code>US</code> represents the United States and <code>DE</code> represents Germany. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/logistics/types/bas:CountryCodeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The country_code of this ContactAddress.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this ContactAddress.

        The country of the address, represented as two-letter <a href=\"https://www.iso.org/iso-3166-country-codes.html \" title=\"https://www.iso.org \" target=\"_blank\">ISO 3166</a> country code. For example, <code>US</code> represents the United States and <code>DE</code> represents Germany. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/logistics/types/bas:CountryCodeEnum'>eBay API documentation</a>  # noqa: E501

        :param country_code: The country_code of this ContactAddress.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def county(self):
        """Gets the county of this ContactAddress.  # noqa: E501

        The county (not country) in which the address is located. Counties typically contain multiple cities or towns.  # noqa: E501

        :return: The county of this ContactAddress.  # noqa: E501
        :rtype: str
        """
        return self._county

    @county.setter
    def county(self, county):
        """Sets the county of this ContactAddress.

        The county (not country) in which the address is located. Counties typically contain multiple cities or towns.  # noqa: E501

        :param county: The county of this ContactAddress.  # noqa: E501
        :type: str
        """

        self._county = county

    @property
    def postal_code(self):
        """Gets the postal_code of this ContactAddress.  # noqa: E501

        The postal code of the address.  # noqa: E501

        :return: The postal_code of this ContactAddress.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this ContactAddress.

        The postal code of the address.  # noqa: E501

        :param postal_code: The postal_code of this ContactAddress.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def state_or_province(self):
        """Gets the state_or_province of this ContactAddress.  # noqa: E501

        The state or province in which the address is located. States and provinces often contain multiple counties.  # noqa: E501

        :return: The state_or_province of this ContactAddress.  # noqa: E501
        :rtype: str
        """
        return self._state_or_province

    @state_or_province.setter
    def state_or_province(self, state_or_province):
        """Sets the state_or_province of this ContactAddress.

        The state or province in which the address is located. States and provinces often contain multiple counties.  # noqa: E501

        :param state_or_province: The state_or_province of this ContactAddress.  # noqa: E501
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
        if issubclass(ContactAddress, dict):
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
        if not isinstance(other, ContactAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
