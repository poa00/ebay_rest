# coding: utf-8

"""
    Notification API

    The eBay Notification API enables management of the entire end-to-end eBay notification experience by allowing users to:<ul><li>Browse for supported notification topics and retrieve topic details</li><li>Create, configure, and manage notification destination endpoints</li><li>Configure, manage, and test notification subscriptions</li><li>Process eBay notifications and verify the integrity of the message payload</li></ul>  # noqa: E501

    OpenAPI spec version: v1.4.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PublicKey(object):
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
        'algorithm': 'str',
        'digest': 'str',
        'key': 'str'
    }

    attribute_map = {
        'algorithm': 'algorithm',
        'digest': 'digest',
        'key': 'key'
    }

    def __init__(self, algorithm=None, digest=None, key=None):  # noqa: E501
        """PublicKey - a model defined in Swagger"""  # noqa: E501
        self._algorithm = None
        self._digest = None
        self._key = None
        self.discriminator = None
        if algorithm is not None:
            self.algorithm = algorithm
        if digest is not None:
            self.digest = digest
        if key is not None:
            self.key = key

    @property
    def algorithm(self):
        """Gets the algorithm of this PublicKey.  # noqa: E501

        The algorithm associated with the public key that is returned, such as Elliptic Curve Digital Signature Algorithm (ECDSA).  # noqa: E501

        :return: The algorithm of this PublicKey.  # noqa: E501
        :rtype: str
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        """Sets the algorithm of this PublicKey.

        The algorithm associated with the public key that is returned, such as Elliptic Curve Digital Signature Algorithm (ECDSA).  # noqa: E501

        :param algorithm: The algorithm of this PublicKey.  # noqa: E501
        :type: str
        """

        self._algorithm = algorithm

    @property
    def digest(self):
        """Gets the digest of this PublicKey.  # noqa: E501

        The digest associated with the public key that is returned, such as Secure Hash Algorithm 1 (SHA1).  # noqa: E501

        :return: The digest of this PublicKey.  # noqa: E501
        :rtype: str
        """
        return self._digest

    @digest.setter
    def digest(self, digest):
        """Sets the digest of this PublicKey.

        The digest associated with the public key that is returned, such as Secure Hash Algorithm 1 (SHA1).  # noqa: E501

        :param digest: The digest of this PublicKey.  # noqa: E501
        :type: str
        """

        self._digest = digest

    @property
    def key(self):
        """Gets the key of this PublicKey.  # noqa: E501

        The public key that is returned for the specified key ID.<br /><br />This value is used to validate the eBay push notification message payload.  # noqa: E501

        :return: The key of this PublicKey.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this PublicKey.

        The public key that is returned for the specified key ID.<br /><br />This value is used to validate the eBay push notification message payload.  # noqa: E501

        :param key: The key of this PublicKey.  # noqa: E501
        :type: str
        """

        self._key = key

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
        if issubclass(PublicKey, dict):
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
        if not isinstance(other, PublicKey):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
