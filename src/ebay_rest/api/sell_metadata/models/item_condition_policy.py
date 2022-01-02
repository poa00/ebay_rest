# coding: utf-8

"""
    Metadata API

    The Metadata API has operations that retrieve configuration details pertaining to the different eBay marketplaces. In addition to marketplace information, the API also has operations that get information that helps sellers list items on eBay.  # noqa: E501

    OpenAPI spec version: v1.5.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ItemConditionPolicy(object):
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
        'item_condition_required': 'bool',
        'item_conditions': 'list[ItemCondition]'
    }

    attribute_map = {
        'category_id': 'categoryId',
        'category_tree_id': 'categoryTreeId',
        'item_condition_required': 'itemConditionRequired',
        'item_conditions': 'itemConditions'
    }

    def __init__(self, category_id=None, category_tree_id=None, item_condition_required=None, item_conditions=None):  # noqa: E501
        """ItemConditionPolicy - a model defined in Swagger"""  # noqa: E501
        self._category_id = None
        self._category_tree_id = None
        self._item_condition_required = None
        self._item_conditions = None
        self.discriminator = None
        if category_id is not None:
            self.category_id = category_id
        if category_tree_id is not None:
            self.category_tree_id = category_tree_id
        if item_condition_required is not None:
            self.item_condition_required = item_condition_required
        if item_conditions is not None:
            self.item_conditions = item_conditions

    @property
    def category_id(self):
        """Gets the category_id of this ItemConditionPolicy.  # noqa: E501

        The category ID to which the item-condition policy applies.  # noqa: E501

        :return: The category_id of this ItemConditionPolicy.  # noqa: E501
        :rtype: str
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this ItemConditionPolicy.

        The category ID to which the item-condition policy applies.  # noqa: E501

        :param category_id: The category_id of this ItemConditionPolicy.  # noqa: E501
        :type: str
        """

        self._category_id = category_id

    @property
    def category_tree_id(self):
        """Gets the category_tree_id of this ItemConditionPolicy.  # noqa: E501

        A value that indicates the root node of the category tree used for the response set. Each marketplace is based on a category tree whose root node is indicated by this unique category ID value. All category policy information returned by this call pertains to the categories included below this root node of the tree.    <br><br>A <i>category tree</i> is a hierarchical framework of eBay categories that begins at the root node of the tree and extends to include all the child nodes in the tree. Each child node in the tree is an eBay category that is represented by a unique <b>categoryId</b> value. Within a category tree, the root node has no parent node and <i>leaf nodes</i> are nodes that have no child nodes.  # noqa: E501

        :return: The category_tree_id of this ItemConditionPolicy.  # noqa: E501
        :rtype: str
        """
        return self._category_tree_id

    @category_tree_id.setter
    def category_tree_id(self, category_tree_id):
        """Sets the category_tree_id of this ItemConditionPolicy.

        A value that indicates the root node of the category tree used for the response set. Each marketplace is based on a category tree whose root node is indicated by this unique category ID value. All category policy information returned by this call pertains to the categories included below this root node of the tree.    <br><br>A <i>category tree</i> is a hierarchical framework of eBay categories that begins at the root node of the tree and extends to include all the child nodes in the tree. Each child node in the tree is an eBay category that is represented by a unique <b>categoryId</b> value. Within a category tree, the root node has no parent node and <i>leaf nodes</i> are nodes that have no child nodes.  # noqa: E501

        :param category_tree_id: The category_tree_id of this ItemConditionPolicy.  # noqa: E501
        :type: str
        """

        self._category_tree_id = category_tree_id

    @property
    def item_condition_required(self):
        """Gets the item_condition_required of this ItemConditionPolicy.  # noqa: E501

        This flag denotes whether or not you must list the item condition in a listing for the specified category. If set to <code>true</code>, you must specify an item condition for the associated category.  # noqa: E501

        :return: The item_condition_required of this ItemConditionPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._item_condition_required

    @item_condition_required.setter
    def item_condition_required(self, item_condition_required):
        """Sets the item_condition_required of this ItemConditionPolicy.

        This flag denotes whether or not you must list the item condition in a listing for the specified category. If set to <code>true</code>, you must specify an item condition for the associated category.  # noqa: E501

        :param item_condition_required: The item_condition_required of this ItemConditionPolicy.  # noqa: E501
        :type: bool
        """

        self._item_condition_required = item_condition_required

    @property
    def item_conditions(self):
        """Gets the item_conditions of this ItemConditionPolicy.  # noqa: E501

        The item-condition values allowed in the category.<br /><br /><span class=\"tablenote\"><b>Note: </b>In all eBay marketplaces, Condition ID 2000 now maps to an item condition of 'Certified Refurbished', and not 'Manufacturer Refurbished'. To list an item as 'Certified Refurbished', a seller must be pre-qualified by eBay for this feature. Any seller who is not eligible for this feature will be blocked if they try to create a new listing or revise an existing listing with this item condition.<br><br> Any seller that is interested in eligibility requirements to list with 'Certified Refurbished' should see the <a href=\"https://pages.ebay.com/seller-center/listing-and-marketing/certified-refurbished-program.html\" target=\"_blank\">Certified refurbished program</a> page in Seller Center. </span><br /><br /><span class=\"tablenote\"><b>Note:</b> For the Cell Phones & Smartphones category (9355), the <code>SELLER_REFURBISHED</code> condition is being deprecated. Sellers trying to list an item in this category (9355) with the condition <code>SELLER_REFURBISHED</code> will be blocked. Starting September 1, 2021, existing listings for this category (9355) with this item condition will be ended by eBay but three new additional refurbished items conditions will be available: <code>EXCELLENT_REFURBISHED</code>, <code>VERY_GOOD_REFURBISHED</code>, and <code>GOOD_REFURBISHED</code>. To be eligible to list with these three item conditions, sellers will have to go through an application process. See <a href=\"https://www.ebay.com/help/selling/listings/creating-managing-listings/item-conditions-category?id=4765#section4\"  target=\"_blank\">Cameras & Photo, Cell Phones & Accessories...</a> for details.</span>  # noqa: E501

        :return: The item_conditions of this ItemConditionPolicy.  # noqa: E501
        :rtype: list[ItemCondition]
        """
        return self._item_conditions

    @item_conditions.setter
    def item_conditions(self, item_conditions):
        """Sets the item_conditions of this ItemConditionPolicy.

        The item-condition values allowed in the category.<br /><br /><span class=\"tablenote\"><b>Note: </b>In all eBay marketplaces, Condition ID 2000 now maps to an item condition of 'Certified Refurbished', and not 'Manufacturer Refurbished'. To list an item as 'Certified Refurbished', a seller must be pre-qualified by eBay for this feature. Any seller who is not eligible for this feature will be blocked if they try to create a new listing or revise an existing listing with this item condition.<br><br> Any seller that is interested in eligibility requirements to list with 'Certified Refurbished' should see the <a href=\"https://pages.ebay.com/seller-center/listing-and-marketing/certified-refurbished-program.html\" target=\"_blank\">Certified refurbished program</a> page in Seller Center. </span><br /><br /><span class=\"tablenote\"><b>Note:</b> For the Cell Phones & Smartphones category (9355), the <code>SELLER_REFURBISHED</code> condition is being deprecated. Sellers trying to list an item in this category (9355) with the condition <code>SELLER_REFURBISHED</code> will be blocked. Starting September 1, 2021, existing listings for this category (9355) with this item condition will be ended by eBay but three new additional refurbished items conditions will be available: <code>EXCELLENT_REFURBISHED</code>, <code>VERY_GOOD_REFURBISHED</code>, and <code>GOOD_REFURBISHED</code>. To be eligible to list with these three item conditions, sellers will have to go through an application process. See <a href=\"https://www.ebay.com/help/selling/listings/creating-managing-listings/item-conditions-category?id=4765#section4\"  target=\"_blank\">Cameras & Photo, Cell Phones & Accessories...</a> for details.</span>  # noqa: E501

        :param item_conditions: The item_conditions of this ItemConditionPolicy.  # noqa: E501
        :type: list[ItemCondition]
        """

        self._item_conditions = item_conditions

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
        if issubclass(ItemConditionPolicy, dict):
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
        if not isinstance(other, ItemConditionPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
