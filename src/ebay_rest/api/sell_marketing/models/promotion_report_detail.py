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

class PromotionReportDetail(object):
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
        'average_item_discount': 'Amount',
        'average_item_revenue': 'Amount',
        'average_order_discount': 'Amount',
        'average_order_revenue': 'Amount',
        'average_order_size': 'str',
        'base_sale': 'Amount',
        'items_sold_quantity': 'int',
        'number_of_orders_sold': 'int',
        'percentage_sales_lift': 'str',
        'promotion_href': 'str',
        'promotion_id': 'str',
        'promotion_report_id': 'str',
        'promotion_sale': 'Amount',
        'promotion_type': 'str',
        'total_discount': 'Amount',
        'total_sale': 'Amount'
    }

    attribute_map = {
        'average_item_discount': 'averageItemDiscount',
        'average_item_revenue': 'averageItemRevenue',
        'average_order_discount': 'averageOrderDiscount',
        'average_order_revenue': 'averageOrderRevenue',
        'average_order_size': 'averageOrderSize',
        'base_sale': 'baseSale',
        'items_sold_quantity': 'itemsSoldQuantity',
        'number_of_orders_sold': 'numberOfOrdersSold',
        'percentage_sales_lift': 'percentageSalesLift',
        'promotion_href': 'promotionHref',
        'promotion_id': 'promotionId',
        'promotion_report_id': 'promotionReportId',
        'promotion_sale': 'promotionSale',
        'promotion_type': 'promotionType',
        'total_discount': 'totalDiscount',
        'total_sale': 'totalSale'
    }

    def __init__(self, average_item_discount=None, average_item_revenue=None, average_order_discount=None, average_order_revenue=None, average_order_size=None, base_sale=None, items_sold_quantity=None, number_of_orders_sold=None, percentage_sales_lift=None, promotion_href=None, promotion_id=None, promotion_report_id=None, promotion_sale=None, promotion_type=None, total_discount=None, total_sale=None):  # noqa: E501
        """PromotionReportDetail - a model defined in Swagger"""  # noqa: E501
        self._average_item_discount = None
        self._average_item_revenue = None
        self._average_order_discount = None
        self._average_order_revenue = None
        self._average_order_size = None
        self._base_sale = None
        self._items_sold_quantity = None
        self._number_of_orders_sold = None
        self._percentage_sales_lift = None
        self._promotion_href = None
        self._promotion_id = None
        self._promotion_report_id = None
        self._promotion_sale = None
        self._promotion_type = None
        self._total_discount = None
        self._total_sale = None
        self.discriminator = None
        if average_item_discount is not None:
            self.average_item_discount = average_item_discount
        if average_item_revenue is not None:
            self.average_item_revenue = average_item_revenue
        if average_order_discount is not None:
            self.average_order_discount = average_order_discount
        if average_order_revenue is not None:
            self.average_order_revenue = average_order_revenue
        if average_order_size is not None:
            self.average_order_size = average_order_size
        if base_sale is not None:
            self.base_sale = base_sale
        if items_sold_quantity is not None:
            self.items_sold_quantity = items_sold_quantity
        if number_of_orders_sold is not None:
            self.number_of_orders_sold = number_of_orders_sold
        if percentage_sales_lift is not None:
            self.percentage_sales_lift = percentage_sales_lift
        if promotion_href is not None:
            self.promotion_href = promotion_href
        if promotion_id is not None:
            self.promotion_id = promotion_id
        if promotion_report_id is not None:
            self.promotion_report_id = promotion_report_id
        if promotion_sale is not None:
            self.promotion_sale = promotion_sale
        if promotion_type is not None:
            self.promotion_type = promotion_type
        if total_discount is not None:
            self.total_discount = total_discount
        if total_sale is not None:
            self.total_sale = total_sale

    @property
    def average_item_discount(self):
        """Gets the average_item_discount of this PromotionReportDetail.  # noqa: E501


        :return: The average_item_discount of this PromotionReportDetail.  # noqa: E501
        :rtype: Amount
        """
        return self._average_item_discount

    @average_item_discount.setter
    def average_item_discount(self, average_item_discount):
        """Sets the average_item_discount of this PromotionReportDetail.


        :param average_item_discount: The average_item_discount of this PromotionReportDetail.  # noqa: E501
        :type: Amount
        """

        self._average_item_discount = average_item_discount

    @property
    def average_item_revenue(self):
        """Gets the average_item_revenue of this PromotionReportDetail.  # noqa: E501


        :return: The average_item_revenue of this PromotionReportDetail.  # noqa: E501
        :rtype: Amount
        """
        return self._average_item_revenue

    @average_item_revenue.setter
    def average_item_revenue(self, average_item_revenue):
        """Sets the average_item_revenue of this PromotionReportDetail.


        :param average_item_revenue: The average_item_revenue of this PromotionReportDetail.  # noqa: E501
        :type: Amount
        """

        self._average_item_revenue = average_item_revenue

    @property
    def average_order_discount(self):
        """Gets the average_order_discount of this PromotionReportDetail.  # noqa: E501


        :return: The average_order_discount of this PromotionReportDetail.  # noqa: E501
        :rtype: Amount
        """
        return self._average_order_discount

    @average_order_discount.setter
    def average_order_discount(self, average_order_discount):
        """Sets the average_order_discount of this PromotionReportDetail.


        :param average_order_discount: The average_order_discount of this PromotionReportDetail.  # noqa: E501
        :type: Amount
        """

        self._average_order_discount = average_order_discount

    @property
    def average_order_revenue(self):
        """Gets the average_order_revenue of this PromotionReportDetail.  # noqa: E501


        :return: The average_order_revenue of this PromotionReportDetail.  # noqa: E501
        :rtype: Amount
        """
        return self._average_order_revenue

    @average_order_revenue.setter
    def average_order_revenue(self, average_order_revenue):
        """Sets the average_order_revenue of this PromotionReportDetail.


        :param average_order_revenue: The average_order_revenue of this PromotionReportDetail.  # noqa: E501
        :type: Amount
        """

        self._average_order_revenue = average_order_revenue

    @property
    def average_order_size(self):
        """Gets the average_order_size of this PromotionReportDetail.  # noqa: E501

        The <i>average order size</i> is the average number of items that each order contained in a promotion. This value is calculated as follows:  <br><br><b>itemsSoldQuantity</b> / <b>numberOfOrdersSold</b> = <b>averageOrderSize</b>   # noqa: E501

        :return: The average_order_size of this PromotionReportDetail.  # noqa: E501
        :rtype: str
        """
        return self._average_order_size

    @average_order_size.setter
    def average_order_size(self, average_order_size):
        """Sets the average_order_size of this PromotionReportDetail.

        The <i>average order size</i> is the average number of items that each order contained in a promotion. This value is calculated as follows:  <br><br><b>itemsSoldQuantity</b> / <b>numberOfOrdersSold</b> = <b>averageOrderSize</b>   # noqa: E501

        :param average_order_size: The average_order_size of this PromotionReportDetail.  # noqa: E501
        :type: str
        """

        self._average_order_size = average_order_size

    @property
    def base_sale(self):
        """Gets the base_sale of this PromotionReportDetail.  # noqa: E501


        :return: The base_sale of this PromotionReportDetail.  # noqa: E501
        :rtype: Amount
        """
        return self._base_sale

    @base_sale.setter
    def base_sale(self, base_sale):
        """Sets the base_sale of this PromotionReportDetail.


        :param base_sale: The base_sale of this PromotionReportDetail.  # noqa: E501
        :type: Amount
        """

        self._base_sale = base_sale

    @property
    def items_sold_quantity(self):
        """Gets the items_sold_quantity of this PromotionReportDetail.  # noqa: E501

        This is the quantity of items purchased in a threshold promotion where the threshold <i>has been met</i> and the discount was applied. <br><br>For example, suppose you're running a \"Buy 1, get 1 at 50%\" promotion on $5 socks. One buyer purchases two pairs of socks, so they pay $7.50 for both pairs (rather than the full price of $10). Your number of items sold (<b>itemsSoldQuantity</b>) would be 2 and you number of orders sold (<b>numberOfOrdersSold</b>) would be 1.  # noqa: E501

        :return: The items_sold_quantity of this PromotionReportDetail.  # noqa: E501
        :rtype: int
        """
        return self._items_sold_quantity

    @items_sold_quantity.setter
    def items_sold_quantity(self, items_sold_quantity):
        """Sets the items_sold_quantity of this PromotionReportDetail.

        This is the quantity of items purchased in a threshold promotion where the threshold <i>has been met</i> and the discount was applied. <br><br>For example, suppose you're running a \"Buy 1, get 1 at 50%\" promotion on $5 socks. One buyer purchases two pairs of socks, so they pay $7.50 for both pairs (rather than the full price of $10). Your number of items sold (<b>itemsSoldQuantity</b>) would be 2 and you number of orders sold (<b>numberOfOrdersSold</b>) would be 1.  # noqa: E501

        :param items_sold_quantity: The items_sold_quantity of this PromotionReportDetail.  # noqa: E501
        :type: int
        """

        self._items_sold_quantity = items_sold_quantity

    @property
    def number_of_orders_sold(self):
        """Gets the number_of_orders_sold of this PromotionReportDetail.  # noqa: E501

        This is the number of orders sold in a threshold promotion where the threshold <i>has been met</i> and the discount was applied. <br><br>For example, suppose you're running a \"Buy 1, get 1 at 50%\" promotion on $5 socks. One buyer purchases two pairs of socks, so they pay $7.50 for both pairs (rather than the full price of $10). Your <b>numberOfOrdersSold</b> would be 1 and your <b>itemsSoldQuantity</b> would be 2.  # noqa: E501

        :return: The number_of_orders_sold of this PromotionReportDetail.  # noqa: E501
        :rtype: int
        """
        return self._number_of_orders_sold

    @number_of_orders_sold.setter
    def number_of_orders_sold(self, number_of_orders_sold):
        """Sets the number_of_orders_sold of this PromotionReportDetail.

        This is the number of orders sold in a threshold promotion where the threshold <i>has been met</i> and the discount was applied. <br><br>For example, suppose you're running a \"Buy 1, get 1 at 50%\" promotion on $5 socks. One buyer purchases two pairs of socks, so they pay $7.50 for both pairs (rather than the full price of $10). Your <b>numberOfOrdersSold</b> would be 1 and your <b>itemsSoldQuantity</b> would be 2.  # noqa: E501

        :param number_of_orders_sold: The number_of_orders_sold of this PromotionReportDetail.  # noqa: E501
        :type: int
        """

        self._number_of_orders_sold = number_of_orders_sold

    @property
    def percentage_sales_lift(self):
        """Gets the percentage_sales_lift of this PromotionReportDetail.  # noqa: E501

        The <i>percentage sales lift</i> is the total dollar amount gained due to promotions. This value is calculated as follows:  <br><br> <b>promotionSale</b> / <b>totalSale</b> =  <b>percentageSalesLift</b>   # noqa: E501

        :return: The percentage_sales_lift of this PromotionReportDetail.  # noqa: E501
        :rtype: str
        """
        return self._percentage_sales_lift

    @percentage_sales_lift.setter
    def percentage_sales_lift(self, percentage_sales_lift):
        """Sets the percentage_sales_lift of this PromotionReportDetail.

        The <i>percentage sales lift</i> is the total dollar amount gained due to promotions. This value is calculated as follows:  <br><br> <b>promotionSale</b> / <b>totalSale</b> =  <b>percentageSalesLift</b>   # noqa: E501

        :param percentage_sales_lift: The percentage_sales_lift of this PromotionReportDetail.  # noqa: E501
        :type: str
        """

        self._percentage_sales_lift = percentage_sales_lift

    @property
    def promotion_href(self):
        """Gets the promotion_href of this PromotionReportDetail.  # noqa: E501

        The URI of the promotion report.  # noqa: E501

        :return: The promotion_href of this PromotionReportDetail.  # noqa: E501
        :rtype: str
        """
        return self._promotion_href

    @promotion_href.setter
    def promotion_href(self, promotion_href):
        """Sets the promotion_href of this PromotionReportDetail.

        The URI of the promotion report.  # noqa: E501

        :param promotion_href: The promotion_href of this PromotionReportDetail.  # noqa: E501
        :type: str
        """

        self._promotion_href = promotion_href

    @property
    def promotion_id(self):
        """Gets the promotion_id of this PromotionReportDetail.  # noqa: E501

        A unique eBay-assigned ID for the promotion that's generated when the promotion is created.  # noqa: E501

        :return: The promotion_id of this PromotionReportDetail.  # noqa: E501
        :rtype: str
        """
        return self._promotion_id

    @promotion_id.setter
    def promotion_id(self, promotion_id):
        """Sets the promotion_id of this PromotionReportDetail.

        A unique eBay-assigned ID for the promotion that's generated when the promotion is created.  # noqa: E501

        :param promotion_id: The promotion_id of this PromotionReportDetail.  # noqa: E501
        :type: str
        """

        self._promotion_id = promotion_id

    @property
    def promotion_report_id(self):
        """Gets the promotion_report_id of this PromotionReportDetail.  # noqa: E501

        The unique eBay-assigned ID of the promotion report that is generated when the report is created.  # noqa: E501

        :return: The promotion_report_id of this PromotionReportDetail.  # noqa: E501
        :rtype: str
        """
        return self._promotion_report_id

    @promotion_report_id.setter
    def promotion_report_id(self, promotion_report_id):
        """Sets the promotion_report_id of this PromotionReportDetail.

        The unique eBay-assigned ID of the promotion report that is generated when the report is created.  # noqa: E501

        :param promotion_report_id: The promotion_report_id of this PromotionReportDetail.  # noqa: E501
        :type: str
        """

        self._promotion_report_id = promotion_report_id

    @property
    def promotion_sale(self):
        """Gets the promotion_sale of this PromotionReportDetail.  # noqa: E501


        :return: The promotion_sale of this PromotionReportDetail.  # noqa: E501
        :rtype: Amount
        """
        return self._promotion_sale

    @promotion_sale.setter
    def promotion_sale(self, promotion_sale):
        """Sets the promotion_sale of this PromotionReportDetail.


        :param promotion_sale: The promotion_sale of this PromotionReportDetail.  # noqa: E501
        :type: Amount
        """

        self._promotion_sale = promotion_sale

    @property
    def promotion_type(self):
        """Gets the promotion_type of this PromotionReportDetail.  # noqa: E501

        Indicates the type of the promotion, either <code>CODED_COUPON</code>, <code>MARKDOWN_SALE</code>, <code>ORDER_DISCOUNT</code>, or <code>VOLUME_DISCOUNT</code>. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/sme:PromotionTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The promotion_type of this PromotionReportDetail.  # noqa: E501
        :rtype: str
        """
        return self._promotion_type

    @promotion_type.setter
    def promotion_type(self, promotion_type):
        """Sets the promotion_type of this PromotionReportDetail.

        Indicates the type of the promotion, either <code>CODED_COUPON</code>, <code>MARKDOWN_SALE</code>, <code>ORDER_DISCOUNT</code>, or <code>VOLUME_DISCOUNT</code>. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/sme:PromotionTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param promotion_type: The promotion_type of this PromotionReportDetail.  # noqa: E501
        :type: str
        """

        self._promotion_type = promotion_type

    @property
    def total_discount(self):
        """Gets the total_discount of this PromotionReportDetail.  # noqa: E501


        :return: The total_discount of this PromotionReportDetail.  # noqa: E501
        :rtype: Amount
        """
        return self._total_discount

    @total_discount.setter
    def total_discount(self, total_discount):
        """Sets the total_discount of this PromotionReportDetail.


        :param total_discount: The total_discount of this PromotionReportDetail.  # noqa: E501
        :type: Amount
        """

        self._total_discount = total_discount

    @property
    def total_sale(self):
        """Gets the total_sale of this PromotionReportDetail.  # noqa: E501


        :return: The total_sale of this PromotionReportDetail.  # noqa: E501
        :rtype: Amount
        """
        return self._total_sale

    @total_sale.setter
    def total_sale(self, total_sale):
        """Sets the total_sale of this PromotionReportDetail.


        :param total_sale: The total_sale of this PromotionReportDetail.  # noqa: E501
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
        if issubclass(PromotionReportDetail, dict):
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
        if not isinstance(other, PromotionReportDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
