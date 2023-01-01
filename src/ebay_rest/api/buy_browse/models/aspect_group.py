# coding: utf-8

"""
    Browse API

    <p>The Browse API has the following resources:</p>   <ul> <li><b> item_summary: </b> Lets shoppers search for specific items by keyword, GTIN, category, charity, product, or item aspects and refine the results by using filters, such as aspects, compatibility, and fields values.</li>  <li><b> search_by_image: </b><a href=\"https://developer.ebay.com/api-docs/static/versioning.html#experimental \" target=\"_blank\"><img src=\"/cms/img/docs/experimental-icon.svg\" class=\"legend-icon experimental-icon\" alt=\"Experimental Resource\" title=\"Experimental Resource\" />&nbsp;(Experimental Resource)</a> Lets shoppers search for specific items by image. You can refine the results by using URI parameters and filters.</li>   <li><b> item: </b> <ul><li>Lets you retrieve the details of a specific item or all the items in an item group, which is an item with variations such as color and size and check if a product is compatible with the specified item, such as if a specific car is compatible with a specific part.</li> <li>Provides a bridge between the eBay legacy APIs, such as <b> Finding</b>, and the RESTful APIs, which use different formats for the item IDs.</li>  </ul> </li>  <li> <b> shopping_cart: </b> <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#experimental \" target=\"_blank\"><img src=\"/cms/img/docs/experimental-icon.svg\" class=\"legend-icon experimental-icon\" alt=\"Experimental Resource\" title=\"Experimental Resource\" />&nbsp;(Experimental Resource)</a> <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited \" target=\"_blank\"> <img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"  alt=\"Limited Release\" />(Limited Release)</a> Provides the ability for eBay members to see the contents of their eBay cart, and add, remove, and change the quantity of items in their eBay cart.&nbsp;&nbsp;<b> Note: </b> This resource is not available in the eBay API Explorer.</li></ul>       <p>The <b> item_summary</b>, <b> search_by_image</b>, and <b> item</b> resource calls require an <a href=\"/api-docs/static/oauth-client-credentials-grant.html\">Application access token</a>. The <b> shopping_cart</b> resource calls require a <a href=\"/api-docs/static/oauth-authorization-code-grant.html\">User access token</a>.</p>  # noqa: E501

    OpenAPI spec version: v1.18.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AspectGroup(object):
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
        'aspects': 'list[Aspect]',
        'localized_group_name': 'str'
    }

    attribute_map = {
        'aspects': 'aspects',
        'localized_group_name': 'localizedGroupName'
    }

    def __init__(self, aspects=None, localized_group_name=None):  # noqa: E501
        """AspectGroup - a model defined in Swagger"""  # noqa: E501
        self._aspects = None
        self._localized_group_name = None
        self.discriminator = None
        if aspects is not None:
            self.aspects = aspects
        if localized_group_name is not None:
            self.localized_group_name = localized_group_name

    @property
    def aspects(self):
        """Gets the aspects of this AspectGroup.  # noqa: E501

        An array of the name/value pairs for the aspects of the product. For example: BRAND/Apple  # noqa: E501

        :return: The aspects of this AspectGroup.  # noqa: E501
        :rtype: list[Aspect]
        """
        return self._aspects

    @aspects.setter
    def aspects(self, aspects):
        """Sets the aspects of this AspectGroup.

        An array of the name/value pairs for the aspects of the product. For example: BRAND/Apple  # noqa: E501

        :param aspects: The aspects of this AspectGroup.  # noqa: E501
        :type: list[Aspect]
        """

        self._aspects = aspects

    @property
    def localized_group_name(self):
        """Gets the localized_group_name of this AspectGroup.  # noqa: E501

        The name of a group of aspects. <br /><br />In the following example, <b> Product Identifiers</b> and <b> Process</b> are product aspect group names. Under the group name are the product aspect name/value pairs. <p><b> Product Identifiers</b> <br />&nbsp;&nbsp;&nbsp;Brand/Apple <br />&nbsp;&nbsp;&nbsp;Product Family/iMac</p> <p><b> Processor</b><br />&nbsp;&nbsp;&nbsp;Processor Type/Intel <br />&nbsp;&nbsp;&nbsp;Processor Speed/3.10</p>   # noqa: E501

        :return: The localized_group_name of this AspectGroup.  # noqa: E501
        :rtype: str
        """
        return self._localized_group_name

    @localized_group_name.setter
    def localized_group_name(self, localized_group_name):
        """Sets the localized_group_name of this AspectGroup.

        The name of a group of aspects. <br /><br />In the following example, <b> Product Identifiers</b> and <b> Process</b> are product aspect group names. Under the group name are the product aspect name/value pairs. <p><b> Product Identifiers</b> <br />&nbsp;&nbsp;&nbsp;Brand/Apple <br />&nbsp;&nbsp;&nbsp;Product Family/iMac</p> <p><b> Processor</b><br />&nbsp;&nbsp;&nbsp;Processor Type/Intel <br />&nbsp;&nbsp;&nbsp;Processor Speed/3.10</p>   # noqa: E501

        :param localized_group_name: The localized_group_name of this AspectGroup.  # noqa: E501
        :type: str
        """

        self._localized_group_name = localized_group_name

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
        if issubclass(AspectGroup, dict):
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
        if not isinstance(other, AspectGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
