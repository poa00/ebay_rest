# coding: utf-8

"""
    Taxonomy API

    Use the Taxonomy API to discover the most appropriate eBay categories under which sellers can offer inventory items for sale, and the most likely categories under which buyers can browse or search for items to purchase. In addition, the Taxonomy API provides metadata about the required and recommended category aspects to include in listings, and also has two operations to retrieve parts compatibility information.  # noqa: E501

    OpenAPI spec version: v1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ValueConstraint(object):
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
        'applicable_for_localized_aspect_name': 'str',
        'applicable_for_localized_aspect_values': 'list[str]'
    }

    attribute_map = {
        'applicable_for_localized_aspect_name': 'applicableForLocalizedAspectName',
        'applicable_for_localized_aspect_values': 'applicableForLocalizedAspectValues'
    }

    def __init__(self, applicable_for_localized_aspect_name=None, applicable_for_localized_aspect_values=None):  # noqa: E501
        """ValueConstraint - a model defined in Swagger"""  # noqa: E501
        self._applicable_for_localized_aspect_name = None
        self._applicable_for_localized_aspect_values = None
        self.discriminator = None
        if applicable_for_localized_aspect_name is not None:
            self.applicable_for_localized_aspect_name = applicable_for_localized_aspect_name
        if applicable_for_localized_aspect_values is not None:
            self.applicable_for_localized_aspect_values = applicable_for_localized_aspect_values

    @property
    def applicable_for_localized_aspect_name(self):
        """Gets the applicable_for_localized_aspect_name of this ValueConstraint.  # noqa: E501

        The name of the control aspect on which the current aspect value depends.  # noqa: E501

        :return: The applicable_for_localized_aspect_name of this ValueConstraint.  # noqa: E501
        :rtype: str
        """
        return self._applicable_for_localized_aspect_name

    @applicable_for_localized_aspect_name.setter
    def applicable_for_localized_aspect_name(self, applicable_for_localized_aspect_name):
        """Sets the applicable_for_localized_aspect_name of this ValueConstraint.

        The name of the control aspect on which the current aspect value depends.  # noqa: E501

        :param applicable_for_localized_aspect_name: The applicable_for_localized_aspect_name of this ValueConstraint.  # noqa: E501
        :type: str
        """

        self._applicable_for_localized_aspect_name = applicable_for_localized_aspect_name

    @property
    def applicable_for_localized_aspect_values(self):
        """Gets the applicable_for_localized_aspect_values of this ValueConstraint.  # noqa: E501

        Contains a list of the values of the control aspect on which this aspect's value depends. When the control aspect has any of the specified values, the current value of the current aspect will also be available.  # noqa: E501

        :return: The applicable_for_localized_aspect_values of this ValueConstraint.  # noqa: E501
        :rtype: list[str]
        """
        return self._applicable_for_localized_aspect_values

    @applicable_for_localized_aspect_values.setter
    def applicable_for_localized_aspect_values(self, applicable_for_localized_aspect_values):
        """Sets the applicable_for_localized_aspect_values of this ValueConstraint.

        Contains a list of the values of the control aspect on which this aspect's value depends. When the control aspect has any of the specified values, the current value of the current aspect will also be available.  # noqa: E501

        :param applicable_for_localized_aspect_values: The applicable_for_localized_aspect_values of this ValueConstraint.  # noqa: E501
        :type: list[str]
        """

        self._applicable_for_localized_aspect_values = applicable_for_localized_aspect_values

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
        if issubclass(ValueConstraint, dict):
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
        if not isinstance(other, ValueConstraint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other