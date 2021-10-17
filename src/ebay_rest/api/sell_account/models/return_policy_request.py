# coding: utf-8

"""
    Account API

    The <b>Account API</b> gives sellers the ability to configure their eBay seller accounts, including the seller's policies (the Fulfillment Policy, Payment Policy, and Return Policy), opt in and out of eBay seller programs, configure sales tax tables, and get account information.  <br><br>For details on the availability of the methods in this API, see <a href=\"/api-docs/sell/account/overview.html#requirements\">Account API requirements and restrictions</a>.  # noqa: E501

    OpenAPI spec version: v1.6.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ReturnPolicyRequest(object):
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
        'category_types': 'list[CategoryType]',
        'description': 'str',
        'extended_holiday_returns_offered': 'bool',
        'international_override': 'InternationalReturnOverrideType',
        'marketplace_id': 'str',
        'name': 'str',
        'refund_method': 'str',
        'restocking_fee_percentage': 'str',
        'return_instructions': 'str',
        'return_method': 'str',
        'return_period': 'TimeDuration',
        'return_shipping_cost_payer': 'str',
        'returns_accepted': 'bool'
    }

    attribute_map = {
        'category_types': 'categoryTypes',
        'description': 'description',
        'extended_holiday_returns_offered': 'extendedHolidayReturnsOffered',
        'international_override': 'internationalOverride',
        'marketplace_id': 'marketplaceId',
        'name': 'name',
        'refund_method': 'refundMethod',
        'restocking_fee_percentage': 'restockingFeePercentage',
        'return_instructions': 'returnInstructions',
        'return_method': 'returnMethod',
        'return_period': 'returnPeriod',
        'return_shipping_cost_payer': 'returnShippingCostPayer',
        'returns_accepted': 'returnsAccepted'
    }

    def __init__(self, category_types=None, description=None, extended_holiday_returns_offered=None, international_override=None, marketplace_id=None, name=None, refund_method=None, restocking_fee_percentage=None, return_instructions=None, return_method=None, return_period=None, return_shipping_cost_payer=None, returns_accepted=None):  # noqa: E501
        """ReturnPolicyRequest - a model defined in Swagger"""  # noqa: E501
        self._category_types = None
        self._description = None
        self._extended_holiday_returns_offered = None
        self._international_override = None
        self._marketplace_id = None
        self._name = None
        self._refund_method = None
        self._restocking_fee_percentage = None
        self._return_instructions = None
        self._return_method = None
        self._return_period = None
        self._return_shipping_cost_payer = None
        self._returns_accepted = None
        self.discriminator = None
        if category_types is not None:
            self.category_types = category_types
        if description is not None:
            self.description = description
        if extended_holiday_returns_offered is not None:
            self.extended_holiday_returns_offered = extended_holiday_returns_offered
        if international_override is not None:
            self.international_override = international_override
        if marketplace_id is not None:
            self.marketplace_id = marketplace_id
        if name is not None:
            self.name = name
        if refund_method is not None:
            self.refund_method = refund_method
        if restocking_fee_percentage is not None:
            self.restocking_fee_percentage = restocking_fee_percentage
        if return_instructions is not None:
            self.return_instructions = return_instructions
        if return_method is not None:
            self.return_method = return_method
        if return_period is not None:
            self.return_period = return_period
        if return_shipping_cost_payer is not None:
            self.return_shipping_cost_payer = return_shipping_cost_payer
        if returns_accepted is not None:
            self.returns_accepted = returns_accepted

    @property
    def category_types(self):
        """Gets the category_types of this ReturnPolicyRequest.  # noqa: E501

        For return policies, this field can be set to only <code>ALL_EXCLUDING_MOTORS_VEHICLES</code> (returns on motor vehicles are not processed through eBay flows.) <br><br><b>Default</b>: <code>ALL_EXCLUDING_MOTORS_VEHICLES</code> (for return policies only)  # noqa: E501

        :return: The category_types of this ReturnPolicyRequest.  # noqa: E501
        :rtype: list[CategoryType]
        """
        return self._category_types

    @category_types.setter
    def category_types(self, category_types):
        """Sets the category_types of this ReturnPolicyRequest.

        For return policies, this field can be set to only <code>ALL_EXCLUDING_MOTORS_VEHICLES</code> (returns on motor vehicles are not processed through eBay flows.) <br><br><b>Default</b>: <code>ALL_EXCLUDING_MOTORS_VEHICLES</code> (for return policies only)  # noqa: E501

        :param category_types: The category_types of this ReturnPolicyRequest.  # noqa: E501
        :type: list[CategoryType]
        """

        self._category_types = category_types

    @property
    def description(self):
        """Gets the description of this ReturnPolicyRequest.  # noqa: E501

        An optional seller-defined description of the return policy for internal use (this value is not displayed to end users).  <br><br><b>Max length</b>: 250  # noqa: E501

        :return: The description of this ReturnPolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ReturnPolicyRequest.

        An optional seller-defined description of the return policy for internal use (this value is not displayed to end users).  <br><br><b>Max length</b>: 250  # noqa: E501

        :param description: The description of this ReturnPolicyRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def extended_holiday_returns_offered(self):
        """Gets the extended_holiday_returns_offered of this ReturnPolicyRequest.  # noqa: E501

        <p class=\"tablenote\"><span  style=\"color: #dd1e31;\"><b>Important!</b></span> This field has been deprecated as of version 1.2.0, released on May 31, 2018. Any value supplied in this field is ignored, it is neither read nor returned.</p>  <p>If set to <code>true</code>, the seller offers an <em>Extended Holiday Returns</em> policy for their listings.  <p><span class=\"tablenote\"><strong>IMPORTANT:</strong> Extended Holiday Returns is a seasonally available feature that is offered on some eBay marketplaces. To see if the feature is enabled in any given year, check the <a href=\"http://pages.ebay.com/seller-center/shipping/returns.html\">Returns on eBay</a> page before the holiday season begins. If the feature is not enabled for the season, this field is ignored.</span></p>  <p>The extended holiday returns period is defined by three dates:</p> <ul><li>The start date = start of November.</li><li>The purchase cutoff date = end of the year.</li><li>The end date = end of January.</li></ul>  <p>The above dates may vary by a few days each year. Sellers are notified of the current dates on their eBay marketplace before the holiday period starts.</p>  <p>Sellers can specify Extended Holiday Returns (as well as their regular non-holiday returns period) for chosen listings at any time during the year. The Extended Holiday Returns offer is not visible in listings until the start date of current year's holiday returns period, at which point it overrides the non-holiday returns policy. Buyers can see the Extended Holiday Returns offer in listings displayed through the purchase cutoff date and are able to return those purchases until the end date of the period.</p>  <p>After the purchase cutoff date, the Extended Holiday Returns offer automatically disappears from the listings and the seller's non-holiday returns period reappears. Purchases made from that point on are subject to the non-holiday returns period, while purchases made before the cutoff date still have until the end of the period to return under the program.</p>  <p>If the value of <strong>holidayReturns</strong> is <code>false</code> for an item, the return period specified by the <strong>returnsWithinOption</strong> field applies, regardless of the purchase date. If the item is listed with a policy of no returns, <strong>holidayReturns</strong> is automatically reset to <code>false</code>.</p>  # noqa: E501

        :return: The extended_holiday_returns_offered of this ReturnPolicyRequest.  # noqa: E501
        :rtype: bool
        """
        return self._extended_holiday_returns_offered

    @extended_holiday_returns_offered.setter
    def extended_holiday_returns_offered(self, extended_holiday_returns_offered):
        """Sets the extended_holiday_returns_offered of this ReturnPolicyRequest.

        <p class=\"tablenote\"><span  style=\"color: #dd1e31;\"><b>Important!</b></span> This field has been deprecated as of version 1.2.0, released on May 31, 2018. Any value supplied in this field is ignored, it is neither read nor returned.</p>  <p>If set to <code>true</code>, the seller offers an <em>Extended Holiday Returns</em> policy for their listings.  <p><span class=\"tablenote\"><strong>IMPORTANT:</strong> Extended Holiday Returns is a seasonally available feature that is offered on some eBay marketplaces. To see if the feature is enabled in any given year, check the <a href=\"http://pages.ebay.com/seller-center/shipping/returns.html\">Returns on eBay</a> page before the holiday season begins. If the feature is not enabled for the season, this field is ignored.</span></p>  <p>The extended holiday returns period is defined by three dates:</p> <ul><li>The start date = start of November.</li><li>The purchase cutoff date = end of the year.</li><li>The end date = end of January.</li></ul>  <p>The above dates may vary by a few days each year. Sellers are notified of the current dates on their eBay marketplace before the holiday period starts.</p>  <p>Sellers can specify Extended Holiday Returns (as well as their regular non-holiday returns period) for chosen listings at any time during the year. The Extended Holiday Returns offer is not visible in listings until the start date of current year's holiday returns period, at which point it overrides the non-holiday returns policy. Buyers can see the Extended Holiday Returns offer in listings displayed through the purchase cutoff date and are able to return those purchases until the end date of the period.</p>  <p>After the purchase cutoff date, the Extended Holiday Returns offer automatically disappears from the listings and the seller's non-holiday returns period reappears. Purchases made from that point on are subject to the non-holiday returns period, while purchases made before the cutoff date still have until the end of the period to return under the program.</p>  <p>If the value of <strong>holidayReturns</strong> is <code>false</code> for an item, the return period specified by the <strong>returnsWithinOption</strong> field applies, regardless of the purchase date. If the item is listed with a policy of no returns, <strong>holidayReturns</strong> is automatically reset to <code>false</code>.</p>  # noqa: E501

        :param extended_holiday_returns_offered: The extended_holiday_returns_offered of this ReturnPolicyRequest.  # noqa: E501
        :type: bool
        """

        self._extended_holiday_returns_offered = extended_holiday_returns_offered

    @property
    def international_override(self):
        """Gets the international_override of this ReturnPolicyRequest.  # noqa: E501


        :return: The international_override of this ReturnPolicyRequest.  # noqa: E501
        :rtype: InternationalReturnOverrideType
        """
        return self._international_override

    @international_override.setter
    def international_override(self, international_override):
        """Sets the international_override of this ReturnPolicyRequest.


        :param international_override: The international_override of this ReturnPolicyRequest.  # noqa: E501
        :type: InternationalReturnOverrideType
        """

        self._international_override = international_override

    @property
    def marketplace_id(self):
        """Gets the marketplace_id of this ReturnPolicyRequest.  # noqa: E501

        The ID of the eBay marketplace to which this return policy applies. If this value is not specified, value defaults to the seller's eBay registration site. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/ba:MarketplaceIdEnum'>eBay API documentation</a>  # noqa: E501

        :return: The marketplace_id of this ReturnPolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._marketplace_id

    @marketplace_id.setter
    def marketplace_id(self, marketplace_id):
        """Sets the marketplace_id of this ReturnPolicyRequest.

        The ID of the eBay marketplace to which this return policy applies. If this value is not specified, value defaults to the seller's eBay registration site. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/ba:MarketplaceIdEnum'>eBay API documentation</a>  # noqa: E501

        :param marketplace_id: The marketplace_id of this ReturnPolicyRequest.  # noqa: E501
        :type: str
        """

        self._marketplace_id = marketplace_id

    @property
    def name(self):
        """Gets the name of this ReturnPolicyRequest.  # noqa: E501

        A user-defined name for this return policy. Names must be unique for policies assigned to the same marketplace. <br><br><b>Max length</b>: 64  # noqa: E501

        :return: The name of this ReturnPolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ReturnPolicyRequest.

        A user-defined name for this return policy. Names must be unique for policies assigned to the same marketplace. <br><br><b>Max length</b>: 64  # noqa: E501

        :param name: The name of this ReturnPolicyRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def refund_method(self):
        """Gets the refund_method of this ReturnPolicyRequest.  # noqa: E501

        <p class=\"tablenote\"><span  style=\"color: #dd1e31;\"><b>Important!</b></span> this field has been deprecated as of version 1.2.0, released on May 31, 2018. Any value other than <code>MONEY_BACK</code> will be treated as <code>MONEY_BACK</code> (although for a period of time, eBay will store and return the legacy values to preserve backwards compatibility).</p>  Indicates the method the seller uses to compensate the buyer for returned items. The return method specified applies only to <a href=\"http://developer.ebay.com/DevZone/guides/features-guide/default.html#Development/Post-Order-Returns.html#return-reasons\" target=\"_blank\">remorse returns</a>. <br><br>Note that each eBay marketplace can support different sets of refund methods. Also, each eBay marketplace has a default setting for this value and if you do not specifically set this value, sellers are obligated to honor the setting that displays in their listings. Call <b>GeteBayDetails</b> in the Trading API to see what refund methods the marketplaces you sell into support. <br><br>We recommend you set this field to the value of your preferred refund method and that you use the <b>description</b> field to detail the seller's return policy (such as indicating how quickly the seller will process a refund, whether the seller must receive the item before processing a refund, and other similar useful details). <br><br>You cannot modify this value in a Revise item call if (1) the listing has bids or (2) the listing ends within 12 hours. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/api:RefundMethodEnum'>eBay API documentation</a>  # noqa: E501

        :return: The refund_method of this ReturnPolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._refund_method

    @refund_method.setter
    def refund_method(self, refund_method):
        """Sets the refund_method of this ReturnPolicyRequest.

        <p class=\"tablenote\"><span  style=\"color: #dd1e31;\"><b>Important!</b></span> this field has been deprecated as of version 1.2.0, released on May 31, 2018. Any value other than <code>MONEY_BACK</code> will be treated as <code>MONEY_BACK</code> (although for a period of time, eBay will store and return the legacy values to preserve backwards compatibility).</p>  Indicates the method the seller uses to compensate the buyer for returned items. The return method specified applies only to <a href=\"http://developer.ebay.com/DevZone/guides/features-guide/default.html#Development/Post-Order-Returns.html#return-reasons\" target=\"_blank\">remorse returns</a>. <br><br>Note that each eBay marketplace can support different sets of refund methods. Also, each eBay marketplace has a default setting for this value and if you do not specifically set this value, sellers are obligated to honor the setting that displays in their listings. Call <b>GeteBayDetails</b> in the Trading API to see what refund methods the marketplaces you sell into support. <br><br>We recommend you set this field to the value of your preferred refund method and that you use the <b>description</b> field to detail the seller's return policy (such as indicating how quickly the seller will process a refund, whether the seller must receive the item before processing a refund, and other similar useful details). <br><br>You cannot modify this value in a Revise item call if (1) the listing has bids or (2) the listing ends within 12 hours. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/api:RefundMethodEnum'>eBay API documentation</a>  # noqa: E501

        :param refund_method: The refund_method of this ReturnPolicyRequest.  # noqa: E501
        :type: str
        """

        self._refund_method = refund_method

    @property
    def restocking_fee_percentage(self):
        """Gets the restocking_fee_percentage of this ReturnPolicyRequest.  # noqa: E501

        <p class=\"tablenote\"><span  style=\"color: #dd1e31;\"><b>Important!</b></span> This field has been deprecated as of version 1.2.0, released on May 31, 2018. Any value supplied in this field is ignored, it is neither read nor returned.</p>  <p>Sellers who accept returns should include this field if they charge buyers a restocking fee when items are returned. A restocking fee comes into play only when an item is returned due to buyer remorse and/or a purchasing mistake, but sellers cannot charge a restocking fee for SNAD-related returns. The total amount returned to the buyer is reduced by the cost of the item multiplied by the percentage indicated by this field. <p>Allowable restocking fee values are:</p> <ul><li><code>0.0</code>: No restocking fee is charged to the buyer</li><li><code>10.0</code>: 10 percent of the item price is charged to the buyer</li><li><code>15.0</code>: 15 percent of the item price is charged to the buyer</li> <li><code>20.0</code>: Up to 20 percent of the item price is charged to the buyer</li></ul>  # noqa: E501

        :return: The restocking_fee_percentage of this ReturnPolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._restocking_fee_percentage

    @restocking_fee_percentage.setter
    def restocking_fee_percentage(self, restocking_fee_percentage):
        """Sets the restocking_fee_percentage of this ReturnPolicyRequest.

        <p class=\"tablenote\"><span  style=\"color: #dd1e31;\"><b>Important!</b></span> This field has been deprecated as of version 1.2.0, released on May 31, 2018. Any value supplied in this field is ignored, it is neither read nor returned.</p>  <p>Sellers who accept returns should include this field if they charge buyers a restocking fee when items are returned. A restocking fee comes into play only when an item is returned due to buyer remorse and/or a purchasing mistake, but sellers cannot charge a restocking fee for SNAD-related returns. The total amount returned to the buyer is reduced by the cost of the item multiplied by the percentage indicated by this field. <p>Allowable restocking fee values are:</p> <ul><li><code>0.0</code>: No restocking fee is charged to the buyer</li><li><code>10.0</code>: 10 percent of the item price is charged to the buyer</li><li><code>15.0</code>: 15 percent of the item price is charged to the buyer</li> <li><code>20.0</code>: Up to 20 percent of the item price is charged to the buyer</li></ul>  # noqa: E501

        :param restocking_fee_percentage: The restocking_fee_percentage of this ReturnPolicyRequest.  # noqa: E501
        :type: str
        """

        self._restocking_fee_percentage = restocking_fee_percentage

    @property
    def return_instructions(self):
        """Gets the return_instructions of this ReturnPolicyRequest.  # noqa: E501

        <p class=\"tablenote\"><span  style=\"color: #dd1e31;\"><b>Important!</b></span> This field is being deprecated on many marketplaces. Once deprecated, this field will be ignored on marketplaces where it is not supported and it will neither be read nor returned.</p>  <p>This optional field contains the seller's detailed explanation for their return policy and is displayed in the Return Policy section of the View Item page. This field is valid in only the following marketplaces (the field is otherwise ignored):</p> <ul> <li>Germany (DE)</li> <li>Spain (ES)</li> <li>France (FR)</li> <li>Italy (IT)</li> </ul> Where valid, sellers can use this field to add details about their return policies. eBay uses this text string as-is in the Return Policy section of the View Item page. Avoid HTML and avoid character entity references (such as &amp;amp;pound; or &amp;amp;#163;). To include special characters in the return policy description, use the literal UTF-8 or ISO-8559-1 character (e.g. &amp;#163;).  <br><br><b>Max length</b>: 5000 (8000 for DE)  # noqa: E501

        :return: The return_instructions of this ReturnPolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._return_instructions

    @return_instructions.setter
    def return_instructions(self, return_instructions):
        """Sets the return_instructions of this ReturnPolicyRequest.

        <p class=\"tablenote\"><span  style=\"color: #dd1e31;\"><b>Important!</b></span> This field is being deprecated on many marketplaces. Once deprecated, this field will be ignored on marketplaces where it is not supported and it will neither be read nor returned.</p>  <p>This optional field contains the seller's detailed explanation for their return policy and is displayed in the Return Policy section of the View Item page. This field is valid in only the following marketplaces (the field is otherwise ignored):</p> <ul> <li>Germany (DE)</li> <li>Spain (ES)</li> <li>France (FR)</li> <li>Italy (IT)</li> </ul> Where valid, sellers can use this field to add details about their return policies. eBay uses this text string as-is in the Return Policy section of the View Item page. Avoid HTML and avoid character entity references (such as &amp;amp;pound; or &amp;amp;#163;). To include special characters in the return policy description, use the literal UTF-8 or ISO-8559-1 character (e.g. &amp;#163;).  <br><br><b>Max length</b>: 5000 (8000 for DE)  # noqa: E501

        :param return_instructions: The return_instructions of this ReturnPolicyRequest.  # noqa: E501
        :type: str
        """

        self._return_instructions = return_instructions

    @property
    def return_method(self):
        """Gets the return_method of this ReturnPolicyRequest.  # noqa: E501

        Valid in the US marketplace only, this optional field indicates additional services (other than money-back) that sellers can offer buyers for <a href=\"http://developer.ebay.com/DevZone/guides/features-guide/default.html#Development/Post-Order-Returns.html#return-reasons\" target=\"_blank\">remorse returns</a>.  <br><br>As of version 1.2.0, the only accepted value for this field is <code>REPLACEMENT</code>. This field is valid in only the US marketplace, any supplied value is ignored in other marketplaces. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/api:ReturnMethodEnum'>eBay API documentation</a>  # noqa: E501

        :return: The return_method of this ReturnPolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._return_method

    @return_method.setter
    def return_method(self, return_method):
        """Sets the return_method of this ReturnPolicyRequest.

        Valid in the US marketplace only, this optional field indicates additional services (other than money-back) that sellers can offer buyers for <a href=\"http://developer.ebay.com/DevZone/guides/features-guide/default.html#Development/Post-Order-Returns.html#return-reasons\" target=\"_blank\">remorse returns</a>.  <br><br>As of version 1.2.0, the only accepted value for this field is <code>REPLACEMENT</code>. This field is valid in only the US marketplace, any supplied value is ignored in other marketplaces. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/api:ReturnMethodEnum'>eBay API documentation</a>  # noqa: E501

        :param return_method: The return_method of this ReturnPolicyRequest.  # noqa: E501
        :type: str
        """

        self._return_method = return_method

    @property
    def return_period(self):
        """Gets the return_period of this ReturnPolicyRequest.  # noqa: E501


        :return: The return_period of this ReturnPolicyRequest.  # noqa: E501
        :rtype: TimeDuration
        """
        return self._return_period

    @return_period.setter
    def return_period(self, return_period):
        """Sets the return_period of this ReturnPolicyRequest.


        :param return_period: The return_period of this ReturnPolicyRequest.  # noqa: E501
        :type: TimeDuration
        """

        self._return_period = return_period

    @property
    def return_shipping_cost_payer(self):
        """Gets the return_shipping_cost_payer of this ReturnPolicyRequest.  # noqa: E501

        This field indicates who is responsible for paying for the shipping charges for returned items. The field can be set to either <code>BUYER</code> or <code>SELLER</code>.  <br><br>Depending on the return policy and specifics of the return, either the buyer or the seller can be responsible for the return shipping costs. Note that the seller is always responsible for return shipping costs for SNAD-related issues.  <br><br><i>Required if </i> <b>returnsAccepted</b> is set to <code>true</code>. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/api:ReturnShippingCostPayerEnum'>eBay API documentation</a>  # noqa: E501

        :return: The return_shipping_cost_payer of this ReturnPolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._return_shipping_cost_payer

    @return_shipping_cost_payer.setter
    def return_shipping_cost_payer(self, return_shipping_cost_payer):
        """Sets the return_shipping_cost_payer of this ReturnPolicyRequest.

        This field indicates who is responsible for paying for the shipping charges for returned items. The field can be set to either <code>BUYER</code> or <code>SELLER</code>.  <br><br>Depending on the return policy and specifics of the return, either the buyer or the seller can be responsible for the return shipping costs. Note that the seller is always responsible for return shipping costs for SNAD-related issues.  <br><br><i>Required if </i> <b>returnsAccepted</b> is set to <code>true</code>. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/api:ReturnShippingCostPayerEnum'>eBay API documentation</a>  # noqa: E501

        :param return_shipping_cost_payer: The return_shipping_cost_payer of this ReturnPolicyRequest.  # noqa: E501
        :type: str
        """

        self._return_shipping_cost_payer = return_shipping_cost_payer

    @property
    def returns_accepted(self):
        """Gets the returns_accepted of this ReturnPolicyRequest.  # noqa: E501

        If set to <code>true</code>, the seller accepts returns. <p>Call the <b>getReturnPolicies</b> in the Metadata API to see what categories require returns to be offered for listings in each category. Also, note that some European marketplaces (for example, UK, IE, and DE) require sellers to accept returns for fixed-price items and auctions listed with Buy It Now. For details, see <a href=\"http://pages.ebay.co.uk/help/policies/user-agreement.html#returns\">Returns and the Law (UK)</a>.</p>  <p><span class=\"tablenote\"><strong>Note:</strong>Top-Rated sellers must accept item returns and the <b>handlingTime</b> should be set to zero days or one day for a listing to receive a Top-Rated Plus badge on the View Item or search result pages. For more information on eBay's Top-Rated seller program, see <a href=\"http://pages.ebay.com/help/sell/top-rated.html\">Becoming a Top Rated Seller and qualifying for Top Rated Plus benefits</a>.</span></p>  # noqa: E501

        :return: The returns_accepted of this ReturnPolicyRequest.  # noqa: E501
        :rtype: bool
        """
        return self._returns_accepted

    @returns_accepted.setter
    def returns_accepted(self, returns_accepted):
        """Sets the returns_accepted of this ReturnPolicyRequest.

        If set to <code>true</code>, the seller accepts returns. <p>Call the <b>getReturnPolicies</b> in the Metadata API to see what categories require returns to be offered for listings in each category. Also, note that some European marketplaces (for example, UK, IE, and DE) require sellers to accept returns for fixed-price items and auctions listed with Buy It Now. For details, see <a href=\"http://pages.ebay.co.uk/help/policies/user-agreement.html#returns\">Returns and the Law (UK)</a>.</p>  <p><span class=\"tablenote\"><strong>Note:</strong>Top-Rated sellers must accept item returns and the <b>handlingTime</b> should be set to zero days or one day for a listing to receive a Top-Rated Plus badge on the View Item or search result pages. For more information on eBay's Top-Rated seller program, see <a href=\"http://pages.ebay.com/help/sell/top-rated.html\">Becoming a Top Rated Seller and qualifying for Top Rated Plus benefits</a>.</span></p>  # noqa: E501

        :param returns_accepted: The returns_accepted of this ReturnPolicyRequest.  # noqa: E501
        :type: bool
        """

        self._returns_accepted = returns_accepted

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
        if issubclass(ReturnPolicyRequest, dict):
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
        if not isinstance(other, ReturnPolicyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
