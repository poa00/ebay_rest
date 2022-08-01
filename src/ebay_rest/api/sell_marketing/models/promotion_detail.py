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

class PromotionDetail(object):
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
        'coupon_code': 'str',
        'description': 'str',
        'end_date': 'str',
        'marketplace_id': 'str',
        'name': 'str',
        'priority': 'str',
        'promotion_href': 'str',
        'promotion_id': 'str',
        'promotion_image_url': 'str',
        'promotion_status': 'str',
        'promotion_type': 'str',
        'start_date': 'str'
    }

    attribute_map = {
        'coupon_code': 'couponCode',
        'description': 'description',
        'end_date': 'endDate',
        'marketplace_id': 'marketplaceId',
        'name': 'name',
        'priority': 'priority',
        'promotion_href': 'promotionHref',
        'promotion_id': 'promotionId',
        'promotion_image_url': 'promotionImageUrl',
        'promotion_status': 'promotionStatus',
        'promotion_type': 'promotionType',
        'start_date': 'startDate'
    }

    def __init__(self, coupon_code=None, description=None, end_date=None, marketplace_id=None, name=None, priority=None, promotion_href=None, promotion_id=None, promotion_image_url=None, promotion_status=None, promotion_type=None, start_date=None):  # noqa: E501
        """PromotionDetail - a model defined in Swagger"""  # noqa: E501
        self._coupon_code = None
        self._description = None
        self._end_date = None
        self._marketplace_id = None
        self._name = None
        self._priority = None
        self._promotion_href = None
        self._promotion_id = None
        self._promotion_image_url = None
        self._promotion_status = None
        self._promotion_type = None
        self._start_date = None
        self.discriminator = None
        if coupon_code is not None:
            self.coupon_code = coupon_code
        if description is not None:
            self.description = description
        if end_date is not None:
            self.end_date = end_date
        if marketplace_id is not None:
            self.marketplace_id = marketplace_id
        if name is not None:
            self.name = name
        if priority is not None:
            self.priority = priority
        if promotion_href is not None:
            self.promotion_href = promotion_href
        if promotion_id is not None:
            self.promotion_id = promotion_id
        if promotion_image_url is not None:
            self.promotion_image_url = promotion_image_url
        if promotion_status is not None:
            self.promotion_status = promotion_status
        if promotion_type is not None:
            self.promotion_type = promotion_type
        if start_date is not None:
            self.start_date = start_date

    @property
    def coupon_code(self):
        """Gets the coupon_code of this PromotionDetail.  # noqa: E501

        A unique code that buyers can use during checkout to receive a discount. The code must be unique across eBay.  # noqa: E501

        :return: The coupon_code of this PromotionDetail.  # noqa: E501
        :rtype: str
        """
        return self._coupon_code

    @coupon_code.setter
    def coupon_code(self, coupon_code):
        """Sets the coupon_code of this PromotionDetail.

        A unique code that buyers can use during checkout to receive a discount. The code must be unique across eBay.  # noqa: E501

        :param coupon_code: The coupon_code of this PromotionDetail.  # noqa: E501
        :type: str
        """

        self._coupon_code = coupon_code

    @property
    def description(self):
        """Gets the description of this PromotionDetail.  # noqa: E501

        This is the seller-defined \"tag line\" for the offer, such as \"Save on designer shoes.\" Tag lines appear under the \"offer-type text\" that is generated for a promotion and displayed under the offer tile that is shown on the seller's <b>All Offers</b> page and on the promotion's event page.  <p class=\"tablenote\"><b>Note:</b> Offer-type text is a teaser that's presented throughout the buyer's journey through the sales flow and is generated by eBay. This text is not editable by the seller&mdash;it's derived from the settings in the <b>discountRules</b> and <b>discountSpecification</b> fields&mdash;and can be, for example, \"Extra 20% off when you buy 3+\".</p>  <br><b>Maximum length:</b> 50 <br><br><i>Required if</i> you are configuring ORDER_DISCOUNT or MARKDOWN_SALE promotions (and not valid for VOLUME_DISCOUNT promotions).  # noqa: E501

        :return: The description of this PromotionDetail.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PromotionDetail.

        This is the seller-defined \"tag line\" for the offer, such as \"Save on designer shoes.\" Tag lines appear under the \"offer-type text\" that is generated for a promotion and displayed under the offer tile that is shown on the seller's <b>All Offers</b> page and on the promotion's event page.  <p class=\"tablenote\"><b>Note:</b> Offer-type text is a teaser that's presented throughout the buyer's journey through the sales flow and is generated by eBay. This text is not editable by the seller&mdash;it's derived from the settings in the <b>discountRules</b> and <b>discountSpecification</b> fields&mdash;and can be, for example, \"Extra 20% off when you buy 3+\".</p>  <br><b>Maximum length:</b> 50 <br><br><i>Required if</i> you are configuring ORDER_DISCOUNT or MARKDOWN_SALE promotions (and not valid for VOLUME_DISCOUNT promotions).  # noqa: E501

        :param description: The description of this PromotionDetail.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def end_date(self):
        """Gets the end_date of this PromotionDetail.  # noqa: E501

        The date and time the promotion ends in UTC format (<code>yyyy-MM-ddThh:mm:ssZ</code>). For display purposes, convert this time into the local time of the seller.  # noqa: E501

        :return: The end_date of this PromotionDetail.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this PromotionDetail.

        The date and time the promotion ends in UTC format (<code>yyyy-MM-ddThh:mm:ssZ</code>). For display purposes, convert this time into the local time of the seller.  # noqa: E501

        :param end_date: The end_date of this PromotionDetail.  # noqa: E501
        :type: str
        """

        self._end_date = end_date

    @property
    def marketplace_id(self):
        """Gets the marketplace_id of this PromotionDetail.  # noqa: E501

        The eBay marketplace ID of the site where the promotion is hosted. Threshold promotions are supported on a select set of marketplaces while markdown promotions are supported on all eBay marketplaces. <p><b>Valid values for threshold promotions are as follows:</b></p>  <ul class=\"compact\"><li><code>EBAY_AU</code> = Australia</li> <li><code>EBAY_DE</code> = Germany</li> <li><code>EBAY_ES</code> = Spain</li> <li><code>EBAY_FR</code> = France</li> <li><code>EBAY_GB</code> = Great Britain</li> <li><code>EBAY_IT</code> = Italy</li> <li><code>EBAY_US</code> = United States</li></ul> For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/ba:MarketplaceIdEnum'>eBay API documentation</a>  # noqa: E501

        :return: The marketplace_id of this PromotionDetail.  # noqa: E501
        :rtype: str
        """
        return self._marketplace_id

    @marketplace_id.setter
    def marketplace_id(self, marketplace_id):
        """Sets the marketplace_id of this PromotionDetail.

        The eBay marketplace ID of the site where the promotion is hosted. Threshold promotions are supported on a select set of marketplaces while markdown promotions are supported on all eBay marketplaces. <p><b>Valid values for threshold promotions are as follows:</b></p>  <ul class=\"compact\"><li><code>EBAY_AU</code> = Australia</li> <li><code>EBAY_DE</code> = Germany</li> <li><code>EBAY_ES</code> = Spain</li> <li><code>EBAY_FR</code> = France</li> <li><code>EBAY_GB</code> = Great Britain</li> <li><code>EBAY_IT</code> = Italy</li> <li><code>EBAY_US</code> = United States</li></ul> For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/ba:MarketplaceIdEnum'>eBay API documentation</a>  # noqa: E501

        :param marketplace_id: The marketplace_id of this PromotionDetail.  # noqa: E501
        :type: str
        """

        self._marketplace_id = marketplace_id

    @property
    def name(self):
        """Gets the name of this PromotionDetail.  # noqa: E501

        The seller-defined name or \"title\" of the promotion, such as \"Buy 1 Get 1\", that the seller can use to identify a promotion. This label is not displayed in end-user flows.  <br><br><b>Maximum length:</b> 90  # noqa: E501

        :return: The name of this PromotionDetail.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PromotionDetail.

        The seller-defined name or \"title\" of the promotion, such as \"Buy 1 Get 1\", that the seller can use to identify a promotion. This label is not displayed in end-user flows.  <br><br><b>Maximum length:</b> 90  # noqa: E501

        :param name: The name of this PromotionDetail.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def priority(self):
        """Gets the priority of this PromotionDetail.  # noqa: E501

        Applicable for only <b>ORDER_DISCOUNT</b> promotions, this field indicates the precedence of the promotion, which is used to determine the position of a promotion on the seller's <b>All Offers</b> page. If an item is associated with multiple promotions, the promotion with the higher priority takes precedence. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/sme:PromotionPriorityEnum'>eBay API documentation</a>  # noqa: E501

        :return: The priority of this PromotionDetail.  # noqa: E501
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this PromotionDetail.

        Applicable for only <b>ORDER_DISCOUNT</b> promotions, this field indicates the precedence of the promotion, which is used to determine the position of a promotion on the seller's <b>All Offers</b> page. If an item is associated with multiple promotions, the promotion with the higher priority takes precedence. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/sme:PromotionPriorityEnum'>eBay API documentation</a>  # noqa: E501

        :param priority: The priority of this PromotionDetail.  # noqa: E501
        :type: str
        """

        self._priority = priority

    @property
    def promotion_href(self):
        """Gets the promotion_href of this PromotionDetail.  # noqa: E501

        The URI of the promotion details.  # noqa: E501

        :return: The promotion_href of this PromotionDetail.  # noqa: E501
        :rtype: str
        """
        return self._promotion_href

    @promotion_href.setter
    def promotion_href(self, promotion_href):
        """Sets the promotion_href of this PromotionDetail.

        The URI of the promotion details.  # noqa: E501

        :param promotion_href: The promotion_href of this PromotionDetail.  # noqa: E501
        :type: str
        """

        self._promotion_href = promotion_href

    @property
    def promotion_id(self):
        """Gets the promotion_id of this PromotionDetail.  # noqa: E501

        A unique eBay-assigned ID for the promotion that's generated when the promotion is created.  # noqa: E501

        :return: The promotion_id of this PromotionDetail.  # noqa: E501
        :rtype: str
        """
        return self._promotion_id

    @promotion_id.setter
    def promotion_id(self, promotion_id):
        """Sets the promotion_id of this PromotionDetail.

        A unique eBay-assigned ID for the promotion that's generated when the promotion is created.  # noqa: E501

        :param promotion_id: The promotion_id of this PromotionDetail.  # noqa: E501
        :type: str
        """

        self._promotion_id = promotion_id

    @property
    def promotion_image_url(self):
        """Gets the promotion_image_url of this PromotionDetail.  # noqa: E501

        Required for CODED_COUPON, MARKDOWN_SALE, and ORDER_DISCOUNT promotions, and not applicable for <b>VOLUME_DISCOUNT</b> promotions, this field is a URL that points to an image for the promotion. This image is displayed on the seller's <b>All Offers</b> page. The URL must point to either JPEG or PNG image and it must be a minimum of 500x500 pixels in dimension and cannot exceed 12Mb in size.  # noqa: E501

        :return: The promotion_image_url of this PromotionDetail.  # noqa: E501
        :rtype: str
        """
        return self._promotion_image_url

    @promotion_image_url.setter
    def promotion_image_url(self, promotion_image_url):
        """Sets the promotion_image_url of this PromotionDetail.

        Required for CODED_COUPON, MARKDOWN_SALE, and ORDER_DISCOUNT promotions, and not applicable for <b>VOLUME_DISCOUNT</b> promotions, this field is a URL that points to an image for the promotion. This image is displayed on the seller's <b>All Offers</b> page. The URL must point to either JPEG or PNG image and it must be a minimum of 500x500 pixels in dimension and cannot exceed 12Mb in size.  # noqa: E501

        :param promotion_image_url: The promotion_image_url of this PromotionDetail.  # noqa: E501
        :type: str
        """

        self._promotion_image_url = promotion_image_url

    @property
    def promotion_status(self):
        """Gets the promotion_status of this PromotionDetail.  # noqa: E501

        The current status of the promotion. When creating a new promotion, you must set this value to either <code>DRAFT</code> or <code>SCHEDULED</code>. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/sme:PromotionStatusEnum'>eBay API documentation</a>  # noqa: E501

        :return: The promotion_status of this PromotionDetail.  # noqa: E501
        :rtype: str
        """
        return self._promotion_status

    @promotion_status.setter
    def promotion_status(self, promotion_status):
        """Sets the promotion_status of this PromotionDetail.

        The current status of the promotion. When creating a new promotion, you must set this value to either <code>DRAFT</code> or <code>SCHEDULED</code>. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/sme:PromotionStatusEnum'>eBay API documentation</a>  # noqa: E501

        :param promotion_status: The promotion_status of this PromotionDetail.  # noqa: E501
        :type: str
        """

        self._promotion_status = promotion_status

    @property
    def promotion_type(self):
        """Gets the promotion_type of this PromotionDetail.  # noqa: E501

        Indicates type of the promotion, either <code>CODED_COUPON</code>, <code>MARKDOWN_SALE</code>, <code>ORDER_DISCOUNT</code>, or <code>VOLUME_DISCOUNT</code>. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/sme:PromotionTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The promotion_type of this PromotionDetail.  # noqa: E501
        :rtype: str
        """
        return self._promotion_type

    @promotion_type.setter
    def promotion_type(self, promotion_type):
        """Sets the promotion_type of this PromotionDetail.

        Indicates type of the promotion, either <code>CODED_COUPON</code>, <code>MARKDOWN_SALE</code>, <code>ORDER_DISCOUNT</code>, or <code>VOLUME_DISCOUNT</code>. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/sme:PromotionTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param promotion_type: The promotion_type of this PromotionDetail.  # noqa: E501
        :type: str
        """

        self._promotion_type = promotion_type

    @property
    def start_date(self):
        """Gets the start_date of this PromotionDetail.  # noqa: E501

        The date and time the promotion starts in UTC format (<code>yyyy-MM-ddThh:mm:ssZ</code>). For display purposes, convert this time into the local time of the seller.  # noqa: E501

        :return: The start_date of this PromotionDetail.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this PromotionDetail.

        The date and time the promotion starts in UTC format (<code>yyyy-MM-ddThh:mm:ssZ</code>). For display purposes, convert this time into the local time of the seller.  # noqa: E501

        :param start_date: The start_date of this PromotionDetail.  # noqa: E501
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
        if issubclass(PromotionDetail, dict):
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
        if not isinstance(other, PromotionDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
