# coding: utf-8

"""
    Marketing API

    <p>The <i>Marketing API </i> offers two platforms that sellers can use to promote and advertise their products:</p> <ul><li><b>Promoted Listings</b> is an eBay ad service that lets sellers set up <i>ad campaigns </i> for the products they want to promote. eBay displays the ads in search results and in other marketing modules as <b>SPONSORED</b> listings. If an item in a Promoted Listings campaign sells, the seller is assessed a Promoted Listings fee, which is a seller-specified percentage applied to the sales price. For complete details, refer to the <a href=\"/api-docs/sell/static/marketing/pl-landing.html\">Promoted Listings playbook</a>.</li><li><b>Promotions Manager</b> gives sellers a way to offer discounts on specific items as a way to attract buyers to their inventory. Sellers can set up discounts (such as \"20% off\" and other types of offers) on specific items or on an entire customer order. To further attract buyers, eBay prominently displays promotion <i>teasers</i> throughout buyer flows. For complete details, see <a href=\"/api-docs/sell/static/marketing/promotions-manager.html\">Promotions Manager</a>.</li></ul>  <p><b>Marketing reports</b>, on both the Promoted Listings and Promotions Manager platforms, give sellers information that shows the effectiveness of their marketing strategies. The data gives sellers the ability to review and fine tune their marketing efforts.</p> <p class=\"tablenote\"><b>Important!</b> Sellers must have an active eBay Store subscription, and they must accept the <b>Terms and Conditions</b> before they can make requests to these APIs in the Production environment. There are also site-specific listings requirements and restrictions associated with these marketing tools, as listed in the \"requirements and restrictions\" sections for <a href=\"/api-docs/sell/marketing/static/overview.html#PL-requirements\">Promoted Listings</a> and <a href=\"/api-docs/sell/marketing/static/overview.html#PM-requirements\">Promotions Manager</a>.</p> <p>The table below lists all the Marketing API calls grouped by resource.</p>  # noqa: E501

    OpenAPI spec version: v1.14.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ItemPromotion(object):
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
        'apply_discount_to_single_item_only': 'bool',
        'budget': 'Amount',
        'coupon_configuration': 'CouponConfiguration',
        'description': 'str',
        'discount_rules': 'list[DiscountRule]',
        'end_date': 'str',
        'inventory_criterion': 'InventoryCriterion',
        'marketplace_id': 'str',
        'name': 'str',
        'priority': 'str',
        'promotion_image_url': 'str',
        'promotion_status': 'str',
        'promotion_type': 'str',
        'start_date': 'str'
    }

    attribute_map = {
        'apply_discount_to_single_item_only': 'applyDiscountToSingleItemOnly',
        'budget': 'budget',
        'coupon_configuration': 'couponConfiguration',
        'description': 'description',
        'discount_rules': 'discountRules',
        'end_date': 'endDate',
        'inventory_criterion': 'inventoryCriterion',
        'marketplace_id': 'marketplaceId',
        'name': 'name',
        'priority': 'priority',
        'promotion_image_url': 'promotionImageUrl',
        'promotion_status': 'promotionStatus',
        'promotion_type': 'promotionType',
        'start_date': 'startDate'
    }

    def __init__(self, apply_discount_to_single_item_only=None, budget=None, coupon_configuration=None, description=None, discount_rules=None, end_date=None, inventory_criterion=None, marketplace_id=None, name=None, priority=None, promotion_image_url=None, promotion_status=None, promotion_type=None, start_date=None):  # noqa: E501
        """ItemPromotion - a model defined in Swagger"""  # noqa: E501
        self._apply_discount_to_single_item_only = None
        self._budget = None
        self._coupon_configuration = None
        self._description = None
        self._discount_rules = None
        self._end_date = None
        self._inventory_criterion = None
        self._marketplace_id = None
        self._name = None
        self._priority = None
        self._promotion_image_url = None
        self._promotion_status = None
        self._promotion_type = None
        self._start_date = None
        self.discriminator = None
        if apply_discount_to_single_item_only is not None:
            self.apply_discount_to_single_item_only = apply_discount_to_single_item_only
        if budget is not None:
            self.budget = budget
        if coupon_configuration is not None:
            self.coupon_configuration = coupon_configuration
        if description is not None:
            self.description = description
        if discount_rules is not None:
            self.discount_rules = discount_rules
        if end_date is not None:
            self.end_date = end_date
        if inventory_criterion is not None:
            self.inventory_criterion = inventory_criterion
        if marketplace_id is not None:
            self.marketplace_id = marketplace_id
        if name is not None:
            self.name = name
        if priority is not None:
            self.priority = priority
        if promotion_image_url is not None:
            self.promotion_image_url = promotion_image_url
        if promotion_status is not None:
            self.promotion_status = promotion_status
        if promotion_type is not None:
            self.promotion_type = promotion_type
        if start_date is not None:
            self.start_date = start_date

    @property
    def apply_discount_to_single_item_only(self):
        """Gets the apply_discount_to_single_item_only of this ItemPromotion.  # noqa: E501

        This flag is relevant in only when <b>promotionType</b> is set to <code>VOLUME_DISCOUNT</code>. For details on volume pricing promotions, see <a href=\"/api-docs/sell/static/marketing/pm-volume-discounts.html\">Configuring volume pricing discounts</a>.  <br><br>If set to <code>true</code>, the discount is applied only when the buyer purchases multiple quantities of a single item in the promotion. Otherwise, the promotional discount applies to multiple quantities of any items in the promotion. Different variations of a multi-variation item are considered to be the same item. Note that this flag is not relevant if the <b>inventoryCriterion</b> container identifies a single listing ID for the promotion.  # noqa: E501

        :return: The apply_discount_to_single_item_only of this ItemPromotion.  # noqa: E501
        :rtype: bool
        """
        return self._apply_discount_to_single_item_only

    @apply_discount_to_single_item_only.setter
    def apply_discount_to_single_item_only(self, apply_discount_to_single_item_only):
        """Sets the apply_discount_to_single_item_only of this ItemPromotion.

        This flag is relevant in only when <b>promotionType</b> is set to <code>VOLUME_DISCOUNT</code>. For details on volume pricing promotions, see <a href=\"/api-docs/sell/static/marketing/pm-volume-discounts.html\">Configuring volume pricing discounts</a>.  <br><br>If set to <code>true</code>, the discount is applied only when the buyer purchases multiple quantities of a single item in the promotion. Otherwise, the promotional discount applies to multiple quantities of any items in the promotion. Different variations of a multi-variation item are considered to be the same item. Note that this flag is not relevant if the <b>inventoryCriterion</b> container identifies a single listing ID for the promotion.  # noqa: E501

        :param apply_discount_to_single_item_only: The apply_discount_to_single_item_only of this ItemPromotion.  # noqa: E501
        :type: bool
        """

        self._apply_discount_to_single_item_only = apply_discount_to_single_item_only

    @property
    def budget(self):
        """Gets the budget of this ItemPromotion.  # noqa: E501


        :return: The budget of this ItemPromotion.  # noqa: E501
        :rtype: Amount
        """
        return self._budget

    @budget.setter
    def budget(self, budget):
        """Sets the budget of this ItemPromotion.


        :param budget: The budget of this ItemPromotion.  # noqa: E501
        :type: Amount
        """

        self._budget = budget

    @property
    def coupon_configuration(self):
        """Gets the coupon_configuration of this ItemPromotion.  # noqa: E501


        :return: The coupon_configuration of this ItemPromotion.  # noqa: E501
        :rtype: CouponConfiguration
        """
        return self._coupon_configuration

    @coupon_configuration.setter
    def coupon_configuration(self, coupon_configuration):
        """Sets the coupon_configuration of this ItemPromotion.


        :param coupon_configuration: The coupon_configuration of this ItemPromotion.  # noqa: E501
        :type: CouponConfiguration
        """

        self._coupon_configuration = coupon_configuration

    @property
    def description(self):
        """Gets the description of this ItemPromotion.  # noqa: E501

        This is the seller-defined \"tag line\" for the offer, such as \"Save on designer shoes.\"  <br><br>The tag line appears under the \"offer-type text\" that is generated for the promotion and is displayed on the offer tile that's shown on the seller's <b>All Offers</b> page, and on the event page for the promotion.  <p class=\"tablenote\"><b>Note:</b> Offer-type text is a teaser that's presented throughout the buyer's journey through the sales flow and is generated by eBay. The offer-type text is not editable by the seller&mdash;it's derived from the settings in the <b>discountRules</b> and <b>discountSpecification</b> fields&mdash;and can be, for example, \"Extra 20% off when you buy 3+\".</p>  <br><b>Maximum length:</b> 50 <br><br><i>Required if</i> you are configuring CODED_COUPON, ORDER_DISCOUNT, or MARKDOWN_SALE promotions (and not valid for VOLUME_DISCOUNT promotions).  # noqa: E501

        :return: The description of this ItemPromotion.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ItemPromotion.

        This is the seller-defined \"tag line\" for the offer, such as \"Save on designer shoes.\"  <br><br>The tag line appears under the \"offer-type text\" that is generated for the promotion and is displayed on the offer tile that's shown on the seller's <b>All Offers</b> page, and on the event page for the promotion.  <p class=\"tablenote\"><b>Note:</b> Offer-type text is a teaser that's presented throughout the buyer's journey through the sales flow and is generated by eBay. The offer-type text is not editable by the seller&mdash;it's derived from the settings in the <b>discountRules</b> and <b>discountSpecification</b> fields&mdash;and can be, for example, \"Extra 20% off when you buy 3+\".</p>  <br><b>Maximum length:</b> 50 <br><br><i>Required if</i> you are configuring CODED_COUPON, ORDER_DISCOUNT, or MARKDOWN_SALE promotions (and not valid for VOLUME_DISCOUNT promotions).  # noqa: E501

        :param description: The description of this ItemPromotion.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def discount_rules(self):
        """Gets the discount_rules of this ItemPromotion.  # noqa: E501

        This container defines a promotion using the following two required fields: <ul><li><b>discountBenefit</b> &ndash; Defines a discount as either a monetary amount or a percentage that is subtracted from the sales price of an item, a set of items, or an order.</li>  <li><b>discountSpecification</b> &ndash; Defines a set of rules that determine when the promotion is applied.</li></ul> <p class=\"tablenote\"><b>Note:</b> For volume pricing, you must specify at least two and not more than four <b>discountBenefit</b>/<b>discountSpecification</b> pairs. In addition, you must define each set of rules with a <b>ruleOrder</b> value that corresponds with the order of volume discounts you present.</p>  <p><b>Tip:</b> Refer to <a href=\"/api-docs/sell/static/marketing/pm-specifying-discounts.html\">Specifying item promotion discounts</a> for information and examples on how to combine <b>discountBenefit</b> and <b>discountSpecification</b> to create different types of promotions.</p>  # noqa: E501

        :return: The discount_rules of this ItemPromotion.  # noqa: E501
        :rtype: list[DiscountRule]
        """
        return self._discount_rules

    @discount_rules.setter
    def discount_rules(self, discount_rules):
        """Sets the discount_rules of this ItemPromotion.

        This container defines a promotion using the following two required fields: <ul><li><b>discountBenefit</b> &ndash; Defines a discount as either a monetary amount or a percentage that is subtracted from the sales price of an item, a set of items, or an order.</li>  <li><b>discountSpecification</b> &ndash; Defines a set of rules that determine when the promotion is applied.</li></ul> <p class=\"tablenote\"><b>Note:</b> For volume pricing, you must specify at least two and not more than four <b>discountBenefit</b>/<b>discountSpecification</b> pairs. In addition, you must define each set of rules with a <b>ruleOrder</b> value that corresponds with the order of volume discounts you present.</p>  <p><b>Tip:</b> Refer to <a href=\"/api-docs/sell/static/marketing/pm-specifying-discounts.html\">Specifying item promotion discounts</a> for information and examples on how to combine <b>discountBenefit</b> and <b>discountSpecification</b> to create different types of promotions.</p>  # noqa: E501

        :param discount_rules: The discount_rules of this ItemPromotion.  # noqa: E501
        :type: list[DiscountRule]
        """

        self._discount_rules = discount_rules

    @property
    def end_date(self):
        """Gets the end_date of this ItemPromotion.  # noqa: E501

        The date and time the promotion ends in UTC format (<code>yyyy-MM-ddThh:mm:ssZ</code>). For display purposes, convert this time into the local time of the seller.  # noqa: E501

        :return: The end_date of this ItemPromotion.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this ItemPromotion.

        The date and time the promotion ends in UTC format (<code>yyyy-MM-ddThh:mm:ssZ</code>). For display purposes, convert this time into the local time of the seller.  # noqa: E501

        :param end_date: The end_date of this ItemPromotion.  # noqa: E501
        :type: str
        """

        self._end_date = end_date

    @property
    def inventory_criterion(self):
        """Gets the inventory_criterion of this ItemPromotion.  # noqa: E501


        :return: The inventory_criterion of this ItemPromotion.  # noqa: E501
        :rtype: InventoryCriterion
        """
        return self._inventory_criterion

    @inventory_criterion.setter
    def inventory_criterion(self, inventory_criterion):
        """Sets the inventory_criterion of this ItemPromotion.


        :param inventory_criterion: The inventory_criterion of this ItemPromotion.  # noqa: E501
        :type: InventoryCriterion
        """

        self._inventory_criterion = inventory_criterion

    @property
    def marketplace_id(self):
        """Gets the marketplace_id of this ItemPromotion.  # noqa: E501

        The eBay marketplace ID of the site where the threshold promotion is hosted. Threshold promotions are currently supported on a limited number of eBay marketplaces.  <p><b>Valid values:</b></p>  <ul><li><code>EBAY_AU</code> = Australia</li> <li><code>EBAY_DE</code> = Germany</li> <li><code>EBAY_ES</code> = Spain</li> <li><code>EBAY_FR</code> = France</li> <li><code>EBAY_GB</code> = Great Britain</li> <li><code>EBAY_IT</code> = Italy</li> <li><code>EBAY_US</code> = United States</li></ul> For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/ba:MarketplaceIdEnum'>eBay API documentation</a>  # noqa: E501

        :return: The marketplace_id of this ItemPromotion.  # noqa: E501
        :rtype: str
        """
        return self._marketplace_id

    @marketplace_id.setter
    def marketplace_id(self, marketplace_id):
        """Sets the marketplace_id of this ItemPromotion.

        The eBay marketplace ID of the site where the threshold promotion is hosted. Threshold promotions are currently supported on a limited number of eBay marketplaces.  <p><b>Valid values:</b></p>  <ul><li><code>EBAY_AU</code> = Australia</li> <li><code>EBAY_DE</code> = Germany</li> <li><code>EBAY_ES</code> = Spain</li> <li><code>EBAY_FR</code> = France</li> <li><code>EBAY_GB</code> = Great Britain</li> <li><code>EBAY_IT</code> = Italy</li> <li><code>EBAY_US</code> = United States</li></ul> For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/ba:MarketplaceIdEnum'>eBay API documentation</a>  # noqa: E501

        :param marketplace_id: The marketplace_id of this ItemPromotion.  # noqa: E501
        :type: str
        """

        self._marketplace_id = marketplace_id

    @property
    def name(self):
        """Gets the name of this ItemPromotion.  # noqa: E501

        The seller-defined name or \"title\" of the promotion that the seller can use to identify a promotion. This label is not displayed in end-user flows.  <br><br><b>Maximum length:</b> 90  # noqa: E501

        :return: The name of this ItemPromotion.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ItemPromotion.

        The seller-defined name or \"title\" of the promotion that the seller can use to identify a promotion. This label is not displayed in end-user flows.  <br><br><b>Maximum length:</b> 90  # noqa: E501

        :param name: The name of this ItemPromotion.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def priority(self):
        """Gets the priority of this ItemPromotion.  # noqa: E501

        Applicable for only <b>ORDER_DISCOUNT</b> promotions, this field indicates the precedence of the promotion, which is used to determine the position of a promotion on the seller's <b>All Offers</b> page. If an item is associated with multiple promotions, the promotion with the higher priority takes precedence. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/sme:PromotionPriorityEnum'>eBay API documentation</a>  # noqa: E501

        :return: The priority of this ItemPromotion.  # noqa: E501
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this ItemPromotion.

        Applicable for only <b>ORDER_DISCOUNT</b> promotions, this field indicates the precedence of the promotion, which is used to determine the position of a promotion on the seller's <b>All Offers</b> page. If an item is associated with multiple promotions, the promotion with the higher priority takes precedence. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/sme:PromotionPriorityEnum'>eBay API documentation</a>  # noqa: E501

        :param priority: The priority of this ItemPromotion.  # noqa: E501
        :type: str
        """

        self._priority = priority

    @property
    def promotion_image_url(self):
        """Gets the promotion_image_url of this ItemPromotion.  # noqa: E501

        Required for CODED_COUPON, MARKDOWN_SALE, and ORDER_DISCOUNT promotions, and not valid for VOLUME_DISCOUNT promotions.  <br><br>Populate this field with a URL that points to an image to be used with the promotion. This image is displayed on the seller's <b>All Offers</b> page. The URL must point to either JPEG or PNG image and it must be a minimum of 500x500 pixels in dimension and cannot exceed 12Mb in size.  # noqa: E501

        :return: The promotion_image_url of this ItemPromotion.  # noqa: E501
        :rtype: str
        """
        return self._promotion_image_url

    @promotion_image_url.setter
    def promotion_image_url(self, promotion_image_url):
        """Sets the promotion_image_url of this ItemPromotion.

        Required for CODED_COUPON, MARKDOWN_SALE, and ORDER_DISCOUNT promotions, and not valid for VOLUME_DISCOUNT promotions.  <br><br>Populate this field with a URL that points to an image to be used with the promotion. This image is displayed on the seller's <b>All Offers</b> page. The URL must point to either JPEG or PNG image and it must be a minimum of 500x500 pixels in dimension and cannot exceed 12Mb in size.  # noqa: E501

        :param promotion_image_url: The promotion_image_url of this ItemPromotion.  # noqa: E501
        :type: str
        """

        self._promotion_image_url = promotion_image_url

    @property
    def promotion_status(self):
        """Gets the promotion_status of this ItemPromotion.  # noqa: E501

        The current status of the promotion. When creating a new promotion, this value must be set to either <code>DRAFT</code> or <code>SCHEDULED</code>.  <br><br>Note that you must set this value to <code>SCHEDULED</code> when you update a <b>RUNNING</b> promotion. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/sme:PromotionStatusEnum'>eBay API documentation</a>  # noqa: E501

        :return: The promotion_status of this ItemPromotion.  # noqa: E501
        :rtype: str
        """
        return self._promotion_status

    @promotion_status.setter
    def promotion_status(self, promotion_status):
        """Sets the promotion_status of this ItemPromotion.

        The current status of the promotion. When creating a new promotion, this value must be set to either <code>DRAFT</code> or <code>SCHEDULED</code>.  <br><br>Note that you must set this value to <code>SCHEDULED</code> when you update a <b>RUNNING</b> promotion. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/sme:PromotionStatusEnum'>eBay API documentation</a>  # noqa: E501

        :param promotion_status: The promotion_status of this ItemPromotion.  # noqa: E501
        :type: str
        """

        self._promotion_status = promotion_status

    @property
    def promotion_type(self):
        """Gets the promotion_type of this ItemPromotion.  # noqa: E501

        Use this field to specify the type of the promotion you are creating. <p>The supported types are:</p> <ul><li><code>CODED_COUPON</code> &ndash; A coupon code promotion set with <b>createItemPromotion</b>.</li> <li><code>MARKDOWN_SALE</code> &ndash; A markdown promotion set with <b>createItemPriceMarkdownPromotion</b>.</li> <li><code>ORDER_DISCOUNT</code> &ndash; A threshold promotion set with <b>createItemPromotion</b>.</li> <li><code>VOLUME_DISCOUNT</code> &ndash; A volume pricing promotion set with <b>createItemPromotion</b>.</li></ul> <p>See the <a href=\"/api-docs/sell/static/marketing/promotions-manager.html\" target=\"_blank\">Promotions Manager</a> documentation for details.</p> <p><i>Required if </i> you are creating a volume pricing promotion (<code>VOLUME_DISCOUNT</code>).</p> For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/sme:PromotionTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The promotion_type of this ItemPromotion.  # noqa: E501
        :rtype: str
        """
        return self._promotion_type

    @promotion_type.setter
    def promotion_type(self, promotion_type):
        """Sets the promotion_type of this ItemPromotion.

        Use this field to specify the type of the promotion you are creating. <p>The supported types are:</p> <ul><li><code>CODED_COUPON</code> &ndash; A coupon code promotion set with <b>createItemPromotion</b>.</li> <li><code>MARKDOWN_SALE</code> &ndash; A markdown promotion set with <b>createItemPriceMarkdownPromotion</b>.</li> <li><code>ORDER_DISCOUNT</code> &ndash; A threshold promotion set with <b>createItemPromotion</b>.</li> <li><code>VOLUME_DISCOUNT</code> &ndash; A volume pricing promotion set with <b>createItemPromotion</b>.</li></ul> <p>See the <a href=\"/api-docs/sell/static/marketing/promotions-manager.html\" target=\"_blank\">Promotions Manager</a> documentation for details.</p> <p><i>Required if </i> you are creating a volume pricing promotion (<code>VOLUME_DISCOUNT</code>).</p> For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/sme:PromotionTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param promotion_type: The promotion_type of this ItemPromotion.  # noqa: E501
        :type: str
        """

        self._promotion_type = promotion_type

    @property
    def start_date(self):
        """Gets the start_date of this ItemPromotion.  # noqa: E501

        The date and time the promotion starts in UTC format (<code>yyyy-MM-ddThh:mm:ssZ</code>). For display purposes, convert this time into the local time of the seller.  # noqa: E501

        :return: The start_date of this ItemPromotion.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ItemPromotion.

        The date and time the promotion starts in UTC format (<code>yyyy-MM-ddThh:mm:ssZ</code>). For display purposes, convert this time into the local time of the seller.  # noqa: E501

        :param start_date: The start_date of this ItemPromotion.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

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
        if issubclass(ItemPromotion, dict):
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
        if not isinstance(other, ItemPromotion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
