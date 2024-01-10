# coding: utf-8

"""
    Marketing API

    <p>The <i>Marketing API </i> offers two platforms that sellers can use to promote and advertise their products:</p> <ul><li><b>Promoted Listings</b> is an eBay ad service that lets sellers set up <i>ad campaigns </i> for the products they want to promote. eBay displays the ads in search results and in other marketing modules as <b>SPONSORED</b> listings. If an item in a Promoted Listings campaign sells, the seller is assessed a Promoted Listings fee, which is a seller-specified percentage applied to the sales price. For complete details, refer to the <a href=\"/api-docs/sell/static/marketing/pl-landing.html\">Promoted Listings playbook</a>.</li><li><b>Promotions Manager</b> gives sellers a way to offer discounts on specific items as a way to attract buyers to their inventory. Sellers can set up discounts (such as \"20% off\" and other types of offers) on specific items or on an entire customer order. To further attract buyers, eBay prominently displays promotion <i>teasers</i> throughout buyer flows. For complete details, see <a href=\"/api-docs/sell/static/marketing/promotions-manager.html\">Promotions Manager</a>.</li></ul>  <p><b>Marketing reports</b>, on both the Promoted Listings and Promotions Manager platforms, give sellers information that shows the effectiveness of their marketing strategies. The data gives sellers the ability to review and fine tune their marketing efforts.</p><p><b>Store Email Campaign</b> allows sellers to create and send email campaigns to customers who have signed up to receive their newsletter. For more information on email campaigns, see <a href=\"/api-docs/sell/static/marketing/store-email-campaigns.html#email-campain-types\" target=\"_blank\">Store Email Campaigns</a>.<p class=\"tablenote\"><b>Important!</b> Sellers must have an active eBay Store subscription, and they must accept the <b>Terms and Conditions</b> before they can make requests to these APIs in the Production environment. There are also site-specific listings requirements and restrictions associated with these marketing tools, as listed in the \"requirements and restrictions\" sections for <a href=\"/api-docs/sell/marketing/static/overview.html#PL-requirements\">Promoted Listings</a> and <a href=\"/api-docs/sell/marketing/static/overview.html#PM-requirements\">Promotions Manager</a>.</p> <p>The table below lists all the Marketing API calls grouped by resource.</p>  # noqa: E501

    OpenAPI spec version: v1.20.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CreateEmailCampaignRequest(object):
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
        'audience_codes': 'list[str]',
        'category_id': 'str',
        'category_type': 'str',
        'email_campaign_type': 'str',
        'item_ids': 'list[str]',
        'item_select_mode': 'str',
        'personalized_message': 'str',
        'price_range': 'PriceRange',
        'promotion_id': 'str',
        'promotion_select_mode_enum': 'str',
        'schedule_date': 'str',
        'sort': 'str',
        'subject': 'str'
    }

    attribute_map = {
        'audience_codes': 'audienceCodes',
        'category_id': 'categoryId',
        'category_type': 'categoryType',
        'email_campaign_type': 'emailCampaignType',
        'item_ids': 'itemIds',
        'item_select_mode': 'itemSelectMode',
        'personalized_message': 'personalizedMessage',
        'price_range': 'priceRange',
        'promotion_id': 'promotionId',
        'promotion_select_mode_enum': 'promotionSelectModeEnum',
        'schedule_date': 'scheduleDate',
        'sort': 'sort',
        'subject': 'subject'
    }

    def __init__(self, audience_codes=None, category_id=None, category_type=None, email_campaign_type=None, item_ids=None, item_select_mode=None, personalized_message=None, price_range=None, promotion_id=None, promotion_select_mode_enum=None, schedule_date=None, sort=None, subject=None):  # noqa: E501
        """CreateEmailCampaignRequest - a model defined in Swagger"""  # noqa: E501
        self._audience_codes = None
        self._category_id = None
        self._category_type = None
        self._email_campaign_type = None
        self._item_ids = None
        self._item_select_mode = None
        self._personalized_message = None
        self._price_range = None
        self._promotion_id = None
        self._promotion_select_mode_enum = None
        self._schedule_date = None
        self._sort = None
        self._subject = None
        self.discriminator = None
        if audience_codes is not None:
            self.audience_codes = audience_codes
        if category_id is not None:
            self.category_id = category_id
        if category_type is not None:
            self.category_type = category_type
        if email_campaign_type is not None:
            self.email_campaign_type = email_campaign_type
        if item_ids is not None:
            self.item_ids = item_ids
        if item_select_mode is not None:
            self.item_select_mode = item_select_mode
        if personalized_message is not None:
            self.personalized_message = personalized_message
        if price_range is not None:
            self.price_range = price_range
        if promotion_id is not None:
            self.promotion_id = promotion_id
        if promotion_select_mode_enum is not None:
            self.promotion_select_mode_enum = promotion_select_mode_enum
        if schedule_date is not None:
            self.schedule_date = schedule_date
        if sort is not None:
            self.sort = sort
        if subject is not None:
            self.subject = subject

    @property
    def audience_codes(self):
        """Gets the audience_codes of this CreateEmailCampaignRequest.  # noqa: E501

        An array of audience codes for the audiences of the email campaign. At least one audience code is required. There is no upper limit to the number of audience codes.<br><br>To retrieve seller audiences, call <a href=\"/api-docs/sell/marketing/resources/email_campaign/methods/getAudiences\" target=\"_blank\">getAudiences</a>. Use the <b>code</b> values in the response to populate <b>audienceCodes</b>.  # noqa: E501

        :return: The audience_codes of this CreateEmailCampaignRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._audience_codes

    @audience_codes.setter
    def audience_codes(self, audience_codes):
        """Sets the audience_codes of this CreateEmailCampaignRequest.

        An array of audience codes for the audiences of the email campaign. At least one audience code is required. There is no upper limit to the number of audience codes.<br><br>To retrieve seller audiences, call <a href=\"/api-docs/sell/marketing/resources/email_campaign/methods/getAudiences\" target=\"_blank\">getAudiences</a>. Use the <b>code</b> values in the response to populate <b>audienceCodes</b>.  # noqa: E501

        :param audience_codes: The audience_codes of this CreateEmailCampaignRequest.  # noqa: E501
        :type: list[str]
        """

        self._audience_codes = audience_codes

    @property
    def category_id(self):
        """Gets the category_id of this CreateEmailCampaignRequest.  # noqa: E501

        The unique identifier of either an eBay category or a store category.<br><br>This field is used if a seller wants to apply an email campaign to a specific eBay category or store category. The <b>categoryType</b> determines whether the <b>categoryId</b> value is an eBay category or store category.<br><br>To retrieve eBay categories, use the <a href=\"https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetCategories.html\" target=\"_blank\">getCategories</a> or Taxonomy API. To retrieve seller store categories, use the <a href=\"https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetStore.html\" target=\"_blank\">getStore</a> call. Use the <b>categoryId</b> value of the desired category from the results as the value in the request.<br><br><b>itemSelectMode</b> must be set to <code>AUTO</code> in order to use a category ID.  # noqa: E501

        :return: The category_id of this CreateEmailCampaignRequest.  # noqa: E501
        :rtype: str
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this CreateEmailCampaignRequest.

        The unique identifier of either an eBay category or a store category.<br><br>This field is used if a seller wants to apply an email campaign to a specific eBay category or store category. The <b>categoryType</b> determines whether the <b>categoryId</b> value is an eBay category or store category.<br><br>To retrieve eBay categories, use the <a href=\"https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetCategories.html\" target=\"_blank\">getCategories</a> or Taxonomy API. To retrieve seller store categories, use the <a href=\"https://developer.ebay.com/devzone/xml/docs/reference/ebay/GetStore.html\" target=\"_blank\">getStore</a> call. Use the <b>categoryId</b> value of the desired category from the results as the value in the request.<br><br><b>itemSelectMode</b> must be set to <code>AUTO</code> in order to use a category ID.  # noqa: E501

        :param category_id: The category_id of this CreateEmailCampaignRequest.  # noqa: E501
        :type: str
        """

        self._category_id = category_id

    @property
    def category_type(self):
        """Gets the category_type of this CreateEmailCampaignRequest.  # noqa: E501

        This field must be set when applying an email campaign to a specific eBay category or store category. The enumeration value used indicates which type of category the <b>categoryId</b> belongs to. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/api:CategoryTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The category_type of this CreateEmailCampaignRequest.  # noqa: E501
        :rtype: str
        """
        return self._category_type

    @category_type.setter
    def category_type(self, category_type):
        """Sets the category_type of this CreateEmailCampaignRequest.

        This field must be set when applying an email campaign to a specific eBay category or store category. The enumeration value used indicates which type of category the <b>categoryId</b> belongs to. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/api:CategoryTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param category_type: The category_type of this CreateEmailCampaignRequest.  # noqa: E501
        :type: str
        """

        self._category_type = category_type

    @property
    def email_campaign_type(self):
        """Gets the email_campaign_type of this CreateEmailCampaignRequest.  # noqa: E501

        The email campaign type of the email campaign being created. There are six <a href=\"/api-docs/sell/marketing/types/api:CampaignTypeEnum\">email campaigns</a> that a user can create:<ul><li><code>WELCOME</code> - an email sent automatically to new subscribers.</li><li><code>ITEM_SHOWCASE</code> - an email featuring new products & collections that the seller wants to highlight.</li><li><code>COUPON</code> - an email containing a coupon code and up to 4 items that this coupon can be applied to.</li><li><code>ORDER_DISCOUNT</code> - an email containing an order discount and up to 10 items that this discount can be applied to.</li><li><code>SALE_EVENT</code> - an email about a sale event and up to 10 items that the sale can be applied to.</li><li><code>VOLUME_PRICING</code> - an email containing up to 10 items that are eligible for volume pricing.</li></ul><br><span class=\"tablenote\"><b>Note:</b> <b>emailCampaignType</b> cannot be updated once the email campaign is created.</span> For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/api:CampaignTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The email_campaign_type of this CreateEmailCampaignRequest.  # noqa: E501
        :rtype: str
        """
        return self._email_campaign_type

    @email_campaign_type.setter
    def email_campaign_type(self, email_campaign_type):
        """Sets the email_campaign_type of this CreateEmailCampaignRequest.

        The email campaign type of the email campaign being created. There are six <a href=\"/api-docs/sell/marketing/types/api:CampaignTypeEnum\">email campaigns</a> that a user can create:<ul><li><code>WELCOME</code> - an email sent automatically to new subscribers.</li><li><code>ITEM_SHOWCASE</code> - an email featuring new products & collections that the seller wants to highlight.</li><li><code>COUPON</code> - an email containing a coupon code and up to 4 items that this coupon can be applied to.</li><li><code>ORDER_DISCOUNT</code> - an email containing an order discount and up to 10 items that this discount can be applied to.</li><li><code>SALE_EVENT</code> - an email about a sale event and up to 10 items that the sale can be applied to.</li><li><code>VOLUME_PRICING</code> - an email containing up to 10 items that are eligible for volume pricing.</li></ul><br><span class=\"tablenote\"><b>Note:</b> <b>emailCampaignType</b> cannot be updated once the email campaign is created.</span> For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/api:CampaignTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param email_campaign_type: The email_campaign_type of this CreateEmailCampaignRequest.  # noqa: E501
        :type: str
        """

        self._email_campaign_type = email_campaign_type

    @property
    def item_ids(self):
        """Gets the item_ids of this CreateEmailCampaignRequest.  # noqa: E501

        An array of unique identifiers for the listings displayed in an email campaign. Used if the seller wishes to select the eBay listings in the email campaign rather than have eBay automatically select them. <br><br>Call <a href=\"/DevZone/XML/docs/Reference/eBay/GetSellerList.html#GetSellerList\">getSellerList</a> to retrieve all seller listings. Each <b>Item</b> result contains an <b>ItemID</b> value. Use this value in <b>itemIds</b> to feature that listing.<br><br>The maximum number of <b>itemIds</b> for the <code>COUPON</code> campaign type is 4, and for every other campaign type is 10<br><br><b>itemSelectMode</b> must be set to <code>MANUAL</code> in order to use this field.  # noqa: E501

        :return: The item_ids of this CreateEmailCampaignRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._item_ids

    @item_ids.setter
    def item_ids(self, item_ids):
        """Sets the item_ids of this CreateEmailCampaignRequest.

        An array of unique identifiers for the listings displayed in an email campaign. Used if the seller wishes to select the eBay listings in the email campaign rather than have eBay automatically select them. <br><br>Call <a href=\"/DevZone/XML/docs/Reference/eBay/GetSellerList.html#GetSellerList\">getSellerList</a> to retrieve all seller listings. Each <b>Item</b> result contains an <b>ItemID</b> value. Use this value in <b>itemIds</b> to feature that listing.<br><br>The maximum number of <b>itemIds</b> for the <code>COUPON</code> campaign type is 4, and for every other campaign type is 10<br><br><b>itemSelectMode</b> must be set to <code>MANUAL</code> in order to use this field.  # noqa: E501

        :param item_ids: The item_ids of this CreateEmailCampaignRequest.  # noqa: E501
        :type: list[str]
        """

        self._item_ids = item_ids

    @property
    def item_select_mode(self):
        """Gets the item_select_mode of this CreateEmailCampaignRequest.  # noqa: E501

        Determines whether listings featured in an email campaign are selected by the seller or by eBay.<br><br>If <b>itemSelectMode</b> is set to <code>AUTO</code>, eBay automatically choses listings based on values set for <b>sort</b>, <b>categoryType</b>, <b>categoryId</b>, and <b>priceRange</b>.<br><br>If <b>itemSelectMode</b> is set to <code>MANUAL</code>, listings are set by the seller by populating the <b>itemIds</b> array.<br><br><span class=\"tablenote\"><b>Note: </b><b>itemSelectMode</b> is always set to <code>AUTO</code> for <code>WELCOME</code> email campaigns.</span> For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/api:ItemSelectModeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The item_select_mode of this CreateEmailCampaignRequest.  # noqa: E501
        :rtype: str
        """
        return self._item_select_mode

    @item_select_mode.setter
    def item_select_mode(self, item_select_mode):
        """Sets the item_select_mode of this CreateEmailCampaignRequest.

        Determines whether listings featured in an email campaign are selected by the seller or by eBay.<br><br>If <b>itemSelectMode</b> is set to <code>AUTO</code>, eBay automatically choses listings based on values set for <b>sort</b>, <b>categoryType</b>, <b>categoryId</b>, and <b>priceRange</b>.<br><br>If <b>itemSelectMode</b> is set to <code>MANUAL</code>, listings are set by the seller by populating the <b>itemIds</b> array.<br><br><span class=\"tablenote\"><b>Note: </b><b>itemSelectMode</b> is always set to <code>AUTO</code> for <code>WELCOME</code> email campaigns.</span> For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/api:ItemSelectModeEnum'>eBay API documentation</a>  # noqa: E501

        :param item_select_mode: The item_select_mode of this CreateEmailCampaignRequest.  # noqa: E501
        :type: str
        """

        self._item_select_mode = item_select_mode

    @property
    def personalized_message(self):
        """Gets the personalized_message of this CreateEmailCampaignRequest.  # noqa: E501

        The body of the email campaign. Accepts HTML and CSS.<br><br><b>Max length:</b> 1000  # noqa: E501

        :return: The personalized_message of this CreateEmailCampaignRequest.  # noqa: E501
        :rtype: str
        """
        return self._personalized_message

    @personalized_message.setter
    def personalized_message(self, personalized_message):
        """Sets the personalized_message of this CreateEmailCampaignRequest.

        The body of the email campaign. Accepts HTML and CSS.<br><br><b>Max length:</b> 1000  # noqa: E501

        :param personalized_message: The personalized_message of this CreateEmailCampaignRequest.  # noqa: E501
        :type: str
        """

        self._personalized_message = personalized_message

    @property
    def price_range(self):
        """Gets the price_range of this CreateEmailCampaignRequest.  # noqa: E501


        :return: The price_range of this CreateEmailCampaignRequest.  # noqa: E501
        :rtype: PriceRange
        """
        return self._price_range

    @price_range.setter
    def price_range(self, price_range):
        """Sets the price_range of this CreateEmailCampaignRequest.


        :param price_range: The price_range of this CreateEmailCampaignRequest.  # noqa: E501
        :type: PriceRange
        """

        self._price_range = price_range

    @property
    def promotion_id(self):
        """Gets the promotion_id of this CreateEmailCampaignRequest.  # noqa: E501

        The unique identifier of the promotion used for an email campaign if the <b>emailCampaignType</b> is set to <code>COUPON</code>, <code>SALE_EVENT</code>, or <code>ORDER_DISCOUNT</code>. <b>promotionSelectModeEnum</b> must set to <code>MANUAL</code> if a promotion is selected.<br><br>Call <a href=\"/api-docs/sell/marketing/resources/promotion/methods/getPromotions\" target=\"_blank\">getPromotions</a> to retrieve a list of the seller's promotions. Use the <b>promotionId</b> from an individual <b>PromotionDetail</b> in the result to populate the request.  # noqa: E501

        :return: The promotion_id of this CreateEmailCampaignRequest.  # noqa: E501
        :rtype: str
        """
        return self._promotion_id

    @promotion_id.setter
    def promotion_id(self, promotion_id):
        """Sets the promotion_id of this CreateEmailCampaignRequest.

        The unique identifier of the promotion used for an email campaign if the <b>emailCampaignType</b> is set to <code>COUPON</code>, <code>SALE_EVENT</code>, or <code>ORDER_DISCOUNT</code>. <b>promotionSelectModeEnum</b> must set to <code>MANUAL</code> if a promotion is selected.<br><br>Call <a href=\"/api-docs/sell/marketing/resources/promotion/methods/getPromotions\" target=\"_blank\">getPromotions</a> to retrieve a list of the seller's promotions. Use the <b>promotionId</b> from an individual <b>PromotionDetail</b> in the result to populate the request.  # noqa: E501

        :param promotion_id: The promotion_id of this CreateEmailCampaignRequest.  # noqa: E501
        :type: str
        """

        self._promotion_id = promotion_id

    @property
    def promotion_select_mode_enum(self):
        """Gets the promotion_select_mode_enum of this CreateEmailCampaignRequest.  # noqa: E501

        The selection mode for the promotion used if the <b>emailCampaignType</b> is set to <code>COUPON</code>, <code>SALE_EVENT</code>, or <code>ORDER_DISCOUNT</code>.<br><br>If <b>promotionSelectModeEnum</b> is set to <code>AUTO</code>, eBay will choose the promotion to include in the email campaign. If set to <code>MANUAL</code>, the seller must specify the promotion in the <b>promotionId</b> field. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/api:PromotionSelectModeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The promotion_select_mode_enum of this CreateEmailCampaignRequest.  # noqa: E501
        :rtype: str
        """
        return self._promotion_select_mode_enum

    @promotion_select_mode_enum.setter
    def promotion_select_mode_enum(self, promotion_select_mode_enum):
        """Sets the promotion_select_mode_enum of this CreateEmailCampaignRequest.

        The selection mode for the promotion used if the <b>emailCampaignType</b> is set to <code>COUPON</code>, <code>SALE_EVENT</code>, or <code>ORDER_DISCOUNT</code>.<br><br>If <b>promotionSelectModeEnum</b> is set to <code>AUTO</code>, eBay will choose the promotion to include in the email campaign. If set to <code>MANUAL</code>, the seller must specify the promotion in the <b>promotionId</b> field. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/api:PromotionSelectModeEnum'>eBay API documentation</a>  # noqa: E501

        :param promotion_select_mode_enum: The promotion_select_mode_enum of this CreateEmailCampaignRequest.  # noqa: E501
        :type: str
        """

        self._promotion_select_mode_enum = promotion_select_mode_enum

    @property
    def schedule_date(self):
        """Gets the schedule_date of this CreateEmailCampaignRequest.  # noqa: E501

        The date and time that the email campaign newsletter will be sent, given in UTC format. Example: 2023-05-20T03:13:35Z<br><br>This field should be used if the seller wishes to send the email campaign on a future date. If no <b>scheduleDate</b> is set, the email campaign will send once it is created or updated.  # noqa: E501

        :return: The schedule_date of this CreateEmailCampaignRequest.  # noqa: E501
        :rtype: str
        """
        return self._schedule_date

    @schedule_date.setter
    def schedule_date(self, schedule_date):
        """Sets the schedule_date of this CreateEmailCampaignRequest.

        The date and time that the email campaign newsletter will be sent, given in UTC format. Example: 2023-05-20T03:13:35Z<br><br>This field should be used if the seller wishes to send the email campaign on a future date. If no <b>scheduleDate</b> is set, the email campaign will send once it is created or updated.  # noqa: E501

        :param schedule_date: The schedule_date of this CreateEmailCampaignRequest.  # noqa: E501
        :type: str
        """

        self._schedule_date = schedule_date

    @property
    def sort(self):
        """Gets the sort of this CreateEmailCampaignRequest.  # noqa: E501

        The sort rule is used to display the listings featured in the email campaign.<br><br>Sort rules are only used if <b>itemSelectMode</b> is set to <code>AUTO</code>. If <b>itemSelectMode</b> is <code>MANUAL</code>, listings are displayed in the order in which they are listed in the <b>itemIds</b> array. The following sort rules are available:<ul><li><code>ENDING_FIRST</code> displays listings by ending date, from soonest to latest.</li><li><code>LOWEST_PRICED</code> displays listings by price, from lowest to highest.</li><li><code>HIGHEST_PRICED</code> displays listings by price, from highest to lowest.</li><li><code>NEWLY_LISTED</code> displays listings by date listed, with the newest first.</li></ul><br><br>The default sort rule is <code>NEWLY_LISTED</code>. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/api:ItemSortEnum'>eBay API documentation</a>  # noqa: E501

        :return: The sort of this CreateEmailCampaignRequest.  # noqa: E501
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this CreateEmailCampaignRequest.

        The sort rule is used to display the listings featured in the email campaign.<br><br>Sort rules are only used if <b>itemSelectMode</b> is set to <code>AUTO</code>. If <b>itemSelectMode</b> is <code>MANUAL</code>, listings are displayed in the order in which they are listed in the <b>itemIds</b> array. The following sort rules are available:<ul><li><code>ENDING_FIRST</code> displays listings by ending date, from soonest to latest.</li><li><code>LOWEST_PRICED</code> displays listings by price, from lowest to highest.</li><li><code>HIGHEST_PRICED</code> displays listings by price, from highest to lowest.</li><li><code>NEWLY_LISTED</code> displays listings by date listed, with the newest first.</li></ul><br><br>The default sort rule is <code>NEWLY_LISTED</code>. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/api:ItemSortEnum'>eBay API documentation</a>  # noqa: E501

        :param sort: The sort of this CreateEmailCampaignRequest.  # noqa: E501
        :type: str
        """

        self._sort = sort

    @property
    def subject(self):
        """Gets the subject of this CreateEmailCampaignRequest.  # noqa: E501

        The subject line of the email campaign.<br><br><b>Max length:</b> 70  # noqa: E501

        :return: The subject of this CreateEmailCampaignRequest.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this CreateEmailCampaignRequest.

        The subject line of the email campaign.<br><br><b>Max length:</b> 70  # noqa: E501

        :param subject: The subject of this CreateEmailCampaignRequest.  # noqa: E501
        :type: str
        """

        self._subject = subject

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
        if issubclass(CreateEmailCampaignRequest, dict):
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
        if not isinstance(other, CreateEmailCampaignRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
