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

class Version(object):
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
        'instance': 'Version',
        'version': 'str'
    }

    attribute_map = {
        'instance': 'instance',
        'version': 'version'
    }

    def __init__(self, instance=None, version=None):  # noqa: E501
        """Version - a model defined in Swagger"""  # noqa: E501
        self._instance = None
        self._version = None
        self.discriminator = None
        if instance is not None:
            self.instance = instance
        if version is not None:
            self.version = version

    @property
    def instance(self):
        """Gets the instance of this Version.  # noqa: E501


        :return: The instance of this Version.  # noqa: E501
        :rtype: Version
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        """Sets the instance of this Version.


        :param instance: The instance of this Version.  # noqa: E501
        :type: Version
        """

        self._instance = instance

    @property
    def version(self):
        """Gets the version of this Version.  # noqa: E501

        The version number of the service or API.  # noqa: E501

        :return: The version of this Version.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Version.

        The version number of the service or API.  # noqa: E501

        :param version: The version of this Version.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if issubclass(Version, dict):
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
        if not isinstance(other, Version):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
