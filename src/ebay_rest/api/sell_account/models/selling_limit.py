# coding: utf-8

"""
    Account API

    The <b>Account API</b> gives sellers the ability to configure their eBay seller accounts, including the seller's policies (eBay business policies and seller-defined custom policies), opt in and out of eBay seller programs, configure sales tax tables, and get account information.  <br><br>For details on the availability of the methods in this API, see <a href=\"/api-docs/sell/account/overview.html#requirements\">Account API requirements and restrictions</a>.  # noqa: E501

    OpenAPI spec version: v1.9.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SellingLimit(object):
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
        'amount': 'Amount',
        'quantity': 'int'
    }

    attribute_map = {
        'amount': 'amount',
        'quantity': 'quantity'
    }

    def __init__(self, amount=None, quantity=None):  # noqa: E501
        """SellingLimit - a model defined in Swagger"""  # noqa: E501
        self._amount = None
        self._quantity = None
        self.discriminator = None
        if amount is not None:
            self.amount = amount
        if quantity is not None:
            self.quantity = quantity

    @property
    def amount(self):
        """Gets the amount of this SellingLimit.  # noqa: E501


        :return: The amount of this SellingLimit.  # noqa: E501
        :rtype: Amount
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this SellingLimit.


        :param amount: The amount of this SellingLimit.  # noqa: E501
        :type: Amount
        """

        self._amount = amount

    @property
    def quantity(self):
        """Gets the quantity of this SellingLimit.  # noqa: E501

        This field shows the monthly cap for total quantity sold allowed for the seller's account. This container may not be returned if a seller does not have a monthly cap for total quantity sold.  # noqa: E501

        :return: The quantity of this SellingLimit.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this SellingLimit.

        This field shows the monthly cap for total quantity sold allowed for the seller's account. This container may not be returned if a seller does not have a monthly cap for total quantity sold.  # noqa: E501

        :param quantity: The quantity of this SellingLimit.  # noqa: E501
        :type: int
        """

        self._quantity = quantity

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
        if issubclass(SellingLimit, dict):
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
        if not isinstance(other, SellingLimit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
