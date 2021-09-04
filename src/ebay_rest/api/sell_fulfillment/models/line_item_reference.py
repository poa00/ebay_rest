# coding: utf-8

"""
    Fulfillment API

    Use the Fulfillment API to complete the process of packaging, addressing, handling, and shipping each order on behalf of the seller, in accordance with the payment method and timing specified at checkout.  # noqa: E501

    OpenAPI spec version: v1.19.9
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class LineItemReference(object):
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
        'line_item_id': 'str',
        'quantity': 'int'
    }

    attribute_map = {
        'line_item_id': 'lineItemId',
        'quantity': 'quantity'
    }

    def __init__(self, line_item_id=None, quantity=None):  # noqa: E501
        """LineItemReference - a model defined in Swagger"""  # noqa: E501
        self._line_item_id = None
        self._quantity = None
        self.discriminator = None
        if line_item_id is not None:
            self.line_item_id = line_item_id
        if quantity is not None:
            self.quantity = quantity

    @property
    def line_item_id(self):
        """Gets the line_item_id of this LineItemReference.  # noqa: E501

        This is the unique identifier of the eBay order line item that is part of the shipping fulfillment. The line item ID is created as soon as there is a commitment to buy from the seller.  # noqa: E501

        :return: The line_item_id of this LineItemReference.  # noqa: E501
        :rtype: str
        """
        return self._line_item_id

    @line_item_id.setter
    def line_item_id(self, line_item_id):
        """Sets the line_item_id of this LineItemReference.

        This is the unique identifier of the eBay order line item that is part of the shipping fulfillment. The line item ID is created as soon as there is a commitment to buy from the seller.  # noqa: E501

        :param line_item_id: The line_item_id of this LineItemReference.  # noqa: E501
        :type: str
        """

        self._line_item_id = line_item_id

    @property
    def quantity(self):
        """Gets the quantity of this LineItemReference.  # noqa: E501

        This field is reserved for internal or future use.  # noqa: E501

        :return: The quantity of this LineItemReference.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this LineItemReference.

        This field is reserved for internal or future use.  # noqa: E501

        :param quantity: The quantity of this LineItemReference.  # noqa: E501
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
        if issubclass(LineItemReference, dict):
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
        if not isinstance(other, LineItemReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
