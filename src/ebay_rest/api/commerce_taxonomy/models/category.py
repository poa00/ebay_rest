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

class Category(object):
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
        'category_id': 'str',
        'category_name': 'str'
    }

    attribute_map = {
        'category_id': 'categoryId',
        'category_name': 'categoryName'
    }

    def __init__(self, category_id=None, category_name=None):  # noqa: E501
        """Category - a model defined in Swagger"""  # noqa: E501
        self._category_id = None
        self._category_name = None
        self.discriminator = None
        if category_id is not None:
            self.category_id = category_id
        if category_name is not None:
            self.category_name = category_name

    @property
    def category_id(self):
        """Gets the category_id of this Category.  # noqa: E501

        The unique identifier of the eBay category within its category tree. Note: The root node of a full default category tree includes the categoryId field, but its value should not be relied upon. It provides no useful information for application development.  # noqa: E501

        :return: The category_id of this Category.  # noqa: E501
        :rtype: str
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this Category.

        The unique identifier of the eBay category within its category tree. Note: The root node of a full default category tree includes the categoryId field, but its value should not be relied upon. It provides no useful information for application development.  # noqa: E501

        :param category_id: The category_id of this Category.  # noqa: E501
        :type: str
        """

        self._category_id = category_id

    @property
    def category_name(self):
        """Gets the category_name of this Category.  # noqa: E501

        The name of the category identified by categoryId.  # noqa: E501

        :return: The category_name of this Category.  # noqa: E501
        :rtype: str
        """
        return self._category_name

    @category_name.setter
    def category_name(self, category_name):
        """Sets the category_name of this Category.

        The name of the category identified by categoryId.  # noqa: E501

        :param category_name: The category_name of this Category.  # noqa: E501
        :type: str
        """

        self._category_name = category_name

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
        if issubclass(Category, dict):
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
        if not isinstance(other, Category):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
