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

class NegativeKeyword(object):
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
        'campaign_id': 'str',
        'negative_keyword_id': 'str',
        'negative_keyword_match_type': 'str',
        'negative_keyword_status': 'str',
        'negative_keyword_text': 'str'
    }

    attribute_map = {
        'ad_group_id': 'adGroupId',
        'campaign_id': 'campaignId',
        'negative_keyword_id': 'negativeKeywordId',
        'negative_keyword_match_type': 'negativeKeywordMatchType',
        'negative_keyword_status': 'negativeKeywordStatus',
        'negative_keyword_text': 'negativeKeywordText'
    }

    def __init__(self, ad_group_id=None, campaign_id=None, negative_keyword_id=None, negative_keyword_match_type=None, negative_keyword_status=None, negative_keyword_text=None):  # noqa: E501
        """NegativeKeyword - a model defined in Swagger"""  # noqa: E501
        self._ad_group_id = None
        self._campaign_id = None
        self._negative_keyword_id = None
        self._negative_keyword_match_type = None
        self._negative_keyword_status = None
        self._negative_keyword_text = None
        self.discriminator = None
        if ad_group_id is not None:
            self.ad_group_id = ad_group_id
        if campaign_id is not None:
            self.campaign_id = campaign_id
        if negative_keyword_id is not None:
            self.negative_keyword_id = negative_keyword_id
        if negative_keyword_match_type is not None:
            self.negative_keyword_match_type = negative_keyword_match_type
        if negative_keyword_status is not None:
            self.negative_keyword_status = negative_keyword_status
        if negative_keyword_text is not None:
            self.negative_keyword_text = negative_keyword_text

    @property
    def ad_group_id(self):
        """Gets the ad_group_id of this NegativeKeyword.  # noqa: E501

        An ad group ID that is generated when an ad group is first created and associated with a campaign.<br /><br /><span class=\"tablenote\"><b>Note:</b> You can call the  <a href=\"/api-docs/sell/marketing/resources/adgroup/methods/getAdGroups\">getAdGroups</a> method to retrieve the ad group IDs for a seller.</span>  # noqa: E501

        :return: The ad_group_id of this NegativeKeyword.  # noqa: E501
        :rtype: str
        """
        return self._ad_group_id

    @ad_group_id.setter
    def ad_group_id(self, ad_group_id):
        """Sets the ad_group_id of this NegativeKeyword.

        An ad group ID that is generated when an ad group is first created and associated with a campaign.<br /><br /><span class=\"tablenote\"><b>Note:</b> You can call the  <a href=\"/api-docs/sell/marketing/resources/adgroup/methods/getAdGroups\">getAdGroups</a> method to retrieve the ad group IDs for a seller.</span>  # noqa: E501

        :param ad_group_id: The ad_group_id of this NegativeKeyword.  # noqa: E501
        :type: str
        """

        self._ad_group_id = ad_group_id

    @property
    def campaign_id(self):
        """Gets the campaign_id of this NegativeKeyword.  # noqa: E501

        A unique eBay-assigned ID for a campaign. This ID is generated when a campaign is created.  # noqa: E501

        :return: The campaign_id of this NegativeKeyword.  # noqa: E501
        :rtype: str
        """
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, campaign_id):
        """Sets the campaign_id of this NegativeKeyword.

        A unique eBay-assigned ID for a campaign. This ID is generated when a campaign is created.  # noqa: E501

        :param campaign_id: The campaign_id of this NegativeKeyword.  # noqa: E501
        :type: str
        """

        self._campaign_id = campaign_id

    @property
    def negative_keyword_id(self):
        """Gets the negative_keyword_id of this NegativeKeyword.  # noqa: E501

        A unique eBay-assigned ID for a negative keyword. This keyword ID will be generated for each successfully created negative keyword.  # noqa: E501

        :return: The negative_keyword_id of this NegativeKeyword.  # noqa: E501
        :rtype: str
        """
        return self._negative_keyword_id

    @negative_keyword_id.setter
    def negative_keyword_id(self, negative_keyword_id):
        """Sets the negative_keyword_id of this NegativeKeyword.

        A unique eBay-assigned ID for a negative keyword. This keyword ID will be generated for each successfully created negative keyword.  # noqa: E501

        :param negative_keyword_id: The negative_keyword_id of this NegativeKeyword.  # noqa: E501
        :type: str
        """

        self._negative_keyword_id = negative_keyword_id

    @property
    def negative_keyword_match_type(self):
        """Gets the negative_keyword_match_type of this NegativeKeyword.  # noqa: E501

        A field that defines the match type for the negative keyword.<br /><br /><span class=\"tablenote\"><span style=\"color:#004680\"><strong>Note:</strong></span> Broad matching of negative keywords is not currently supported.</span><br /><b>Valid Values:</b><ul><li><code>EXACT</code></li><li><code>PHRASE</code></li></ul> For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/pls:NegativeKeywordMatchTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The negative_keyword_match_type of this NegativeKeyword.  # noqa: E501
        :rtype: str
        """
        return self._negative_keyword_match_type

    @negative_keyword_match_type.setter
    def negative_keyword_match_type(self, negative_keyword_match_type):
        """Sets the negative_keyword_match_type of this NegativeKeyword.

        A field that defines the match type for the negative keyword.<br /><br /><span class=\"tablenote\"><span style=\"color:#004680\"><strong>Note:</strong></span> Broad matching of negative keywords is not currently supported.</span><br /><b>Valid Values:</b><ul><li><code>EXACT</code></li><li><code>PHRASE</code></li></ul> For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/pls:NegativeKeywordMatchTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param negative_keyword_match_type: The negative_keyword_match_type of this NegativeKeyword.  # noqa: E501
        :type: str
        """

        self._negative_keyword_match_type = negative_keyword_match_type

    @property
    def negative_keyword_status(self):
        """Gets the negative_keyword_status of this NegativeKeyword.  # noqa: E501

        A field that defines the status of the negative keyword. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/pls:NegativeKeywordStatusEnum'>eBay API documentation</a>  # noqa: E501

        :return: The negative_keyword_status of this NegativeKeyword.  # noqa: E501
        :rtype: str
        """
        return self._negative_keyword_status

    @negative_keyword_status.setter
    def negative_keyword_status(self, negative_keyword_status):
        """Sets the negative_keyword_status of this NegativeKeyword.

        A field that defines the status of the negative keyword. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/pls:NegativeKeywordStatusEnum'>eBay API documentation</a>  # noqa: E501

        :param negative_keyword_status: The negative_keyword_status of this NegativeKeyword.  # noqa: E501
        :type: str
        """

        self._negative_keyword_status = negative_keyword_status

    @property
    def negative_keyword_text(self):
        """Gets the negative_keyword_text of this NegativeKeyword.  # noqa: E501

        The text for the negative keyword.  # noqa: E501

        :return: The negative_keyword_text of this NegativeKeyword.  # noqa: E501
        :rtype: str
        """
        return self._negative_keyword_text

    @negative_keyword_text.setter
    def negative_keyword_text(self, negative_keyword_text):
        """Sets the negative_keyword_text of this NegativeKeyword.

        The text for the negative keyword.  # noqa: E501

        :param negative_keyword_text: The negative_keyword_text of this NegativeKeyword.  # noqa: E501
        :type: str
        """

        self._negative_keyword_text = negative_keyword_text

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
        if issubclass(NegativeKeyword, dict):
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
        if not isinstance(other, NegativeKeyword):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other