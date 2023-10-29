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

class DeliveryCost(object):
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
        'discount_amount': 'Amount',
        'handling_cost': 'Amount',
        'import_charges': 'Amount',
        'shipping_cost': 'Amount',
        'shipping_intermediation_fee': 'Amount'
    }

    attribute_map = {
        'discount_amount': 'discountAmount',
        'handling_cost': 'handlingCost',
        'import_charges': 'importCharges',
        'shipping_cost': 'shippingCost',
        'shipping_intermediation_fee': 'shippingIntermediationFee'
    }

    def __init__(self, discount_amount=None, handling_cost=None, import_charges=None, shipping_cost=None, shipping_intermediation_fee=None):  # noqa: E501
        """DeliveryCost - a model defined in Swagger"""  # noqa: E501
        self._discount_amount = None
        self._handling_cost = None
        self._import_charges = None
        self._shipping_cost = None
        self._shipping_intermediation_fee = None
        self.discriminator = None
        if discount_amount is not None:
            self.discount_amount = discount_amount
        if handling_cost is not None:
            self.handling_cost = handling_cost
        if import_charges is not None:
            self.import_charges = import_charges
        if shipping_cost is not None:
            self.shipping_cost = shipping_cost
        if shipping_intermediation_fee is not None:
            self.shipping_intermediation_fee = shipping_intermediation_fee

    @property
    def discount_amount(self):
        """Gets the discount_amount of this DeliveryCost.  # noqa: E501


        :return: The discount_amount of this DeliveryCost.  # noqa: E501
        :rtype: Amount
        """
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        """Sets the discount_amount of this DeliveryCost.


        :param discount_amount: The discount_amount of this DeliveryCost.  # noqa: E501
        :type: Amount
        """

        self._discount_amount = discount_amount

    @property
    def handling_cost(self):
        """Gets the handling_cost of this DeliveryCost.  # noqa: E501


        :return: The handling_cost of this DeliveryCost.  # noqa: E501
        :rtype: Amount
        """
        return self._handling_cost

    @handling_cost.setter
    def handling_cost(self, handling_cost):
        """Sets the handling_cost of this DeliveryCost.


        :param handling_cost: The handling_cost of this DeliveryCost.  # noqa: E501
        :type: Amount
        """

        self._handling_cost = handling_cost

    @property
    def import_charges(self):
        """Gets the import_charges of this DeliveryCost.  # noqa: E501


        :return: The import_charges of this DeliveryCost.  # noqa: E501
        :rtype: Amount
        """
        return self._import_charges

    @import_charges.setter
    def import_charges(self, import_charges):
        """Sets the import_charges of this DeliveryCost.


        :param import_charges: The import_charges of this DeliveryCost.  # noqa: E501
        :type: Amount
        """

        self._import_charges = import_charges

    @property
    def shipping_cost(self):
        """Gets the shipping_cost of this DeliveryCost.  # noqa: E501


        :return: The shipping_cost of this DeliveryCost.  # noqa: E501
        :rtype: Amount
        """
        return self._shipping_cost

    @shipping_cost.setter
    def shipping_cost(self, shipping_cost):
        """Sets the shipping_cost of this DeliveryCost.


        :param shipping_cost: The shipping_cost of this DeliveryCost.  # noqa: E501
        :type: Amount
        """

        self._shipping_cost = shipping_cost

    @property
    def shipping_intermediation_fee(self):
        """Gets the shipping_intermediation_fee of this DeliveryCost.  # noqa: E501


        :return: The shipping_intermediation_fee of this DeliveryCost.  # noqa: E501
        :rtype: Amount
        """
        return self._shipping_intermediation_fee

    @shipping_intermediation_fee.setter
    def shipping_intermediation_fee(self, shipping_intermediation_fee):
        """Sets the shipping_intermediation_fee of this DeliveryCost.


        :param shipping_intermediation_fee: The shipping_intermediation_fee of this DeliveryCost.  # noqa: E501
        :type: Amount
        """

        self._shipping_intermediation_fee = shipping_intermediation_fee

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
        if issubclass(DeliveryCost, dict):
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
        if not isinstance(other, DeliveryCost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
