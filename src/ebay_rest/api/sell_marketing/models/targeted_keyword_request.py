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

class TargetedKeywordRequest(object):
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
        'additional_info': 'list[str]',
        'exclusions': 'list[str]',
        'listing_ids': 'list[str]',
        'match_type': 'str'
    }

    attribute_map = {
        'additional_info': 'additionalInfo',
        'exclusions': 'exclusions',
        'listing_ids': 'listingIds',
        'match_type': 'matchType'
    }

    def __init__(self, additional_info=None, exclusions=None, listing_ids=None, match_type=None):  # noqa: E501
        """TargetedKeywordRequest - a model defined in Swagger"""  # noqa: E501
        self._additional_info = None
        self._exclusions = None
        self._listing_ids = None
        self._match_type = None
        self.discriminator = None
        if additional_info is not None:
            self.additional_info = additional_info
        if exclusions is not None:
            self.exclusions = exclusions
        if listing_ids is not None:
            self.listing_ids = listing_ids
        if match_type is not None:
            self.match_type = match_type

    @property
    def additional_info(self):
        """Gets the additional_info of this TargetedKeywordRequest.  # noqa: E501

        A field used to indicate whether additional information and insight data shall be provided for suggested keywords.<br><br>Use this array to retrieve keyword insights, including active seller count and search volume.<br /><br /><strong>Valid Value:</strong> <code>KEYWORD_INSIGHTS</code>  # noqa: E501

        :return: The additional_info of this TargetedKeywordRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this TargetedKeywordRequest.

        A field used to indicate whether additional information and insight data shall be provided for suggested keywords.<br><br>Use this array to retrieve keyword insights, including active seller count and search volume.<br /><br /><strong>Valid Value:</strong> <code>KEYWORD_INSIGHTS</code>  # noqa: E501

        :param additional_info: The additional_info of this TargetedKeywordRequest.  # noqa: E501
        :type: list[str]
        """

        self._additional_info = additional_info

    @property
    def exclusions(self):
        """Gets the exclusions of this TargetedKeywordRequest.  # noqa: E501

        A field used to indicate that the keywords already selected by sellers for the specified listing IDs should be filtered out of the response, and only new and unique keyword recommendations shall be returned.<br /><br /><strong>Valid Value:</strong> <code>ADOPTED_KEYWORDS</code>  # noqa: E501

        :return: The exclusions of this TargetedKeywordRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._exclusions

    @exclusions.setter
    def exclusions(self, exclusions):
        """Sets the exclusions of this TargetedKeywordRequest.

        A field used to indicate that the keywords already selected by sellers for the specified listing IDs should be filtered out of the response, and only new and unique keyword recommendations shall be returned.<br /><br /><strong>Valid Value:</strong> <code>ADOPTED_KEYWORDS</code>  # noqa: E501

        :param exclusions: The exclusions of this TargetedKeywordRequest.  # noqa: E501
        :type: list[str]
        """

        self._exclusions = exclusions

    @property
    def listing_ids(self):
        """Gets the listing_ids of this TargetedKeywordRequest.  # noqa: E501

        A set of comma-separated listing IDs for the specific listings you wish to retrieve suggested keywords. <br /><br /><b>Maximum number of listings requested: </b>300  # noqa: E501

        :return: The listing_ids of this TargetedKeywordRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._listing_ids

    @listing_ids.setter
    def listing_ids(self, listing_ids):
        """Sets the listing_ids of this TargetedKeywordRequest.

        A set of comma-separated listing IDs for the specific listings you wish to retrieve suggested keywords. <br /><br /><b>Maximum number of listings requested: </b>300  # noqa: E501

        :param listing_ids: The listing_ids of this TargetedKeywordRequest.  # noqa: E501
        :type: list[str]
        """

        self._listing_ids = listing_ids

    @property
    def match_type(self):
        """Gets the match_type of this TargetedKeywordRequest.  # noqa: E501

        A field that defines the match type for the keyword.<br /><br /><b>Valid Values:</b><ul><li><code>BROAD</code></li><li><code>EXACT</code></li><li><code>PHRASE</code></li></ul> For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/pls:MatchTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The match_type of this TargetedKeywordRequest.  # noqa: E501
        :rtype: str
        """
        return self._match_type

    @match_type.setter
    def match_type(self, match_type):
        """Sets the match_type of this TargetedKeywordRequest.

        A field that defines the match type for the keyword.<br /><br /><b>Valid Values:</b><ul><li><code>BROAD</code></li><li><code>EXACT</code></li><li><code>PHRASE</code></li></ul> For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/pls:MatchTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param match_type: The match_type of this TargetedKeywordRequest.  # noqa: E501
        :type: str
        """

        self._match_type = match_type

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
        if issubclass(TargetedKeywordRequest, dict):
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
        if not isinstance(other, TargetedKeywordRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
