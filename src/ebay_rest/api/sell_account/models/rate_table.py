# coding: utf-8

"""
    Account API

    The <b>Account API</b> gives sellers the ability to configure their eBay seller accounts, including the seller's policies (eBay business policies and seller-defined custom policies), opt in and out of eBay seller programs, configure sales tax tables, and get account information.  <br><br>For details on the availability of the methods in this API, see <a href=\"/api-docs/sell/account/overview.html#requirements\">Account API requirements and restrictions</a>.  # noqa: E501

    OpenAPI spec version: v1.9.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class RateTable(object):
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
        'locality': 'str',
        'name': 'str',
        'rate_table_id': 'str'
    }

    attribute_map = {
        'country_code': 'countryCode',
        'locality': 'locality',
        'name': 'name',
        'rate_table_id': 'rateTableId'
    }

    def __init__(self, country_code=None, locality=None, name=None, rate_table_id=None):  # noqa: E501
        """RateTable - a model defined in Swagger"""  # noqa: E501
        self._country_code = None
        self._locality = None
        self._name = None
        self._rate_table_id = None
        self.discriminator = None
        if country_code is not None:
            self.country_code = country_code
        if locality is not None:
            self.locality = locality
        if name is not None:
            self.name = name
        if rate_table_id is not None:
            self.rate_table_id = rate_table_id

    @property
    def country_code(self):
        """Gets the country_code of this RateTable.  # noqa: E501

        A two-letter <a href=\"https://www.iso.org/iso-3166-country-codes.html \" title=\"https://www.iso.org \" target=\"_blank\">ISO 3166</a> country code representing the eBay marketplace where the shipping rate table is defined. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/ba:CountryCodeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The country_code of this RateTable.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this RateTable.

        A two-letter <a href=\"https://www.iso.org/iso-3166-country-codes.html \" title=\"https://www.iso.org \" target=\"_blank\">ISO 3166</a> country code representing the eBay marketplace where the shipping rate table is defined. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/ba:CountryCodeEnum'>eBay API documentation</a>  # noqa: E501

        :param country_code: The country_code of this RateTable.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def locality(self):
        """Gets the locality of this RateTable.  # noqa: E501

        This enumeration value returned here indicates whether the shipping rate table is a domestic or international shipping rate table. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/api:ShippingOptionTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The locality of this RateTable.  # noqa: E501
        :rtype: str
        """
        return self._locality

    @locality.setter
    def locality(self, locality):
        """Sets the locality of this RateTable.

        This enumeration value returned here indicates whether the shipping rate table is a domestic or international shipping rate table. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/api:ShippingOptionTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param locality: The locality of this RateTable.  # noqa: E501
        :type: str
        """

        self._locality = locality

    @property
    def name(self):
        """Gets the name of this RateTable.  # noqa: E501

        The seller-defined name for the shipping rate table.  # noqa: E501

        :return: The name of this RateTable.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RateTable.

        The seller-defined name for the shipping rate table.  # noqa: E501

        :param name: The name of this RateTable.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def rate_table_id(self):
        """Gets the rate_table_id of this RateTable.  # noqa: E501

        A unique eBay-assigned ID for a seller's shipping rate table. These <b>rateTableId</b> values are used to associate shipping rate tables to fulfillment business policies or directly to listings through an add/revise/relist call in the Trading API.  # noqa: E501

        :return: The rate_table_id of this RateTable.  # noqa: E501
        :rtype: str
        """
        return self._rate_table_id

    @rate_table_id.setter
    def rate_table_id(self, rate_table_id):
        """Sets the rate_table_id of this RateTable.

        A unique eBay-assigned ID for a seller's shipping rate table. These <b>rateTableId</b> values are used to associate shipping rate tables to fulfillment business policies or directly to listings through an add/revise/relist call in the Trading API.  # noqa: E501

        :param rate_table_id: The rate_table_id of this RateTable.  # noqa: E501
        :type: str
        """

        self._rate_table_id = rate_table_id

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
        if issubclass(RateTable, dict):
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
        if not isinstance(other, RateTable):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
