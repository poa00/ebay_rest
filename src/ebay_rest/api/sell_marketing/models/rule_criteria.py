# coding: utf-8

"""
    Marketing API

    <p>The <i>Marketing API </i> offers two platforms that sellers can use to promote and advertise their products:</p> <ul><li><b>Promoted Listings</b> is an eBay ad service that lets sellers set up <i>ad campaigns </i> for the products they want to promote. eBay displays the ads in search results and in other marketing modules as <b>SPONSORED</b> listings. If an item in a Promoted Listings campaign sells, the seller is assessed a Promoted Listings fee, which is a seller-specified percentage applied to the sales price. For complete details, see <a href=\"/api-docs/sell/static/marketing/promoted-listings.html\">Promoted Listings</a>.</li>  <li><b>Promotions Manager</b> gives sellers a way to offer discounts on specific items as a way to attract buyers to their inventory. Sellers can set up discounts (such as \"20% off\" and other types of offers) on specific items or on an entire customer order. To further attract buyers, eBay prominently displays promotion <i>teasers</i> throughout buyer flows. For complete details, see <a href=\"/api-docs/sell/static/marketing/promotions-manager.html\">Promotions Manager</a>.</li></ul>  <p><b>Marketing reports</b>, on both the Promoted Listings and Promotions Manager platforms, give sellers information that shows the effectiveness of their marketing strategies. The data gives sellers the ability to review and fine tune their marketing efforts.</p> <p class=\"tablenote\"><b>Important!</b> Sellers must have an active eBay Store subscription, and they must accept the <b>Terms and Conditions</b> before they can make requests to these APIs in the Production environment. There are also site-specific listings requirements and restrictions associated with these marketing tools, as listed in the \"requirements and restrictions\" sections for <a href=\"/api-docs/sell/marketing/static/overview.html#PL-requirements\">Promoted Listings</a> and <a href=\"/api-docs/sell/marketing/static/overview.html#PM-requirements\">Promotions Manager</a>.</p> <p>The table below lists all the Marketing API calls grouped by resource.</p>  # noqa: E501

    OpenAPI spec version: v1.10.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class RuleCriteria(object):
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
        'exclude_inventory_items': 'list[InventoryItem]',
        'exclude_listing_ids': 'list[str]',
        'markup_inventory_items': 'list[InventoryItem]',
        'markup_listing_ids': 'list[str]',
        'selection_rules': 'list[SelectionRule]'
    }

    attribute_map = {
        'exclude_inventory_items': 'excludeInventoryItems',
        'exclude_listing_ids': 'excludeListingIds',
        'markup_inventory_items': 'markupInventoryItems',
        'markup_listing_ids': 'markupListingIds',
        'selection_rules': 'selectionRules'
    }

    def __init__(self, exclude_inventory_items=None, exclude_listing_ids=None, markup_inventory_items=None, markup_listing_ids=None, selection_rules=None):  # noqa: E501
        """RuleCriteria - a model defined in Swagger"""  # noqa: E501
        self._exclude_inventory_items = None
        self._exclude_listing_ids = None
        self._markup_inventory_items = None
        self._markup_listing_ids = None
        self._selection_rules = None
        self.discriminator = None
        if exclude_inventory_items is not None:
            self.exclude_inventory_items = exclude_inventory_items
        if exclude_listing_ids is not None:
            self.exclude_listing_ids = exclude_listing_ids
        if markup_inventory_items is not None:
            self.markup_inventory_items = markup_inventory_items
        if markup_listing_ids is not None:
            self.markup_listing_ids = markup_listing_ids
        if selection_rules is not None:
            self.selection_rules = selection_rules

    @property
    def exclude_inventory_items(self):
        """Gets the exclude_inventory_items of this RuleCriteria.  # noqa: E501

        A list of seller inventory reference IDs to exclude from the promotion.  <br><br><p class=\"tablenote\"><b>Note:</b> The request can have either <b>excludeInventoryItems</b> or <b>excludeListingIds</b> but not both.</p> <b>Maximum:</b> 100 parent items <br><b>Maximum SKU or custom label length:</b> 50 characters  # noqa: E501

        :return: The exclude_inventory_items of this RuleCriteria.  # noqa: E501
        :rtype: list[InventoryItem]
        """
        return self._exclude_inventory_items

    @exclude_inventory_items.setter
    def exclude_inventory_items(self, exclude_inventory_items):
        """Sets the exclude_inventory_items of this RuleCriteria.

        A list of seller inventory reference IDs to exclude from the promotion.  <br><br><p class=\"tablenote\"><b>Note:</b> The request can have either <b>excludeInventoryItems</b> or <b>excludeListingIds</b> but not both.</p> <b>Maximum:</b> 100 parent items <br><b>Maximum SKU or custom label length:</b> 50 characters  # noqa: E501

        :param exclude_inventory_items: The exclude_inventory_items of this RuleCriteria.  # noqa: E501
        :type: list[InventoryItem]
        """

        self._exclude_inventory_items = exclude_inventory_items

    @property
    def exclude_listing_ids(self):
        """Gets the exclude_listing_ids of this RuleCriteria.  # noqa: E501

        A list of eBay listing IDs to exclude from the promotion.  <br><br><p class=\"tablenote\"><b>Note:</b> The request can have either <b>excludeInventoryItems</b> or <b>excludeListingIds</b> but not both.</p> <b>Maximum:</b> 100 parent items <br><b>Maximum SKU or custom label length:</b> 50 characters  # noqa: E501

        :return: The exclude_listing_ids of this RuleCriteria.  # noqa: E501
        :rtype: list[str]
        """
        return self._exclude_listing_ids

    @exclude_listing_ids.setter
    def exclude_listing_ids(self, exclude_listing_ids):
        """Sets the exclude_listing_ids of this RuleCriteria.

        A list of eBay listing IDs to exclude from the promotion.  <br><br><p class=\"tablenote\"><b>Note:</b> The request can have either <b>excludeInventoryItems</b> or <b>excludeListingIds</b> but not both.</p> <b>Maximum:</b> 100 parent items <br><b>Maximum SKU or custom label length:</b> 50 characters  # noqa: E501

        :param exclude_listing_ids: The exclude_listing_ids of this RuleCriteria.  # noqa: E501
        :type: list[str]
        """

        self._exclude_listing_ids = exclude_listing_ids

    @property
    def markup_inventory_items(self):
        """Gets the markup_inventory_items of this RuleCriteria.  # noqa: E501

        A list of SKUs to remove from a markdown promotion. The listed SKUs are 'marked up' to their standard price after being part of the markdown promotion.  # noqa: E501

        :return: The markup_inventory_items of this RuleCriteria.  # noqa: E501
        :rtype: list[InventoryItem]
        """
        return self._markup_inventory_items

    @markup_inventory_items.setter
    def markup_inventory_items(self, markup_inventory_items):
        """Sets the markup_inventory_items of this RuleCriteria.

        A list of SKUs to remove from a markdown promotion. The listed SKUs are 'marked up' to their standard price after being part of the markdown promotion.  # noqa: E501

        :param markup_inventory_items: The markup_inventory_items of this RuleCriteria.  # noqa: E501
        :type: list[InventoryItem]
        """

        self._markup_inventory_items = markup_inventory_items

    @property
    def markup_listing_ids(self):
        """Gets the markup_listing_ids of this RuleCriteria.  # noqa: E501

        A list of listing IDs to remove from a markdown promotion. The listed items are 'marked up' to their standard price after being part of the markdown promotion.  # noqa: E501

        :return: The markup_listing_ids of this RuleCriteria.  # noqa: E501
        :rtype: list[str]
        """
        return self._markup_listing_ids

    @markup_listing_ids.setter
    def markup_listing_ids(self, markup_listing_ids):
        """Sets the markup_listing_ids of this RuleCriteria.

        A list of listing IDs to remove from a markdown promotion. The listed items are 'marked up' to their standard price after being part of the markdown promotion.  # noqa: E501

        :param markup_listing_ids: The markup_listing_ids of this RuleCriteria.  # noqa: E501
        :type: list[str]
        """

        self._markup_listing_ids = markup_listing_ids

    @property
    def selection_rules(self):
        """Gets the selection_rules of this RuleCriteria.  # noqa: E501

        The container for the rules that select the items to include in a promotion.  <br><br><i>Required if </i> <b>inventoryCriterionType</b> is set to <code>INVENTORY_BY_RULE</code>.  # noqa: E501

        :return: The selection_rules of this RuleCriteria.  # noqa: E501
        :rtype: list[SelectionRule]
        """
        return self._selection_rules

    @selection_rules.setter
    def selection_rules(self, selection_rules):
        """Sets the selection_rules of this RuleCriteria.

        The container for the rules that select the items to include in a promotion.  <br><br><i>Required if </i> <b>inventoryCriterionType</b> is set to <code>INVENTORY_BY_RULE</code>.  # noqa: E501

        :param selection_rules: The selection_rules of this RuleCriteria.  # noqa: E501
        :type: list[SelectionRule]
        """

        self._selection_rules = selection_rules

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
        if issubclass(RuleCriteria, dict):
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
        if not isinstance(other, RuleCriteria):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
