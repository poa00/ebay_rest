# coding: utf-8

"""
    Inventory API

    The Inventory API is used to create and manage inventory, and then to publish and manage this inventory on an eBay marketplace. There are also methods in this API that will convert eligible, active eBay listings into the Inventory API model.  # noqa: E501

    OpenAPI spec version: 1.16.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InventoryItems(object):
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
        'href': 'str',
        'inventory_items': 'list[InventoryItemWithSkuLocaleGroupid]',
        'limit': 'int',
        'next': 'str',
        'prev': 'str',
        'size': 'int',
        'total': 'int'
    }

    attribute_map = {
        'href': 'href',
        'inventory_items': 'inventoryItems',
        'limit': 'limit',
        'next': 'next',
        'prev': 'prev',
        'size': 'size',
        'total': 'total'
    }

    def __init__(self, href=None, inventory_items=None, limit=None, next=None, prev=None, size=None, total=None):  # noqa: E501
        """InventoryItems - a model defined in Swagger"""  # noqa: E501
        self._href = None
        self._inventory_items = None
        self._limit = None
        self._next = None
        self._prev = None
        self._size = None
        self._total = None
        self.discriminator = None
        if href is not None:
            self.href = href
        if inventory_items is not None:
            self.inventory_items = inventory_items
        if limit is not None:
            self.limit = limit
        if next is not None:
            self.next = next
        if prev is not None:
            self.prev = prev
        if size is not None:
            self.size = size
        if total is not None:
            self.total = total

    @property
    def href(self):
        """Gets the href of this InventoryItems.  # noqa: E501

        This is the URL to the current page of inventory items.  # noqa: E501

        :return: The href of this InventoryItems.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this InventoryItems.

        This is the URL to the current page of inventory items.  # noqa: E501

        :param href: The href of this InventoryItems.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def inventory_items(self):
        """Gets the inventory_items of this InventoryItems.  # noqa: E501

        This container is an array of one or more inventory items, with detailed information on each inventory item.  # noqa: E501

        :return: The inventory_items of this InventoryItems.  # noqa: E501
        :rtype: list[InventoryItemWithSkuLocaleGroupid]
        """
        return self._inventory_items

    @inventory_items.setter
    def inventory_items(self, inventory_items):
        """Sets the inventory_items of this InventoryItems.

        This container is an array of one or more inventory items, with detailed information on each inventory item.  # noqa: E501

        :param inventory_items: The inventory_items of this InventoryItems.  # noqa: E501
        :type: list[InventoryItemWithSkuLocaleGroupid]
        """

        self._inventory_items = inventory_items

    @property
    def limit(self):
        """Gets the limit of this InventoryItems.  # noqa: E501

        This integer value is the number of inventory items that will be displayed on each results page.  # noqa: E501

        :return: The limit of this InventoryItems.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this InventoryItems.

        This integer value is the number of inventory items that will be displayed on each results page.  # noqa: E501

        :param limit: The limit of this InventoryItems.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def next(self):
        """Gets the next of this InventoryItems.  # noqa: E501

        This is the URL to the next page of inventory items. This field will only be returned if there are additional inventory items to view.  # noqa: E501

        :return: The next of this InventoryItems.  # noqa: E501
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this InventoryItems.

        This is the URL to the next page of inventory items. This field will only be returned if there are additional inventory items to view.  # noqa: E501

        :param next: The next of this InventoryItems.  # noqa: E501
        :type: str
        """

        self._next = next

    @property
    def prev(self):
        """Gets the prev of this InventoryItems.  # noqa: E501

        This is the URL to the previous page of inventory items. This field will only be returned if there are previous inventory items to view.  # noqa: E501

        :return: The prev of this InventoryItems.  # noqa: E501
        :rtype: str
        """
        return self._prev

    @prev.setter
    def prev(self, prev):
        """Sets the prev of this InventoryItems.

        This is the URL to the previous page of inventory items. This field will only be returned if there are previous inventory items to view.  # noqa: E501

        :param prev: The prev of this InventoryItems.  # noqa: E501
        :type: str
        """

        self._prev = prev

    @property
    def size(self):
        """Gets the size of this InventoryItems.  # noqa: E501

        This integer value indicates the total number of pages of results that are available. This number will depend on the total number of inventory items available for viewing, and on the <strong>limit</strong> value.  # noqa: E501

        :return: The size of this InventoryItems.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this InventoryItems.

        This integer value indicates the total number of pages of results that are available. This number will depend on the total number of inventory items available for viewing, and on the <strong>limit</strong> value.  # noqa: E501

        :param size: The size of this InventoryItems.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def total(self):
        """Gets the total of this InventoryItems.  # noqa: E501

        This integer value is the total number of inventory items that exist for the seller's account. Based on this number and on the <strong>limit</strong> value, the seller may have to toggle through multiple pages to view all inventory items.  # noqa: E501

        :return: The total of this InventoryItems.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this InventoryItems.

        This integer value is the total number of inventory items that exist for the seller's account. Based on this number and on the <strong>limit</strong> value, the seller may have to toggle through multiple pages to view all inventory items.  # noqa: E501

        :param total: The total of this InventoryItems.  # noqa: E501
        :type: int
        """

        self._total = total

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
        if issubclass(InventoryItems, dict):
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
        if not isinstance(other, InventoryItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
