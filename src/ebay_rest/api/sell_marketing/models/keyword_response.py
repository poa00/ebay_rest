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

class KeywordResponse(object):
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
        'errors': 'list[Error]',
        'href': 'str',
        'keyword_id': 'str',
        'keyword_text': 'str',
        'match_type': 'str',
        'status_code': 'int'
    }

    attribute_map = {
        'ad_group_id': 'adGroupId',
        'errors': 'errors',
        'href': 'href',
        'keyword_id': 'keywordId',
        'keyword_text': 'keywordText',
        'match_type': 'matchType',
        'status_code': 'statusCode'
    }

    def __init__(self, ad_group_id=None, errors=None, href=None, keyword_id=None, keyword_text=None, match_type=None, status_code=None):  # noqa: E501
        """KeywordResponse - a model defined in Swagger"""  # noqa: E501
        self._ad_group_id = None
        self._errors = None
        self._href = None
        self._keyword_id = None
        self._keyword_text = None
        self._match_type = None
        self._status_code = None
        self.discriminator = None
        if ad_group_id is not None:
            self.ad_group_id = ad_group_id
        if errors is not None:
            self.errors = errors
        if href is not None:
            self.href = href
        if keyword_id is not None:
            self.keyword_id = keyword_id
        if keyword_text is not None:
            self.keyword_text = keyword_text
        if match_type is not None:
            self.match_type = match_type
        if status_code is not None:
            self.status_code = status_code

    @property
    def ad_group_id(self):
        """Gets the ad_group_id of this KeywordResponse.  # noqa: E501

        The identifier of the ad group that the keyword was added to.  # noqa: E501

        :return: The ad_group_id of this KeywordResponse.  # noqa: E501
        :rtype: str
        """
        return self._ad_group_id

    @ad_group_id.setter
    def ad_group_id(self, ad_group_id):
        """Sets the ad_group_id of this KeywordResponse.

        The identifier of the ad group that the keyword was added to.  # noqa: E501

        :param ad_group_id: The ad_group_id of this KeywordResponse.  # noqa: E501
        :type: str
        """

        self._ad_group_id = ad_group_id

    @property
    def errors(self):
        """Gets the errors of this KeywordResponse.  # noqa: E501

        This container will be returned if there is an issue creating the corresponding keyword and/or adding that keyword to the corresponding ad group.  # noqa: E501

        :return: The errors of this KeywordResponse.  # noqa: E501
        :rtype: list[Error]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this KeywordResponse.

        This container will be returned if there is an issue creating the corresponding keyword and/or adding that keyword to the corresponding ad group.  # noqa: E501

        :param errors: The errors of this KeywordResponse.  # noqa: E501
        :type: list[Error]
        """

        self._errors = errors

    @property
    def href(self):
        """Gets the href of this KeywordResponse.  # noqa: E501

        The getKeyword URI for the keyword, which is used to retrieve the keyword. This URI will be returned for each successfully created keyword.  # noqa: E501

        :return: The href of this KeywordResponse.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this KeywordResponse.

        The getKeyword URI for the keyword, which is used to retrieve the keyword. This URI will be returned for each successfully created keyword.  # noqa: E501

        :param href: The href of this KeywordResponse.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def keyword_id(self):
        """Gets the keyword_id of this KeywordResponse.  # noqa: E501

        A unique eBay-assigned ID for a keyword that is generated for an ad group. This keyword ID will be generated for each successfully created keyword.  # noqa: E501

        :return: The keyword_id of this KeywordResponse.  # noqa: E501
        :rtype: str
        """
        return self._keyword_id

    @keyword_id.setter
    def keyword_id(self, keyword_id):
        """Sets the keyword_id of this KeywordResponse.

        A unique eBay-assigned ID for a keyword that is generated for an ad group. This keyword ID will be generated for each successfully created keyword.  # noqa: E501

        :param keyword_id: The keyword_id of this KeywordResponse.  # noqa: E501
        :type: str
        """

        self._keyword_id = keyword_id

    @property
    def keyword_text(self):
        """Gets the keyword_text of this KeywordResponse.  # noqa: E501

        The text of the keyword.  # noqa: E501

        :return: The keyword_text of this KeywordResponse.  # noqa: E501
        :rtype: str
        """
        return self._keyword_text

    @keyword_text.setter
    def keyword_text(self, keyword_text):
        """Sets the keyword_text of this KeywordResponse.

        The text of the keyword.  # noqa: E501

        :param keyword_text: The keyword_text of this KeywordResponse.  # noqa: E501
        :type: str
        """

        self._keyword_text = keyword_text

    @property
    def match_type(self):
        """Gets the match_type of this KeywordResponse.  # noqa: E501

        A field that defines the match type for the keyword.<br /><br /><span class=\"tablenote\"><span style=\"color:#004680\"><strong>Note:</strong></span> Broad matching of keywords is currently only supported in the AU marketplace.</span><br /><b>Valid Values:</b><ul><li><code>BROAD</code></li><li><code>EXACT</code></li><li><code>PHRASE</code></li></ul> For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/pls:MatchTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The match_type of this KeywordResponse.  # noqa: E501
        :rtype: str
        """
        return self._match_type

    @match_type.setter
    def match_type(self, match_type):
        """Sets the match_type of this KeywordResponse.

        A field that defines the match type for the keyword.<br /><br /><span class=\"tablenote\"><span style=\"color:#004680\"><strong>Note:</strong></span> Broad matching of keywords is currently only supported in the AU marketplace.</span><br /><b>Valid Values:</b><ul><li><code>BROAD</code></li><li><code>EXACT</code></li><li><code>PHRASE</code></li></ul> For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/pls:MatchTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param match_type: The match_type of this KeywordResponse.  # noqa: E501
        :type: str
        """

        self._match_type = match_type

    @property
    def status_code(self):
        """Gets the status_code of this KeywordResponse.  # noqa: E501

        An HTTP status code is returned for each keyword to indicate the success or failure of adding that keyword to the ad group.  # noqa: E501

        :return: The status_code of this KeywordResponse.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this KeywordResponse.

        An HTTP status code is returned for each keyword to indicate the success or failure of adding that keyword to the ad group.  # noqa: E501

        :param status_code: The status_code of this KeywordResponse.  # noqa: E501
        :type: int
        """

        self._status_code = status_code

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
        if issubclass(KeywordResponse, dict):
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
        if not isinstance(other, KeywordResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
