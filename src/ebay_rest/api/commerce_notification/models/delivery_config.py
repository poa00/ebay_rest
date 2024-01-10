# coding: utf-8

"""
    Notification API

    The eBay Notification API enables management of the entire end-to-end eBay notification experience by allowing users to:<ul><li>Browse for supported notification topics and retrieve topic details</li><li>Create, configure, and manage notification destination endpoints</li><li>Configure, manage, and test notification subscriptions</li><li>Process eBay notifications and verify the integrity of the message payload</li></ul>  # noqa: E501

    OpenAPI spec version: v1.5.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DeliveryConfig(object):
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
        'endpoint': 'str',
        'verification_token': 'str'
    }

    attribute_map = {
        'endpoint': 'endpoint',
        'verification_token': 'verificationToken'
    }

    def __init__(self, endpoint=None, verification_token=None):  # noqa: E501
        """DeliveryConfig - a model defined in Swagger"""  # noqa: E501
        self._endpoint = None
        self._verification_token = None
        self.discriminator = None
        if endpoint is not None:
            self.endpoint = endpoint
        if verification_token is not None:
            self.verification_token = verification_token

    @property
    def endpoint(self):
        """Gets the endpoint of this DeliveryConfig.  # noqa: E501

        The endpoint for this destination.  # noqa: E501

        :return: The endpoint of this DeliveryConfig.  # noqa: E501
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this DeliveryConfig.

        The endpoint for this destination.  # noqa: E501

        :param endpoint: The endpoint of this DeliveryConfig.  # noqa: E501
        :type: str
        """

        self._endpoint = endpoint

    @property
    def verification_token(self):
        """Gets the verification_token of this DeliveryConfig.  # noqa: E501

        The verification token associated with this endpoint.  # noqa: E501

        :return: The verification_token of this DeliveryConfig.  # noqa: E501
        :rtype: str
        """
        return self._verification_token

    @verification_token.setter
    def verification_token(self, verification_token):
        """Sets the verification_token of this DeliveryConfig.

        The verification token associated with this endpoint.  # noqa: E501

        :param verification_token: The verification_token of this DeliveryConfig.  # noqa: E501
        :type: str
        """

        self._verification_token = verification_token

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
        if issubclass(DeliveryConfig, dict):
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
        if not isinstance(other, DeliveryConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
