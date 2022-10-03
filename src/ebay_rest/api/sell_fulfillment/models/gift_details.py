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

class GiftDetails(object):
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
        'message': 'str',
        'recipient_email': 'str',
        'sender_name': 'str'
    }

    attribute_map = {
        'message': 'message',
        'recipient_email': 'recipientEmail',
        'sender_name': 'senderName'
    }

    def __init__(self, message=None, recipient_email=None, sender_name=None):  # noqa: E501
        """GiftDetails - a model defined in Swagger"""  # noqa: E501
        self._message = None
        self._recipient_email = None
        self._sender_name = None
        self.discriminator = None
        if message is not None:
            self.message = message
        if recipient_email is not None:
            self.recipient_email = recipient_email
        if sender_name is not None:
            self.sender_name = sender_name

    @property
    def message(self):
        """Gets the message of this GiftDetails.  # noqa: E501

        This field contains the gift message from the buyer to the gift recipient. This field is only returned if the buyer of the gift included a message for the gift.  # noqa: E501

        :return: The message of this GiftDetails.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this GiftDetails.

        This field contains the gift message from the buyer to the gift recipient. This field is only returned if the buyer of the gift included a message for the gift.  # noqa: E501

        :param message: The message of this GiftDetails.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def recipient_email(self):
        """Gets the recipient_email of this GiftDetails.  # noqa: E501

        The email address of the gift recipient. The seller will send the digital gift card to this email address.  # noqa: E501

        :return: The recipient_email of this GiftDetails.  # noqa: E501
        :rtype: str
        """
        return self._recipient_email

    @recipient_email.setter
    def recipient_email(self, recipient_email):
        """Sets the recipient_email of this GiftDetails.

        The email address of the gift recipient. The seller will send the digital gift card to this email address.  # noqa: E501

        :param recipient_email: The recipient_email of this GiftDetails.  # noqa: E501
        :type: str
        """

        self._recipient_email = recipient_email

    @property
    def sender_name(self):
        """Gets the sender_name of this GiftDetails.  # noqa: E501

        The name of the buyer, which will appear on the email that is sent to the gift recipient.  # noqa: E501

        :return: The sender_name of this GiftDetails.  # noqa: E501
        :rtype: str
        """
        return self._sender_name

    @sender_name.setter
    def sender_name(self, sender_name):
        """Sets the sender_name of this GiftDetails.

        The name of the buyer, which will appear on the email that is sent to the gift recipient.  # noqa: E501

        :param sender_name: The sender_name of this GiftDetails.  # noqa: E501
        :type: str
        """

        self._sender_name = sender_name

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
        if issubclass(GiftDetails, dict):
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
        if not isinstance(other, GiftDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
