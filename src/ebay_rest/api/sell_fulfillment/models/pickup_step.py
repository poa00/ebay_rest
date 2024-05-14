# coding: utf-8

"""
    Fulfillment API

    Use the Fulfillment API to complete the process of packaging, addressing, handling, and shipping each order on behalf of the seller, in accordance with the payment method and timing specified at checkout.  # noqa: E501

    OpenAPI spec version: v1.20.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PickupStep(object):
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
        'merchant_location_key': 'str'
    }

    attribute_map = {
        'merchant_location_key': 'merchantLocationKey'
    }

    def __init__(self, merchant_location_key=None):  # noqa: E501
        """PickupStep - a model defined in Swagger"""  # noqa: E501
        self._merchant_location_key = None
        self.discriminator = None
        if merchant_location_key is not None:
            self.merchant_location_key = merchant_location_key

    @property
    def merchant_location_key(self):
        """Gets the merchant_location_key of this PickupStep.  # noqa: E501

        A merchant-defined unique identifier of the merchant's store where the buyer will pick up their In-Store Pickup order.<br><br> This field is always returned with the <b>pickupStep</b> container.  # noqa: E501

        :return: The merchant_location_key of this PickupStep.  # noqa: E501
        :rtype: str
        """
        return self._merchant_location_key

    @merchant_location_key.setter
    def merchant_location_key(self, merchant_location_key):
        """Sets the merchant_location_key of this PickupStep.

        A merchant-defined unique identifier of the merchant's store where the buyer will pick up their In-Store Pickup order.<br><br> This field is always returned with the <b>pickupStep</b> container.  # noqa: E501

        :param merchant_location_key: The merchant_location_key of this PickupStep.  # noqa: E501
        :type: str
        """

        self._merchant_location_key = merchant_location_key

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
        if issubclass(PickupStep, dict):
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
        if not isinstance(other, PickupStep):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
