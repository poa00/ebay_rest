# coding: utf-8

"""
    Marketing API

    <p>The <i>Marketing API </i> offers two platforms that sellers can use to promote and advertise their products:</p> <ul><li><b>Promoted Listings</b> is an eBay ad service that lets sellers set up <i>ad campaigns </i> for the products they want to promote. eBay displays the ads in search results and in other marketing modules as <b>SPONSORED</b> listings. If an item in a Promoted Listings campaign sells, the seller is assessed a Promoted Listings fee, which is a seller-specified percentage applied to the sales price. For complete details, refer to the <a href=\"/api-docs/sell/static/marketing/pl-landing.html\">Promoted Listings playbook</a>.</li><li><b>Promotions Manager</b> gives sellers a way to offer discounts on specific items as a way to attract buyers to their inventory. Sellers can set up discounts (such as \"20% off\" and other types of offers) on specific items or on an entire customer order. To further attract buyers, eBay prominently displays promotion <i>teasers</i> throughout buyer flows. For complete details, see <a href=\"/api-docs/sell/static/marketing/promotions-manager.html\">Promotions Manager</a>.</li></ul>  <p><b>Marketing reports</b>, on both the Promoted Listings and Promotions Manager platforms, give sellers information that shows the effectiveness of their marketing strategies. The data gives sellers the ability to review and fine tune their marketing efforts.</p><p><b>Store Email Campaign</b> allows sellers to create and send email campaigns to customers who have signed up to receive their newsletter. For more information on email campaigns, see <a href=\"/api-docs/sell/static/marketing/store-email-campaigns.html#email-campain-types\" target=\"_blank\">Store Email Campaigns</a>.<p class=\"tablenote\"><b>Important!</b> Sellers must have an active eBay Store subscription, and they must accept the <b>Terms and Conditions</b> before they can make requests to these APIs in the Production environment. There are also site-specific listings requirements and restrictions associated with these marketing tools, as listed in the \"requirements and restrictions\" sections for <a href=\"/api-docs/sell/marketing/static/overview.html#PL-requirements\">Promoted Listings</a> and <a href=\"/api-docs/sell/marketing/static/overview.html#PM-requirements\">Promotions Manager</a>.</p> <p>The table below lists all the Marketing API calls grouped by resource.</p>  # noqa: E501

    OpenAPI spec version: v1.18.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Ad(object):
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
        'ad_group_id': 'str',
        'ad_id': 'str',
        'ad_status': 'str',
        'alerts': 'list[Alert]',
        'bid_percentage': 'str',
        'inventory_reference_id': 'str',
        'inventory_reference_type': 'str',
        'listing_id': 'str'
    }

    attribute_map = {
        'ad_group_id': 'adGroupId',
        'ad_id': 'adId',
        'ad_status': 'adStatus',
        'alerts': 'alerts',
        'bid_percentage': 'bidPercentage',
        'inventory_reference_id': 'inventoryReferenceId',
        'inventory_reference_type': 'inventoryReferenceType',
        'listing_id': 'listingId'
    }

    def __init__(self, ad_group_id=None, ad_id=None, ad_status=None, alerts=None, bid_percentage=None, inventory_reference_id=None, inventory_reference_type=None, listing_id=None):  # noqa: E501
        """Ad - a model defined in Swagger"""  # noqa: E501
        self._ad_group_id = None
        self._ad_id = None
        self._ad_status = None
        self._alerts = None
        self._bid_percentage = None
        self._inventory_reference_id = None
        self._inventory_reference_type = None
        self._listing_id = None
        self.discriminator = None
        if ad_group_id is not None:
            self.ad_group_id = ad_group_id
        if ad_id is not None:
            self.ad_id = ad_id
        if ad_status is not None:
            self.ad_status = ad_status
        if alerts is not None:
            self.alerts = alerts
        if bid_percentage is not None:
            self.bid_percentage = bid_percentage
        if inventory_reference_id is not None:
            self.inventory_reference_id = inventory_reference_id
        if inventory_reference_type is not None:
            self.inventory_reference_type = inventory_reference_type
        if listing_id is not None:
            self.listing_id = listing_id

    @property
    def ad_group_id(self):
        """Gets the ad_group_id of this Ad.  # noqa: E501

        A unique eBay-assigned ID for an ad group in a campaign that uses the Cost Per Click (CPC) funding model. This ID is created after a successful <a href=\"/api-docs/sell/marketing/resources/adgroup/methods/createAdGroup\">createAdGroup</a> call, and all ad groups must be associated with a CPC campaign.  # noqa: E501

        :return: The ad_group_id of this Ad.  # noqa: E501
        :rtype: str
        """
        return self._ad_group_id

    @ad_group_id.setter
    def ad_group_id(self, ad_group_id):
        """Sets the ad_group_id of this Ad.

        A unique eBay-assigned ID for an ad group in a campaign that uses the Cost Per Click (CPC) funding model. This ID is created after a successful <a href=\"/api-docs/sell/marketing/resources/adgroup/methods/createAdGroup\">createAdGroup</a> call, and all ad groups must be associated with a CPC campaign.  # noqa: E501

        :param ad_group_id: The ad_group_id of this Ad.  # noqa: E501
        :type: str
        """

        self._ad_group_id = ad_group_id

    @property
    def ad_id(self):
        """Gets the ad_id of this Ad.  # noqa: E501

        A unique eBay-assigned ID that is generated when the ad is created.  # noqa: E501

        :return: The ad_id of this Ad.  # noqa: E501
        :rtype: str
        """
        return self._ad_id

    @ad_id.setter
    def ad_id(self, ad_id):
        """Sets the ad_id of this Ad.

        A unique eBay-assigned ID that is generated when the ad is created.  # noqa: E501

        :param ad_id: The ad_id of this Ad.  # noqa: E501
        :type: str
        """

        self._ad_id = ad_id

    @property
    def ad_status(self):
        """Gets the ad_status of this Ad.  # noqa: E501

        The current status of the CPC ad.<br /><br /><b>Valid Values:</b><ul><li><code>ACTIVE</code></li><li><code>PAUSED</code></li><li><code>ARCHIVED</code></li></ul><span class=\"tablenote\"><b>Note:</b> This type only applies to the Cost Per Click (CPC) funding model; it does not apply to the Cost Per Sale (CPS) funding model.</span> For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/pls:AdStatusEnum'>eBay API documentation</a>  # noqa: E501

        :return: The ad_status of this Ad.  # noqa: E501
        :rtype: str
        """
        return self._ad_status

    @ad_status.setter
    def ad_status(self, ad_status):
        """Sets the ad_status of this Ad.

        The current status of the CPC ad.<br /><br /><b>Valid Values:</b><ul><li><code>ACTIVE</code></li><li><code>PAUSED</code></li><li><code>ARCHIVED</code></li></ul><span class=\"tablenote\"><b>Note:</b> This type only applies to the Cost Per Click (CPC) funding model; it does not apply to the Cost Per Sale (CPS) funding model.</span> For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/pls:AdStatusEnum'>eBay API documentation</a>  # noqa: E501

        :param ad_status: The ad_status of this Ad.  # noqa: E501
        :type: str
        """

        self._ad_status = ad_status

    @property
    def alerts(self):
        """Gets the alerts of this Ad.  # noqa: E501

        An array containing alert messages for the ad.  # noqa: E501

        :return: The alerts of this Ad.  # noqa: E501
        :rtype: list[Alert]
        """
        return self._alerts

    @alerts.setter
    def alerts(self, alerts):
        """Sets the alerts of this Ad.

        An array containing alert messages for the ad.  # noqa: E501

        :param alerts: The alerts of this Ad.  # noqa: E501
        :type: list[Alert]
        """

        self._alerts = alerts

    @property
    def bid_percentage(self):
        """Gets the bid_percentage of this Ad.  # noqa: E501

        The user-defined <b>bid percentage</b> (also known as the <i>ad rate</i>) sets the level that eBay increases the visibility in search results for the associated listing. The higher the <b>bidPercentage</b> value, the more eBay promotes the listing.  <br><br>The value specified here is also used to calculate the Promoted Listings fee. This percentage value is multiplied by the final sales price to determine the fee. <br><br>The Promoted Listings fee is determined at the time the transaction completes and the seller is assessed the fee only when an item sells through a Promoted Listings ad campaign. <br><br>The <b>bidPercentage</b> is a single precision value that is guided by the following rules: <ul><li>These values are <b>valid</b>:<br>&nbsp;&nbsp;&nbsp;<code>4.1</code>, &nbsp;&nbsp;&nbsp;<code>5.0</code>, &nbsp;&nbsp;&nbsp;<code>5.5</code>, ...</li>  <li>These values are <b>not valid</b>:<br /> &nbsp;&nbsp;&nbsp;<code>0.01</code>, &nbsp;&nbsp;&nbsp;<code>10.75</code>, &nbsp;&nbsp;&nbsp;<code>99.99</code>,<br /> &nbsp;&nbsp;&nbsp;and so on.</li></ul>This is default bid percentage for the campaigns using the Cost Per Sale (CPS) funding model, and this value will be overridden by any ads in the campaign that have their own set bid percentages.<br /><br />If a bid percentage is not provided for an ad, eBay uses the default bid percentage of the associated campaign.<br /><br /><span class=\"tablenote\"><b>Note:</b>This field will always be returned for campaigns that use the Cost Per Sale (CPS) funding model. It will not be returned for campaigns that use the Cost Per Click (CPC) funding model.</span><br /><b>Minimum value:</b> 2.0 <br><b>Maximum value:</b> 100.0  # noqa: E501

        :return: The bid_percentage of this Ad.  # noqa: E501
        :rtype: str
        """
        return self._bid_percentage

    @bid_percentage.setter
    def bid_percentage(self, bid_percentage):
        """Sets the bid_percentage of this Ad.

        The user-defined <b>bid percentage</b> (also known as the <i>ad rate</i>) sets the level that eBay increases the visibility in search results for the associated listing. The higher the <b>bidPercentage</b> value, the more eBay promotes the listing.  <br><br>The value specified here is also used to calculate the Promoted Listings fee. This percentage value is multiplied by the final sales price to determine the fee. <br><br>The Promoted Listings fee is determined at the time the transaction completes and the seller is assessed the fee only when an item sells through a Promoted Listings ad campaign. <br><br>The <b>bidPercentage</b> is a single precision value that is guided by the following rules: <ul><li>These values are <b>valid</b>:<br>&nbsp;&nbsp;&nbsp;<code>4.1</code>, &nbsp;&nbsp;&nbsp;<code>5.0</code>, &nbsp;&nbsp;&nbsp;<code>5.5</code>, ...</li>  <li>These values are <b>not valid</b>:<br /> &nbsp;&nbsp;&nbsp;<code>0.01</code>, &nbsp;&nbsp;&nbsp;<code>10.75</code>, &nbsp;&nbsp;&nbsp;<code>99.99</code>,<br /> &nbsp;&nbsp;&nbsp;and so on.</li></ul>This is default bid percentage for the campaigns using the Cost Per Sale (CPS) funding model, and this value will be overridden by any ads in the campaign that have their own set bid percentages.<br /><br />If a bid percentage is not provided for an ad, eBay uses the default bid percentage of the associated campaign.<br /><br /><span class=\"tablenote\"><b>Note:</b>This field will always be returned for campaigns that use the Cost Per Sale (CPS) funding model. It will not be returned for campaigns that use the Cost Per Click (CPC) funding model.</span><br /><b>Minimum value:</b> 2.0 <br><b>Maximum value:</b> 100.0  # noqa: E501

        :param bid_percentage: The bid_percentage of this Ad.  # noqa: E501
        :type: str
        """

        self._bid_percentage = bid_percentage

    @property
    def inventory_reference_id(self):
        """Gets the inventory_reference_id of this Ad.  # noqa: E501

        An ID that identifies a single-item listing or multiple-variation listing that is managed with the <a href=\"/api-docs/sell/inventory/resources/methods\" title=\"Inventory API Reference\">Inventory API</a>. <p>The <i>inventory reference ID</i> is a seller-defined value that can be either an <b>SKU</b> for a single-item listing or an <b>inventoryItemGroupKey</b> for a multiple-value listing.</p>  <p>An <i>inventoryItemGroupKey</i> is a value that the seller defines to indicate a listing that's the parent of an inventory item group (a multiple-variation listing, such as a listing for a shirt that's available in multiple sizes and colors).</p><p>This field is only returned if the ad is associated with a SKU or an inventory item group value.</p>  # noqa: E501

        :return: The inventory_reference_id of this Ad.  # noqa: E501
        :rtype: str
        """
        return self._inventory_reference_id

    @inventory_reference_id.setter
    def inventory_reference_id(self, inventory_reference_id):
        """Sets the inventory_reference_id of this Ad.

        An ID that identifies a single-item listing or multiple-variation listing that is managed with the <a href=\"/api-docs/sell/inventory/resources/methods\" title=\"Inventory API Reference\">Inventory API</a>. <p>The <i>inventory reference ID</i> is a seller-defined value that can be either an <b>SKU</b> for a single-item listing or an <b>inventoryItemGroupKey</b> for a multiple-value listing.</p>  <p>An <i>inventoryItemGroupKey</i> is a value that the seller defines to indicate a listing that's the parent of an inventory item group (a multiple-variation listing, such as a listing for a shirt that's available in multiple sizes and colors).</p><p>This field is only returned if the ad is associated with a SKU or an inventory item group value.</p>  # noqa: E501

        :param inventory_reference_id: The inventory_reference_id of this Ad.  # noqa: E501
        :type: str
        """

        self._inventory_reference_id = inventory_reference_id

    @property
    def inventory_reference_type(self):
        """Gets the inventory_reference_type of this Ad.  # noqa: E501

        The enumeration value returned here indicates the type of listing the inventoryReferenceId references. The value returned here will be <code>INVENTORY_ITEM</code> for a single-variation listing, or <code>INVENTORY_ITEM_GROUP</code> for a multiple-variation listing. <p>This field is only returned if the ad is associated with a SKU or an inventory item group value.</p> For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/pls:InventoryReferenceTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The inventory_reference_type of this Ad.  # noqa: E501
        :rtype: str
        """
        return self._inventory_reference_type

    @inventory_reference_type.setter
    def inventory_reference_type(self, inventory_reference_type):
        """Sets the inventory_reference_type of this Ad.

        The enumeration value returned here indicates the type of listing the inventoryReferenceId references. The value returned here will be <code>INVENTORY_ITEM</code> for a single-variation listing, or <code>INVENTORY_ITEM_GROUP</code> for a multiple-variation listing. <p>This field is only returned if the ad is associated with a SKU or an inventory item group value.</p> For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/pls:InventoryReferenceTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param inventory_reference_type: The inventory_reference_type of this Ad.  # noqa: E501
        :type: str
        """

        self._inventory_reference_type = inventory_reference_type

    @property
    def listing_id(self):
        """Gets the listing_id of this Ad.  # noqa: E501

        A unique eBay-assigned ID that is generated when a listing is created.  # noqa: E501

        :return: The listing_id of this Ad.  # noqa: E501
        :rtype: str
        """
        return self._listing_id

    @listing_id.setter
    def listing_id(self, listing_id):
        """Sets the listing_id of this Ad.

        A unique eBay-assigned ID that is generated when a listing is created.  # noqa: E501

        :param listing_id: The listing_id of this Ad.  # noqa: E501
        :type: str
        """

        self._listing_id = listing_id

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
        if issubclass(Ad, dict):
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
        if not isinstance(other, Ad):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
