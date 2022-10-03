# coding: utf-8

"""
    Fulfillment API

    Use the Fulfillment API to complete the process of packaging, addressing, handling, and shipping each order on behalf of the seller, in accordance with the payment method and timing specified at checkout.  # noqa: E501

    OpenAPI spec version: v1.19.15
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PaymentSummary(object):
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
        'payments': 'list[Payment]',
        'refunds': 'list[OrderRefund]',
        'total_due_seller': 'Amount'
    }

    attribute_map = {
        'payments': 'payments',
        'refunds': 'refunds',
        'total_due_seller': 'totalDueSeller'
    }

    def __init__(self, payments=None, refunds=None, total_due_seller=None):  # noqa: E501
        """PaymentSummary - a model defined in Swagger"""  # noqa: E501
        self._payments = None
        self._refunds = None
        self._total_due_seller = None
        self.discriminator = None
        if payments is not None:
            self.payments = payments
        if refunds is not None:
            self.refunds = refunds
        if total_due_seller is not None:
            self.total_due_seller = total_due_seller

    @property
    def payments(self):
        """Gets the payments of this PaymentSummary.  # noqa: E501

        This array consists of payment information for the order, including payment status, payment method, payment amount, and payment date. This array is always returned, although some of the fields under this container will not be returned until payment has been made.  # noqa: E501

        :return: The payments of this PaymentSummary.  # noqa: E501
        :rtype: list[Payment]
        """
        return self._payments

    @payments.setter
    def payments(self, payments):
        """Sets the payments of this PaymentSummary.

        This array consists of payment information for the order, including payment status, payment method, payment amount, and payment date. This array is always returned, although some of the fields under this container will not be returned until payment has been made.  # noqa: E501

        :param payments: The payments of this PaymentSummary.  # noqa: E501
        :type: list[Payment]
        """

        self._payments = payments

    @property
    def refunds(self):
        """Gets the refunds of this PaymentSummary.  # noqa: E501

        This array is always returned, but is returned as an empty array unless the seller has submitted a partial or full refund to the buyer for the order. If a refund has occurred, the refund amount and refund date will be shown for each refund.  # noqa: E501

        :return: The refunds of this PaymentSummary.  # noqa: E501
        :rtype: list[OrderRefund]
        """
        return self._refunds

    @refunds.setter
    def refunds(self, refunds):
        """Sets the refunds of this PaymentSummary.

        This array is always returned, but is returned as an empty array unless the seller has submitted a partial or full refund to the buyer for the order. If a refund has occurred, the refund amount and refund date will be shown for each refund.  # noqa: E501

        :param refunds: The refunds of this PaymentSummary.  # noqa: E501
        :type: list[OrderRefund]
        """

        self._refunds = refunds

    @property
    def total_due_seller(self):
        """Gets the total_due_seller of this PaymentSummary.  # noqa: E501


        :return: The total_due_seller of this PaymentSummary.  # noqa: E501
        :rtype: Amount
        """
        return self._total_due_seller

    @total_due_seller.setter
    def total_due_seller(self, total_due_seller):
        """Sets the total_due_seller of this PaymentSummary.


        :param total_due_seller: The total_due_seller of this PaymentSummary.  # noqa: E501
        :type: Amount
        """

        self._total_due_seller = total_due_seller

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
        if issubclass(PaymentSummary, dict):
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
        if not isinstance(other, PaymentSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
