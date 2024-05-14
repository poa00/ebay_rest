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

class GetEmailPreviewResponse(object):
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
        'content': 'str',
        'render_date': 'str'
    }

    attribute_map = {
        'content': 'content',
        'render_date': 'renderDate'
    }

    def __init__(self, content=None, render_date=None):  # noqa: E501
        """GetEmailPreviewResponse - a model defined in Swagger"""  # noqa: E501
        self._content = None
        self._render_date = None
        self.discriminator = None
        if content is not None:
            self.content = content
        if render_date is not None:
            self.render_date = render_date

    @property
    def content(self):
        """Gets the content of this GetEmailPreviewResponse.  # noqa: E501

        The raw HTML code of the email campaign contents. The client side can use this HTML output directly.<br><br>Because the contents of an email campaign are subject to change, these contents are a \"snapshot\" of the email campaign at a specific time and date, indicated by the <b>renderDate</b> field.  # noqa: E501

        :return: The content of this GetEmailPreviewResponse.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this GetEmailPreviewResponse.

        The raw HTML code of the email campaign contents. The client side can use this HTML output directly.<br><br>Because the contents of an email campaign are subject to change, these contents are a \"snapshot\" of the email campaign at a specific time and date, indicated by the <b>renderDate</b> field.  # noqa: E501

        :param content: The content of this GetEmailPreviewResponse.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def render_date(self):
        """Gets the render_date of this GetEmailPreviewResponse.  # noqa: E501

        The date and time when a \"snapshot\" of the email campaign contents contained in the <b>content</b> result was taken. Given in UTC format.  # noqa: E501

        :return: The render_date of this GetEmailPreviewResponse.  # noqa: E501
        :rtype: str
        """
        return self._render_date

    @render_date.setter
    def render_date(self, render_date):
        """Sets the render_date of this GetEmailPreviewResponse.

        The date and time when a \"snapshot\" of the email campaign contents contained in the <b>content</b> result was taken. Given in UTC format.  # noqa: E501

        :param render_date: The render_date of this GetEmailPreviewResponse.  # noqa: E501
        :type: str
        """

        self._render_date = render_date

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
        if issubclass(GetEmailPreviewResponse, dict):
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
        if not isinstance(other, GetEmailPreviewResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
