# coding: utf-8

"""
    Marketing API

    <p>The <i>Marketing API </i> offers two platforms that sellers can use to promote and advertise their products:</p> <ul><li><b>Promoted Listings</b> is an eBay ad service that lets sellers set up <i>ad campaigns </i> for the products they want to promote. eBay displays the ads in search results and in other marketing modules as <b>SPONSORED</b> listings. If an item in a Promoted Listings campaign sells, the seller is assessed a Promoted Listings fee, which is a seller-specified percentage applied to the sales price. For complete details, refer to the <a href=\"/api-docs/sell/static/marketing/pl-landing.html\">Promoted Listings playbook</a>.</li><li><b>Promotions Manager</b> gives sellers a way to offer discounts on specific items as a way to attract buyers to their inventory. Sellers can set up discounts (such as \"20% off\" and other types of offers) on specific items or on an entire customer order. To further attract buyers, eBay prominently displays promotion <i>teasers</i> throughout buyer flows. For complete details, see <a href=\"/api-docs/sell/static/marketing/promotions-manager.html\">Promotions Manager</a>.</li></ul>  <p><b>Marketing reports</b>, on both the Promoted Listings and Promotions Manager platforms, give sellers information that shows the effectiveness of their marketing strategies. The data gives sellers the ability to review and fine tune their marketing efforts.</p><p><b>Store Email Campaign</b> allows sellers to create and send email campaigns to customers who have signed up to receive their newsletter. For more information on email campaigns, see <a href=\"/api-docs/sell/static/marketing/store-email-campaigns.html#email-campain-types\" target=\"_blank\">Store Email Campaigns</a>.<p class=\"tablenote\"><b>Important!</b> Sellers must have an active eBay Store subscription, and they must accept the <b>Terms and Conditions</b> before they can make requests to these APIs in the Production environment. There are also site-specific listings requirements and restrictions associated with these marketing tools, as listed in the \"requirements and restrictions\" sections for <a href=\"/api-docs/sell/marketing/static/overview.html#PL-requirements\">Promoted Listings</a> and <a href=\"/api-docs/sell/marketing/static/overview.html#PM-requirements\">Promotions Manager</a>.</p> <p>The table below lists all the Marketing API calls grouped by resource.</p>  # noqa: E501

    OpenAPI spec version: v1.21.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CouponConfiguration(object):
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
        'coupon_type': 'str',
        'max_coupon_redemption_per_user': 'int'
    }

    attribute_map = {
        'coupon_code': 'couponCode',
        'coupon_type': 'couponType',
        'max_coupon_redemption_per_user': 'maxCouponRedemptionPerUser'
    }

    def __init__(self, coupon_code=None, coupon_type=None, max_coupon_redemption_per_user=None):  # noqa: E501
        """CouponConfiguration - a model defined in Swagger"""  # noqa: E501
        self._coupon_code = None
        self._coupon_type = None
        self._max_coupon_redemption_per_user = None
        self.discriminator = None
        if coupon_code is not None:
            self.coupon_code = coupon_code
        if coupon_type is not None:
            self.coupon_type = coupon_type
        if max_coupon_redemption_per_user is not None:
            self.max_coupon_redemption_per_user = max_coupon_redemption_per_user

    @property
    def coupon_code(self):
        """Gets the coupon_code of this CouponConfiguration.  # noqa: E501

        A unique code that buyers can use during checkout to receive a discount. The code must be unique across eBay. <br><br>The code must be from 8-15 alphanumeric characters and can contain no more than two dashes ( - ).<br><br>This is required when the promotion type is CODED_COUPON.  # noqa: E501

        :return: The coupon_code of this CouponConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._coupon_code

    @coupon_code.setter
    def coupon_code(self, coupon_code):
        """Sets the coupon_code of this CouponConfiguration.

        A unique code that buyers can use during checkout to receive a discount. The code must be unique across eBay. <br><br>The code must be from 8-15 alphanumeric characters and can contain no more than two dashes ( - ).<br><br>This is required when the promotion type is CODED_COUPON.  # noqa: E501

        :param coupon_code: The coupon_code of this CouponConfiguration.  # noqa: E501
        :type: str
        """

        self._coupon_code = coupon_code

    @property
    def coupon_type(self):
        """Gets the coupon_type of this CouponConfiguration.  # noqa: E501

        This indicates the type of Coded Coupon promotion, and is required when the promotion type is <b>CODED_COUPON</b>.<br><br>Supported types:<ul><li><b>PRIVATE_SINGLE_SELLER_COUPON:</b> Anyone can use and share the coupon code, but it isn't posted on eBay.</li><li><b>PUBLIC_SINGLE_SELLER_COUPON:</b> Anyone can find the coupon code on eBay and use it.</li></ul> For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/sme:CouponTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The coupon_type of this CouponConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._coupon_type

    @coupon_type.setter
    def coupon_type(self, coupon_type):
        """Sets the coupon_type of this CouponConfiguration.

        This indicates the type of Coded Coupon promotion, and is required when the promotion type is <b>CODED_COUPON</b>.<br><br>Supported types:<ul><li><b>PRIVATE_SINGLE_SELLER_COUPON:</b> Anyone can use and share the coupon code, but it isn't posted on eBay.</li><li><b>PUBLIC_SINGLE_SELLER_COUPON:</b> Anyone can find the coupon code on eBay and use it.</li></ul> For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/sme:CouponTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param coupon_type: The coupon_type of this CouponConfiguration.  # noqa: E501
        :type: str
        """

        self._coupon_type = coupon_type

    @property
    def max_coupon_redemption_per_user(self):
        """Gets the max_coupon_redemption_per_user of this CouponConfiguration.  # noqa: E501

        This sets the limit on the number of times a buyer can use this coupon. The range of values is 1-10. If no value is provided, a buyer can use the coupon an unlimited number of times.  # noqa: E501

        :return: The max_coupon_redemption_per_user of this CouponConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._max_coupon_redemption_per_user

    @max_coupon_redemption_per_user.setter
    def max_coupon_redemption_per_user(self, max_coupon_redemption_per_user):
        """Sets the max_coupon_redemption_per_user of this CouponConfiguration.

        This sets the limit on the number of times a buyer can use this coupon. The range of values is 1-10. If no value is provided, a buyer can use the coupon an unlimited number of times.  # noqa: E501

        :param max_coupon_redemption_per_user: The max_coupon_redemption_per_user of this CouponConfiguration.  # noqa: E501
        :type: int
        """

        self._max_coupon_redemption_per_user = max_coupon_redemption_per_user

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
        if issubclass(CouponConfiguration, dict):
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
        if not isinstance(other, CouponConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
