# coding: utf-8

"""
    Account API

    The <b>Account API</b> gives sellers the ability to configure their eBay seller accounts, including the seller's policies (the Fulfillment Policy, Payment Policy, and Return Policy), opt in and out of eBay seller programs, configure sales tax tables, and get account information.  <br><br>For details on the availability of the methods in this API, see <a href=\"/api-docs/sell/account/overview.html#requirements\">Account API requirements and restrictions</a>.  # noqa: E501

    OpenAPI spec version: v1.6.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SalesTaxBase(object):
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
        'sales_tax_percentage': 'str',
        'shipping_and_handling_taxed': 'bool'
    }

    attribute_map = {
        'sales_tax_percentage': 'salesTaxPercentage',
        'shipping_and_handling_taxed': 'shippingAndHandlingTaxed'
    }

    def __init__(self, sales_tax_percentage=None, shipping_and_handling_taxed=None):  # noqa: E501
        """SalesTaxBase - a model defined in Swagger"""  # noqa: E501
        self._sales_tax_percentage = None
        self._shipping_and_handling_taxed = None
        self.discriminator = None
        if sales_tax_percentage is not None:
            self.sales_tax_percentage = sales_tax_percentage
        if shipping_and_handling_taxed is not None:
            self.shipping_and_handling_taxed = shipping_and_handling_taxed

    @property
    def sales_tax_percentage(self):
        """Gets the sales_tax_percentage of this SalesTaxBase.  # noqa: E501

        The sales tax rate, as a percentage of the sale.  # noqa: E501

        :return: The sales_tax_percentage of this SalesTaxBase.  # noqa: E501
        :rtype: str
        """
        return self._sales_tax_percentage

    @sales_tax_percentage.setter
    def sales_tax_percentage(self, sales_tax_percentage):
        """Sets the sales_tax_percentage of this SalesTaxBase.

        The sales tax rate, as a percentage of the sale.  # noqa: E501

        :param sales_tax_percentage: The sales_tax_percentage of this SalesTaxBase.  # noqa: E501
        :type: str
        """

        self._sales_tax_percentage = sales_tax_percentage

    @property
    def shipping_and_handling_taxed(self):
        """Gets the shipping_and_handling_taxed of this SalesTaxBase.  # noqa: E501

        If set to true, shipping and handling charges are taxed.  # noqa: E501

        :return: The shipping_and_handling_taxed of this SalesTaxBase.  # noqa: E501
        :rtype: bool
        """
        return self._shipping_and_handling_taxed

    @shipping_and_handling_taxed.setter
    def shipping_and_handling_taxed(self, shipping_and_handling_taxed):
        """Sets the shipping_and_handling_taxed of this SalesTaxBase.

        If set to true, shipping and handling charges are taxed.  # noqa: E501

        :param shipping_and_handling_taxed: The shipping_and_handling_taxed of this SalesTaxBase.  # noqa: E501
        :type: bool
        """

        self._shipping_and_handling_taxed = shipping_and_handling_taxed

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
        if issubclass(SalesTaxBase, dict):
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
        if not isinstance(other, SalesTaxBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
