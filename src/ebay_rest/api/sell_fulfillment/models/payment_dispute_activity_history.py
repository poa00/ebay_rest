# coding: utf-8

"""
    Fulfillment API

    Use the Fulfillment API to complete the process of packaging, addressing, handling, and shipping each order on behalf of the seller, in accordance with the payment method and timing specified at checkout.  # noqa: E501

    OpenAPI spec version: v1.19.15
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PaymentDisputeActivityHistory(object):
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
        'activity': 'list[PaymentDisputeActivity]'
    }

    attribute_map = {
        'activity': 'activity'
    }

    def __init__(self, activity=None):  # noqa: E501
        """PaymentDisputeActivityHistory - a model defined in Swagger"""  # noqa: E501
        self._activity = None
        self.discriminator = None
        if activity is not None:
            self.activity = activity

    @property
    def activity(self):
        """Gets the activity of this PaymentDisputeActivityHistory.  # noqa: E501

        This array holds all activities of a payment dispute, from creation to resolution. For each activity, the activity type, the actor, and a timestamp is shown. The <strong>getActivities</strong> response is dynamic, and grows with each recorded activity.  # noqa: E501

        :return: The activity of this PaymentDisputeActivityHistory.  # noqa: E501
        :rtype: list[PaymentDisputeActivity]
        """
        return self._activity

    @activity.setter
    def activity(self, activity):
        """Sets the activity of this PaymentDisputeActivityHistory.

        This array holds all activities of a payment dispute, from creation to resolution. For each activity, the activity type, the actor, and a timestamp is shown. The <strong>getActivities</strong> response is dynamic, and grows with each recorded activity.  # noqa: E501

        :param activity: The activity of this PaymentDisputeActivityHistory.  # noqa: E501
        :type: list[PaymentDisputeActivity]
        """

        self._activity = activity

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
        if issubclass(PaymentDisputeActivityHistory, dict):
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
        if not isinstance(other, PaymentDisputeActivityHistory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
