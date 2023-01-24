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

class InventoryItemWithSkuLocaleGroupKeys(object):
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
        'availability': 'AvailabilityWithAll',
        'condition': 'str',
        'condition_description': 'str',
        'inventory_item_group_keys': 'list[str]',
        'locale': 'str',
        'package_weight_and_size': 'PackageWeightAndSize',
        'product': 'Product',
        'sku': 'str'
    }

    attribute_map = {
        'availability': 'availability',
        'condition': 'condition',
        'condition_description': 'conditionDescription',
        'inventory_item_group_keys': 'inventoryItemGroupKeys',
        'locale': 'locale',
        'package_weight_and_size': 'packageWeightAndSize',
        'product': 'product',
        'sku': 'sku'
    }

    def __init__(self, availability=None, condition=None, condition_description=None, inventory_item_group_keys=None, locale=None, package_weight_and_size=None, product=None, sku=None):  # noqa: E501
        """InventoryItemWithSkuLocaleGroupKeys - a model defined in Swagger"""  # noqa: E501
        self._availability = None
        self._condition = None
        self._condition_description = None
        self._inventory_item_group_keys = None
        self._locale = None
        self._package_weight_and_size = None
        self._product = None
        self._sku = None
        self.discriminator = None
        if availability is not None:
            self.availability = availability
        if condition is not None:
            self.condition = condition
        if condition_description is not None:
            self.condition_description = condition_description
        if inventory_item_group_keys is not None:
            self.inventory_item_group_keys = inventory_item_group_keys
        if locale is not None:
            self.locale = locale
        if package_weight_and_size is not None:
            self.package_weight_and_size = package_weight_and_size
        if product is not None:
            self.product = product
        if sku is not None:
            self.sku = sku

    @property
    def availability(self):
        """Gets the availability of this InventoryItemWithSkuLocaleGroupKeys.  # noqa: E501


        :return: The availability of this InventoryItemWithSkuLocaleGroupKeys.  # noqa: E501
        :rtype: AvailabilityWithAll
        """
        return self._availability

    @availability.setter
    def availability(self, availability):
        """Sets the availability of this InventoryItemWithSkuLocaleGroupKeys.


        :param availability: The availability of this InventoryItemWithSkuLocaleGroupKeys.  # noqa: E501
        :type: AvailabilityWithAll
        """

        self._availability = availability

    @property
    def condition(self):
        """Gets the condition of this InventoryItemWithSkuLocaleGroupKeys.  # noqa: E501

        This enumeration value indicates the condition of the item. Supported item condition values will vary by eBay site and category. <br><br> Since the condition of an inventory item must be specified before being published in an offer, this field is always returned in the 'Get' calls for SKUs that are part of a published offer. If a SKU is not part of a published offer, this field will only be returned if set for the inventory item.<br><br> <span class=\"tablenote\"> <strong>Note:</strong> The 'Manufacturer Refurbished' item condition is no longer a valid item condition on any eBay marketplace, and to reflect this change, the <code>MANUFACTURER_REFURBISHED</code> value has essentially been replaced with the <code>CERTIFIED_REFURBISHED</code> enumeration value with Version 1.13.0. For any existing inventory items that have <code>MANUFACTURER_REFURBISHED</code> set as their <strong>condition</strong> value, eBay will automatically convert the condition of these inventory items to <code>CERTIFIED_REFURBISHED</code>, so it is not necessary for the developer to update these inventory items with a 'create or replace' call. <br><br> To list an item as 'Certified Refurbished', a seller must be pre-qualified by eBay for this feature. Any seller who is not eligible for this feature will be blocked if they try to create a new listing or revise an existing listing with this item condition. <br><br> Any seller that is interested in eligibility requirements to list with 'Certified Refurbished' should see the <a href=\"https://pages.ebay.com/seller-center/listing-and-marketing/certified-refurbished-program.html \" target=\"_blank\">Certified refurbished program</a> page in Seller Center. </span> For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/inventory/types/slr:ConditionEnum'>eBay API documentation</a>  # noqa: E501

        :return: The condition of this InventoryItemWithSkuLocaleGroupKeys.  # noqa: E501
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this InventoryItemWithSkuLocaleGroupKeys.

        This enumeration value indicates the condition of the item. Supported item condition values will vary by eBay site and category. <br><br> Since the condition of an inventory item must be specified before being published in an offer, this field is always returned in the 'Get' calls for SKUs that are part of a published offer. If a SKU is not part of a published offer, this field will only be returned if set for the inventory item.<br><br> <span class=\"tablenote\"> <strong>Note:</strong> The 'Manufacturer Refurbished' item condition is no longer a valid item condition on any eBay marketplace, and to reflect this change, the <code>MANUFACTURER_REFURBISHED</code> value has essentially been replaced with the <code>CERTIFIED_REFURBISHED</code> enumeration value with Version 1.13.0. For any existing inventory items that have <code>MANUFACTURER_REFURBISHED</code> set as their <strong>condition</strong> value, eBay will automatically convert the condition of these inventory items to <code>CERTIFIED_REFURBISHED</code>, so it is not necessary for the developer to update these inventory items with a 'create or replace' call. <br><br> To list an item as 'Certified Refurbished', a seller must be pre-qualified by eBay for this feature. Any seller who is not eligible for this feature will be blocked if they try to create a new listing or revise an existing listing with this item condition. <br><br> Any seller that is interested in eligibility requirements to list with 'Certified Refurbished' should see the <a href=\"https://pages.ebay.com/seller-center/listing-and-marketing/certified-refurbished-program.html \" target=\"_blank\">Certified refurbished program</a> page in Seller Center. </span> For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/inventory/types/slr:ConditionEnum'>eBay API documentation</a>  # noqa: E501

        :param condition: The condition of this InventoryItemWithSkuLocaleGroupKeys.  # noqa: E501
        :type: str
        """

        self._condition = condition

    @property
    def condition_description(self):
        """Gets the condition_description of this InventoryItemWithSkuLocaleGroupKeys.  # noqa: E501

        This string field is used by the seller to more clearly describe the condition of used items, or items that are not 'Brand New', 'New with tags', or 'New in box'. The ConditionDescription field is available for all categories. If the ConditionDescription field is used with an item in a new condition (Condition IDs 1000-1499), eBay will simply ignore this field if included, and eBay will return a warning message to the user. This field should only be used to further clarify the condition of the used item. It should not be used for branding, promotions, shipping, returns, payment or other information unrelated to the condition of the item. Make sure that the condition value, condition description, listing description, and the item's pictures do not contradict one another.Max length: 1000.  # noqa: E501

        :return: The condition_description of this InventoryItemWithSkuLocaleGroupKeys.  # noqa: E501
        :rtype: str
        """
        return self._condition_description

    @condition_description.setter
    def condition_description(self, condition_description):
        """Sets the condition_description of this InventoryItemWithSkuLocaleGroupKeys.

        This string field is used by the seller to more clearly describe the condition of used items, or items that are not 'Brand New', 'New with tags', or 'New in box'. The ConditionDescription field is available for all categories. If the ConditionDescription field is used with an item in a new condition (Condition IDs 1000-1499), eBay will simply ignore this field if included, and eBay will return a warning message to the user. This field should only be used to further clarify the condition of the used item. It should not be used for branding, promotions, shipping, returns, payment or other information unrelated to the condition of the item. Make sure that the condition value, condition description, listing description, and the item's pictures do not contradict one another.Max length: 1000.  # noqa: E501

        :param condition_description: The condition_description of this InventoryItemWithSkuLocaleGroupKeys.  # noqa: E501
        :type: str
        """

        self._condition_description = condition_description

    @property
    def inventory_item_group_keys(self):
        """Gets the inventory_item_group_keys of this InventoryItemWithSkuLocaleGroupKeys.  # noqa: E501

        This array is returned if the inventory item is associated with any inventory item group(s). The value(s) returned in this array are the unique identifier(s) of the inventory item's variation in a multiple-variation listing. This array is not returned if the inventory item is not associated with any inventory item groups.  # noqa: E501

        :return: The inventory_item_group_keys of this InventoryItemWithSkuLocaleGroupKeys.  # noqa: E501
        :rtype: list[str]
        """
        return self._inventory_item_group_keys

    @inventory_item_group_keys.setter
    def inventory_item_group_keys(self, inventory_item_group_keys):
        """Sets the inventory_item_group_keys of this InventoryItemWithSkuLocaleGroupKeys.

        This array is returned if the inventory item is associated with any inventory item group(s). The value(s) returned in this array are the unique identifier(s) of the inventory item's variation in a multiple-variation listing. This array is not returned if the inventory item is not associated with any inventory item groups.  # noqa: E501

        :param inventory_item_group_keys: The inventory_item_group_keys of this InventoryItemWithSkuLocaleGroupKeys.  # noqa: E501
        :type: list[str]
        """

        self._inventory_item_group_keys = inventory_item_group_keys

    @property
    def locale(self):
        """Gets the locale of this InventoryItemWithSkuLocaleGroupKeys.  # noqa: E501

        This field returns the natural language that was provided in the field values of the request payload (i.e., en_AU, en_GB or de_DE). For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/inventory/types/slr:LocaleEnum'>eBay API documentation</a>  # noqa: E501

        :return: The locale of this InventoryItemWithSkuLocaleGroupKeys.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this InventoryItemWithSkuLocaleGroupKeys.

        This field returns the natural language that was provided in the field values of the request payload (i.e., en_AU, en_GB or de_DE). For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/inventory/types/slr:LocaleEnum'>eBay API documentation</a>  # noqa: E501

        :param locale: The locale of this InventoryItemWithSkuLocaleGroupKeys.  # noqa: E501
        :type: str
        """

        self._locale = locale

    @property
    def package_weight_and_size(self):
        """Gets the package_weight_and_size of this InventoryItemWithSkuLocaleGroupKeys.  # noqa: E501


        :return: The package_weight_and_size of this InventoryItemWithSkuLocaleGroupKeys.  # noqa: E501
        :rtype: PackageWeightAndSize
        """
        return self._package_weight_and_size

    @package_weight_and_size.setter
    def package_weight_and_size(self, package_weight_and_size):
        """Sets the package_weight_and_size of this InventoryItemWithSkuLocaleGroupKeys.


        :param package_weight_and_size: The package_weight_and_size of this InventoryItemWithSkuLocaleGroupKeys.  # noqa: E501
        :type: PackageWeightAndSize
        """

        self._package_weight_and_size = package_weight_and_size

    @property
    def product(self):
        """Gets the product of this InventoryItemWithSkuLocaleGroupKeys.  # noqa: E501


        :return: The product of this InventoryItemWithSkuLocaleGroupKeys.  # noqa: E501
        :rtype: Product
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this InventoryItemWithSkuLocaleGroupKeys.


        :param product: The product of this InventoryItemWithSkuLocaleGroupKeys.  # noqa: E501
        :type: Product
        """

        self._product = product

    @property
    def sku(self):
        """Gets the sku of this InventoryItemWithSkuLocaleGroupKeys.  # noqa: E501

        The seller-defined Stock-Keeping Unit (SKU) of the inventory item. The seller should have a unique SKU value for every product that they sell.  # noqa: E501

        :return: The sku of this InventoryItemWithSkuLocaleGroupKeys.  # noqa: E501
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this InventoryItemWithSkuLocaleGroupKeys.

        The seller-defined Stock-Keeping Unit (SKU) of the inventory item. The seller should have a unique SKU value for every product that they sell.  # noqa: E501

        :param sku: The sku of this InventoryItemWithSkuLocaleGroupKeys.  # noqa: E501
        :type: str
        """

        self._sku = sku

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
        if issubclass(InventoryItemWithSkuLocaleGroupKeys, dict):
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
        if not isinstance(other, InventoryItemWithSkuLocaleGroupKeys):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
