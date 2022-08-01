# coding: utf-8

"""
    Marketing API

    <p>The <i>Marketing API </i> offers two platforms that sellers can use to promote and advertise their products:</p> <ul><li><b>Promoted Listings</b> is an eBay ad service that lets sellers set up <i>ad campaigns </i> for the products they want to promote. eBay displays the ads in search results and in other marketing modules as <b>SPONSORED</b> listings. If an item in a Promoted Listings campaign sells, the seller is assessed a Promoted Listings fee, which is a seller-specified percentage applied to the sales price. For complete details, refer to the <a href=\"/api-docs/sell/static/marketing/pl-landing.html\">Promoted Listings playbook</a>.</li><li><b>Promotions Manager</b> gives sellers a way to offer discounts on specific items as a way to attract buyers to their inventory. Sellers can set up discounts (such as \"20% off\" and other types of offers) on specific items or on an entire customer order. To further attract buyers, eBay prominently displays promotion <i>teasers</i> throughout buyer flows. For complete details, see <a href=\"/api-docs/sell/static/marketing/promotions-manager.html\">Promotions Manager</a>.</li></ul>  <p><b>Marketing reports</b>, on both the Promoted Listings and Promotions Manager platforms, give sellers information that shows the effectiveness of their marketing strategies. The data gives sellers the ability to review and fine tune their marketing efforts.</p> <p class=\"tablenote\"><b>Important!</b> Sellers must have an active eBay Store subscription, and they must accept the <b>Terms and Conditions</b> before they can make requests to these APIs in the Production environment. There are also site-specific listings requirements and restrictions associated with these marketing tools, as listed in the \"requirements and restrictions\" sections for <a href=\"/api-docs/sell/marketing/static/overview.html#PL-requirements\">Promoted Listings</a> and <a href=\"/api-docs/sell/marketing/static/overview.html#PM-requirements\">Promotions Manager</a>.</p> <p>The table below lists all the Marketing API calls grouped by resource.</p>  # noqa: E501

    OpenAPI spec version: v1.13.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CampaignCriterion(object):
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
        'auto_select_future_inventory': 'bool',
        'criterion_type': 'str',
        'selection_rules': 'list[SelectionRule]'
    }

    attribute_map = {
        'auto_select_future_inventory': 'autoSelectFutureInventory',
        'criterion_type': 'criterionType',
        'selection_rules': 'selectionRules'
    }

    def __init__(self, auto_select_future_inventory=None, criterion_type=None, selection_rules=None):  # noqa: E501
        """CampaignCriterion - a model defined in Swagger"""  # noqa: E501
        self._auto_select_future_inventory = None
        self._criterion_type = None
        self._selection_rules = None
        self.discriminator = None
        if auto_select_future_inventory is not None:
            self.auto_select_future_inventory = auto_select_future_inventory
        if criterion_type is not None:
            self.criterion_type = criterion_type
        if selection_rules is not None:
            self.selection_rules = selection_rules

    @property
    def auto_select_future_inventory(self):
        """Gets the auto_select_future_inventory of this CampaignCriterion.  # noqa: E501

        A field used to indicate whether listings shall be automatically added to, or removed from, a Promoted Listings campaign based on the rules that have been configured for the campaign.<br /><br />If set to <code>true</code>, eBay adds all listings matching the campaign criterion to the campaign, including any new listings created from the items in a seller's inventory.<br /><br /><b>Default:</b> <code>false</code>  # noqa: E501

        :return: The auto_select_future_inventory of this CampaignCriterion.  # noqa: E501
        :rtype: bool
        """
        return self._auto_select_future_inventory

    @auto_select_future_inventory.setter
    def auto_select_future_inventory(self, auto_select_future_inventory):
        """Sets the auto_select_future_inventory of this CampaignCriterion.

        A field used to indicate whether listings shall be automatically added to, or removed from, a Promoted Listings campaign based on the rules that have been configured for the campaign.<br /><br />If set to <code>true</code>, eBay adds all listings matching the campaign criterion to the campaign, including any new listings created from the items in a seller's inventory.<br /><br /><b>Default:</b> <code>false</code>  # noqa: E501

        :param auto_select_future_inventory: The auto_select_future_inventory of this CampaignCriterion.  # noqa: E501
        :type: bool
        """

        self._auto_select_future_inventory = auto_select_future_inventory

    @property
    def criterion_type(self):
        """Gets the criterion_type of this CampaignCriterion.  # noqa: E501

        This enum defines the criterion (selection rule) types. Currently, the only criterion type supported is <code>INVENTORY_PARTITION</code>, and you must specify this value if you manage your items with the Inventory API and you want to include items based on their inventory reference IDs.  <br><br>Do not include this field if you manage your listings with Trading API/legacy model. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/pls:CriterionTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The criterion_type of this CampaignCriterion.  # noqa: E501
        :rtype: str
        """
        return self._criterion_type

    @criterion_type.setter
    def criterion_type(self, criterion_type):
        """Sets the criterion_type of this CampaignCriterion.

        This enum defines the criterion (selection rule) types. Currently, the only criterion type supported is <code>INVENTORY_PARTITION</code>, and you must specify this value if you manage your items with the Inventory API and you want to include items based on their inventory reference IDs.  <br><br>Do not include this field if you manage your listings with Trading API/legacy model. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/pls:CriterionTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param criterion_type: The criterion_type of this CampaignCriterion.  # noqa: E501
        :type: str
        """

        self._criterion_type = criterion_type

    @property
    def selection_rules(self):
        """Gets the selection_rules of this CampaignCriterion.  # noqa: E501

        This container shows all of the rules/inclusion filters used to add listings to the campaign.  # noqa: E501

        :return: The selection_rules of this CampaignCriterion.  # noqa: E501
        :rtype: list[SelectionRule]
        """
        return self._selection_rules

    @selection_rules.setter
    def selection_rules(self, selection_rules):
        """Sets the selection_rules of this CampaignCriterion.

        This container shows all of the rules/inclusion filters used to add listings to the campaign.  # noqa: E501

        :param selection_rules: The selection_rules of this CampaignCriterion.  # noqa: E501
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
        if issubclass(CampaignCriterion, dict):
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
        if not isinstance(other, CampaignCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
