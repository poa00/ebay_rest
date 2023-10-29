# coding: utf-8

"""
    Inventory API

    The Inventory API is used to create and manage inventory, and then to publish and manage this inventory on an eBay marketplace. There are also methods in this API that will convert eligible, active eBay listings into the Inventory API model.  # noqa: E501

    OpenAPI spec version: 1.17.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Fee(object):
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
        'fee_type': 'str',
        'promotional_discount': 'Amount'
    }

    attribute_map = {
        'amount': 'amount',
        'fee_type': 'feeType',
        'promotional_discount': 'promotionalDiscount'
    }

    def __init__(self, amount=None, fee_type=None, promotional_discount=None):  # noqa: E501
        """Fee - a model defined in Swagger"""  # noqa: E501
        self._amount = None
        self._fee_type = None
        self._promotional_discount = None
        self.discriminator = None
        if amount is not None:
            self.amount = amount
        if fee_type is not None:
            self.fee_type = fee_type
        if promotional_discount is not None:
            self.promotional_discount = promotional_discount

    @property
    def amount(self):
        """Gets the amount of this Fee.  # noqa: E501


        :return: The amount of this Fee.  # noqa: E501
        :rtype: Amount
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Fee.


        :param amount: The amount of this Fee.  # noqa: E501
        :type: Amount
        """

        self._amount = amount

    @property
    def fee_type(self):
        """Gets the fee_type of this Fee.  # noqa: E501

        The value returned in this field indicates the type of listing fee that the seller may incur if one or more unpublished offers (offers are specified in the call request) are published on the marketplace specified in the <strong>marketplaceId</strong> field. Applicable listing fees will often include things such as <code>InsertionFee</code> or <code>SubtitleFee</code>, but many fee types will get returned even when they are <code>0.0</code>.<br><br>See the <a href=\"https://pages.ebay.com/help/sell/fees.html \" target=\"_blank\">Standard selling fees</a> help page for more information on listing fees.  # noqa: E501

        :return: The fee_type of this Fee.  # noqa: E501
        :rtype: str
        """
        return self._fee_type

    @fee_type.setter
    def fee_type(self, fee_type):
        """Sets the fee_type of this Fee.

        The value returned in this field indicates the type of listing fee that the seller may incur if one or more unpublished offers (offers are specified in the call request) are published on the marketplace specified in the <strong>marketplaceId</strong> field. Applicable listing fees will often include things such as <code>InsertionFee</code> or <code>SubtitleFee</code>, but many fee types will get returned even when they are <code>0.0</code>.<br><br>See the <a href=\"https://pages.ebay.com/help/sell/fees.html \" target=\"_blank\">Standard selling fees</a> help page for more information on listing fees.  # noqa: E501

        :param fee_type: The fee_type of this Fee.  # noqa: E501
        :type: str
        """

        self._fee_type = fee_type

    @property
    def promotional_discount(self):
        """Gets the promotional_discount of this Fee.  # noqa: E501


        :return: The promotional_discount of this Fee.  # noqa: E501
        :rtype: Amount
        """
        return self._promotional_discount

    @promotional_discount.setter
    def promotional_discount(self, promotional_discount):
        """Sets the promotional_discount of this Fee.


        :param promotional_discount: The promotional_discount of this Fee.  # noqa: E501
        :type: Amount
        """

        self._promotional_discount = promotional_discount

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
        if issubclass(Fee, dict):
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
        if not isinstance(other, Fee):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
