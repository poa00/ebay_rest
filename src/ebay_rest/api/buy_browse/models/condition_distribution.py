# coding: utf-8

"""
    Browse API

    <p>The Browse API has the following resources:</p>   <ul> <li><b> item_summary: </b> Lets shoppers search for specific items by keyword, GTIN, category, charity, product, or item aspects and refine the results by using filters, such as aspects, compatibility, and fields values.</li>  <li> <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#API\" target=\"_blank\"><img src=\"/cms/img/docs/experimental-icon.svg\" class=\"legend-icon experimental-icon\" alt=\"Experimental Release\" title=\"Experimental Release\" />&nbsp;(Experimental)</a> <b> search_by_image: </b> Lets shoppers search for specific items by image. You can refine the results by using URI parameters and filters.</li>   <li><b> item: </b> <ul><li>Lets you retrieve the details of a specific item or all the items in an item group, which is an item with variations such as color and size and check if a product is compatible with the specified item, such as if a specific car is compatible with a specific part.</li> <li>Provides a bridge between the eBay legacy APIs, such as <b> Finding</b>, and the RESTful APIs, which use different formats for the item IDs.</li>  </ul> </li>  <li><a href=\"https://developer.ebay.com/api-docs/static/versioning.html#API\" target=\"_blank\"><img src=\"/cms/img/docs/experimental-icon.svg\" class=\"legend-icon experimental-icon\" alt=\"Experimental Release\" title=\"Experimental Release\" />&nbsp;(Experimental)</a> <b> shopping_cart: </b> Provides the ability for eBay members to see the contents of their eBay cart, and add, remove, and change the quantity of items in their eBay cart.&nbsp;&nbsp;<b> Note: </b> This resource is not available in the eBay API Explorer.</li></ul>       <p>The <b> item_summary</b>, <b> search_by_image</b>, and <b> item</b> resource calls require an <a href=\"/api-docs/static/oauth-client-credentials-grant.html\">Application access token</a>. The <b> shopping_cart</b> resource calls require a <a href=\"/api-docs/static/oauth-authorization-code-grant.html\">User access token</a>.</p>  # noqa: E501

    OpenAPI spec version: v1.4.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ConditionDistribution(object):
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
        'condition': 'str',
        'condition_id': 'str',
        'match_count': 'int',
        'refinement_href': 'str'
    }

    attribute_map = {
        'condition': 'condition',
        'condition_id': 'conditionId',
        'match_count': 'matchCount',
        'refinement_href': 'refinementHref'
    }

    def __init__(self, condition=None, condition_id=None, match_count=None, refinement_href=None):  # noqa: E501
        """ConditionDistribution - a model defined in Swagger"""  # noqa: E501
        self._condition = None
        self._condition_id = None
        self._match_count = None
        self._refinement_href = None
        self.discriminator = None
        if condition is not None:
            self.condition = condition
        if condition_id is not None:
            self.condition_id = condition_id
        if match_count is not None:
            self.match_count = match_count
        if refinement_href is not None:
            self.refinement_href = refinement_href

    @property
    def condition(self):
        """Gets the condition of this ConditionDistribution.  # noqa: E501

        The text describing the condition of the item, such as New or Used. For a list of condition names, see Item Condition IDs and Names. Code so that your app gracefully handles any future changes to this list. Note: In all eBay marketplaces, Condition ID 2000 now maps to an item condition of 'Certified Refurbished', and not 'Manufacturer Refurbished'. To list an item as 'Certified Refurbished', a seller must be pre-qualified by eBay for this feature.  # noqa: E501

        :return: The condition of this ConditionDistribution.  # noqa: E501
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this ConditionDistribution.

        The text describing the condition of the item, such as New or Used. For a list of condition names, see Item Condition IDs and Names. Code so that your app gracefully handles any future changes to this list. Note: In all eBay marketplaces, Condition ID 2000 now maps to an item condition of 'Certified Refurbished', and not 'Manufacturer Refurbished'. To list an item as 'Certified Refurbished', a seller must be pre-qualified by eBay for this feature.  # noqa: E501

        :param condition: The condition of this ConditionDistribution.  # noqa: E501
        :type: str
        """

        self._condition = condition

    @property
    def condition_id(self):
        """Gets the condition_id of this ConditionDistribution.  # noqa: E501

        The identifier of the condition. For example, 1000 is the identifier for NEW. Note: In all eBay marketplaces, Condition ID 2000 now maps to an item condition of 'Certified Refurbished', and not 'Manufacturer Refurbished'. To list an item as 'Certified Refurbished', a seller must be pre-qualified by eBay for this feature.  # noqa: E501

        :return: The condition_id of this ConditionDistribution.  # noqa: E501
        :rtype: str
        """
        return self._condition_id

    @condition_id.setter
    def condition_id(self, condition_id):
        """Sets the condition_id of this ConditionDistribution.

        The identifier of the condition. For example, 1000 is the identifier for NEW. Note: In all eBay marketplaces, Condition ID 2000 now maps to an item condition of 'Certified Refurbished', and not 'Manufacturer Refurbished'. To list an item as 'Certified Refurbished', a seller must be pre-qualified by eBay for this feature.  # noqa: E501

        :param condition_id: The condition_id of this ConditionDistribution.  # noqa: E501
        :type: str
        """

        self._condition_id = condition_id

    @property
    def match_count(self):
        """Gets the match_count of this ConditionDistribution.  # noqa: E501

        The number of items having the condition.  # noqa: E501

        :return: The match_count of this ConditionDistribution.  # noqa: E501
        :rtype: int
        """
        return self._match_count

    @match_count.setter
    def match_count(self, match_count):
        """Sets the match_count of this ConditionDistribution.

        The number of items having the condition.  # noqa: E501

        :param match_count: The match_count of this ConditionDistribution.  # noqa: E501
        :type: int
        """

        self._match_count = match_count

    @property
    def refinement_href(self):
        """Gets the refinement_href of this ConditionDistribution.  # noqa: E501

        The HATEOAS reference of this condition.  # noqa: E501

        :return: The refinement_href of this ConditionDistribution.  # noqa: E501
        :rtype: str
        """
        return self._refinement_href

    @refinement_href.setter
    def refinement_href(self, refinement_href):
        """Sets the refinement_href of this ConditionDistribution.

        The HATEOAS reference of this condition.  # noqa: E501

        :param refinement_href: The refinement_href of this ConditionDistribution.  # noqa: E501
        :type: str
        """

        self._refinement_href = refinement_href

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
        if issubclass(ConditionDistribution, dict):
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
        if not isinstance(other, ConditionDistribution):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other