# coding: utf-8

"""
    Inventory API

    The Inventory API is used to create and manage inventory, and then to publish and manage this inventory on an eBay marketplace. There are also methods in this API that will convert eligible, active eBay listings into the Inventory API model.  # noqa: E501

    OpenAPI spec version: 1.17.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Tax(object):
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
        'apply_tax': 'bool',
        'third_party_tax_category': 'str',
        'vat_percentage': 'float'
    }

    attribute_map = {
        'apply_tax': 'applyTax',
        'third_party_tax_category': 'thirdPartyTaxCategory',
        'vat_percentage': 'vatPercentage'
    }

    def __init__(self, apply_tax=None, third_party_tax_category=None, vat_percentage=None):  # noqa: E501
        """Tax - a model defined in Swagger"""  # noqa: E501
        self._apply_tax = None
        self._third_party_tax_category = None
        self._vat_percentage = None
        self.discriminator = None
        if apply_tax is not None:
            self.apply_tax = apply_tax
        if third_party_tax_category is not None:
            self.third_party_tax_category = third_party_tax_category
        if vat_percentage is not None:
            self.vat_percentage = vat_percentage

    @property
    def apply_tax(self):
        """Gets the apply_tax of this Tax.  # noqa: E501

        When set to <code>true</code>, the seller's account-level sales-tax table will be used to calculate sales tax for an order.<br><br><span class=\"tablenote\"><b>Note:</b> Sales-tax tables are available only for the US and Canada marketplaces.</span><br><div class=\"msgbox_important\"><p class=\"msgbox_importantInDiv\" data-mc-autonum=\"&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;\"><span class=\"autonumber\"><span><b><span style=\"color: #dd1e31;\" class=\"mcFormatColor\">Important!</span></b></span></span> In the US, eBay now calculates, collects, and remits sales tax to the proper taxing authorities in all 50 states and Washington, DC. Sellers can no longer specify sales-tax rates for these jurisdictions using a tax table.<br><br>However, sellers may continue to use a sales-tax table to set rates for the following US territories:<ul><li>American Samoa (AS)</li><li>Guam (GU)</li><li>Northern Mariana Islands (MP)</li><li>Palau (PW)</li><li>US Virgin Islands (VI)</li></ul></p></div><br>For complete information about using sales-tax tables, refer to <a href=\"/api-docs/sell/static/seller-accounts/tax-tables.html\" target=\"_blank\">Establishing sales-tax tables</a>.<br><br>Note that a seller can enable the use of a sales-tax table, but if a sales-tax rate is not specified for the buyer's tax jurisdiction, sales tax will not be applied to the order.<br><br>When a <code>thirdPartyTaxCategory</code> value is used, <code>applyTax</code> must also be set to <code>true</code>.<br><br>This field will be returned by <a href=\"/api-docs/sell/inventory/resources/offer/methods/getOffer\">getOffer</a> and <a href=\"/api-docs/sell/inventory/resources/offer/methods/getOffers\">getOffers</a> if set for the offer.<br><br>For additional information, refer to <a href=\"https://www.ebay.com/help/selling/fees-credits-invoices/taxes-import-charges?id=4121 \" target=\"_blank\">Taxes and import charges</a>.  # noqa: E501

        :return: The apply_tax of this Tax.  # noqa: E501
        :rtype: bool
        """
        return self._apply_tax

    @apply_tax.setter
    def apply_tax(self, apply_tax):
        """Sets the apply_tax of this Tax.

        When set to <code>true</code>, the seller's account-level sales-tax table will be used to calculate sales tax for an order.<br><br><span class=\"tablenote\"><b>Note:</b> Sales-tax tables are available only for the US and Canada marketplaces.</span><br><div class=\"msgbox_important\"><p class=\"msgbox_importantInDiv\" data-mc-autonum=\"&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;\"><span class=\"autonumber\"><span><b><span style=\"color: #dd1e31;\" class=\"mcFormatColor\">Important!</span></b></span></span> In the US, eBay now calculates, collects, and remits sales tax to the proper taxing authorities in all 50 states and Washington, DC. Sellers can no longer specify sales-tax rates for these jurisdictions using a tax table.<br><br>However, sellers may continue to use a sales-tax table to set rates for the following US territories:<ul><li>American Samoa (AS)</li><li>Guam (GU)</li><li>Northern Mariana Islands (MP)</li><li>Palau (PW)</li><li>US Virgin Islands (VI)</li></ul></p></div><br>For complete information about using sales-tax tables, refer to <a href=\"/api-docs/sell/static/seller-accounts/tax-tables.html\" target=\"_blank\">Establishing sales-tax tables</a>.<br><br>Note that a seller can enable the use of a sales-tax table, but if a sales-tax rate is not specified for the buyer's tax jurisdiction, sales tax will not be applied to the order.<br><br>When a <code>thirdPartyTaxCategory</code> value is used, <code>applyTax</code> must also be set to <code>true</code>.<br><br>This field will be returned by <a href=\"/api-docs/sell/inventory/resources/offer/methods/getOffer\">getOffer</a> and <a href=\"/api-docs/sell/inventory/resources/offer/methods/getOffers\">getOffers</a> if set for the offer.<br><br>For additional information, refer to <a href=\"https://www.ebay.com/help/selling/fees-credits-invoices/taxes-import-charges?id=4121 \" target=\"_blank\">Taxes and import charges</a>.  # noqa: E501

        :param apply_tax: The apply_tax of this Tax.  # noqa: E501
        :type: bool
        """

        self._apply_tax = apply_tax

    @property
    def third_party_tax_category(self):
        """Gets the third_party_tax_category of this Tax.  # noqa: E501

        The tax exception category code. If this field is used, sales tax will also apply to a service/fee, and not just the item price. This is to be used only by sellers who have opted into sales tax being calculated by a sales tax calculation vendor. If you are interested in becoming a tax calculation vendor partner with eBay, contact <a href=\"mailto:developer-relations@ebay.com \">developer-relations@ebay.com</a>. One supported value for this field is <code>WASTE_RECYCLING_FEE</code>. If this field is used, the <strong>applyTax</strong> field must also be used and set to <code>true</code><br><br>This field will be returned by <a href=\"/api-docs/sell/inventory/resources/offer/methods/getOffer\">getOffer</a> and <a href=\"/api-docs/sell/inventory/resources/offer/methods/getOffers\">getOffers</a> if set for the offer.  # noqa: E501

        :return: The third_party_tax_category of this Tax.  # noqa: E501
        :rtype: str
        """
        return self._third_party_tax_category

    @third_party_tax_category.setter
    def third_party_tax_category(self, third_party_tax_category):
        """Sets the third_party_tax_category of this Tax.

        The tax exception category code. If this field is used, sales tax will also apply to a service/fee, and not just the item price. This is to be used only by sellers who have opted into sales tax being calculated by a sales tax calculation vendor. If you are interested in becoming a tax calculation vendor partner with eBay, contact <a href=\"mailto:developer-relations@ebay.com \">developer-relations@ebay.com</a>. One supported value for this field is <code>WASTE_RECYCLING_FEE</code>. If this field is used, the <strong>applyTax</strong> field must also be used and set to <code>true</code><br><br>This field will be returned by <a href=\"/api-docs/sell/inventory/resources/offer/methods/getOffer\">getOffer</a> and <a href=\"/api-docs/sell/inventory/resources/offer/methods/getOffers\">getOffers</a> if set for the offer.  # noqa: E501

        :param third_party_tax_category: The third_party_tax_category of this Tax.  # noqa: E501
        :type: str
        """

        self._third_party_tax_category = third_party_tax_category

    @property
    def vat_percentage(self):
        """Gets the vat_percentage of this Tax.  # noqa: E501

        This value is the Value Add Tax (VAT) rate for the item, if any. When a VAT percentage is specified, the item's VAT information appears on the listing's View Item page. In addition, the seller can choose to print an invoice that includes the item's net price, VAT percent, VAT amount, and total price. Since VAT rates vary depending on the item and on the user's country of residence, a seller is responsible for entering the correct VAT rate; it is not calculated by eBay. <br><br> To use VAT, a seller must be a business seller with a VAT-ID registered with eBay, and must be listing the item on a VAT-enabled site. Max applicable length is 6 characters, including the decimal (e.g., 12.345). The scale is 3 decimal places. (If you pass in 12.3456, eBay may round up the value to 12.346).<br><br>This field will be returned by <a href=\"/api-docs/sell/inventory/resources/offer/methods/getOffer\">getOffer</a> and <a href=\"/api-docs/sell/inventory/resources/offer/methods/getOffers\">getOffers</a> if set for the offer.  # noqa: E501

        :return: The vat_percentage of this Tax.  # noqa: E501
        :rtype: float
        """
        return self._vat_percentage

    @vat_percentage.setter
    def vat_percentage(self, vat_percentage):
        """Sets the vat_percentage of this Tax.

        This value is the Value Add Tax (VAT) rate for the item, if any. When a VAT percentage is specified, the item's VAT information appears on the listing's View Item page. In addition, the seller can choose to print an invoice that includes the item's net price, VAT percent, VAT amount, and total price. Since VAT rates vary depending on the item and on the user's country of residence, a seller is responsible for entering the correct VAT rate; it is not calculated by eBay. <br><br> To use VAT, a seller must be a business seller with a VAT-ID registered with eBay, and must be listing the item on a VAT-enabled site. Max applicable length is 6 characters, including the decimal (e.g., 12.345). The scale is 3 decimal places. (If you pass in 12.3456, eBay may round up the value to 12.346).<br><br>This field will be returned by <a href=\"/api-docs/sell/inventory/resources/offer/methods/getOffer\">getOffer</a> and <a href=\"/api-docs/sell/inventory/resources/offer/methods/getOffers\">getOffers</a> if set for the offer.  # noqa: E501

        :param vat_percentage: The vat_percentage of this Tax.  # noqa: E501
        :type: float
        """

        self._vat_percentage = vat_percentage

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
        if issubclass(Tax, dict):
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
        if not isinstance(other, Tax):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
