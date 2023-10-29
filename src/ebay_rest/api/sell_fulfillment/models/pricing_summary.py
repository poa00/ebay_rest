# coding: utf-8

"""
    Fulfillment API

    Use the Fulfillment API to complete the process of packaging, addressing, handling, and shipping each order on behalf of the seller, in accordance with the payment method and timing specified at checkout.  # noqa: E501

    OpenAPI spec version: v1.20.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PricingSummary(object):
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
        'adjustment': 'Amount',
        'delivery_cost': 'Amount',
        'delivery_discount': 'Amount',
        'fee': 'Amount',
        'price_discount': 'Amount',
        'price_subtotal': 'Amount',
        'tax': 'Amount',
        'total': 'Amount'
    }

    attribute_map = {
        'adjustment': 'adjustment',
        'delivery_cost': 'deliveryCost',
        'delivery_discount': 'deliveryDiscount',
        'fee': 'fee',
        'price_discount': 'priceDiscount',
        'price_subtotal': 'priceSubtotal',
        'tax': 'tax',
        'total': 'total'
    }

    def __init__(self, adjustment=None, delivery_cost=None, delivery_discount=None, fee=None, price_discount=None, price_subtotal=None, tax=None, total=None):  # noqa: E501
        """PricingSummary - a model defined in Swagger"""  # noqa: E501
        self._adjustment = None
        self._delivery_cost = None
        self._delivery_discount = None
        self._fee = None
        self._price_discount = None
        self._price_subtotal = None
        self._tax = None
        self._total = None
        self.discriminator = None
        if adjustment is not None:
            self.adjustment = adjustment
        if delivery_cost is not None:
            self.delivery_cost = delivery_cost
        if delivery_discount is not None:
            self.delivery_discount = delivery_discount
        if fee is not None:
            self.fee = fee
        if price_discount is not None:
            self.price_discount = price_discount
        if price_subtotal is not None:
            self.price_subtotal = price_subtotal
        if tax is not None:
            self.tax = tax
        if total is not None:
            self.total = total

    @property
    def adjustment(self):
        """Gets the adjustment of this PricingSummary.  # noqa: E501


        :return: The adjustment of this PricingSummary.  # noqa: E501
        :rtype: Amount
        """
        return self._adjustment

    @adjustment.setter
    def adjustment(self, adjustment):
        """Sets the adjustment of this PricingSummary.


        :param adjustment: The adjustment of this PricingSummary.  # noqa: E501
        :type: Amount
        """

        self._adjustment = adjustment

    @property
    def delivery_cost(self):
        """Gets the delivery_cost of this PricingSummary.  # noqa: E501


        :return: The delivery_cost of this PricingSummary.  # noqa: E501
        :rtype: Amount
        """
        return self._delivery_cost

    @delivery_cost.setter
    def delivery_cost(self, delivery_cost):
        """Sets the delivery_cost of this PricingSummary.


        :param delivery_cost: The delivery_cost of this PricingSummary.  # noqa: E501
        :type: Amount
        """

        self._delivery_cost = delivery_cost

    @property
    def delivery_discount(self):
        """Gets the delivery_discount of this PricingSummary.  # noqa: E501


        :return: The delivery_discount of this PricingSummary.  # noqa: E501
        :rtype: Amount
        """
        return self._delivery_discount

    @delivery_discount.setter
    def delivery_discount(self, delivery_discount):
        """Sets the delivery_discount of this PricingSummary.


        :param delivery_discount: The delivery_discount of this PricingSummary.  # noqa: E501
        :type: Amount
        """

        self._delivery_discount = delivery_discount

    @property
    def fee(self):
        """Gets the fee of this PricingSummary.  # noqa: E501


        :return: The fee of this PricingSummary.  # noqa: E501
        :rtype: Amount
        """
        return self._fee

    @fee.setter
    def fee(self, fee):
        """Sets the fee of this PricingSummary.


        :param fee: The fee of this PricingSummary.  # noqa: E501
        :type: Amount
        """

        self._fee = fee

    @property
    def price_discount(self):
        """Gets the price_discount of this PricingSummary.  # noqa: E501


        :return: The price_discount of this PricingSummary.  # noqa: E501
        :rtype: Amount
        """
        return self._price_discount

    @price_discount.setter
    def price_discount(self, price_discount):
        """Sets the price_discount of this PricingSummary.


        :param price_discount: The price_discount of this PricingSummary.  # noqa: E501
        :type: Amount
        """

        self._price_discount = price_discount

    @property
    def price_subtotal(self):
        """Gets the price_subtotal of this PricingSummary.  # noqa: E501


        :return: The price_subtotal of this PricingSummary.  # noqa: E501
        :rtype: Amount
        """
        return self._price_subtotal

    @price_subtotal.setter
    def price_subtotal(self, price_subtotal):
        """Sets the price_subtotal of this PricingSummary.


        :param price_subtotal: The price_subtotal of this PricingSummary.  # noqa: E501
        :type: Amount
        """

        self._price_subtotal = price_subtotal

    @property
    def tax(self):
        """Gets the tax of this PricingSummary.  # noqa: E501


        :return: The tax of this PricingSummary.  # noqa: E501
        :rtype: Amount
        """
        return self._tax

    @tax.setter
    def tax(self, tax):
        """Sets the tax of this PricingSummary.


        :param tax: The tax of this PricingSummary.  # noqa: E501
        :type: Amount
        """

        self._tax = tax

    @property
    def total(self):
        """Gets the total of this PricingSummary.  # noqa: E501


        :return: The total of this PricingSummary.  # noqa: E501
        :rtype: Amount
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this PricingSummary.


        :param total: The total of this PricingSummary.  # noqa: E501
        :type: Amount
        """

        self._total = total

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
        if issubclass(PricingSummary, dict):
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
        if not isinstance(other, PricingSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
