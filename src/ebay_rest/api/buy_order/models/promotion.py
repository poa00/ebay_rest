# coding: utf-8

"""
    Order API

    <span class=\"tablenote\"><b>Note:</b> The Order API (v2) currently only supports the guest payment/checkout flow. If you need to support member payment/checkout flow, use the <a href=\"/api-docs/buy/order_v1/resources/methods\">v1_beta version</a> of the Order API.</span><br><br><span class=\"tablenote\"><b>Note:</b> This is a <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited\" target=\"_blank\"><img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\"  alt=\"Limited Release\" title=\"Limited Release\" />(Limited Release)</a> API available only to select developers approved by business units.</span><br><br>The Order API provides interfaces that let shoppers pay for items. It also returns payment and shipping status of the order.  # noqa: E501

    OpenAPI spec version: v2.1.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Promotion(object):
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
        'discount': 'Amount',
        'message': 'str',
        'promotion_type': 'str'
    }

    attribute_map = {
        'discount': 'discount',
        'message': 'message',
        'promotion_type': 'promotionType'
    }

    def __init__(self, discount=None, message=None, promotion_type=None):  # noqa: E501
        """Promotion - a model defined in Swagger"""  # noqa: E501
        self._discount = None
        self._message = None
        self._promotion_type = None
        self.discriminator = None
        if discount is not None:
            self.discount = discount
        if message is not None:
            self.message = message
        if promotion_type is not None:
            self.promotion_type = promotion_type

    @property
    def discount(self):
        """Gets the discount of this Promotion.  # noqa: E501


        :return: The discount of this Promotion.  # noqa: E501
        :rtype: Amount
        """
        return self._discount

    @discount.setter
    def discount(self, discount):
        """Sets the discount of this Promotion.


        :param discount: The discount of this Promotion.  # noqa: E501
        :type: Amount
        """

        self._discount = discount

    @property
    def message(self):
        """Gets the message of this Promotion.  # noqa: E501

        The text for the promotion title, which describes the promotion.  # noqa: E501

        :return: The message of this Promotion.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Promotion.

        The text for the promotion title, which describes the promotion.  # noqa: E501

        :param message: The message of this Promotion.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def promotion_type(self):
        """Gets the promotion_type of this Promotion.  # noqa: E501

        The kind of promotion. Some examples are: <code>SellerDiscountedPromotionalOffer</code> and <code>COUPON</code>.  # noqa: E501

        :return: The promotion_type of this Promotion.  # noqa: E501
        :rtype: str
        """
        return self._promotion_type

    @promotion_type.setter
    def promotion_type(self, promotion_type):
        """Sets the promotion_type of this Promotion.

        The kind of promotion. Some examples are: <code>SellerDiscountedPromotionalOffer</code> and <code>COUPON</code>.  # noqa: E501

        :param promotion_type: The promotion_type of this Promotion.  # noqa: E501
        :type: str
        """

        self._promotion_type = promotion_type

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
        if issubclass(Promotion, dict):
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
        if not isinstance(other, Promotion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
