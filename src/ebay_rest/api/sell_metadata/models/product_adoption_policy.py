# coding: utf-8

"""
    Metadata API

    The Metadata API has operations that retrieve configuration details pertaining to the different eBay marketplaces. In addition to marketplace information, the API also has operations that get information that helps sellers list items on eBay.  # noqa: E501

    OpenAPI spec version: v1.4.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ProductAdoptionPolicy(object):
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
        'category_tree_id': 'str',
        'exclusion': 'Exclusion',
        'product_required': 'bool'
    }

    attribute_map = {
        'category_id': 'categoryId',
        'category_tree_id': 'categoryTreeId',
        'exclusion': 'exclusion',
        'product_required': 'productRequired'
    }

    def __init__(self, category_id=None, category_tree_id=None, exclusion=None, product_required=None):  # noqa: E501
        """ProductAdoptionPolicy - a model defined in Swagger"""  # noqa: E501
        self._category_id = None
        self._category_tree_id = None
        self._exclusion = None
        self._product_required = None
        self.discriminator = None
        if category_id is not None:
            self.category_id = category_id
        if category_tree_id is not None:
            self.category_tree_id = category_tree_id
        if exclusion is not None:
            self.exclusion = exclusion
        if product_required is not None:
            self.product_required = product_required

    @property
    def category_id(self):
        """Gets the category_id of this ProductAdoptionPolicy.  # noqa: E501

        The category ID to which the listing policies apply.  # noqa: E501

        :return: The category_id of this ProductAdoptionPolicy.  # noqa: E501
        :rtype: str
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this ProductAdoptionPolicy.

        The category ID to which the listing policies apply.  # noqa: E501

        :param category_id: The category_id of this ProductAdoptionPolicy.  # noqa: E501
        :type: str
        """

        self._category_id = category_id

    @property
    def category_tree_id(self):
        """Gets the category_tree_id of this ProductAdoptionPolicy.  # noqa: E501

        A value that indicates the root node of the category tree used for the response set. Each marketplace is based on a category tree whose root node is indicated by this unique category ID value. All category policy information returned by this call pertains to the categories included below this root node of the tree. A category tree is a hierarchical framework of eBay categories that begins at the root node of the tree and extends to include all the child nodes in the tree. Each child node in the tree is an eBay category that is represented by a unique categoryId value. Within a category tree, the root node has no parent node and leaf nodes are nodes that have no child nodes.  # noqa: E501

        :return: The category_tree_id of this ProductAdoptionPolicy.  # noqa: E501
        :rtype: str
        """
        return self._category_tree_id

    @category_tree_id.setter
    def category_tree_id(self, category_tree_id):
        """Sets the category_tree_id of this ProductAdoptionPolicy.

        A value that indicates the root node of the category tree used for the response set. Each marketplace is based on a category tree whose root node is indicated by this unique category ID value. All category policy information returned by this call pertains to the categories included below this root node of the tree. A category tree is a hierarchical framework of eBay categories that begins at the root node of the tree and extends to include all the child nodes in the tree. Each child node in the tree is an eBay category that is represented by a unique categoryId value. Within a category tree, the root node has no parent node and leaf nodes are nodes that have no child nodes.  # noqa: E501

        :param category_tree_id: The category_tree_id of this ProductAdoptionPolicy.  # noqa: E501
        :type: str
        """

        self._category_tree_id = category_tree_id

    @property
    def exclusion(self):
        """Gets the exclusion of this ProductAdoptionPolicy.  # noqa: E501


        :return: The exclusion of this ProductAdoptionPolicy.  # noqa: E501
        :rtype: Exclusion
        """
        return self._exclusion

    @exclusion.setter
    def exclusion(self, exclusion):
        """Sets the exclusion of this ProductAdoptionPolicy.


        :param exclusion: The exclusion of this ProductAdoptionPolicy.  # noqa: E501
        :type: Exclusion
        """

        self._exclusion = exclusion

    @property
    def product_required(self):
        """Gets the product_required of this ProductAdoptionPolicy.  # noqa: E501

        If set to true, items must include an ePID value in their item description before they can be listed in the category identified by the associated categoryId. In contrast, a value of false indicates that items listed in the associated category do not require ePID values. Important! It is possible for a productAdoptionPolicies container to not contain this productRequired field. This occurs if the eBay category is not part of the PBSE Phase 1 or Phase 2 mandate. In these scenarios, please treat the response the same as if this field were present and contained a value of false.  # noqa: E501

        :return: The product_required of this ProductAdoptionPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._product_required

    @product_required.setter
    def product_required(self, product_required):
        """Sets the product_required of this ProductAdoptionPolicy.

        If set to true, items must include an ePID value in their item description before they can be listed in the category identified by the associated categoryId. In contrast, a value of false indicates that items listed in the associated category do not require ePID values. Important! It is possible for a productAdoptionPolicies container to not contain this productRequired field. This occurs if the eBay category is not part of the PBSE Phase 1 or Phase 2 mandate. In these scenarios, please treat the response the same as if this field were present and contained a value of false.  # noqa: E501

        :param product_required: The product_required of this ProductAdoptionPolicy.  # noqa: E501
        :type: bool
        """

        self._product_required = product_required

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
        if issubclass(ProductAdoptionPolicy, dict):
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
        if not isinstance(other, ProductAdoptionPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
