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

class OrderLineItems(object):
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
        'item_id': 'str',
        'line_item_id': 'str'
    }

    attribute_map = {
        'item_id': 'itemId',
        'line_item_id': 'lineItemId'
    }

    def __init__(self, item_id=None, line_item_id=None):  # noqa: E501
        """OrderLineItems - a model defined in Swagger"""  # noqa: E501
        self._item_id = None
        self._line_item_id = None
        self.discriminator = None
        if item_id is not None:
            self.item_id = item_id
        if line_item_id is not None:
            self.line_item_id = line_item_id

    @property
    def item_id(self):
        """Gets the item_id of this OrderLineItems.  # noqa: E501

        The unique identifier of the eBay listing associated with the order.  # noqa: E501

        :return: The item_id of this OrderLineItems.  # noqa: E501
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """Sets the item_id of this OrderLineItems.

        The unique identifier of the eBay listing associated with the order.  # noqa: E501

        :param item_id: The item_id of this OrderLineItems.  # noqa: E501
        :type: str
        """

        self._item_id = item_id

    @property
    def line_item_id(self):
        """Gets the line_item_id of this OrderLineItems.  # noqa: E501

        The unique identifier of the line item within the order. The <strong>lineItemId</strong> value is created once the buyer actually purchases the item, or if there is a commitment to buy (such as an auction that is won by the buyer, an accepted Best Offer, or other situation that does not require immediate payment from the buyer).  # noqa: E501

        :return: The line_item_id of this OrderLineItems.  # noqa: E501
        :rtype: str
        """
        return self._line_item_id

    @line_item_id.setter
    def line_item_id(self, line_item_id):
        """Sets the line_item_id of this OrderLineItems.

        The unique identifier of the line item within the order. The <strong>lineItemId</strong> value is created once the buyer actually purchases the item, or if there is a commitment to buy (such as an auction that is won by the buyer, an accepted Best Offer, or other situation that does not require immediate payment from the buyer).  # noqa: E501

        :param line_item_id: The line_item_id of this OrderLineItems.  # noqa: E501
        :type: str
        """

        self._line_item_id = line_item_id

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
        if issubclass(OrderLineItems, dict):
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
        if not isinstance(other, OrderLineItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
