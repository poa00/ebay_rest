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

class Deposit(object):
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
        'due_in': 'TimeDuration',
        'payment_methods': 'list[PaymentMethod]'
    }

    attribute_map = {
        'amount': 'amount',
        'due_in': 'dueIn',
        'payment_methods': 'paymentMethods'
    }

    def __init__(self, amount=None, due_in=None, payment_methods=None):  # noqa: E501
        """Deposit - a model defined in Swagger"""  # noqa: E501
        self._amount = None
        self._due_in = None
        self._payment_methods = None
        self.discriminator = None
        if amount is not None:
            self.amount = amount
        if due_in is not None:
            self.due_in = due_in
        if payment_methods is not None:
            self.payment_methods = payment_methods

    @property
    def amount(self):
        """Gets the amount of this Deposit.  # noqa: E501


        :return: The amount of this Deposit.  # noqa: E501
        :rtype: Amount
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Deposit.


        :param amount: The amount of this Deposit.  # noqa: E501
        :type: Amount
        """

        self._amount = amount

    @property
    def due_in(self):
        """Gets the due_in of this Deposit.  # noqa: E501


        :return: The due_in of this Deposit.  # noqa: E501
        :rtype: TimeDuration
        """
        return self._due_in

    @due_in.setter
    def due_in(self, due_in):
        """Sets the due_in of this Deposit.


        :param due_in: The due_in of this Deposit.  # noqa: E501
        :type: TimeDuration
        """

        self._due_in = due_in

    @property
    def payment_methods(self):
        """Gets the payment_methods of this Deposit.  # noqa: E501

        This array is no longer applicable and should not be used since eBay now manages the electronic payment options available to buyers to pay the deposit.  # noqa: E501

        :return: The payment_methods of this Deposit.  # noqa: E501
        :rtype: list[PaymentMethod]
        """
        return self._payment_methods

    @payment_methods.setter
    def payment_methods(self, payment_methods):
        """Sets the payment_methods of this Deposit.

        This array is no longer applicable and should not be used since eBay now manages the electronic payment options available to buyers to pay the deposit.  # noqa: E501

        :param payment_methods: The payment_methods of this Deposit.  # noqa: E501
        :type: list[PaymentMethod]
        """

        self._payment_methods = payment_methods

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
        if issubclass(Deposit, dict):
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
        if not isinstance(other, Deposit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
