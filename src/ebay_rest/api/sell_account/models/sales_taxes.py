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

class SalesTaxes(object):
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
        'sales_taxes': 'list[SalesTax]'
    }

    attribute_map = {
        'sales_taxes': 'salesTaxes'
    }

    def __init__(self, sales_taxes=None):  # noqa: E501
        """SalesTaxes - a model defined in Swagger"""  # noqa: E501
        self._sales_taxes = None
        self.discriminator = None
        if sales_taxes is not None:
            self.sales_taxes = sales_taxes

    @property
    def sales_taxes(self):
        """Gets the sales_taxes of this SalesTaxes.  # noqa: E501

        An array of one or more sales tax rate entries for a specific marketplace (or all applicable marketplaces if the <b>country_code</b> query parameter is not used.<br><br>If no sales tax rate entries are set up, no response payload is returned, but only an HTTP status code of <code>204 No Content</code>.  # noqa: E501

        :return: The sales_taxes of this SalesTaxes.  # noqa: E501
        :rtype: list[SalesTax]
        """
        return self._sales_taxes

    @sales_taxes.setter
    def sales_taxes(self, sales_taxes):
        """Sets the sales_taxes of this SalesTaxes.

        An array of one or more sales tax rate entries for a specific marketplace (or all applicable marketplaces if the <b>country_code</b> query parameter is not used.<br><br>If no sales tax rate entries are set up, no response payload is returned, but only an HTTP status code of <code>204 No Content</code>.  # noqa: E501

        :param sales_taxes: The sales_taxes of this SalesTaxes.  # noqa: E501
        :type: list[SalesTax]
        """

        self._sales_taxes = sales_taxes

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
        if issubclass(SalesTaxes, dict):
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
        if not isinstance(other, SalesTaxes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
