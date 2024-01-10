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

class LegacyReference(object):
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
        'legacy_item_id': 'str',
        'legacy_transaction_id': 'str'
    }

    attribute_map = {
        'legacy_item_id': 'legacyItemId',
        'legacy_transaction_id': 'legacyTransactionId'
    }

    def __init__(self, legacy_item_id=None, legacy_transaction_id=None):  # noqa: E501
        """LegacyReference - a model defined in Swagger"""  # noqa: E501
        self._legacy_item_id = None
        self._legacy_transaction_id = None
        self.discriminator = None
        if legacy_item_id is not None:
            self.legacy_item_id = legacy_item_id
        if legacy_transaction_id is not None:
            self.legacy_transaction_id = legacy_transaction_id

    @property
    def legacy_item_id(self):
        """Gets the legacy_item_id of this LegacyReference.  # noqa: E501

        The unique identifier of a listing.<br><br> This value can be found in the <a href=\"/devzone/xml/docs/reference/ebay/getorders.html#Response.OrderArray.Order.TransactionArray.Transaction\" target=\"_blank\">Transaction</a> container in the response of the <a href=\"/devzone/xml/docs/reference/ebay/getorders.html\" target=\"_blank\">getOrder</a> call of the <b>Trading API</b>.<br><br><span class=\"tablenote\"><strong>Note:</strong> Both <b>legacyItemId</b> and <b>legacyTransactionId</b> are needed to identify an order line item. </span>  # noqa: E501

        :return: The legacy_item_id of this LegacyReference.  # noqa: E501
        :rtype: str
        """
        return self._legacy_item_id

    @legacy_item_id.setter
    def legacy_item_id(self, legacy_item_id):
        """Sets the legacy_item_id of this LegacyReference.

        The unique identifier of a listing.<br><br> This value can be found in the <a href=\"/devzone/xml/docs/reference/ebay/getorders.html#Response.OrderArray.Order.TransactionArray.Transaction\" target=\"_blank\">Transaction</a> container in the response of the <a href=\"/devzone/xml/docs/reference/ebay/getorders.html\" target=\"_blank\">getOrder</a> call of the <b>Trading API</b>.<br><br><span class=\"tablenote\"><strong>Note:</strong> Both <b>legacyItemId</b> and <b>legacyTransactionId</b> are needed to identify an order line item. </span>  # noqa: E501

        :param legacy_item_id: The legacy_item_id of this LegacyReference.  # noqa: E501
        :type: str
        """

        self._legacy_item_id = legacy_item_id

    @property
    def legacy_transaction_id(self):
        """Gets the legacy_transaction_id of this LegacyReference.  # noqa: E501

        The unique identifier of a sale/transaction in legacy/Trading API format. A 'transaction ID' is created once a buyer purchases a 'Buy It Now' item or if an auction listing ends with a winning bidder.<br><br> This value can be found in the <a href=\"/devzone/xml/docs/reference/ebay/getorders.html#Response.OrderArray.Order.TransactionArray.Transaction\" target=\"_blank\">Transaction</a> container in the response of the <a href=\"/devzone/xml/docs/reference/ebay/getorders.html\" target=\"_blank\">getOrder</a> call of the <b>Trading API</b>. <br><br><span class=\"tablenote\"><strong>Note:</strong> Both <b>legacyItemId</b> and <b>legacyTransactionId</b> are needed to identify an order line item. </span>  # noqa: E501

        :return: The legacy_transaction_id of this LegacyReference.  # noqa: E501
        :rtype: str
        """
        return self._legacy_transaction_id

    @legacy_transaction_id.setter
    def legacy_transaction_id(self, legacy_transaction_id):
        """Sets the legacy_transaction_id of this LegacyReference.

        The unique identifier of a sale/transaction in legacy/Trading API format. A 'transaction ID' is created once a buyer purchases a 'Buy It Now' item or if an auction listing ends with a winning bidder.<br><br> This value can be found in the <a href=\"/devzone/xml/docs/reference/ebay/getorders.html#Response.OrderArray.Order.TransactionArray.Transaction\" target=\"_blank\">Transaction</a> container in the response of the <a href=\"/devzone/xml/docs/reference/ebay/getorders.html\" target=\"_blank\">getOrder</a> call of the <b>Trading API</b>. <br><br><span class=\"tablenote\"><strong>Note:</strong> Both <b>legacyItemId</b> and <b>legacyTransactionId</b> are needed to identify an order line item. </span>  # noqa: E501

        :param legacy_transaction_id: The legacy_transaction_id of this LegacyReference.  # noqa: E501
        :type: str
        """

        self._legacy_transaction_id = legacy_transaction_id

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
        if issubclass(LegacyReference, dict):
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
        if not isinstance(other, LegacyReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
