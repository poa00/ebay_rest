# coding: utf-8

"""
    eBay Finances API

    This API is used to retrieve seller payouts and monetary transaction details related to those payouts.  # noqa: E501

    OpenAPI spec version: 1.8.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PayoutSummaryResponse(object):
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
        'payout_count': 'int',
        'transaction_count': 'int'
    }

    attribute_map = {
        'amount': 'amount',
        'payout_count': 'payoutCount',
        'transaction_count': 'transactionCount'
    }

    def __init__(self, amount=None, payout_count=None, transaction_count=None):  # noqa: E501
        """PayoutSummaryResponse - a model defined in Swagger"""  # noqa: E501
        self._amount = None
        self._payout_count = None
        self._transaction_count = None
        self.discriminator = None
        if amount is not None:
            self.amount = amount
        if payout_count is not None:
            self.payout_count = payout_count
        if transaction_count is not None:
            self.transaction_count = transaction_count

    @property
    def amount(self):
        """Gets the amount of this PayoutSummaryResponse.  # noqa: E501


        :return: The amount of this PayoutSummaryResponse.  # noqa: E501
        :rtype: Amount
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this PayoutSummaryResponse.


        :param amount: The amount of this PayoutSummaryResponse.  # noqa: E501
        :type: Amount
        """

        self._amount = amount

    @property
    def payout_count(self):
        """Gets the payout_count of this PayoutSummaryResponse.  # noqa: E501

        This integer value indicates the total count of payouts to the seller that match the input criteria. This field is always returned, even if there are no payouts that match the input criteria (its value will show 0).  # noqa: E501

        :return: The payout_count of this PayoutSummaryResponse.  # noqa: E501
        :rtype: int
        """
        return self._payout_count

    @payout_count.setter
    def payout_count(self, payout_count):
        """Sets the payout_count of this PayoutSummaryResponse.

        This integer value indicates the total count of payouts to the seller that match the input criteria. This field is always returned, even if there are no payouts that match the input criteria (its value will show 0).  # noqa: E501

        :param payout_count: The payout_count of this PayoutSummaryResponse.  # noqa: E501
        :type: int
        """

        self._payout_count = payout_count

    @property
    def transaction_count(self):
        """Gets the transaction_count of this PayoutSummaryResponse.  # noqa: E501

        This integer value indicates the total count of monetary transactions (order payments, buyer refunds, and seller credits) associated with the payouts that match the input criteria. This field is always returned, even if there are no payouts that match the input criteria (its value will show 0). If there is at least one payout that matches the input criteria, the value in this field will be at least 1.  # noqa: E501

        :return: The transaction_count of this PayoutSummaryResponse.  # noqa: E501
        :rtype: int
        """
        return self._transaction_count

    @transaction_count.setter
    def transaction_count(self, transaction_count):
        """Sets the transaction_count of this PayoutSummaryResponse.

        This integer value indicates the total count of monetary transactions (order payments, buyer refunds, and seller credits) associated with the payouts that match the input criteria. This field is always returned, even if there are no payouts that match the input criteria (its value will show 0). If there is at least one payout that matches the input criteria, the value in this field will be at least 1.  # noqa: E501

        :param transaction_count: The transaction_count of this PayoutSummaryResponse.  # noqa: E501
        :type: int
        """

        self._transaction_count = transaction_count

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
        if issubclass(PayoutSummaryResponse, dict):
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
        if not isinstance(other, PayoutSummaryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
