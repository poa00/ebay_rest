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

class VariesBy(object):
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
        'aspects_image_varies_by': 'list[str]',
        'specifications': 'list[Specification]'
    }

    attribute_map = {
        'aspects_image_varies_by': 'aspectsImageVariesBy',
        'specifications': 'specifications'
    }

    def __init__(self, aspects_image_varies_by=None, specifications=None):  # noqa: E501
        """VariesBy - a model defined in Swagger"""  # noqa: E501
        self._aspects_image_varies_by = None
        self._specifications = None
        self.discriminator = None
        if aspects_image_varies_by is not None:
            self.aspects_image_varies_by = aspects_image_varies_by
        if specifications is not None:
            self.specifications = specifications

    @property
    def aspects_image_varies_by(self):
        """Gets the aspects_image_varies_by of this VariesBy.  # noqa: E501

        This container is used if the seller wants to include multiple images to demonstrate how variations within a multiple-variation listing differ. In this string field, the seller will specify the product aspect where the variations of the inventory item group vary, such as color. If <code>Color</code> is specified in this field, <code>Color</code> must also be one of the <strong>specifications.name</strong> values, and all available colors must appear in the corresponding <strong>specifications.values</strong> array.<br><br>If the <strong>aspectsImageVariesBy</strong> container is used, links to images of each variation should be specified through the <strong>imageUrls</strong> container of the inventory item group, or the seller can choose to include those links to images in each inventory item record for the inventory items in the group.  # noqa: E501

        :return: The aspects_image_varies_by of this VariesBy.  # noqa: E501
        :rtype: list[str]
        """
        return self._aspects_image_varies_by

    @aspects_image_varies_by.setter
    def aspects_image_varies_by(self, aspects_image_varies_by):
        """Sets the aspects_image_varies_by of this VariesBy.

        This container is used if the seller wants to include multiple images to demonstrate how variations within a multiple-variation listing differ. In this string field, the seller will specify the product aspect where the variations of the inventory item group vary, such as color. If <code>Color</code> is specified in this field, <code>Color</code> must also be one of the <strong>specifications.name</strong> values, and all available colors must appear in the corresponding <strong>specifications.values</strong> array.<br><br>If the <strong>aspectsImageVariesBy</strong> container is used, links to images of each variation should be specified through the <strong>imageUrls</strong> container of the inventory item group, or the seller can choose to include those links to images in each inventory item record for the inventory items in the group.  # noqa: E501

        :param aspects_image_varies_by: The aspects_image_varies_by of this VariesBy.  # noqa: E501
        :type: list[str]
        """

        self._aspects_image_varies_by = aspects_image_varies_by

    @property
    def specifications(self):
        """Gets the specifications of this VariesBy.  # noqa: E501

        This container consists of an array of one or more product aspects where each variation differs, and values for each of those product aspects. This container is not immediately required, but will be required before the first offer of the inventory item group is published. <br><br>If a product aspect is specified in the <strong>aspectsImageVariesBy</strong> container, this product aspect (along with all variations of that product aspect) must be included in the <strong>specifications</strong> container. Before offers related to the inventory item group are published, the product aspects and values specified through the <strong>specifications</strong> container should be in synch with the name-value pairs specified through the <strong>product.aspects</strong> containers of the inventory items contained in the group. For example, if <code>Color</code> and <code>Size</code> are in this <strong>specifications</strong> container, each inventory item of the group should also have <code>Color</code> and <code>Size</code> as aspect names in their inventory item records.<br><br>This container is always returned if one or more offers associated with the inventory item group have been published. For inventory item groups that have yet to have any published offers, this container is only returned if set.  # noqa: E501

        :return: The specifications of this VariesBy.  # noqa: E501
        :rtype: list[Specification]
        """
        return self._specifications

    @specifications.setter
    def specifications(self, specifications):
        """Sets the specifications of this VariesBy.

        This container consists of an array of one or more product aspects where each variation differs, and values for each of those product aspects. This container is not immediately required, but will be required before the first offer of the inventory item group is published. <br><br>If a product aspect is specified in the <strong>aspectsImageVariesBy</strong> container, this product aspect (along with all variations of that product aspect) must be included in the <strong>specifications</strong> container. Before offers related to the inventory item group are published, the product aspects and values specified through the <strong>specifications</strong> container should be in synch with the name-value pairs specified through the <strong>product.aspects</strong> containers of the inventory items contained in the group. For example, if <code>Color</code> and <code>Size</code> are in this <strong>specifications</strong> container, each inventory item of the group should also have <code>Color</code> and <code>Size</code> as aspect names in their inventory item records.<br><br>This container is always returned if one or more offers associated with the inventory item group have been published. For inventory item groups that have yet to have any published offers, this container is only returned if set.  # noqa: E501

        :param specifications: The specifications of this VariesBy.  # noqa: E501
        :type: list[Specification]
        """

        self._specifications = specifications

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
        if issubclass(VariesBy, dict):
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
        if not isinstance(other, VariesBy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
