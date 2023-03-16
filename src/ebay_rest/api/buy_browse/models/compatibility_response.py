# coding: utf-8

"""
    Browse API

    <p>The Browse API has the following resources:</p>   <ul> <li><b> item_summary: </b> Lets shoppers search for specific items by keyword, GTIN, category, charity, product, or item aspects and refine the results by using filters, such as aspects, compatibility, and fields values.</li>  <li><b> search_by_image: </b><a href=\"https://developer.ebay.com/api-docs/static/versioning.html#experimental \" target=\"_blank\"><img src=\"/cms/img/docs/experimental-icon.svg\" class=\"legend-icon experimental-icon\" alt=\"Experimental Resource\" title=\"Experimental Resource\" />&nbsp;(Experimental Resource)</a> Lets shoppers search for specific items by image. You can refine the results by using URI parameters and filters.</li>   <li><b> item: </b> <ul><li>Lets you retrieve the details of a specific item or all the items in an item group, which is an item with variations such as color and size and check if a product is compatible with the specified item, such as if a specific car is compatible with a specific part.</li> <li>Provides a bridge between the eBay legacy APIs, such as <b> Finding</b>, and the RESTful APIs, which use different formats for the item IDs.</li>  </ul> </li>  <li> <b> shopping_cart: </b> <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#experimental \" target=\"_blank\"><img src=\"/cms/img/docs/experimental-icon.svg\" class=\"legend-icon experimental-icon\" alt=\"Experimental Resource\" title=\"Experimental Resource\" />&nbsp;(Experimental Resource)</a> <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited \" target=\"_blank\"> <img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"  alt=\"Limited Release\" />(Limited Release)</a> Provides the ability for eBay members to see the contents of their eBay cart, and add, remove, and change the quantity of items in their eBay cart.&nbsp;&nbsp;<b> Note: </b> This resource is not available in the eBay API Explorer.</li></ul>       <p>The <b> item_summary</b>, <b> search_by_image</b>, and <b> item</b> resource calls require an <a href=\"/api-docs/static/oauth-client-credentials-grant.html\">Application access token</a>. The <b> shopping_cart</b> resource calls require a <a href=\"/api-docs/static/oauth-authorization-code-grant.html\">User access token</a>.</p>  # noqa: E501

    OpenAPI spec version: v1.18.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CompatibilityResponse(object):
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
        'compatibility_status': 'str',
        'warnings': 'list[Error]'
    }

    attribute_map = {
        'compatibility_status': 'compatibilityStatus',
        'warnings': 'warnings'
    }

    def __init__(self, compatibility_status=None, warnings=None):  # noqa: E501
        """CompatibilityResponse - a model defined in Swagger"""  # noqa: E501
        self._compatibility_status = None
        self._warnings = None
        self.discriminator = None
        if compatibility_status is not None:
            self.compatibility_status = compatibility_status
        if warnings is not None:
            self.warnings = warnings

    @property
    def compatibility_status(self):
        """Gets the compatibility_status of this CompatibilityResponse.  # noqa: E501

        An enumeration value that tells you if the item is compatible with the product. <br><br>The values are: <ul>   <li>   <b> COMPATIBLE</b> - Indicates the item is compatible with the product specified in the request.</li>   <li>   <b> NOT_COMPATIBLE</b> - Indicates the item is not compatible with the product specified in the request. Be sure to check all the <b> value</b> fields to ensure they are correct as errors in the value can also cause this response.</li>   <li> <b> UNDETERMINED</b> - Indicates one or more attributes for the specified product are missing so compatibility cannot be determined.  The response returns the attributes that are missing.</li>  </ul>  Code so that your app gracefully handles any future changes to this list. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/buy/browse/types/gct:CompatibilityStatus'>eBay API documentation</a>  # noqa: E501

        :return: The compatibility_status of this CompatibilityResponse.  # noqa: E501
        :rtype: str
        """
        return self._compatibility_status

    @compatibility_status.setter
    def compatibility_status(self, compatibility_status):
        """Sets the compatibility_status of this CompatibilityResponse.

        An enumeration value that tells you if the item is compatible with the product. <br><br>The values are: <ul>   <li>   <b> COMPATIBLE</b> - Indicates the item is compatible with the product specified in the request.</li>   <li>   <b> NOT_COMPATIBLE</b> - Indicates the item is not compatible with the product specified in the request. Be sure to check all the <b> value</b> fields to ensure they are correct as errors in the value can also cause this response.</li>   <li> <b> UNDETERMINED</b> - Indicates one or more attributes for the specified product are missing so compatibility cannot be determined.  The response returns the attributes that are missing.</li>  </ul>  Code so that your app gracefully handles any future changes to this list. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/buy/browse/types/gct:CompatibilityStatus'>eBay API documentation</a>  # noqa: E501

        :param compatibility_status: The compatibility_status of this CompatibilityResponse.  # noqa: E501
        :type: str
        """

        self._compatibility_status = compatibility_status

    @property
    def warnings(self):
        """Gets the warnings of this CompatibilityResponse.  # noqa: E501

        An array of warning messages. These types of errors do not prevent the method from executing but should be checked.  # noqa: E501

        :return: The warnings of this CompatibilityResponse.  # noqa: E501
        :rtype: list[Error]
        """
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        """Sets the warnings of this CompatibilityResponse.

        An array of warning messages. These types of errors do not prevent the method from executing but should be checked.  # noqa: E501

        :param warnings: The warnings of this CompatibilityResponse.  # noqa: E501
        :type: list[Error]
        """

        self._warnings = warnings

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
        if issubclass(CompatibilityResponse, dict):
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
        if not isinstance(other, CompatibilityResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
