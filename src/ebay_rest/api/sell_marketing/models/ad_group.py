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

class AdGroup(object):
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
        'ad_group_status': 'str',
        'default_bid': 'Amount',
        'name': 'str'
    }

    attribute_map = {
        'ad_group_id': 'adGroupId',
        'ad_group_status': 'adGroupStatus',
        'default_bid': 'defaultBid',
        'name': 'name'
    }

    def __init__(self, ad_group_id=None, ad_group_status=None, default_bid=None, name=None):  # noqa: E501
        """AdGroup - a model defined in Swagger"""  # noqa: E501
        self._ad_group_id = None
        self._ad_group_status = None
        self._default_bid = None
        self._name = None
        self.discriminator = None
        if ad_group_id is not None:
            self.ad_group_id = ad_group_id
        if ad_group_status is not None:
            self.ad_group_status = ad_group_status
        if default_bid is not None:
            self.default_bid = default_bid
        if name is not None:
            self.name = name

    @property
    def ad_group_id(self):
        """Gets the ad_group_id of this AdGroup.  # noqa: E501

        A unique eBay-assigned ID for an ad group in a campaign that uses the Cost Per Click (CPC) funding model.  # noqa: E501

        :return: The ad_group_id of this AdGroup.  # noqa: E501
        :rtype: str
        """
        return self._ad_group_id

    @ad_group_id.setter
    def ad_group_id(self, ad_group_id):
        """Sets the ad_group_id of this AdGroup.

        A unique eBay-assigned ID for an ad group in a campaign that uses the Cost Per Click (CPC) funding model.  # noqa: E501

        :param ad_group_id: The ad_group_id of this AdGroup.  # noqa: E501
        :type: str
        """

        self._ad_group_id = ad_group_id

    @property
    def ad_group_status(self):
        """Gets the ad_group_status of this AdGroup.  # noqa: E501

        An enumeration value representing the current status of the ad group.<br /><br /><b>Valid Values:</b><ul><li><code>ACTIVE</code></li><li><code>PAUSED</code></li><li><code>ARCHIVED</code></li></ul> For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/pls:AdGroupStatusEnum'>eBay API documentation</a>  # noqa: E501

        :return: The ad_group_status of this AdGroup.  # noqa: E501
        :rtype: str
        """
        return self._ad_group_status

    @ad_group_status.setter
    def ad_group_status(self, ad_group_status):
        """Sets the ad_group_status of this AdGroup.

        An enumeration value representing the current status of the ad group.<br /><br /><b>Valid Values:</b><ul><li><code>ACTIVE</code></li><li><code>PAUSED</code></li><li><code>ARCHIVED</code></li></ul> For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/pls:AdGroupStatusEnum'>eBay API documentation</a>  # noqa: E501

        :param ad_group_status: The ad_group_status of this AdGroup.  # noqa: E501
        :type: str
        """

        self._ad_group_status = ad_group_status

    @property
    def default_bid(self):
        """Gets the default_bid of this AdGroup.  # noqa: E501


        :return: The default_bid of this AdGroup.  # noqa: E501
        :rtype: Amount
        """
        return self._default_bid

    @default_bid.setter
    def default_bid(self, default_bid):
        """Sets the default_bid of this AdGroup.


        :param default_bid: The default_bid of this AdGroup.  # noqa: E501
        :type: Amount
        """

        self._default_bid = default_bid

    @property
    def name(self):
        """Gets the name of this AdGroup.  # noqa: E501

        The seller-defined name of the ad group.  # noqa: E501

        :return: The name of this AdGroup.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AdGroup.

        The seller-defined name of the ad group.  # noqa: E501

        :param name: The name of this AdGroup.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(AdGroup, dict):
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
        if not isinstance(other, AdGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
