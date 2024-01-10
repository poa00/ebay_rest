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

class GetEmailCampaignsResponse(object):
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
        'campaigns': 'list[CampaignDTO]',
        'href': 'str',
        'limit': 'int',
        'next': 'str',
        'offset': 'int',
        'prev': 'str',
        'total': 'int'
    }

    attribute_map = {
        'campaigns': 'campaigns',
        'href': 'href',
        'limit': 'limit',
        'next': 'next',
        'offset': 'offset',
        'prev': 'prev',
        'total': 'total'
    }

    def __init__(self, campaigns=None, href=None, limit=None, next=None, offset=None, prev=None, total=None):  # noqa: E501
        """GetEmailCampaignsResponse - a model defined in Swagger"""  # noqa: E501
        self._campaigns = None
        self._href = None
        self._limit = None
        self._next = None
        self._offset = None
        self._prev = None
        self._total = None
        self.discriminator = None
        if campaigns is not None:
            self.campaigns = campaigns
        if href is not None:
            self.href = href
        if limit is not None:
            self.limit = limit
        if next is not None:
            self.next = next
        if offset is not None:
            self.offset = offset
        if prev is not None:
            self.prev = prev
        if total is not None:
            self.total = total

    @property
    def campaigns(self):
        """Gets the campaigns of this GetEmailCampaignsResponse.  # noqa: E501

        A list of email campaigns that match the search criteria.  # noqa: E501

        :return: The campaigns of this GetEmailCampaignsResponse.  # noqa: E501
        :rtype: list[CampaignDTO]
        """
        return self._campaigns

    @campaigns.setter
    def campaigns(self, campaigns):
        """Sets the campaigns of this GetEmailCampaignsResponse.

        A list of email campaigns that match the search criteria.  # noqa: E501

        :param campaigns: The campaigns of this GetEmailCampaignsResponse.  # noqa: E501
        :type: list[CampaignDTO]
        """

        self._campaigns = campaigns

    @property
    def href(self):
        """Gets the href of this GetEmailCampaignsResponse.  # noqa: E501

        The URL to the current page of store email campaigns.  # noqa: E501

        :return: The href of this GetEmailCampaignsResponse.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this GetEmailCampaignsResponse.

        The URL to the current page of store email campaigns.  # noqa: E501

        :param href: The href of this GetEmailCampaignsResponse.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def limit(self):
        """Gets the limit of this GetEmailCampaignsResponse.  # noqa: E501

        The value of the limit parameter submitted in the request, which is the maximum number of store email campaigns to return on a page from the result set.  # noqa: E501

        :return: The limit of this GetEmailCampaignsResponse.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this GetEmailCampaignsResponse.

        The value of the limit parameter submitted in the request, which is the maximum number of store email campaigns to return on a page from the result set.  # noqa: E501

        :param limit: The limit of this GetEmailCampaignsResponse.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def next(self):
        """Gets the next of this GetEmailCampaignsResponse.  # noqa: E501

        The URI for the next page of results. This value is returned if there is an additional page of results to return from the result set.  # noqa: E501

        :return: The next of this GetEmailCampaignsResponse.  # noqa: E501
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this GetEmailCampaignsResponse.

        The URI for the next page of results. This value is returned if there is an additional page of results to return from the result set.  # noqa: E501

        :param next: The next of this GetEmailCampaignsResponse.  # noqa: E501
        :type: str
        """

        self._next = next

    @property
    def offset(self):
        """Gets the offset of this GetEmailCampaignsResponse.  # noqa: E501

        This value indicates the offset used for current page of store email campaigns being returned.  # noqa: E501

        :return: The offset of this GetEmailCampaignsResponse.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this GetEmailCampaignsResponse.

        This value indicates the offset used for current page of store email campaigns being returned.  # noqa: E501

        :param offset: The offset of this GetEmailCampaignsResponse.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def prev(self):
        """Gets the prev of this GetEmailCampaignsResponse.  # noqa: E501

        The URI for the previous page of results. This is returned if there is a previous page of results from the result set.  # noqa: E501

        :return: The prev of this GetEmailCampaignsResponse.  # noqa: E501
        :rtype: str
        """
        return self._prev

    @prev.setter
    def prev(self, prev):
        """Sets the prev of this GetEmailCampaignsResponse.

        The URI for the previous page of results. This is returned if there is a previous page of results from the result set.  # noqa: E501

        :param prev: The prev of this GetEmailCampaignsResponse.  # noqa: E501
        :type: str
        """

        self._prev = prev

    @property
    def total(self):
        """Gets the total of this GetEmailCampaignsResponse.  # noqa: E501

        Total number of available results returned under the filter criteria submitted in the request.  # noqa: E501

        :return: The total of this GetEmailCampaignsResponse.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this GetEmailCampaignsResponse.

        Total number of available results returned under the filter criteria submitted in the request.  # noqa: E501

        :param total: The total of this GetEmailCampaignsResponse.  # noqa: E501
        :type: int
        """

        self._total = total

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
        if issubclass(GetEmailCampaignsResponse, dict):
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
        if not isinstance(other, GetEmailCampaignsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
