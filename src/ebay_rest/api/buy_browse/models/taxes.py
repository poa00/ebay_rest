# coding: utf-8

"""
    Browse API

    <p>The Browse API has the following resources:</p>   <ul> <li><b> item_summary: </b> Lets shoppers search for specific items by keyword, GTIN, category, charity, product, or item aspects and refine the results by using filters, such as aspects, compatibility, and fields values.</li>  <li><b> search_by_image: </b><a href=\"https://developer.ebay.com/api-docs/static/versioning.html#experimental\" target=\"_blank\"><img src=\"/cms/img/docs/experimental-icon.svg\" class=\"legend-icon experimental-icon\" alt=\"Experimental Release\" title=\"Experimental Release\" />&nbsp;(Experimental)</a> Lets shoppers search for specific items by image. You can refine the results by using URI parameters and filters.</li>   <li><b> item: </b> <ul><li>Lets you retrieve the details of a specific item or all the items in an item group, which is an item with variations such as color and size and check if a product is compatible with the specified item, such as if a specific car is compatible with a specific part.</li> <li>Provides a bridge between the eBay legacy APIs, such as <b> Finding</b>, and the RESTful APIs, which use different formats for the item IDs.</li>  </ul> </li>  <li> <b> shopping_cart: </b> <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#experimental\" target=\"_blank\"><img src=\"/cms/img/docs/experimental-icon.svg\" class=\"legend-icon experimental-icon\" alt=\"Experimental Release\" title=\"Experimental Release\" />&nbsp;(Experimental)</a> <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited\" target=\"_blank\"> <img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"  alt=\"Limited Release\" />(Limited Release)</a> Provides the ability for eBay members to see the contents of their eBay cart, and add, remove, and change the quantity of items in their eBay cart.&nbsp;&nbsp;<b> Note: </b> This resource is not available in the eBay API Explorer.</li></ul>       <p>The <b> item_summary</b>, <b> search_by_image</b>, and <b> item</b> resource calls require an <a href=\"/api-docs/static/oauth-client-credentials-grant.html\">Application access token</a>. The <b> shopping_cart</b> resource calls require a <a href=\"/api-docs/static/oauth-authorization-code-grant.html\">User access token</a>.</p>  # noqa: E501

    OpenAPI spec version: v1.12.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Taxes(object):
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
        'ebay_collect_and_remit_tax': 'bool',
        'included_in_price': 'bool',
        'shipping_and_handling_taxed': 'bool',
        'tax_jurisdiction': 'TaxJurisdiction',
        'tax_percentage': 'str',
        'tax_type': 'str'
    }

    attribute_map = {
        'ebay_collect_and_remit_tax': 'ebayCollectAndRemitTax',
        'included_in_price': 'includedInPrice',
        'shipping_and_handling_taxed': 'shippingAndHandlingTaxed',
        'tax_jurisdiction': 'taxJurisdiction',
        'tax_percentage': 'taxPercentage',
        'tax_type': 'taxType'
    }

    def __init__(self, ebay_collect_and_remit_tax=None, included_in_price=None, shipping_and_handling_taxed=None, tax_jurisdiction=None, tax_percentage=None, tax_type=None):  # noqa: E501
        """Taxes - a model defined in Swagger"""  # noqa: E501
        self._ebay_collect_and_remit_tax = None
        self._included_in_price = None
        self._shipping_and_handling_taxed = None
        self._tax_jurisdiction = None
        self._tax_percentage = None
        self._tax_type = None
        self.discriminator = None
        if ebay_collect_and_remit_tax is not None:
            self.ebay_collect_and_remit_tax = ebay_collect_and_remit_tax
        if included_in_price is not None:
            self.included_in_price = included_in_price
        if shipping_and_handling_taxed is not None:
            self.shipping_and_handling_taxed = shipping_and_handling_taxed
        if tax_jurisdiction is not None:
            self.tax_jurisdiction = tax_jurisdiction
        if tax_percentage is not None:
            self.tax_percentage = tax_percentage
        if tax_type is not None:
            self.tax_type = tax_type

    @property
    def ebay_collect_and_remit_tax(self):
        """Gets the ebay_collect_and_remit_tax of this Taxes.  # noqa: E501

        This field is only returned if <code>true</code>, and indicates that eBay will collect tax (sales tax, Goods and Services tax, or VAT) for at least one line item in the order, and remit the tax to the taxing authority of the buyer's residence.   # noqa: E501

        :return: The ebay_collect_and_remit_tax of this Taxes.  # noqa: E501
        :rtype: bool
        """
        return self._ebay_collect_and_remit_tax

    @ebay_collect_and_remit_tax.setter
    def ebay_collect_and_remit_tax(self, ebay_collect_and_remit_tax):
        """Sets the ebay_collect_and_remit_tax of this Taxes.

        This field is only returned if <code>true</code>, and indicates that eBay will collect tax (sales tax, Goods and Services tax, or VAT) for at least one line item in the order, and remit the tax to the taxing authority of the buyer's residence.   # noqa: E501

        :param ebay_collect_and_remit_tax: The ebay_collect_and_remit_tax of this Taxes.  # noqa: E501
        :type: bool
        """

        self._ebay_collect_and_remit_tax = ebay_collect_and_remit_tax

    @property
    def included_in_price(self):
        """Gets the included_in_price of this Taxes.  # noqa: E501

        This indicates if tax was applied for the cost of the item.  # noqa: E501

        :return: The included_in_price of this Taxes.  # noqa: E501
        :rtype: bool
        """
        return self._included_in_price

    @included_in_price.setter
    def included_in_price(self, included_in_price):
        """Sets the included_in_price of this Taxes.

        This indicates if tax was applied for the cost of the item.  # noqa: E501

        :param included_in_price: The included_in_price of this Taxes.  # noqa: E501
        :type: bool
        """

        self._included_in_price = included_in_price

    @property
    def shipping_and_handling_taxed(self):
        """Gets the shipping_and_handling_taxed of this Taxes.  # noqa: E501

        This indicates if tax is applied for the shipping cost.  # noqa: E501

        :return: The shipping_and_handling_taxed of this Taxes.  # noqa: E501
        :rtype: bool
        """
        return self._shipping_and_handling_taxed

    @shipping_and_handling_taxed.setter
    def shipping_and_handling_taxed(self, shipping_and_handling_taxed):
        """Sets the shipping_and_handling_taxed of this Taxes.

        This indicates if tax is applied for the shipping cost.  # noqa: E501

        :param shipping_and_handling_taxed: The shipping_and_handling_taxed of this Taxes.  # noqa: E501
        :type: bool
        """

        self._shipping_and_handling_taxed = shipping_and_handling_taxed

    @property
    def tax_jurisdiction(self):
        """Gets the tax_jurisdiction of this Taxes.  # noqa: E501


        :return: The tax_jurisdiction of this Taxes.  # noqa: E501
        :rtype: TaxJurisdiction
        """
        return self._tax_jurisdiction

    @tax_jurisdiction.setter
    def tax_jurisdiction(self, tax_jurisdiction):
        """Sets the tax_jurisdiction of this Taxes.


        :param tax_jurisdiction: The tax_jurisdiction of this Taxes.  # noqa: E501
        :type: TaxJurisdiction
        """

        self._tax_jurisdiction = tax_jurisdiction

    @property
    def tax_percentage(self):
        """Gets the tax_percentage of this Taxes.  # noqa: E501

        The percentage of tax.  # noqa: E501

        :return: The tax_percentage of this Taxes.  # noqa: E501
        :rtype: str
        """
        return self._tax_percentage

    @tax_percentage.setter
    def tax_percentage(self, tax_percentage):
        """Sets the tax_percentage of this Taxes.

        The percentage of tax.  # noqa: E501

        :param tax_percentage: The tax_percentage of this Taxes.  # noqa: E501
        :type: str
        """

        self._tax_percentage = tax_percentage

    @property
    def tax_type(self):
        """Gets the tax_type of this Taxes.  # noqa: E501

        This field indicates the type of tax that may be collected for the item. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/buy/browse/types/gct:TaxType'>eBay API documentation</a>  # noqa: E501

        :return: The tax_type of this Taxes.  # noqa: E501
        :rtype: str
        """
        return self._tax_type

    @tax_type.setter
    def tax_type(self, tax_type):
        """Sets the tax_type of this Taxes.

        This field indicates the type of tax that may be collected for the item. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/buy/browse/types/gct:TaxType'>eBay API documentation</a>  # noqa: E501

        :param tax_type: The tax_type of this Taxes.  # noqa: E501
        :type: str
        """

        self._tax_type = tax_type

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
        if issubclass(Taxes, dict):
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
        if not isinstance(other, Taxes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
