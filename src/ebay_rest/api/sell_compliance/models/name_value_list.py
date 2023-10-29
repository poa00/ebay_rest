# coding: utf-8

"""
    Compliance API

    Service for providing information to sellers about their listings being non-compliant, or at risk for becoming non-compliant, against eBay listing policies.  # noqa: E501

    OpenAPI spec version: 1.4.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class NameValueList(object):
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
        'name': 'str',
        'value': 'str'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value'
    }

    def __init__(self, name=None, value=None):  # noqa: E501
        """NameValueList - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._value = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if value is not None:
            self.value = value

    @property
    def name(self):
        """Gets the name of this NameValueList.  # noqa: E501

        This is the name of the variation aspect, or the name of the category of information that is returned through the name-value pair. The type of information that appears here will vary based on the compliance type and type of violation.  # noqa: E501

        :return: The name of this NameValueList.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NameValueList.

        This is the name of the variation aspect, or the name of the category of information that is returned through the name-value pair. The type of information that appears here will vary based on the compliance type and type of violation.  # noqa: E501

        :param name: The name of this NameValueList.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def value(self):
        """Gets the value of this NameValueList.  # noqa: E501

        This is the value of the variation aspect (in <strong>name</strong> field), or the value of the category of information that is returned through the name-value pair. The type of information that appears here will vary based on the compliance type and type of violation.  # noqa: E501

        :return: The value of this NameValueList.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this NameValueList.

        This is the value of the variation aspect (in <strong>name</strong> field), or the value of the category of information that is returned through the name-value pair. The type of information that appears here will vary based on the compliance type and type of violation.  # noqa: E501

        :param value: The value of this NameValueList.  # noqa: E501
        :type: str
        """

        self._value = value

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
        if issubclass(NameValueList, dict):
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
        if not isinstance(other, NameValueList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
