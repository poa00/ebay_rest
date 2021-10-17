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

class SellerActionsToRelease(object):
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
        'seller_action_to_release': 'str'
    }

    attribute_map = {
        'seller_action_to_release': 'sellerActionToRelease'
    }

    def __init__(self, seller_action_to_release=None):  # noqa: E501
        """SellerActionsToRelease - a model defined in Swagger"""  # noqa: E501
        self._seller_action_to_release = None
        self.discriminator = None
        if seller_action_to_release is not None:
            self.seller_action_to_release = seller_action_to_release

    @property
    def seller_action_to_release(self):
        """Gets the seller_action_to_release of this SellerActionsToRelease.  # noqa: E501

        A possible action that the seller can take to expedite the release of a payment hold. A <strong>sellerActionToRelease</strong> field is returned for each possible action that a seller may take. Possible actions may include providing shipping/tracking information, issuing a refund, providing refund information, contacting customer support, etc.  # noqa: E501

        :return: The seller_action_to_release of this SellerActionsToRelease.  # noqa: E501
        :rtype: str
        """
        return self._seller_action_to_release

    @seller_action_to_release.setter
    def seller_action_to_release(self, seller_action_to_release):
        """Sets the seller_action_to_release of this SellerActionsToRelease.

        A possible action that the seller can take to expedite the release of a payment hold. A <strong>sellerActionToRelease</strong> field is returned for each possible action that a seller may take. Possible actions may include providing shipping/tracking information, issuing a refund, providing refund information, contacting customer support, etc.  # noqa: E501

        :param seller_action_to_release: The seller_action_to_release of this SellerActionsToRelease.  # noqa: E501
        :type: str
        """

        self._seller_action_to_release = seller_action_to_release

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
        if issubclass(SellerActionsToRelease, dict):
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
        if not isinstance(other, SellerActionsToRelease):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
