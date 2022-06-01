# coding: utf-8

"""
    Marketing API

    <p>The <i>Marketing API </i> offers two platforms that sellers can use to promote and advertise their products:</p> <ul><li><b>Promoted Listings</b> is an eBay ad service that lets sellers set up <i>ad campaigns </i> for the products they want to promote. eBay displays the ads in search results and in other marketing modules as <b>SPONSORED</b> listings. If an item in a Promoted Listings campaign sells, the seller is assessed a Promoted Listings fee, which is a seller-specified percentage applied to the sales price. For complete details, see <a href=\"/api-docs/sell/static/marketing/promoted-listings.html\">Promoted Listings</a>.</li>  <li><b>Promotions Manager</b> gives sellers a way to offer discounts on specific items as a way to attract buyers to their inventory. Sellers can set up discounts (such as \"20% off\" and other types of offers) on specific items or on an entire customer order. To further attract buyers, eBay prominently displays promotion <i>teasers</i> throughout buyer flows. For complete details, see <a href=\"/api-docs/sell/static/marketing/promotions-manager.html\">Promotions Manager</a>.</li></ul>  <p><b>Marketing reports</b>, on both the Promoted Listings and Promotions Manager platforms, give sellers information that shows the effectiveness of their marketing strategies. The data gives sellers the ability to review and fine tune their marketing efforts.</p> <p class=\"tablenote\"><b>Important!</b> Sellers must have an active eBay Store subscription, and they must accept the <b>Terms and Conditions</b> before they can make requests to these APIs in the Production environment. There are also site-specific listings requirements and restrictions associated with these marketing tools, as listed in the \"requirements and restrictions\" sections for <a href=\"/api-docs/sell/marketing/static/overview.html#PL-requirements\">Promoted Listings</a> and <a href=\"/api-docs/sell/marketing/static/overview.html#PM-requirements\">Promotions Manager</a>.</p> <p>The table below lists all the Marketing API calls grouped by resource.</p>  # noqa: E501

    OpenAPI spec version: v1.10.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SummaryReportResponse(object):
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
        'base_sale': 'Amount',
        'last_updated': 'str',
        'percentage_sales_lift': 'str',
        'promotion_sale': 'Amount',
        'total_sale': 'Amount'
    }

    attribute_map = {
        'base_sale': 'baseSale',
        'last_updated': 'lastUpdated',
        'percentage_sales_lift': 'percentageSalesLift',
        'promotion_sale': 'promotionSale',
        'total_sale': 'totalSale'
    }

    def __init__(self, base_sale=None, last_updated=None, percentage_sales_lift=None, promotion_sale=None, total_sale=None):  # noqa: E501
        """SummaryReportResponse - a model defined in Swagger"""  # noqa: E501
        self._base_sale = None
        self._last_updated = None
        self._percentage_sales_lift = None
        self._promotion_sale = None
        self._total_sale = None
        self.discriminator = None
        if base_sale is not None:
            self.base_sale = base_sale
        if last_updated is not None:
            self.last_updated = last_updated
        if percentage_sales_lift is not None:
            self.percentage_sales_lift = percentage_sales_lift
        if promotion_sale is not None:
            self.promotion_sale = promotion_sale
        if total_sale is not None:
            self.total_sale = total_sale

    @property
    def base_sale(self):
        """Gets the base_sale of this SummaryReportResponse.  # noqa: E501


        :return: The base_sale of this SummaryReportResponse.  # noqa: E501
        :rtype: Amount
        """
        return self._base_sale

    @base_sale.setter
    def base_sale(self, base_sale):
        """Sets the base_sale of this SummaryReportResponse.


        :param base_sale: The base_sale of this SummaryReportResponse.  # noqa: E501
        :type: Amount
        """

        self._base_sale = base_sale

    @property
    def last_updated(self):
        """Gets the last_updated of this SummaryReportResponse.  # noqa: E501

        The date the report was generated.  # noqa: E501

        :return: The last_updated of this SummaryReportResponse.  # noqa: E501
        :rtype: str
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this SummaryReportResponse.

        The date the report was generated.  # noqa: E501

        :param last_updated: The last_updated of this SummaryReportResponse.  # noqa: E501
        :type: str
        """

        self._last_updated = last_updated

    @property
    def percentage_sales_lift(self):
        """Gets the percentage_sales_lift of this SummaryReportResponse.  # noqa: E501

        The percentage of the total dollar amount gained due to promotions. This value is calculated as follows:  <br><br><b>precentageSalesLift</b> = <b>promotionSale</b> / (<b>baseSale</b> + <b>promotionSale</b>)  # noqa: E501

        :return: The percentage_sales_lift of this SummaryReportResponse.  # noqa: E501
        :rtype: str
        """
        return self._percentage_sales_lift

    @percentage_sales_lift.setter
    def percentage_sales_lift(self, percentage_sales_lift):
        """Sets the percentage_sales_lift of this SummaryReportResponse.

        The percentage of the total dollar amount gained due to promotions. This value is calculated as follows:  <br><br><b>precentageSalesLift</b> = <b>promotionSale</b> / (<b>baseSale</b> + <b>promotionSale</b>)  # noqa: E501

        :param percentage_sales_lift: The percentage_sales_lift of this SummaryReportResponse.  # noqa: E501
        :type: str
        """

        self._percentage_sales_lift = percentage_sales_lift

    @property
    def promotion_sale(self):
        """Gets the promotion_sale of this SummaryReportResponse.  # noqa: E501


        :return: The promotion_sale of this SummaryReportResponse.  # noqa: E501
        :rtype: Amount
        """
        return self._promotion_sale

    @promotion_sale.setter
    def promotion_sale(self, promotion_sale):
        """Sets the promotion_sale of this SummaryReportResponse.


        :param promotion_sale: The promotion_sale of this SummaryReportResponse.  # noqa: E501
        :type: Amount
        """

        self._promotion_sale = promotion_sale

    @property
    def total_sale(self):
        """Gets the total_sale of this SummaryReportResponse.  # noqa: E501


        :return: The total_sale of this SummaryReportResponse.  # noqa: E501
        :rtype: Amount
        """
        return self._total_sale

    @total_sale.setter
    def total_sale(self, total_sale):
        """Sets the total_sale of this SummaryReportResponse.


        :param total_sale: The total_sale of this SummaryReportResponse.  # noqa: E501
        :type: Amount
        """

        self._total_sale = total_sale

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
        if issubclass(SummaryReportResponse, dict):
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
        if not isinstance(other, SummaryReportResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
