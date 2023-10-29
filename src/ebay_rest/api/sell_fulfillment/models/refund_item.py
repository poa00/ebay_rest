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

class RefundItem(object):
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
        'refund_amount': 'SimpleAmount',
        'line_item_id': 'str',
        'legacy_reference': 'LegacyReference'
    }

    attribute_map = {
        'refund_amount': 'refundAmount',
        'line_item_id': 'lineItemId',
        'legacy_reference': 'legacyReference'
    }

    def __init__(self, refund_amount=None, line_item_id=None, legacy_reference=None):  # noqa: E501
        """RefundItem - a model defined in Swagger"""  # noqa: E501
        self._refund_amount = None
        self._line_item_id = None
        self._legacy_reference = None
        self.discriminator = None
        if refund_amount is not None:
            self.refund_amount = refund_amount
        if line_item_id is not None:
            self.line_item_id = line_item_id
        if legacy_reference is not None:
            self.legacy_reference = legacy_reference

    @property
    def refund_amount(self):
        """Gets the refund_amount of this RefundItem.  # noqa: E501


        :return: The refund_amount of this RefundItem.  # noqa: E501
        :rtype: SimpleAmount
        """
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, refund_amount):
        """Sets the refund_amount of this RefundItem.


        :param refund_amount: The refund_amount of this RefundItem.  # noqa: E501
        :type: SimpleAmount
        """

        self._refund_amount = refund_amount

    @property
    def line_item_id(self):
        """Gets the line_item_id of this RefundItem.  # noqa: E501

        The unique identifier of an order line item. This identifier is created once a buyer purchases a 'Buy It Now' item or if an auction listing ends with a winning bidder. Either this field or the <b>legacyReference</b> container is needed to identify an individual order line item that will receive a refund.<br><br><span class=\"tablenote\"><strong>Note:</strong> The <b>lineItemId</b> field is used to identify an order line item in REST API format, and the  <b>legacyReference</b> container is used to identify an order line item in Trading/legacy API format. Both legacy and REST API identifiers are returned in <b>getOrder</b> (Fulfillment API) and <b>GetOrders</b> (Trading API).</span>  # noqa: E501

        :return: The line_item_id of this RefundItem.  # noqa: E501
        :rtype: str
        """
        return self._line_item_id

    @line_item_id.setter
    def line_item_id(self, line_item_id):
        """Sets the line_item_id of this RefundItem.

        The unique identifier of an order line item. This identifier is created once a buyer purchases a 'Buy It Now' item or if an auction listing ends with a winning bidder. Either this field or the <b>legacyReference</b> container is needed to identify an individual order line item that will receive a refund.<br><br><span class=\"tablenote\"><strong>Note:</strong> The <b>lineItemId</b> field is used to identify an order line item in REST API format, and the  <b>legacyReference</b> container is used to identify an order line item in Trading/legacy API format. Both legacy and REST API identifiers are returned in <b>getOrder</b> (Fulfillment API) and <b>GetOrders</b> (Trading API).</span>  # noqa: E501

        :param line_item_id: The line_item_id of this RefundItem.  # noqa: E501
        :type: str
        """

        self._line_item_id = line_item_id

    @property
    def legacy_reference(self):
        """Gets the legacy_reference of this RefundItem.  # noqa: E501


        :return: The legacy_reference of this RefundItem.  # noqa: E501
        :rtype: LegacyReference
        """
        return self._legacy_reference

    @legacy_reference.setter
    def legacy_reference(self, legacy_reference):
        """Sets the legacy_reference of this RefundItem.


        :param legacy_reference: The legacy_reference of this RefundItem.  # noqa: E501
        :type: LegacyReference
        """

        self._legacy_reference = legacy_reference

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
        if issubclass(RefundItem, dict):
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
        if not isinstance(other, RefundItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
