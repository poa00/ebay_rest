# coding: utf-8

"""
    Account API

    The <b>Account API</b> gives sellers the ability to configure their eBay seller accounts, including the seller's policies (seller-defined custom policies and eBay business policies), opt in and out of eBay seller programs, configure sales tax tables, and get account information.  <br><br>For details on the availability of the methods in this API, see <a href=\"/api-docs/sell/account/overview.html#requirements\">Account API requirements and restrictions</a>.  # noqa: E501

    OpenAPI spec version: v1.7.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SetPaymentPolicyResponse(object):
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
        'deposit': 'Deposit',
        'description': 'str',
        'full_payment_due_in': 'TimeDuration',
        'immediate_pay': 'bool',
        'marketplace_id': 'str',
        'name': 'str',
        'payment_instructions': 'str',
        'payment_methods': 'list[PaymentMethod]',
        'payment_policy_id': 'str',
        'warnings': 'list[Error]'
    }

    attribute_map = {
        'category_types': 'categoryTypes',
        'deposit': 'deposit',
        'description': 'description',
        'full_payment_due_in': 'fullPaymentDueIn',
        'immediate_pay': 'immediatePay',
        'marketplace_id': 'marketplaceId',
        'name': 'name',
        'payment_instructions': 'paymentInstructions',
        'payment_methods': 'paymentMethods',
        'payment_policy_id': 'paymentPolicyId',
        'warnings': 'warnings'
    }

    def __init__(self, category_types=None, deposit=None, description=None, full_payment_due_in=None, immediate_pay=None, marketplace_id=None, name=None, payment_instructions=None, payment_methods=None, payment_policy_id=None, warnings=None):  # noqa: E501
        """SetPaymentPolicyResponse - a model defined in Swagger"""  # noqa: E501
        self._category_types = None
        self._deposit = None
        self._description = None
        self._full_payment_due_in = None
        self._immediate_pay = None
        self._marketplace_id = None
        self._name = None
        self._payment_instructions = None
        self._payment_methods = None
        self._payment_policy_id = None
        self._warnings = None
        self.discriminator = None
        if category_types is not None:
            self.category_types = category_types
        if deposit is not None:
            self.deposit = deposit
        if description is not None:
            self.description = description
        if full_payment_due_in is not None:
            self.full_payment_due_in = full_payment_due_in
        if immediate_pay is not None:
            self.immediate_pay = immediate_pay
        if marketplace_id is not None:
            self.marketplace_id = marketplace_id
        if name is not None:
            self.name = name
        if payment_instructions is not None:
            self.payment_instructions = payment_instructions
        if payment_methods is not None:
            self.payment_methods = payment_methods
        if payment_policy_id is not None:
            self.payment_policy_id = payment_policy_id
        if warnings is not None:
            self.warnings = warnings

    @property
    def category_types(self):
        """Gets the category_types of this SetPaymentPolicyResponse.  # noqa: E501

        The <b>CategoryTypeEnum</b> value to which this policy applies. This container is used to discern accounts that sell motor vehicles from those that do not.<br /><br /><b>Restriction:</b> Currently, each policy can be set to only one <b>categoryTypes</b> value at a time.  # noqa: E501

        :return: The category_types of this SetPaymentPolicyResponse.  # noqa: E501
        :rtype: list[CategoryType]
        """
        return self._category_types

    @category_types.setter
    def category_types(self, category_types):
        """Sets the category_types of this SetPaymentPolicyResponse.

        The <b>CategoryTypeEnum</b> value to which this policy applies. This container is used to discern accounts that sell motor vehicles from those that do not.<br /><br /><b>Restriction:</b> Currently, each policy can be set to only one <b>categoryTypes</b> value at a time.  # noqa: E501

        :param category_types: The category_types of this SetPaymentPolicyResponse.  # noqa: E501
        :type: list[CategoryType]
        """

        self._category_types = category_types

    @property
    def deposit(self):
        """Gets the deposit of this SetPaymentPolicyResponse.  # noqa: E501


        :return: The deposit of this SetPaymentPolicyResponse.  # noqa: E501
        :rtype: Deposit
        """
        return self._deposit

    @deposit.setter
    def deposit(self, deposit):
        """Sets the deposit of this SetPaymentPolicyResponse.


        :param deposit: The deposit of this SetPaymentPolicyResponse.  # noqa: E501
        :type: Deposit
        """

        self._deposit = deposit

    @property
    def description(self):
        """Gets the description of this SetPaymentPolicyResponse.  # noqa: E501

        An optional seller-defined description of the payment policy.  # noqa: E501

        :return: The description of this SetPaymentPolicyResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SetPaymentPolicyResponse.

        An optional seller-defined description of the payment policy.  # noqa: E501

        :param description: The description of this SetPaymentPolicyResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def full_payment_due_in(self):
        """Gets the full_payment_due_in of this SetPaymentPolicyResponse.  # noqa: E501


        :return: The full_payment_due_in of this SetPaymentPolicyResponse.  # noqa: E501
        :rtype: TimeDuration
        """
        return self._full_payment_due_in

    @full_payment_due_in.setter
    def full_payment_due_in(self, full_payment_due_in):
        """Sets the full_payment_due_in of this SetPaymentPolicyResponse.


        :param full_payment_due_in: The full_payment_due_in of this SetPaymentPolicyResponse.  # noqa: E501
        :type: TimeDuration
        """

        self._full_payment_due_in = full_payment_due_in

    @property
    def immediate_pay(self):
        """Gets the immediate_pay of this SetPaymentPolicyResponse.  # noqa: E501

        If set to <code>true</code>,  payment is due upon receipt (eBay generates a receipt when the buyer agrees to purchase an item). The items will be available for other buyers until the payment is complete.<br /><br />This boolean must be set in the payment policy if the seller wants to create a listing that has an <i>immediate payment</i> requirement. <p class=\"tablenote\"><b>Note:</b> This container can be used for sellers who opt-in to the <a href=\"/managed-payments\" title=\"eBay Developers Program page\" target=\"_blank\">managed payments</a> program, but some requirements do not apply.</p><b>Default:</b> False  # noqa: E501

        :return: The immediate_pay of this SetPaymentPolicyResponse.  # noqa: E501
        :rtype: bool
        """
        return self._immediate_pay

    @immediate_pay.setter
    def immediate_pay(self, immediate_pay):
        """Sets the immediate_pay of this SetPaymentPolicyResponse.

        If set to <code>true</code>,  payment is due upon receipt (eBay generates a receipt when the buyer agrees to purchase an item). The items will be available for other buyers until the payment is complete.<br /><br />This boolean must be set in the payment policy if the seller wants to create a listing that has an <i>immediate payment</i> requirement. <p class=\"tablenote\"><b>Note:</b> This container can be used for sellers who opt-in to the <a href=\"/managed-payments\" title=\"eBay Developers Program page\" target=\"_blank\">managed payments</a> program, but some requirements do not apply.</p><b>Default:</b> False  # noqa: E501

        :param immediate_pay: The immediate_pay of this SetPaymentPolicyResponse.  # noqa: E501
        :type: bool
        """

        self._immediate_pay = immediate_pay

    @property
    def marketplace_id(self):
        """Gets the marketplace_id of this SetPaymentPolicyResponse.  # noqa: E501

        The ID of the eBay marketplace to which this payment policy applies. If this value is not specified, the value defaults to the seller's eBay registration site. <p class=\"tablenote\"><b>Note:</b> A limited number of sellers, on a limited number of eBay marketplaces, are currently opted-in to the eBay managed payments program. To view the eBay marketplaces where managed payments are currently supported, see the <a href=\"/managed-payments\" title=\"eBay Developers Program page\" target=\"_blank\">managed payments</a> landing page.</p> For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/ba:MarketplaceIdEnum'>eBay API documentation</a>  # noqa: E501

        :return: The marketplace_id of this SetPaymentPolicyResponse.  # noqa: E501
        :rtype: str
        """
        return self._marketplace_id

    @marketplace_id.setter
    def marketplace_id(self, marketplace_id):
        """Sets the marketplace_id of this SetPaymentPolicyResponse.

        The ID of the eBay marketplace to which this payment policy applies. If this value is not specified, the value defaults to the seller's eBay registration site. <p class=\"tablenote\"><b>Note:</b> A limited number of sellers, on a limited number of eBay marketplaces, are currently opted-in to the eBay managed payments program. To view the eBay marketplaces where managed payments are currently supported, see the <a href=\"/managed-payments\" title=\"eBay Developers Program page\" target=\"_blank\">managed payments</a> landing page.</p> For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/ba:MarketplaceIdEnum'>eBay API documentation</a>  # noqa: E501

        :param marketplace_id: The marketplace_id of this SetPaymentPolicyResponse.  # noqa: E501
        :type: str
        """

        self._marketplace_id = marketplace_id

    @property
    def name(self):
        """Gets the name of this SetPaymentPolicyResponse.  # noqa: E501

        A user-defined name for this payment policy. Names must be unique for policies assigned to the same marketplace. <p class=\"tablenote\"><b>Note</b>: eBay will create a new payment policy for sellers who opt-in to the <a href=\"/managed-payments\" title=\"eBay Developers Program page\" target=\"_blank\">managed payments</a> program.</p><b>Max length:</b> 64  # noqa: E501

        :return: The name of this SetPaymentPolicyResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SetPaymentPolicyResponse.

        A user-defined name for this payment policy. Names must be unique for policies assigned to the same marketplace. <p class=\"tablenote\"><b>Note</b>: eBay will create a new payment policy for sellers who opt-in to the <a href=\"/managed-payments\" title=\"eBay Developers Program page\" target=\"_blank\">managed payments</a> program.</p><b>Max length:</b> 64  # noqa: E501

        :param name: The name of this SetPaymentPolicyResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def payment_instructions(self):
        """Gets the payment_instructions of this SetPaymentPolicyResponse.  # noqa: E501

        <p class=\"tablenote\"><b>Note:</b> NO LONGER SUPPORTED. Although this field may be returned for some older payment business policies, payment instructions are no longer supported by payment business policies. If this field is returned, it can be ignored and these payment instructions will not appear in any listings that use the corresponding business policy.</p>A free-form string field that allows sellers to add detailed payment instructions to their listings. The payment instructions appear on eBay's View Item and Checkout pages. <br><br>eBay recommends sellers use this field to clarify payment policies for motor vehicle listings on eBay Motors. For example, sellers can include the specifics on the deposit (if required), pickup/delivery arrangements, and full payment details on the vehicle. <br><br>The field allows only 500 characters as input, but due to the way the eBay web site UI treats characters, this field can return more than 500 characters in the response. For example, characters like & and ' (ampersand and single quote) count as 5 characters each. <br /><br /><b>Restriction:</b> This container is not supported for sellers who opt-in to the <a href=\"/managed-payments\" title=\"eBay Developers Program page\" target=\"_blank\">managed payments</a> program.  <br><br><b>Max length:</b> 1000  # noqa: E501

        :return: The payment_instructions of this SetPaymentPolicyResponse.  # noqa: E501
        :rtype: str
        """
        return self._payment_instructions

    @payment_instructions.setter
    def payment_instructions(self, payment_instructions):
        """Sets the payment_instructions of this SetPaymentPolicyResponse.

        <p class=\"tablenote\"><b>Note:</b> NO LONGER SUPPORTED. Although this field may be returned for some older payment business policies, payment instructions are no longer supported by payment business policies. If this field is returned, it can be ignored and these payment instructions will not appear in any listings that use the corresponding business policy.</p>A free-form string field that allows sellers to add detailed payment instructions to their listings. The payment instructions appear on eBay's View Item and Checkout pages. <br><br>eBay recommends sellers use this field to clarify payment policies for motor vehicle listings on eBay Motors. For example, sellers can include the specifics on the deposit (if required), pickup/delivery arrangements, and full payment details on the vehicle. <br><br>The field allows only 500 characters as input, but due to the way the eBay web site UI treats characters, this field can return more than 500 characters in the response. For example, characters like & and ' (ampersand and single quote) count as 5 characters each. <br /><br /><b>Restriction:</b> This container is not supported for sellers who opt-in to the <a href=\"/managed-payments\" title=\"eBay Developers Program page\" target=\"_blank\">managed payments</a> program.  <br><br><b>Max length:</b> 1000  # noqa: E501

        :param payment_instructions: The payment_instructions of this SetPaymentPolicyResponse.  # noqa: E501
        :type: str
        """

        self._payment_instructions = payment_instructions

    @property
    def payment_methods(self):
        """Gets the payment_methods of this SetPaymentPolicyResponse.  # noqa: E501

        If the seller is not opted-in to managed payments, this container returns a list of the payment methods accepted by the seller.  <br><br>When not opted-in to managed payments, each payment policy must specify at least one payment method. <p class=\"tablenote\"><b>Note:</b> The <b>paymentMethods</b> container is not returned if the seller is opted-in to the <a href=\"https://pages.ebay.com/seller-center/service-and-payments/managed-payments-on-ebay.html\" title=\"eBay Seller Center page\" target=\"_blank\">managed payments</a> program.</p>  # noqa: E501

        :return: The payment_methods of this SetPaymentPolicyResponse.  # noqa: E501
        :rtype: list[PaymentMethod]
        """
        return self._payment_methods

    @payment_methods.setter
    def payment_methods(self, payment_methods):
        """Sets the payment_methods of this SetPaymentPolicyResponse.

        If the seller is not opted-in to managed payments, this container returns a list of the payment methods accepted by the seller.  <br><br>When not opted-in to managed payments, each payment policy must specify at least one payment method. <p class=\"tablenote\"><b>Note:</b> The <b>paymentMethods</b> container is not returned if the seller is opted-in to the <a href=\"https://pages.ebay.com/seller-center/service-and-payments/managed-payments-on-ebay.html\" title=\"eBay Seller Center page\" target=\"_blank\">managed payments</a> program.</p>  # noqa: E501

        :param payment_methods: The payment_methods of this SetPaymentPolicyResponse.  # noqa: E501
        :type: list[PaymentMethod]
        """

        self._payment_methods = payment_methods

    @property
    def payment_policy_id(self):
        """Gets the payment_policy_id of this SetPaymentPolicyResponse.  # noqa: E501

        A unique eBay-assigned ID for a payment policy. This ID is generated when the policy is created.  # noqa: E501

        :return: The payment_policy_id of this SetPaymentPolicyResponse.  # noqa: E501
        :rtype: str
        """
        return self._payment_policy_id

    @payment_policy_id.setter
    def payment_policy_id(self, payment_policy_id):
        """Sets the payment_policy_id of this SetPaymentPolicyResponse.

        A unique eBay-assigned ID for a payment policy. This ID is generated when the policy is created.  # noqa: E501

        :param payment_policy_id: The payment_policy_id of this SetPaymentPolicyResponse.  # noqa: E501
        :type: str
        """

        self._payment_policy_id = payment_policy_id

    @property
    def warnings(self):
        """Gets the warnings of this SetPaymentPolicyResponse.  # noqa: E501

        A list of warnings related to request. This field normally returns empty, which indicates the request did not generate any warnings.  # noqa: E501

        :return: The warnings of this SetPaymentPolicyResponse.  # noqa: E501
        :rtype: list[Error]
        """
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        """Sets the warnings of this SetPaymentPolicyResponse.

        A list of warnings related to request. This field normally returns empty, which indicates the request did not generate any warnings.  # noqa: E501

        :param warnings: The warnings of this SetPaymentPolicyResponse.  # noqa: E501
        :type: list[Error]
        """

        self._warnings = warnings

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
        if issubclass(SetPaymentPolicyResponse, dict):
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
        if not isinstance(other, SetPaymentPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
