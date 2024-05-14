# coding: utf-8

"""
    Inventory API

    The Inventory API is used to create and manage inventory, and then to publish and manage this inventory on an eBay marketplace. There are also methods in this API that will convert eligible, active eBay listings into the Inventory API model.  # noqa: E501

    OpenAPI spec version: 1.17.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Compatibility(object):
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
        'compatible_products': 'list[CompatibleProduct]',
        'sku': 'str'
    }

    attribute_map = {
        'compatible_products': 'compatibleProducts',
        'sku': 'sku'
    }

    def __init__(self, compatible_products=None, sku=None):  # noqa: E501
        """Compatibility - a model defined in Swagger"""  # noqa: E501
        self._compatible_products = None
        self._sku = None
        self.discriminator = None
        if compatible_products is not None:
            self.compatible_products = compatible_products
        if sku is not None:
            self.sku = sku

    @property
    def compatible_products(self):
        """Gets the compatible_products of this Compatibility.  # noqa: E501

        This container consists of an array of motor vehicles (make, model, year, trim, engine) that are compatible with the motor vehicle part or accessory specified by the sku value.  # noqa: E501

        :return: The compatible_products of this Compatibility.  # noqa: E501
        :rtype: list[CompatibleProduct]
        """
        return self._compatible_products

    @compatible_products.setter
    def compatible_products(self, compatible_products):
        """Sets the compatible_products of this Compatibility.

        This container consists of an array of motor vehicles (make, model, year, trim, engine) that are compatible with the motor vehicle part or accessory specified by the sku value.  # noqa: E501

        :param compatible_products: The compatible_products of this Compatibility.  # noqa: E501
        :type: list[CompatibleProduct]
        """

        self._compatible_products = compatible_products

    @property
    def sku(self):
        """Gets the sku of this Compatibility.  # noqa: E501

        The seller-defined SKU value of the inventory item that will be associated with the compatible vehicles.<br><br><span class=\"tablenote\"><b>Note:</b> This field is not applicable to the <strong>createOrReplaceProductCompatibility</strong> method, as the SKU value for the inventory item is passed in as part of the call URI and not in the request payload. It is always returned with the <a href=\"/api-docs/sell/inventory/resources/inventory_item/product_compatibility/methods/getProductCompatibility\" target=\"_blank \">getProductCompatibility</a> method.</span>  # noqa: E501

        :return: The sku of this Compatibility.  # noqa: E501
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this Compatibility.

        The seller-defined SKU value of the inventory item that will be associated with the compatible vehicles.<br><br><span class=\"tablenote\"><b>Note:</b> This field is not applicable to the <strong>createOrReplaceProductCompatibility</strong> method, as the SKU value for the inventory item is passed in as part of the call URI and not in the request payload. It is always returned with the <a href=\"/api-docs/sell/inventory/resources/inventory_item/product_compatibility/methods/getProductCompatibility\" target=\"_blank \">getProductCompatibility</a> method.</span>  # noqa: E501

        :param sku: The sku of this Compatibility.  # noqa: E501
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
        if issubclass(Compatibility, dict):
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
        if not isinstance(other, Compatibility):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
