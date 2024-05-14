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

class EconomicOperator(object):
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
        'company_name': 'str',
        'address_line1': 'str',
        'address_line2': 'str',
        'city': 'str',
        'state_or_province': 'str',
        'postal_code': 'str',
        'country': 'str',
        'phone': 'str',
        'email': 'str'
    }

    attribute_map = {
        'company_name': 'companyName',
        'address_line1': 'addressLine1',
        'address_line2': 'addressLine2',
        'city': 'city',
        'state_or_province': 'stateOrProvince',
        'postal_code': 'postalCode',
        'country': 'country',
        'phone': 'phone',
        'email': 'email'
    }

    def __init__(self, company_name=None, address_line1=None, address_line2=None, city=None, state_or_province=None, postal_code=None, country=None, phone=None, email=None):  # noqa: E501
        """EconomicOperator - a model defined in Swagger"""  # noqa: E501
        self._company_name = None
        self._address_line1 = None
        self._address_line2 = None
        self._city = None
        self._state_or_province = None
        self._postal_code = None
        self._country = None
        self._phone = None
        self._email = None
        self.discriminator = None
        if company_name is not None:
            self.company_name = company_name
        if address_line1 is not None:
            self.address_line1 = address_line1
        if address_line2 is not None:
            self.address_line2 = address_line2
        if city is not None:
            self.city = city
        if state_or_province is not None:
            self.state_or_province = state_or_province
        if postal_code is not None:
            self.postal_code = postal_code
        if country is not None:
            self.country = country
        if phone is not None:
            self.phone = phone
        if email is not None:
            self.email = email

    @property
    def company_name(self):
        """Gets the company_name of this EconomicOperator.  # noqa: E501

        The company name of the registered Economic Operator.  # noqa: E501

        :return: The company_name of this EconomicOperator.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this EconomicOperator.

        The company name of the registered Economic Operator.  # noqa: E501

        :param company_name: The company_name of this EconomicOperator.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    @property
    def address_line1(self):
        """Gets the address_line1 of this EconomicOperator.  # noqa: E501

        The first line of the registered Economic Operator's street address.  # noqa: E501

        :return: The address_line1 of this EconomicOperator.  # noqa: E501
        :rtype: str
        """
        return self._address_line1

    @address_line1.setter
    def address_line1(self, address_line1):
        """Sets the address_line1 of this EconomicOperator.

        The first line of the registered Economic Operator's street address.  # noqa: E501

        :param address_line1: The address_line1 of this EconomicOperator.  # noqa: E501
        :type: str
        """

        self._address_line1 = address_line1

    @property
    def address_line2(self):
        """Gets the address_line2 of this EconomicOperator.  # noqa: E501

        The second line, if any, of the registered Economic Operator's street address. This field is not always used, but can be used for 'Suite Number' or 'Apt Number'.  # noqa: E501

        :return: The address_line2 of this EconomicOperator.  # noqa: E501
        :rtype: str
        """
        return self._address_line2

    @address_line2.setter
    def address_line2(self, address_line2):
        """Sets the address_line2 of this EconomicOperator.

        The second line, if any, of the registered Economic Operator's street address. This field is not always used, but can be used for 'Suite Number' or 'Apt Number'.  # noqa: E501

        :param address_line2: The address_line2 of this EconomicOperator.  # noqa: E501
        :type: str
        """

        self._address_line2 = address_line2

    @property
    def city(self):
        """Gets the city of this EconomicOperator.  # noqa: E501

        The city of the registered Economic Operator's street address.  # noqa: E501

        :return: The city of this EconomicOperator.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this EconomicOperator.

        The city of the registered Economic Operator's street address.  # noqa: E501

        :param city: The city of this EconomicOperator.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def state_or_province(self):
        """Gets the state_or_province of this EconomicOperator.  # noqa: E501

        The state or province of the registered Economic Operator's street address.  # noqa: E501

        :return: The state_or_province of this EconomicOperator.  # noqa: E501
        :rtype: str
        """
        return self._state_or_province

    @state_or_province.setter
    def state_or_province(self, state_or_province):
        """Sets the state_or_province of this EconomicOperator.

        The state or province of the registered Economic Operator's street address.  # noqa: E501

        :param state_or_province: The state_or_province of this EconomicOperator.  # noqa: E501
        :type: str
        """

        self._state_or_province = state_or_province

    @property
    def postal_code(self):
        """Gets the postal_code of this EconomicOperator.  # noqa: E501

        The postal code of the registered Economic Operator's street address.  # noqa: E501

        :return: The postal_code of this EconomicOperator.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this EconomicOperator.

        The postal code of the registered Economic Operator's street address.  # noqa: E501

        :param postal_code: The postal_code of this EconomicOperator.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def country(self):
        """Gets the country of this EconomicOperator.  # noqa: E501

        The two-letter <a href=\"https://www.iso.org/iso-3166-country-codes.html \" target=\"_blank\">ISO 3166</a> standard abbreviation of the country of the registered Economic Operator's address.  # noqa: E501

        :return: The country of this EconomicOperator.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this EconomicOperator.

        The two-letter <a href=\"https://www.iso.org/iso-3166-country-codes.html \" target=\"_blank\">ISO 3166</a> standard abbreviation of the country of the registered Economic Operator's address.  # noqa: E501

        :param country: The country of this EconomicOperator.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def phone(self):
        """Gets the phone of this EconomicOperator.  # noqa: E501

        The registered Economic Operator's business phone number.  # noqa: E501

        :return: The phone of this EconomicOperator.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this EconomicOperator.

        The registered Economic Operator's business phone number.  # noqa: E501

        :param phone: The phone of this EconomicOperator.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def email(self):
        """Gets the email of this EconomicOperator.  # noqa: E501

        The registered Economic Operator's business email address.  # noqa: E501

        :return: The email of this EconomicOperator.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this EconomicOperator.

        The registered Economic Operator's business email address.  # noqa: E501

        :param email: The email of this EconomicOperator.  # noqa: E501
        :type: str
        """

        self._email = email

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
        if issubclass(EconomicOperator, dict):
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
        if not isinstance(other, EconomicOperator):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
