# coding: utf-8

"""
    eBay Finances API

    This API is used to retrieve seller payouts and monetary transaction details related to those payouts.  # noqa: E501

    OpenAPI spec version: v1.17.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class BalanceAdjustment(object):
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
        'adjustment_amount': 'Amount',
        'adjustment_type': 'str'
    }

    attribute_map = {
        'adjustment_amount': 'adjustmentAmount',
        'adjustment_type': 'adjustmentType'
    }

    def __init__(self, adjustment_amount=None, adjustment_type=None):  # noqa: E501
        """BalanceAdjustment - a model defined in Swagger"""  # noqa: E501
        self._adjustment_amount = None
        self._adjustment_type = None
        self.discriminator = None
        if adjustment_amount is not None:
            self.adjustment_amount = adjustment_amount
        if adjustment_type is not None:
            self.adjustment_type = adjustment_type

    @property
    def adjustment_amount(self):
        """Gets the adjustment_amount of this BalanceAdjustment.  # noqa: E501


        :return: The adjustment_amount of this BalanceAdjustment.  # noqa: E501
        :rtype: Amount
        """
        return self._adjustment_amount

    @adjustment_amount.setter
    def adjustment_amount(self, adjustment_amount):
        """Sets the adjustment_amount of this BalanceAdjustment.


        :param adjustment_amount: The adjustment_amount of this BalanceAdjustment.  # noqa: E501
        :type: Amount
        """

        self._adjustment_amount = adjustment_amount

    @property
    def adjustment_type(self):
        """Gets the adjustment_type of this BalanceAdjustment.  # noqa: E501

        The enumeration value returned here indicates if the charge is a <code>DEBIT</code> or a <code>CREDIT</code> to the seller. Generally, all transfer transaction types are going to be <code>DEBIT</code>, since the money is being tranferred from the seller to eBay. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/finances/types/pay:BookingEntryEnum'>eBay API documentation</a>  # noqa: E501

        :return: The adjustment_type of this BalanceAdjustment.  # noqa: E501
        :rtype: str
        """
        return self._adjustment_type

    @adjustment_type.setter
    def adjustment_type(self, adjustment_type):
        """Sets the adjustment_type of this BalanceAdjustment.

        The enumeration value returned here indicates if the charge is a <code>DEBIT</code> or a <code>CREDIT</code> to the seller. Generally, all transfer transaction types are going to be <code>DEBIT</code>, since the money is being tranferred from the seller to eBay. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/finances/types/pay:BookingEntryEnum'>eBay API documentation</a>  # noqa: E501

        :param adjustment_type: The adjustment_type of this BalanceAdjustment.  # noqa: E501
        :type: str
        """

        self._adjustment_type = adjustment_type

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
        if issubclass(BalanceAdjustment, dict):
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
        if not isinstance(other, BalanceAdjustment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
