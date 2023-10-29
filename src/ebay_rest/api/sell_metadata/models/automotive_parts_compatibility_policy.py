# coding: utf-8

"""
    Metadata API

    The Metadata API has operations that retrieve configuration details pertaining to the different eBay marketplaces. In addition to marketplace information, the API also has operations that get information that helps sellers list items on eBay.  # noqa: E501

    OpenAPI spec version: v1.7.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AutomotivePartsCompatibilityPolicy(object):
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
        'compatibility_based_on': 'str',
        'compatible_vehicle_types': 'list[str]',
        'max_number_of_compatible_vehicles': 'int'
    }

    attribute_map = {
        'category_id': 'categoryId',
        'category_tree_id': 'categoryTreeId',
        'compatibility_based_on': 'compatibilityBasedOn',
        'compatible_vehicle_types': 'compatibleVehicleTypes',
        'max_number_of_compatible_vehicles': 'maxNumberOfCompatibleVehicles'
    }

    def __init__(self, category_id=None, category_tree_id=None, compatibility_based_on=None, compatible_vehicle_types=None, max_number_of_compatible_vehicles=None):  # noqa: E501
        """AutomotivePartsCompatibilityPolicy - a model defined in Swagger"""  # noqa: E501
        self._category_id = None
        self._category_tree_id = None
        self._compatibility_based_on = None
        self._compatible_vehicle_types = None
        self._max_number_of_compatible_vehicles = None
        self.discriminator = None
        if category_id is not None:
            self.category_id = category_id
        if category_tree_id is not None:
            self.category_tree_id = category_tree_id
        if compatibility_based_on is not None:
            self.compatibility_based_on = compatibility_based_on
        if compatible_vehicle_types is not None:
            self.compatible_vehicle_types = compatible_vehicle_types
        if max_number_of_compatible_vehicles is not None:
            self.max_number_of_compatible_vehicles = max_number_of_compatible_vehicles

    @property
    def category_id(self):
        """Gets the category_id of this AutomotivePartsCompatibilityPolicy.  # noqa: E501

        The category ID to which the automotive-parts-compatibility policies apply.  # noqa: E501

        :return: The category_id of this AutomotivePartsCompatibilityPolicy.  # noqa: E501
        :rtype: str
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this AutomotivePartsCompatibilityPolicy.

        The category ID to which the automotive-parts-compatibility policies apply.  # noqa: E501

        :param category_id: The category_id of this AutomotivePartsCompatibilityPolicy.  # noqa: E501
        :type: str
        """

        self._category_id = category_id

    @property
    def category_tree_id(self):
        """Gets the category_tree_id of this AutomotivePartsCompatibilityPolicy.  # noqa: E501

        A value that indicates the root node of the category tree used for the response set. Each marketplace is based on a category tree whose root node is indicated by this unique category ID value. All category policy information returned by this call pertains to the categories included below this root node of the tree.    <br><br>A <i>category tree</i> is a hierarchical framework of eBay categories that begins at the root node of the tree and extends to include all the child nodes in the tree. Each child node in the tree is an eBay category that is represented by a unique <b>categoryId</b> value. Within a category tree, the root node has no parent node and <i>leaf nodes</i> are nodes that have no child nodes.  # noqa: E501

        :return: The category_tree_id of this AutomotivePartsCompatibilityPolicy.  # noqa: E501
        :rtype: str
        """
        return self._category_tree_id

    @category_tree_id.setter
    def category_tree_id(self, category_tree_id):
        """Sets the category_tree_id of this AutomotivePartsCompatibilityPolicy.

        A value that indicates the root node of the category tree used for the response set. Each marketplace is based on a category tree whose root node is indicated by this unique category ID value. All category policy information returned by this call pertains to the categories included below this root node of the tree.    <br><br>A <i>category tree</i> is a hierarchical framework of eBay categories that begins at the root node of the tree and extends to include all the child nodes in the tree. Each child node in the tree is an eBay category that is represented by a unique <b>categoryId</b> value. Within a category tree, the root node has no parent node and <i>leaf nodes</i> are nodes that have no child nodes.  # noqa: E501

        :param category_tree_id: The category_tree_id of this AutomotivePartsCompatibilityPolicy.  # noqa: E501
        :type: str
        """

        self._category_tree_id = category_tree_id

    @property
    def compatibility_based_on(self):
        """Gets the compatibility_based_on of this AutomotivePartsCompatibilityPolicy.  # noqa: E501

        Indicates whether the category supports parts compatibility by either <code>ASSEMBLY</code> or by <code>SPECIFICATION</code>. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/metadata/types/sel:CompatibilityTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The compatibility_based_on of this AutomotivePartsCompatibilityPolicy.  # noqa: E501
        :rtype: str
        """
        return self._compatibility_based_on

    @compatibility_based_on.setter
    def compatibility_based_on(self, compatibility_based_on):
        """Sets the compatibility_based_on of this AutomotivePartsCompatibilityPolicy.

        Indicates whether the category supports parts compatibility by either <code>ASSEMBLY</code> or by <code>SPECIFICATION</code>. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/metadata/types/sel:CompatibilityTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param compatibility_based_on: The compatibility_based_on of this AutomotivePartsCompatibilityPolicy.  # noqa: E501
        :type: str
        """

        self._compatibility_based_on = compatibility_based_on

    @property
    def compatible_vehicle_types(self):
        """Gets the compatible_vehicle_types of this AutomotivePartsCompatibilityPolicy.  # noqa: E501

        Indicates the compatibility classification of the part based on high-level vehicle types.  # noqa: E501

        :return: The compatible_vehicle_types of this AutomotivePartsCompatibilityPolicy.  # noqa: E501
        :rtype: list[str]
        """
        return self._compatible_vehicle_types

    @compatible_vehicle_types.setter
    def compatible_vehicle_types(self, compatible_vehicle_types):
        """Sets the compatible_vehicle_types of this AutomotivePartsCompatibilityPolicy.

        Indicates the compatibility classification of the part based on high-level vehicle types.  # noqa: E501

        :param compatible_vehicle_types: The compatible_vehicle_types of this AutomotivePartsCompatibilityPolicy.  # noqa: E501
        :type: list[str]
        """

        self._compatible_vehicle_types = compatible_vehicle_types

    @property
    def max_number_of_compatible_vehicles(self):
        """Gets the max_number_of_compatible_vehicles of this AutomotivePartsCompatibilityPolicy.  # noqa: E501

        Specifies the maximum number of compatible vehicle-applications allowed per item.  # noqa: E501

        :return: The max_number_of_compatible_vehicles of this AutomotivePartsCompatibilityPolicy.  # noqa: E501
        :rtype: int
        """
        return self._max_number_of_compatible_vehicles

    @max_number_of_compatible_vehicles.setter
    def max_number_of_compatible_vehicles(self, max_number_of_compatible_vehicles):
        """Sets the max_number_of_compatible_vehicles of this AutomotivePartsCompatibilityPolicy.

        Specifies the maximum number of compatible vehicle-applications allowed per item.  # noqa: E501

        :param max_number_of_compatible_vehicles: The max_number_of_compatible_vehicles of this AutomotivePartsCompatibilityPolicy.  # noqa: E501
        :type: int
        """

        self._max_number_of_compatible_vehicles = max_number_of_compatible_vehicles

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
        if issubclass(AutomotivePartsCompatibilityPolicy, dict):
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
        if not isinstance(other, AutomotivePartsCompatibilityPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
